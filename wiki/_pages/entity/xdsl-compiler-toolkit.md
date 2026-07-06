---
canonical_name: xDSL
aliases:
- xDSL project
- xDSL Python Compiler Framework
- Python-native SSA Compiler Framework
- xdslproject
- xdsl
- xdslproject/xdsl
- xDSL compiler framework
- Python-native compiler framework
subtype: null
tags: []
scorecard:
  novelty_delta: 0.8
  claim_density: 0.6
  self_containedness: 0.9
  bridge_score: 0.8
  hub_potential: 0.6
sources:
- raw/cache/77e826817d004ed0.md
- https://github.com/xdslproject/xdsl
- raw/cache/24631a4f1ece9250.md
- https://github.com/xdslproject
- raw/cache/2a2c38803b5d26e2.md
- https://xdsl.dev/
- raw/cache/256a47515edbb2ed.md
- https://xdsl.readthedocs.io/stable/marimo/
source_url: https://github.com/xdslproject/xdsl
fetched_at: '2026-07-03T14:52:11.255030+00:00'
type: entity
created: '2026-07-03'
updated: '2026-07-06'
cold_start: true
inbound_links: 0
outbound_links:
- target: mlir-xdsl-rvv-codegen-pipeline
  reason: xDSL is the Python-native compiler framework used to implement the custom
    lowering stages for RVV code generation in this pipeline, demonstrating xDSL's
    ability to extend MLIR's compilation flow with custom dialects and transformation
    passes
- target: mlir-xdsl-gemm-benchmark-k230-banana-pi
  reason: The benchmark evaluates GEMM kernels generated using the MLIR-xDSL pipeline,
    which relies on xDSL's IR construction and transformation capabilities to produce
    portable C code that invokes RVV intrinsics
---

# xDSL

xDSL is a Python-native framework for building compiler infrastructure, providing SSA-based intermediate representations (IRs) and Pythonic APIs to define, assemble, and optimize custom IRs. Originally developed as a research and teaching tool, xDSL has grown into a full-featured compiler design toolkit with support for multiple backends and integration with the MLIR ecosystem. It is MLIR-compatible, sharing the same textual MLIR format for IR, which enables seamless interoperability with MLIR-based tools and access to LLVM's backend for code generation. The framework includes a library of predefined domain-specific IRs and allows users to define custom IRs for specific compilation tasks. xDSL is cross-platform, running on any system that supports Python. The project is organized under the xdslproject GitHub organization, which hosts over 30 repositories covering a range of compiler-related domains: xdsl (the core toolkit), xdsl-jax (extending JAX with xDSL), xdsl-quantum (quantum compiler utilities), xdsl-torch (a reimplementation of torch-mlir), xdsl-webgpu (WebGPU support), xdsl-clang (interoperability with Clang via CIR), xdsl-asl (integrating Arm ASL in the xDSL/MLIR ecosystem), and xdsl-bench (benchmarking infrastructure for the xDSL compiler framework). The project is licensed under Apache-2.0 with LLVM Exceptions and is actively maintained with several hundred stars on GitHub. Developed by the xDSL project community, it is inspired by MLIR from the LLVM project and emphasizes seamless compatibility with MLIR, allowing users to prototype compilers entirely in Python while still accessing MLIR's optimization and code generation pipeline. xDSL supports assembling compilers from predefined or custom IRs and organizing transformations across a multi-level IR stack, making it suitable for domain-specific language development and compiler research. It can be installed via pip and supports subprojects with extra dependencies for GUI, JAX, or RISC-V, with a validated compatibility against MLIR version 22.1.2.

## Key Claims

- xDSL is a Python-native SSA compiler framework inspired by MLIR.
- It provides Pythonic APIs to define, assemble, and optimize custom intermediate representations.
- It is MLIR-compatible, sharing the same textual IR format as MLIR, enabling integration with MLIR-based tools.
- The framework includes a library of predefined domain-specific IRs and supports the definition of custom IRs.
- It offers seamless compatibility with MLIR, enabling access to LLVM's backend for code generation.
- The framework supports building domain-specific languages with custom IRs and running analyses and transformations via simple scripts.
- xDSL is cross-platform (runs on any platform with Python).
- xDSL can be installed via `pip install xdsl`, with extra dependencies for subprojects like GUI, JAX, and RISC-V.
- The supported MLIR version is 22.1.2.
- It relies on an experimental Pyright feature called TypeForm for type checking.
- The xdslproject organization hosts over 30 repositories, including sub-projects for JAX integration, quantum computing, PyTorch, WebGPU, Clang/CIR, and benchmarking.
- xDSL is used in research to implement missing lowering stages for RISC-V Vector (RVV) code generation in the MLIR ecosystem.
- The project is licensed under Apache-2.0 with LLVM Exceptions and has active community contributions.

## Relationships

- [[mlir-xdsl-rvv-codegen-pipeline]]: xDSL is the Python-native compiler framework used to implement the custom lowering stages for RVV code generation in this pipeline, demonstrating xDSL's ability to extend MLIR's compilation flow with custom dialects and transformation passes.
- [[mlir-xdsl-gemm-benchmark-k230-banana-pi]]: The benchmark evaluates GEMM kernels generated using the MLIR-xDSL pipeline, which relies on xDSL's IR construction and transformation capabilities to produce portable C code that invokes RVV intrinsics.
- [[sophon-sg2044-hardware-target]]: Both xDSL and the Sophon SG2044 are part of the LLVM/MLIR compiler ecosystem; xDSL can produce MLIR that is lowered through LLVM to target the SG2044's C920v2 cores with RVV 1.0 acceleration.

## Sources

- https://github.com/xdslproject/xdsl
- https://github.com/xdslproject
- https://xdsl.dev/
