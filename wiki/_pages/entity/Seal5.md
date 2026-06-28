---
cold_start: true
created: YYYY-MM-DD
inbound_links: 0
scorecard:
  bridge_score: 0.8
  claim_density: 0.8
  hub_potential: 0.6
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://www.computer.org/csdl/proceedings-article/dsd/2024/803800a335/21EtCMIsAHC
- https://github.com/tum-ei-eda/seal5
tags:
- RISC-V
- LLVM
- compiler
- ISA extension
- automation
type: entity
updated: '2026-06-28'
---

# Seal5

Seal5 is a semi-automated tool flow for generating LLVM compiler support for custom RISC-V instruction set architecture (ISA) extensions. Developed at the Technical University of Munich's Chair of Electronic Design Automation, Seal5 takes as input a description of custom instructions written in the CoreDSL2 ISA description language, a C-style language, and produces LLVM backend components including assembler support, builtin functions, and compiler code generation patterns. The tool is designed to accelerate the exploration of custom RISC-V instruction candidates by reducing the manual effort required to build software toolchain support, and it includes capabilities for autovectorization using the RISC-V Vector Extension. Seal5 is available as open-source software on GitHub under the tum-ei-eda/seal5 repository and has been presented at the 2024 Euromicro Conference on Digital System Design (DSD).

## Key Claims

- Semi-automated flow generates LLVM compiler support for custom RISC-V instructions from a CoreDSL2 ISA description.
- Generates assembler-level support, builtin functions, and compiler code generation patterns for scalar and vector instructions.
- Capable of autovectorization using the RISC-V Vector Extension (RVV).
- Open-source project hosted on GitHub at tum-ei-eda/seal5.
- Presented at the 2024 Euromicro Conference on Digital System Design (DSD).

## Relationships

- [[Sipeed_MAIX_series]] – Both are part of the RISC-V ecosystem; Seal5 could provide toolchain support for custom instructions on Sipeed hardware.

## Sources

- [Computer.org proceedings: Seal5: Semi-Automated LLVM Support for RISC-V ISA Extensions (DSD 2024)](https://www.computer.org/csdl/proceedings-article/dsd/2024/803800a335/21EtCMIsAHC)
- [GitHub repository: tum-ei-eda/seal5](https://github.com/tum-ei-eda/seal5)
