---
cold_start: false
created: '2025-09-01'
datatypes:
- double-precision (assumed)
evidence_strength: reported
hardware_targets:
- Tenstorrent Wormhole n300
hardware_versions:
- Tenstorrent Wormhole n300
inbound_links: 0
measurement_method: Comparison of accelerated N-body code on Wormhole n300 against
  a highly optimized CPU implementation of the same algorithm; measurements of execution
  time and energy consumption.
metrics:
- speedup
- energy efficiency
needs_summary_revision: false
scorecard:
  bridge_score: 0.7
  claim_density: 0.7
  hub_potential: 0.6
  novelty_delta: 0.8
  self_containedness: 0.8
software_versions: []
sources:
- https://arxiv.org/html/2509.19294v1
tags:
- N-body
- astrophysics
- Tenstorrent
- Wormhole
- RISC-V
- benchmark
toolchains:
- TT-Metalium
type: benchmark_result
updated: '2026-06-29'
workloads:
- Gravitational N-body simulation
---

# N-Body Simulation on Tenstorrent Wormhole Benchmark

Benchmark results for accelerating gravitational N-body simulations on the RISC-V-based Tenstorrent Wormhole n300 accelerator are reported in the paper 'Accelerating Gravitational N-Body Simulations Using the RISC-V-Based Tenstorrent Wormhole' (arXiv:2509.19294). The implementation ports an astrophysical direct N-body code to the Wormhole using the TT-Metalium programming interface, offloading the force calculation to the accelerator. Measurements indicate more than a 2x speedup and approximately 2x energy savings compared to a highly optimized CPU implementation of the same algorithm. This result demonstrates the viability of RISC-V accelerators for scientific high-performance computing, particularly for linear algebra-heavy workloads common in astrophysics.

## Key Claims

- More than 2x speedup achieved compared to an optimized CPU implementation.
- Approximately 2x energy savings compared to the CPU baseline.
- First demonstration of an astrophysical N-body code on a RISC-V accelerator.
- The porting effort used the TT-Metalium SDK to offload computationally expensive force calculations.

## Measurement Context

- **Hardware version:** Tenstorrent Wormhole n300 (64 Tensix cores, 12 GB GDDR6, PCIe 4.0 x16).
- **Software/toolchain version:** TT-Metalium (low-level SDK).
- **Workload shape:** Direct gravitational N-body simulation, O(N^2) force computation for all particle pairs.
- **Metric:** Speedup (execution time ratio) and energy savings (energy consumption ratio).
- **Method:** Experimental comparison of accelerated code on Wormhole vs. highly optimized CPU version of the same N-body algorithm.
- **Evidence strength:** reported (claims from a peer-reviewed paper, detailed experimental setup not fully extracted).

## Relationships

- [[Tenstorrent_Wormhole_n300]] – Hardware target used for this benchmark.
- [[Parallel_GEMM_Convolution_on_GAP8]] – Another RISC-V acceleration benchmark for comparison.

## Sources

- [Accelerating Gravitational N-Body Simulations Using the RISC-V-Based Tenstorrent Wormhole (arXiv:2509.19294)](https://arxiv.org/html/2509.19294v1)

