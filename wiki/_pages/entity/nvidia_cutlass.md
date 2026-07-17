---
canonical_name: NVIDIA CUTLASS
aliases:
- CUTLASS
- CUTLASS 4.6.0
subtype: null
tags: []
scorecard:
  novelty_delta: 0.7
  claim_density: 0.8
  self_containedness: 1.0
  bridge_score: 0.5
  hub_potential: 0.6
sources:
- raw/cache/4aa78f52f58ac122.md
- https://docs.nvidia.com/cutlass/4.6.0/overview.html
source_url: https://docs.nvidia.com/cutlass/4.6.0/overview.html
fetched_at: '2026-07-17T12:40:08.821557+00:00'
type: entity
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 0
outbound_links:
- target: nvidia_blackwell_ultra
  reason: CUTLASS 4.6 provides template abstractions and CuTe DSL support for implementing
    high-performance GEMM kernels on the Blackwell Ultra architecture, including support
    for block-scaled NVFP4 data types introduced in Blackwell
- target: nvidia_hopper_architecture
  reason: CUTLASS supports the Hopper architecture's Tensor Cores and Transformer
    Engine, enabling efficient mixed-precision matrix operations for transformer workloads
---

# NVIDIA CUTLASS

NVIDIA CUTLASS is a CUDA C++ template library providing modular abstractions for implementing high-performance matrix-matrix multiplication (GEMM) and related linear algebra computations at all levels within the CUDA parallel programming model. It decomposes the hierarchical decomposition and data movement strategies of GPU kernel execution into reusable software components, enabling specialization via custom tiling sizes, data types, and algorithmic policies. CUTLASS has been actively developed since 2017 and supports a wide range of numeric types including FP64, FP32, TF32, FP16, BF16, 8-bit floating point (e5m2, e4m3), block-scaled types (NVIDIA NVFP4, OCP MXFP4, MXFP6, MXFP8), narrow integer types (4 and 8-bit signed/unsigned), and binary 1-bit data, across NVIDIA GPU architectures from Volta through Blackwell.

## Key Claims

- CUTLASS is a collection of reusable, modular C++ template abstractions for high-performance GEMM and related computations in CUDA.
- Supports mixed-precision computations including FP64, FP32, TF32, FP16, BF16, 8-bit floating point (e5m2, e4m3), block-scaled data types (NVFP4, MXFP4, MXFP6, MXFP8), narrow integer types (4 and 8-bit signed/unsigned), and binary 1-bit data types.
- Supports NVIDIA GPU architectures from Volta, Turing, Ampere, Ada, Hopper, and Blackwell.
- CUTLASS 4 introduces domain-specific languages (DSLs) with CuTe DSL as the first release, providing a Python-native interface for writing high-performance CUDA kernels without C++ expertise.
- CuTe DSL targets Tensor Cores on Ampere, Hopper, and Blackwell architectures for optimal matrix multiply and linear algebra operations.
- CUTLASS 4.6.0 adds fine-grained compilation API (cute.compile_to), in-kernel event tracing (IKET) profiler, AoT cross-compilation for aarch64-linux-gnu, and automatic shared memory size calculation.
- The library provides primitives for hierarchical parallelization that can be specialized via custom tiling sizes, data types, and algorithmic policies.
- CuTe DSL is currently in public beta and is expected to graduate by end of summer 2026.

## Relationships

- [[nvidia_blackwell_ultra]]: CUTLASS 4.6 provides template abstractions and CuTe DSL support for implementing high-performance GEMM kernels on the Blackwell Ultra architecture, including support for block-scaled NVFP4 data types introduced in Blackwell.
- [[nvidia_hopper_architecture]]: CUTLASS supports the Hopper architecture's Tensor Cores and Transformer Engine, enabling efficient mixed-precision matrix operations for transformer workloads.

## Sources

- [Overview — NVIDIA CUTLASS Documentation](raw/cache/4aa78f52f58ac122.md)
