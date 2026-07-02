---
canonical_name: Compiler Benchmark Comparison on BananaPi-F3 (RVV 1.0)
aliases:
- GCC 15 vs Clang 21 on RVV
- BananaPi-F3 compiler benchmark
- RVV compiler performance evaluation
subtype: null
tags: []
hardware_targets:
- BananaPi F3
workloads:
- SGEMM
- DGEMM
- Qsim (quantum circuit simulator)
- three additional HPC/ML proxy applications
datatypes:
- fp32
metrics:
- relative performance
- predication overhead (35%)
- strided load cost (4x)
- instruction count reduction
toolchains:
- GCC 15
- Clang 21
hardware_versions:
- BananaPi-F3 (RVV 1.0)
software_versions:
- GCC 15
- Clang 21
measurement_method: Assembly microbenchmarks and application benchmarks using validated
  perf counters on BananaPi-F3 RVV hardware.
evidence_strength: measured
scorecard:
  novelty_delta: 0.9
  claim_density: 0.9
  self_containedness: 0.8
  bridge_score: 0.8
  hub_potential: 0.7
sources:
- raw/cache/48d543e9ad72412e.md
- https://arxiv.org/html/2605.10860v2
source_url: https://arxiv.org/html/2605.10860v2
fetched_at: '2026-07-02T05:28:25.222253+00:00'
type: benchmark_result
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# Compiler Benchmark Comparison on BananaPi-F3 (RVV 1.0)

This benchmark study evaluates the auto-vectorization capabilities of GCC 15 and Clang 21 on the RISC-V Vector Extension (RVV) 1.0 hardware platform BananaPi-F3, using a custom suite of assembly microbenchmarks and six scientific and machine learning applications. The microbenchmarks specifically target RVV 1.0 arithmetic and data access operations, and are used to validate hardware performance monitoring counters through the Linux perf interface. Predication masks are found to introduce 35% overhead relative to unmasked vsetvl for tail elements, while strided vector load/store instructions incur up to 4x the cost of unit-stride equivalents. Across six benchmarks (including SGEMM, DGEMM, and a quantum circuit simulator Qsim), GCC 15 produces more stable and efficient code generation, outperforming Clang 21 in four of six benchmarks. Clang 21 achieves superior performance only in SGEMM and DGEMM, attributable to more aggressive instruction reduction as confirmed by the validated perf counters. Default LMUL selection proves near-optimal in most cases, though GCC 15 shows greater potential for performance gains through larger LMUL tuning than Clang 21. An RVV backend for Google's Qsim quantum circuit simulator, implemented using RVV intrinsics, demonstrates that GCC 15 again outperforms LLVM 21 on this complex, real-world workload.

## Key Claims

- Predication masks introduce 35% overhead compared to unmasked vsetvl for tail elements.
- Strided vector load/store instructions incur up to 4x the cost of unit-stride equivalents.
- GCC 15 outperforms Clang 21 in four of six scientific/ML benchmarks, while Clang 21 wins in SGEMM and DGEMM due to more aggressive instruction reduction.
- Default LMUL selection is near-optimal for both compilers, but GCC 15 shows more potential for performance gains through larger LMUL tuning.
- GCC 15 outperforms LLVM 21 on the Qsim quantum circuit simulator with an RVV intrinsic backend.
- Perf counters on RVV hardware were validated using assembly microbenchmarks.

## Measurement Context

- Hardware version: BananaPi-F3 with RVV 1.0 support.
- Software/toolchain version: GCC 15, Clang 21.
- Workload shape: Six proxy applications including SGEMM (single-precision GEMM), DGEMM (double-precision GEMM), Qsim (quantum circuit simulation), and three additional unnamed HPC/ML proxy apps.
- Metric: Relative performance comparison, predication overhead (35%), strided load cost (4x), instruction count reduction.
- Method: Assembly microbenchmarks and application runs using Linux perf counters; measurements validated by custom calibration.
- Evidence strength: measured.

## Relationships

- The hardware target for this benchmark is [[BananaPi-F3]], an RVV 1.0 platform also used in the [[mlir_xdsl_rvv_gemm_codegen_recipe]] recipe.
- Comparable compiler analysis for a different RVV hardware target is available on [[coral_npu_vector_execution_engine]], though that engine uses the Zve32x subset.
- The SiFive [[sifive_performance_p570_gen3]] core provides a contrasting RVV 1.0 implementation with a 128-bit vector pipeline, serving as another potential target for similar compiler benchmarking.
- The Qsim RVV backend contributed in this work is a new quantum simulation workload kernel relevant to [[workload_kernel]] pages in the wiki.

## Sources

- arXiv:2605.10860v2, "Towards Portable Performance on RISC-V Vector Processors" (May 2026).
