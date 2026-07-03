---
canonical_name: RISC-V Matrix Extension Specification
aliases:
- RISC-V Matrix Extension
- riscv-matrix-extension
- Matrix Extension Specification
subtype: null
tags:
- risc-v
- isa
- matrix
- extension
scorecard:
  novelty_delta: 0.85
  claim_density: 0.6
  self_containedness: 0.8
  bridge_score: 0.3
  hub_potential: 0.7
sources:
- raw/cache/69ba79650d1c86b5.md
- https://deepwiki.com/riscv-stc/riscv-matrix-project/4.1-matrix-extension-specification
source_url: https://deepwiki.com/riscv-stc/riscv-matrix-project/4.1-matrix-extension-specification
fetched_at: '2026-07-03T13:51:11.299731+00:00'
type: entity
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 0
---

# RISC-V Matrix Extension Specification

The RISC-V Matrix Extension Specification defines the foundational Instruction Set Architecture (ISA) extensions that enable matrix operations within the RISC-V ecosystem. It serves as the authoritative reference for implementing matrix computation capabilities across the entire toolchain, from compiler support to hardware implementation. The specification is a standalone extension, highly inspired by the RISC-V vector extension, but does not require vector extension support; it uses the Zmv extension to bridge matrix and vector data exchange between vector registers and memory as well as between vector and matrix registers. The project includes a complete open-source toolchain ecosystem with LLVM, GNU toolchain, and Spike ISS support, and is developed within the riscv-stc/riscv-matrix-project. The first version v0.1 was submitted in September 2022, with ongoing collaboration with Damo Academy since May 2023. The matrix extension is intended to enhance RISC-V capabilities for high-performance AI chips and stream computing, and is supported by hardware implementations such as Chipyard with the BOOM core.

## Key Claims

- The Matrix Extension Specification defines foundational ISA extensions for matrix operations in RISC-V.
- It serves as the authoritative reference for implementing matrix computation across the entire toolchain from compiler to hardware.
- The specification is a standalone extension, highly inspired by the RISC-V vector extension but does not require vector support.
- It uses the Zmv extension to exchange matrix data between vector registers and memory, and between vector registers and matrix registers.
- The project includes toolchain support: LLVM compiler, GNU toolchain, and Spike ISS simulator.
- Version v0.1 of the specification was completed and submitted in September 2022.
- Collaboration with Damo Academy (Alibaba) to jointly explore the RISC-V matrix instruction set began in May 2023.
- The matrix extension is intended to enhance RISC-V AI chip capabilities, specifically for stream computing in high-performance AI chips.

## Relationships

No specific relationship to visible context pages.

## Sources

- https://deepwiki.com/riscv-stc/riscv-matrix-project/4.1-matrix-extension-specification
