---
cold_start: false
constraints:
- RVA23 profile
- RVV 1.0 vector extension with vector crypto
- AMBA CHI bridge for cross-cluster communication
- Up to 256 cores via Arteris Ncore interconnect
- Sv57 virtual address space (57-bit)
- Distributed and scalable IOMMU
- Cross-cluster RAS (reliability, availability, serviceability)
created: '2025-03-26'
hardware_targets:
- SiFive Performance P870-D
inbound_links: 0
needs_summary_revision: false
scorecard:
  bridge_score: 0.5
  claim_density: 0.7
  hub_potential: 0.4
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://www.tomshardware.com/pc-components/cpus/sifive-sets-the-stage-for-256-core-risc-v-cpus-with-p870-d-core
tags:
- RISC-V
- datacenter
- SiFive
- P870-D
- high-performance
toolchains: []
type: hardware_target
updated: '2026-06-29'
---

# SiFive Performance P870-D

The SiFive Performance P870-D is a high-performance RISC-V processor core introduced in August 2024, specifically designed for datacenter and mission-critical applications. It builds upon the SiFive Performance P870 core, which is a six-wide out-of-order core implementing the RVA23 profile of the RISC-V instruction set architecture with support for vector (RVV 1.0) and vector crypto processing acceleration. The P870-D adds an open AMBA CHI bridge for energy-efficient cross-cluster communication, where each cluster contains one to four cores sharing an L2 cache, and introduces cross-cluster reliability, availability, and serviceability (RAS) features that enable processor designs with up to 256 cores. It also supports the RISC-V Sv57 extension providing a 57-bit virtual address space and includes a distributed, scalable IOMMU for accelerated virtualized device I/O. To scale to 256 cores, chip designers combine the P870-D with the Arteris Ncore cache coherent network-on-chip. SiFive began sampling the P870-D to lead customers in 2024, with production samples expected by the end of 2024 and first customer processors anticipated in 2025.

## Key Claims

- Up to 256 cores configurable in heterogeneous SoC and chiplet designs via Arteris Ncore NoC.
- Six-wide out-of-order pipeline with RVA23 profile compliance.
- RVV 1.0 vector extension with vector crypto acceleration.
- AMBA CHI bridge enabling low-latency, high-bandwidth cross-cluster communication.
- Cross-cluster RAS features for mission-critical reliability.
- Sv57 virtual address space (57-bit) for large memory addressability.
- Distributed and scalable IOMMU for virtualized device I/O.
- Claimed energy efficiency edge over x86 competitors for AI and datacenter workloads (qualitative statement from SiFive).
- Sampling to lead customers in 2024, production samples end of 2024, first processors expected in 2025.

## Relationships

- [[Chiplet_RISC_V_AI_SoC_Benchmark_Results]] – A chiplet-based RISC-V SoC benchmark showing how multi-chiplet RISC-V designs can achieve high performance, relevant as the P870-D targets similar multi-core/multi-chiplet datacenter implementations.
- [[Tenstorrent_Grayskull_MatMul_Efficiency]] – A competing datacenter-oriented RISC-V processor family (Grayskull) that also emphasizes performance-per-watt, providing a contrast for efficiency claims.

## Sources

- [SiFive sets the stage for 256-core RISC-V CPUs with P870-D core – Tom's Hardware](https://www.tomshardware.com/pc-components/cpus/sifive-sets-the-stage-for-256-core-risc-v-cpus-with-p870-d-core)

