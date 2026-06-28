---
cold_start: true
created: '2025-03-08'
inbound_links: 0
needs_summary_revision: false
scorecard:
  bridge_score: 0.7
  claim_density: 0.7
  hub_potential: 0.5
  novelty_delta: 0.8
  self_containedness: 0.8
sources:
- https://www.bitcraze.io/documentation/repository/aideck-gap8-examples/master/development/gap8/
tags:
- risc-v
- processor
- greenwaves
- pulp
- iot
type: entity
updated: '2026-06-28'
---

# Greenwaves GAP8

The GAP8 is a 9-core IoT application processor produced by Greenwaves Technologies, based on the RISC-V instruction set architecture and the PULP (Parallel Ultra-Low-Power Processing Platform) open-source platform. Designed for ultra-low-power edge AI and IoT applications, GAP8 integrates a fabric controller (FC) core and an 8-core cluster (CL) that share on-chip non-persistent memory divided into three levels: 16 kB of FC L1 memory, 64 kB of CL L1 memory, and 512 kB of shared L2 memory. External memory is supported via a HyperBus interface, providing 64 Mb of L3 RAM and additional flash. The processor is used on the Bitcraze AIdeck, where it interfaces with a camera through CPI, an ESP32 WiFi module via SPI, and an STM32 flight controller through UART and GPIOs, with data transfers offloaded to a micro DMA engine.

## Key Claims

- GAP8 contains nine RISC-V cores: one fabric controller (FC) for system management and peripheral access, and an 8-core cluster (CL) optimized for parallel data processing with shared L1 memory.
- On-chip memory consists of 16 kB FC L1, 64 kB CL L1, and 512 kB shared L2; all on-chip memory is non-persistent.
- External L3 memory is provided via a HyperBus interface, offering 64 Mb of RAM and additional flash.
- Key peripherals include CPI for camera, SPI for ESP32 WiFi module, and UART/GPIOs for STM32 flight controller; a micro DMA engine offloads data transfers from the FC.
- The GAP8 SDK (GAP SDK) provides compilation, programming, flashing, and neural network deployment tools, supporting operating systems like FreeRTOS via the autotiler and DORY as an alternative deployment framework.
- The Greenwaves website has been unavailable, preventing autotiler downloads; however, neural network deployment remains possible through DORY without the autotiler.

## Relationships

- [[risc_v_vector_extension]] — GAP8 is a RISC-V-based processor; while its cluster architecture differs from vector extensions, both represent RISC-V execution models relevant to the ecosystem.
- [[alibaba_xuantie_c910_c920]] — Both GAP8 and the XuanTie C910/C920 are RISC-V processors, but GAP8 targets ultra-low-power IoT with a 9-core asymmetric architecture, contrasting with the C910/C920's high-performance out-of-order design.
- insufficient context for additional cross-links

## Sources

- Bitcraze AIdeck GAP8 documentation: https://www.bitcraze.io/documentation/repository/aideck-gap8-examples/master/development/gap8/
