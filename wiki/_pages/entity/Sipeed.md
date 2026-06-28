---
cold_start: true
created: '2026-07-15'
inbound_links: 0
scorecard:
  bridge_score: 0.4
  claim_density: 0.8
  hub_potential: 0.5
  novelty_delta: 0.8
  self_containedness: 0.7
sources:
- https://wiki.sipeed.com/en/
tags:
- Sipeed
- RISC-V
- AI
- FPGA
- SBC
- development_board
type: entity
updated: '2026-06-28'
---

# Sipeed

Sipeed (Shenzhen Sipeed Technology Co., Ltd.) is a Chinese hardware company founded in 2015 that develops a range of open-source development boards, modules, and AI accelerators for edge computing, AIoT, and embedded systems. Their product portfolio includes the Classic Maix Vision Series and New Maix Ecosystem for AI vision, the Tang FPGA Series for programmable logic, the RISC-V SBC Series (LicheePi) and ARM SBC Series (LonganPi, LicheePi Zero/Nano), as well as accessory modules such as the NanoKVM and SLogic logic analyzer. The Maix series boards feature integrated NPUs ranging from 0.2 Tops to 3.2 Tops and support MaixPy, MaixCDK, and CSDK software frameworks. The Tang FPGA series is built around Gowin FPGA chips and includes models from the Nano 4K to the Mega 138K Pro with onboard DDR3 SDRAM and SoC integration. The RISC-V SBC series features processors from T-HEAD (C906, C910) and Allwinner, while the ARM SBC series uses Allwinner H618, V3S, and F1C100s processors.

## Key Claims

- The MaixCAM2 board features an AX630C dual-core ARM A53 processor and a 3.2 Tops NPU supporting INT4/INT8/INT16/BF16/FP16/FP32, achieving 113 FPS on YOLO11n 640x640.
- The MaixCAM board uses an SG2002 processor with a 1 Tops NPU, achieving 23 FPS on YOLO11n 640x640 and 95 FPS on 320x320.
- The Tang Mega 138K Pro FPGA board uses a GW5AST-138B FPGA with 138240 LUT4, 4Gb DDR3 SDRAM (x2), and a RISC-V AE350 SoC, supporting PCIe 3.0 and 12.5G transceivers.
- The LicheePi 4A RISC-V SBC features a TH1520 SoC with four C910 cores at 1.85 GHz, 8GB/16GB LPDDR4X, and a BXM-4-64 GPU with Vulkan 1.2 support.
- The LonganPi 3H ARM SBC uses an Allwinner H618 quad-core Cortex-A53 at 1.5 GHz, Mali-G31 GPU, and supports 4K H.264/H.265 video encode/decode.

## Relationships

- [[Sipeed_MAIX_series]] – The original MAIX series based on the Kendryte K210, complemented by the newer Maix ecosystem models.
- [[T-HEAD_C910_SPEC_CPU_Benchmark]] – Benchmark results for the C910 core used in the LicheePi 4A, one of Sipeed's RISC-V SBCs.

## Sources

- [Sipeed Wiki – Documentation](https://wiki.sipeed.com/en/)
