---
canonical_name: SG2042 NAS Parallel Benchmark Performance
aliases:
- Sophon SG2042 NPB benchmark
- NAS Parallel Benchmark Performance on SG2042
- SG2042 NPB benchmark result
- SG2042 NAS Parallel Benchmark performance
- SG2042 single-core RISC-V performance comparison
subtype: null
tags: []
hardware_targets:
- Sophon SG2042
workloads:
- NAS Parallel Benchmark (NPB) suite
datatypes: []
metrics:
- relative performance
- single-core performance improvement ratio
toolchains: []
hardware_versions:
- Sophon SG2042 (64-core, first released summer 2023)
software_versions: []
measurement_method: Performance characterization using NASA's NAS Parallel Benchmark
  (NPB) suite on the 64-core SG2042 compared against other RISC-V CPUs, x86-64, and
  AArch64 processors.
evidence_strength: reported
scorecard:
  novelty_delta: 0.7
  claim_density: 0.7
  self_containedness: 0.9
  bridge_score: 0.8
  hub_potential: 0.6
sources:
- raw/cache/20307e0c2e5b2ca7.md
- https://link.springer.com/chapter/10.1007/978-3-031-73716-9_25
- raw/cache/439ac77e161d2083.md
- https://arxiv.org/html/2406.12394
source_url: https://link.springer.com/chapter/10.1007/978-3-031-73716-9_25
fetched_at: '2026-07-02T12:43:17.273149+00:00'
type: benchmark_result
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# SG2042 NAS Parallel Benchmark Performance

The SG2042 NAS Parallel Benchmark Performance result characterizes the 64-core Sophon SG2042 RISC-V CPU using NASA's NAS Parallel Benchmark (NPB) suite. Published in a 2024 ISC High Performance workshop paper by Brown and Jamieson, the benchmark compares the SG2042 against other RISC-V CPUs, as well as x86-64 and AArch64 processors. The SG2042 consistently outperforms all other RISC-V solutions at the single-core level, delivering between 2.6× and 16.7× performance improvement. However, relative performance decreases for memory bandwidth- or latency-bound algorithms, identifying the memory subsystem as the greatest bottleneck. The benchmark provides evidence for the SG2042's viability in HPC applications despite its memory subsystem limitations.

## Key Claims

- SG2042 delivers 2.6× to 16.7× single-core performance improvement over other RISC-V CPUs in the NAS Parallel Benchmarks.
- SG2042 performs comparatively well on compute-bound algorithms versus x86-64 and AArch64 CPUs.
- SG2042's relative performance decreases on memory bandwidth- or latency-bound algorithms, indicating the memory subsystem is the primary bottleneck.

## Measurement Context

- Hardware version: Sophon SG2042 (64-core RISC-V CPU, first released summer 2023)
- Software/toolchain version: Not specified; NAS Parallel Benchmark suite (version not detailed)
- Workload shape: NASA NPB suite (includes benchmarks such as CG, IS, MG, FT, EP, etc.)
- Metric: Single-core performance improvement ratio (2.6–16.7×), relative performance comparison across compute-bound vs memory-bound algorithms
- Method: The NPB suite was executed on the SG2042 and compared against other RISC-V CPUs, x86-64, and AArch64 systems. Performance was characterized in terms of execution time and scalability. Specific numbers for x86-64 and AArch64 comparisons are not quantified in the abstract.
- Evidence strength: reported (conference paper)

## Relationships

- [[gap9-vs-stm32f7-odtl-benchmark]]: This benchmark also evaluates RISC-V hardware (GAP9) for performance-critical workloads, providing another data point for RISC-V in HPC-like scenarios.
- [[earth-shifting-based-vector-memory-access]]: The memory bottleneck identified in this benchmark highlights the need for optimization recipes targeting memory access patterns in RISC-V vector units.
- Insufficient context for additional cross-links; no entity pages for SG2042 or related hardware are available in the current wiki context.

## Sources

- [Performance Characterisation of the 64-Core SG2042 RISC-V CPU for HPC](https://link.springer.com/chapter/10.1007/978-3-031-73716-9_25)
