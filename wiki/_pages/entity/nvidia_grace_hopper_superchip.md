---
canonical_name: Nvidia Grace Hopper Superchip
aliases:
- Grace Hopper
- GH100
- Grace CPU + Hopper GPU
subtype: null
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.7
  self_containedness: 0.8
  bridge_score: 0.3
  hub_potential: 0.2
sources:
- raw/cache/6f359f0b05b283b3.md
- https://www.pcgameshardware.de/Grafikkarten-Grafikkarte-97980/News/Nvidia-Grace-Hopper-HPC-Details-Hot-Chips-Praesentation-1401626/
source_url: https://www.pcgameshardware.de/Grafikkarten-Grafikkarte-97980/News/Nvidia-Grace-Hopper-HPC-Details-Hot-Chips-Praesentation-1401626/
fetched_at: '2026-07-17T12:13:05.736219+00:00'
type: entity
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 0
---

# Nvidia Grace Hopper Superchip

The Nvidia Grace Hopper superchip is a high-performance computing platform that integrates a Grace CPU with 72 ARM Neoverse cores and a Hopper GPU, manufactured on TSMC's N4 (enhanced 5nm) process. The Grace CPU utilizes Nvidia's Scalable Coherency Fabric (SCF), a mesh network providing 3.2 TB/s of internal bandwidth to connect the ARM cores, memory, and I/O controllers, and is based on ARM's CMN-700 mesh technology customized by Nvidia. It supports up to 512 GB of LPDDR5X memory at a bandwidth of 546 GB/s, driven by 16 dual-channel memory controllers, and includes 68 PCIe 5.0 lanes and 12 NVLink lanes for external connectivity. The Hopper GPU employs HBM2e memory and is linked to the Grace CPU via NVLink, achieving up to 900 GB/s of bandwidth with five times the energy efficiency of PCIe 5.0, allowing direct memory access across the combined system even when the components reside on separate motherboards.

## Key Claims

- Grace CPU contains 72 ARM Neoverse cores.
- Both Grace and Hopper chips use TSMC's N4 (5nm-class) fabrication process.
- Grace CPU uses Nvidia's Scalable Coherency Fabric (SCF) with 3.2 TB/s bandwidth.
- The SCF is based on ARM's CMN-700 mesh network, customized by Nvidia.
- Grace supports up to 512 GB of LPDDR5X memory at 546 GB/s via 16 dual-channel memory controllers.
- The CPU provides 68 PCIe 5.0 lanes and 12 NVLink lanes.
- Hopper GPU uses HBM2e memory.
- NVLink connects Grace and Hopper at up to 900 GB/s with five times the energy efficiency of PCIe 5.0.
- Nvidia plans a Grace Superchip with two Grace CPUs and a Hopper Superchip with one Grace CPU and one Hopper GPU.

## Relationships

No specific relationship to visible context pages.

## Sources

- [Nvidia Grace und Hopper: Erste Details der Hot-Chips-Präsentation...](raw/cache/6f359f0b05b283b3.md)
