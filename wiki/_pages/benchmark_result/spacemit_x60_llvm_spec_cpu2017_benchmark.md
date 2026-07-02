---
canonical_name: SPEC CPU 2017 LLVM Optimization Results on SpacemiT X60
aliases:
- LLVM RISC-V benchmark results
- SpacemiT X60 SPEC benchmark
subtype: null
tags:
- LLVM
- RISC-V
- SpacemiT X60
- SPEC CPU 2017
- scheduling
- vectorization
- IPRA
hardware_targets:
- SpacemiT X60
workloads:
- SPEC CPU 2017
datatypes: []
metrics:
- execution time improvement (percentage)
- geometric mean improvement
toolchains:
- LLVM
hardware_versions:
- Banana Pi BPI-F3 (SpacemiT X60)
software_versions:
- LLVM (post 10-month RISE project)
measurement_method: Benchmarking on real hardware using SPEC CPU 2017, comparing baseline
  LLVM vs patched LLVM.
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
type: benchmark_result
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# SPEC CPU 2017 LLVM Optimization Results on SpacemiT X60

This benchmark result reports the execution time improvements from LLVM compiler optimizations targeting the SpacemiT X60 processor on the Banana Pi BPI-F3 board, measured using the SPEC CPU 2017 benchmark suite. The improvements were obtained by applying three LLVM patches: a scheduling model for the X60, enhanced vectorization across calls in the SLP vectorizer, and IPRA support for the RISC-V backend. Testing was performed on real hardware by the RISE project, and results show up to 16% speedup (overall) and geometric mean improvements of -4.75% (scalar-only RVA22U64) and -3.28% (with vectors RVA22U64_V). Individual benchmark improvements include 16.8% on 538.imagick_r, 16% on 508.namd_r, 11.9% on 544.nab_r, 3.2% on 538.lbm_r, and 3.4% on 508.deepsjeng_r. No regressions were observed in tested configurations.

## Key Claims

- Overall SPEC CPU 2017 improvement: up to 16% execution time reduction (aggregate of scheduling, vectorization across calls, and IPRA).
- Scheduling model alone: up to 16.8% improvement on 538.imagick_r; geometric mean -4.75% on scalar RVA22U64, -3.28% on RVA22U64_V. No regressions.
- Vectorization across calls alone: up to 11.9% improvement on 544.nab_r; geometric mean -3.28% on RVA22U64_V. No regressions.
- IPRA alone: up to 3.2% on 538.lbm_r (scalar), 3.4% on 508.deepsjeng_r (with vectors); geometric mean -0.50% scalar, -0.39% with vectors. No regressions on SPEC.
- All measurements from real hardware; no regressions reported.

## Measurement Context

- Hardware version: SpacemiT X60 on Banana Pi BPI-F3 board (in-order, 8-core, RVA22U64, RVV 1.0, 256-bit vectors).
- Software/toolchain version: LLVM after applying the three optimization patches (exact commit not specified in source).
- Workload shape: SPEC CPU 2017 benchmarks (including 538.imagick_r, 508.namd_r, 544.nab_r, 538.lbm_r, 508.deepsjeng_r, and others).
- Metric: Execution time improvement (percentage reduction relative to baseline LLVM).
- Method: Measured on real Banana Pi BPI-F3 hardware; baseline LLVM compared with patched LLVM; geometric mean computed across benchmark suite.
- Evidence strength: measured

## Relationships

- [[spacemit_x60]]: The hardware target for these benchmarks.
- [[llvm_optimization_for_risc_v_scheduling_vectorization_ipra]]: The optimization recipe that produced these measured improvements.
- [[llvm_riscv_target]]: The LLVM RISC-V backend used.
- [[mlir_xdsl_rvv_gemm_codegen_recipe]]: A related optimization for the same board, targeting GEMM workloads with different techniques.

## Sources

- https://blogs.igalia.com/compilers/2025/11/22/unlocking-15-more-performance-a-case-study-in-llvm-optimization-for-risc-v/
