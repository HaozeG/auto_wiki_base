---
canonical_name: Ventana Veyron V2
aliases:
- Ventana Veyron V2
- Veyron V2
- Ventana Veyron V2 RISC-V CPU
- Ventana Veyron V2 platform
- Veyron V2 server chip
- Ventana Veyron V2 processor
subtype: null
tags:
- RISC-V
- Ventana
- server
- data center
- UCIe
- DSA
sources:
- raw/cache/67ec111109127562.md
- https://www.servethehome.com/ventana-veyron-v2-risc-v-cpu-launched-for-the-dsa-future/
- raw/cache/24d8bef31f86f608.md
- https://linuxgizmos.com/ventana-to-launch-veyron-v2-risc-v-platform-for-hpc-in-2025/
- raw/cache/d7fab3ad8db66982.md
- https://www.nextplatform.com/2023/11/07/ventana-launches-veyron-v2-risc-v-into-the-datacenter/
- raw/cache/c9aeb0391338c334.md
- https://www.storagereview.com/news/ventana-veyron-v2-risc-v-processor-announced
hardware_targets:
- Ventana Veyron V2
toolchains: []
constraints:
- RISC-V RVA23 profile
- UCIe chiplet interconnect
- AMBA CHI
- 192 cores per socket (6 x 32-core chiplets)
- 512KB I-cache per core
- 128KB D-cache per core
- 1MB L2 D-cache per core
- 128MB L3 cache per 32-core cluster
- DDR and PCIe controllers via I/O hub
- RAS (ECC, data poisoning)
- Secure boot and chiplet authentication
- IOMMU
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
scorecard:
  novelty_delta: 0.9
  claim_density: 0.7
  self_containedness: 0.8
  bridge_score: 0.5
  hub_potential: 0.6
source_url: https://www.servethehome.com/ventana-veyron-v2-risc-v-cpu-launched-for-the-dsa-future/
fetched_at: '2026-07-02T11:50:26.605789+00:00'
type: hardware_target
---

# Ventana Veyron V2

The Ventana Veyron V2 is a RISC-V data center processor designed by Ventana Micro Systems, targeting domain-specific acceleration and cloud workloads through a chiplet-based architecture. It implements the RVA23 profile, which includes ratified RISC-V vector extensions, and uses UCIe for chiplet interconnect to achieve up to 192 cores per socket. Each 32-core cluster is fabricated as a compute chiplet with up to 128 MB of shared L3 cache, while per-core caches include a 512 KB instruction cache, a 128 KB data cache, and a 1 MB L2 data cache. The processor supports AMBA CHI for cache coherence and integrates an I/O hub with DDR memory and PCIe controllers. Additional platform features include RAS capabilities (ECC, data poisoning), secure boot with chiplet authentication, and an IOMMU. The design emphasizes standards-based domain-specific acceleration by allowing chiplets other than CPU cores to be attached via UCIe.

## Key Claims

- Chiplet-based architecture with UCIe interconnect enables up to 192 cores per socket.
- Implements RVA23 profile (RISC-V vector extensions) and AMBA CHI.
- Each 32-core cluster has up to 128 MB of L3 cache.
- Per-core caches: 512 KB I-cache, 128 KB D-cache, 1 MB L2 D-cache.
- Supports RAS features including ECC and data poisoning.
- Includes secure boot and chiplet authentication.
- Domain-specific acceleration chiplets can be attached via UCIe alongside CPU compute chiplets.
- Integrates IOMMU for modern virtualization.

## Optimization-Relevant Details

- ISA/profile: RISC-V, RVA23 (includes vector extensions).
- Vector/matrix/accelerator support: RISC-V vector extensions (RVV); domain-specific acceleration chiplets via UCIe.
- Memory/cache/TLB/DMA: 512 KB I-cache, 128 KB D-cache, 1 MB L2 D-cache per core; up to 128 MB L3 per cluster; DDR memory controllers in I/O hub.
- Compiler/toolchain support: Not specified in available sources.

## Relationships

- [[gemmini]]: Both the Ventana Veyron V2 and Gemmini are part of the broader RISC-V ecosystem; Gemmini provides an agile systolic array generator for AI acceleration, while Veyron V2 targets general-purpose and DSA workloads in the data center.
- [[xuantie-c950]]: The XuanTie C950 is a competing RISC-V server processor from Alibaba's Damo Academy, offering a 5nm 64-bit multi-core design for AI and cloud computing; both represent the push of RISC-V into high-performance server-class computing.

## Sources

- [Ventana Veyron V2 RISC-V CPU Launched for the DSA Future](https://www.servethehome.com/ventana-veyron-v2-risc-v-cpu-launched-for-the-dsa-future/)
