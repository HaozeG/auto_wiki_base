---
cold_start: false
created: '2026-06-26'
inbound_links: 0
scorecard:
  bridge_score: 0.6
  claim_density: 0.7
  hub_potential: 0.3
  novelty_delta: 0.6
  self_containedness: 0.8
sources:
- https://www.hackster.io/news/mangopi-mq1-is-an-ultra-compact-soon-to-be-open-source-allwinner-d1-risc-v-dev-board-eb5388783a0e
tags:
- risc-v
- allwinner
- single-board-computer
- open-hardware
type: entity
updated: '2026-06-27'
---

# MangoPi-MQ1

The MangoPi-MQ1 (later renamed MangoPi-Nezha MQ) is an ultra-compact single-board computer developed by MangoPi, based on the Allwinner F133-A system-on-chip (SoC), which is a variant of the Allwinner D1 that integrates 64 MB of on-chip memory. The board features a single 64-bit XuanTie C906 RISC-V core operating at 1 GHz, and was initially introduced in October 2021 with a planned retail price below $10, though it ultimately launched via Crowd Supply in 2022 at $39 with free worldwide shipping. The design files were released on GitHub under an unspecified open-source license, and the board was marketed as a compact competitor to the Nezha D1 development board. The MangoPi-MQ1 exemplifies the growing ecosystem of low-cost, open-source RISC-V hardware targeting hobbyists and embedded developers.

## Key Claims

- The MangoPi-MQ1 uses the Allwinner F133-A SoC, a variant of the D1 with integrated 64 MB DRAM, eliminating the need for an external memory chip.
- It contains a single 64-bit XuanTie C906 RISC-V core clocked at 1 GHz.
- Originally announced with an expected price under $10, the board's crowdfunding campaign on Crowd Supply offered it at $39 including free worldwide shipping, with shipments starting July 2022.
- The project's design files were published to GitHub under an unspecified open-source license.
- The board was designed to compete directly with the Nezha D1 development board, offering a smaller form factor.
- Targeted applications include Internet of Things (IoT) and hardware prototyping.

## Relationships

- [[allwinner_d1]] — The base SoC platform; the F133-A is a derivative.
- [[xuantie_c906]] — The RISC-V core used in the SoC.
- [[nezha_d1]] — A competing board that the MangoPi-MQ1 was designed to challenge.
- [[ai_chip_export_controls]] — While not directly constrained, the board is part of the broader Chinese RISC-V ecosystem that emerged partly in response to export restrictions on proprietary architectures.

## Sources

- Gareth Halfacree, "MangoPi-MQ1 Is an Ultra-Compact, Soon-to-be-Open Source Allwinner D1 RISC-V Dev Board," Hackster.io, October 26, 2021 (updated May 9, 2026). https://www.hackster.io/news/mangopi-mq1-is-an-ultra-compact-soon-to-be-open-source-allwinner-d1-risc-v-dev-board-eb5388783a0e
