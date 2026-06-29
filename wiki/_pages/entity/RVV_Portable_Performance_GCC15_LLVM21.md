---
type: entity
tags:
  - RISC-V
  - RVV
  - compiler
  - GCC
  - LLVM
  - benchmark
  - autovectorization
  - performance analysis
sources:
  - https://arxiv.org/abs/2605.10860
created: 2026-06-29
updated: 2026-06-29
cold_start: false
inbound_links: 0
scorecard:
  novelty_delta: 0.85
  claim_density: 0.9
  self_containedness: 0.9
  bridge_score: 0.85
  hub_potential: 0.8
---

# RVV Portable Performance: GCC 15 vs. LLVM 21 Autovectorization

This entity summarizes "Closer in the Gap: Towards Portable Performance on RISC-V Vector Processors" (arXiv:2605.10860, KTH Royal Institute of Technology, Lawrence Livermore National Laboratory, Barcelona Supercomputing Center, May 2026). The paper designs a suite of assembly microbenchmarks to establish performance ceilings and calibrate hardware PMU counters on real RVV 1.0 hardware, then uses those calibrated counters to evaluate GCC 15 and Clang/LLVM 21 autovectorization across six scientific and ML proxy applications. Key findings: GCC 15 produces more stable vectorized code in 4 of 6 benchmarks; Clang 21 outperforms only in SGEMM and DGEMM due to more aggressive instruction reduction; predication overhead and strided loads are the primary performance bottlenecks not captured by current compiler cost models.

## Key Claims

- Assembly microbenchmarks reveal that compiler-generated RVV code leaves measurable performance on the table compared to hand-tuned baselines.
- GCC 15 outperforms Clang/LLVM 21 in 4 out of 6 applications (HPC and ML proxy apps).
- Clang 21 outperforms GCC 15 only in SGEMM and DGEMM, driven by more aggressive instruction reduction (fewer total vector instructions issued).
- Predication overhead: masked vector operations impose non-trivial cost on current RVV hardware; compiler cost models do not fully account for predication latency, causing over-use of masked execution.
- Strided load bottleneck: non-unit-stride vector loads are a major performance bottleneck; current compilers do not adequately model strided load throughput in their cost models, leading to suboptimal memory access patterns.
- Default LMUL selection (LMUL=1 or auto) is near-optimal in most cases; manual LMUL tuning yields marginal gains with GCC 15 but greater potential improvement exists.
- PMU calibration method: assembly microbenchmarks cross-validate hardware performance counter readings; the calibrated counters are used to confirm instruction reduction claims (Clang 21 SGEMM/DGEMM improvement is attributed to ~15% fewer vector instructions).
- Study platforms: real RVV 1.0 hardware (not specified in abstract, likely SiFive or T-Head based).

## Relationships

- [[PMU_Roofline_Analysis_RISCV]] — both works deal with PMU calibration on RISC-V; this paper uses assembly microbenchmarks for calibration while the PMU Roofline paper uses LLVM IR arithmetic intensity to bypass faulty PMU hardware.
- [[RISC-V_Vector_Extension]] — study evaluates autovectorization of RVV 1.0 specifically.
- [[RVV_Autovectorization_Optimization_Insights]] — related wiki page on RVV autovectorization patterns; this paper provides updated 2026 data on GCC 15 vs. LLVM 21.
- [[Kernel_Dispatch_Decision_Tree_RVV_AME]] — compiler-generated RVV code underperforms hand-tuned code; the dispatch decision tree should prefer SHL/CSI-NN2 hand-tuned kernels over autovectorized fallbacks for GEMV and activation functions.
- [[GEMM_with_RISC-V_Vector_Extension]] — SGEMM and DGEMM are the benchmarks where Clang 21 outperforms GCC 15; GEMM-specific instruction scheduling is where LLVM's more aggressive optimization wins.

## Sources

- Closer in the Gap: Towards Portable Performance on RISC-V Vector Processors. arXiv:2605.10860v2. KTH, LLNL, BSC. May 2026.
