---
type: optimization_recipe
hardware_targets:
  - XuanTie C908
  - XuanTie C930
  - XuanTie C950
workloads:
  - GEMM (INT8→INT32)
  - GEMM (FP16→FP16)
  - FullyConnected (INT8)
  - Convolution 1×1 (INT8)
datatypes:
  - INT8
  - FP16
metrics:
  - throughput (ops/cycle)
  - requantization overhead
toolchains:
  - XuanTie GNU Toolchain (riscv-matrix-extension-spec)
  - SHL / CSI-NN2 (XUANTIE-RV/csi-nn2)
tags:
  - RISC-V
  - AME
  - T-Head
  - XuanTie
  - matrix extension
  - GEMM
  - INT8
  - SHL
sources:
  - https://github.com/XUANTIE-RV/csi-nn2/tree/master/source/thead_matrix
  - https://github.com/XUANTIE-RV/riscv-matrix-extension-spec/blob/master/doc/intrinsic/rvm-intrinsic-api.adoc
created: 2026-06-29
updated: 2026-06-29
cold_start: false
inbound_links: 0
scorecard:
  novelty_delta: 0.95
  claim_density: 0.9
  self_containedness: 0.9
  bridge_score: 0.9
  hub_potential: 0.85
---

# SHL AME GEMM Optimization Recipe

SHL (Structure of Heterogeneous Library, formerly CSI-NN2) provides hand-written assembly and C-intrinsic GEMM kernels targeting the XuanTie AME (Advanced Matrix Engine) via the `thead_matrix` backend. The INT8→INT32 path achieves full AME utilization through a 2-row-by-N-column tiling scheme, separating zero-point compensation (3 extra `mmaqa` calls) from the main accumulation loop, and using `mzero`+`mdup` to pre-initialize accumulators from bias and zero-point products. The FP16 path mirrors the same structure using `mld_f16` loads. The recipe is grounded in the open-source SHL codebase (`XUANTIE-RV/csi-nn2`).

## Transformation

### Prerequisites
- Hardware: RISC-V core implementing XuanTie AME (C908, C930, C950) with `mmi8i32` and `mmf16f16` misa bits set.
- Toolchain: XuanTie GNU toolchain with matrix extension support (`-march=rv64gcvxtheadmatmul` or equivalent).
- SHL/CSI-NN2 compiled with `MATRIX_PW_I32` define for INT8 path; weight tensor pre-packed to `[N/msize_n, K/msize_k, msize_n, msize_k]` layout.
- K dimension must satisfy `K % mlenb == 0` (mlenb = `csrr_xrlenb()` bytes = TRLEN/8) for the no-tail path.

### Tile Dimension Query
```c
int mcols = csrr_xrlenb();   // TRLEN/8 — bytes per tile row
int mrows = mcols / 4;        // INT32 elements per row → tile height for INT8
```
For a typical TLEN=512 implementation: TRLEN=64 bytes → mrows=16 (INT8 tile is 16×16).

### Core INT8 Tiling Loop (C intrinsics)
```c
// Outer loops: i over M in steps of mrows, j over N in steps of mrows
mcfgn(msize_n);                              // set N tile dimension
mcfgk(msize_n * sizeof(int32_t));            // set K for bias/zp init phase
mcfgm(msize_m);

// Initialize accumulators from bias + zero-point cross-products
mint32_t acc  = mzero_mi32();               // main accumulator
mint32_t z1q2 = mzero_mi32();               // z1 * q2 correction
mint32_t q1z2 = mzero_mi32();               // q1 * z2 correction
mint32_t z1z2 = mdup_m_x(z1 * z2 * K);     // z1*z2*K scalar broadcast

mcfgk(mcols * sizeof(int8_t));              // set K for matrix multiply phase
mint8_t m_z1  = mdup_m_x(z1_i8);           // broadcast input zero point
mint8_t m_z2  = mdup_m_x(z2_i8);           // broadcast weight zero point

// Inner K loop
for (int c = 0; c < K; c += msize_k) {
    mcfgk(msize_k * sizeof(int8_t));
    mint8_t m0 = mld_i8(a_ptr, stride_a);   // load A tile (msize_m × msize_k)
    mcfgm(msize_n);
    mint8_t m2 = msld_i8(b_ptr, msize_k);   // load B tile (msize_n × msize_k), stride-loaded
    mcfgm(msize_m);
    acc  = mmaqa(acc,  m2, m0);             // q1 * q2 accumulation
    z1q2 = mmaqa(z1q2, m2, m_z1);          // z1 * q2
    q1z2 = mmaqa(q1z2, m_z2, m0);          // q1 * z2
}

// Zero-point compensation
mcfgk(msize_n * sizeof(int32_t));
acc = msub_mi32(acc, z1q2);                 // - z1*q2
acc = msub_mi32(acc, q1z2);                 // - q1*z2
acc = madd_mi32(acc, z1z2);                 // + z1*z2*K

// Requantize INT32 → INT8 (per-channel multiply-shift)
// ... (RVV-based requantize using vfmacc/vcvt; AME not used for this step)
msst_i8_mi8(c_ptr, stride_c, result);       // store output
```

### Assembly Kernel (2-row × N variant, `gemm_int8_nhwc_matrix.S`)
The assembly path processes 2 rows of A simultaneously using registers m0–m7:
- `m0`, `m1`: input A tiles for row 0 and row 1
- `m4`, `m5`: accumulators for (row0 × weight) and (row0 × bias)
- `m6`, `m7`: accumulators for (row1 × weight) and (row1 × bias)
- `mcfgmi`, `mcfgm`, `mcfgk`, `mcfgn`: configure tile dimensions per kernel variant
- `mldb`: load B (weight) tile; `mmov.mv.i`: move accumulator row

### Key Intrinsic Names (C API)
```c
// Configuration
mcfgm(m);   mcfgk(k_bytes);   mcfgn(n);    // set tile dimensions

// Initialize
mint32_t acc = mzero_mi32();               // zero accumulator → mzero inst
mint8_t  bcast = mdup_m_x(val);            // broadcast scalar → mdup inst

// Load
mint8_t ma = mld_i8(ptr, row_stride);      // load A tile → mlae8
mint8_t mb = msld_i8(ptr, k_stride);       // load B tile (stride) → mlbe8
mfloat16_t mf = mld_f16(ptr, stride);      // FP16 load → mlae16

// Compute
mint32_t out = mmaqa(acc, mb, ma);         // INT8 signed MAC → mmaqa.b asm
mint32_t out = mmaqau(acc, mb, ma);        // UINT8 MAC
mint32_t out = mmaqaus(acc, mb, ma);       // unsigned×signed
mint32_t out = mmaqasu(acc, mb, ma);       // signed×unsigned

// Store
msst_i8_mi8(ptr, stride, result);          // store INT8 output
```

### Convolution 1×1 Mapping
`convolution_1x1_int8_matrix.c` and `convolution_1x1_fp16_matrix.c` use the same tile loop. The 1×1 conv maps directly: input HW spatial positions → M dimension, output channels → N, input channels → K. No im2col required.

## Expected Effect
- Full AME tile utilization when M, N ≥ mrows and K ≥ mcols (mlenb). The 2-row-by-N assembly kernel doubles effective M-tile throughput for small-batch inference.
- Three extra `mmaqa` calls per K-tile for zero-point compensation add ~20% overhead vs. symmetric INT8 — this is the cost of asymmetric quantization.
- Requantization (INT32→INT8 per-output-channel) uses RVV, not AME; it is bandwidth-bound and runs in parallel with the next A-tile load.

## Failure Modes
- `K % mlenb != 0`: the assembly kernel has no tail handling; C intrinsic path handles K-tail via `mcfgk(k_tail)`.
- AME tile dimension exceeds hardware TMMAX/TKMAX/TNMAX: raises illegal instruction; query via `misa` CSR before dispatch.
- Weight pre-packing to `[N_tiles, K_tiles, msize_n, msize_k]` layout is required; unpacked weights cause strided loads with poor cache behavior.

## Relationships

- [[XuanTie_AME_ISA]] — the underlying ISA: mmaqa assembly mnemonic, tile register model, misa capability bits.
- [[SHL_Library]] — SHL is the library providing this backend; AME path is in `source/thead_matrix/`.
- [[XuanTie_C908]] — primary target hardware; AIoT chip with AME.
- [[XuanTie_C930]] — server-class target; 512-bit RVV + AME.
- [[XuanTie_C950]] — latest generation (5nm, 3.2 GHz, announced 2026-03), integrates AI acceleration engine.
- [[TVM_CSINN2_Integration_Optimization_Recipe]] — TVM BYOC path to SHL; uses same CSI-NN2 operators but wraps them via Relay.
- [[Kernel_Dispatch_Decision_Tree_RVV_AME]] — dispatch logic: AME for compute-bound GEMM; RVV for bandwidth-bound GEMV.

## Sources

- SHL AME INT8 GEMM C kernel: `XUANTIE-RV/csi-nn2/source/thead_matrix/matmul_int8.c`
- SHL AME INT8 GEMM assembly kernel: `XUANTIE-RV/csi-nn2/source/thead_matrix/gemm_int8_nhwc_matrix.S`
- SHL AME FP16 FullyConnected: `XUANTIE-RV/csi-nn2/source/thead_matrix/fullyconnected_fp16.c`
- RVM C intrinsic API: `XUANTIE-RV/riscv-matrix-extension-spec/doc/intrinsic/rvm-intrinsic-api.adoc`
