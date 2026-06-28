---
cold_start: false
created: 2026-06-27
inbound_links: 0
needs_summary_revision: false
scorecard:
  bridge_score: null
  claim_density: null
  hub_potential: null
  novelty_delta: null
  self_containedness: null
sources:
- https://www.sifive.com/boards/hifive-unleashed
- https://www.sifive.com/boards/hifive-unmatched
- https://linuxgizmos.com/updated-hifive-unmatched-sbc-showcases-new-fu740-risc-v-soc/
- https://www.phoronix.com/review/hifive-unmatched-benchmarks/2
tags:
- risc-v
- developer-board
- linux
- sifive
- FU540
- FU740
type: entity
updated: 2026-06-27
---

# SiFive HiFive Unleashed and HiFive Unmatched

The SiFive HiFive Unleashed (2018) and HiFive Unmatched (2021) are the two landmark Linux-capable RISC-V development boards from SiFive that enabled the first generation of native RISC-V OS and application development. The HiFive Unleashed was the world's first commercially available Linux-capable RISC-V board, powered by the SiFive Freedom U540 (FU540) SoC featuring four U54 application cores (RV64GC) plus one S51 monitor core, 8 GB DDR4, and Gigabit Ethernet; it ran Linux via the Freedom U-SDK and was instrumental in bootstrapping the RISC-V software ecosystem. The HiFive Unmatched succeeded it with the SiFive Freedom U740 (FU740) SoC, upgrading to four U74 dual-issue superscalar application cores plus one S71 monitor core, 16 GB DDR4, PCIe x16, USB 3.2 Gen1, M.2 NVMe and Wi-Fi/BT slots in a 170×170 mm mini-ITX form factor. The Unmatched became the canonical RISC-V PC-class board for Linux distribution porting: Fedora, Debian, Ubuntu, and OpenEmbedded all gained official Unmatched support. Although neither board includes a GPU or dedicated AI accelerator, their PCIe slots allowed GPU add-in cards and positioned them as the first general-purpose RISC-V development machines capable of compiling large code-bases natively.

## Key Claims

- HiFive Unleashed (2018) was the first commercially available Linux-capable RISC-V development board, using the FU540 SoC.
- FU540 integrates four RV64GC U54 cores plus one S51 monitor core and 8 GB DDR4.
- HiFive Unmatched (2021) uses the FU740 SoC with four U74 dual-issue superscalar cores and one S71 monitor core.
- Unmatched provides a PCIe x16 slot, USB 3.2 Gen1, M.2 M-key NVMe, and M.2 E-key Wi-Fi/BT in mini-ITX (170×170 mm).
- Fedora, Debian, Ubuntu RISC-V, and OpenEmbedded Yocto all provide official images for HiFive Unmatched.
- FireSim (FPGA-accelerated simulation) and other UC Berkeley tools were validated on FU540/FU740-class reference designs.

## Relationships

- [[sifive_intelligence_x280]]: SiFive's AI-focused X280 and P870/X390 lines descend from the same IP portfolio that produced the U54/U74 cores.
- [[risc_v_profiles_rva]]: FU540/FU740 cores predate RVA22/23 profiles; they established the baseline Linux-capable RISC-V platform.
- [[chipyard_soc_framework]]: Chipyard's Rocket core (basis for U54/U74) is the open-source upstream of SiFive's commercial cores.

## Sources

- https://www.sifive.com/boards/hifive-unleashed (official Unleashed product page)
- https://www.sifive.com/boards/hifive-unmatched (official Unmatched product page)
- https://linuxgizmos.com/updated-hifive-unmatched-sbc-showcases-new-fu740-risc-v-soc/ (FU740 specs)
- https://www.phoronix.com/review/hifive-unmatched-benchmarks/2 (benchmark results)
