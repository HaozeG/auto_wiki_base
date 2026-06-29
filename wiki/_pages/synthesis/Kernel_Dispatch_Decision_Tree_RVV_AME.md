---
type: synthesis
connected_entities:
  - RISC-V_Vector_Extension
  - RISC-V_Matrix_Extension
  - RVME_Matrix_Engine
  - XuanTie_C908
  - XuanTie_C930
  - RVV_1_0_Programming
  - PMU_Roofline_Analysis_RISCV
  - T-SAR_In_Place_SIMD_ALU_Reorganization
  - I-LLM_Integer_Only_LLM_Optimization
  - TeraPool_Barrier_Synchronization_Benchmark_Results
  - Ara_Microarchitectural_Co_Optimization
  - TVM_CSINN2_Integration_Optimization_Recipe
  - llama.cpp_RVV_1.0_Q4_0_8_8_Optimization
synthesis_status: active
created: 2026-06-29
updated: 2026-06-29
cold_start: false
inbound_links: 0
sources:
  - wiki/_pages/hardware_target/RVME_Matrix_Engine.md
  - wiki/_pages/entity/RISC-V_Vector_Extension.md
  - wiki/_pages/entity/PMU_Roofline_Analysis_RISCV.md
  - wiki/_pages/benchmark_result/TeraPool_Barrier_Synchronization_Benchmark_Results.md
  - wiki/_pages/optimization_recipe/T-SAR_In_Place_SIMD_ALU_Reorganization.md
scorecard:
  bridge_score: 0.9
  contradiction_potential: 0.4
  cross_domain_connection: 0.85
---

# Kernel Dispatch Decision Tree for RVV+AME

## RAG Summary

On a RISC-V multi-PE chip with both an RVV 1.0 vector unit and an AME-style matrix engine (e.g., RVME, XuanTie AME), the optimal kernel backend depends on three factors: operator shape, datatype, and arithmetic intensity. For large square or near-square matrix multiplications with INT8 source operands accumulating to INT32, the AME path dominates: the RVME matrix engine achieves 7.9–13.4× speedup over an RVV GEMM baseline by replacing 64 vector-MAC operations with a single `mmacc` tile instruction. The AME bubble-free condition requires K ≥ m (tile row count); violating this stalls the outer product array (OPA) pipeline. For decode-phase GEMV (M=1 or small batch), RVV wins: the operation is bandwidth-bound at roughly 1 arithmetic operation per byte of weight loaded, and AME hardware is under-utilized at small M. For ternary or INT4 weight quantization, neither standard path is optimal; the T-SAR in-register LUT technique reorganizes SIMD registers to generate lookup tables on-chip, yielding 1.1–86.2× GEMV throughput improvement. Integer-only INT8/INT4 quantization (I-LLM) enables deployments that eliminate all floating-point operations. On multi-PE configs, barrier synchronization overhead stays below 10% of runtime when the working set fits the shared L1 scratchpad. Roofline model construction on RISC-V hardware requires PMU workarounds (SpacemiT X60 PMU sampling bug) or compiler-driven LLVM IR arithmetic intensity analysis via the miniperf toolchain.

---

## Full Synthesis

### Decision Tree

```
Operator shape?
├── GEMM (large M, N, K — compute-bound)
│   ├── INT8 inputs, INT32 accumulation + K ≥ tile_row_count?
│   │   └── → AME (mmacc): 7.9–13.4× over RVV baseline (RVME paper)
│   ├── FP16/BF16 or mixed types?
│   │   └── → RVV (vfmacc/vfmul): AME ISA subset is INT8→INT32 only
│   └── Ternary weights (BitNet / T-SAR)?
│       └── → RVV + in-register LUT (T-SAR): eliminates TLUT memory traffic
│
└── GEMV / decode phase (M=1 or small batch — bandwidth-bound)
    ├── FP16/FP32 weights?
    │   └── → RVV GEMV: arithmetic intensity ~1 op/byte; AME under-utilized
    ├── INT4 quantized weights (llama.cpp Q4_0)?
    │   └── → RVV dequantize-on-load: llama.cpp RVV 1.0 Q4_0_8_8, up to 3.5×
    └── INT8 fully-quantized (I-LLM)?
        └── → RVV integer path (DI-MatMul) or AME if batch ≥ tile threshold
```

### Why AME Wins at Large GEMM

The RVME OPA (Outer Product Array) eliminates the pre-load phase and inter-PE communication latency of systolic arrays. A single `mmacc` instruction computes an 8×8 tile of INT8→INT32 multiply-accumulate, replacing 64 scalar MACs or a corresponding RVV loop nest. Instruction count reduction is 21.7× vs. a vectorized baseline. The ping-pong PSM register scheme makes execution bubble-free whenever the K dimension satisfies K ≥ m (the tile row count); this is the primary scheduling constraint for the AME dispatch decision.

The RVM ISA instruction set (Table I in the RVME paper) exposes: `mmacc` (C+=A×BT), `mld`/`mat`/`mst` (tile load/transpose/store), element-wise `madd`/`msub`/`mmul`/`mmax`/`mmin`/`mshift`, `mcfg<m/n/k>` (tile dimension configuration), and `mzero` (zero accumulator). No FP or wider-integer variants are defined in the INT8-only implementation.

### Why RVV Wins at GEMV / Decode Phase

GEMV with a large weight matrix (N×K, e.g., 4096×4096) and a single activation vector (M=1) has arithmetic intensity = 2MNK / (MK + NK bytes) ≈ 2 ops/byte for INT8 — well below peak compute of any matrix engine. The bottleneck is memory bandwidth; AME provides no advantage when tiles are never full. RVV's vector load + vmacc pipeline overlaps memory and compute for sequential rows. For Q4_0 INT4 weights, the dequantize-on-load pattern (llama.cpp RVV 1.0 Q4_0_8_8) achieves up to 350% speedup by vectorizing the dequantization step with RVV 1.0 indexed loads.

### Ternary / INT4: T-SAR In-Register LUT

For ternary-weight networks (weights ∈ {-1, 0, +1}), neither conventional GEMM nor standard GEMV is efficient — the multiplication reduces to conditional add/subtract, but constructing lookup tables stresses the memory system (>75% of memory requests become LUT accesses in naive implementations). T-SAR reorganizes SIMD vector registers to generate ternary LUTs dynamically inside the register file, eliminating LUT memory traffic at 3.2% power and 1.4% area overhead. The technique targets x86 AVX2 but the authors demonstrate extension to ARM NEON and RISC-V Vector, making it directly applicable to RVV pipelines.

### Multi-PE Synchronization Budget

On many-core RISC-V clusters (e.g., TeraPool: 1024 cores, 4 MB shared L1), fork-join barrier synchronization overhead is below 10% of total runtime when the problem working set fits the 4 MB L1 scratchpad. Optimized tree barriers outperform naïve central-counter barriers at scale. The practical rule for multi-PE kernel dispatch: if the combined tile (across all PEs) exceeds L1, partition via DMA double-buffering and pay the synchronization tax only at tile boundaries.

### Roofline Model Construction

Constructing a roofline on RISC-V hardware requires measuring peak compute (FLOPS) and peak memory bandwidth simultaneously. Key tooling: the PMU Roofline/miniperf open-source toolchain for SpacemiT X60 works around a hardware PMU sampling bug (cycles/instructions counters fail under Linux perf_event). The compiler-driven mode uses LLVM IR to compute arithmetic intensity without hardware counters, making it portable across platforms with immature PMU support. For XuanTie C908/C930, the SHL (CSINN2) library provides hand-tuned kernels that approach the roofline ceiling; TVM BYOC integration offloads Relay operators to these SHL routines.

### Dispatch Heuristics Summary

| Regime | Operator | Datatype | Backend |
|--------|----------|----------|---------|
| Compute-bound | GEMM, M≥tile_m, K≥tile_k | INT8→INT32 | AME (mmacc) |
| Compute-bound | GEMM | FP16/BF16 | RVV (vfmacc) |
| Bandwidth-bound | GEMV, M=1 | FP16/INT8 | RVV GEMV |
| Bandwidth-bound | GEMV, M=1 | INT4 Q4_0 | RVV dequantize-on-load |
| ALU-bound | GEMV, M=1 | Ternary | RVV + T-SAR LUT |
| Mixed | Attention (prefill) | INT8 | AME for QK^T, RVV for softmax |
| Multi-PE | Any | Any | DMA double-buffer; barrier budget ≤10% if fits L1 |

## Open Questions

- T-Head AME ISA is now documented in `XUANTIE-RV/riscv-matrix-extension-spec` (v0.6.0, master branch). The core instruction is `mmaqa.b` (XuanTie naming) / `mmacc.w.b` (community RVM naming) — both are INT8→INT32 quad-widen MACs. The C intrinsic is `mmaqa()`. Throughput numbers for C930 AME at real workloads remain unconfirmed in public benchmarks; no direct comparison of XuanTie AME vs. RVME OPA at identical GEMM dimensions has been published. See [[XuanTie_AME_ISA]] for the full register model.
- The AME tile-fill threshold for M is implementation-specific (RVME uses 8×8 OPAs); for prefill attention with sequence length S > 1, the crossover point between AME and RVV depends on the tile dimensions of the target hardware.
- I-LLM's DI-MatMul integer-only quantization has only been validated on ARM/GPU targets; applicability to RISC-V RVV integer pipelines (no hardware multiplication widening) needs verification.
- RVV autovectorization from compilers (GCC 12+, LLVM 14+) does not yet generate AME instructions automatically; a compiler that jointly schedules RVV and AME requires an MLIR linalg-to-AME lowering path not yet described in the wiki.
- Benchmarked roofline numbers for XuanTie C910/C930 memory bandwidth (L1/L2/DRAM) are absent; SpacemiT X60 characterization from the PMU paper is the only RISC-V roofline data point currently in the wiki.

## Connected Pages

- [[RVME_Matrix_Engine]] — hardware implementation, OPA architecture, INT8→INT32 mmacc, EDP-optimal tiling
- [[RISC-V_Matrix_Extension]] — RVM ISA v0.6.0 spec, tile and accumulator register model
- [[RISC-V_Vector_Extension]] — RVV 1.0 ratified ISA, vsetvl/vsetvli, VLEN-agnostic programming
- [[RVV_1_0_Programming]] — practical RVV 1.0 programming patterns
- [[XuanTie_C908]] — T-Head RISC-V core with RVV 1.0 and AME, target for SHL kernels
- [[XuanTie_C930]] — T-Head server-class RISC-V core with 512-bit RVV and AME
- [[PMU_Roofline_Analysis_RISCV]] — LLVM IR + miniperf toolchain for RISC-V roofline construction
- [[T-SAR_In_Place_SIMD_ALU_Reorganization]] — ternary weight inference via in-register SIMD LUT
- [[I-LLM_Integer_Only_LLM_Optimization]] — INT8/INT4 fully-integer quantized LLM inference
- [[TeraPool_Barrier_Synchronization_Benchmark_Results]] — multi-PE barrier overhead characterization
- [[Ara_Microarchitectural_Co_Optimization]] — RVV vector processor co-design, scalar bottleneck analysis
- [[TVM_CSINN2_Integration_Optimization_Recipe]] — TVM BYOC to SHL/CSINN2 for XuanTie RVV
- [[llama.cpp_RVV_1.0_Q4_0_8_8_Optimization]] — INT4 dequantize-on-load RVV kernel
