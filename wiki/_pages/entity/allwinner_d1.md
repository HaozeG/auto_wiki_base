---
cold_start: true
created: 2026-06-27
inbound_links: 2
needs_summary_revision: true
scorecard:
  bridge_score: null
  claim_density: null
  hub_potential: null
  novelty_delta: null
  self_containedness: null
sources:
- https://docs.aw-ol.com/d1/en/
- https://www.cnx-software.com/2021/04/13/allwinner-d1-linux-risc-v-sbc-processor/
- https://linux-sunxi.org/Allwinner_Nezha
- https://linuxgizmos.com/17-sbc-runs-linux-on-allwinner-d1-risc-v-soc/
tags:
- risc-v
- SoC
- linux
- embedded
- allwinner
- mass-market
type: entity
updated: 2026-06-27
---

# Allwinner D1

Allwinner D1 is the first mass-market RISC-V application processor capable of running a full Linux distribution, announced by Allwinner Technology in 2021. It integrates a single T-Head XuanTie C906 64-bit RISC-V core running at up to 1 GHz, with support for the RISC-V Vector extension (RVV). The D1 targets AIoT and edge computing applications requiring Linux software compatibility at minimal cost, and spawned the Sipeed Nezha, the world's first mass-produced 64-bit RISC-V Linux single-board computer. Beyond the CPU, the D1-H variant includes a HiFi4 DSP, hardware H.264/H.265 video decode at up to 4K@30fps, and supports up to 2 GB DDR3 memory, making it unusually capable for a sub-$10 SoC die.

## Key Claims

- Allwinner D1 integrates a single XuanTie C906 RISC-V core at 1 GHz with 128-bit RVV support.
- Supports up to 2 GB DDR3 external memory via an integrated memory controller.
- Hardware video decode: H.265/H.264 up to 4K@30fps; MPEG-1/2/4 and JPEG up to 1080p@60fps.
- D1-H variant includes an embedded HiFi4 DSP for audio signal processing.
- Nezha development board retails at approximately $17 USD, making it the lowest-cost Linux-capable RISC-V board at launch.
- Sipeed Nezha was marketed as the world's first mass-produced 64-bit RISC-V Linux SBC.
- Official software support via Tina Linux (based on Linux 5.4 and U-Boot 2018) with mainline Linux community support via linux-sunxi.org.

## Relationships

- [[alibaba_xuantie_c910_c920]]: D1's C906 core is from the same T-Head XuanTie family as C910/C920 but is simpler and lower-power.
- [[risc_v_vector_extension]]: C906 implements an early RVV draft, providing 128-bit vector width for AI/DSP kernels.
- [[thead_th1520]]: TH1520 is the higher-end T-Head SoC with four C910 cores; D1 is the entry-level single-C906 sibling.
- [[beaglev_ahead]]: Both boards target the Linux RISC-V developer market; BeagleV-Ahead uses the more powerful TH1520.

## Sources

- https://docs.aw-ol.com/d1/en/
- https://www.cnx-software.com/2021/04/13/allwinner-d1-linux-risc-v-sbc-processor/
- https://linux-sunxi.org/Allwinner_Nezha
- https://linuxgizmos.com/17-sbc-runs-linux-on-allwinner-d1-risc-v-soc/
