---
cold_start: true
constraints:
- PCI Express 5.0 x16
- up to 300W TBP
- GDDR6 memory (28 GB or 32 GB)
- 120 Tensix Cores
- 16 big RISC-V cores
- 180 MB SRAM
- active or passive cooling
- QSFP-DD 800G ports (P150 series)
created: '2026-07-20'
hardware_targets:
- Blackhole P100a
- Blackhole P150a
- Blackhole P150b
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
- Blackhole
- Tensix
- RISC-V
- AI accelerator
toolchains:
- TT-Buda
- TT-Metalium
type: hardware_target
updated: '2026-06-29'
---

# Blackhole Tensix Processor

The Blackhole family of Tensix processors from Tenstorrent are high-performance RISC-V-based AI accelerator cards designed for scalable AI processing in data center and workstation environments. They feature 120 Tensix cores and 16 big RISC-V cores per chip, with up to 32 GB of GDDR6 memory and memory bandwidth up to 512 GB/s. The Blackhole P100a operates at 300W with active cooling, while the P150 series includes both active (P150a) and passive (P150b) cooling options and adds four QSFP-DD 800G ports for multi-card linking to pool memory and improve performance. The processors support a fully open source software stack including TT-Buda and TT-Metalium SDKs, granting developers low-level hardware access. Key specifications include a 1.35 GHz AI clock, 180 MB SRAM, 664 TFLOPS (BLOCKFP8) peak performance, and a PCI Express 5.0 x16 system interface.

## Key Claims

- 120 Tensix Cores per chip
- 16 big RISC-V cores
- AI clock speed: 1.35 GHz
- SRAM: 180 MB
- Memory: 28 GB GDDR6 (P100a) or 32 GB GDDR6 (P150 series)
- Memory speed: 16 GT/sec
- Memory bandwidth: 448 GB/sec (P100a) or 512 GB/sec (P150 series)
- Peak performance: 664 TFLOPS (BLOCKFP8)
- Total Board Power: 300W
- External power: 12V-2x6
- Connectivity: N/A (P100a) / 4x QSFP-DD 800G (P150 series)
- System interface: PCI Express 5.0 x16
- Cooling: Active (P100a, P150a) / Passive (P150b)
- Dimensions: 42mm x 270mm x 111mm
- Fully open source software stack (TT-Buda, TT-Metalium)

## Relationships

- [[DSC_Fused_Dataflow_Benchmark_Results]] – A benchmark for a different RISC-V AI accelerator, providing contrast in architecture and performance.
- [[Chiplet_RISC_V_AI_SoC_Benchmark_Results]] – Benchmark results for a chiplet-based RISC-V AI SoC, showing alternative approach to AI acceleration.

*Note: Insufficient context for additional entity page cross-links in the current wiki.*

## Sources

- [Tenstorrent Cards Page](https://tenstorrent.com/en/hardware/cards)
