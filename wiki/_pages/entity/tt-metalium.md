---
canonical_name: TT-Metalium
aliases:
- tt-metal
- TT-Metalium
- tt-metalium
- Tenstorrent Metalium
- Metalium
- TT-Metalium programming model
subtype: null
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.7
  self_containedness: 0.9
  bridge_score: 0.6
  hub_potential: 0.8
sources:
- raw/cache/d4ff3eb460f806ad.md
- https://docs.tenstorrent.com/tt-metal/latest/tt-metalium/get_started/get_started.html
- raw/cache/b34a6dc3b6ec45d2.md
- https://github.com/afuller-TT/tt-metalium
- raw/cache/8a04855274dd9c94.md
- https://github.com/tenstorrent/tt-metal/blob/main/METALIUM_GUIDE.md
source_url: https://docs.tenstorrent.com/tt-metal/latest/tt-metalium/get_started/get_started.html
fetched_at: '2026-07-09T10:01:57.311293+00:00'
type: entity
created: '2026-07-09'
updated: '2026-07-09'
cold_start: false
inbound_links: 1
outbound_links:
- target: blackhole
  reason: TT-Metalium is the low-level software layer for all Tenstorrent hardware,
    including the Blackhole chip. The Blackhole's Tensix cores execute kernels programmed
    through TT-Metalium's API, making this framework the foundational tool for developing
    optimized workloads on Tenstorrent accelerators
- target: tenstorrent-memory-model
  reason: TT-Metalium's kernel programming model is built directly on Tenstorrent's
    (x, y, local_address) NoC-tuple memory addressing scheme, documented in detail
    on the Tenstorrent Memory Model page.
needs_summary_revision: false
---

# TT-Metalium

TT-Metalium is a low-level C++ programming interface and SDK developed by Tenstorrent for accelerating machine learning and non-machine learning workloads on Tenstorrent's Tensix hardware. It provides a programming model that exposes three kernel types per Tensix core: a reader kernel for data input, a compute kernel for the main arithmetic operations, and a writer kernel for data output. These kernels coordinate through circular buffers in the core's local SRAM, enabling a software-pipelined execution pattern with explicit data movement and overlapped execution of data movement and computation. TT-Metalium sits at the foundation of Tenstorrent's software stack, beneath the higher-level TTNN library of common ML operations and the TT-Forge/TT-MLIR compilation frameworks. The Metalium stack provides compute APIs and data movement APIs that abstract underlying hardware details while allowing developers to control resource allocation, kernel dispatch, and a fast dispatch mechanism for efficient kernel launches. It supports a Single Program Multiple Data (SPMD) paradigm for scaling workloads across multiple Tensix cores and chips. The architecture natively operates on 32×32 tiles, and the programming model is designed to minimize DRAM access by leveraging the local L1 SRAM hierarchy and dual NoC interconnect. Metalium kernels are compiled to the Baby RISC-V cores for instruction dispatch, not for direct computation, making the programming model distinct from CUDA-style thread-level parallelism.

Operations are typically designed bottom-up: starting with a single Tensix core kernel, then scaling to multiple cores, and finally to multiple devices. The getting started guide progresses through six steps: DRAM Loopback, Eltwise Binary Kernel (FPU matrix engine), Eltwise SFPU (vector engine), Single-core Matrix Multiplication, Multi-core Matrix Multiplication, and Optimized Multi-core Matrix Multiplication. Step 6 optimizes multi-core matmul by exploiting grid structure, avoiding redundant DRAM reads and NoC congestion through broadcast data sharing.

TT-Metalium is also open-source and provides a kernel development programming model that gives close-to-metal access to Tenstorrent's AI accelerator chips. Installation is available via four methods: pre-built binaries (via wheel), a Docker release image, building from source, or using Anaconda. The source installation involves cloning the repository and building the library. The SDK is part of the tt-metal repository, which also includes the TT-NN operator library.

## Key Claims

- TT-Metalium is a C++ framework for writing and executing kernels on Tenstorrent Tensix hardware.
- Each Tensix kernel set includes three distinct kernel types: reader, compute, and writer, coordinated via circular buffers in SRAM.
- It provides full programmer control over hardware resources and data movement for performance optimization.
- The software stack hierarchy is: TT-Forge/TT-MLIR (high-level compilation) → TTNN (ML kernel library) → TT-Metalium (low-level interface) → TT-LLK (hardware-specific kernels).
- Kernels follow a three-stage pipeline: Reader Kernel (data movement from DRAM/SRAM to circular buffers), Compute Kernel (matrix/vector engine processing), Writer Kernel (writing results back).
- Circular buffers act as FIFO structures enabling communication and synchronization between kernels.
- Metalium provides compute APIs and data movement APIs for kernel development, ensuring compatibility across hardware generations.
- Fast dispatch is a mechanism for efficient kernel launch and resource management.
- SPMD (Single Program Multiple Data) is supported for multi-core and multi-chip scaling.
- The programming model is built for the tile-based (32×32) architecture and capitalizes on local L1 SRAM and the dual NoC wraparound topology.
- Metalium kernels are compiled to the Baby RISC-V cores for instruction dispatch, not for direct computation, distinguishing it from CUDA-style thread-level parallelism.
- The getting started guide progresses through six steps: DRAM Loopback, Eltwise Binary Kernel (FPU matrix engine), Eltwise SFPU (vector engine), Single-core Matrix Multiplication, Multi-core Matrix Multiplication, and Optimized Multi-core Matrix Multiplication.
- Step 6 optimizes multi-core matmul by exploiting grid structure, avoiding redundant DRAM reads and NoC congestion through broadcast data sharing.
- TT-Metalium is open-source and serves as the foundation for the TT-NN operator library.
- Installation supports four methods: pre-built binaries, Docker, source build, and Anaconda.
- The SDK targets custom kernel development and experimentation on Tenstorrent hardware, providing close-to-metal access.

## Relationships

- [[tensix-core]]: TT-Metalium programs each Tensix core with a set of three kernels (reader, compute, writer) that map to the core's hardware resources.
- [[blackhole]]: TT-Metalium is the low-level software layer for all Tenstorrent hardware, including the Blackhole chip. The Blackhole's Tensix cores execute kernels programmed through TT-Metalium's API, making this framework the foundational tool for developing optimized workloads on Tenstorrent accelerators.

- [[tenstorrent-memory-model]]: TT-Metalium's kernel programming model is built directly on Tenstorrent's (x, y, local_address) NoC-tuple memory addressing scheme, documented in detail on the Tenstorrent Memory Model page.

## Sources

- https://docs.tenstorrent.com/tt-metal/latest/tt-metalium/get_started/get_started.html
- https://github.com/afuller-TT/tt-metalium
- https://github.com/tenstorrent/tt-metal/blob/main/METALIUM_GUIDE.md
