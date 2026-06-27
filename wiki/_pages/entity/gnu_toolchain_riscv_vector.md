---
cold_start: true
created: 2026-06-27
inbound_links: 3
scorecard:
  bridge_score: null
  claim_density: null
  hub_potential: null
  novelty_delta: null
  self_containedness: null
sources:
- https://gcc.gnu.org/onlinedocs/gcc-14.1.0/gcc/RISC-V-Vector-Intrinsics.html
- https://www.phoronix.com/news/GCC-RISC-V-Auto-Vectorization
- https://llvm.org/docs/RISCVUsage.html
- https://lists.riscv.org/g/tech-vector-ext/message/364
tags:
- risc-v
- compiler
- GCC
- LLVM
- toolchain
- RVV
- auto-vectorization
- software-stack
type: entity
updated: 2026-06-27
---

# GNU Toolchain RISC-V Vector Support

The GNU Compiler Collection (GCC) and LLVM together form the primary open-source compiler infrastructure for RISC-V Vector (RVV) code generation, covering both explicit vector intrinsics and automatic vectorization. GCC 13 introduced RVV intrinsic support based on version 0.11 of the RISC-V Vector Intrinsic Specification; GCC 14 (released April 2024) added initial auto-vectorization for RVV, contributed primarily by engineers at Rivos Inc. This auto-vectorizer supports integer arithmetic (add, subtract, multiply) and floating-point operations using a new vector cost model integrated into GCC's tree-loop-vectorization (TLV) pass. To enable auto-vectorization, users build with -march=rv64gcv and -O3 or -ftree-vectorize. LLVM/Clang has supported RVV code generation since LLVM 12 (2021), covering both intrinsics and backend codegen; it is generally considered ahead of GCC in RVV optimization maturity. Both compilers expose Zve* embedded sub-extensions via -march= flags (e.g., rv32gcv_zve32x). Apache TVM's RVV backend uses LLVM as its code-generation layer, achieving 46% lower latency versus raw GCC. The combined GCC + LLVM + binutils (gas assembler with RVV instruction support) ecosystem enables the full RISC-V software-hardware stack for AI inference from model compilation down to optimized assembly.

## Key Claims

- GCC 13 added RVV intrinsics (spec v0.11); GCC 14 (April 2024) added initial RVV auto-vectorization.
- RVV auto-vectorization in GCC 14 contributed by Rivos Inc.; activated with -march=rv64gcv and -O3/-ftree-vectorize.
- LLVM/Clang supports RVV codegen since LLVM 12 (2021); generally more mature than GCC for RVV optimization.
- Both GCC and LLVM expose all Zve* embedded vector sub-extensions via -march= flags.
- Apache TVM uses LLVM as its RISC-V codegen backend, achieving 46% latency reduction over GCC.
- Linux kernel hwprobe API allows runtime detection of which Zve sub-extensions are present.

## Relationships

- [[risc_v_vector_extension]]: GNU toolchain is the primary compiler infrastructure for generating RVV 1.0 code.
- [[risc_v_zve_embedded_vector]]: GCC/LLVM both expose Zve* sub-extensions via -march= enabling embedded RVV targets.
- [[tvm_riscv_backend]]: TVM relies on LLVM's RISC-V RVV backend for final machine code generation.
- [[mlir_riscv_backend]]: MLIR RISC-V backend lowers to LLVM IR which then uses the same LLVM RVV codegen.
- [[iree_riscv]]: IREE uses LLVM (via MLIR) as its RISC-V backend, depending on the same RVV toolchain support.

## Sources

- https://gcc.gnu.org/onlinedocs/gcc-14.1.0/gcc/RISC-V-Vector-Intrinsics.html
- https://www.phoronix.com/news/GCC-RISC-V-Auto-Vectorization
- https://llvm.org/docs/RISCVUsage.html
- https://lists.riscv.org/g/tech-vector-ext/message/364
