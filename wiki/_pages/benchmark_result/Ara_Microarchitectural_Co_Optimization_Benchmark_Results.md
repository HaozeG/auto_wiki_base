---
cold_start: true
created: '2026-06-28'
datatypes:
- single-precision (assumed)
evidence_strength: measured
hardware_targets:
- Ara (open-source RVV 1.0 processor)
hardware_versions:
- Ara baseline (fixed hardware configuration)
inbound_links: 0
measurement_method: RTL simulation comparing Ara-Opt to baseline Ara; geometric mean
  across workloads.
metrics:
- speedup
- gap-closed ratio
scorecard:
  bridge_score: 0.7
  claim_density: 0.8
  hub_potential: 0.6
  novelty_delta: 0.9
  self_containedness: 0.8
software_versions: []
sources:
- https://arxiv.org/html/2604.22314v2
tags:
- RISC-V
- Ara
- RVV
- vector
- microarchitecture
- chaining
- speedup
toolchains: []
type: benchmark_result
updated: '2026-06-29'
workloads:
- scal
- axpy
- ger
- gemm
---

# Ara Microarchitectural Co-Optimization Benchmark Results

Benchmark results for the Ara-Opt microarchitectural optimizations are reported from RTL simulation on the Ara open-source RVV 1.0 processor with a fixed hardware configuration. The workloads evaluated include scal (vector scalar multiply), axpy (axpy operation), ger (rank-1 update), and gemm (general matrix multiply), assumed to be single-precision floating-point. The metrics are speedup over the baseline Ara and the gap-closed ratio, defined as the fraction of the gap between baseline performance and the roofline bound that is closed by the optimization. The optimizations achieve a geometric-mean speedup of 1.33× and a geometric-mean gap-closed ratio of 12.2% across all workloads. These results are sourced from the paper "Microarchitectural Co-Optimization for Sustained Throughput of RISC-V Multi-Lane Chaining Vector Processors" (arXiv:2604.22314v2) and provide the primary quantitative evidence for the optimization recipe [[Ara_Microarchitectural_Co_Optimization]].

## Key Claims

- Scal achieves a speedup of 2.41× with a gap-closed ratio of 93.7%.
- Axpy achieves a speedup of 1.60× with a gap-closed ratio of 88.9%.
- Ger achieves a speedup of 1.52× with a gap-closed ratio of 78.3%.
- Gemm achieves a speedup of 1.42× with a gap-closed ratio of 59.3%.
- The geometric-mean speedup across all workloads is 1.33×.
- The geometric-mean gap-closed ratio is 12.2%.

## Measurement Context

- **Hardware version**: Ara open-source RVV 1.0 processor (fixed configuration; lane count and VLEN not explicitly specified in the source).
- **Software/toolchain version**: Not specified in the source.
- **Workload shape**: scal (vector scalar multiply), axpy (axpy), ger (rank-1 update), gemm (matrix multiply); assumed single-precision floating-point data types.
- **Metric**: Speedup (×) and gap-closed ratio (%).
- **Method**: RTL simulation; the Ara-Opt implementation is compared to baseline Ara under the same hardware configuration and memory bandwidth. Results are presented as geometric means across workloads.
- **Evidence strength**: measured (RTL implementation).

## Relationships

- [[GEMM_with_RISC-V_Vector_Extension]] – Both use the Ara platform; this benchmark reports a 1.42× speedup for gemm.
- [[Ara_Microarchitectural_Co_Optimization]] – The optimization recipe that these benchmark results evaluate.

## Sources

- [arXiv:2604.22314v2](https://arxiv.org/html/2604.22314v2) – Microarchitectural Co-Optimization for Sustained Throughput of RISC-V Multi-Lane Chaining Vector Processors
