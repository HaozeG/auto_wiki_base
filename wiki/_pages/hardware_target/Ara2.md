---
cold_start: false
constraints:
- RVV 1.0 frozen ISA
- 22nm CMOS technology
- 2 to 16 lane configurable vector unit
- scalar core issue-rate bound for short vectors
created: '2025-03-28'
hardware_targets:
- Ara2
inbound_links: 1
needs_summary_revision: false
scorecard:
  bridge_score: 0.7
  claim_density: 0.9
  hub_potential: 0.8
  novelty_delta: 0.9
  self_containedness: 0.85
sources:
- https://arxiv.org/abs/2311.07493
tags:
- RISC-V
- vector processor
- open-source
- RVV 1.0
toolchains: []
type: hardware_target
updated: '2026-06-29'
---

# Ara2

Ara2 is the first fully open-source vector processor that implements the RISC-V V 1.0 frozen instruction set architecture, developed at ETH Zurich in collaboration with Huawei. It is a configurable multi-lane vector processor designed to exploit data-level parallelism across a wide range of data-parallel workloads. Ara2 is implemented in 22nm CMOS technology and supports 2 to 16 lanes, achieving a clock frequency of 1.35 GHz with a critical path of approximately 40 FO4 gates. The design is fully open-source, enabling detailed performance characterization, physical implementation analysis, and exploration of single- and multi-core vector processing trade-offs. Ara2 achieves a state-of-the-art energy efficiency of 37.8 DP-GFLOPS/W at 0.8V and an average functional-unit utilization of 95% on computationally intensive kernels, with performance bottlenecks identified across the scalar core, memories, and vector architecture.

## Key Claims

- First fully open-source vector processor to support the RISC-V V 1.0 frozen ISA.
- Configurable vector unit with 2 to 16 lanes; implemented in 22nm CMOS.
- Clock frequency of 1.35 GHz and critical path of ~40 FO4 gates.
- Energy efficiency of 37.8 DP-GFLOPS/W at 0.8V.
- Average functional-unit utilization of 95% on the most computationally intensive kernels.
- Multi-core clusters (e.g., eight 2-lane Ara2) overcome scalar core issue-rate bound and achieve >3x performance improvement over a single 16-lane core on 32x32x32 matrix multiplication, with 1.5x improved energy efficiency.
- Scalar core, memories, and vector architecture identified as primary performance boosters and bottlenecks.

## Optimization-Relevant Details

- ISA/profile: RISC-V V 1.0 (vector extension frozen).
- Vector/matrix/accelerator support: Multi-lane vector unit with configurable lane count (2–16).
- Memory/cache/TLB/DMA: Scalar core and memory hierarchy considered in performance analysis; details in paper.
- Compiler/toolchain support: Not specified in available resource (open-source toolchain likely).

## Relationships

- [[Chiplet_RISC_V_AI_SoC_Benchmark_Results]] – A different RISC-V AI accelerator benchmark on chiplet-based SoC.
- [[DSC_Fused_Dataflow_Benchmark_Results]] – Benchmark results for a fused dataflow accelerator for depthwise separable convolutions on RISC-V.
- insufficient context for additional cross-links (no existing Ara or RVV entity pages in wiki context).

## Sources

- [arXiv:2311.07493](https://arxiv.org/abs/2311.07493)
- [IEEE TC paper DOI: 10.1109/TC.2024.3388896](https://doi.org/10.1109/TC.2024.3388896)
