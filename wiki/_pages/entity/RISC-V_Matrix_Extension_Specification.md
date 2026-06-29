---
cold_start: true
created: '2025-04-09'
inbound_links: 0
scorecard:
  bridge_score: 0.7
  claim_density: 0.6
  hub_potential: 0.5
  novelty_delta: 0.9
  self_containedness: 0.8
sources:
- https://github.com/XUANTIE-RV/riscv-matrix-extension-spec/
tags:
- RISC-V
- matrix extension
- XuanTie
- AI
- specification
type: entity
updated: '2026-06-29'
---

# RISC-V Matrix Extension Specification (XuanTie)

The RISC-V Matrix Extension Specification is a proposal for a matrix computation extension to the RISC-V instruction set architecture, developed by T-HEAD (XuanTie) to accelerate AI and machine learning workloads. Currently at version 0.6.0, this extension introduces tile registers for source operands and accumulation registers for destination operands, allowing flexible register shapes with adjustable numbers of rows and columns. It supports a range of matrix multiplication modes from pure outer products to pure inner products and adds new element-wise instructions for operator fusion. The specification is accompanied by a toolchain including a GNU compiler and assembler, a QEMU emulator with matrix support, a neural network library (SHL 2.0), a deployment toolkit (HHB), and demonstration applications for ResNet-50 and GEMM benchmarks. The extension is designed to complement the RISC-V Vector Extension and is available as an open-source project on GitHub.

## Key Claims

- Separated source (tile) and accumulation registers allow source and destination registers of different sizes.
- Adjustable number of rows and columns in matrix registers, not limited to rows = RLEN/32, enabling full coverage from pure outer products to pure inner products.
- New element-wise instructions have been added to facilitate operator fusion.
- The project includes SHL 2.0 (a neural network library using the matrix extension), HHB (a deployment toolkit), a QEMU emulator, and a GNU toolchain with matrix extension support.
- Provided demos include ResNet-50 evaluation and GEMM evaluation to demonstrate performance.
- Extension is currently in version 0.6.0 as a preview demo project, still under construction.

## Relationships

- [[GEMM_with_RISC-V_Vector_Extension]] – This workload kernel implements GEMM using the standard RISC-V Vector Extension; the matrix extension specification provides dedicated matrix operations that could potentially improve such implementations.
- [[XuanTie_C908_SHL_GEMM_Optimization]] – This optimization recipe for the XuanTie C908 uses an outer-product approach with register blocking; the matrix extension specification could enable more efficient matrix operations on compatible hardware.
- Note: insufficient context for additional cross-links to entity pages in the wiki context.

## Sources

- [XUANTIE-RV/riscv-matrix-extension-spec on GitHub](https://github.com/XUANTIE-RV/riscv-matrix-extension-spec/)

