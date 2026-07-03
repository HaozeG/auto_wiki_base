---
canonical_name: llvm-rv
aliases:
- compiler-dev/llvm-rv
- LLVM RVV
- LLVM RISC-V Vector Extension Support
- RVV LLVM support
- LLVM RISC-V Vector
subtype: null
tags: []
scorecard:
  novelty_delta: 0.5
  claim_density: 0.3
  self_containedness: 0.7
  bridge_score: 0.6
  hub_potential: 0.6
sources:
- raw/cache/1fb6afe68a9417ba.md
- https://github.com/compiler-dev/llvm-rv
- raw/cache/ba008059e7113c2a.md
- https://llvm.org/docs/RISCV/RISCVVectorExtension.html
source_url: https://github.com/compiler-dev/llvm-rv
fetched_at: '2026-07-02T10:22:25.273890+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# llvm-rv

llvm-rv is a fork of the LLVM and Clang compiler infrastructure that provides full support for the RISC-V Vector Extension (RVV) version 0.8 targeting the 32-bit RISC-V (RV32) instruction set architecture. Developed by Hunan Compiler Information Technology Co., Ltd. (compiler-dev), the project delivers a complete toolchain including the Clang C/C++ compiler, the llvm-mc assembler, and the llvm-objdump disassembler, implementing over 6000 intrinsic interfaces. The compiler requires a prebuilt RISC-V GNU toolchain (riscv-gnu-toolchain) for linking and the SPIKE simulator for running compiled vector programs. Build instructions and test cases are provided in the repository, including a vector addition test and an RVV sgemm matrix multiplication example that demonstrate the workflow on a Linux x86 host.

## Key Claims

- Full support for RVV version 0.8 on RV32.
- Over 6000 intrinsic interfaces implemented.
- Includes Clang, llvm-mc, and llvm-objdump.
- Compatible with SPIKE simulator and RISC-V GNU toolchain.
- Provides build instructions and test cases (vadd_vv_i32, rvv_sgemm).

## Relationships

- [[gemmini]]: llvm-rv can generate vector code for RISC-V hardware such as Gemmini-based systems.
- [[nncase]]: A complementary compiler stack for neural networks targeting RISC-V AI accelerators.

## Sources

- [GitHub README: compiler-dev/llvm-rv](https://github.com/compiler-dev/llvm-rv)
