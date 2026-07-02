---
canonical_name: 'LLVM Optimization for RISC-V: Scheduling, Vectorization, and IPRA
  on SpacemiT X60'
aliases:
- LLVM RISC-V optimization case study
- RISE LLVM optimization
subtype: null
tags:
- LLVM
- RISC-V
- scheduling
- vectorization
- IPRA
- SpacemiT X60
hardware_targets:
- SpacemiT X60
workloads:
- SPEC CPU 2017
datatypes: []
metrics:
- execution time improvement
toolchains:
- LLVM
constraints:
- RVA22U64
- RVV 1.0
evidence_strength: measured
scorecard:
  novelty_delta: 0.9
  claim_density: 0.85
  self_containedness: 0.9
  bridge_score: 0.8
  hub_potential: 0.5
sources:
- raw/cache/e33233e6a6f364e1.md
- https://blogs.igalia.com/compilers/2025/11/22/unlocking-15-more-performance-a-case-study-in-llvm-optimization-for-risc-v/
source_url: https://blogs.igalia.com/compilers/2025/11/22/unlocking-15-more-performance-a-case-study-in-llvm-optimization-for-risc-v/
fetched_at: '2026-07-02T04:33:14.593320+00:00'
type: optimization_recipe
created: '2026-07-02'
updated: '2026-07-02'
cold_start: false
inbound_links: 1
needs_summary_revision: false
---

# LLVM Optimization for RISC-V: Scheduling, Vectorization, and IPRA on SpacemiT X60

This optimization recipe describes three LLVM improvements targeting the SpacemiT X60 processor on the Banana Pi BPI-F3 board: a full scheduling model for the in-order core, improved vectorization across function calls by better cost estimation in the SLP vectorizer, and enabling Inter-Procedural Register Allocation (IPRA) for the RISC-V backend. The prerequisite hardware is the SpacemiT X60 with RVA22U64 and RVV 1.0, and the software is LLVM with patches submitted upstream. The combined effect on SPEC CPU 2017 is up to 16% execution time improvement (later refined to 16% from the originally reported 15%). Failure modes include compilation time regressions for SLP vectorization, which were addressed in a refined patch. All measurements were performed on real hardware.

## Key Claims

- Scheduling model: up to 16.8% improvement on 538.imagick_r, geometric mean -4.75% on scalar-only RVA22U64, -3.28% with vectors (RVA22U64_V). No regressions.
- Vectorization across calls (SLP vectorizer modification): up to 11.9% improvement on 544.nab_r, geometric mean -3.28% with vectors, no regressions. Original patch caused compilation time regression; refined patch by maintainer fixed it.
- IPRA support: up to 3.2% improvement on 538.lbm_r (scalar), 3.4% on 508.deepsjeng_r (with vectors). Geometric mean improvements -0.50% scalar, -0.39% with vectors. No regressions on SPEC; cannot be enabled by default due to open bug.
- All improvements together yield up to 16% speedup on SPEC CPU 2017.

## Transformation

- Prerequisites: SpacemiT X60 hardware on Banana Pi BPI-F3 board, LLVM toolchain, access to SPEC CPU 2017 benchmarks, microbenchmarking tools for instruction latency collection.
- Steps:
  1. Scheduling model: Write custom microbenchmarks to measure latency for every instruction (201 scalar, 82 FP, 9185 RVV combinations at LMUL × SEW granularity). Use camel-cdr's RVV throughput data. Analyze and produce upstream LLVM patches to reflect scheduling data.
  2. Vectorization across calls: Modify the SLP vectorizer's cost model to walk all blocks in the region, not just basic blocks performing loads/stores, to account for vector register spills at function call boundaries. After refinement by maintainer Alexey Bataev, the patch avoids compilation time slowdown.
  3. IPRA: Enable IPRA in the RISC-V backend to track register liveness across call boundaries, reducing conservative spills and shortening prologues/epilogues.
- Expected effect: Up to 16% execution time improvement on SPEC CPU 2017, with geometric mean improvements around 4-5% on scalar and 3-4% on vector configurations.
- Failure modes: SLP vectorizer patch can cause compilation time increases of +6.9% (e.g., 502.gcc_r) without refinement; refined patch eliminates this. IPRA has open bug preventing default enablement, but does not affect SPEC performance.
- Measurements: SPEC CPU 2017 benchmarks on real hardware. Detailed per-benchmark improvements: 538.imagick_r +16.8%, 508.namd_r +16%, 544.nab_r +11.9%, 538.lbm_r +3.2%, 508.deepsjeng_r +3.4%.

## Relationships

- [[spacemit_x60]]: The hardware target that these optimizations were designed for.
- [[llvm_riscv_target]]: The LLVM RISC-V backend that received the patches for scheduling, vectorization, and IPRA.
- [[mlir_xdsl_rvv_gemm_codegen_recipe]]: Another optimization targeting the same board, focused on GEMM via MLIR/xDSL.
- [[spacemit_x60_llvm_spec_cpu2017_benchmark]]: Benchmark result page with more detailed measurements.

## Sources

- https://blogs.igalia.com/compilers/2025/11/22/unlocking-15-more-performance-a-case-study-in-llvm-optimization-for-risc-v/
