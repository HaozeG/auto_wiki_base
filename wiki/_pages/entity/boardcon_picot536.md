---
canonical_name: Boardcon PICOT536
aliases:
- PICOT536
- Boardcon PICOT536 SoM
- Boardcon EMT536
- EMT536 SBC
subtype: null
tags: []
scorecard:
  novelty_delta: 0.7
  claim_density: 0.8
  self_containedness: 0.9
  bridge_score: 0.4
  hub_potential: 0.3
sources:
- raw/cache/8a25f17099d5f27f.md
- https://www.cnx-software.com/2026/05/04/boardcon-picot536-som-and-emt536-sbc-feature-allwinner-t536-edge-ai-processor/
source_url: https://www.cnx-software.com/2026/05/04/boardcon-picot536-som-and-emt536-sbc-feature-allwinner-t536-edge-ai-processor/
fetched_at: '2026-07-02T03:50:08.241236+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# Boardcon PICOT536

Boardcon PICOT536 is a system-on-module (SoM) developed by Boardcon Technology, featuring the Allwinner T536 SoC with a quad-core Arm Cortex-A55 CPU, XuanTie E907 and XuanTie E902 RISC-V coprocessors, and a 2 TOPS neural processing unit (NPU) for edge AI workloads. The module supports up to 8GB LPDDR4/LPDDR4X memory with inline ECC, up to 64GB eMMC flash storage, and optional WiFi 6 and Bluetooth 5.4 connectivity via a VS6621S80 module. It exposes a wide range of interfaces through a 314-pin MXM 3.0 edge connector, including MIPI DSI, LVDS, dual MIPI CSI camera inputs, Gigabit Ethernet, PCIe, USB 3.0, and multiple UART, I2C, SPI, and GPIO lines. The PICOT536 is designed for industrial HMI, machine vision, robotics, and other edge computing applications that require a balance of CPU performance, RISC-V coprocessing, and AI acceleration.

## Key Claims

- Based on Allwinner T536 SoC (quad-core Cortex-A55 at 1.6 GHz, XuanTie E907 at 600 MHz, XuanTie E902 at 200 MHz).
- Integrates a 2 TOPS NPU supporting INT8, UINT8, and INT16 data types.
- Memory options: 2 GB, 4 GB, or 8 GB LPDDR4/LPDDR4X with inline ECC.
- Storage options: 8 GB, 16 GB, 32 GB, or 64 GB eMMC flash.
- Optional on-module WiFi 6 (802.11a/b/g/n/ac/ax) and Bluetooth 5.4 module.
- Form factor: 82 x 50 mm, 8-layer PCB.
- Operating temperature ranges: 0 to 70°C (commercial) and -40 to 85°C (industrial).
- Software support: Buildroot with Linux kernel 5.15.147 and U-Boot 2023.04, with cross-compilation toolchain.
- The companion EMT536 development board integrates the PICOT536 SoM and adds peripherals such as Gigabit Ethernet RJ45, M.2 NVMe support, mPCIe for 4G LTE, CAN bus, RS485, and additional USB ports.

## Relationships

The PICOT536 SoM is built around the Allwinner T536 SoC. The XuanTie E907 and E902 cores are part of the XuanTie family of RISC-V processor cores. The EMT536 SBC serves as a reference development platform for the SoM.

## Sources

- CNX Software article: https://www.cnx-software.com/2026/05/04/boardcon-picot536-som-and-emt536-sbc-feature-allwinner-t536-edge-ai-processor/
