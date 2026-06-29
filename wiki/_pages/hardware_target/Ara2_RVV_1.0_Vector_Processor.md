---
cold_start: true
constraints:
- RVV 1.0 frozen ISA
- 22nm FD-SOI technology
- 2-16 processing lanes
- slide unit all-to-all interconnect (SLDU)
- scalar core issue-rate bound
- vector register file (VRF) organization
created: '2025-07-16'
hardware_targets:
- Ara2
inbound_links: 0
scorecard:
  bridge_score: 0.6
  claim_density: 0.8
  hub_potential: 0.7
  novelty_delta: 0.9
  self_containedness: 0.8
sources:
- https://arxiv.org/html/2311.07493v2
tags:
- RISC-V
- Ara2
- RVV 1.0
- vector processor
- open-source
toolchains: []
type: hardware_target
updated: '2026-06-29'
---

# Ara2 RVV 1.0 Vector Processor

Ara2 is a fully open-source vector processor designed by ETH Zurich and Huawei that implements the RISC-V Vector Extension 1.0 (RVV 1.0) frozen ISA. It extends the earlier Ara processor with full RVV 1.0 instruction support and microarchitectural optimizations that enable scalable performance from 2 to 16 processing lanes. Ara2 targets data-parallel workloads including linear algebra, digital signal processing, and machine learning. Implemented in a 22nm FD-SOI technology, it achieves a clock frequency of 1.35 GHz with a critical path of approximately 40 FO4 gates. The design is parameterizable in the number of lanes, allowing exploration of single- and multi-core vector processing trade-offs. Ara2 provides a research platform for detailed architectural performance studies on scalar core bottlenecks, vector register file organization, and multi-core configurations.

## Key Claims

- First fully open-source processor to support the RISC-V V 1.0 frozen ISA.
- Supports all RVV 1.0 instructions not supported in the preliminary version of Ara.
- Achieves average functional-unit utilization of 95% on computationally intensive kernels.
- Scalable from 2 to 16 lanes; implemented in 22nm FD-SOI technology.
- Clock frequency of 1.35 GHz with critical path ~40 FO4 gates.
- State-of-the-art energy efficiency of 37.8 DP-GFLOPS/W at 0.8V.
- Multi-core configurations can overcome scalar core issue-rate bound for short vectors.

## Optimization-Relevant Details

- **ISA/profile:** RISC-V with RVV 1.0 vector extension (frozen).
- **Vector/matrix/accelerator support:** Full RVV 1.0 instruction set including vector reductions; slide unit (SLDU) for all-to-all lane communication.
- **Memory/cache/TLB/DMA:** Scalar core with memory system analyzed as performance bottleneck; vector register file (VRF) with configurable size.
- **Compiler/toolchain support:** Open-source RISC-V toolchain; specific toolchain versions not reported in available resource.

## Relationships

- [[Tenstorrent_Grayskull_MatMul_Efficiency]] – Another RISC-V vector processor benchmark with efficiency comparison for matrix multiplication workloads.
- [[Chiplet_RISC_V_AI_SoC_Benchmark_Results]] – Benchmark results for a chiplet-based RISC-V AI accelerator, providing a contrast with heterogeneous integration approaches.

## Sources

- [arXiv:2311.07493v2](https://arxiv.org/html/2311.07493v2)
