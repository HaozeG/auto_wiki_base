---
canonical_name: XuanTie GNU Compiler Toolchain
aliases:
- Xuantie GNU Toolchain
- xuantie-gnu-toolchain
subtype: null
tags: []
scorecard:
  novelty_delta: 0.8
  claim_density: 0.5
  self_containedness: 0.8
  bridge_score: 0.6
  hub_potential: 0.2
sources:
- raw/cache/e2d11e0e15367364.md
- https://github.com/XUANTIE-RV/xuantie-gnu-toolchain/
source_url: https://github.com/XUANTIE-RV/xuantie-gnu-toolchain/
fetched_at: '2026-07-03T13:20:08.490104+00:00'
type: entity
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 0
outbound_links:
- target: xuantie-ai-benchmark-suite
  reason: The XuanTie AI Benchmark Suite uses this toolchain to compile precompiled
    model binaries for XuanTie C907 and C908 cores
---

# XuanTie GNU Compiler Toolchain

The XuanTie GNU Compiler Toolchain is an open-source RISC-V cross-compiler maintained by XUANTIE-RV for building C and C++ applications targeting XuanTie processors. It supports two build configurations: a Newlib-based ELF toolchain for bare-metal or embedded environments, and a Linux-ELF glibc-based toolchain for Linux userspace development. The toolchain can target both RV32GC and RV64GC architectures and includes support for standard RISC-V extensions such as atomics (A), multiplication/division (M), single-precision float (F), and double-precision float (D), with a 'general' group (G) combining M, A, F, and D. Multilib builds allow a single compiler to target both 32-bit and 64-bit systems using the most common -march/-mabi combinations. The repository also provides prebuilt toolchains via the Open Chip Community (OCC) download center.

## Key Claims

- Provides both Newlib (bare-metal) and Linux (glibc) cross-compiler toolchains for RISC-V XuanTie cores.
- Supports architectures rv32i/rv64i and extensions A, M, F, D, and G (which includes M, A, F, D).
- Supports ABIs: ilp32, ilp32d, ilp32f, lp64, lp64f, lp64d.
- Multilib mode enables a single compiler to target both 32-bit and 64-bit systems with common -march/-mabi options.
- Prebuilt toolchains are available from the Open Chip Community (OCC) download center.
- Build requires approximately 8 GiB of disk space and specific system packages.

## Relationships

- [[xuantie-ai-benchmark-suite]]: The XuanTie AI Benchmark Suite uses this toolchain to compile precompiled model binaries for XuanTie C907 and C908 cores.

## Sources

- https://github.com/XUANTIE-RV/xuantie-gnu-toolchain
