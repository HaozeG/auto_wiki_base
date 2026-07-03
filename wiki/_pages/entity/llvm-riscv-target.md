---
canonical_name: LLVM RISC-V Target
aliases:
- LLVM RISC-V
- RISC-V LLVM
- LLVM RISC-V Backend
- LLVM 23.0.0 RISC-V
- LLVM RISC-V Vector Extension
- LLVM RVV
- RVV LLVM implementation
- RISC-V Vector Extension in LLVM
- RISCVVectorExtension
- LLVM
- llvm
- LLVM Compiler Infrastructure
subtype: null
tags: []
scorecard:
  novelty_delta: 0.8
  claim_density: 0.5
  self_containedness: 0.9
  bridge_score: 0.6
  hub_potential: 0.7
sources:
- raw/cache/d899f76c1cbbbeda.md
- https://llvm.org/docs/RISCVUsage.html
- raw/cache/915ca891a1497a12.md
- https://github.com/llvm/llvm-project/blob/main/llvm/docs/RISCV/RISCVVectorExtension.rst
- raw/cache/6ff772e4360a5a10.md
- https://llvm.org/
source_url: https://llvm.org/docs/RISCVUsage.html
fetched_at: '2026-07-02T09:47:03.000700+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# LLVM RISC-V Target

The LLVM RISC-V target provides code generation for processors implementing supported variations of the RISC-V specification. It resides in the llvm/lib/Target/RISCV directory and is part of the LLVM 23.0.0 release cycle. The target aims to implement the most recent ratified versions of the standard RISC-V base ISAs and ISA extensions, with pragmatic variances documented when necessary. Currently, LLVM fully supports RV32I and RV64I base instruction sets for code generation, while RV32E and RV64E are supported only by assembly-based tools. Over one hundred ratified extensions are supported with varying levels of maturity, ranging from assembly-only support (e.g., H, Sdext, Sdtrig) to full compiler support with intrinsics and pattern matching (e.g., A, C, D, F, M, V, Zba, Zbb, Zbc, Zbs, Zfh, Zk, Zvbb, and many others). The target also supports ISA profiles such as rva20u64, rva22u64, rva23u64, and rvb23u64, which can be passed via -march. This user guide serves as the authoritative reference for LLVM's RISC-V target capabilities.

## Key Claims

- LLVM fully supports RV32I and RV64I base ISAs for code generation.
- LLVM provides assembly-level support for RV32E and RV64E (experimental).
- Over 100 ratified RISC-V extensions are supported, including extensions for cryptography (Zk*), vector (V), and scalar bit manipulation (Zba, Zbb, Zbc, Zbs).
- ISA profiles rva20u64, rva22u64, rva23u64, rvb23u64, rvi20u32, rvi20u64 are supported via -march.
- Experimental profiles like rvm23u32 require -menable-experimental-extensions.
- Known variances from the specification: unconditional allowance of zifencei, zicsr, zicntr, zihpm without gating; CSR naming without extension gating; no enforcement of ordering of z*, s*, x* prefixes in ISA naming strings.
- Pattern matching for Zbkb and Zbkx is supported.

## Relationships

- [[xuantie-c950]]: The XuanTie C950 RISC-V server processor requires LLVM RISC-V target support for compilation and optimization.
- [[sifive-intelligence-x160-gen-2]]: The SiFive Intelligence X160 Gen 2 core leverages LLVM's RISC-V backend, particularly for vector extension and custom instruction support.
- [[gemmini]]: Gemmini's integration with Rocket Chip may utilize LLVM's RISC-V backend for compiling software targeting RISC-V cores.

## Sources

- [User Guide for RISC-V Target — LLVM 23.0.0git documentation](https://llvm.org/docs/RISCVUsage.html)
