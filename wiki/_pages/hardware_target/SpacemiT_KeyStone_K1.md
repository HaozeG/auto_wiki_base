---
cold_start: true
constraints:
- RVA22 profile
- RISC-V 64GCVB
- 8 cores
- 1.6 GHz
- 2.0 TOPS AI
created: '2026-07-10'
hardware_targets:
- SpacemiT KeyStone K1
inbound_links: 1
scorecard:
  bridge_score: 0.3
  claim_density: 0.5
  hub_potential: 0.4
  novelty_delta: 0.6
  self_containedness: 0.8
sources:
- https://www.spacemit.com/products/keystone/k1
tags:
- RISC-V
- SpacemiT
- KeyStone K1
- X60
toolchains: []
type: hardware_target
updated: '2026-06-28'
---

# SpacemiT KeyStone K1

The SpacemiT KeyStone K1 is a high-performance, ultra-low-power system-on-chip designed for RISC-V AI applications. It integrates eight SpacemiT X60 RISC-V CPU cores compliant with the RVA22 profile and the RISC-V 64GCVB architecture. The SoC delivers 2.0 TOPS of AI computing power via a dedicated neural engine, making it suitable for single-board computers (SBCs), intelligent robotics, edge AI terminals, home storage/computing devices, AI PCs, and industrial edge nodes. Key applications include the Banana Pi BPI-F3 and BPI-CM6 modules, where it operates at frequencies up to 1.6 GHz. The K1 emphasizes open-source and open-ecosystem computing, supporting global RISC-V software infrastructure.

## Key Claims

- Integrates eight 64-bit RISC-V CPU cores based on the SpacemiT X60 microarchitecture.
- Supports the RVA22 profile and RISC-V 64GCVB instruction set.
- Provides 2.0 TOPS of AI computing power.
- Operates at a maximum clock frequency of 1.6 GHz.
- Targets markets including SBCs, robotics, edge AI, and network-attached storage.
- Used in commercial products such as the Banana Pi BPI-F3 single-board computer and BPI-CM6 compute module.
- Promotes open-source ecosystem and is designed for Linux-capable software stacks.

## Optimization-Relevant Details

- ISA/profile: RISC-V 64GCVB with RVA22 profile.
- Vector/matrix/accelerator support: Includes a neural engine delivering 2.0 TOPS (further architecture details not specified in the available resource).
- Memory/cache/TLB/DMA: Core-specific details not provided in the extracted content; typical RISC-V SoC memory hierarchy (cache sizes, DMA) not specified.
- Compiler/toolchain support: General Linux toolchains; no vendor-specific compiler version mentioned in the resource.

## Relationships

- [[Chiplet_RISC_V_AI_SoC_Benchmark_Results]] – A benchmark for a different RISC-V SoC design with chiplet architecture and AI acceleration, offering contrast in design philosophy.
- [[DSC_Fused_Dataflow_Benchmark_Results]] – Benchmark results for a fused dataflow accelerator on RISC-V, relevant to edge AI workloads that the K1 targets.
- Insufficient context for additional cross-links to entity pages within the current wiki.

## Sources

- [K1 Product Page – SpacemiT](https://www.spacemit.com/products/keystone/k1)
