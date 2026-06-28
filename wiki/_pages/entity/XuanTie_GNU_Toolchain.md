---
cold_start: true
created: '2025-03-04'
inbound_links: 0
scorecard:
  bridge_score: 0.7
  claim_density: 0.9
  hub_potential: 0.6
  novelty_delta: 0.8
  self_containedness: 0.9
sources:
- https://github.com/XUANTIE-RV/xuantie-gnu-toolchain
tags:
- Xuantie
- GNU
- toolchain
- RISC-V
type: entity
updated: '2026-06-28'
---

# XuanTie GNU Toolchain

The XuanTie GNU Toolchain is the official C and C++ cross-compiler for Xuantie RISC-V CPUs, provided by T-Head Semiconductor through the XUANTIE-RV organization on GitHub. It supports two build modes: a generic ELF/Newlib toolchain for bare-metal or embedded development and a Linux-ELF/glibc toolchain for cross-compiling Linux applications. The toolchain includes GCC, Binutils, and related components, and can be built from source or downloaded as a prebuilt package from the Open Chip Community (OCC) resource center. It supports a range of RISC-V architectures (rv32i, rv64i, and extensions including A, M, F, D, and G) and ABIs (ilp32, ilp32d, ilp32f, lp64, lp64f, lp64d), and provides multilib support for targeting both 32-bit and 64-bit systems from a single toolchain installation. The repository also includes build scripts and documentation for prerequisites and troubleshooting.

## Key Claims

- The XuanTie GNU Toolchain is a C/C++ cross-compiler for Xuantie RISC-V CPUs, supporting Newlib (ELF) and glibc (Linux) build modes.
- Architectures supported: rv32i, rv64i, and extensions A, M, F, D, G (general MAFD).
- ABIs supported: ilp32, ilp32d, ilp32f, lp64, lp64f, lp64d.
- Multilib mode enables a single compiler to target both 32-bit and 64-bit systems with common -march/-mabi options.
- Prebuilt toolchains are available for download from the OCC resource center (https://www.xrvm.cn/community/download).
- Build prerequisites: autoconf, automake, python3, libmpc-dev, libmpfr-dev, libgmp-dev, and others.
- Build instructions use `./configure --prefix=<path>`, then `make` for Newlib or `make linux` for glibc.
- Troubleshooting notes: building into an empty directory avoids linker conflicts; mixing hard-float and soft-float toolchains in the same prefix can cause errors; Linux toolchain builds on MacOS require a case-sensitive filesystem.
- The toolchain is developed and maintained by T-Head Semiconductor under the XUANTIE-RV organization.

## Relationships

- [[Gemmini_systolic_array_GEMM_accelerator]] – The Gemmini accelerator relies on GNU toolchain support for encoding custom RISC-V instructions; the XuanTie GNU toolchain may be used in compilation flows targeting systems that integrate Gemmini or other Xuantie cores.
- Insufficient context for additional cross-links.

## Sources

- https://github.com/XUANTIE-RV/xuantie-gnu-toolchain

