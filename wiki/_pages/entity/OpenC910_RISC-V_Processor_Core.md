---
cold_start: true
created: '2026-06-28'
inbound_links: 0
scorecard:
  bridge_score: 0.6
  claim_density: 0.7
  hub_potential: 0.4
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://deepwiki.com/XUANTIE-RV/openc910
tags:
- RISC-V
- T-Head
- open-source
- processor_core
- simulation
type: entity
updated: '2026-06-28'
---

# OpenC910 RISC-V Processor Core

The OpenC910 is an open-source RISC-V processor core developed by T-Head Semiconductor (a subsidiary of Alibaba Group) and released under a permissive license. The core is designed for high-performance computing and features a sophisticated architecture that includes multiple execution units such as an Integer Unit (IU), Vector Floating-Point Unit (VFPU), Cache Interface Unit (CIU), and Load/Store Unit (LSU). It supports multicore configurations and includes a cache coherence subsystem. The repository provides both the RTL source code (the C910 RTL Factory) and a complete simulation and testing infrastructure called smart_run, enabling developers to simulate, verify, and synthesize the core. The smart_run environment supports multiple simulators including Verilator, Icarus Verilog, VCS, and Cadence IUS, and integrates with the GNU toolchain for RISC-V. The OpenC910 is a significant open-source RISC-V implementation that can be used for research, education, and product development.

## Key Claims

- The OpenC910 is a RISC-V processor core developed by T-Head Semiconductor.
- The repository contains the C910 RTL Factory (Verilog source code) and the smart_run simulation environment.
- The core architecture includes Integer Unit, Vector Floating-Point Unit, Cache Interface Unit, and Load/Store Unit.
- It supports multicore configurations with cache coherence.
- The simulation environment supports Verilator (4.215+), Icarus Verilog, VCS, and Cadence IUS (irun).
- The development workflow uses the GNU toolchain for RISC-V.
- Waveform viewing is supported via Gtkwave and Verdi.

## Relationships

- [[Sipeed_MAIX_series]] – Both are RISC-V based platforms, though the Sipeed MAIX series targets edge AI with the Kendryte K210 while OpenC910 is a general-purpose core for higher-performance use.
- [[fpga-sdv_RISC-V_Vector_Cluster]] – Both represent RISC-V hardware targets with simulation and development environments, and both support vector processing capabilities.

## Sources

- [DeepWiki: XUANTIE-RV/openc910](https://deepwiki.com/XUANTIE-RV/openc910)

