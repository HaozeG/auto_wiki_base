---
canonical_name: Allwinner V851s
aliases:
- V851s
- Allwinner V851S
- V851S
subtype: null
tags:
- allwinner
- ip-camera
- risc-v
- arm-cortex-a7
- npu
hardware_targets:
- Allwinner V851s
toolchains:
- Tina Linux
- FreeRTOS
constraints:
- Arm Cortex-A7 up to 900MHz
- RISC-V XuanTie E907 up to 600MHz
- 0.5 TOPS NPU (INT8)
- SiP 64MB DDR
- H.265/H.264 video encoding up to 4M@30fps
- H.264 video decoding up to 4M@30fps
- Parallel CSI 10-bit
- MIPI CSI 2*2-lane
- MIPI-DSI, RGB888, BT656 display output
- USB 2.0 DRD
- GMAC
- SMHC*3
- UART*4
- TWI*5
- SPI*4
- PWM*11
- GPADC
- GPIO*6
scorecard:
  novelty_delta: 0.8
  claim_density: 0.7
  self_containedness: 0.8
  bridge_score: 0.6
  hub_potential: 0.5
sources:
- raw/cache/163ffb16268e271b.md
- https://www.allwinnertech.com/index.php?c=product&a=index&id=118
source_url: https://www.allwinnertech.com/index.php?c=product&a=index&id=118
fetched_at: '2026-07-01T06:48:54.173276+00:00'
type: hardware_target
created: '2026-07-01'
updated: '2026-07-01'
cold_start: true
inbound_links: 1
needs_summary_revision: false
---

# Allwinner V851s

The Allwinner V851s is a high-performance, low-power system-on-chip (SoC) designed for professional smart IP camera applications. It integrates an Arm Cortex-A7 CPU running at up to 900 MHz, a RISC-V MCU based on the XuanTie E907 core operating at up to 600 MHz, and a 0.5 TOPS neural processing unit (NPU) for on-device AI inference tasks such as human detection and crossing alarm. The chip incorporates a self-developed video codec engine supporting H.265/H.264 encoding up to 4M@30fps and H.264 decoding, a high-performance ISP image processor, and a suite of peripheral interfaces including USB 2.0 DRD, GMAC Ethernet, multiple SPI, I2C, UART, and PWM controllers. The V851s includes an integrated 64 MB DDR memory in a system-in-package (SiP) configuration, enabling compact board designs for network cameras and smart vision devices. The SoC is supported by Allwinner's Tina Linux distribution and FreeRTOS real-time operating system.

## Key Claims

- Arm Cortex-A7 CPU up to 900 MHz.
- RISC-V MCU (XuanTie E907) up to 600 MHz.
- NPU with 0.5 TOPS (INT8) performance.
- SiP 64 MB DDR memory.
- H.265/H.264 video encoding up to 4M@30fps.
- Video decoding: H.264 4M@30fps; JPEG up to 16384x16384.
- Camera interfaces: Parallel CSI (10-bit), MIPI CSI (2x2-lane).
- Display interfaces: MIPI-DSI, RGB888, BT656.
- Peripheral interfaces: USB 2.0 DRD, GMAC, 3x SMHC, 4x UART, 5x TWI, 4x SPI, 11x PWM, GPADC, 6x GPIO.
- Software support: Tina Linux and FreeRTOS.

## Optimization-Relevant Details

- ISA/profile: ARMv7-A (Cortex-A7), RISC-V (XuanTie E907). The E907 is a 32-bit RISC-V core; specific ISA extensions are not publicly detailed.
- Vector/matrix/accelerator support: 0.5 TOPS NPU (INT8), no explicit vector processing unit.
- Memory/cache/TLB/DMA: Integrated 64MB DDR (likely DDR2/DDR3 or similar), cache hierarchy details not provided in the source.
- Compiler/toolchain support: Tina Linux (Linux distribution based on OpenWrt) and FreeRTOS; standard GCC/LLVM toolchains for Arm and RISC-V targets.

## Relationships

- The V851s integrates a [[xuantie_c908]] related XuanTie RISC-V MCU core (E907) from T-Head Semiconductor. The C908 page describes the vector extension and optimization techniques for the same processor family.
- The [[xuantie_c908_fp16_gemm_kernel]] workload kernel documents a GEMM micro-kernel for a related XuanTie core (C908), providing insight into the kind of optimization patterns that could be adapted for RISC-V software stacks on the V851s.

## Sources

- https://www.allwinnertech.com/index.php?c=product&a=index&id=118
