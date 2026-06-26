---
cold_start: true
created: '2026-07-01'
inbound_links: 0
scorecard:
  bridge_score: null
  claim_density: null
  hub_potential: null
  novelty_delta: null
  self_containedness: null
sources:
- github_riscv_vme
tags:
- risc-v
- matrix-extension
- specification
type: entity
updated: '2026-07-01'
---

# RISC-V Vector Matrix Extension (VME)

The RISC-V Vector Matrix Extension (VME) is a proposed instruction set extension for the RISC-V architecture that adds matrix operations on top of the existing vector extension (RVV). VME defines new instructions for matrix load and store, matrix multiply-accumulate (MMAC), and element-wise matrix operations, enabling efficient hardware acceleration of linear algebra kernels common in machine learning inference, scientific computing, and signal processing. The specification is maintained in the riscv-vme GitHub repository under the RISC-V organization, and it is part of a broader family of RISC-V matrix extensions that includes the Integer Matrix Extension (IME) and the Arithmetic Matrix Extension (AME). VME targets applications requiring mixed-precision and low-latency matrix computation, and it is designed to leverage the existing vector register file and instruction encoding space. The extension is still under development and has not yet been ratified as an official RISC-V standard. This page documents the VME specification as hosted in the referenced repository.

## Key Claims

- The riscv-vme GitHub repository contains the specification for the RISC-V Vector Matrix Extension.
- VME defines instructions for matrix load/store, matrix multiply-accumulate, and element-wise operations.
- VME builds upon the RISC-V Vector Extension (RVV) and uses the vector register file.
- The extension is part of a family including IME and AME, targeting different precision and compute characteristics.
- The specification is maintained under the RISC-V GitHub organization and is in the proposal stage.

## Relationships

- [[fpga_riscv_isa_extension_nn_inference]]: FPGA-based prototypes of RISC-V matrix acceleration; VME represents a standardized approach to such extensions.
- [[risc_v_vector_extension]]: VME is built on top of the vector extension and extends it with matrix operations.
- [[riscv_ai_ecosystem]]: VME contributes to the RISC-V AI acceleration ecosystem by providing standardized matrix instructions.

## Sources

- github_riscv_vme: GitHub page for the riscv-vme repository (https://github.com/riscv/riscv-vme).

