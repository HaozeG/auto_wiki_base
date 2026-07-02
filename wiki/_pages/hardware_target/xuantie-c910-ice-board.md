---
canonical_name: Xuantie C910
aliases:
- T-HEAD C910
- ICE SoC
- RVB-ICE
subtype: null
tags: []
hardware_targets:
- Xuantie C910
- ICE SoC Board
toolchains:
- riscv64-unknown-linux-gnu
- Buildroot
constraints: []
scorecard:
  novelty_delta: 0.7
  claim_density: 0.5
  self_containedness: 0.6
  bridge_score: 0.3
  hub_potential: 0.3
sources:
- raw/cache/2653baa6434ac0da.md
- https://github.com/XUANTIE-RV/buildroot
source_url: https://github.com/XUANTIE-RV/buildroot
fetched_at: '2026-07-02T09:39:38.959595+00:00'
type: hardware_target
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# Xuantie C910 / ICE SoC Board

The Xuantie C910 is a 64-bit RISC-V CPU core developed by T-Head Semiconductor, implementing the RV64IMAFDCSU ISA profile with vector extension version 0.7.1. It operates at 1.2 GHz and features a three-core configuration integrated into the ICE SoC board. The ICE SoC includes three C910 cores, a GPU, NPU, and DPU, along with 4 GiB of DRAM and various high-speed interfaces for 3D graphics, visual AI, and multimedia processing. The C910 core has a 64 kB instruction cache, 64 kB data cache, a 2 MB L2 cache, and a 1024-entry 4-way TLB. The core also supports memory management with sv39 virtual addressing and 40-bit physical addressing. The Buildroot repository customized for Xuantie CPU series provides a complete Linux system build flow for the ICE board, including kernel, root filesystem, U-Boot, and flash tools.

## Key Claims

- Xuantie C910 is a RISC-V 64-bit core with ISA rv64imafdcsu and vector extension v0.7.1.
- Operating frequency: 1.2 GHz.
- Composed of three cores in the ICE SoC.
- Cache: 64 kB instruction cache, 64 kB data cache, 2 MB L2 cache per core.
- TLB: 1024 entries, 4-way set-associative.
- System memory: 4 GiB DRAM on ICE board.
- ICE SoC includes GPU, NPU, and DPU accelerators.
- Buildroot customization enables building boot.ext4 (kernel+opensbi+dtb), rootfs, and U-Boot for the board.

## Optimization-Relevant Details

- **ISA/profile:** RV64IMAFDCSU, vector extension v0.7.1
- **Vector/matrix/accelerator support:** Vector extension v0.7.1; on-chip GPU, NPU, DPU (detailed interfaces not specified in source)
- **Memory/cache/TLB:** 64 kB I-cache, 64 kB D-cache, 2 MB L2 cache, 1024-entry 4-way TLB, 39-bit virtual (sv39), 40-bit physical address space
- **Compiler/toolchain support:** riscv64-unknown-linux-gnu cross-compiler, Buildroot build system

## Relationships

- [[cpa-factored-gemmini-systolic-array]]: This optimization recipe targets the Gemmini systolic array generator; the Xuantie C910 is a different hardware target but both belong to the RISC-V AI accelerator ecosystem. Further cross-links are not possible due to insufficient context in the wiki.

## Sources

- [GitHub - XUANTIE-RV/buildroot](https://github.com/XUANTIE-RV/buildroot)
