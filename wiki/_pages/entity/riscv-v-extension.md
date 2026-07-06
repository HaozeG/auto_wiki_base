---
canonical_name: RISC-V V Extension
aliases:
- RVV
- RISC-V Vector Extension
- V extension
- CORE-V
- CORE-V Family
- OpenHW CORE-V
- CORE-V cores
- RVV Bench
- camel-cdr/rvv-bench
- rvv-bench
- RISC-V Vector benchmark
- RISC-V
- RISC V
- risk-five
- RV32
- RV64
- RV128
subtype: null
tags: []
scorecard:
  novelty_delta: 0.8
  claim_density: 0.4
  self_containedness: 0.8
  bridge_score: 0.2
  hub_potential: 0.8
sources:
- raw/cache/0f909339888951bc.md
- https://opensecura.googlesource.com/docs/+/fabd959628cc5cfdeaed81c784222fa3d4869125/RiscVVectorSpecDoc.md
- raw/cache/a71b0e3b12c36de7.md
- https://github.com/openhwgroup/core-v-cores
- raw/cache/282a556eaea822f1.md
- https://github.com/camel-cdr/rvv-bench
- raw/cache/798e46c0b34cd5af.md
- https://en.wikipedia.org/wiki/RISC-V
source_url: https://opensecura.googlesource.com/docs/+/fabd959628cc5cfdeaed81c784222fa3d4869125/RiscVVectorSpecDoc.md
fetched_at: '2026-07-03T15:51:28.357627+00:00'
type: entity
created: '2026-07-03'
updated: '2026-07-06'
cold_start: true
inbound_links: 0
---

# RISC-V V Extension

RISC-V (pronounced 'risk-five') is a free and open standard instruction set architecture (ISA) based on reduced instruction set computer (RISC) principles, originally developed at the University of California, Berkeley starting in 2010. Unlike proprietary ISAs such as x86 and ARM, RISC-V specifications are released under permissive open-source licenses and can be implemented without paying royalties. The ISA supports 32-bit, 64-bit, and 128-bit address space variants, uses a load–store architecture with variable-length encoding (primarily 32-bit instructions with optional 16-bit compressed instructions via the C extension), and is little-endian by default. It defines a small base integer instruction set (RV32I, RV64I, RV128I) plus a growing set of standard extensions including M (integer multiplication and division), A (atomics with LR/SC and fetch-and-op), F (single-precision floating-point), D (double-precision floating-point), Q (quad-precision floating-point), C (compressed 16-bit instructions), B (bit manipulation), V (vector operations), and J (interpreted/JIT language support). Development and maintenance of the standard is managed by RISC-V International, a non-profit organization based in Switzerland with over 4,500 members as of 2025. RISC-V is widely adopted in microcontrollers and embedded systems and is increasingly targeted for higher-performance implementations in mobile, desktop, and server markets, supported by commercial SoCs from companies including SiFive, Andes Technology, SpacemiT, Alibaba, StarFive, and Espressif Systems.

The RISC-V Vector Extension (RVV) is the standard instruction set extension for vector processing in the RISC-V ISA, providing data-level parallelism for compute-intensive workloads. Version 1.0 of the specification has been frozen by RISC-V International and is undergoing public review, marking a stable baseline for hardware and software implementations. The extension defines 32 vector registers (v0–v31) with a configurable vector length (VLEN), along with instructions for arithmetic, memory access (unit-stride, strided, and indexed), reductions, and masking. The specification evolves through the riscv-v-spec GitHub repository, which hosts working drafts and release candidates such as v1.0-rc1 and v1.0-rc2. RVV is designed to support a wide range of microarchitectures, from tiny embedded cores to high-performance out-of-order implementations, and forms the foundation for further vector and matrix extensions like Zve (embedded) and Zvfh (half-precision floating-point).

## Key Claims

- RISC-V is an open-standard, royalty-free ISA based on RISC design principles, originally developed at UC Berkeley in 2010 and now maintained by RISC-V International.
- The ISA defines base integer variants for 32-bit (RV32I), 64-bit (RV64I), and 128-bit (RV128I) address spaces, each with a minimal set of instructions.
- Standard extensions cover multiplication (M), atomics (A), floating-point (F/D/Q), compressed instructions (C), bit manipulation (B), vector operations (V), and JIT support (J), among others.
- The architecture uses a load–store design with variable-length encoding (instructions are always little-endian) and a compare-and-branch branching style.
- RISC-V is supported by major Linux distributions and by compilers such as GCC and LLVM.
- Commercial implementations are available from multiple vendors, covering microcontrollers to server-class processors.
- Over 4,500 members of RISC-V International as of 2025.
- The RISC-V Vector Extension (RVV) version 1.0 has been frozen and is undergoing public review as part of the RISC-V International ratification process.
- The specification defines 32 vector registers (v0–v31) with a configurable vector length (VLEN).
- RVV includes instructions for arithmetic, memory access (unit-stride, strided, indexed), reductions, and masking.
- The specification is developed in the open-source riscv-v-spec GitHub repository, with release candidates v1.0-rc1 and v1.0-rc2 preceding the v1.0 frozen release.
- RVV Bench is a collection of RISC-V Vector (RVV) benchmarks hosted on GitHub under the camel-cdr organization, providing a standardized benchmarking suite designed to help developers write portably performant RVV code.
- The project includes algorithm benchmarks (located in ./bench/) and instruction cycle count measurements (located in ./instructions/), covering various implementations of common algorithms and measuring cycle counts of RVV instructions by unrolling and looping repeatedly.
- The repository includes a bench-all.sh script for easy execution and configurable parameters for runtime and precision. Benchmark results are published on a companion results page at https://camel-cdr.github.io/rvv-bench-results.
- The tool requires appropriate Linux kernel settings for performance counter access via /proc/sys/kernel/perf_user_access and /proc/sys/kernel/perf_event_paranoid (<= 2), and supports both standard RVV and XTheadVector (deprecated) instruction sets.
- The project is licensed under the MIT license and accepts contributions via GitHub issues or pull requests.

## Relationships

- RVV Bench is a benchmarking framework for the RISC-V V Extension, providing performance measurement tools and code examples for RVV instructions and algorithms.
- [[sophon-sg2044-hardware-target]]: The SG2044's XuanTie C920v2 cores implement the RISC-V ISA with the ratified Vector Extension version 1.0, using a 128-bit vector unit.
- [[xuantie-c906-hardware-target]]: The XuanTie C906 core implements the RISC-V RV64IMA[FD]C[V] base architecture and adds 130 custom instruction extensions beyond the standard RISC-V set, while also using a 128-bit SIMD vector unit that is not standard RISC-V V.
- [[spacemit-x60-hardware-target]]: The SpacemiT X60 core implements the RISC-V RVA22 profile with the ratified Vector Extension version 1.0 (VLEN 256/128-bit) and is targeted by GCC tuning that models its in-order dual-issue pipeline and vector unit.

## Sources

- https://opensecura.googlesource.com/docs/+/fabd959628cc5cfdeaed81c784222fa3d4869125/RiscVVectorSpecDoc.md
- https://github.com/riscvarchive/riscv-v-spec
- https://github.com/camel-cdr/rvv-bench
- https://en.wikipedia.org/wiki/RISC-V
