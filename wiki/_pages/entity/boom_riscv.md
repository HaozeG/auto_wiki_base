---
cold_start: true
created: 2026-06-27
inbound_links: 0
needs_summary_revision: true
scorecard:
  bridge_score: null
  claim_density: null
  hub_potential: null
  novelty_delta: null
  self_containedness: null
sources:
- https://github.com/riscv-boom/riscv-boom
- https://boom-core.org/
- https://docs.boom-core.org/en/latest/sections/intro-overview/boom.html
- https://www2.eecs.berkeley.edu/Pubs/TechRpts/2017/EECS-2017-157.html
tags:
- risc-v
- open-source
- out-of-order
- uc-berkeley
- research
- chisel
type: entity
updated: 2026-06-27
---

# BOOM (Berkeley Out-of-Order Machine)

BOOM (Berkeley Out-of-Order Machine), also known as SonicBOOM in its third generation, is a synthesizable, parameterizable, open-source out-of-order RISC-V processor core developed at UC Berkeley's Architecture Research group. Implemented in Chisel and integrated into the Chipyard SoC framework, BOOM serves as the primary academic vehicle for out-of-order microarchitecture research in the open-source RISC-V ecosystem. Its design draws heavily from the MIPS R10000 and Alpha 21264 processors and uses a unified physical register file with precise exceptions and tomasulo-style register renaming.

## Key Claims

- SonicBOOM (BOOMv3) achieves 6.2 CoreMarks/MHz, making it performance-competitive with commercial high-performance out-of-order cores in the same pipeline class.
- Supports RV64GC ISA including atomics and IEEE 754-2008 floating-point; parameterizable issue width, ROB size, physical register counts, and branch predictor configurations.
- Uses a unified physical register file microarchitecture (inspired by MIPS R10000 and Alpha 21264), contrasting with reservation-station designs.
- FPGA simulation runs at 90+ MHz on Amazon EC2 F1 instances via the FireSim flow, enabling large-scale architectural evaluation.
- Written entirely in Chisel, enabling rapid parameterized design-space exploration from in-order to deeply out-of-order configurations without RTL rewrite.
- Three named generations: BOOMv1 (initial), BOOMv2 (improved branch prediction and execution), SonicBOOM/BOOMv3 (current, performance-competitive).
- Integrated with Gemmini for AI acceleration experiments — host BOOM CPU issues RoCC instructions to the Gemmini systolic array co-processor.

## Relationships

- [[gemmini]]: BOOM serves as the host RISC-V CPU for Gemmini in Chipyard; issues RoCC instructions to trigger systolic array operations.
- [[xiangshan_riscv]]: XiangShan and BOOM are the two leading open-source out-of-order RISC-V designs; XiangShan targets higher peak performance, BOOM targets research flexibility.
- [[risc_v_vector_extension]]: BOOM can be paired with vector co-processors; BOOMv3 itself does not include integrated vector lanes.

## Sources

- GitHub: https://github.com/riscv-boom/riscv-boom
- Homepage: https://boom-core.org/
- Documentation: https://docs.boom-core.org/en/latest/sections/intro-overview/boom.html
- Technical report BOOMv2: EECS-2017-157, UC Berkeley
