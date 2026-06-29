---
cold_start: true
created: '2026-07-02'
inbound_links: 0
scorecard:
  bridge_score: 0.7
  claim_density: 0.6
  hub_potential: 0.9
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://github.com/ucb-bar/chipyard
tags:
- RISC-V
- SoC
- framework
- agile hardware
- UC Berkeley
type: entity
updated: '2026-06-29'
---

# Chipyard Framework

Chipyard is an open-source framework for agile development of Chisel-based systems-on-chip (SoCs), developed by the Berkeley Architecture Research Group at the University of California, Berkeley. It integrates the Chisel hardware construction language, the Rocket Chip SoC generator, and numerous Berkeley projects to produce full-featured RISC-V SoCs with MMIO-mapped peripherals, custom accelerators, and memory systems. The framework includes a range of processor cores such as Rocket, BOOM, and CVA6 (Ariane), vector units like Saturn and Ara, accelerators including Gemmini and NVDLA, and supports multiple concurrent development flows: software RTL simulation, FPGA-accelerated simulation via FireSim, automated VLSI flows using Hammer, and software workload generation with FireMarshal for bare-metal and Linux-based systems. Chipyard is designed to enable rapid design-space exploration and full-stack evaluation of deep-learning and general-purpose workloads on customizable RISC-V platforms.

## Key Claims

- Chipyard is an open-source framework for agile development of Chisel-based RISC-V SoCs.
- It integrates processor cores: Rocket, BOOM, CVA6 (Ariane); vector units: Saturn, Ara; accelerators: Gemmini, NVDLA; and memory systems.
- Supports multiple concurrent flows: software RTL simulation, FPGA-accelerated simulation (FireSim), automated VLSI flows (Hammer), and software workload generation (FireMarshal).
- Developed by the Berkeley Architecture Research Group at UC Berkeley.
- Allows users to produce full SoCs with MMIO-mapped peripherals and custom accelerators.
- Supports both bare-metal and Linux-based workload execution.

## Relationships

- [[Sipeed_MAIX_series]] – Both are RISC-V platforms, though Sipeed MAIX is a development board while Chipyard is a design framework for custom SoCs.
- Insufficient context for additional cross-links to entity pages; only one entity page (Sipeed_MAIX_series) is present in the current wiki.

## Sources

- [GitHub - ucb-bar/chipyard](https://github.com/ucb-bar/chipyard)

