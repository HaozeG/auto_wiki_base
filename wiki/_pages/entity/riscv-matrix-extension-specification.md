---
canonical_name: RISC-V Matrix Extension Specification
aliases:
- RISC-V Matrix Extension
- riscv-matrix-extension
- Matrix Extension Specification
- Xuantie Matrix Extension
- Xuantie-RV Matrix Extension
- RISC-V Matrix Extension Proposal V0.6.0
- Xuantie RV Matrix Extension
- riscv-matrix-extension-spec
- RV Matrix Extension v0.4.0
- T-Head Matrix Extension
- RVM extension
- RV matrix extension
- RISC-V matrix extension spec
- RVME
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
- raw/cache/9425b98e97b53c45.md
- https://github.com/XUANTIE-RV/riscv-matrix-extension-spec
- raw/cache/b852143582393cff.md
- https://github.com/XUANTIE-RV/riscv-matrix-extension-spec/tree/v0.4.0
- raw/cache/03efd9e471335133.md
- https://github.com/XUANTIE-RV/riscv-matrix-extension-spec/blob/master/demos/README.md
- raw/cache/4a3d1a40a7af9a4e.md
- https://github.com/XUANTIE-RV/riscv-matrix-extension-spec/
source_url: https://deepwiki.com/riscv-stc/riscv-matrix-project/4.1-matrix-extension-specification
fetched_at: '2026-07-03T13:51:11.299731+00:00'
type: entity
created: '2026-07-03'
updated: '2026-07-06'
cold_start: true
inbound_links: 0
---

# RISC-V Matrix Extension Specification

The RISC-V Matrix Extension Specification defines foundational ISA extensions for matrix operations within the RISC-V ecosystem, serving as an authoritative reference for implementing matrix computation across the entire toolchain from compiler to hardware. It is a standalone extension, proposed for AI applications, highly inspired by the RISC-V vector extension, but does not require vector support; it uses the Zmv extension to exchange matrix data between vector registers and memory, and between vector registers and matrix registers. The specification is currently at version 0.6.0 and is under active development by Alibaba's T-Head (Xuantie), with ongoing collaboration with Damo Academy since May 2023. The first version v0.1 was submitted in September 2022. Key architectural features include separation of source (tile) and accumulation registers of different sizes, adjustable matrix register shapes (rows and columns independent, supporting configurations from pure outer products to pure inner products), and new element-wise instructions to facilitate operator fusion. The software ecosystem includes LLVM and GNU toolchains (GCC, binutils), Spike ISS simulator, QEMU emulator with matrix extension support, the SHL 2.0 neural network library, the HHB model deployment toolkit, the GEM5-RVME simulator providing a detailed microarchitectural model, an ABI manual, and an intrinsic API reference manual. Evaluation demos for ResNet50 and GEMM kernels are provided. The specification documents are built using AsciiDoctor and can be generated as PDFs; the repository is a preview demo project under construction. The matrix extension is intended to enhance RISC-V capabilities for high-performance AI chips and stream computing, and is supported by hardware implementations such as Chipyard with the BOOM core.

## Key Claims

- The RISC-V Matrix Extension Specification defines foundational ISA extensions for matrix operations in RISC-V, currently at version 0.6.0, proposed for AI applications.
- It serves as the authoritative reference for implementing matrix computation across the entire toolchain from compiler to hardware.
- The specification is a standalone extension, highly inspired by the RISC-V vector extension but does not require vector support; it uses the Zmv extension for data exchange.
- Key architectural features: separation of source (tile) and accumulation registers, adjustable matrix register shapes (rows and columns independently configurable, covering pure outer products to pure inner products), and new element-wise instructions for operator fusion.
- The project includes toolchain support: LLVM compiler, GNU toolchain (GCC, binutils), Spike ISS simulator, QEMU emulator with matrix extension, SHL 2.0 neural network library, HHB deployment toolkit, GEM5-RVME simulator, an ABI manual, and an intrinsic API reference manual.
- Version v0.1 of the specification was completed and submitted in September 2022.
- Collaboration with Damo Academy (Alibaba) to jointly explore the RISC-V matrix instruction set began in May 2023.
- Evaluation demos for ResNet50 and GEMM are provided. The repository is a preview demo project; the specification is still under construction and documents are built with AsciiDoctor.
- The matrix extension is intended to enhance RISC-V capabilities for high-performance AI chips and stream computing, and is supported by hardware implementations such as Chipyard with the BOOM core.

## Relationships

- [[xuantie-c906-hardware-target]]: The XuanTie C906 core uses custom SIMD instructions but does not implement the RISC-V Matrix Extension; the Matrix Extension is a separate proposal that may target future XuanTie cores for matrix-intensive AI workloads.
- [[mlir-xdsl-rvv-codegen-pipeline]]: Both target AI computation on RISC-V; the MLIR-xDSL pipeline generates RVV code for GEMM kernels, while the Matrix Extension proposes dedicated matrix instructions that could complement or replace vector-based approaches for similar workloads.
- [[spacemit-x60-hardware-target]]: The SpacemiT X60 implements RVV 1.0 for vector operations; the Matrix Extension proposes a complementary matrix-level instruction set not yet supported on the X60, representing a different approach to AI acceleration on RISC-V.

## Sources

- https://deepwiki.com/riscv-stc/riscv-matrix-project/4.1-matrix-extension-specification
- https://github.com/XUANTIE-RV/riscv-matrix-extension-spec
