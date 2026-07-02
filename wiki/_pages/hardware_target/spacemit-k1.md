---
canonical_name: SpacemiT K1
aliases:
- K1
- SpacemiT K1 RISC-V chip
- SpacemiT K1 SoC
- SpacemiT Key Stone K1
- Key Stone K1
- SpacemiT K1 (X60)
subtype: null
tags: []
hardware_targets:
- SpacemiT K1
toolchains: []
constraints:
- RISC-V 64GCVB
- RVA22
- RISC-V Debug v0.13.2
- Dual-cluster octa-core X60 processors
- Power-islands and two-level power strategies
- LPDDR4/LPDDR4x up to 16GB, 2666Mbps
scorecard:
  novelty_delta: 0.7
  claim_density: 0.6
  self_containedness: 0.6
  bridge_score: 0.3
  hub_potential: 0.5
sources:
- raw/cache/8bdb883da88e7bfa.md
- https://docs.banana-pi.org/en/BPI-F3/SpacemiT_K1_datasheet
- raw/cache/fc87ec79ea2a4857.md
- https://www.cnx-software.com/2024/04/30/muse-book-laptop-spacemit-k1-octa-core-risc-v-ai-processor-16gb-ram/?trk=article-ssr-frontend-pulse_little-text-block
- raw/cache/c26eb4ccb070aed1.md
- https://wccftech.com/chinese-startup-unveils-first-risc-v-based-ai-cpu-powers-k1-domestic-laptop/
- raw/cache/bf951b75c4bed3ca.md
- http://wikidevi.wive-ng.ru/SpacemiT
source_url: https://docs.banana-pi.org/en/BPI-F3/SpacemiT_K1_datasheet
fetched_at: '2026-07-02T10:28:10.817365+00:00'
type: hardware_target
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# SpacemiT K1

The SpacemiT K1 is an octa-core RISC-V processor designed by SpacemiT, based on the RISC-V 64GCVB architecture and adhering to the RVA22 profile. It integrates dual-cluster X60 cores with support for up to 16GB of LPDDR4/LPDDR4x SDRAM at 2666Mbps. The chip features power-islands and two-level power strategies for each CPU core and cluster to achieve ultra power savings, and it complies with the RISC-V Debug v0.13.2 standard. Additionally, the K1 incorporates a neural processing unit delivering 2.0 TOPs of AI computing power, making it suitable for edge AI and industrial control applications.

## Key Claims

- RISC-V 64GCVB architecture, compliant with RVA22.
- Dual-cluster octa-core X60 processors.
- Supports up to 16GB LPDDR4/LPDDR4x at 2666Mbps.
- 2.0 TOPs AI computing power.
- RISC-V Debug v0.13.2.
- Power-islands and two-level power strategies.
- Used in the Banana Pi BPI-F3 development board.

## Optimization-Relevant Details

- ISA/profile: RISC-V 64GCVB, RVA22.
- Vector/matrix/accelerator support: AI accelerator providing 2.0 TOPs (specific microarchitecture not detailed).
- Memory/cache/TLB/DMA: LPDDR4/LPDDR4x up to 16GB, 2666Mbps, dual-chip select (further cache hierarchy not specified).
- Compiler/toolchain support: Not specified in source.

## Relationships

- [[banana-pi-bpi-f3]] (entity page for the board that uses this chip).
- [[cpa-factored-gemmini-systolic-array]] (related as an optimization recipe applicable to RISC-V AI accelerators; cross-link provided despite different page types).
- Insufficient context for additional cross-links; no existing entity pages for other RISC-V chips or board-level targets are present in the wiki context.

## Sources

- [Banana Pi BPI-F3 SpacemiT K1 RISC-V chip datasheet](https://docs.banana-pi.org/en/BPI-F3/SpacemiT_K1_datasheet)
