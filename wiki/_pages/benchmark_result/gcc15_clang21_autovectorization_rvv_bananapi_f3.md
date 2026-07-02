---
canonical_name: GCC 15 vs Clang 21 Autovectorization on BananaPi-F3 (RVV)
aliases:
- RVV compiler autovectorization benchmark
- GCC15 vs LLVM21 RVV performance
- arXiv:2605.10860 benchmark
subtype: null
tags:
- RISC-V
- RVV
- compiler
- autovectorization
- GCC
- LLVM
- BananaPi
hardware_targets:
- BananaPi F3
workloads:
- SGEMM
- DGEMM
- scientific proxy applications (unspecified)
- ML proxy applications (unspecified)
datatypes:
- fp32
metrics:
- throughput (relative performance)
toolchains:
- GCC 15
- LLVM/Clang 21
hardware_versions:
- BananaPi-F3 (RVV 1.0)
software_versions:
- GCC 15
- Clang 21 (LLVM 21)
measurement_method: Assembly microbenchmarks for performance counter calibration;
  validated perf counters on RVV hardware.
evidence_strength: measured
scorecard:
  novelty_delta: 0.6
  claim_density: 0.8
  self_containedness: 0.5
  bridge_score: 0.6
  hub_potential: 0.4
sources:
- raw/cache/53f948c53967f26e.md
- https://arxiv.org/abs/2605.10860
source_url: https://arxiv.org/abs/2605.10860
fetched_at: '2026-07-02T04:32:20.321465+00:00'
type: benchmark_result
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# GCC 15 vs Clang 21 Autovectorization on BananaPi-F3 (RVV)

This benchmark result compares the autovectorization performance of GCC 15 and Clang 21 (part of the LLVM 21 toolchain) on the BananaPi-F3 RISC-V development board, which implements the RISC-V Vector Extension (RVV) 1.0. The evaluation covers six scientific and machine-learning proxy applications, including SGEMM and DGEMM. Performance is measured using validated performance counters after calibrating counter accuracy with a suite of assembly microbenchmarks. The study is presented in the paper "Closer in the Gap: Towards Portable Performance on RISC-V Vector Processors" (arXiv:2605.10860). Key findings include that GCC 15 produces more efficient and stable code generation in four of the six applications, while Clang 21 achieves superior performance only in SGEMM and DGEMM due to more aggressive instruction reduction. The paper also finds that default LMUL selection is near-optimal, and that predication overhead and stride loads are performance bottlenecks not fully addressed by current compiler cost models.

## Key Claims

- GCC 15 outperforms Clang 21 in four of six proxy applications on BananaPi-F3 RVV hardware.
- Clang 21 outperforms GCC 15 in SGEMM and DGEMM, attributed to more aggressive instruction reduction confirmed by validated perf counters.
- Default LMUL selection is near-optimal for both compilers; GCC 15 shows greater potential for additional performance gains through LMUL tuning.
- Predication overhead and stride loads pose performance challenges not captured by current compiler cost models.
- The paper introduces an RVV intrinsics backend for Google's Qsim quantum simulator; GCC 15 outperforms Clang 21 on this workload, revealing immaturity in current RVV compilers for complex memory access patterns.

## Measurement Context

- Hardware version: BananaPi-F3 (RVV 1.0)
- Software/toolchain version: GCC 15, Clang 21 (LLVM 21)
- Workload shape: Six proxy applications including SGEMM and DGEMM; remaining four unnamed in the available excerpt.
- Metric: Relative throughput comparison (no absolute metric values provided in the source excerpt)
- Method: Assembly microbenchmarks for performance counter calibration; validated perf counters on RVV hardware.
- Evidence strength: measured

## Relationships

- [[llvm_riscv_target]]: The LLVM RISC-V backend used by Clang 21 is documented in this target page.
- [[mlir_xdsl_rvv_gemm_codegen_recipe]]: This optimization recipe uses the LLVM toolchain for RVV code generation on similar BananaPi hardware, providing a complementary perspective on compiler-driven RVV performance.

## Sources

- https://arxiv.org/abs/2605.10860 ("Closer in the Gap: Towards Portable Performance on RISC-V Vector Processors")
