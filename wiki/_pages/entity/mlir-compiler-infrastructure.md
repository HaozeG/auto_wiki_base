---
canonical_name: MLIR
aliases:
- Multi-Level Intermediate Representation
- MLIR project
subtype: null
tags:
- compiler
- LLVM
- intermediate representation
scorecard:
  novelty_delta: 0.8
  claim_density: 0.5
  self_containedness: 0.9
  bridge_score: 0.7
  hub_potential: 0.6
sources:
- raw/cache/d1265777c7bb0eb2.md
- https://mlir.llvm.org/
source_url: https://mlir.llvm.org/
fetched_at: '2026-07-03T14:53:32.326600+00:00'
type: entity
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 0
outbound_links:
- target: mlir-xdsl-rvv-codegen-pipeline
  reason: MLIR is the compiler infrastructure used by the MLIR-xDSL RVV Code Generation
    Pipeline to provide intermediate representations and transformation passes for
    RISC-V vector code generation
---

# MLIR

MLIR (Multi-Level Intermediate Representation) is an open-source compiler infrastructure project developed as a sub-project of the LLVM project. It provides a modular and extensible intermediate representation (IR) framework intended to facilitate the construction of domain-specific compilers and improve compilation for heterogeneous computing platforms. MLIR supports multiple abstraction levels, from high-level dataflow graphs (such as those in TensorFlow) to low-level hardware-specific operations, enabling optimizations like fusion, loop interchange, tiling, and vectorization. It also provides infrastructure for quantization, polyhedral transformations, and hardware synthesis tools (HLS). MLIR is designed to address software fragmentation by providing a unified IR that can connect existing compilers and reduce the cost of building domain-specific compilers. The project incorporates lessons from LLVM IR, XLA HLO, and Swift SIL, and its design enables multithreaded compilation through limited SSA scope and explicit symbol references.

## Key Claims

- MLIR is a multi-level intermediate representation that addresses software fragmentation, improves compilation for heterogeneous hardware, reduces cost of building domain-specific compilers, and aids in connecting existing compilers together.
- MLIR can represent dataflow graphs (e.g., in TensorFlow) including dynamic shapes, a user-extensible op ecosystem, and TensorFlow variables.
- MLIR hosts high-performance-computing-style loop optimizations across kernels (fusion, loop interchange, tiling) and can transform memory layouts of data.
- MLIR supports code generation lowering transformations such as DMA insertion, explicit cache management, memory tiling, and vectorization for 1D and 2D register architectures.
- MLIR can represent target-specific operations, e.g., accelerator-specific high-level operations.
- MLIR includes support for quantization, polyhedral primitives, and hardware synthesis tools (HLS).
- MLIR is not intended for low-level machine code generation (register allocation and instruction scheduling) nor as a source language for end-user kernel writing (analogous to CUDA C++).
- MLIR incorporates experience from LLVM IR, XLA HLO, and Swift SIL; it uses limited SSA scope and explicit symbol references to enable multithreaded compilation.

## Relationships

- [[mlir-xdsl-rvv-codegen-pipeline]]: MLIR is the compiler infrastructure used by the MLIR-xDSL RVV Code Generation Pipeline to provide intermediate representations and transformation passes for RISC-V vector code generation.

## Sources

- https://mlir.llvm.org/
