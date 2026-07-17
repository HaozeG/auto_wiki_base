---
canonical_name: AMD Pollara 400
aliases:
- Pensando Pollara 400
- Pollara 400 AI NIC
- Pollara 400
- Pensando Pollara 400 AI NIC
- AMD Pensando Pollara 400 AI NIC
- AMD Pensando Pollara 400
subtype: network_interface_card
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.6
  self_containedness: 0.9
  bridge_score: 0.7
  hub_potential: 0.3
sources:
- raw/cache/38bbda5aa9eac159.md
- https://www.servethehome.com/amd-pollara-400-details-at-hot-chips-2025/
- raw/cache/bdebbab11fd0fde4.md
- https://wccftech.com/amd-400gbe-speeds-industrys-first-uec-ready-pensando-pollara-400-ai-nic/
- raw/cache/8c063fa79585065f.md
- https://www.amd.com/en/products/network-interface-cards/pensando.html
- raw/cache/79ab67274d6a82e7.md
- https://www.storagereview.com/news/amds-pensando-pollara-400-nic-brings-programmability-and-performance-to-ai-networking
- raw/cache/608e554c10f29d3a.md
- https://www.tweaktown.com/news/101087/amd-reveals-worlds-first-ultra-ethernet-400-gbps-network-card/index.html
source_url: https://www.servethehome.com/amd-pollara-400-details-at-hot-chips-2025/
fetched_at: '2026-07-17T09:31:32.557509+00:00'
type: entity
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 0
---

# AMD Pollara 400

The AMD Pollara 400 is a 400GbE AI network interface card (NIC) developed by AMD’s Pensando division, unveiled at Hot Chips 2025. Designed specifically for AI scale-out networks, it features a P4 programmable packet processing pipeline and supports the Ultra Ethernet Consortium (UEC) standard for congestion control, multipathing, and packet spraying. The NIC is intended to be paired with AMD Instinct accelerators in a 1:1 ratio via PCIe switches, offloading networking tasks and addressing challenges such as packet loss, high utilization, and congestion in large training clusters. Unlike NVIDIA’s ConnectX-7, the Pollara 400 does not incorporate an internal PCIe switch, instead relying on external PCIe switches for host connectivity.

## Key Claims

- The AMD Pollara 400 is a 400GbE AI NIC that is UEC-ready, supporting Ultra Ethernet Consortium features such as multipathing, congestion control, and selective acknowledgment (SACK).
- It employs a P4 programmable packet pipeline, including a Table Engine (TE) for key generation and memory reads, and a Match Processing Unit (MPU) for flow pattern matching.
- The NIC provides hardware acceleration for virtual address to physical address translation, atomic memory operations, and pipeline cache coherency.
- AMD recommends a 1:1 ratio of Pollara 400 NICs to Instinct GPUs in systems (e.g., Gigabyte G893-ZX1-AAX2, ASUS ESC A8A-E12U), leveraging external PCIe switches rather than an internal switch on the NIC.
- With UEC-ready Pollara 400 NICs, AMD’s RCCL (counterpart to NCCNCCL) can improve training performance by reducing the impact of network congestion and packet loss.

## Relationships

- The AMD Pollara 400 is designed to pair with AMD Instinct accelerators built on the [[amd_cdna]] microarchitecture, connecting in a 1:1 ratio via PCIe switches without an internal PCIe switch on the NIC itself. Both target large-scale AI training clusters, with the NIC providing the networking offload for the compute accelerators.

## Sources

- [AMD Pollara 400 Details at Hot Chips 2025 - ServeTheHome](raw/cache/38bbda5aa9eac159.md)
