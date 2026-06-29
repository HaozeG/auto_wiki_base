---
cold_start: true
constraints:
- RVV 1.0
created: '2025-12-30'
datatypes: []
evidence_strength: reported
hardware_targets:
- RISC-V Vector Extension 1.0 (RVV 1.0)
inbound_links: 0
metrics:
- area reduction
- power reduction
scorecard:
  bridge_score: 0.6
  claim_density: 0.7
  hub_potential: 0.5
  novelty_delta: 0.9
  self_containedness: 0.8
sources:
- https://www.researchgate.net/publication/390749222_Efficient_Architecture_for_RISC-V_Vector_Memory_Access
tags:
- RISC-V
- vector
- memory access
- shift network
- EARTH
toolchains: []
type: optimization_recipe
updated: '2026-06-29'
workloads:
- strided memory access
- segment memory access
---

# EARTH: Efficient Architecture for RISC-V Vector Memory Access

EARTH is a novel vector memory access architecture proposed for RISC-V vector processors to overcome inefficiencies in strided and segment memory access patterns. It replaces conventional high-overhead crossbars with specialized shift networks that gather and scatter strided elements while coalescing multiple accesses within the same cache line into a single request. The architecture introduces components such as DROM, LSDO, and RCVRF to implement shifting-based optimizations. This optimization recipe describes the transformation from conventional crossbar-based design to EARTH's shift network approach. According to the paper, EARTH reduces hardware area by 9% and power consumption by 41% compared to conventional designs. The implementation targets the RISC-V Vector Extension (RVV) version 1.0. Measurements are reported from the original publication and have evidence strength classified as reported.

## Key Claims

- EARTH integrates specialized shift networks for gathering and scattering strided elements, eliminating the need for full crossbars.
- Coalescing multiple accesses into one request within the same cache line reduces memory access overhead.
- Compared to conventional designs, EARTH achieves a 9% reduction in hardware area and a 41% reduction in power consumption.
- The architecture supports constant-stride and segment memory access patterns as specified in RVV 1.0.
- Key components include DROM, LSDO, and RCVRF for shifting-based data routing.

## Transformation

- Prerequisites: RISC-V vector processor implementing RVV 1.0; frequent strided or segment memory access patterns in workloads.
- Steps:
  1. Identify strided or segment memory access patterns in the vector processor.
  2. Replace the conventional crossbar with specialized shift networks that handle fixed-stride gathering and scattering.
  3. Implement coalescing logic to combine multiple memory accesses that fall within the same cache line into a single request.
  4. Route data between memory and vector registers through the shift network using DROM, LSDO, and RCVRF components.
- Expected effect: Reduced hardware area (9%) and power (41%) while maintaining or improving performance for strided/segment access patterns.
- Failure modes: Not explicitly discussed; naive implementations that retain full crossbars incur high overhead; the shift network may be less flexible for arbitrary (non-stride) gather/scatter patterns.
- Measurements: Paper reports 9% area reduction and 41% power reduction compared to conventional crossbar-based designs. Evidence strength is reported.

## Relationships

- [[Parallel_GEMM_Convolution_on_GAP8]] – Another RISC-V optimization recipe for convolution, illustrating a different approach to data movement optimization.
- [[DSC_Fused_Dataflow_Benchmark_Results]] – A benchmark result for a fused dataflow accelerator, providing contrast on data movement reduction techniques.
- [[Chiplet_RISC_V_AI_SoC_Benchmark_Results]] – A benchmark for a RISC-V AI SoC that may benefit from improved vector memory access.

## Sources

- [ResearchGate: Efficient Architecture for RISC-V Vector Memory Access](https://www.researchgate.net/publication/390749222_Efficient_Architecture_for_RISC-V_Vector_Memory_Access)

