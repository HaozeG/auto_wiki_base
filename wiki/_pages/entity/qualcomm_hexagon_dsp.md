---
type: entity
tags: [dsp, vliw, hvx, neural-processing, mobile, qualcomm]
sources:
  - https://en.wikipedia.org/wiki/Qualcomm_Hexagon
  - https://chipsandcheese.com/p/qualcomms-hexagon-dsp-and-now-npu
  - https://thechipletter.substack.com/p/qualcomms-hexagon-ai-accelerators
  - https://docs.qualcomm.com/bundle/publicresource/topics/80-88500-4/147_HTA.html
  - https://old.hotchips.org/wp-content/uploads/hc_archives/hc25/HC25.70-Mobility-epub/HC25.27.712-Hot%20Chips%202013%20Final%20Presentation%20--%20Qualcomm_Lucian_Codrescu%20v2.pdf
created: 2026-06-26
updated: 2026-06-26
cold_start: true
inbound_links: 0
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# Qualcomm Hexagon DSP

Qualcomm Hexagon is a family of digital signal processors (DSPs) and, from the Snapdragon 855 generation onward, neural processing units (NPUs) integrated into Qualcomm Snapdragon system-on-chip (SoC) platforms. First introduced in 2006 on a 65 nm process, the Hexagon architecture is built around a 4-issue Very Long Instruction Word (VLIW) core with dual load/store slots and dual 64-bit execution slots, and supports grouping of both independent and certain dependent instructions in a single bundle—an extension beyond conventional VLIW designs. Over successive generations the processor has accumulated three distinct compute layers: a scalar VLIW core, the Hexagon Vector eXtensions (HVX) for wide SIMD parallelism, and the Hexagon Tensor Accelerator (HTA) for deep learning inference. This layered design allows Qualcomm to map heterogeneous neural network workloads—convolutional layers to the HTA, activation functions to HVX, and control logic to the scalar core—without transferring intermediate data off the DSP subsystem. The Hexagon processor is central to Qualcomm's on-device AI strategy, enabling inference directly within the SoC at far lower power than offloading to a discrete accelerator.

## Key Claims

- The Hexagon ISA is a 4-issue VLIW architecture with dual load/store slots and dual 64-bit execution slots, first introduced in 2006 on a 65 nm process and reaching its fifth generation (V5) by 2012 on 28 nm.
- Hexagon Vector eXtensions (HVX), introduced in 2013, provide 32 vector registers of 1024-bit width, enabling SIMD operations on byte, halfword, and word elements across the full register width.
- The Hexagon Tensor Accelerator (HTA) debuted in the Snapdragon 855 (2018) as part of the Hexagon 690 DSP, targeting fixed-point deep convolutional neural network (DCNN) inference; the Snapdragon 865 (2019) reached 15 TOPS with the Hexagon 698 and achieved 4× the HTA throughput of its predecessor at 35% better power efficiency.
- The Snapdragon X2 Elite (announced 2025) features the Hexagon NPU 6 with 12 scalar threads on a 4-wide VLIW core (143% throughput increase over prior generation), 8 parallel vector threads supporting FP8 and BF16 formats, and a matrix unit capable of 16,000 multiply-accumulate operations per cycle.
- HTA is programmable through the Qualcomm Neural Processing SDK, the Hexagon-HTA-NN API, and the Android Neural Networks API (NNAPI), allowing the same model to target HTA, HVX, or the scalar core depending on operator support.
- The Hexagon architecture supports up to four hardware threads with configurable vector contexts, allowing the DSP to interleave inference, audio, and sensor-fusion tasks without CPU involvement.

## Relationships

- [[qualcomm_ai_engine]] — The Hexagon DSP is the core compute element of Qualcomm's AI Engine; NSP cores in each Snapdragon SoC are instantiations of the Hexagon architecture.
- [[intel_amx]] — Intel AMX similarly adds a dedicated tile-matrix execution unit on top of an existing scalar ISA; Hexagon's HTA follows the same pattern of layering a tensor unit onto a VLIW scalar core.
- [[apple_neural_engine]] — Apple's ANE takes the opposite design philosophy: a fixed-function matrix engine fully separate from the application processor, versus Hexagon's tightly integrated DSP+tensor approach.
- [[gemmini]] — Gemmini is an open-source research accelerator exploring the same scalar+systolic array composition that the Hexagon HTA exemplifies in a commercial product.
- [[tenstorrent]] — Qualcomm announced an intent to acquire Tenstorrent in 2025, signaling convergence of on-device and datacenter AI acceleration strategies under the Qualcomm portfolio.

## Sources

- Qualcomm Hexagon Wikipedia page: generational history, VLIW description, HVX register width
- Chips and Cheese — "Qualcomm's Hexagon DSP, and now, NPU": microarchitecture analysis, HVX details
- The Chip Letter — "Qualcomm's Hexagon AI Accelerators": HTA introduction timeline, Snapdragon 855/865 TOPS figures
- Qualcomm official docs (RB5 Reference Manual): HTA programming model and SDK integration
- Hot Chips 2013 presentation (Codrescu): original VLIW bundle structure and scalar architecture details
- Semiaccurate (2025): Hexagon NPU 6 specifications for Snapdragon X2 Elite
