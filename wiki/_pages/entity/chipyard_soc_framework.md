---
type: entity
tags: [risc-v, SoC-generator, open-source, UC-Berkeley, Chisel, EDA, research]
sources:
  - https://github.com/ucb-bar/chipyard
  - https://slice.eecs.berkeley.edu/projects/chipyard/
  - https://hc32.hotchips.org/assets/program/posters/HC2020.UCBerkeley.AlonAmid.v01.pdf
  - https://numfer.com/ucb-bar/chipyard
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

# Chipyard SoC Framework

Chipyard is an open-source, agile RISC-V SoC design and evaluation framework developed by the UC Berkeley Architecture Research (BAR / SLICE) lab, released under the Apache 2.0 license on GitHub. It provides a unified environment for integrating processor cores, vector units, accelerators, memory subsystems, and peripherals into a complete SoC, then simulating or taping out that design from a single coherent repository. Chipyard bundles in-order cores (Rocket), out-of-order cores (BOOM, CVA6/Ariane), vector units (Ara, Saturn), and accelerators (Gemmini, NVDLA) alongside a shared memory system and standard peripheral IP. The framework supports four parallel development flows: software RTL simulation via Verilator or VCS, FPGA-accelerated cycle-accurate simulation via FireSim on AWS EC2 F1 instances, automated VLSI flows via Hammer targeting TSMC and other processes, and workload generation for bare-metal and Linux systems via FireMarshal. All hardware is described in Chisel (a Scala-embedded HDL), enabling parameterized design: users specify core count, cache sizes, vector lane count, and accelerator configuration through Scala parameters without editing RTL manually. Chipyard has been used in numerous published research papers on RISC-V AI acceleration, processor microarchitecture, and memory subsystem design, and serves as the shared upstream for tools like Gemmini, FireSim, and BOOM.

## Key Claims

- Chipyard integrates Rocket, BOOM, CVA6, Ara, Saturn, Gemmini, and NVDLA as first-class configurable components.
- All hardware is written in Chisel (Scala-embedded HDL), enabling parameterized SoC generation without manual RTL editing.
- Supports four flows: Verilator/VCS simulation, FireSim FPGA simulation, Hammer VLSI, and FireMarshal workloads.
- FireSim integration allows cycle-accurate multi-node RISC-V cluster simulation on AWS EC2 F1 FPGAs.
- Released under the Apache 2.0 license at github.com/ucb-bar/chipyard with active UC Berkeley SLICE lab maintenance.
- Tenstorrent forked Chipyard to integrate its own RISC-V IP, demonstrating its role as an industry-accessible research platform.

## Relationships

- [[boom_riscv]]: BOOM (SonicBOOM) is developed within the Chipyard ecosystem and included as an OoO core option.
- [[gemmini]]: Gemmini is a Chipyard-integrated RISC-V AI accelerator attached via RoCC to Rocket or BOOM.
- [[firesim_fpga_simulation]]: FireSim is Chipyard's FPGA-accelerated simulation flow, tightly coupled to the framework.
- [[hwacha_vector_accelerator]]: Hwacha historical configurations remain available in Chipyard as reference designs.
- [[ara_vector_processor]]: Ara is included in Chipyard as a lane-scalable RVV 1.0 vector processor option.

## Sources

- https://github.com/ucb-bar/chipyard (source repository with README and documentation links)
- https://slice.eecs.berkeley.edu/projects/chipyard/ (SLICE lab project page)
- https://hc32.hotchips.org/assets/program/posters/HC2020.UCBerkeley.AlonAmid.v01.pdf (Hot Chips 2020 poster)
- https://numfer.com/ucb-bar/chipyard (Chipyard overview and component list)
