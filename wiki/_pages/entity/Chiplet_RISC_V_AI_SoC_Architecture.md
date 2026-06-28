---
cold_start: true
created: '2025-03-25'
inbound_links: 2
scorecard:
  bridge_score: 0.8
  claim_density: 0.8
  hub_potential: 0.7
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://arxiv.org/abs/2509.18355
tags:
- RISC-V
- chiplet
- AI accelerator
- UCIe
- DVFS
- edge AI
type: entity
updated: '2026-06-28'
---

# Chiplet-Based RISC-V SoC with Modular AI Acceleration

The Chiplet-Based RISC-V SoC with Modular AI Acceleration is a novel architecture designed for edge AI devices, addressing the limitations of monolithic SoC designs such as low manufacturing yields at advanced process nodes. It integrates a 7nm RISC-V CPU chiplet with dual 5nm AI accelerators providing 15 TOPS INT8 each, along with 16GB HBM3 memory stacks and dedicated power management controllers. Key innovations include adaptive cross-chiplet Dynamic Voltage and Frequency Scaling (DVFS), AI-aware Universal Chiplet Interconnect Express (UCIe) protocol extensions with streaming flow control and compression-aware transfers, distributed cryptographic security, and intelligent sensor-driven load migration. The architecture is implemented on a 30mm x 30mm silicon interposer and achieves significant performance improvements over basic chiplet implementations, including ~14.7% latency reduction, 17.3% throughput improvement, and 16.2% power reduction on benchmarks such as MobileNetV2, ResNet-50, and real-time video processing.

## Key Claims

- Integrates a 7nm RISC-V CPU chiplet with dual 5nm AI accelerators (15 TOPS INT8 each) and 16GB HBM3 memory stacks.
- Achieves ~14.7% latency reduction, 17.3% throughput improvement, and 16.2% power reduction compared to previous basic chiplet implementations.
- Delivers a 40.1% efficiency gain corresponding to ~3.5 mJ per MobileNetV2 inference at 860 mW and 244 images/s.
- Maintains sub-5ms real-time capability across all experimented workloads (MobileNetV2, ResNet-50, real-time video).

## Relationships

- [[DSC_Fused_Dataflow_Benchmark_Results]] – This benchmark result for a different RISC-V AI accelerator provides contrast in measurement methodology and performance targets.
- [[Chiplet_RISC_V_AI_SoC_Benchmark_Results]] – Detailed benchmark results of this architecture.

Insufficient context for additional entity cross-links.

## Sources

- [arXiv:2509.18355](https://arxiv.org/abs/2509.18355)

