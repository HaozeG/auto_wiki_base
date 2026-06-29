---
cold_start: true
constraints:
- RISC-V 64GCVB
- RVA22
- RISC-V IME extension
- RISC-V Debug v0.13.2
- Power-Islands and two-level power strategies
- 2.0 TOPS AI computing power
created: '2025-01-29'
hardware_targets:
- SpacemiT K1
inbound_links: 0
scorecard:
  bridge_score: 0.5
  claim_density: 0.5
  hub_potential: 0.7
  novelty_delta: 0.9
  self_containedness: 0.6
sources:
- https://forum.banana-pi.org/t/spacemit-k1-risc-v-chip-datasheet-update/18233
tags:
- RISC-V
- SpacemiT K1
- AI accelerator
- Banana Pi
toolchains:
- TensorFlow Lite
- TensorFlow
- ONNX RunTime
type: hardware_target
updated: '2026-06-29'
---

# SpacemiT K1

The SpacemiT K1 (KeyStone K1) is an octa-core RISC-V SoC designed by SpacemiT, featuring the company's self-developed X60 processor core that adheres to the RISC-V 64GCVB architecture and the RVA22 standard. It integrates 2.0 TOPS of AI computing power through a set of RISC-V customized instructions known as the IME (Intelligent Matrix Extension) extension, which reuses Vector register resources and provides over tenfold performance improvement for AI applications compared to scalar execution. The K1 supports mainstream AI inference frameworks including TensorFlow Lite, TensorFlow, and ONNX Runtime via its CPU AI fusion computing architecture. For debugging, it adheres to the RISC-V Debug v0.13.2 standard. The SoC implements two-level power management with Power-Islands and per-core/cluster voltage scaling to achieve ultra-low power consumption. It is paired with LPDDR4 memory and eMMC storage in typical board implementations such as the Banana Pi BPI-F3 single-board computer and the BPI-CM6 compute module.

## Key Claims

- 2.0 TOPS AI computing power via RISC-V IME extension.
- Over tenfold performance improvement for AI applications.
- Supports TensorFlow Lite, TensorFlow, and ONNX Runtime.
- RISC-V 64GCVB compliant with RVA22 standard.
- Implements RISC-V Debug v0.13.2.
- Power-Islands and two-level power strategies for efficiency.
- Used in Banana Pi BPI-F3 and BPI-CM6 boards.

## Optimization-Relevant Details

- ISA/profile: RISC-V 64GCVB, RVA22, IME extension.
- Vector/matrix/accelerator support: IME extension using Vector register resources, CPU AI fusion computing, 2.0 TOPS.
- Memory/cache/TLB/DMA: On-chip memory controller for LPDDR4 and eMMC (board-specific capacities up to 16 GB DDR, 128 GB eMMC).
- Compiler/toolchain support: TensorFlow Lite, TensorFlow, ONNX RunTime.

## Relationships

- [[Tenstorrent_Grayskull_e150]] – Alternative RISC-V-based AI accelerator hardware providing contrast with dataflow architecture.
- [[Chiplet_RISC_V_AI_SoC_Benchmark_Results]] – Benchmark results for a chiplet-based RISC-V AI SoC, offering a point of comparison for performance measurement methodologies.

## Sources

- [https://forum.banana-pi.org/t/spacemit-k1-risc-v-chip-datasheet-update/18233]

