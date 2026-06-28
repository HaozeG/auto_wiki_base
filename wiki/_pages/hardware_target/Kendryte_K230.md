---
cold_start: true
constraints:
- 'CPU 1: 1.6GHz, 32KB I-cache, 32KB D-cache, 256KB L2 Cache, 128-bit RVV 1.0'
- 'CPU 0: 0.8GHz, 32KB I-cache, 32KB D-cache, 128KB L2 Cache'
- 'KPU: INT8/INT16, Resnet50 >=85fps, Mobilenet_v2 >=670fps, YoloV5S >=38fps'
- 'DPU: 3D structured light depth engine up to 1920x1080'
- 'VPU: H.264/H.265 encode/decode up to 4096x4096'
- JPEG codec up to 8K
- 'MIPI CSI: up to 3 lanes (1x4lane + 1x2lane or 3x2lane)'
- 'Display: 1x4 or 1x2 MIPI DSI, max 1920x1080@60fps'
- 'Interfaces: 5xUART, 5xI2C, 6xPWM, 64+8 GPIO, 2xUSB 2.0, 2xSD, 3xSPI, WDT/RTC/Timer'
created: YYYY-MM-DD
hardware_targets:
- K230
inbound_links: 0
scorecard:
  bridge_score: 0.5
  claim_density: 0.8
  hub_potential: 0.3
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://www.kendryte.com/en/proDetail/230
tags:
- RISC-V
- AIoT
- Kendryte
- K230
- NPU
toolchains: []
type: hardware_target
updated: '2026-06-28'
---

# Kendryte K230

The Kendryte K230 is the latest generation system-on-chip (SoC) from the Kendryte series, designed for end-side AIoT (Artificial Intelligence of Things) applications using a dual-core RISC-V architecture. The K230 integrates a high-performance CPU 1 core operating at 1.6 GHz with 32KB I-cache, 32KB D-cache, 256KB L2 cache, and 128-bit RVV 1.0 vector extension, along with a secondary CPU 0 core at 0.8 GHz with 32KB I-cache, 32KB D-cache, and 128KB L2 cache. The chip features a dedicated KPU (Neural Processing Unit) supporting INT8 and INT16 inference, achieving typical network performance of Resnet50 at ≥85 fps, Mobilenet_v2 at ≥670 fps, and YoloV5S at ≥38 fps at INT8 precision. Additional processing units include a DPU for 3D structured light depth sensing up to 1920×1080 resolution, a VPU for H.264/H.265 encoding and decoding up to 4096×4096 resolution, and a JPEG codec supporting up to 8K resolution. The K230 also provides rich on-chip interfaces including MIPI CSI for camera input, MIPI DSI for display output, multiple UART, I2C, PWM, GPIO, USB 2.0, SD/eMMC, and SPI interfaces. Software support includes MicroPython, RT-Smart, and Linux SDKs, making the chip suitable for edge computing, smart cameras, robotics, and open-source hardware.

## Key Claims

- Dual-core RISC-V architecture: CPU 1 at 1.6 GHz with RVV 1.0 vector extension, CPU 0 at 0.8 GHz.
- KPU supports INT8 and INT16 with benchmarked performance: Resnet50 ≥85fps, Mobilenet_v2 ≥670fps, YoloV5S ≥38fps at INT8.
- DPU for 3D structured light depth processing at up to 1920×1080 resolution.
- VPU supports H.264/H.265 encode up to 3840×2160@20fps and decode up to 3840×2160@40fps; JPEG codec up to 8192×8192.
- Display output via MIPI DSI up to 1920×1080@60fps.
- On-chip interfaces: 5xUART, 5xI2C, 6xPWM, 64+8 GPIO, 2xUSB 2.0 OTG, 2xSD/eMMC, 3xSPI (1 OSPI + 2 QSPI), WDT/RTC/Timer.
- Software SDKs: MicroPython, RT-Smart (C/C++), Linux (C/C++), and Linux+RT-Smart dual-core heterogeneous system.

## Optimization-Relevant Details

- ISA/profile: RISC-V 64-bit with RVV 1.0 extension on CPU 1.
- Vector/matrix/accelerator support: 128-bit RVV 1.0 on CPU 1; dedicated KPU for neural network acceleration.
- Memory/cache/TLB/DMA: CPU 1: 32KB I-cache, 32KB D-cache, 256KB L2 cache; CPU 0: 32KB I-cache, 32KB D-cache, 128KB L2 cache.
- Compiler/toolchain support: MicroPython firmware, RT-Smart SDK (C/C++), Linux SDK (C/C++); specific compiler versions not detailed in source.

## Relationships

- [[Sipeed_MAIX_series]] – Prior-generation development platform based on the Kendryte K210, providing context for K230’s improved performance and capabilities.
- [[T-HEAD_C910_SPEC_CPU_Benchmark]] – Another high-performance RISC-V chip benchmark, useful for cross-chip performance comparisons.
- Insufficient context for additional cross-links to other entity pages.

## Sources

- [Kendryte K230 product page](https://www.kendryte.com/en/proDetail/230)
