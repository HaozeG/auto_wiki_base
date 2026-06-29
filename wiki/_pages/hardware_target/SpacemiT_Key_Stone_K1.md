---
cold_start: true
constraints:
- RVV 1.0
- 8 cores (2 clusters of 4)
created: '2025-07-16'
hardware_targets:
- SpacemiT Key Stone K1
inbound_links: 0
scorecard:
  bridge_score: 0.5
  claim_density: 0.6
  hub_potential: 0.4
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://wiki.postmarketos.org/wiki/SpacemiT_Key_Stone_K1
tags:
- RISC-V
- SpacemiT
- Key Stone K1
toolchains:
- U-Boot (SpacemiT fork)
type: hardware_target
updated: '2026-06-29'
---

# SpacemiT Key Stone K1

The SpacemiT Key Stone K1 (also known as M1) is a RISC-V SoC released in 2024 by Chinese chip designer SpacemiT. It is a high-performance octa-core 64-bit RISC-V AI CPU utilizing the RISC-V Vector Extension 1.0. The SoC consists of two clusters of four SpacemiT X60 cores each, offering a total of eight cores. Early mainline Linux support was added in Summer 2024. SpacemiT provides a U-Boot fork for this SoC, though the provided U-Boot uses proprietary blobs. The Key Stone K1 is positioned as an energy-efficient AI processor platform and is used in devices such as the Banana Pi BPI-F3.

## Key Claims

- Octa-core 64-bit RISC-V CPU with two clusters of four SpacemiT X60 cores.
- Supports RISC-V Vector Extension 1.0 (RVV 1.0).
- Early mainline Linux support added in Summer 2024.
- SpacemiT provides a U-Boot fork; the default U-Boot includes proprietary blobs.
- Designed for AI workloads and energy-efficient processing.

## Optimization-Relevant Details

- ISA/profile: RV64GCVB (RISC-V with Vector extension 1.0)
- Vector/matrix/accelerator support: RISC-V Vector Extension 1.0, dual-cluster core configuration
- Memory/cache/TLB/DMA: Not detailed in available sources.
- Compiler/toolchain support: SpacemiT provides a U-Boot fork; mainline toolchains (GCC, LLVM) support RVV 1.0.

## Relationships

- [[Chiplet_RISC_V_AI_SoC_Benchmark_Results]] – A benchmark page for a different RISC-V AI SoC architecture, providing contrast in design approach.

Insufficient context for additional cross-links.

## Sources

- [SpacemiT Key Stone K1 - postmarketOS Wiki](https://wiki.postmarketos.org/wiki/SpacemiT_Key_Stone_K1)
- [SpacemiT - Wikipedia](https://en.wikipedia.org/wiki/SpacemiT)
- [SpacemiT Key Stone K1 - RISC-V International](https://riscv.org)
