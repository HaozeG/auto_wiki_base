---
canonical_name: XuanTie E907
aliases:
- E907
- XuanTie E907 processor
subtype: null
tags:
- e907
- risc-v
- xuantie
hardware_targets:
- XuanTie E907
toolchains: []
constraints:
- 16/32-bit mixed instruction set
- Five-stage integer pipeline
- Configurable FPU (single or single+double precision)
- Configurable DSP unit
scorecard:
  novelty_delta: 0.9
  claim_density: 0.6
  self_containedness: 0.8
  bridge_score: 0.2
  hub_potential: 0.5
sources:
- raw/cache/a50cb3adec26b2bf.md
- https://www.segger.com/supported-devices/xuantie/e907/
source_url: https://www.segger.com/supported-devices/xuantie/e907/
fetched_at: '2026-07-01T06:47:31.995758+00:00'
type: hardware_target
created: '2026-07-01'
updated: '2026-07-01'
cold_start: true
inbound_links: 1
needs_summary_revision: false
---

# XuanTie E907

The XuanTie E907 is a RISC-V-based high-performance embedded microprocessor developed by T-Head Semiconductor (XuanTie), designed for MCU-class applications such as voice processing, MPU, navigation, and WiFi. It adopts a 16/32-bit mixed instruction set and implements a classic five-stage integer pipeline. The processor can be configured with a floating-point unit (FPU) supporting single-precision or single+double precision, or a digital signal processor (DSP) unit. The E907 is positioned as the highest-performance processor in the XuanTie RISC-V MCU product line, and has been integrated into heterogeneous systems along with ARM Cortex-A55 cores in products such as the Forlinx embedded platform. SEGGER development tools support the E907 family including the E907F and E907FD variants.

## Key Claims

- Adopts 16/32-bit mixed instruction set for flexible encoding.
- Implements a classic five-stage integer pipeline.
- Configurable FPU supporting single precision or single+double precision, or a DSP unit.
- Targets applications in voice, MPU, navigation, and WiFi domains.
- Supported by SEGGER for device families E907, E907F, and E907FD.
- Integrated in Forlinx Embedded product alongside quad-core Cortex-A55 at 1.6 GHz and 2 TOPS NPU.

## Optimization-Relevant Details

- ISA/profile: RISC-V with 16/32-bit mixed instruction set, five-stage pipeline.
- Vector/matrix/accelerator support: None specified; optional FPU/DSP.
- Memory/cache/TLB/DMA: (not specified)
- Compiler/toolchain support: Not specified beyond SEGGER support.

## Relationships

- [[xuantie_c908]] (both XuanTie RISC-V processor families)

Insufficient context for additional cross-links.

## Sources

- https://www.segger.com/supported-devices/xuantie/e907/
- XuanTie_E907_Datasheet_20251017 (xmosc.org.cn)
- RT-Thread GitHub: rt-thread/bsp/xuantie/smartl/e907
- Forlinx Embedded 2025 Product Recap
