---
cold_start: false
created: '2026-06-27'
inbound_links: 0
scorecard:
  bridge_score: 0.5
  claim_density: 0.9
  hub_potential: 0.7
  novelty_delta: 0.8
  self_containedness: 0.7
sources:
- https://github.com/sophgocommunity/CV180-Duo
tags:
- Milk-V Duo
- Sophgo
- CV1800B
- embedded development
- RISC-V
- AIoT
- TPU
type: entity
updated: '2026-06-27'
---

# Milk-V Duo Development Board

The Milk-V Duo is an ultra-compact embedded development platform designed around the Sophgo CV1800B chip, which integrates two RISC-V C906 cores (one at 1 GHz and one at 700 MHz) along with 64 MB of RAM, a Tensor Processing Unit (TPU) for edge AI inference, and support for both Linux and RTOS dual-boot configurations. The board measures 21 mm by 51 mm and provides up to 26 GPIO pins, a MIPI CSI camera connector, a USB Type-C port for data and power, and a microSD slot for storage, with optional Ethernet via an add-on board. It is aimed at professionals, industrial ODMs, AIoT enthusiasts, DIY hobbyists, and creators as a low-cost, high-performance platform.

## Key Claims

- The Milk-V Duo is based on the Sophgo CV1800B system-on-chip featuring two RISC-V C906 cores: one running at 1 GHz and one at 700 MHz.
- It includes 64 MB of on-chip memory and supports both microSD card storage and an optional SD NAND solder pad.
- Connectivity includes one USB Type-C port for data/power, one USB2 solder pad, a 16-pin MIPI CSI 2-lane camera connector, and up to 26 GPIO pins.
- The board measures 21 mm × 51 mm and supports 10/100 Mbps Ethernet via a separate add-on board.
- It can run both Linux and RTOS (Real-Time Operating System) simultaneously, enabling dual-OS configurations.
- The CV1800B includes a Tensor Processing Unit (TPU) capable of accelerating AI inference models; a list of supported models is provided in the official resources.
- Official documentation, SDKs, and images are available from the Milk-V website and GitHub repositories, including a Buildroot-based SDK and hardware design files (schematics, PCB footprints, mechanical drawings).
- The Milk-V Duo is developed in partnership with Milk-V, a company that produces open-hardware development boards.

## Relationships

- [[sophgo_cv1800b]] — The Milk-V Duo is the primary development board based on the Sophgo CV1800B SoC.
- [[milk_v_company]] — Milk-V is the hardware partner and maintainer of the official SDK and documentation.
- [[risc_v_c906]] — Both CPU cores are RISC-V C906 designs from Alibaba's T-Head.
- [[ai_chip_export_controls]] — The CV1800B is a Chinese-designed chip from Sophgo, making it relevant to export control discussions; however, the board itself is not a high-performance AI accelerator and currently not subject to U.S. export restrictions.

## Sources

- GitHub README: sophgocommunity/CV180-Duo — Primary source for hardware specifications and links to official documentation.
- Milk-V Official Docs: https://milkv.io/docs/duo/overview
- CV180xB Datasheet (PDF): Provided in the GitHub repository.
- Duo Buildroot SDK: https://github.com/milkv-duo/duo-buildroot-sdk
