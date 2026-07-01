---
canonical_name: Allwinner T536
aliases:
- T536
- FET536-C
- FET536-C SoM
- Allwinner T536 industrial processor
subtype: null
tags:
- allwinner
- risc-v
- arm
- npu
- industrial
hardware_targets:
- Allwinner T536
toolchains: []
constraints:
- Quad-core Cortex-A55 @ 1.6GHz
- Xuantie E907 RISC-V MCU @ 600MHz
- Xuantie E902 low-power RISC-V MCU
- 2 TOPS NPU
- Secure boot
- Full-path ECC
- AMPRT (Asymmetric Multi-Processing)
- ISP 8MP @ 30fps, WDR, 3DNR
- 'Interfaces: USB, SDIO, UART, SPI, CAN-FD, Ethernet, ADC, LocalBus (16-bit @ 100MHz
  or 32-bit @ 50MHz)'
- Industrial grade components
scorecard:
  novelty_delta: 0.7
  claim_density: 0.6
  self_containedness: 0.8
  bridge_score: 0.4
  hub_potential: 0.3
sources:
- raw/cache/4732299fa1005290.md
- https://www.forlinx.net/industrial-news/allwinner-t536-industrial-embedded-riscv-mcu-669.html
source_url: https://www.forlinx.net/industrial-news/allwinner-t536-industrial-embedded-riscv-mcu-669.html
fetched_at: '2026-07-01T06:50:50.458710+00:00'
type: hardware_target
created: '2026-07-01'
updated: '2026-07-01'
cold_start: true
inbound_links: 1
needs_summary_revision: false
---

# Allwinner T536

The Allwinner T536 is an industrial-grade system-on-chip (SoC) that integrates a quad-core ARM Cortex-A55 application processor running at up to 1.6 GHz, a 64-bit Xuantie E907 RISC-V microcontroller core for real-time control at up to 600 MHz, and a secondary Xuantie E902 RISC-V core for low-power management. It includes a built-in neural processing unit (NPU) delivering 2 TOPS of integer inference performance, supporting edge machine learning workloads. The SoC is designed for industrial applications and features secure boot, full-path error-correcting code (ECC) memory, asymmetric multiprocessing (AMPRT), an integrated image signal processor (ISP) capable of 8 MP at 30 fps with WDR and 3DNR, and a comprehensive set of connectivity interfaces including USB, SDIO, UART, SPI, CAN-FD, Ethernet, ADC, and a parallel LocalBus interface. The T536 targets data concentrators, FTU, DTU, EV charging stations, transportation robots, and industrial control systems. It is commercially available through Forlinx Embedded as the FET536-C system-on-module, which exposes all SoC pins and provides a development platform with support for Linux RT, FreeRTOS, and bare-metal code.

## Key Claims

- Quad-core ARM Cortex-A55 CPU at 1.6 GHz with 64-bit architecture.
- 64-bit Xuantie E907 RISC-V MCU at 600 MHz for real-time tasks.
- Secondary Xuantie E902 RISC-V MCU for ultra-low-power management.
- 2 TOPS NPU for edge inference.
- Secure boot and full-path ECC memory.
- AMPRT (asymmetric multiprocessing) support for mixed-criticality workloads.
- ISP with 8 MP @ 30 fps, WDR, and 3DNR.
- Parallel LocalBus interface (16-bit @ 100 MHz or 32-bit @ 50 MHz).
- Industrial-grade design with extended temperature range components.
- Software support for Linux RT, FreeRTOS, and bare-metal.

## Optimization-Relevant Details

- ISA/profile: ARMv8.2-A (Cortex-A55); RV64GC (Xuantie E907, no vector extension confirmed).
- Vector/matrix/accelerator support: 2 TOPS NPU (exact ISA not disclosed); no RISC-V vector unit specified.
- Memory/cache/TLB/DMA: Not publicly detailed for on-chip hierarchy; external DDR and LocalBus are exposed.
- Compiler/toolchain support: Linux RT, FreeRTOS, bare-metal development; Arm and RISC-V toolchains required for heterogeneous builds.

## Relationships

- Xuantie E907 is a sibling core from T-Head Semiconductor, related to the higher-performance [[xuantie_c908]] core.
- As an industrial RISC-V-Arm hybrid SoC, the T536 targets similar application domains as other heterogeneous platforms, e.g., the K230-based designs referenced in the RISC-V AI accelerator ecosystem, linking conceptually to designs like [[rvme]] for broader context on RISC-V matrix acceleration.
- The primary module implementation is the FET536-C system-on-module by Forlinx Embedded.

## Sources

- https://www.forlinx.net/industrial-news/allwinner-t536-industrial-embedded-riscv-mcu-669.html
