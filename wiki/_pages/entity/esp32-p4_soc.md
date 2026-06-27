---
cold_start: false
created: '2026-06-26'
inbound_links: 0
scorecard:
  bridge_score: 0.3
  claim_density: 0.6
  hub_potential: 0.4
  novelty_delta: 0.5
  self_containedness: 0.9
sources:
- https://www.espressif.com/en/products/socs/esp32-p4
tags:
- espressif
- soc
- risc-v
- embedded
- hmi
type: entity
updated: '2026-06-27'
---

# ESP32-P4 SoC

The ESP32-P4 is a high-performance system-on-chip (SoC) developed by Espressif Systems, designed for demanding embedded applications requiring robust human-machine interfaces (HMI), edge computing, and extensive IO connectivity. It is powered by a dual-core RISC-V CPU running at up to 400 MHz, featuring single-precision floating-point unit (FPU) and AI instruction extensions, alongside a low-power core (LP-Core) operating at up to 40 MHz. The SoC integrates 768 KB of on-chip SRAM, 8 KB of zero-wait TCM RAM, and supports MIPI-CSI with an integrated image signal processor (ISP) and MIPI-DSI for high-resolution display and camera interfaces up to 1080p. It includes hardware accelerators for H.264 encoding at 1080p@30fps, a pixel processing accelerator (PPA), 2D-DMA, and a rich set of peripherals including 55 programmable GPIOs, USB OTG 2.0 HS, Ethernet, and SDIO Host 3.0, making it suitable for a wide range of IoT and multimedia applications.

## Key Claims

- The ESP32-P4 is powered by a dual-core RISC-V CPU with a maximum clock speed of 400 MHz, supporting single-precision FPU and AI instruction extensions.
- It includes a low-power core (LP-Core) running at up to 40 MHz for ultra-low-power operation while the high-performance cores remain dormant.
- The HP core system includes 768 KB of on-chip SRAM, usable as cache when external PSRAM is available, plus 8 KB of zero-wait TCM RAM.
- Supports MIPI-CSI with integrated ISP and MIPI-DSI, handling up to 1080p resolution for both display and camera interfaces.
- Integrates hardware accelerators for H.264 encoding with a maximum performance of 1080p@30fps.
- Includes a hardware Pixel Processing Accelerator (PPA) and 2D-DMA for GUI development.
- Offers 55 programmable GPIOs, the highest count among Espressif SoCs.
- Supports USB OTG 2.0 HS, Ethernet, and SDIO Host 3.0 for high-speed connectivity.
- Additional peripherals include SPI, I2S, I2C, LED PWM, MCPWM, RMT, ADC, UART, and TWAI™.

## Relationships

- No directly related pages currently exist in the wiki; this page serves as the primary reference for the ESP32-P4 SoC.

## Sources

- https://www.espressif.com/en/products/socs/esp32-p4
