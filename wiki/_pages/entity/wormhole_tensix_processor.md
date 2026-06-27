---
cold_start: false
created: '2026-06-26'
inbound_links: 0
scorecard:
  bridge_score: 0.6
  claim_density: 0.5
  hub_potential: 0.3
  novelty_delta: 0.8
  self_containedness: 0.2
sources:
- https://docs.tenstorrent.com/aibs/wormhole/index.html
tags:
- ai-accelerator
- tenstorrent
- tensix
type: entity
updated: '2026-06-27'
---

# Wormhole Tensix Processor

The Wormhole series (n150d/n150s/n300d/n300s) from Tenstorrent is a family of PCI Express add-in boards designed for high-performance artificial intelligence and machine learning workloads. Each board is built around Tensix cores—a proprietary multi-core architecture that integrates compute units, a network-on-chip (NoC), local cache memory, and small RISC-V processors for data movement. The lineup includes single-ASIC variants (n150d, n150s) and dual-ASIC variants (n300d, n300s), with the latter offering up to double the processing capacity. The Wormhole n300s is passively cooled and priced at $1,399, and it forms the building block of Tenstorrent's TT-LoudBox workstation, which combines four n300s cards for an eight-processor configuration. The official documentation covers system requirements, hardware installation, software setup, specifications, and regulatory compliance.

## Key Claims

- Wormhole n150 and n300 PCIe boards feature Tensix Cores, each containing a compute unit, network-on-chip (NoC), local cache, and small RISC-V cores for data movement.
- The Wormhole n300s is a dual-ASIC board with passive cooling, listed at a price of $1,399.
- Tenstorrent offers the TT-LoudBox workstation, which is powered by four Wormhole n300s boards, providing a total of eight processors.
- Wormhole boards are marketed as providing superior performance per dollar compared to traditional GPUs.
- Full documentation is available at Tenstorrent's official site, including hardware installation, software setup, specifications/requirements, FAQ, troubleshooting, and regulatory compliance statements.
- Wormhole n150/n300 developer kits and the TT-LoudBox workstation are available for immediate purchase as of the documentation's last update (June 2026).

## Relationships

- [[tensix_architecture]] — Wormhole is a direct implementation of Tenstorrent's Tensix architecture; a dedicated page on Tensix architecture is a planned addition to the wiki.
- [[ai_chip_export_controls]] — As an AI accelerator, the Wormhole series may be affected by US export controls on high-performance semiconductors; however, no specific regulatory status for Wormhole is documented in the current resource.
- [[tenstorrent_metalium_software_stack]] — Wormhole boards are programmed using Tenstorrent's Metalium software stack, which is detailed in a separate set of documentation.

## Sources

- Tenstorrent Wormhole PCIe Card Documentation: https://docs.tenstorrent.com/aibs/wormhole/index.html
- DDG search snippets providing supplemental product details (price, variants, TT-LoudBox configuration).

