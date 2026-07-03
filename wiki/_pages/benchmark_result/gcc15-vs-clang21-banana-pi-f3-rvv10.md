---
canonical_name: GCC 15 vs Clang 21 on BananaPi-F3 (RVV 1.0)
aliases:
- BananaPi-F3 GCC Clang comparison
- RVV compiler evaluation 2026
subtype: null
tags:
- RVV
- compiler
- GCC
- Clang
hardware_targets:
- BananaPi F3
workloads:
- six scientific and ML proxy applications
- SGEMM
- DGEMM
- Qsim quantum circuit simulator
datatypes:
- float
metrics:
- performance (outperf count)
- predication overhead percentage
- stride load cost multiplier
toolchains:
- GCC 15
- Clang 21 (LLVM 21)
hardware_versions:
- BananaPi-F3 (RVV 1.0 hardware)
software_versions:
- GCC 15 (2025 release)
- Clang 21 (LLVM 21, 2025 release)
measurement_method: Assembly microbenchmarks to calibrate performance counters on
  BananaPi-F3 RVV hardware, then full-application benchmarks across six scientific
  and ML proxy applications and the Qsim quantum circuit simulator.
evidence_strength: measured
scorecard:
  novelty_delta: 0.8
  claim_density: 0.8
  self_containedness: 0.7
  bridge_score: 0.6
  hub_potential: 0.5
sources:
- raw/cache/48d543e9ad72412e.md
- https://arxiv.org/html/2605.10860v2
source_url: https://arxiv.org/html/2605.10860v2
fetched_at: '2026-07-03T14:02:39.701291+00:00'
type: benchmark_result
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 0
outbound_links:
- target: gcc-tuning-c908-canmv-k230
  reason: Both works evaluate GCC performance on RISC-V; the C908 benchmark focuses
    on scalar scheduler tuning, while this work evaluates vector-aware compilation
    on RVV 1.0 hardware using GCC 15 and Clang 21
---

# GCC 15 vs Clang 21 on BananaPi-F3 (RVV 1.0)

A comparative evaluation of GCC 15 and Clang 21 (LLVM 21) auto-vectorization support for the RISC-V Vector Extension (RVV) 1.0 was conducted on the BananaPi-F3 development board. The study designed assembly microbenchmarks to calibrate performance counters and then benchmarked six scientific and machine learning proxy applications, as well as the Qsim quantum circuit simulator with an RVV backend. GCC 15 outperformed Clang 21 in four of six applications, producing more stable and efficient code. Clang 21 achieved superior performance only in SGEMM and DGEMM due to more aggressive instruction reduction. Default LMUL selection was near-optimal in most cases, with GCC 15 showing greater tuning potential. Predication masks were found to introduce 35% overhead relative to unmasked vsetvl, and strided vector loads/stores cost up to 4× unit-stride equivalents. These results were reported by Shi et al. in 2026.

## Key Claims

- GCC 15 outperforms Clang 21 in 4 of 6 scientific/ML proxy benchmarks.
- Clang 21 achieves superior performance only in SGEMM and DGEMM.
- Predication masks introduce 35% overhead vs. unmasked vsetvl.
- Strided vector ld/st incur up to 4× cost of unit-stride.
- Default LMUL selection is near-optimal; GCC 15 has greater tuning potential.
- GCC 15 outperforms LLVM 21 on the Qsim quantum circuit simulator with RVV intrinsics.

## Measurement Context

- Hardware version: BananaPi-F3 (RVV 1.0)
- Software/toolchain version: GCC 15, Clang 21 (LLVM 21)
- Workload shape: six proxy apps (unnamed, including SGEMM and DGEMM); Qsim quantum circuit simulator
- Metric: benchmark win count, overhead reduction, stride cost multiplier
- Method: assembly microbenchmarks for perf counter calibration; full-application benchmarks
- Evidence strength: measured

## Relationships

- [[gcc-tuning-c908-canmv-k230]]: Both works evaluate GCC performance on RISC-V; the C908 benchmark focuses on scalar scheduler tuning, while this work evaluates vector-aware compilation on RVV 1.0 hardware using GCC 15 and Clang 21.

## Sources

- https://arxiv.org/html/2605.10860v2
