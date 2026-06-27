---
type: entity
tags: [risc-v, verification, co-simulation, NEMU, difftest, XiangShan, open-source]
sources:
  - https://github.com/OpenXiangShan/NEMU
  - https://xiangshan-doc-en.readthedocs.io/en/latest/tools/nemu/
  - https://github.com/OpenXiangShan/XiangShan
  - https://arxiv.org/pdf/2601.11838
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

# OpenXiangShan Ecosystem: Difftest and NEMU

The OpenXiangShan project (ICT-CAS) developed a specialized processor verification ecosystem centered on two tools: NEMU and Difftest. NEMU (NJU Emulator) is a high-performance RISC-V ISA emulator originally designed for teaching at Nanjing University and subsequently extended to serve as XiangShan's golden reference model. NEMU supports RV64GC and is orders of magnitude faster than RTL simulation, making it practical as a cycle-accurate behavioral reference during hardware verification. Difftest is a co-simulation framework that runs the RTL implementation and NEMU side-by-side, comparing processor state at every instruction commit; any divergence halts simulation and pinpoints the first incorrect microarchitectural state. This approach differs from the BOOM/Rocket toolchain which uses Spike as its reference model — XiangShan chose NEMU for tighter integration and faster iteration. Difftest operates at the RTL level using Verilator-compiled C++ simulation, with NEMU providing the reference; it supports both simulation and FPGA emulation modes via FireSim. A known risk of co-simulation is that bugs shared between the DUT and reference model can go undetected; the XiangShan team documented cases where bugs appeared in both XiangShan and NEMU simultaneously. The SimFuzz fuzzing framework (2025) builds on Difftest infrastructure to perform block-level mutation-based fuzzing of RISC-V processor implementations. These tools have been open-sourced and are reused by other Chinese RISC-V processor projects beyond XiangShan.

## Key Claims

- NEMU: high-speed RISC-V ISA emulator (originally NJU teaching tool) used as XiangShan's golden reference model.
- Difftest: co-simulation framework that compares RTL and NEMU at every instruction commit; divergence triggers halt and diagnosis.
- XiangShan uses NEMU as reference (not Spike); tighter integration enables faster bug turnaround than Spike-based comparison.
- Difftest runs via Verilator C++ RTL simulation and supports FPGA emulation through FireSim.
- Co-simulation has a known blind spot: bugs shared between DUT and NEMU cannot be detected — documented in practice.
- SimFuzz (2025) extends Difftest infrastructure with mutation-based fuzzing for RISC-V processor verification.
- Difftest and NEMU are fully open-source and reused by other Chinese open-source RISC-V processor projects.

## Relationships

- [[xiangshan_riscv]]: Difftest and NEMU are the primary verification tools developed for and around the XiangShan processor.
- [[boom_riscv]]: BOOM uses Spike as its reference model — the alternative co-simulation approach vs. XiangShan's NEMU/Difftest.
- [[ara_vector_processor]]: Ara uses a different verification methodology (formal + simulation); Difftest is specific to scalar OoO pipelines.

## Sources

- https://github.com/OpenXiangShan/NEMU
- https://xiangshan-doc-en.readthedocs.io/en/latest/tools/nemu/
- https://github.com/OpenXiangShan/XiangShan
- https://arxiv.org/pdf/2601.11838
