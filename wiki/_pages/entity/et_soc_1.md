---
cold_start: true
created: '2026-06-26'
inbound_links: 0
scorecard:
  bridge_score: 0.6
  claim_density: 0.8
  hub_potential: 0.8
  novelty_delta: 0.8
  self_containedness: 0.7
sources:
- https://www.corsix.org/content/esperanto-lives-on
tags:
- ai-chips
- risc-v
- manycore
- open-source-hardware
- esperanto
- ainekko
type: entity
updated: '2026-06-27'
---

# ET-SoC-1

The ET-SoC-1 is a manycore RISC-V accelerator originally developed by Esperanto Technologies, an AI chip startup founded in 2014 that ceased operations in July 2025. The chip features a grid of tiles interconnected by a mesh Network-on-Chip (NoC), including 8 DRAM tiles each with a bridge to 4 GiB of LPDDR4x memory, a single PCIe tile for host communication, one Maxion tile containing 4 Maxion CPU cores and a Minion-lite core, and 34 Minion tiles each with 32 Minion CPU cores (2 threads each) and 4 MiB SRAM. One Minion tile is reserved for yield purposes, leaving 33 usable. The architecture adopts a GPU-like single address space model, distinct from competitors such as Tenstorrent. In October 2025, AINekko emerged from stealth and released open-source repositories including a simulator, kernel driver, and firmware under the Apache License v2, with plans to eventually open-source the RTL.

## Key Claims

- Esperanto Technologies completed RTL for Maxion CPUs in September 2018.
- The ET-SoC-1 was undergoing bring-up and characterization in H2 2021.
- Next-generation designs ET-SoC-2x and ET-SoC-3x were outlined in November 2024.
- Esperanto closed down in July 2025, retaining a small team to sell or license IP.
- AINekko released two GitHub repositories in October 2025: `et-platform` (simulator, kernel driver, firmware under Apache License v2) and `et-man` (programmer's reference manual).
- AINekko claimed that the chip's RTL will be open-sourced eventually, excluding third-party licensed IP.
- The chip is a PCIe Gen4 x8 board with 32 GiB of LPDDR4x total DRAM.
- The tile grid consists of 8 DRAM tiles, 1 PCIe tile, 1 Maxion tile, and 34 Minion tiles (33 usable after yield margin).
- Each DRAM tile bridges 4 GiB LPDDR4x via two 16-bit channels.
- The Maxion tile contains 4 Maxion CPU cores, 1 Minion-lite CPU core, and 5 MiB SRAM.
- Each Minion tile contains 32 Minion CPU cores (each with 2 hardware threads) and 4 MiB SRAM.
- The chip uses a mesh Network-on-Chip with a single address space model.

## Relationships

No direct relationships with existing pages yet. Potential future connections include pages on RISC-V manycore architectures, open-source hardware accelerators, and AI chip startups.

## Sources

- https://www.corsix.org/content/esperanto-lives-on
