---
canonical_name: CUTIE
aliases:
- TCN-CUTIE
subtype: null
tags: []
hardware_targets:
- CUTIE
toolchains: []
constraints: []
scorecard:
  novelty_delta: 0.8
  claim_density: 0.7
  self_containedness: 0.9
  bridge_score: 0.3
  hub_potential: 0.4
sources:
- raw/cache/147307ccdc6cecb7.md
- https://www.connectedpapers.com/main/10df6f507dcce20cb51700eb1021ceb2caad9bd2/Ternarized-TCN-for-$\mu-\mathrm{J}/\text{Inference}$-Gesture-Recognition-from-DVS-Event-Frames/graph
source_url: https://www.connectedpapers.com/main/10df6f507dcce20cb51700eb1021ceb2caad9bd2/Ternarized-TCN-for-$\mu-\mathrm{J}/\text{Inference}$-Gesture-Recognition-from-DVS-Event-Frames/graph
fetched_at: '2026-07-02T12:06:29.126058+00:00'
type: hardware_target
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# CUTIE (Ternary Neural Network Accelerator)

CUTIE is an all-digital ternary neural network accelerator fabricated in 22nm FDX (FDSOI) technology. It is designed for extreme-edge inference, targeting applications such as Dynamic Vision Sensor (DVS)-based gesture recognition. The accelerator leverages ternary weights and activations to achieve high energy efficiency, with reported metrics of 1,036 TOp/s/W, 2.72 ≩J per inference, and 12.2 mW power consumption. It supports fully ternarized Temporal Convolutional Networks (TCNs) and is coupled with post-synthesis power simulation results showing inference energy as low as 1.7 ≩J per input frame. No specific ISA or compiler support is detailed in available sources, but the design is optimized for direct mapping of ternarized neural network layers.

## Key Claims

- Fabricated in 22nm FDX technology.
- Achieves 1,036 TOp/s/W energy efficiency.
- Consumes 12.2 mW of power.
- Delivers 2.72 ≩J per inference (accelerator-level measurement).
- Enables 1.7 ≩J per inference for a Ternarized TCN on DVS gesture recognition (post-synthesis simulation).
- All-digital design with ternary weights and activations.

## Optimization-Relevant Details

- ISA/profile: Not specified; likely no standard ISA (custom accelerator).
- Vector/matrix/accelerator support: Dedicated ternary neural network accelerator.
- Memory/cache/TLB/DMA: Not detailed.
- Compiler/toolchain support: Not specified.

## Relationships

- [[gap9-vs-stm32f7-odtl-benchmark]]: Another edge AI benchmark comparison; CUTIE represents a distinct approach using ternary precision for ultra-low energy inference.
- [[cpa-factored-gemmini-systolic-array]]: Gemmini is a systolic array generator for machine learning; CUTIE is a specialized ternary accelerator, contrasting in design philosophy.
- Insufficient context for additional cross-links; no existing entity pages for ternary accelerators or DVS-specific workloads are present in the wiki.

## Sources

- https://www.connectedpapers.com/main/10df6f507dcce20cb51700eb1021ceb2caad9bd2/Ternarized-TCN-for-$\mu-\mathrm{J}/\text{Inference}$-Gesture-Recognition-from-DVS-Event-Frames/graph
