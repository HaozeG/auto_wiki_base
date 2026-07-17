---
canonical_name: Alphawave Semi HBM Subsystem
aliases:
- HBM3/2E/2 IP Subsystem
- HermesCORE HBM3 IP Subsystem
subtype: null
hardware_targets:
- HBM3
- HBM2E
- HBM2
workloads:
- graphics
- high-performance computing
- high-end networking
- communications
- AI inference
datatypes: []
metrics:
- bandwidth
- latency
toolchains: []
constraints:
- JEDEC compliance (HBM3, HBM2E, HBM2)
- 2.5D/3D ASIC system-in-package design
tags:
- HBM
- memory subsystem
- Alphawave Semi
scorecard:
  novelty_delta: 0.7
  claim_density: 0.8
  self_containedness: 0.9
  bridge_score: 0.3
  hub_potential: 0.4
sources:
- raw/cache/91bfd652a9070a86.md
- https://awavesemi.com/silicon-ip/subsystems/hbm-subsystem/
source_url: https://awavesemi.com/silicon-ip/subsystems/hbm-subsystem/
fetched_at: '2026-07-17T11:21:12.066522+00:00'
type: memory_architecture
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 0
---

# Alphawave Semi HBM Subsystem

The Alphawave Semi HBM Subsystem is a complete high-bandwidth memory (HBM) interface solution integrating an HBM controller and HBM physical layer (PHY) that supports JEDEC specifications for HBM3, HBM2E, and HBM2. Designed for applications in graphics, high-performance computing, high-end networking, and communications, the subsystem achieves data rates up to 8.4 Gbps per data pin across 16 independent channels, each 64 bits wide, for a total data width of 1024 bits. The solution is customizable and is deployed in 2.5D and 3D system-in-package designs, leveraging Alphawave Semi's experience in multi-die packaging to break through the memory wall in next-generation SoC applications.

## Key Claims

- Supports JEDEC HBM3, HBM2E, and HBM2 specifications across a wide range of technology and foundry nodes.
- Achieves per-pin data rates up to 8.4 Gbps.
- Features 16 independent channels, each 64 bits wide, for a combined 1024-bit data width.
- Targeted at graphics, HPC, high-end networking, and communications workloads.
- Integrated HBM controller and PHY form a complete subsystem that can be fine-tuned for application-specific AI and HPC workloads.
- Alphawave Semi is an early advocate of 2.5D and 3D ASIC design technologies and has delivered multiple successful 2.5D SoC system-in-package (SiP) demonstrations.
- The subsystem is configurable and can be customized per customer SoC IP specifications.

## Relationships

No specific relationship to visible context pages in the current wiki.

## Sources

- [HBM Subsystem - Alphawave Semi](raw/cache/91bfd652a9070a86.md)
