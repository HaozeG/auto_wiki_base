---
canonical_name: XuanTie GNU Compiler Toolchain
aliases:
- Xuantie GNU Toolchain
- xuantie-gnu-toolchain
- XuanTie GNU Toolchain
- Xuantie GNU cross-compiler
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
updated: '2026-07-06'
cold_start: true
inbound_links: 0
outbound_links:
- target: xuantie-ai-benchmark-suite
  reason: The XuanTie AI Benchmark Suite uses this toolchain to compile precompiled
    model binaries for XuanTie C907 and C908 cores
---

# XuanTie GNU Compiler Toolchain

The XuanTie GNU Compiler Toolchain is an open-source RISC-V cross-compiler suite maintained by XUANTIE-RV, specifically supporting Alibaba/T-Head XuanTie processor cores. It provides two build configurations: a Newlib-based ELF toolchain for bare-metal or embedded environments, and a Linux-ELF glibc-based toolchain for Linux userspace development. The toolchain can target both RV32GC and RV64GC architectures and includes support for standard RISC-V extensions such as atomics (A), multiplication/division (M), single-precision float (F), double-precision float (D), compressed instructions (C), and a 'general' group (G) combining M, A, F, and D. Multilib builds (enabled with `--enable-multilib`) allow a single compiler to target both 32-bit and 64-bit systems using the most common `-march`/`-mabi` combinations. Prebuilt toolchains are available from the Open Chip Community (OCC) download center at https://www.xrvm.cn/community/download. Build dependencies are documented for Ubuntu, Fedora, CentOS/RHEL, Arch Linux, and macOS (via Homebrew); the build process downloads approximately 200 MiB of upstream sources and requires about 8 GiB of disk space. Troubleshooting guidance includes using an empty install directory to prevent hard-float/soft-float conflicts, ensuring a case-sensitive filesystem for glibc builds on macOS, and using devtoolset-7 on CentOS/RHEL to obtain current GNU tools.

## Key Claims

- Provides both Newlib (bare-metal) and Linux (glibc) cross-compiler toolchains for RISC-V XuanTie cores.
- Supports architecture strings rv32i/rv64i with extensions A, M, F, D, C, and G (which includes M, A, F, D).
- Supports ABIs: ilp32, ilp32d, ilp32f, lp64, lp64f, lp64d.
- Multilib mode enables a single compiler to target both 32-bit and 64-bit systems with common `-march`/`-mabi` options.
- Prebuilt toolchains are available from the Open Chip Community (OCC) download center at https://www.xrvm.cn/community/download.
- Build requires approximately 8 GiB of disk space and specific system packages; documented dependencies for Ubuntu, Fedora/CentOS/RHEL, Arch Linux, and macOS.
- Troubleshooting guidance: use an empty install directory to prevent hard-float/soft-float conflicts; a case-sensitive filesystem is required for glibc builds on macOS; CentOS/RHEL users may need devtoolset-7 for current GNU tools.

## Relationships

- [[xuantie-ai-benchmark-suite]]: The XuanTie AI Benchmark Suite uses this toolchain to compile precompiled model binaries for XuanTie C907 and C908 cores.
- [[xuantie-c906-hardware-target]]: The XuanTie GNU Toolchain provides the GCC compiler used to compile code for the XuanTie C906, supporting its custom instruction extensions and 128-bit SIMD vector unit.
- [[gcc-tuning-c908-canmv-k230]]: The GCC tuning patches for the XuanTie C908 are built upon the XuanTie GNU Toolchain, and the benchmark results demonstrate the scheduler model validated using this compiler.

## Sources

- https://github.com/XUANTIE-RV/xuantie-gnu-toolchain
