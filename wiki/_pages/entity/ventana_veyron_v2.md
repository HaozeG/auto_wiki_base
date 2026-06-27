---
cold_start: true
created: 2026-06-27
inbound_links: 6
needs_summary_revision: true
scorecard:
  bridge_score: null
  claim_density: null
  hub_potential: null
  novelty_delta: null
  self_containedness: null
sources:
- https://www.ventanamicro.com/ventana-introduces-veyron-v2/
- https://www.servethehome.com/ventana-veyron-v2-risc-v-cpu-launched-for-the-dsa-future/
- https://www.ventanamicro.com/ventana-announces-2025-shipments-of-veyron-v2-platform-with-broad-market-adoption/
tags:
- risc-v
- server
- data-center
- AI-acceleration
- chiplet
type: entity
updated: 2026-06-27
---

# Ventana Veyron V2

The Ventana Veyron V2 is a server-class RISC-V processor developed by Ventana Micro Systems, positioned as the highest-performance data-center-grade RISC-V CPU available at its launch. Fabricated on a 4nm process and clocked at 3.6 GHz, the Veyron V2 scales to 192 cores organized as 32-core clusters, each cluster carrying 128 MB of shared L3 cache and a 512-bit vector unit. Ventana ships the V2 in both chiplet and standalone IP forms, integrating a UCIe chiplet interface specifically to enable tight coupling with domain-specific accelerators (DSAs) for AI and networking workloads. Volume shipments began in 2025 to early data center customers.

## Key Claims

- The Veyron V2 scales to 192 total cores across clusters of 32 cores each, with 128 MB of shared L3 cache per cluster and a 512-bit vector unit per core, fabricated on a 4nm process at 3.6 GHz.
- Ventana skipped productization of the V1 generation entirely, allowing V2 to launch with RVA23 compliance (including mandatory RVV 1.0) and a UCIe chiplet interface for accelerator integration — features absent from V1 prototypes.
- Each Veyron V2 core implements fifteen comprehensive out-of-order execution pipelines, targeting the throughput requirements of database, networking, and AI inference server workloads.
- The UCIe chiplet interface enables SoC designers to attach custom AI accelerator chiplets directly to the Veyron V2 compute fabric without going through PCIe, reducing memory-copy overhead for inference pipelines.
- Ventana announced 2025 shipments with broad market adoption across multiple customer segments, establishing Veyron V2 as the first commercially shipping RVA23-compliant server-class RISC-V processor in volume.
- Enterprise security features include an I/O memory management unit (IOMMU), Advanced Interrupt Architecture, RAS (Reliability, Availability, Serviceability) capabilities, and side-channel attack defenses — capabilities absent from earlier RISC-V server attempts.

## Relationships

- [[risc_v_vector_extension]] — V2 adopts RVA23, making RVV 1.0 mandatory and enabling vector-parallel AI workloads
- [[tenstorrent_tt_ascalon]] — competing high-performance RISC-V server CPU IP targeting similar data-center workloads

## Sources

- Ventana Veyron V2 introduction: https://www.ventanamicro.com/ventana-introduces-veyron-v2/
- ServeTheHome DSA architecture analysis: https://www.servethehome.com/ventana-veyron-v2-risc-v-cpu-launched-for-the-dsa-future/
- 2025 shipment announcement: https://www.ventanamicro.com/ventana-announces-2025-shipments-of-veyron-v2-platform-with-broad-market-adoption/
