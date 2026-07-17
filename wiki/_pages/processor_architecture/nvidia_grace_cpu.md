---
canonical_name: Nvidia Grace CPU
aliases:
- Grace CPU
- Nvidia Grace Superchip
- Grace Superchip
subtype: null
hardware_targets:
- Grace CPU
- Grace Superchip
workloads:
- HPC
- cloud computing
- data center
datatypes: []
metrics:
- performance per watt
- memory bandwidth
- interconnect bandwidth
- TDP
toolchains:
- Nvidia software stack
constraints:
- TSMC 4N
- Arm v9
- PCIe Gen5
- LPDDR5X ECC
evidence_strength: reported
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.85
  self_containedness: 0.9
  bridge_score: 0.3
  hub_potential: 0.7
sources:
- raw/cache/3220f5e06d9ffb12.md
- https://www.donanimhaber.com/nvidia-nin-grace-cpu-su-amd-ve-intel-rakiplerini-ikiye-katladi--168310
source_url: https://www.donanimhaber.com/nvidia-nin-grace-cpu-su-amd-ve-intel-rakiplerini-ikiye-katladi--168310
fetched_at: '2026-07-17T12:12:12.385954+00:00'
type: processor_architecture
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 0
---

# Nvidia Grace CPU

The Nvidia Grace CPU is an Arm-based processor architecture designed by Nvidia for data center and HPC workloads. Introduced at Hot Chips 2023, it features up to 144 Arm Neoverse V2 cores arranged in a dual-chip Superchip configuration, with each chip containing 72 cores. The Grace CPU is integrated into Nvidia's Superchip platforms, including the Grace Hopper Superchip, which pairs it with a GH200 GPU. The CPU utilizes LPDDR5X memory with ECC support, providing up to 960 GB of capacity and 1 TB/s memory bandwidth. It is manufactured on TSMC's 4N process node and includes 117 MB of L3 cache, 58 PCIe Gen5 lanes, and a proprietary high-speed interconnect (NVLink-C2C) offering 900 GB/s bandwidth. The entire Superchip consumes 500W TDP, delivering up to twice the performance per watt compared to competing x86 solutions like AMD's Genoa and Intel's Sapphire Rapids.

## Key Claims

- 144 Arm Neoverse V2 cores per Superchip (72 per chip) with Arm v9 architecture.
- Up to 960 GB LPDDR5X memory with ECC support, achieving 1 TB/s memory bandwidth.
- 117 MB L3 cache and 58 PCIe Gen5 lanes.
- TSMC 4N process node, 500W TDP for the Superchip.
- Up to 2x performance at the same power compared to dual-socket AMD EPYC 9654 (96 cores, 320W TDP each) and Intel Xeon Platinum 8480+ (56 cores, 350W TDP each) in server benchmarks.
- Up to 40% better performance than AMD Genoa and significantly ahead of Intel Sapphire Rapids in selected benchmarks.
- Up to 2.5x more performance in a 5 MW data center workload comparison.
- Supports full Nvidia software stack including CUDA, HPC, AI, and Omniverse.
- Includes NVLink-C2C interconnect with 900 GB/s bandwidth, 7x faster than PCIe Gen5.

## Relationships

No specific relationship to visible context pages in the current wiki.

## Sources

- [Nvidia’nın Grace CPU’su AMD ve Intel rakiplerini... | DonanımHaber](raw/cache/3220f5e06d9ffb12.md)
