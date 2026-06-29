---
cold_start: true
constraints:
- RVV 1.0
- 64-bit
- lane-based architecture
- coprocessor for CVA6
created: '2025-07-17'
hardware_targets:
- Ara
inbound_links: 0
scorecard:
  bridge_score: 0.6
  claim_density: 0.5
  hub_potential: 0.5
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://www.computer.org/csdl/proceedings-article/asap/2022/830800a043/1HxWu7cUTHq
tags:
- RISC-V
- vector processor
- open-source
- PULP
- Ara
- RVV 1.0
toolchains: []
type: hardware_target
updated: '2026-06-29'
---

# Ara Vector Processor

Ara is a 64-bit open-source vector processing unit designed to augment RISC-V processors with high-performance and energy-efficient vector computation. It implements the RISC-V Vector Extension version 1.0 (RVV 1.0) and serves as a coprocessor for the CVA6 core. Ara is developed by the PULP platform at ETH Zurich and the University of Bologna, and it was presented in 2022 as the first open-source implementation of the RVV 1.0 specification. The microarchitecture is lane-based, allowing scalable performance through configurable processing lanes. The design achieves comparable or better power, performance, and area (PPA) than state-of-the-art vector engines that implement the same specification. Ara interfaces with the scalar core via a coprocessor interface and supports strided and indexed memory accesses via protocols like AXI-Pack.

## Key Claims

- First open-source implementation of the RISC-V V 1.0 vector extension.
- Lane-based microarchitecture for scalable vector processing.
- Achieves comparable or better PPA than state-of-the-art vector engines.
- Developed by the PULP platform (ETH Zurich / University of Bologna).
- Designed as a coprocessor for the CVA6 core, using a coprocessor interface for scalar-vector coupling.

## Optimization-Relevant Details

- ISA/profile: RISC-V V 1.0 (RVV 1.0)
- Vector/matrix/accelerator support: Lane-based vector unit, variable number of lanes.
- Memory/cache/TLB/DMA: Supports strided and indexed memory accesses via AXI-Pack; memory interface details not fully specified in available resource.
- Compiler/toolchain support: No specific toolchain mentioned; expected to work with standard RISC-V toolchains supporting RVV 1.0.

## Relationships

- [[Parallel_GEMM_Convolution_on_GAP8]] – Another optimization recipe targeting the GAP8 processor, which is also part of the PULP platform family; both Ara and GAP8 share the PULP ecosystem heritage.
- [[Chiplet_RISC_V_AI_SoC_Benchmark_Results]] – A benchmark result page for a chiplet-based RISC-V AI SoC, representing a different design approach for RISC-V acceleration that complements the vector-processor philosophy of Ara.
- Insufficient context for additional cross-links: no entity pages for related concepts (e.g., PULP platform, CVA6 core, RISC-V Vector Extension) are present in the current wiki context.

## Sources

- [A “New Ara” for Vector Computing: An Open Source Highly Efficient RISC-V V 1.0 Vector Processor Design (ASAP 2022)](https://www.computer.org/csdl/proceedings-article/asap/2022/830800a043/1HxWu7cUTHq)
