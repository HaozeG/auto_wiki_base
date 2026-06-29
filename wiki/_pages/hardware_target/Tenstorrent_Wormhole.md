---
cold_start: true
constraints:
- Tensix cores
- baby RISC-V cores
- GDDR6 memory
- 12 GB GDDR6 (n150) or dual-chip (n300)
- Up to 160W (n150) or 300W (n300)
- Active or passive cooling
- PCI Express (generation not specified)
- Multichip mesh support (Galaxy)
- Open-source SDKs
created: '2025-07-03'
hardware_targets:
- Wormhole
inbound_links: 0
scorecard:
  bridge_score: 0.6
  claim_density: 0.9
  hub_potential: 0.6
  novelty_delta: 0.8
  self_containedness: 1.0
sources:
- https://tenstorrent.com/en/hardware/cards
tags:
- Tenstorrent
- Wormhole
- RISC-V
- AI accelerator
- Tensix
toolchains:
- TT-Buda
- TT-Metalium
type: hardware_target
updated: '2026-06-29'
---

# Tenstorrent Wormhole

The Tenstorrent Wormhole is a flexible and scalable AI processor designed for PCIe add-in boards, built with Tensix Cores and baby RISC-V cores for data movement. The Wormhole family includes single-chip (n150d/n150s) and dual-chip (n300d/n300s) configurations, operating at up to 160W and 300W respectively, with active or passive cooling options. The n150 features 72 Tensix cores and 12 GB GDDR6 at 288 GB/s bandwidth, while the n300 combines two Wormhole processors for increased compute and memory. Wormhole supports multichip mesh networking via QSFP-DD cables for workstation and server clusters (e.g., Galaxy). The software stack is fully open source, offering TT-Buda for high-level model deployment and TT-Metalium for low-level metal programming. This hardware target provides a cost-effective RISC-V-based alternative to traditional GPUs for AI inference workloads.

## Key Claims

- n150: 72 Tensix cores, 12 GB GDDR6, 288 GB/s bandwidth, up to 160W.
- n300: Dual Wormhole processors, up to 300W.
- Multichip mesh support via Galaxy cable (QSFP-DD 400G DAC).
- Supported by open-source SDKs: TT-Buda (high-level) and TT-Metalium (low-level).
- Broad data precision format support (FP8, BF16, etc.).
- Superior performance for cost compared to traditional GPUs (marketing claim).
- Active cooling included with n150d/n300d; passive cooling available as n150s/n300s.
- System interface: PCI Express (generation not specified).

## Optimization-Relevant Details

- ISA/profile: Tensix cores with baby RISC-V for control.
- Vector/matrix/accelerator support: Tensix cores with NoC.
- Memory/cache/TLB/DMA: GDDR6, NoC, SRAM per core.
- Compiler/toolchain support: TT-Buda, TT-Metalium.

## Relationships

- [[Tenstorrent_Grayskull_MatMul_Efficiency]] – Previous generation efficiency benchmark for context.
- [[Tenstorrent_Blackhole]] – Next-generation Tenstorrent product line with higher performance and newer architecture.

*Note: insufficient context for additional cross-links to other entity pages; no dedicated Tenstorrent entity pages exist in the current wiki.*

## Sources

- [Cards - Tenstorrent](https://tenstorrent.com/en/hardware/cards)
