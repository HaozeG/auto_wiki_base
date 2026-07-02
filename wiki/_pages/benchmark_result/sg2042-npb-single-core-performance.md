---
canonical_name: SG2042 NPB Single-Core Performance
aliases:
- NAS Parallel Benchmark SG2042 result
subtype: null
tags: []
hardware_targets:
- Sophon SG2042
workloads:
- NAS Parallel Benchmark (NPB)
datatypes: []
metrics:
- single-core performance improvement ratio
toolchains: []
hardware_versions:
- Sophon SG2042 (XuanTie C920 core)
software_versions: []
measurement_method: Single-core benchmark runs of the NASA NAS Parallel Benchmark
  suite, comparing the SG2042 against other RISC-V, x86-64, and AArch64 CPUs. Focus
  on single-core performance to control for core count differences.
evidence_strength: reported
scorecard:
  novelty_delta: 0.7
  claim_density: 0.6
  self_containedness: 0.8
  bridge_score: 0.6
  hub_potential: 0.5
sources:
- raw/cache/f40f095c46ded0be.md
- https://www.themoonlight.io/en/review/performance-characterisation-of-the-64-core-sg2042-risc-v-cpu-for-hpc
source_url: https://www.themoonlight.io/en/review/performance-characterisation-of-the-64-core-sg2042-risc-v-cpu-for-hpc
fetched_at: '2026-07-02T10:39:02.738589+00:00'
type: benchmark_result
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# SG2042 NPB Single-Core Performance

The SG2042 NPB single-core performance benchmark result reports the measured performance improvement of the Sophon SG2042 RISC-V CPU relative to other RISC-V solutions on the NASA NAS Parallel Benchmark (NPB) suite. The benchmark was conducted by the authors of arXiv:2406.12394 using single-core execution on the 64-core SG2042, which integrates XuanTie C920 cores with RV64GCV and RVV v0.7.1. The metric is the performance improvement factor in terms of execution speed, reported as a range of 2.6x to 16.7x over other RISC-V CPUs. The NPB benchmarks used include BT and SP, among others. The measurement context is single-core only, as core count differences across RISC-V CPUs were controlled by focusing on per-core performance. The evidence strength is 'reported', as the values are taken from the published paper without independent verification.

## Key Claims

- The Sophon SG2042 achieves a single-core performance improvement of 2.6x to 16.7x over other RISC-V CPUs on the NPB suite.
- The performance was measured using single-core runs to isolate core capability from core count.
- The SG2042 was compared against x86-64 and AArch64 CPUs, but the reported improvement range is specifically relative to RISC-V competitors.

## Measurement Context

- Hardware version: Sophon SG2042 (XuanTie C920 core)
- Software/toolchain version: Not specified in source.
- Workload shape: NAS Parallel Benchmark suite (BT, SP, and others)
- Metric: Performance improvement ratio (unitless)
- Method: Single-core execution, comparison against other RISC-V CPUs.
- Evidence strength: reported

## Relationships

- [[sophon-sg2042]]: The hardware target for which this benchmark was obtained.
- [[xuantie-c950]]: A competing high-performance RISC-V CPU with SPECint2006 results, providing a comparative benchmark context.

## Sources

- [arXiv:2406.12394](https://arxiv.org/abs/2406.12394)
- [Literature Review on The Moonlight](https://www.themoonlight.io/en/review/performance-characterisation-of-the-64-core-sg2042-risc-v-cpu-for-hpc)
