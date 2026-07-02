---
canonical_name: MuRISCV-NN
aliases:
- muRISCV-NN
- MuRISCV NN
subtype: null
tags: []
scorecard:
  novelty_delta: 0.8
  claim_density: 0.6
  self_containedness: 0.7
  bridge_score: 0.5
  hub_potential: 0.6
sources:
- raw/cache/9a06ad773baac6ef.md
- https://portal.fis.tum.de/en/publications/muriscv-nn-challenging-zve32x-autovectorization-with-tinyml-infer
source_url: https://portal.fis.tum.de/en/publications/muriscv-nn-challenging-zve32x-autovectorization-with-tinyml-infer
fetched_at: '2026-07-02T11:21:20.937644+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# MuRISCV-NN

MuRISCV-NN is a lightweight, open-source, vendor-agnostic inference library for RISC-V vector extensions targeting TinyML on embedded devices. Developed at the Technical University of Munich, it ports and optimizes ARM Cortex-M neural network kernels (CMSIS-NN) to the RISC-V vector ISA, achieving up to 60% runtime improvement over LLVM's auto-vectorization on convolutional models with large vectors while reducing ROM overhead. The library is bit-accurate to CMSIS-NN and integrates with existing ML deployment frameworks as a drop-in replacement, requiring minimal changes to the compilation flow. This addresses the gap in the RISC-V ecosystem for a lightweight compute library that fully exploits data-level parallelism on vector processors.

## Key Claims

- MuRISCV-NN is the first lightweight, open-source, vendor-agnostic compute library specifically for RISC-V vector extensions on embedded platforms.
- The library ports existing ARM Cortex-M CMSIS-NN kernel implementations to the RISC-V vector ISA and optimizes operator implementations for data-level parallelism.
- Compared to programs vectorized by LLVM's auto-vectorizer, MuRISCV-NN shows an up to 60% runtime advantage for convolutional models and large vectors.
- MuRISCV-NN introduces less ROM overhead than LLVM-auto-vectorized counterparts.
- The library is bit-accurate to CMSIS-NN, ensuring output correctness when used as a replacement.
- It integrates well with existing ML deployment frameworks and can be used as a drop-in replacement with minimal changes to the compilation flow.

## Relationships

- [[llvm-riscv-fptrunc-narrowing-optimization]]: This LLVM optimization recipe for RISC-V FPTrunc narrowing is relevant to MuRISCV-NN's runtime performance, as both involve LLVM code generation for RISC-V vector extensions. The comparison baseline for MuRISCV-NN is LLVM's auto-vectorizer, and improvements to LLVM's RISC-V codegen could affect the performance differential.
- Insufficient context for additional cross-links to entity pages; the current wiki context does not contain other entity pages directly related to MuRISCV-NN.

## Sources

- [MuRISCV-NN: Challenging Zve32x Autovectorization with TinyML Inference Library for RISC-V Vector Extension - TUM Portal](https://portal.fis.tum.de/en/publications/muriscv-nn-challenging-zve32x-autovectorization-with-tinyml-infer)
- Van Kempen, P., Jones, J. P., Mueller-Gritschneder, D., & Schlichtmann, U. (2024). MuRISCV-NN: Challenging Zve32x Autovectorization with TinyML Inference Library for RISC-V Vector Extension. In Proceedings of the 21st ACM International Conference on Computing Frontiers 2024 Workshops and Special Sessions, CF 2024 Companion (pp. 75-78). Association for Computing Machinery, Inc.
