---
type: entity
tags:
  - risc-v
  - open-source
  - cpu
  - superscalar
  - out-of-order
  - chisel
  - berkeley
sources:
  - https://github.com/riscv-boom/riscv-boom
  - https://boom-core.org/
  - https://arxiv.org/abs/1702.04776
created: 2026-06-27
updated: 2026-06-27
cold_start: false
inbound_links: 0
scorecard:
  novelty_delta: 0.82
  claim_density: 0.79
  self_containedness: 0.87
  bridge_score: 0.62
  hub_potential: 0.58
---

# Berkeley BOOM (Berkeley Out-of-Order Machine)

The Berkeley Out-of-Order Machine (BOOM) is an open-source, parameterizable superscalar out-of-order RISC-V processor generator developed at UC Berkeley and the University of California, Santa Cruz. Written in Chisel HDL, BOOM implements the full RV64GC ISA with speculative execution, a reorder buffer (ROB), register renaming via a unified physical register file, a load/store queue (LSQ), and configurable branch prediction (TAGE predictor). BOOM's generator-based design allows single-source instantiation of cores ranging from SmallBOOM (2-wide, 64-entry ROB) to MediumBOOM (3-wide) and LargeBOOM (4-wide, 128-entry ROB, 20-stage pipeline), targeting Dhrystone performance competitive with ARM Cortex-A75 for LargeBOOM. The core is a foundational component of the Berkeley RISC-V ecosystem and the primary OoO reference for the Chipyard SoC generator framework. BOOM is notable as the open-source OoO RISC-V processor with the most academic publications, having been used to study branch prediction, memory hierarchy, cache side-channel vulnerabilities (Spectre/Meltdown RISC-V demonstrations), and as the host CPU in Gemmini-based AI accelerator SoCs. Tape-outs of BOOM-based SoCs have been demonstrated in TSMC 28 nm through the BWRC fabrication program.

## Key Claims

- LargeBOOM (4-wide issue, 128-entry ROB) achieves approximately 3.91 IPC on SPEC CPU2006 integer benchmarks in simulation, and synthesizes to 1.5–2.0 GHz in a commercial 28 nm process.
- BOOM implements a TAGE (TAgged GEometric history length) branch predictor with configurable history tables, achieving miss-prediction rates below 5% on most integer benchmarks.
- The Chisel generator produces both FPGA bitstreams (targeting Xilinx VCU118, FireSim simulation) and tape-out-ready RTL, verified against a single parameterized source.
- BOOM has been demonstrated booting Linux with the full RV64GC software stack, including SMP multi-core configurations (dual-BOOM SoC).
- The Gemmini systolic-array accelerator attaches to a BOOM host CPU via RoCC (Rocket Custom Coprocessor) interface, forming a complete ML inference SoC used in Berkeley AI research.
- FireSim, a cloud FPGA simulation framework, uses BOOM as its primary DUT (device under test), enabling cycle-accurate performance modeling of BOOM-based data center nodes at 1 MHz effective clock.
- BOOM's ROB-based speculation model was used in the first published RISC-V demonstration of Spectre variant 1 (2019), validating its microarchitectural fidelity as a research platform.

## Relationships

- [[gemmini]] — Gemmini attaches to a BOOM core via the RoCC accelerator interface; together they form the standard Berkeley RISC-V AI accelerator SoC reference design.
- [[cva6_ariane_riscv]] — CVA6 and BOOM represent complementary open-source RISC-V CPU designs; CVA6 is simpler in-order for prototyping, BOOM is OoO for performance research.
- [[pulp_platform_riscv]] — PULP and BOOM share the Chisel heritage (both use Scala-based hardware generators) but target different market segments (edge ultra-low-power vs. application-class performance).
- [[risc_v_vector_extension]] — A vectorized BOOM variant (BOOM+V) has been prototyped with RVV 1.0, targeting HPC workloads.
- [[rva23_profile]] — BOOM aims to implement the RVA23 mandatory and recommended extensions, including Zicntr, Zihpm, and Svnapot.

## Sources

- BOOM GitHub repository: https://github.com/riscv-boom/riscv-boom
- Celio et al., "The Berkeley Out-of-Order Machine (BOOM): An Industry-Competitive, Synthesizable, Parameterized RISC-V Processor," UC Berkeley Tech Report, 2015: https://arxiv.org/abs/1702.04776
- Chipyard SoC framework: https://github.com/ucb-bar/chipyard
- FireSim FPGA simulation platform: https://fires.im/
