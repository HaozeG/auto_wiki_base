---
canonical_name: Ara2 22nm Vector Processing Benchmarks
aliases:
- Ara2 DP-GFLOPS/W measurement
- Ara2 multi-core comparison
subtype: null
tags: []
hardware_targets:
- Ara2
workloads:
- data-parallel kernels
- matrix multiplication 32x32x32
datatypes:
- fp64
metrics:
- DP-GFLOPS/W
- clock frequency (MHz)
- relative speedup (multi-core vs single-core)
- energy efficiency improvement
toolchains: []
hardware_versions:
- 22nm, 1.35 GHz, 0.8V
software_versions: []
measurement_method: Physical implementation (synthesis, place-and-route) in 22nm technology
  for PPA characterization; multi-core performance derived from simulation.
evidence_strength: measured
scorecard:
  novelty_delta: 0.95
  claim_density: 0.9
  self_containedness: 0.85
  bridge_score: 0.7
  hub_potential: 0.8
sources:
- raw/cache/8ed2ac43e51297ac.md
- https://arxiv.org/html/2311.07493v2
source_url: https://arxiv.org/html/2311.07493v2
fetched_at: '2026-07-02T04:47:09.593485+00:00'
type: benchmark_result
created: '2026-07-02'
updated: '2026-07-02'
cold_start: false
inbound_links: 1
needs_summary_revision: false
---

# Ara2 22nm Vector Processing Benchmarks

This benchmark result reports measured performance and energy efficiency of the Ara2 vector processor fabricated in a 22nm CMOS technology at 0.8V supply voltage. The processor was configured with 2–16 lanes and operated at a maximum clock frequency of 1.35 GHz. Key measurements include an energy efficiency of 37.8 DP-GFLOPS/W and a critical path of approximately 40 FO4 gates. On a 32×32×32 matrix multiplication workload, a multi-core cluster of eight 2-lane Ara2 units (16 FPUs total) achieved more than 3× the performance of a single 16-lane Ara2 core (also 16 FPUs), with a 1.5× improvement in energy efficiency. These results are derived from the IEEE TC publication by Perotti et al. (2024) and the accompanying arXiv preprint.

## Key Claims

- Energy efficiency of 37.8 DP-GFLOPS/W at 0.8V on 22nm process.
- Clock frequency of 1.35 GHz with critical path ~40 FO4 gates.
- Average functional-unit utilization of 95% on intensive kernels.
- Multi-core cluster (8×2-lane Ara2) outperforms single 16-lane Ara2 by >3× on 32×32×32 matrix multiplication.
- Energy efficiency of the multi-core cluster is 1.5× better than the single-core 16-lane configuration.

## Measurement Context

- Hardware version: 22nm CMOS, 0.8V supply, 1.35 GHz (max), ~40 FO4 critical path.
- Software/toolchain version: Not specified.
- Workload shape: Data-parallel kernels; specifically 32×32×32 matrix multiplication for multi-core comparison.
- Metric: DP-GFLOPS/W (energy efficiency), clock frequency (MHz), performance ratio (multi-core vs. single-core).
- Method: Physical implementation (synthesis, place-and-route) in 22nm technology for PPA characterization; multi-core performance derived from simulation.
- Evidence strength: measured

## Relationships

- [[ara2]]: The hardware target implementing these benchmarks.
- [[xuantie_c908]]: A comparable RVV 1.0 processor with different microarchitecture and performance targets.
- [[mlir_xdsl_rvv_gemm_codegen_recipe]]: An optimization recipe targeting RVV hardware that could be evaluated against these Ara2 benchmarks.

## Sources

- arXiv:2311.07493v2, "Ara2: Exploring Single- and Multi-Core Vector Processing with an Efficient RVV 1.0 Compliant Open-Source Processor"
- DOI: 10.1109/TC.2024.3388896
