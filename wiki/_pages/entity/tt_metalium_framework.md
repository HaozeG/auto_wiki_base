---
cold_start: true
created: '2026-06-27'
inbound_links: 0
needs_summary_revision: false
scorecard:
  bridge_score: 0.7
  claim_density: 0.6
  hub_potential: 0.6
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://docs.tenstorrent.com/tt-metal/latest/tt-metalium/get_started/get_started.html
tags:
- tenstorrent
- metalium
- framework
- c++-api
- tensix
- ml-acceleration
- dataflow
type: entity
updated: '2026-06-28'
---

# TT-Metalium Framework

TT-Metalium is a low-level C++ programming framework developed by Tenstorrent for accelerating machine learning and non-machine learning workloads on its proprietary Tensix processor architecture. It provides direct hardware control over kernel execution, data movement, and memory management on the Tensix compute array, enabling developers to write highly optimized custom kernels tailored to specific use cases. TT-Metalium sits at the foundation of Tenstorrent's software stack, serving as the abstraction layer between the host system (e.g., x86 CPU) and the Tenstorrent hardware, while higher-level components such as TT-NN and TT-Forge/TT-MLIR build upon it. The framework exposes a three-stage pipeline dataflow pattern consisting of reader kernels that fetch data from DRAM or SRAM into circular buffers, compute kernels that process data using the matrix or vector engines, and writer kernels that store results back to memory. This architecture supports overlay of data movement and computation, facilitating efficient execution across single-core, multi-core, and multi-device configurations.

## Key Claims

- TT-Metalium accelerates both ML and non-ML workloads on Tenstorrent hardware through a C++ API that gives the programmer full control over hardware and data movement.
- It is the lowest-level programmable interface in the Tenstorrent software stack, positioned below TT-Forge/TT-MLIR (high-level compilation), TT-NN (operator library), and above TT-LLK (hardware-specific kernel implementations).
- The programming model follows a bottom-up philosophy: start with a single Tensix core kernel, scale to multiple cores with synchronization, and extend to multiple devices for large model deployment.
- Kernels are structured as a three-stage pipeline: reader (data movement to circular buffers), compute (matrix/vector engines), and writer (data movement to memory). Circular buffers act as FIFOs enabling overlapped execution.
- The Getting Started guide provides six progressive examples: DRAM loopback, element-wise binary kernel, element-wise SFPU kernel, single-core matrix multiplication, multi-core matrix multiplication, and optimized multi-core matrix multiplication.
- Optimization steps for multi-core matrix multiplication include avoiding redundant DRAM reads, avoiding NoC congestion, and maximizing data reuse through broadcast.

## Relationships

- [[gemmini]] — Both Gemmini and TT-Metalium are programmable acceleration frameworks for ML workloads, though Gemmini targets RISC-V-hosted systolic arrays while TT-Metalium targets the Tensix architecture.
- [[tvm_riscv_backend]] — The TVM compiler stack provides a programming model alternative for ML acceleration, similar in abstraction level to TT-Metalium's role in its own hardware ecosystem.
- Insufficient context for additional cross-links: the wiki lacks existing entity pages for Tenstorrent-specific hardware or other Tenstorrent software components.

## Sources

- Tenstorrent TT-Metalium Getting Started documentation: https://docs.tenstorrent.com/tt-metal/latest/tt-metalium/get_started/get_started.html
