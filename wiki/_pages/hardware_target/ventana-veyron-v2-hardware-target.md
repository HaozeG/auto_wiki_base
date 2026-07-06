---
canonical_name: Ventana Veyron V2
aliases:
- Veyron V2
- Ventana V2
- Veyron V2 chiplet
subtype: null
tags: []
hardware_targets:
- Ventana Veyron V2
toolchains: []
constraints:
- 4 nm process
- 3.6 GHz clock frequency
- 15-wide out-of-order pipeline
- 32 cores per cluster
- Up to 192 cores via multi-cluster
- 128 MB shared L3 cache per cluster
- 512-bit vector unit
- Ventana AI matrix extensions
- UCIe chiplet interconnect
- Server-class IOMMU
- Advanced Interrupt Architecture (AIA)
- Comprehensive RAS features
- Advanced side channel attack mitigations
scorecard:
  novelty_delta: 0.9
  claim_density: 0.7
  self_containedness: 0.8
  bridge_score: 0.5
  hub_potential: 0.4
sources:
- raw/cache/81561a3402ca79c0.md
- https://www.techpowerup.com/315523/ventana-introduces-veyron-v2-worlds-highest-performance-data-center-class-risc-v-processor-and-platform
source_url: https://www.techpowerup.com/315523/ventana-introduces-veyron-v2-worlds-highest-performance-data-center-class-risc-v-processor-and-platform
fetched_at: '2026-07-06T02:38:22.471274+00:00'
type: hardware_target
created: '2026-07-06'
updated: '2026-07-06'
cold_start: true
inbound_links: 0
outbound_links:
- target: andes-ax45mpv-hardware-target
  reason: Both are high-performance RISC-V processor implementations with vector processing
    capabilities and AI acceleration features. The Veyron V2 is a complete chiplet-based
    processor targeting data center workloads, while the AX45MPV is a licensable IP
    core for SoC integration in embedded and AI applications. They share the RISC-V
    vector extension paradigm but target different market segments and form factors
---

# Ventana Veyron V2

Ventana Veyron V2 is a second-generation data center-class RISC-V processor from Ventana Micro Systems, announced in November 2023. It is designed as a chiplet-based multi-core processor fabricated on a 4 nm process, featuring a 15-wide aggressive out-of-order pipeline running at 3.6 GHz, with clusters of 32 cores scalable up to 192 cores. The Veyron V2 includes a 512-bit vector unit, Ventana AI matrix extensions for domain-specific acceleration, and server-class IOMMU and Advanced Interrupt Architecture (AIA) for server-level system integration. It supports UCIe chiplet interconnect for composable architectures, allowing customers to right-size compute, I/O, and memory, and claims to accelerate time-to-market by up to two years while reducing development costs by up to 75%. The processor targets data center infrastructure, automotive, 5G, AI, and client applications with a focus on performance per watt per dollar.

## Key Claims

- Up to 40% performance improvement over the previous generation Veyron V1.
- 3.6 GHz clock frequency on a 4 nm process.
- 15-wide aggressive out-of-order pipeline.
- 32 cores per cluster, scalable to 192 cores via multi-cluster.
- 128 MB of shared L3 cache per cluster.
- 512-bit vector unit for SIMD/vector workloads.
- Ventana AI matrix extensions for matrix-intensive workloads.
- UCIe chiplet interconnect enabling composable architectures and reducing time-to-market by up to two years and development costs by up to 75%.
- Server-class IOMMU and Advanced Interrupt Architecture (AIA).
- Comprehensive RAS (Reliability, Availability, Serviceability) features.
- Advanced side channel attack mitigations.
- SDK with software already ported to the Veyron platform, including top-down performance tuning methodology.

## Optimization-Relevant Details

- ISA/profile: RISC-V with custom AI matrix extensions and vector unit (512-bit).
- Vector/matrix/accelerator support: 512-bit vector unit, Ventana AI matrix extensions.
- Memory/cache/TLB/DMA: 128 MB shared L3 cache per cluster; no further cache hierarchy details provided.
- Compiler/toolchain support: SDK provided with ported software; no specific compiler versions mentioned.

## Relationships

- [[andes-ax45mpv-hardware-target]]: Both are high-performance RISC-V processor implementations with vector processing capabilities and AI acceleration features. The Veyron V2 is a complete chiplet-based processor targeting data center workloads, while the AX45MPV is a licensable IP core for SoC integration in embedded and AI applications. They share the RISC-V vector extension paradigm but target different market segments and form factors.

## Sources

- https://www.techpowerup.com/315523/ventana-introduces-veyron-v2-worlds-highest-performance-data-center-class-risc-v-processor-and-platform (Ventana press release via TechPowerUp, November 8, 2023)
