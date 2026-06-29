---
cold_start: true
created: '2024-02-09'
inbound_links: 1
scorecard:
  bridge_score: 0.5
  claim_density: 0.7
  hub_potential: 0.3
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://codeplay.com/portal/blogs/2024/02/09/experiences-building-an-mlir-based-sycl-compiler
tags:
- MLIR
- SYCL
- compiler
- compiler optimization
- codeplay
type: entity
updated: '2026-06-29'
---

# SYCL-MLIR Compiler

The SYCL-MLIR compiler is a research prototype developed by Codeplay Software Ltd in collaboration with Intel, designed to demonstrate the potential of using the MLIR (Multi-Level Intermediate Representation) compiler framework to optimize SYCL device code. Unlike traditional SYCL compilers such as DPC++, which translate the Clang AST directly to low-level LLVM IR early in the pipeline, the SYCL-MLIR compiler introduces a custom SYCL dialect within MLIR that captures high-level domain-specific semantics of the SYCL programming model, such as work-item grid positions and memory access via buffers and accessors. This allows the compiler to perform optimizations at multiple levels of abstraction, applying transformations on the SYCL dialect before gradual lowering to lower-level dialects. Additionally, the compiler leverages MLIR's ability to nest device code inside host code modules, enabling cross-module analyses that extract information from the host side (e.g., constant parameters, accessor aliasing) to inform device code optimization. The project was presented at CGO 2024 and the preprint is available on arXiv.

## Key Claims

- The SYCL-MLIR compiler uses a custom SYCL dialect in MLIR to represent core SYCL elements at a high level, preserving domain-specific semantics throughout the compilation pipeline.
- MLIR's gradual lowering approach, through multiple small steps, allows optimizations to operate at the right level of abstraction, unlike the single-step AST-to-LLVM-IR translation in DPC++.
- The compiler performs host analyses (e.g., constant parameters, accessor aliasing) that are fed to device transformations, enabled by MLIR's ability to nest device modules inside host modules.
- On an Intel Data Center GPU Max 1100 (Ponte Vecchio), the compiler achieved a geomean 1.18x speedup over DPC++ across polybench benchmarks from the SYCL-Bench suite.
- The compiler also outperformed AdaptiveCpp (a JIT-based SYCL implementation) on the same benchmarks.

## Relationships

- [[SYCL_MLIR_Compiler_Benchmark_Results]] – Detailed benchmark results for the SYCL-MLIR compiler.
- [[Parallel_GEMM_Convolution_on_GAP8]] – A contrasting optimization recipe for GEMM-based convolution on a RISC-V platform (GAP8), demonstrating different compiler and hardware contexts.
- [[XuanTie_C908_SHL_GEMM_Optimization]] – Another optimization recipe for GEMM on a RISC-V processor, highlighting the variety of compiler approaches for different architectures.
- Due to limited context, no additional entity page cross-links are available.

## Sources

- [Codeplay Blog: Experiences Building an MLIR-based SYCL Compiler](https://codeplay.com/portal/blogs/2024/02/09/experiences-building-an-mlir-based-sycl-compiler)
- [arXiv preprint: Experiences Building an MLIR-based SYCL Compiler](https://arxiv.org/abs/2312.13170)

