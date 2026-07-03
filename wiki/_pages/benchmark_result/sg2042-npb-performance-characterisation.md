---
canonical_name: SG2042 NPB Performance Characterisation
aliases:
- NAS Parallel Benchmark on SG2042
- SG2042 NPB results
subtype: null
tags: []
hardware_targets:
- Sophon SG2042
workloads:
- NAS Parallel Benchmark (NPB) suite
- Integer Sort (IS)
- Multi Grid (MG)
- Embarrassingly Parallel (EP)
- Conjugate Gradient (CG)
- Fast Fourier Transform (FT)
datatypes:
- float64 (implied, not explicitly stated)
metrics:
- performance (speedup ratio)
- relative performance
- memory bandwidth/latency sensitivity
toolchains: []
hardware_versions:
- Sophon SG2042 (64-core, 2 GHz, XuanTie C920)
software_versions:
- NPB suite (version not specified)
measurement_method: NASA's NAS Parallel Benchmark (NPB) suite run on the SG2042 and
  compared against other RISC-V, x86-64, and AArch64 CPUs. Single-core and multi-core
  results are reported.
evidence_strength: measured
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 0.7
  bridge_score: 0.5
  hub_potential: 0.6
sources:
- raw/cache/5b1c2c5ef89a99ef.md
- https://arxiv.org/abs/2406.12394
source_url: https://arxiv.org/abs/2406.12394
fetched_at: '2026-07-02T10:40:08.572250+00:00'
type: benchmark_result
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# SG2042 NPB Performance Characterisation

This page summarises the NAS Parallel Benchmark (NPB) performance characterisation of the Sophon SG2042 RISC-V CPU as published by Brown and Jamieson (2024, arXiv:2406.12394). The benchmark suite was used to evaluate the SG2042 against other CPUs implementing the RISC-V, x86-64, and AArch64 ISAs, with the goal of assessing its viability for HPC workloads. Key findings include a 2.6× to 16.7× single-core performance improvement over other RISC-V solutions, competitive performance on compute-bound algorithms against x86-64 and AArch64 CPUs, and a significant drop in relative performance on memory-bound algorithms. The memory subsystem (bandwidth and latency) is identified as the primary bottleneck. The SG2042 is the first mass-produced high-core-count RISC-V CPU and represents a notable step for RISC-V in the HPC space.

## Key Claims

- The SG2042 delivers a 2.6× to 16.7× single-core performance improvement over all other RISC-V CPUs tested using the NPB suite.
- When compared to x86-64 and AArch64 CPUs, the SG2042 performs comparatively well on computationally bound algorithms.
- Performance decreases significantly on memory-bandwidth- and latency-bound algorithms relative to x86-64 and AArch64 CPUs.
- The memory subsystem is the greatest performance bottleneck of the SG2042.

## Measurement Context

- Hardware version: Sophon SG2042 (64-core, 2 GHz, XuanTie C920 cores).
- Software/toolchain version: NPB suite (exact version not specified); compiler/toolchain not disclosed.
- Workload shape: NAS Parallel Benchmark suite including IS, MG, EP, CG, FT, and others.
- Metric: Performance (speedup ratios, relative performance).
- Method: Benchmarks executed on each CPU; results compared across architectures. Single-core and multi-core runs.
- Evidence strength: measured (empirical results from a research paper with documented methodology).

## Relationships

- [[sg2042-npb-single-core-performance]]: related via shared npb, performance, sg2042, sophon sg2042.

- [[sg2042-npb-benchmark]]: related via shared nas parallel benchmark (npb) suite, performance, sg2042, sophon sg2042.

- [[sophcon-sg2042]]: The hardware target that these benchmark results characterise.
- [[llvm-riscv-fptrunc-narrowing-optimization]]: A compiler optimisation that could potentially improve performance on the SG2042, though not directly connected by the paper.
- Insufficient context for additional cross-links: only one relevant page exists in the wiki.

## Sources

- [https://arxiv.org/abs/2406.12394](https://arxiv.org/abs/2406.12394)
