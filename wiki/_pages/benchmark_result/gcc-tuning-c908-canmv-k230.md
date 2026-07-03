---
canonical_name: GCC Tuning Benchmark on XuanTie C908
aliases:
- C908 GCC tuning benchmark
- CoreMark C908 0.8%
- XuanTie C908 GCC Tuning
- C908 GCC scheduler model
- xt-c908 tuning
subtype: null
tags: []
hardware_targets:
- XuanTie C908
workloads:
- CoreMark
- instruction throughput loops (add, fadd etc.)
datatypes: []
metrics:
- CoreMark score improvement
- cycle-count improvement
toolchains:
- GCC
hardware_versions:
- CanMV-K230-V1.1 board
- XuanTie C908 R1S0
software_versions:
- GCC patch (2026-06-03)
measurement_method: 20 warm-up runs, 200 measured runs, aligned memory access
evidence_strength: measured
scorecard:
  novelty_delta: 0.9
  claim_density: 0.7
  self_containedness: 0.8
  bridge_score: 0.6
  hub_potential: 0.4
sources:
- raw/cache/84a65460eb9d8421.md
- https://gcc.gnu.org/pipermail/gcc-patches/2026-June/719208.html
- raw/cache/1369a5b7d9302dfe.md
- https://www.mail-archive.com/gcc-patches@gcc.gnu.org/msg406284.html
source_url: https://gcc.gnu.org/pipermail/gcc-patches/2026-June/719208.html
fetched_at: '2026-07-03T13:30:30.422521+00:00'
type: benchmark_result
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 5
outbound_links:
- target: xuantie-c908-gcc-tuning
  reason: This benchmark result is the direct performance validation of the GCC scheduler
    model documented on that hardware target page
- target: c908-wino-gemm-optimization
  reason: Contrasts a software library (SHL) optimization benchmark with the GCC compiler
    tuning benchmark; the SHL optimization assumes vector support, while this GCC
    benchmark confirms scalar-only measurement
---

# GCC Tuning Benchmark on XuanTie C908

The GCC tuning and scheduler model patch for the XuanTie C908 was benchmarked on a CanMV-K230-V1.1 development board using CoreMark and custom instruction throughput tests. The instruction throughput tests consisted of unrolled loops with groups of independent register instructions (e.g., adds and floating-point adds). Before measurement, the benchmark performed 20 warm-up runs, followed by 200 measured executions with aligned memory access. The tuning produced a 0.8% improvement in CoreMark score and cycle-count improvements ranging from 5% to 17% on the instruction throughput loops. These results were reported in the GCC patch submission by Milan Tripkovic and are classified as measured evidence based on the documented methodology. No vector instructions were used as the C908 lacks a vector extension.

## Key Claims

- CoreMark improvement: 0.8% on a CanMV-K230-V1.1 board.
- Cycle-count improvements on instruction throughput loops: 5% to 17%.
- Measurement methodology: 20 warm-up runs, then 200 measured runs with aligned memory access.
- The benchmark validates the scalar scheduler model for the C908 GCC tuning.

## Measurement Context

- Hardware version: XuanTie C908 on CanMV-K230-V1.1 board
- Software/toolchain version: GCC patch submitted 2026-06-03 (pre-trunk)
- Workload shape: CoreMark; unrolled loops with independent register groups (add, fadd, etc.)
- Metric: CoreMark score improvement (%), cycle-count improvement (%)
- Method: 20 warm-up runs, 200 measured runs, aligned memory access
- Evidence strength: measured

## Relationships

- [[xuantie-c908-gcc-tuning]]: This benchmark result is the direct performance validation of the GCC scheduler model documented on that hardware target page.
- [[c908-wino-gemm-optimization]]: Contrasts a software library (SHL) optimization benchmark with the GCC compiler tuning benchmark; the SHL optimization assumes vector support, while this GCC benchmark confirms scalar-only measurement.

## Sources

- https://gcc.gnu.org/pipermail/gcc-patches/2026-June/719208.html
