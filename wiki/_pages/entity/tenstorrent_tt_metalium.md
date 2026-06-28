---
cold_start: false
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
- https://docs.tenstorrent.com/tt-metal/latest/tt-metalium/index.html
- https://docs.tenstorrent.com/tt-metal/latest/tt-metalium/get_started/get_started.html
- https://docs.tenstorrent.com/tt-metal/latest/tt-metalium/tt_metal/labs/matmul/lab1/lab1.html
tags:
- tenstorrent
- tt-metalium
- tensix
- accelerator
- programming-model
- c++-api
- dataflow
type: entity
updated: '2026-06-28'
---

# Tenstorrent TT-Metalium

TT-Metalium is a low-level C++ programming framework developed by Tenstorrent for programming its Tensix processor — an AI accelerator delivered as a PCIe card targeting Wormhole and Blackhole hardware generations. The framework gives developers direct control over kernel execution, data movement, and memory management on the Tensix compute array. A Tenstorrent device exposes one or more Tensix cores connected via a Network-on-Chip (NoC) to per-chip DRAM (separate from host system memory) and on-chip SRAM (L1 memory). The L1 SRAM acts as explicit working memory — not a cache — requiring programmer-directed data movement. Data is stored and processed in 32×32 tiles, making tile-level data layout a first-class concern. TT-Metalium sits at the foundation of the Tenstorrent software stack: TT-LLK (hardware-specific kernels) → TT-Metalium → TT-NN (operator library) → TT-Forge/TT-MLIR (compilation), with the framework representing the lowest level accessible to application developers.

## Key Claims

- TT-Metalium provides a C++ API for configuring the accelerator, allocating device memory (DRAM and L1 SRAM), and dispatching kernels to Tensix cores from a standard host program.
- The programming model follows a three-stage dataflow pipeline: reader kernels fetch data from DRAM/SRAM into circular buffers; compute kernels process data using the matrix engine (FPU) or vector engine (SFPU); writer kernels store results back to memory. Circular buffers are FIFOs enabling overlapped execution of these stages.
- On-chip SRAM (L1 memory) is explicit working memory, not a cache. Data movement between DRAM, L1, and across cores via NoC is fully programmer-controlled.
- Data and computation are tile-based: the fundamental unit is a 32×32 tile, with conversion between tile and row-major format handled by host-side APIs.
- Advanced multi-core features include multicast data reuse, semaphore-based synchronization, double buffering for improved throughput, and a Device 2.0 Data Movement API with optimized async read/write and single-packet transfers.
- The software stack hierarchy is TT-LLK (low-level kernels, not user-facing) → TT-Metalium → TT-NN → TT-Forge/TT-MLIR. TT-Metalium is distinct from TT-NN; the latter is a higher-level operator library that builds on Metalium for easier model deployment.
- The Getting Started guide provides six progressive examples: DRAM loopback, element-wise binary kernel, element-wise SFPU kernel, single-core matrix multiplication, multi-core matrix multiplication, and optimized multi-core matrix multiplication.
- Multi-core matrix multiplication optimizations include: avoiding redundant DRAM reads by broadcasting shared operands, avoiding NoC congestion by controlling access patterns, and maximizing data reuse through multicast.
- Debugging and profiling tools include DPRINT (in-kernel debug print), Watcher (hang detection), and tt-triage (device health diagnostics).
- The recommended scaling path is: start with a single Tensix core kernel → add multi-core synchronization → extend to multi-device for large model deployment.

## Relationships

- [[tenstorrent]]: TT-Metalium is the primary developer-facing programming interface for Tenstorrent hardware.
- [[tenstorrent_tensix_architecture]]: TT-Metalium directly programs Tensix cores; the SFPU/FPU compute APIs map to the Tensix hardware execution units.
- [[tenstorrent_tt_metal]]: The `tenstorrent/tt-metal` repository is the open-source SDK containing TT-Metalium alongside TT-NN; they are co-distributed.
- [[gemmini]]: Both Gemmini and TT-Metalium are programmable acceleration frameworks for ML workloads; Gemmini targets RISC-V-hosted systolic arrays while TT-Metalium targets the Tensix architecture.
- [[tvm_riscv_backend]]: TVM provides a compiler-level abstraction alternative; TT-Metalium operates one level lower at the bare-metal kernel API.

## Sources

- https://docs.tenstorrent.com/tt-metal/latest/tt-metalium/index.html
- https://docs.tenstorrent.com/tt-metal/latest/tt-metalium/get_started/get_started.html
- https://docs.tenstorrent.com/tt-metal/latest/tt-metalium/tt_metal/labs/matmul/lab1/lab1.html
