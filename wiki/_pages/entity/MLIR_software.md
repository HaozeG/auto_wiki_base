---
cold_start: true
created: '2025-04-10'
inbound_links: 0
scorecard:
  bridge_score: 0.7
  claim_density: 0.85
  hub_potential: 0.8
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://en.wikipedia.org/wiki/MLIR_(software)
tags:
- compiler
- MLIR
- LLVM
- multi-level IR
type: entity
updated: '2026-06-29'
---

# MLIR (software)

MLIR (Multi-Level Intermediate Representation) is an open-source compiler infrastructure project developed as a sub-project of the LLVM project. It provides a modular and extensible intermediate representation (IR) framework intended to facilitate the construction of domain-specific compilers and improve compilation for heterogeneous computing platforms. MLIR supports multiple abstraction levels in a single IR and introduces dialects, a mechanism for defining custom operations, types, and attributes tailored to specific domains. The name "Multi-Level Intermediate Representation" reflects the system’s ability to model computations at various abstraction levels and progressively lower them toward machine code. MLIR was originally developed in 2018 by Chris Lattner at Google and publicly released as part of LLVM in 2019, and is licensed under the Apache License 2.0 with LLVM exceptions.

## Key Claims

- MLIR was originally developed in 2018 by Chris Lattner at Google and publicly released as part of LLVM in 2019.
- MLIR is an open-source compiler infrastructure project under the LLVM umbrella, licensed under the Apache License 2.0 with LLVM exceptions.
- It provides a modular and extensible IR framework supporting multiple abstraction levels in a single IR.
- Dialects are the primary extensibility mechanism, allowing custom operations, types, and attributes.
- MLIR includes built-in core dialects such as arith (arithmetic), memref (memory), affine (polyhedral loops), scf (structured control flow), func (functions), gpu (GPU primitives), tosa (machine learning inference), and llvm (one-to-one mapping to LLVM IR).
- The affine dialect enables polyhedral optimization through affine loop nests.
- The llvm dialect provides a direct mapping to LLVM IR, enabling reuse of LLVM's optimization and code generation.
- Operations can be defined using the Operation definition specification (ODS) via TableGen, which auto-generates C++ code for parsing, printing, and canonicalization.
- MLIR has been adopted by TensorFlow (as foundation for XLA and TensorFlow Runtime), Mojo, TPU-MLIR, ONNX-MLIR, MLIR-AIE, IREE, DSP-MLIR, and torch-mlir.
- MLIR provides an infrastructure for IR rewriting with rewrite drivers and pattern-matching operations.

## Relationships

- [[Gemmini_Architecture]] – Gemmini is an open-source DNN accelerator generator that integrates with a RISC-V SoC and may benefit from MLIR-based compilation flows for lowering machine learning workloads.
- [[Tenstorrent_Grayskull_e150]] – Tenstorrent Grayskull e150 is a dataflow AI accelerator that could be targeted by MLIR-based compilers, as MLIR supports heterogeneous computing and provides dialects for lowering to diverse hardware backends.
- Note: Insufficient context for additional cross-links to entity pages; the current wiki contains only hardware target pages, limiting cross-references to compiler-related entities.

## Sources

- https://en.wikipedia.org/wiki/MLIR_(software)

