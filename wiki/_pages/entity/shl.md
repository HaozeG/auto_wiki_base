---
canonical_name: SHL
aliases:
- Structure of Heterogeneous Library
- ShiHulan
subtype: null
tags: []
scorecard:
  novelty_delta: 0.8
  claim_density: 0.5
  self_containedness: 0.8
  bridge_score: 0.4
  hub_potential: 0.2
sources:
- raw/cache/7f3fb17b96da7520.md
- https://github.com/BHbean/shl
- raw/cache/6bfe8d9346f64c5e.md
- https://github.com/XUANTIE-RV/riscv-matrix-extension-spec/blob/master/doc/shl/introduce.adoc
source_url: https://github.com/BHbean/shl
fetched_at: '2026-07-03T13:24:16.338757+00:00'
type: entity
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 1
outbound_links:
- target: xuantie-ai-benchmark-suite
  reason: SHL is referenced as a toolchain in the XuanTie AI Benchmark Suite, providing
    optimized neural network operators for XuanTie CPUs
---

# SHL

SHL (Structure of Heterogeneous Library, also known by its Chinese name ShiHulan) is a high-performance heterogeneous computing library provided by T-HEAD, the semiconductor design division of Alibaba Group. SHL provides a series of optimized binary libraries for neural network inference on XuanTie CPU platforms, using the CSI-NN2 neural network library API as its interface. The library is designed to work with the HHB toolchain, which quantizes and compiles neural networks; SHL is then called automatically during inference. In principle, SHL only provides reference implementations for XuanTie CPU targets, while optimization for each NPU target platform is left to the respective vendor. This design allows SHL to serve as a unified library that can be extended for heterogeneous computing across different T-HEAD processors.

## Key Claims

- SHL is a high-performance heterogeneous computing library from T-HEAD.
- It uses the CSI-NN2 API for XuanTie CPU platforms.
- It provides optimized binary libraries for neural network inference.
- It integrates with the HHB toolchain for quantization and compilation.
- SHL only provides reference implementations for XuanTie CPU; NPU optimizations are vendor-specific.

## Relationships

- [[xuantie-ai-benchmark-suite]]: SHL is referenced as a toolchain in the XuanTie AI Benchmark Suite, providing optimized neural network operators for XuanTie CPUs.

## Sources

- https://github.com/BHbean/shl
