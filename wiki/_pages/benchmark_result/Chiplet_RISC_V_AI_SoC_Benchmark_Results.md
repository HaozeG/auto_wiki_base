---
cold_start: false
created: '2025-03-25'
datatypes:
- INT8
evidence_strength: reported
hardware_targets:
- 7nm RISC-V CPU chiplet
- 5nm AI accelerator
hardware_versions:
- 7nm RISC-V CPU chiplet
- 5nm AI accelerator (15 TOPS INT8)
inbound_links: 6
measurement_method: Experimental results across industry standard benchmarks (MobileNetV2,
  ResNet-50, real-time video) compared to previous basic chiplet implementations.
metrics:
- latency
- throughput
- power
- energy
- efficiency
needs_summary_revision: true
scorecard:
  bridge_score: 0.8
  claim_density: 0.8
  hub_potential: 0.7
  novelty_delta: 0.9
  self_containedness: 0.9
software_versions: []
sources:
- https://arxiv.org/abs/2509.18355
tags:
- RISC-V
- chiplet
- AI accelerator
- MobileNetV2
- ResNet-50
toolchains: []
type: benchmark_result
updated: '2026-06-28'
workloads:
- MobileNetV2
- ResNet-50
- real-time video processing
---

# Chiplet-Based RISC-V AI SoC Benchmark Results

Benchmark results for the Chiplet-Based RISC-V SoC with Modular AI Acceleration are reported in the paper 'Chiplet-Based RISC-V SoC with Modular AI Acceleration' (arXiv:2509.18355). The architecture integrates a 7nm RISC-V CPU chiplet with dual 5nm AI accelerators (15 TOPS INT8 each), 16GB HBM3 memory, and adaptive DVFS and UCIe extensions. Measurements were conducted on MobileNetV2, ResNet-50, and real-time video processing workloads. The AI-optimized configuration demonstrates a ~14.7% latency reduction, 17.3% throughput improvement, 16.2% power reduction, and a 40.1% efficiency gain, achieving ~3.5 mJ per MobileNetV2 inference at 860 mW and 244 images/s, with sub-5ms latency across all workloads. Comparison is made against previous basic chiplet implementations.

## Key Claims

- ~14.7% latency reduction compared to basic chiplet implementations.
- 17.3% throughput improvement.
- 16.2% power reduction.
- 40.1% efficiency gain.
- ~3.5 mJ per MobileNetV2 inference (860 mW, 244 images/s).
- Sub-5ms latency across all workloads.

## Measurement Context

- Hardware version: 7nm RISC-V CPU chiplet; dual 5nm AI accelerators (15 TOPS INT8 each) on a 30mm x 30mm silicon interposer; 16GB HBM3 memory.
- Software/toolchain version: Not specified in available resource.
- Workload shape: MobileNetV2 (image classification), ResNet-50 (image classification), real-time video processing (unspecified resolution).
- Metric: Latency (ms), throughput (images/s), power (mW), energy (mJ), efficiency gain (%).
- Method: Experimental results comparing this architecture to previous basic chiplet implementations.
- Evidence strength: reported (claims from paper; actual measurement setup not detailed in abstract).

## Relationships

- [[Chiplet_RISC_V_AI_SoC_Architecture]] – Entity page describing this architecture.
- [[DSC_Fused_Dataflow_Benchmark_Results]] – Another benchmark for a RISC-V AI accelerator on different hardware.

## Sources

- [arXiv:2509.18355](https://arxiv.org/abs/2509.18355)

