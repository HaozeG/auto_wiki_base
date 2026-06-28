---
cold_start: true
constraints:
- RVV 1.0
- INT8/INT16
- dual-core heterogeneous (1.6GHz + 0.8GHz)
- KPU with INT8/INT16
- DPU 3D structured light up to 1920x1080
- VPU H.264/H.265 encode/decode up to 4096x4096
- JPEG codec up to 8K
- MIPI CSI (up to 3 lanes)
- MIPI DSI (1x4/1x2)
- 'interfaces: 5xUART, 5xI2C, 6xPWM, 64+8 GPIO, 2xUSB 2.0, 2xSD/eMMC, 3xSPI, WDT/RTC/Timer'
created: '2025-03-25'
hardware_targets:
- K230
inbound_links: 1
scorecard:
  bridge_score: 0.5
  claim_density: 0.85
  hub_potential: 0.7
  novelty_delta: 0.9
  self_containedness: 0.95
sources:
- https://www.kendryte.com/en/proDetail/230
tags:
- RISC-V
- AIoT
- Kendryte
- K230
toolchains:
- CanMV (Micropython)
- RT-Smart SDK
- Linux SDK
- Linux + RT-Smart SDK
type: hardware_target
updated: '2026-06-28'
---

# Kendryte K230 SoC

The Kendryte K230 is a RISC-V-based AIoT (Artificial Intelligence of Things) system-on-chip (SoC) designed by Kendryte for edge-side intelligent applications. It integrates a heterogeneous dual-core RISC-V processor complex: CPU 1 operates at 1.6 GHz with 32 KB I-cache, 32 KB D-cache, 256 KB L2 cache, and supports the 128-bit RISC-V Vector Extension (RVV 1.0), while CPU 0 runs at 0.8 GHz with 32 KB I-cache, 32 KB D-cache, and 128 KB L2 cache. The chip includes a Neural Processing Unit (KPU) supporting INT8 and INT16 inference with typical performance of ResNet-50 at 85+ fps, MobileNet_v2 at 670+ fps, and YOLOv5S at 38+ fps (all at INT8). The DPU provides a 3D structured light depth engine supporting up to 1920x1080 resolution. The VPU encodes and decodes H.264/H.265 streams up to 4096x4096 at 20 fps encoding and 40 fps decoding, and the JPEG codec supports resolutions up to 8192x8192. The SoC supports MIPI CSI camera input (up to 3 lanes) and MIPI DSI display output (up to 1920x1080@60fps). On-chip interfaces include 5 UART, 5 I2C, 6 PWM, 64 plus 8 PMU GPIO, 2 USB 2.0 OTG, 2 SD/eMMC controllers, 3 SPI (one OSPI and two QSPI), WDT, RTC, and timers. Software support includes the CanMV Micropython SDK, RT-Smart SDK, Linux SDK, and a dual-core Linux + RT-Smart SDK. The K230 is positioned as the successor to the K210, claiming up to 13.7x the reasoning capability for typical networks.

## Key Claims

- Dual-core RISC-V: CPU 1 at 1.6 GHz with RVV 1.0, CPU 0 at 0.8 GHz.
- KPU supports INT8 and INT16 with typical performance: ResNet-50 ≥85 fps, MobileNet_v2 ≥670 fps, YOLOv5S ≥38 fps (INT8).
- DPU: 3D structured light depth engine, max resolution 1920x1080.
- VPU: H.264/H.265 encode up to 3840x2160@20fps, decode up to 3840x2160@40fps; JPEG codec up to 8192x8192.
- Display: MIPI DSI (1x4 or 1x2) supports 1920x1080@60fps.
- Camera input: MIPI CSI (max 1x4 + 1x2 or 3x2 lanes).
- Multiple SDKs: CanMV (Micropython), RT-Smart, Linux, and Linux+RT-Smart dual-core.
- Claims 13.7x reasoning capability compared to K210 under typical networks.

## Relationships

- [[Chiplet_RISC_V_AI_SoC_Benchmark_Results]] – Benchmark results for a different RISC-V AI SoC, providing context for comparison with the K230's claimed performance.
- [[DSC_Fused_Dataflow_Benchmark_Results]] – Benchmark results for a RISC-V-based TinyML accelerator using Depthwise Separable Convolutions, related to the edge AI application space of the K230.
- Insufficient context for additional cross-links to entity pages in the available wiki context.

## Sources

- [K230 product page – Kendryte](https://www.kendryte.com/en/proDetail/230)
