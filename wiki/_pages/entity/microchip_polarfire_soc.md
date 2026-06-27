---
type: entity
tags: [risc-v, FPGA, SoC, edge-AI, embedded, microchip, mi-v]
sources:
  - https://www.microchip.com/en-us/products/fpgas-and-plds/system-on-chip-fpgas/polarfire-soc-fpgas
  - https://www.eejournal.com/article/microchip-polarfire-and-the-imperative-of-the-intelligent-edge/
  - https://riscv.org/blog/microchips-polarfire-soc-fpga-meets-beagle-board-high-performance-soc-with-beaglev-fire/
  - https://www.microchip.com/en-us/about/media-center/blog/2025/polarfire-core-fpgas-and-socs
created: 2026-06-27
updated: 2026-06-27
cold_start: true
inbound_links: 0
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# Microchip PolarFire SoC (Mi-V RISC-V)

The Microchip PolarFire SoC is a family of non-volatile FPGA devices that combine a hard 64-bit RISC-V CPU cluster with reconfigurable FPGA fabric, targeting low-power, secure edge-AI and industrial-IoT applications. The hard CPU subsystem contains five RISC-V cores: four U54 application cores and one E51 monitor core, all running at up to 667 MHz and implementing the RV64GC ISA, enabling Linux and real-time RTOS execution simultaneously on the same device. The FPGA fabric reaches up to 460K logic elements, giving designers the ability to implement custom AI accelerators, neural network inference engines, or soft additional RISC-V cores alongside the hard CPU complex. Power consumption is up to 50% lower than comparable SRAM-based FPGAs due to PolarFire's flash-based non-volatile cell technology, which also eliminates configuration-loading overhead at power-up and reduces the attack surface for bitstream security. Microchip supports the family through its Mi-V RISC-V ecosystem, which bundles the Libero SoC design suite, the SmartHLS high-level synthesis tool, the VectorBlox Accelerator SDK for neural network IP, and a range of reference designs targeting object detection and industrial machine vision. The Icicle Kit and BeagleV-Fire (Beagleboard.org collaboration) are the two most widely available development platforms.

## Key Claims

- Hard CPU cluster: 4× U54 (RV64GC) application cores + 1× E51 monitor core at up to 667 MHz.
- FPGA fabric scales to 460K logic elements, supporting custom accelerator overlays alongside hard RISC-V cores.
- Flash-based non-volatile cells deliver up to 50% lower power than competing SRAM FPGAs.
- VectorBlox Accelerator SDK and Neural Network IP are available within the Mi-V ecosystem for edge-AI workloads.
- SmartHLS (high-level synthesis) supports C/C++ to hardware compilation targeting PolarFire SoC fabric.
- BeagleV-Fire is a publicly available $150 SBC combining PolarFire SoC with BeagleBone cape compatibility.

## Relationships

- [[chips_alliance_governance]]: Microchip participates in CHIPS Alliance and Mi-V ecosystem aligns with open RISC-V tooling.
- [[risc_v_profiles_rva]]: PolarFire SoC hard cores implement RV64GC, predating mandatory RVV of RVA23.
- [[starfive_jh7110_visionfive2]]: Both are RISC-V Linux SBCs targeting edge-AI; PolarFire SoC adds reconfigurable FPGA fabric.

## Sources

- https://www.microchip.com/en-us/products/fpgas-and-plds/system-on-chip-fpgas/polarfire-soc-fpgas (official product page)
- https://www.eejournal.com/article/microchip-polarfire-and-the-imperative-of-the-intelligent-edge/ (Mi-V ecosystem and AI capabilities)
- https://riscv.org/blog/microchips-polarfire-soc-fpga-meets-beagle-board-high-performance-soc-with-beaglev-fire/ (BeagleV-Fire partnership)
- https://www.microchip.com/en-us/about/media-center/blog/2025/polarfire-core-fpgas-and-socs (2025 PolarFire Core update)
