---
canonical_name: RISC-V Optimization Guide
aliases:
- riscv-optimization-guide
- RISC-V optimization guide
- RISCV Optimization Guide
subtype: null
tags: []
scorecard:
  novelty_delta: 0.8
  claim_density: 0.5
  self_containedness: 0.9
  bridge_score: 0.6
  hub_potential: 0.5
sources:
- raw/cache/bb20701460e56062.md
- https://github.com/dzhang28/riscv-optimization-guide/blob/main/riscv-optimization-guide.adoc
source_url: https://github.com/dzhang28/riscv-optimization-guide/blob/main/riscv-optimization-guide.adoc
fetched_at: '2026-07-02T13:04:31.011863+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# RISC-V Optimization Guide

The RISC-V Optimization Guide is a vendor-neutral and implementation-neutral reference document that provides actionable optimization recommendations for software developers writing code for RISC-V application processors. Published online at riscv-optimization-guide.riseproject.dev, the guide covers topics such as detecting RISC-V extensions on Linux using the riscv_hwprobe syscall introduced in Linux kernel 6.4. It includes an example C program demonstrating how to query vendor ID, architecture ID, implementation ID, CPU performance information, and supported extensions including FD, C, V, Zba, Zbb, and Zbs. The guide is intended for toolchain developers, operating system engineers, vectorized library contributors, and educators creating assembly language examples. It also notes that implementation-specific optimizations are clearly marked and that non-RISC-V-standard ISA extensions are out of scope.

## Key Claims

- The RISC-V Optimization Guide is vendor-neutral and implementation-neutral, presenting optimizations applicable to many RISC-V application processors.
- It provides specific, actionable optimization recommendations for RISC-V application processors.
- It includes a section on detecting RISC-V extensions on Linux using the riscv_hwprobe syscall, which was introduced in Linux kernel 6.4.
- The guide provides an example C program that queries vendor ID, March ID, Mimpid, CPU performance (e.g., misaligned access speed), and extensions (FD, C, V, Zba, Zbb, Zbs).
- riscv_hwprobe is preferred over HWCAP because it is extensible, supports multi-letter extension names, has versioned bits, and can determine unaligned access efficiency.
- The program requires Linux 6.5 to build; if the syscall returns ENOSYS, then V, Zba, Zbb, and Zbs are not supported.
- Multi-versioning currently requires separate compilation units and manual runtime checks; single-translation-unit multi-versioning is planned for future toolchains.

## Relationships

- [[spacemit-x60-processor]]: As a RISC-V hardware target, the SpacemiT X60 may benefit from the extension detection and optimization advice in the RISC-V Optimization Guide, especially for AI acceleration workloads.
- [[vectrans]]: VecTrans is a compiler optimization recipe that uses LLMs to enhance auto-vectorization; the RISC-V Optimization Guide provides background on RISC-V extensions and detection methods that could inform such compiler work.
- [[llvm-riscv-fptrunc-narrowing-optimization]]: This optimization recipe for LLVM on RISC-V exemplifies the kind of implementation-specific technique that the guide alludes to in its section on implementation-specific optimizations. Insufficient context for additional cross-links to entity pages; no entity pages are present in the current wiki context.

## Sources

- [GitHub - riscv-optimization-guide](https://github.com/dzhang28/riscv-optimization-guide/blob/main/riscv-optimization-guide.adoc)
