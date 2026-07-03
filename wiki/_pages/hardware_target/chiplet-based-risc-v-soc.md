---
canonical_name: Chiplet-Based RISC-V SoC
aliases:
- Chiplet-Based RISC-V SoC with Modular AI Acceleration
- '2509.18355'
subtype: null
tags: []
hardware_targets:
- Chiplet-Based RISC-V SoC
toolchains: []
constraints:
- 7nm RISC-V CPU chiplet
- dual 5nm AI accelerators (15 TOPS INT8 each)
- 16GB HBM3 memory stacks
- 30mm x 30mm silicon interposer
- UCIe with AI-aware extensions
- adaptive cross-chiplet DVFS
- distributed cryptographic security
- sensor-driven load migration
scorecard:
  novelty_delta: 0.8
  claim_density: 0.9
  self_containedness: 0.8
  bridge_score: 0.6
  hub_potential: 0.5
sources:
- raw/cache/9149f34be0ad216b.md
- https://arxiv.org/abs/2509.18355
source_url: https://arxiv.org/abs/2509.18355
fetched_at: '2026-07-03T16:48:10.843643+00:00'
type: hardware_target
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 0
---

# Chiplet-Based RISC-V SoC

The Chiplet-Based RISC-V SoC with Modular AI Acceleration is a proposed heterogeneous architecture that combines a 7nm RISC-V CPU chiplet with dual 5nm AI accelerators on a 30mm x 30mm silicon interposer. The design integrates adaptive cross-chiplet Dynamic Voltage and Frequency Scaling (DVFS), AI-aware Universal Chiplet Interconnect Express (UCIe) protocol extensions with streaming flow control and compression-aware transfers, distributed cryptographic security across heterogeneous chiplets, and intelligent sensor-driven load migration. The system includes 16GB HBM3 memory stacks and dedicated power management controllers. Each AI accelerator delivers 15 TOPS INT8. The architecture targets edge AI applications demanding high performance, energy efficiency, and cost-effectiveness, aiming to overcome monolithic SoC yield limitations.

## Key Claims

- The proposed architecture achieves ~14.7% latency reduction, 17.3% throughput improvement, and 16.2% power reduction compared to previous basic chiplet implementations on MobileNetV2, ResNet-50, and real-time video processing workloads.
- A 40.1% efficiency gain is reported, corresponding to ~3.5 mJ per MobileNetV2 inference (860 mW/244 images/s).
- Sub-5ms real-time capability is maintained across all experimented workloads.
- Four key innovations: adaptive cross-chiplet DVFS, AI-aware UCIe extensions, distributed cryptographic security, and intelligent sensor-driven load migration.

## Relationships

No specific relationship to visible context pages.

## Sources

- https://arxiv.org/abs/2509.18355 (Section: Experimental Results)
