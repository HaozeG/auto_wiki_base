---
canonical_name: TT-Forge-ONNX
aliases:
- TT-Forge ONNX
- tt-forge-onnx
subtype: null
tags: []
scorecard:
  novelty_delta: 0.8
  claim_density: 0.5
  self_containedness: 1.0
  bridge_score: 0.5
  hub_potential: 0.3
sources:
- raw/cache/36835d6301e580b1.md
- https://github.com/tenstorrent/tt-forge-onnx
source_url: https://github.com/tenstorrent/tt-forge-onnx
fetched_at: '2026-07-09T11:17:52.189503+00:00'
type: entity
created: '2026-07-09'
updated: '2026-07-09'
cold_start: true
inbound_links: 1
---

# TT-Forge-ONNX

TT-Forge-ONNX is a graph compiler for running ONNX, TensorFlow, and PaddlePaddle models on Tenstorrent hardware, optimizing computational graphs for performance and efficiency. It is a TVM-based frontend within the TT-Forge compiler ecosystem. It supports compilation for Tenstorrent hardware including Wormhole and Blackhole chips, and is designed for single-chip configurations only. The frontend supports over 70 ONNX operations and can load models exported from PyTorch, TensorFlow, and PaddlePaddle. TT-Forge-ONNX is part of a larger Tenstorrent software stack that also includes TT-XLA for PyTorch and JAX, TT-MLIR as the core MLIR-based compiler framework, and TT-Metal for low-level kernel development.

## Key Claims

- TT-Forge-ONNX supports ONNX, TensorFlow, and PaddlePaddle model formats as input.
- It is a TVM-based frontend within the broader TT-Forge compiler ecosystem.
- It compiles models for Tenstorrent hardware platforms including Wormhole and Blackhole.
- TT-Forge-ONNX is restricted to single-chip configurations only.
- The frontend supports over 70 ONNX operations.
- PyTorch models are also supported, but Tenstorrent recommends using TT-XLA for PyTorch and JAX.
- Installation is available via pip from a private Tenstorrent package index.

## Relationships

- [[tt-xla-performance-optimization-techniques]] describes optimization techniques for the TT-XLA frontend. TT-Forge-ONNX is a companion frontend within the same Tenstorrent compiler ecosystem but targets ONNX, TensorFlow, and PaddlePaddle models instead of PyTorch and JAX, and is limited to single-chip configurations. Both frontends share the same TT-MLIR compiler backend and Tenstorrent hardware targets (Wormhole, Blackhole).

## Sources

- https://github.com/tenstorrent/tt-forge-onnx
