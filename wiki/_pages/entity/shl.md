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
updated: '2026-07-06'
cold_start: true
inbound_links: 2
outbound_links:
- target: xuantie-ai-benchmark-suite
  reason: SHL is referenced as a toolchain in the XuanTie AI Benchmark Suite, providing
    optimized neural network operators for XuanTie CPUs
---

# SHL

SHL (Structure of Heterogeneous Library, also known by its Chinese name ShiHulan) is a high-performance heterogeneous computing library developed by T-HEAD, the semiconductor design division of Alibaba Group, for the XuanTie CPU platform. SHL provides optimized binary libraries for neural network inference using the CSI-NN2 neural network library API, supporting both reference C implementations and assembly optimizations for XuanTie CPUs. It supports symmetric and asymmetric quantization, 8-bit, 16-bit, and FP16 data types, and is compatible with both NCHW and NHWC tensor formats. The library is designed to work with the HHB toolchain, which quantizes and compiles neural networks; SHL is then called automatically during inference. SHL covers different architectures including CPU, DSP, NPU, and GPU, and provides a reference heterogeneous schedule implementation. It uses a per-layer API for CPU and DSP execution and a graph execution mode for NPU and GPU, with a modular architecture that includes Vector Instruction OPT and Driver Wrapper modules. In principle, SHL only provides reference implementations for XuanTie CPU targets, while optimization for each NPU target platform is left to the respective vendor. This design allows SHL to serve as a unified library that can be extended for heterogeneous computing across different T-HEAD processors.

## Key Claims

- SHL is a high-performance heterogeneous computing library from T-HEAD.
- It uses the CSI-NN2 API for XuanTie CPU platforms.
- It provides both reference C implementations and assembly-optimized binary libraries for neural network inference.
- It integrates with the HHB toolchain for quantization and compilation.
- Supports symmetric and asymmetric quantization, and data types 8-bit, 16-bit, and FP16.
- Compatible with NCHW and NHWC tensor formats.
- Covers CPU, DSP, NPU, and GPU architectures with a reference heterogeneous schedule; per-layer API for CPU/DSP, graph execution for NPU/GPU.
- Modular architecture includes Vector Instruction OPT, Driver Wrapper, and Reference Runtime modules.
- Buildable from source via git clone and make targets (x86 reference, C906 optimization).
- SHL only provides reference implementations for XuanTie CPU; NPU optimizations are vendor-specific.

## Relationships

- [[xuantie-ai-benchmark-suite]]: SHL is referenced as a toolchain in the XuanTie AI Benchmark Suite, providing optimized neural network operators for XuanTie CPUs.
- [[c908-wino-gemm-optimization]]: SHL is the library that implements the Winograd and GEMM optimization techniques described on that page for the XuanTie C908.

## Sources

- https://github.com/BHbean/shl
- https://github.com/XUANTIE-RV/riscv-matrix-extension-spec/blob/master/doc/shl/introduce.adoc
