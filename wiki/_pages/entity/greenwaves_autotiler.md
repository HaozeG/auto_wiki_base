---
cold_start: true
created: '2025-02-24'
inbound_links: 0
needs_summary_revision: false
scorecard:
  bridge_score: 0.7
  claim_density: 0.6
  hub_potential: 0.6
  novelty_delta: 0.7
  self_containedness: 0.9
sources:
- https://github.com/GreenWaves-Technologies/gap_sdk/blob/master/tools/docs/autotiler.rst
tags:
- greenwaves
- gap-sdk
- autotiler
- memory-management
- neural-network-compilation
type: entity
updated: '2026-06-28'
---

# Autotiler

The Autotiler is a C library developed by GreenWaves Technologies as part of the GAP SDK for GAP-series processors (GAP8, GAP9). It runs on the user's PC prior to target code compilation and automatically generates optimized C code for memory tiling and data transfers across the multi-level memory hierarchy of GAP chips. The generated code leverages the micro-DMA (uDMA) engine for bulk transfers from external memories (Flash and L3) into the L2 memory and the cluster-DMA engine for transfers from L2 to the tightly-coupled L1 memory. The Autotiler is an integral component of the GapFlow toolchain, which converts neural network models in ONNX and TensorFlow Lite formats into efficiently tiled GAP code. It provides a set of pre-built generators for common signal processing and neural network layers such as convolutions, pooling, linear layers, and softmax, and also allows users to create custom generators for their own algorithms.

## Key Claims

- The Autotiler runs on the host PC before GAP compilation and produces C code implementing memory tiling and DMA transfers across L1, L2, and L3 memory levels.
- The generated code uses uDMA for L3/L2 transfers and cluster-DMA for L2/L1 transfers, enabling efficient data movement.
- It is part of the GapFlow toolchain, which converts ONNX and TFlite models into GAP code.
- Pre-built generators are provided for CNN/RNN layers, sound, and image processing, and users can create new generators.
- The library includes a model framework where a list of generator calls and optionally a graph interconnect define the processing pipeline.
- An example MNIST model is provided in the SDK demonstrating convolutional, linear, and softmax layers using the Autotiler API.

## Relationships

- [[tvm_riscv_backend]] — Both the Autotiler and TVM serve as model compilation tools targeting RISC-V based accelerators, though the Autotiler is specific to GreenWaves GAP processors while TVM is vendor-agnostic.
- [[gemmini]] — Gemmini is a systolic array generator for RISC-V systems; the Autotiler performs a similar role in generating optimized compute kernels for a specific memory hierarchy, but at the software level rather than hardware generation.
- Insufficient context for additional cross-links; GreenWaves GAP8/GAP9 pages are not yet present in the wiki.

## Sources

- https://github.com/GreenWaves-Technologies/gap_sdk/blob/master/tools/docs/autotiler.rst

