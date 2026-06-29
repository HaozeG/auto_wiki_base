---
cold_start: true
created: '2025-07-11'
inbound_links: 0
scorecard:
  bridge_score: 0.6
  claim_density: 0.6
  hub_potential: 0.7
  novelty_delta: 0.9
  self_containedness: 0.8
sources:
- https://iopscience.iop.org/article/10.1088/2634-4386/ae688e
tags:
- RISC-V
- SNN
- FPGA
- spiking neural network
- SoC
- vector processor
- DMA
type: entity
updated: '2026-06-29'
---

# FeNN-DMA: A RISC-V SoC for Spiking Neural Network Acceleration

FeNN-DMA is a complete System-on-Chip (SoC) design based on an extended version of the FeNN RISC-V vector processor core, tailored to simulating Spiking Neural Networks (SNNs) on modern UltraScale+ FPGAs. The SoC integrates a RISC-V softcore with a vector co-processor and a DMA controller, designed to address the memory-bound nature of SNN workloads by leveraging FPGA capabilities for high off-chip memory bandwidth and low arithmetic intensity. The design supports complex neuron models and network topologies beyond what fixed-function accelerators allow, and can simulate up to 16 thousand neurons and 256 million synapses per core. FeNN-DMA demonstrates comparable resource usage and energy requirements to state-of-the-art fixed-function SNN accelerators while providing greater programmability.

## Key Claims

- FeNN-DMA is a fully programmable RISC-V SoC for SNN acceleration on UltraScale+ FPGAs.
- Supports up to 16,000 neurons and 256 million synapses per core.
- Comparable resource usage and energy to state-of-the-art fixed-function SNN accelerators.
- Supports more complex neuron models and network topologies than fixed-function accelerators.
- Based on the FeNN RISC-V vector processor with additional DMA and system integration.
- Designed to exploit FPGA off-chip memory bandwidth for memory-bound SNN workloads.

## Relationships

- [[Parallel_GEMM_Convolution_on_GAP8]] – A related optimization recipe for convolution on a RISC-V platform, demonstrating alternative AI acceleration strategies.
- [[Chiplet_RISC_V_AI_SoC_Benchmark_Results]] – Benchmark results for a different RISC-V AI chiplet architecture, providing a comparison for performance and efficiency.
- (Note: insufficient context for additional cross-links to entity pages; linked pages above are benchmark and optimization recipes.)

## Sources

- [FeNN-DMA: A RISC-V system-on-chip for spiking neural network acceleration – IOP Science](https://iopscience.iop.org/article/10.1088/2634-4386/ae688e)
