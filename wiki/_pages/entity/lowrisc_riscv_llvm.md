---
cold_start: false
created: '2026-06-26'
inbound_links: 0
scorecard:
  bridge_score: 0.7
  claim_density: 0.3
  hub_potential: 0.8
  novelty_delta: 0.8
  self_containedness: 0.4
sources:
- https://github.com/lowRISC/riscv-llvm
tags:
- LLVM
- RISC-V
- compiler
- toolchain
- lowRISC
type: entity
updated: '2026-06-27'
---

# lowRISC riscv-llvm

The lowRISC riscv-llvm project is a GitHub repository maintained by lowRISC that provides a comprehensive RISC-V backend and toolchain support within the LLVM compiler infrastructure. It extends LLVM's code generation, assembler, linker, and debug information capabilities to target the RISC-V instruction set architecture (ISA), including support for standard extensions such as the M (multiplication and division), A (atomics), F (single-precision floating-point), D (double-precision floating-point), C (compressed instructions), and V (vector) extensions. The repository is based on upstream LLVM and is regularly rebased to track LLVM releases, ensuring compatibility with the latest LLVM features and optimizations. lowRISC's involvement brings expertise from their work on OpenTitan and other open-source silicon projects, making this toolchain particularly relevant for RISC-V system-on-chip development. The project also includes experimental support for newer RISC-V extensions like the Vector Cryptography extensions and Zvk, and aims to serve as a reference LLVM backend for the RISC-V ecosystem.

## Key Claims

- The repository provides a complete RISC-V backend for LLVM, including instruction selection, register allocation, and scheduling, based on the upstream LLVM RISC-V target.
- It supports the RISC-V Vector Extension (V) version 1.0, enabling auto-vectorization and explicit vector programming in C/C++ through built-in functions and intrinsics.
- lowRISC maintains the repository and regularly merges changes from the LLVM mainline, ensuring that patches for new RISC-V extensions are contributed upstream.
- The project includes support for various RISC-V profiles like RV64GCV and RV32IMAC, and is tested against lowRISC's hardware platforms including the OpenTitan chip.
- It provides a Clang driver that can generate RISC-V binaries targeting Linux and bare-metal environments, with full support for relocations and ELF object generation.
- The repository contains scripts and documentation for building a RISC-V LLVM toolchain from source, including cross-compilation setups for common RISC-V emulators (QEMU, Spike) and FPGAs.

## Relationships

- This project is a downstream fork of the LLVM project with specific focus on RISC-V architecture support. It feeds improvements back into the upstream LLVM mainline through patches and code contributions.
- It is closely related to the RISC-V Vector Extension standard and the RISC-V International foundation's specification process, as new extensions require compiler support to be usable.
- lowRISC's riscv-llvm is used in conjunction with the OpenTitan firmware development, providing compiled firmware for RISC-V cores in that project.
- The project interacts with other RISC-V software toolchains including GCC and Newlib, and is often compared against the RISC-V GCC backend for performance and correctness.

## Sources

- GitHub repository: https://github.com/lowRISC/riscv-llvm
