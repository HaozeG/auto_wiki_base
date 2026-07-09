---
canonical_name: Chipyard
aliases:
- CHIPYARD
- Chipyard Framework
- Chipyard SoC Generator
- Berkeley Chipyard
subtype: null
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.7
  self_containedness: 0.8
  bridge_score: 0.6
  hub_potential: 0.9
sources:
- raw/cache/f17d0eda7b9b0085.md
- https://github.com/ucb-bar/chipyard
- raw/cache/cc91cee5ef218478.md
- https://github.com/pku-liang/aps-chipyard
source_url: https://github.com/ucb-bar/chipyard
fetched_at: '2026-07-09T03:18:04.099896+00:00'
type: entity
created: '2026-07-09'
updated: '2026-07-09'
cold_start: true
inbound_links: 0
outbound_links:
- target: ara
  reason: Ara is a vector unit included in Chipyard as one of its optional accelerator
    components, implementing the RISC-V Vector Extension
---

# Chipyard

Chipyard is an open-source framework for agile development of Chisel-based systems-on-chip (SoCs) that integrates processor cores, vector units, accelerators, memory systems, peripherals, and tooling into a unified design flow. It is developed by the Berkeley Architecture Research Group at UC Berkeley and leverages the Chisel hardware construction language, the Rocket Chip SoC generator, and other Berkeley projects to produce RISC-V SoCs. Chipyard supports a range of processor cores including Rocket, BOOM, and CVA6, vector units such as Saturn and Ara, and accelerators like Gemmini and NVDLA. It enables multiple concurrent flows for agile hardware development, including software RTL simulation, FPGA-accelerated simulation via FireSim, automated VLSI flows through Hammer, and software workload generation with FireMarshal.

## Key Claims

- Chipyard is an open-source framework for Chisel-based SoC design.
- It includes processor cores: Rocket, BOOM, CVA6.
- It includes vector units: Saturn, Ara.
- It includes accelerators: Gemmini, NVDLA.
- It supports RTL simulation, FPGA simulation (FireSim), VLSI flows (Hammer), and workload generation (FireMarshal).
- It is developed by the Berkeley Architecture Research Group at UC Berkeley.

## Relationships

- [[ara]]: Ara is a vector unit included in Chipyard as one of its optional accelerator components, implementing the RISC-V Vector Extension.

## Sources

- [GitHub - ucb-bar/chipyard: An Agile RISC-V SoC Design Framework with in ...](raw/cache/f17d0eda7b9b0085.md)
