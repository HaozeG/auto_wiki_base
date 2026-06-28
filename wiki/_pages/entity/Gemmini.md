---
cold_start: true
created: YYYY-MM-DD
inbound_links: 0
needs_summary_revision: false
scorecard:
  bridge_score: 0.7
  claim_density: 0.8
  hub_potential: 0.6
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://github.com/ucb-bar/gemmini/blob/master/README.md
tags:
- RISC-V
- DNN
- accelerator
- Chipyard
- Chisel
type: entity
updated: '2026-06-28'
---

# Gemmini

Gemmini is an open-source, full-system and full-stack deep neural network (DNN) hardware exploration and evaluation platform developed at UC Berkeley as part of the Chipyard ecosystem. It is implemented using the Chisel hardware description language as a RoCC (Rocket Custom Coprocessor) accelerator that connects to the memory system via the System Bus of a Rocket or BOOM RISC-V tile. The accelerator is built around a configurable systolic array that performs matrix multiplications and supports both output-stationary and weight-stationary dataflows, selectable by the programmer. Gemmini enables architects to study how different system components, beyond the accelerator itself, interact to affect overall DNN performance, and provides a rapid evaluation path through cycle-accurate simulators like Verilator and VCS, as well as the FPGA-accelerated FireSim platform.

## Key Claims

- Gemmini is a full-system, full-stack DNN hardware exploration and evaluation platform.
- Developed using the Chisel hardware description language and part of the Chipyard ecosystem.
- Implemented as a RoCC accelerator with non-standard RISC-V custom instructions.
- Connects via the RoCC port of a Rocket or BOOM tile; by default to the memory system through the System Bus (directly to L2 cache).
- Features a systolic array at its core for matrix multiplications.
- Supports output-stationary and weight-stationary dataflows, selectable at runtime.
- Can be built and simulated with Verilator, VCS, and FireSim (FPGA-accelerated simulation).
- Supports running large DNN models like ResNet50 on cycle-accurate simulators.
- Provides a functional simulator via Spike and a cycle-accurate simulator for performance profiling.
- Includes performance counters for profiling workloads.
- Offers tutorials from MLSys 2022 and IISWC 2021 for building diverse accelerators and adding custom datatypes.

## Relationships

- [[Sipeed_MAIX_series]] – Another RISC-V platform targeting edge AI, providing context for comparison of AI acceleration approaches.
- [[T-HEAD_C910_SPEC_CPU_Benchmark]] – A RISC-V CPU benchmark result that can be used to compare the general-purpose performance of cores that Gemmini accelerators attach to.
- [[GEMM_with_RISC-V_Vector_Extension]] – A vector-based GEMM kernel that contrasts with Gemmini's systolic array approach for similar matrix multiplication operations.

## Sources

- [GitHub: Gemmini README](https://github.com/ucb-bar/gemmini/blob/master/README.md)
