---
cold_start: true
created: '2026-07-01'
datatypes:
- single-precision (f32)
- double-precision (f64)
evidence_strength: measured
hardware_targets:
- RVV 1.0 hardware (unnamed testbeds)
hardware_versions: []
inbound_links: 1
measurement_method: Assembly microbenchmarks with inner loop repeated 10^8 times;
  operands pre-staged in vector registers; dependency broken to expose peak issue
  throughput. Perf counters validated and used to measure instructions retired and
  cycle counts. Proxy applications compiled with -O2 and evaluated on two RVV 1.0
  testbeds.
metrics:
- throughput (instructions/cycle)
- overhead percentage
- speedup factor
scorecard:
  bridge_score: 0.8
  claim_density: 0.8
  hub_potential: 0.7
  novelty_delta: 0.9
  self_containedness: 0.9
software_versions:
- GCC 15
- LLVM 21
- RVV 1.0
sources:
- https://arxiv.org/html/2605.10860v1
tags:
- RVV
- compiler autovectorization
- GCC 15
- LLVM 21
- RISC-V vector
toolchains:
- GCC 15
- LLVM 21
type: benchmark_result
updated: '2026-06-28'
workloads:
- RVV arithmetic microbenchmarks
- RVV stride/unit-stride load microbenchmarks
- HPC proxy applications (SGEMM, DGEMM, Qsim)
- ML proxy applications
---

# RVV Autovectorization Compiler Benchmark (GCC15 vs LLVM21)

The RVV Autovectorization Compiler Benchmark (GCC15 vs LLVM21) documents the first published evaluation of GCC 15 and LLVM 21 on real RISC-V Vector Extension 1.0 hardware. Using custom assembly microbenchmarks that exercise key RVV 1.0 arithmetic and data-access instructions, the study establishes performance ceilings and validates hardware performance monitoring counters. It then applies these validated counters to compare the autovectorization quality of GCC 15 and LLVM 21 on six HPC and ML proxy applications, including SGEMM, DGEMM, and Google's Qsim quantum simulator. The benchmark reveals that predication masking incurs 35% overhead relative to unmasked operations, and strided vector loads cost up to 4x compared to unit-stride equivalents. GCC 15 outperforms LLVM 21 in four of six proxy applications, while LLVM 21 excels in SGEMM and DGEMM thanks to aggressive instruction reduction confirmed by perf counters.

## Key Claims

- Predication masks introduce 35% overhead relative to unmasked vsetvl for tail elements.
- Strided vector load/store instructions incur up to 4x the cost of unit-stride equivalents.
- GCC 15 outperforms LLVM 21 in four of six HPC/ML proxy applications.
- LLVM 21 outperforms GCC 15 in SGEMM and DGEMM, driven by more aggressive instruction reduction.
- Default LMUL selection in both compilers performs close to optimal.
- A set of RVV-specific hardware performance events in perf profiling are validated and reliable.

## Measurement Context

- Hardware version: RVV 1.0 hardware (two unnamed testbeds).
- Software/toolchain version: GCC 15, LLVM 21; RVV 1.0 intrinsics; perf profiling.
- Workload shape: Assembly microbenchmarks (10^8 iterations per instruction), proxy applications (SGEMM, DGEMM, Qsim, others).
- Metric: Throughput (instructions/cycle), overhead percentage, speedup factor.
- Method: Assembly microbenchmarks with controlled sequences, operands pre-staged. Proxy applications compiled with -O2 and run on hardware; perf counters validated and used for analysis.
- Evidence strength: measured.

## Relationships

- [[Gemmini_systolic_array_GEMM_accelerator]] – Both evaluate RISC-V performance for compute-intensive workloads, though using different acceleration approaches.
- [[Q4X_Quantization_LLM_Inference_MilkV_Jupiter_Benchmark]] – Another RVV benchmark demonstrating measured results on specific hardware.

## Sources

- [arXiv:2605.10860v1](https://arxiv.org/html/2605.10860v1)

