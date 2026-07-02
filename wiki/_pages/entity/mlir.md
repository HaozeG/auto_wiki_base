---
canonical_name: MLIR
aliases:
- Multi-Level Intermediate Representation
- LLVM MLIR
subtype: null
tags:
- compiler infrastructure
- IR
- LLVM
scorecard:
  novelty_delta: 0.9
  claim_density: 0.7
  self_containedness: 0.9
  bridge_score: 0.8
  hub_potential: 0.8
sources:
- raw/cache/d1265777c7bb0eb2.md
- https://mlir.llvm.org/
source_url: https://mlir.llvm.org/
fetched_at: '2026-07-02T06:21:12.988049+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# MLIR

MLIR (Multi-Level Intermediate Representation) is a compiler infrastructure project under the LLVM project that provides a reusable and extensible framework for building compilers. It aims to address software fragmentation, improve compilation for heterogeneous hardware, significantly reduce the cost of building domain-specific compilers, and aid in connecting existing compilers together. MLIR is designed as a hybrid IR that can represent dataflow graphs (such as in TensorFlow) with dynamic shapes and a user-extensible op ecosystem, host high-performance-computing-style loop optimizations across kernels (fusion, loop interchange, tiling), transform memory layouts of data, and perform code generation "lowering" transformations such as DMA insertion, explicit cache management, memory tiling, and vectorization for 1D and 2D register architectures. Additionally, MLIR can represent target-specific operations, quantization and other graph transformations for deep learning, polyhedral primitives, and hardware synthesis tools (HLS). MLIR intentionally does not target low-level machine code generation algorithms like register allocation and instruction scheduling, which are better suited for lower-level optimizers such as LLVM, nor is it intended as a source language for end-user kernel programming; it provides the backbone for representing domain-specific languages. The MLIR framework encourages best practices including maintaining an IR spec, building an IR verifier, supporting text dump and parse with FileCheck, and composing modular libraries. It also addresses design lessons from LLVM, such as enabling multithreaded compilation by using limited SSA scope and explicit symbol references instead of cross-function references.

## Key Claims

- MLIR is a multi-level IR that unifies multiple compiler needs in a single infrastructure.
- It can represent dataflow graphs (e.g., TensorFlow) with dynamic shapes and user-extensible ops.
- It hosts HPC-style loop optimizations (fusion, tiling, interchange, memory layout transform).
- It supports code generation lowerings: DMA insertion, cache management, vectorization (1D/2D).
- It can represent target-specific operations (e.g., accelerator-specific high-level ops).
- It supports quantization and deep-learning graph transformations.
- It includes polyhedral primitives and hardware synthesis tools (HLS).
- Non-goals: low-level machine code generation (register allocation, instruction scheduling) and end-user kernel programming language.
- MLIR encourages best practices: IR spec, verifier, text format, FileCheck tests, modular libraries.
- MLIR improves upon LLVM by enabling multithreaded compilation through limited SSA scope and explicit symbol references.

## Relationships

- The [[mlir_xdsl_rvv_gemm_codegen_recipe]] page describes an optimization recipe that uses MLIR combined with xDSL to generate RISC-V Vector GEMM micro-kernels, demonstrating MLIR's role in hardware-aware code generation.
- The [[iree_mlir_ukernel_rvv_matmul]] page documents a proposed MLIR-based ukernel for RISC-V Vector matmul within the IREE compiler framework, showing MLIR's use in compiler-driven kernel generation.
- The MLIR infrastructure is a key dependency for toolchains targeting RISC-V AI accelerators, such as the K230 system-on-chip documented in [[k230]].
- Additional related pages include [[generic_micro_kernel_templates_gemm]] (which uses non-RISC-V micro-kernel templates) and [[llvm_riscv_target]] (which provides the backend instruction selection for MLIR's vector dialect).

## Sources

- https://mlir.llvm.org/
