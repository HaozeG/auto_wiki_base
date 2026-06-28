---
cold_start: false
created: '2026-06-27'
inbound_links: 0
needs_summary_revision: true
scorecard:
  bridge_score: 0.3
  claim_density: 0.6
  hub_potential: 0.7
  novelty_delta: 0.9
  self_containedness: 0.85
sources:
- https://deepwiki.com/tenstorrent/tt-metal
tags:
- tenstorrent
- AI-accelerator
- software-stack
- TT-NN
- TT-Metalium
type: entity
updated: '2026-06-28'
---

# tenstorrent/tt-metal

The tenstorrent/tt-metal repository is the primary software stack for Tenstorrent AI accelerators, comprising a two-tier architecture: TT-NN, a high-level neural network operation library with Python and C++ APIs for tensor operations, collective communications, and model primitives; and TT-Metalium, a low-level programming model and runtime that provides direct access to the Tensix cores, Ethernet cores, and the Network-on-Chip (NoC). The stack is designed to support both high-level productivity for model developers and low-level performance for kernel programmers, enabling optimized execution of large language models such as Llama 3.3, Qwen 2.5, and DeepSeek-R1. The repository includes the Fast Dispatch command queue system for low-latency kernel submission, a JIT build system for on-the-fly RISC-V kernel compilation using the SFPI toolchain, and a comprehensive tensor abstraction layer with support for sharding and distributed execution across multi-chip topologies.

## Key Claims

- TT-Metalium provides hardware abstraction through IDevice with implementations for single chips (Device) and multi-chip clusters (MeshDevice).
- The Fast Dispatch system (HWCommandQueue) manages low-latency command submission to dispatch cores.
- The JIT build system handles on-the-fly compilation of RISC-V kernels using JitBuildEnv and the SFPI toolchain.
- TT-NN provides a tensor abstraction (ttnn::Tensor) managing multi-dimensional data layouts, memory configurations, and sharding strategies.
- Optimized implementations of matmul, convolutions, and transformer-specific ops are used in models like Llama 3.3, Qwen 2.5, and DeepSeek-R1.
- Distributed execution supports Tensor Parallelism (TP) and Data Parallelism (DP) across MeshDevice topologies, critical for large models like Llama 3.3 70B with TP=32.
- The stack is layered from user space (models/demos) through TT-NN, TT-Metalium, LLRT, and hardware execution (umd, firmware).

## Relationships

- [[risc_v_vector_extension]]: The tt-metal JIT build system compiles kernels targeting the RISC-V vector-like Tensix architecture, positioning it as an alternative to standard RISC-V vector extensions for AI acceleration.
- [[tvm_riscv_backend]]: Both tt-metal and the TVM RISC-V backend provide compiler-based optimization and kernel generation for AI hardware, though tt-metal is specific to Tenstorrent while TVM targets multiple backends.

## Sources

- https://deepwiki.com/tenstorrent/tt-metal
