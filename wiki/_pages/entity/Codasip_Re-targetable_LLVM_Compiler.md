---
cold_start: false
created: '2025-03-04'
inbound_links: 0
needs_summary_revision: true
scorecard:
  bridge_score: 0.6
  claim_density: 0.8
  hub_potential: 0.3
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://codasip.com/2023/07/25/re-targetable-llvm-c-c-plus-plus-compiler-for-riscv/
tags: []
type: entity
updated: '2026-06-28'
---

# Codasip Re-targetable LLVM Compiler

The Codasip Re-targetable LLVM C/C++ Compiler is an automated toolchain generation framework that produces a custom LLVM C/C++ compiler backend from a processor description written in the CodAL language, a C-based processor description language. This framework enables RISC-V designers to define custom ISA extensions and automatically have the generated compiler leverage these instructions for improved performance, code size, or power efficiency, without manual modification of the toolchain. The generated backend is fully aware of all instructions, including encoding, semantics, timing, and hazards, and it integrates advanced optimization passes such as improved jump threading, superblock scheduling, loop collapsing, and support for DSP features like zero-overhead loops and post-increment addressing. The compiler is part of the Codasip Studio processor design toolset and is benchmarked against GCC and vanilla LLVM using Coremark, Dhrystone, and Embench-iot on an RV32IMCB RISC-V configuration.

## Key Claims

- The compiler backend is automatically generated from a CodAL processor description that captures instruction encoding, behavior, hazards, ABI, and microarchitectural details.
- The generated backend can automatically use custom instructions without changes to C/C++ source code, and also supports intrinsic and inline assembly access.
- Codasip enhanced vanilla LLVM with advanced optimization passes: improved jump threading, superblock scheduling, loop collapsing/flattening, improved -msave-restore, support for instructions with multiple outputs, machine outliner, zero-overhead loops, dual-stack architecture support, and load/store with post/pre increment.
- The generated compiler outperforms GCC and vanilla LLVM in performance (Coremark, Dhrystone) and code size (Embench-iot) on the RV32IMCB ISA configuration.
- The front-end and optimizer are precompiled and configured for fast design space exploration; only the back-end is compiled from the description.
- The generated back-end is open to designers for adding custom LLVM optimization passes.
- Other outputs from Codasip Studio include executable models, RTL, and verification tools.

## Relationships

- [[Gemmini_systolic_array_GEMM_accelerator]]: Both are RISC-V toolchain/compilation contexts; while Gemmini uses GNU toolchain, the retargetable LLVM approach described here could be applied to support custom accelerators like Gemmini. (Insufficient context for additional cross-links to entity pages.)
- [[Q4X_Quantization_LLM_Inference_MilkV_Jupiter_Benchmark]]: Both involve LLVM-based compiler toolchains (Clang). The Q4X benchmark uses Clang, which is part of the LLVM project; this page describes an alternative methodology for generating LLVM backends for custom RISC-V processors.

## Sources

- [Re-targetable LLVM C/C++ compiler for RISC-V - Codasip blog post](https://codasip.com/2023/07/25/re-targetable-llvm-c-c-plus-plus-compiler-for-riscv/)
