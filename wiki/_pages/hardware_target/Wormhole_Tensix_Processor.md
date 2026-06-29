---
cold_start: true
constraints:
- PCI Express
- up to 160W (n150) or 300W (n300)
- GDDR6 memory
- baby RISC-V cores
- active cooling (n150d, n300d)
- passive cooling (n150s, n300s)
- QSFP-DD cable support
- multichip mesh support (Galaxy)
created: '2026-07-20'
hardware_targets:
- Wormhole n150d
- Wormhole n150s
- Wormhole n300d
- Wormhole n300s
inbound_links: 0
scorecard:
  bridge_score: 0.5
  claim_density: 0.7
  hub_potential: 0.6
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://tenstorrent.com/en/hardware/cards
tags:
- Tenstorrent
- Wormhole
- Tensix
- RISC-V
- AI accelerator
toolchains:
- TT-Buda
- TT-Metalium
type: hardware_target
updated: '2026-06-29'
---

# Wormhole Tensix Processor

The Wormhole family of Tensix processors from Tenstorrent are flexible, scalable RISC-V-based AI accelerator cards designed for cost-efficient AI inference and training. They are built with Tensix cores, each containing a compute unit, network-on-chip, local cache, and "baby RISC-V" cores for data movement. The Wormhole n150d (single processor) features 72 Tensix cores, 108 MB SRAM, 12 GB GDDR6 with 288 GB/s bandwidth, operating at 160W with active axial fan cooling. The n150s offers passive cooling. The n300 series integrates two Wormhole processors on one card for up to 300W, with dual processor capabilities and a 2.5-slot active cooling solution. Both series support networking into a multichip mesh for workstation and server configurations (such as Galaxy) and are supported by the same open-source SDKs as Blackhole. The resource mentions superior performance for cost compared to traditional GPUs and broad data precision format support.

## Key Claims

- Tensix core architecture with compute, network-on-chip, local cache, and baby RISC-V cores
- n150 series: 72 Tensix cores, 108 MB SRAM, 12 GB GDDR6 at 288 GB/s, 160W TBP
- n300 series: dual Wormhole processors, up to 300W
- Active cooling (d variants) or passive (s variants)
- Multichip mesh networking support via Galaxy cable and QSFP-DD interconnects
- Open source software stack: TT-Buda (high-level) and TT-Metalium (low-level)
- Superior price/performance ratio compared to conventional GPUs
- Broad data precision format support

## Relationships

- [[DSC_Fused_Dataflow_Benchmark_Results]] – A benchmark for a different RISC-V AI accelerator, highlighting architectural differences.
- [[Chiplet_RISC_V_AI_SoC_Benchmark_Results]] – Benchmark for a chiplet-based RISC-V SoC, providing a contrasting approach to AI acceleration.

*Note: Insufficient context for additional entity page cross-links in the current wiki.*

## Sources

- [Tenstorrent Cards Page](https://tenstorrent.com/en/hardware/cards)
