---
cold_start: false
created: '2026-06-27'
inbound_links: 0
needs_summary_revision: false
scorecard:
  bridge_score: 0.7
  claim_density: 0.9
  hub_potential: 0.5
  novelty_delta: 0.9
  self_containedness: 0.8
sources:
- https://github.com/redoop/riscv-bitnet-accelerator
tags:
- risc-v
- ai-accelerator
- open-source
- bitnet
- soc
- edge-ai
type: entity
updated: '2026-06-27'
---

# SimpleEdgeAiSoC

SimpleEdgeAiSoC is an open-source System-on-Chip designed for edge AI inference, integrating a PicoRV32 RISC-V processor with BitNet multiplier-free accelerators. Developed by redoop, it targets low-power edge applications with a compact design, achieving 6.4 GOPS at 100 MHz while consuming under 100 mW. The SoC includes peripherals such as UART, SPI-based TFT LCD controller, SPI Flash, and PSRAM, and has been synthesized on ICS55 55nm process with a core area of approximately 0.3 mm². It supports both iEDA and OpenROAD toolchains, and is released under Apache 2.0 license.

## Key Claims

- Integrates PicoRV32 RV32I RISC-V processor with BitNet multiplier-free accelerators.
- BitNet architecture uses ternary weights {-1, 0, +1} for multiplier-free design.
- Achieves 6.4 GOPS at 100 MHz; measured operating frequency up to 178.569 MHz.
- Target power consumption less than 100 mW; static power measured at 627.4 μW.
- Core area approximately 0.3 mm² with 73,829 instances.
- Supports both iEDA (Chinese) and OpenROAD (International) ASIC toolchains.
- v0.2 release (2025-11-16) adds RealUART, TFTLCD (ST7735), bootloader, graphics library, Python tools, and 5 example programs with 97% test coverage.
- v0.3 release (2025-12-03) adds 16 MB SPI Flash and 8 MB PSRAM, increasing storage capacity by 375×.
- v0.4.1 release (2025-12-03) reduces IO pads from 97 to 61 (37% reduction) to meet 81-pad limit.
- Clock verification confirms 100 MHz main clock and 10 MHz SPI clock with 100% test pass rate.
- ASIC synthesis on ICS55 55nm PDK yields 623,516-line netlist, 292,992 μm² chip area, 96,087 standard cells, including 25,553 flip-flops.
- Integrated with ysyxSoC platform for full SoC validation.

## Relationships

- [[gemmini]]: Gemmini and SimpleEdgeAiSoC are both open-source RISC-V-based AI accelerators but differ fundamentally in approach: Gemmini uses a systolic array of MAC units for general DNN inference, while SimpleEdgeAiSoC employs multiplier-free BitNet accelerators with ternary weights for extreme low-power edge inference.
- [[risc_v_vector_extension]]: RVV provides a standardized SIMD vector processing extension for RISC-V, complementing the dedicated accelerator approach of SimpleEdgeAiSoC by offering programmable vector lanes for portable inference across different hardware.
- [[alibaba_xuantie_c910_c920]]: The XuanTie cores are general-purpose RISC-V CPUs with vector extensions, whereas SimpleEdgeAiSoC integrates a minimal PicoRV32 core with specialized AI accelerators, targeting different design points (performance vs. ultra-low-power).

## Sources

- https://github.com/redoop/riscv-bitnet-accelerator
