---
canonical_name: Allwinner V851S
aliases:
- V851S
- V851s
- Yuzukilizard
- SoCXin V851S
- Allwinner V851S SoC
- Allwinner V851s
- V851SE
- Allwinner V851SE
subtype: null
tags:
- allwinner
- v851s
- yuzukilizard
- risc-v
- npu
hardware_targets:
- Allwinner V851S
- Yuzukilizard
toolchains:
- Tina Linux (OpenWrt-based)
- Docker SDK
constraints:
- Cortex-A7@900MHz
- RISC-V E907GC@600MHz
- 0.5 TOPS NPU (int8)
- 64MB DDR2
- 128MB SPI NAND
- XR829 WiFi/BT
- MIPI DSI up to 1280x720@60fps
- MIPI CSI 2-lane
- ISP max 2560x1440
- H.264/H.265 decode 4096x4096
- H.264/H.265 encode 3840x2160@20fps
scorecard:
  novelty_delta: 0.9
  claim_density: 0.6
  self_containedness: 0.8
  bridge_score: 0.5
  hub_potential: 0.2
sources:
- raw/cache/b8702cfd1eae4ccd.md
- https://github.com/SoCXin/V851S
- raw/cache/7e71e2d0a169636f.md
- https://github.com/Jebumon/v851s
- raw/cache/e982dc7bcda39259.md
- https://github.com/Jebumon/v851s/blob/master/README.md
- raw/cache/9c2ada1f1a993197.md
- https://linux-sunxi.org/V851s
source_url: https://github.com/SoCXin/V851S
fetched_at: '2026-07-03T14:58:27.912087+00:00'
type: hardware_target
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 0
---

# Allwinner V851S / Yuzukilizard

The Allwinner V851S is a heterogeneous system-on-chip (SoC) designed for IP camera applications, combining a single ARM Cortex-A7 core clocked at 900MHz, a RISC-V E907GC core clocked at 600MHz, and a 0.5 TOPS int8 neural processing unit (NPU). The SoC integrates 64MB of DDR2 memory and supports up to 128MB SPI NAND flash for storage. It is the basis for the Yuzukilizard development board, a small AI-powered heterogeneous platform that includes on-board XR829 WiFi and Bluetooth, a TF card slot supporting UHS-SDR104, a USB-to-UART bridge, connectors for MIPI DSI displays and MIPI CSI cameras, and a speaker amplifier. The V851S also features a high-performance ISP supporting resolutions up to 2560x1440, H.264/H.265 video encoding at 3840x2160@20fps and decoding at 4096x4096. The board runs the Tina Linux operating system, which is based on OpenWrt, and a Docker image is provided for SDK development.

## Key Claims

- Cortex-A7 core at 900MHz and RISC-V E907GC core at 600MHz provide heterogeneous compute.
- Integrated NPU delivers 0.5 TOPS at int8 precision for AI workloads such as human detection and crossing alarm.
- On-chip 64MB DDR2 memory and 128MB SPI NAND flash for storage.
- Built-in XR829 WiFi and Bluetooth with up to 150Mbps.
- Supports 2-lane MIPI DSI up to 1280x720@60fps and 2-lane MIPI CSI input.
- ISP supports a single input up to 2560x1440 resolution.
- H.264/H.265 decode at 4096x4096 and encode at 3840x2160@20fps at 400MHz.
- Runs Tina Linux (OpenWrt-based) and provides a Docker SDK image.
- Hardware design files licensed under CERN Open Hardware Licence Version 2 - Strongly Reciprocal.

## Optimization-Relevant Details

- **ISA/profile:**
  - Cortex-A7: ARMv7-A (32-bit)
  - E907GC: RISC-V (RV64GC, no vector extension advertised)
  - NPU: proprietary, int8-optimized
- **Vector/matrix/accelerator support:** 0.5 TOPS int8 NPU, no vector extensions on the RISC-V core.
- **Memory/cache/DMA:** 64MB DDR2 on-chip, 128MB SPI NAND, TF card slot (UHS-SDR104), USB, SDIO, Ethernet peripheral interfaces.
- **Compiler/toolchain support:** Tina Linux SDK, Docker image with prebuilt environment.

## Relationships

- Shares the RISC-V ISA family with the [[baby-llama2-milkv-duo-benchmark]] page's Milk-V Duo board, which uses the XuanTie C906 core; however, the E907GC on V851S is a microcontroller-class core without vector extensions, unlike the C906 that implements RVV 0.7.

## Sources

- https://github.com/SoCXin/V851S
