---
canonical_name: RISC-V Matrix Project
aliases:
- riscv-stc/riscv-matrix-project
- RISC-V Matrix Extension Project
- riscv-matrix-project
subtype: null
tags:
- RISC-V
- matrix extension
- prototype
- riscv-stc
scorecard:
  novelty_delta: 0.8
  claim_density: 0.4
  self_containedness: 0.6
  bridge_score: 0.7
  hub_potential: 0.8
sources:
- raw/cache/3fc6944a76be3486.md
- https://github.com/riscv-stc/riscv-matrix-project
source_url: https://github.com/riscv-stc/riscv-matrix-project
fetched_at: '2026-07-02T10:13:58.549286+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# RISC-V Matrix Project

The RISC-V Matrix Project is a demonstration and prototype implementation of matrix operation capabilities for RISC-V processors, hosted under the riscv-stc organization on GitHub. It serves as a top-level project aggregating several sub-modules: the matrix extension specification (riscv-matrix-spec), an LLVM toolchain with matrix extension support (llvm-project), the Spike ISA simulator (riscv-isa-sim) configured for matrix instructions, a Chipyard system-on-chip integration using the BOOM core (chipyard), an ISA verification suite (riscv-pvp-matrix), and a small deep neural network library (riscv-dnn) that exercises both the RISC-V Vector and Matrix extensions. The repository includes build instructions for compiling the LLVM and GNU toolchains, installing Spike, and running DNN operator and ResNet-50 tests on the simulator. The project is intended to advance the RISC-V matrix extension proposal by providing a complete prototyping stack from specification to software and hardware simulation.

## Key Claims

- The RISC-V Matrix Project is a demo project for proposing a RISC-V matrix extension.
- It comprises six sub-modules: specification (riscv-matrix-spec), LLVM toolchain (llvm-project), Spike ISS (riscv-isa-sim), Chipyard integration with BOOM core (chipyard), ISA verification (riscv-pvp-matrix), and a DNN library (riscv-dnn).
- The repository provides build instructions for LLVM and GNU toolchains, Spike installation, and running DNN operator and ResNet-50 tests.
- The project's TODO indicates plans to update modules to support the latest version of the proposal and add Chipyard simulation, verification, and prototype documentation.

## Relationships

- [[gemmini]]: Both Gemmini and the RISC-V Matrix Project target efficient matrix operations on RISC-V, though Gemmini is a hardware generator and this project focuses on an ISA extension.
- [[nncase]]: nncase is a compiler stack for RISC-V AI accelerators; the RISC-V Matrix Project's DNN library and toolchain support complement compiler-based optimization for matrix operations.
- [[cpa-factored-gemmini-systolic-array]]: An optimization recipe for a systolic array matrix multiplier, related to hardware acceleration of matrix operations similar to those targeted by the matrix extension.

## Sources

- [GitHub repository: riscv-stc/riscv-matrix-project](https://github.com/riscv-stc/riscv-matrix-project)
