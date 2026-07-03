---
canonical_name: xDSL
aliases:
- xdsl
- xDSL project
- Python compiler design toolkit
- xdslproject/xdsl
subtype: null
tags: []
scorecard:
  novelty_delta: 0.8
  claim_density: 0.6
  self_containedness: 0.9
  bridge_score: 0.7
  hub_potential: 0.6
sources:
- raw/cache/77e826817d004ed0.md
- https://github.com/xdslproject/xdsl
source_url: https://github.com/xdslproject/xdsl
fetched_at: '2026-07-02T10:15:53.600883+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# xDSL

xDSL is a Python-native SSA compiler framework designed for building compiler infrastructure. It provides static single-assignment (SSA) based intermediate representations (IRs) and Pythonic APIs to define, assemble, and optimize custom IRs, with seamless compatibility with MLIR from the LLVM project. Inspired by MLIR, xDSL enables smooth translation of programs and abstractions between frameworks, allowing users to prototype compilers entirely in Python while still accessing MLIR's powerful optimization and code generation pipeline. All IRs in xDSL employ a unified SSA-based data structure with regions and basic blocks, facilitating the creation of generic analyses and transformation passes.

## Key Claims

- Provides SSA-based intermediate representations with Pythonic APIs for defining, assembling, and optimizing custom IRs.
- Offers seamless compatibility with MLIR (LLVM project) through a bidirectional translation layer.
- Enables rapid prototyping of compilers entirely in Python without sacrificing access to MLIR's code generation backend.
- Supports assembling compilers from predefined or custom IRs with a layered multi-level IR stack for abstraction-specific optimization passes.
- Can be installed via pip (package `xdsl`) and includes extra dependency groups for gui, jax, and riscv subprojects.
- Validated against MLIR version 22.1.2; interoperability with other MLIR versions is not guaranteed.

## Relationships

- [[mlir-xdsl-rvv-lowering-pipeline]]: Optimization recipe that uses xDSL to generate RVV code from MLIR abstractions.
- Insufficient context for additional cross-links.

## Sources

- GitHub repository: https://github.com/xdslproject/xdsl
