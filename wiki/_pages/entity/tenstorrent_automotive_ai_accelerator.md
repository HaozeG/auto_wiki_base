---
cold_start: false
created: '2026-06-26'
inbound_links: 0
scorecard:
  bridge_score: 0.8
  claim_density: 0.6
  contradiction_potential: 0.1
  gap_fill_score: 0.9
  hub_potential: 0.8
  novelty_delta: 0.9
  self_containedness: 0.7
sources:
- https://www.eenewseurope.com/en/tenstorrent-powers-first-automotive-risc-v-ai-accelerator-chiplet/
tags:
- risc-v
- ai-accelerator
- chiplet
- automotive
- tenstorrent
- tensix
type: entity
updated: '2026-06-26'
---

# Tenstorrent Automotive AI Accelerator (Eagle-N)

Tenstorrent, a Canadian AI computing startup, has provided its Tensix NPU core intellectual property for the development of the industry’s first automotive RISC-V AI accelerator chiplet, named Eagle-N, in collaboration with South Korean semiconductor company BOS Semiconductors. This chiplet targets automotive applications such as Advanced Driver Assistance Systems (ADAS) and In-Vehicle Infotainment (IVI) domain computing, combining the flexibility of the RISC-V instruction set architecture with Tenstorrent’s neural processing unit design. The Eagle-N chiplet is fabricated by Samsung Electronics, which secured a foundry order from Tenstorrent for this purpose. Beyond this specific product, Tenstorrent has been expanding its footprint in Japan and partnering with companies like LG to develop custom chips. The company’s solutions extend beyond AI accelerators and RISC-V processors, enabling integration of other companies’ FPGAs and memories as chiplet IP, and they offer evaluation boards and machines for automotive applications.

## Key Claims

- Eagle-N is the industry’s first automotive RISC-V AI accelerator chiplet, jointly developed by BOS Semiconductors and Tenstorrent.
- The chiplet uses Tenstorrent’s Tensix NPU core, tailored for automotive ADAS and IVI systems.
- Samsung Electronics has won a foundry order from Tenstorrent to fabricate the Eagle-N chiplet.
- Tenstorrent is expanding its presence in Japan, offering evaluation boards and machines for automotive use.
- Tenstorrent has partnered with LG to build custom AI chips.
- Tenstorrent’s chiplet ecosystem supports integration of external FPGAs and memories as chiplet IP.

## Relationships

- [[tenstorrent]]: Parent company providing the Tensix NPU core IP used in the Eagle-N chiplet; the automotive accelerator is part of Tenstorrent's commercial product portfolio.
- [[fpga_riscv_isa_extension_nn_inference]]: Both involve RISC-V-based AI acceleration; the existing page covers FPGA prototyping for edge inference, while Tenstorrent focuses on production chiplet solutions for automotive.
- [[risc_v_ai_ecosystem]]: Tenstorrent contributes a commercial RISC-V AI accelerator implementation and chiplet ecosystem to the broader RISC-V AI landscape.
- [[tensix_architecture]]: The Tensix NPU core is Tenstorrent’s proprietary neural processing architecture; future pages may detail its microarchitecture.

## Sources

- https://www.eenewseurope.com/en/tenstorrent-powers-first-automotive-risc-v-ai-accelerator-chiplet/
