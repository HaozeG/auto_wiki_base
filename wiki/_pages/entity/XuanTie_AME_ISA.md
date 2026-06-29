---
type: entity
tags:
  - RISC-V
  - matrix extension
  - T-Head
  - XuanTie
  - AME
  - ISA
  - GEMM
  - AI accelerator
sources:
  - https://github.com/XUANTIE-RV/riscv-matrix-extension-spec/
created: 2026-06-29
updated: 2026-06-29
cold_start: false
inbound_links: 0
scorecard:
  novelty_delta: 0.95
  claim_density: 0.95
  self_containedness: 0.95
  bridge_score: 0.9
  hub_potential: 0.85
---

# XuanTie AME ISA (RISC-V Matrix Extension v0.6.0)

The XuanTie Advanced Matrix Engine (AME) is T-Head Semiconductor's implementation of the RISC-V Matrix Extension (RVM) v0.6.0, published as an open-source specification at `XUANTIE-RV/riscv-matrix-extension-spec`. It extends the RISC-V ISA with 8 dedicated matrix registers (4 tile + 4 accumulation), a set of tile-configuration CSRs, and a full instruction set covering matrix multiplication (integer and float), element-wise operations, and transposed/non-transposed load/store. The extension is designed to complement RVV 1.0 — it handles the compute-bound GEMM core while RVV handles reduction, activation, and bandwidth-bound operations. The compulsory hardware baseline requires `mmi8i32` (INT8→INT32), `mmf16f16` (FP16), `mmf16f32` (FP16→FP32), `mmbf16f32` (BF16→FP32), `mmf8f16`, `mmf8bf16`, and `mmf8f32` (FP8 variants).

## Key Claims

- **Register file**: 4 Tile Registers (tr0–tr3) for source operands, 4 Accumulation Registers (acc0–acc3) for output. Tile registers have TLEN bits total with TRLEN bits per row (TLEN/TRLEN rows). Accumulation registers have ALEN bits with ARLEN = (TLEN/TRLEN) × ELEN bits per row — wider than tile rows to hold widened products.
- **Tile shape flexibility**: TRLEN is software-configurable via `msettile{m|k|n}[i]` instructions. For TLEN=512, ELEN=32: TRLEN can be 32 (16×1 outer product) through 512 (1×16 inner product). INT8 at TRLEN=64 gives 8×8 tiles; FP16 at TRLEN=128 gives 4×8 tiles. Full range from pure outer product to pure inner product.
- **Core multiply-accumulate**: `mmacc.w.b md, ms2, ms1` — INT8→INT32 quad-widen GEMM accumulate: `acc[md] += tr[ms1] × tr[ms2]`. The operation is `C = A × BT` (B is pre-transposed in the register layout). Variants: `mmaccu` (unsigned), `mmaccsu` (signed×unsigned), `mmaccus` (unsigned×signed).
- **Float matrix multiply**: `mfmacc.h` (FP16→FP16), `mfmacc.s` (FP32→FP32), `mfmacc.s.h` (FP16→FP32), `mfmacc.s.bf16` (BF16→FP32), `mfmacc.h.e4/e5` (FP8→FP16), `mfmacc.s.e4/e5` (FP8→FP32). FP8 variants cover both E4M3 and E5M2 formats. Reduction is unordered-sum; rounding after accumulation.
- **Tile configuration CSRs**: `mtilem`, `mtilek`, `mtilen` (read-only, written only by `msettile*` instructions). `xmcsr` aggregates: `xmxrm` (fixed-point rounding, 2 bits), `xmsat` (saturation flag), `xmfflags` (FP exception flags, 5 bits), `xmfrm` (FP rounding mode, 3 bits), `xmsaten` (saturation enable).
- **misa register**: Hardware capability flags — `mmi8i32` (compulsory), `mmf16f16` (compulsory), `mmf16f32` (compulsory), `mmbf16f32` (compulsory), `mmf8f16/bf16/f32` (compulsory), `mmf32f32` (optional), `mmf64f64` (optional), `mmi4i32` (optional, INT4 oct-widen), `miew`/`mfew` (element-wise integer/FP extension, optional).
- **Load/store instructions**: Separate load/store for A (`mlae8/16/32/64`, `msae*`), B (`mlbe*`, `msbe*`), and C (`mlce*`, `msce*`) tiles. Each set has non-transposed and transposed variants (`mlate*`, `mlbte*`, `mlcte*`). A tile loaded as `mtilem × mtilek`; B tile as `mtilen × mtilek`; C tile as `mtilem × mtilen`. Base address in rs1; row byte stride in rs2.
- **Context management**: 2-bit MS field in mstatus/sstatus (Off/Initial/Clean/Dirty), analogous to RVV VS field. Illegal instruction exception when MS=Off.
- **Toolchain support**: GNU toolchain (binutils + gcc), QEMU emulator with matrix extension, SHL 2.0 neural network library using AME kernels, HHB deployment toolkit. Demo applications: ResNet-50 evaluation, GEMM benchmark. Repository last pushed 2026-04-01.
- **INT4 (optional)**: `mmacc.w.hb` (INT4→INT32 oct-widen) is listed as optional in `misa.mmi4i32`; present in commented-out sections of the spec, not yet in the main instruction table.

## Instruction Summary

```
# Tile configuration
msettilemi imm | msettilem rs1    # set mtilem
msettileki imm | msettilek rs1    # set mtilek  
msettileni imm | msettilen rs1    # set mtilen

# Integer matrix multiply-accumulate (acc = acc + A × B)
mmacc.w.b   md, ms2, ms1          # INT8 signed × signed → INT32
mmaccu.w.b  md, ms2, ms1          # UINT8 × UINT8 → INT32
mmaccsu.w.b md, ms2, ms1          # INT8 signed × unsigned → INT32
mmaccus.w.b md, ms2, ms1          # INT8 unsigned × signed → INT32

# Float matrix multiply-accumulate
mfmacc.h        md, ms2, ms1      # FP16 → FP16
mfmacc.s        md, ms2, ms1      # FP32 → FP32
mfmacc.s.h      md, ms2, ms1      # FP16 → FP32
mfmacc.s.bf16   md, ms2, ms1      # BF16 → FP32
mfmacc.h.e4/e5  md, ms2, ms1      # FP8(E4M3/E5M2) → FP16
mfmacc.s.e4/e5  md, ms2, ms1      # FP8(E4M3/E5M2) → FP32

# Load A tile (mtilem × mtilek)
mlae8/16/32/64  md, (rs1), rs2    # non-transposed
mlate8/16/32/64 md, (rs1), rs2    # transposed (column-major input)

# Load B tile (mtilen × mtilek)
mlbe8/16/32/64  md, (rs1), rs2
mlbte8/16/32/64 md, (rs1), rs2

# Load/store C tile (mtilem × mtilen)
mlce8/16/32/64  md, (rs1), rs2
msce8/16/32/64  ms3, (rs1), rs2
```

## C Intrinsic API Names

The XuanTie GNU toolchain uses overloaded C intrinsics prefixed `__riscv_th_` (short aliases without prefix also available in SHL):

| Assembly mnemonic | C intrinsic | Description |
|-------------------|-------------|-------------|
| `mmaqa.b` | `__riscv_th_mmaqa` / `mmaqa()` | INT8 signed×signed → INT32 accumulate |
| `mmaqau.b` | `__riscv_th_mmaqau` / `mmaqau()` | UINT8 unsigned×unsigned → INT32 |
| `mmaqaus.b` | `__riscv_th_mmaqaus` / `mmaqaus()` | UINT8×INT8 → INT32 |
| `mmaqasu.b` | `__riscv_th_mmaqasu` / `mmaqasu()` | INT8×UINT8 → INT32 |
| `mzero` | `__riscv_th_mzero_i32()` / `mzero_mi32()` | Zero accumulation register |
| `mdup<b/h/w/d>.m.x` | `__riscv_th_mdup_m_x(val)` / `mdup_m_x()` | Broadcast scalar to tile |
| `mlae8/16/32/64` | `__riscv_th_mld(ptr, stride, row, col)` / `mld_i8()` | Load A tile |
| `mlbe8` (stride load) | `msld_i8(ptr, k_stride)` | Load B tile with K-stride |
| `mst<b/h/w/d>` | `__riscv_th_mst(ptr, stride, val, row, col)` / `msst_i8_mi8()` | Store output |
| `mcfgi<m/n/k>` | `mcfgm(m)` / `mcfgk(k)` / `mcfgn(n)` | Set tile dimensions |

Note: the assembly mnemonic in v0.6.0 is `mmaqa.b` (not `mmacc.w.b` as in the RVME paper — the XuanTie spec uses `mmaqa` naming while the community RVM proposal uses `mmacc`). These are functionally equivalent INT8→INT32 MACs.

## Relationships

- [[RISC-V_Matrix_Extension]] — the community RVM v0.6.0 draft ISA; XuanTie AME is T-Head's implementation and the primary reference hardware for this spec.
- [[RISC-V_Matrix_Extension_Specification]] — broader T-Head spec page covering the toolchain ecosystem and demo applications.
- [[RVME_Matrix_Engine]] — academic RVME coprocessor also implements RVM v0.6 INT8 subset; uses `mmacc` with 4×8×8 OPA grid; 7.9–13.4× speedup over RVV for GEMM.
- [[RISC-V_Vector_Extension]] — RVV 1.0 is the companion ISA; AME handles GEMM compute while RVV handles activation, softmax, and bandwidth-bound GEMV.
- [[SHL_Library]] — T-Head's SHL 2.0 library provides AME-aware GEMM/attention kernels targeting XuanTie C908/C930 hardware.
- [[XuanTie_C908]] — AIoT RISC-V core implementing RVV 1.0 and AME; SHL GEMM recipe uses 16×12 outer-product register blocking.
- [[XuanTie_C930]] — Server-class RISC-V core with 512-bit RVV and AME; first server-grade RISC-V CPU from Alibaba/T-Head.
- [[Kernel_Dispatch_Decision_Tree_RVV_AME]] — synthesis page describing when to dispatch to AME vs. RVV vs. scalar given operator shape and datatype.

## Sources

- XUANTIE-RV/riscv-matrix-extension-spec (master, pushed 2026-04-01): https://github.com/XUANTIE-RV/riscv-matrix-extension-spec/
  - `spec/tilereg.adoc`: register file (tr0–tr3, acc0–acc3, TLEN/TRLEN/ALEN/ARLEN model)
  - `spec/matmul.adoc`: mmacc/mfmacc instruction table and semantics
  - `spec/program_model.adoc`: CSRs (mtilem/mtilek/mtilen, xmcsr, xmxrm, xmfflags, xmfrm, xmsaten, MS context bits)
  - `spec/load-store.adoc`: mlae*/mlbe*/mlce*/msce* load/store with transposed variants
  - `spec/misa.adoc`: hardware capability flags (compulsory vs. optional features)
  - `spec/config_set.adoc`: msettile{m|k|n}[i] configuration instructions
