---
canonical_name: AraXL 22nm HPC/ML Benchmark
aliases:
- AraXL 146 GFLOPs result
- AraXL 40.1 GFLOPs/W
- AraXL performance at 1.15 GHz
subtype: null
tags: []
hardware_targets:
- AraXL
workloads:
- HPC/ML kernels (unspecified)
datatypes:
- double precision (implied)
metrics:
- GFLOPs
- GFLOPs/W
toolchains: []
hardware_versions:
- 22nm technology node
- 64 lanes
- 1.15 GHz clock
software_versions: []
measurement_method: Implemented in 22-nm technology node, measured at TT corner, 0.8V,
  1.15 GHz, using computation-intensive HPC/ML kernels.
evidence_strength: measured
scorecard:
  novelty_delta: 0.9
  claim_density: 0.9
  self_containedness: 0.9
  bridge_score: 0.7
  hub_potential: 0.6
sources:
- raw/cache/389b543e036b0128.md
- https://arxiv.org/html/2501.10301v1
source_url: https://arxiv.org/html/2501.10301v1
fetched_at: '2026-07-02T04:46:11.151365+00:00'
type: benchmark_result
created: '2026-07-02'
updated: '2026-07-02'
cold_start: false
inbound_links: 1
needs_summary_revision: true
---

# AraXL 22nm HPC/ML Benchmark

The AraXL vector processor, configured with 64 vector lanes and a 64 Kibit per vector register VRF, was fabricated in a 22-nm technology node and measured at 1.15 GHz (TT corner, 0.8V). On a set of computation-intensive HPC and machine learning kernels, the implementation achieves a peak performance of 146 GFLOPs with over 99% FPU utilization. The corresponding energy efficiency is 40.1 GFLOPs/W. These results demonstrate that the distributed hierarchical interconnect approach allows scaling to 64 lanes without wire-dominated degradation, achieving a 3.8× area increase relative to a 16-lane instance. The benchmark is reported in the AraXL paper by ETH Zürich and the University of Bologna.

## Key Claims

- Peak performance: 146 GFLOPs on HPC/ML kernels.
- Energy efficiency: 40.1 GFLOPs/W at 1.15 GHz.
- FPU utilization: >99% during benchmark.
- Area scaling: 64-lane instance uses 3.8× the area of a 16-lane instance.

## Measurement Context

- Hardware version: AraXL 64-lane, 22nm, nominal VDD 0.8V.
- Software/toolchain version: Not specified.
- Workload shape: Computation-intensive HPC and ML kernels (details not disclosed).
- Metric: Peak GFLOPs, energy efficiency in GFLOPs/W.
- Method: Measured on chip at 1.15 GHz, TT corner, 0.8V.
- Evidence strength: measured (from a manufactured test chip).

## Relationships

- [[araxl]]: the hardware target under test.
- [[xuantie_c908]]: a RISC-V vector processor with configurable VLEN 128/256, offering a contrast for smaller-scale vector implementations.
- [[k230]]: an SoC integrating the XuanTie C908 with RVV 1.0, representing a comparable RISC-V vector platform.

## Sources

- arXiv:2501.10301v1, "AraXL: A Physically Scalable, Ultra-Wide RISC-V Vector Processor Design for Fast and Efficient Computation on Long Vectors"
