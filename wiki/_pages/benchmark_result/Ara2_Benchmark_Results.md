---
cold_start: true
created: '2025-03-28'
datatypes:
- double-precision (DP)
evidence_strength: measured
hardware_targets:
- Ara2
hardware_versions:
- Ara2 in 22nm, 2–16 lanes; cluster of eight 2-lane Ara2 (16 FPUs); single 16-lane
  Ara2 (16 FPUs)
inbound_links: 0
measurement_method: Synthesis and physical implementation in 22nm technology; simulation
  and measurement of runtime performance on data-parallel kernels and matrix multiplication.
metrics:
- energy efficiency (DP-GFLOPS/W)
- clock frequency (MHz)
- functional-unit utilization (%)
- performance speedup (3x)
- energy efficiency improvement (1.5x)
scorecard:
  bridge_score: 0.7
  claim_density: 0.9
  hub_potential: 0.8
  novelty_delta: 0.9
  self_containedness: 0.85
software_versions: []
sources:
- https://arxiv.org/abs/2311.07493
tags:
- RISC-V
- vector processor
- Ara2
- RVV 1.0
- energy efficiency
toolchains: []
type: benchmark_result
updated: '2026-06-29'
workloads:
- matrix multiplication (32x32x32)
- data-parallel kernels (diverse set)
---

# Ara2 Benchmark Results

Benchmark results for the Ara2 open-source RISC-V V 1.0 vector processor, implemented in 22nm CMOS technology, are reported in the paper "Ara2: Exploring Single- and Multi-Core Vector Processing with an Efficient RVV 1.0 Compliant Open-Source Processor" (arXiv:2311.07493). The chip was fabricated in 22nm and characterized across configurations from 2 to 16 lanes, for both single-core and multi-core clusters. Key measurements include a peak energy efficiency of 37.8 DP-GFLOPS/W at 0.8V, a clock frequency of 1.35 GHz, and an average functional-unit utilization of 95% on computationally intensive data-parallel kernels. A cluster of eight 2-lane Ara2 cores (16 FPUs total) achieves more than 3x the performance of a single 16-lane Ara2 core on a 32x32x32 matrix multiplication, with 1.5x improved energy efficiency. These results are sourced from the paper and represent measured values from physical implementation.

## Key Claims

- Peak energy efficiency of 37.8 DP-GFLOPS/W at 0.8V on double-precision matrix multiplication.
- Clock frequency of 1.35 GHz with a critical path of ~40 FO4 gates.
- Average functional-unit utilization of 95% on the most computationally intensive kernels.
- Multi-core cluster (eight 2-lane Ara2, 16 FPUs) achieves >3x performance improvement over single 16-lane Ara2 (16 FPUs) on 32x32x32 matrix multiplication.
- Multi-core cluster achieves 1.5x better energy efficiency than the single wide-core configuration on the same workload.
- Scalar core issue-rate bound is identified as the key bottleneck limiting short-vector performance in single-core configurations.

## Measurement Context

- Hardware version: Ara2 fabricated in 22nm CMOS; vector unit configurable from 2 to 16 lanes; tested in single-core (up to 16 lanes) and multi-core cluster (eight 2-lane cores).
- Software/toolchain version: Not specified in the available resource.
- Workload shape: Diverse set of data-parallel kernels (not individually listed) and 32x32x32 double-precision matrix multiplication.
- Metric: Energy efficiency (DP-GFLOPS/W), clock frequency (MHz), functional-unit utilization (%), performance speedup (ratio), energy efficiency improvement (ratio).
- Method: Physical implementation and measurement of fabricated chip; simulation for larger configurations.
- Evidence strength: measured (fabricated chip measurements and post-synthesis characterization).

## Relationships

- [[Ara2]] – The hardware target for which these benchmarks are reported.
- [[Chiplet_RISC_V_AI_SoC_Benchmark_Results]] – Another RISC-V accelerator benchmark for comparison.
- [[DSC_Fused_Dataflow_Benchmark_Results]] – A different TinyML-focused RISC-V accelerator benchmark.

## Sources

- [arXiv:2311.07493](https://arxiv.org/abs/2311.07493)
- [IEEE TC paper DOI: 10.1109/TC.2024.3388896](https://doi.org/10.1109/TC.2024.3388896)
