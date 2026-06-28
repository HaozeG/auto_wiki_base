---
cold_start: true
created: '2026-06-27'
inbound_links: 0
needs_summary_revision: false
scorecard:
  bridge_score: 0.5
  claim_density: 0.3
  hub_potential: 0.6
  novelty_delta: 0.8
  self_containedness: 0.9
sources:
- https://docs.tenstorrent.com/tt-metal/latest/tt-metalium/index.html
tags:
- tenstorrent
- software-stack
- programming-model
- ai-accelerator
type: entity
updated: '2026-06-28'
---

# TT-Metalium

TT-Metalium is a software stack and programming model developed by Tenstorrent for programming their AI accelerator hardware, including Wormhole and Blackhole processors. It provides a low-level API for direct control over Tensix cores, data movement via NoC (Network-on-Chip), circular buffers for efficient data streaming, and kernel management for both compute and data movement operations. TT-Metalium supports various programming paradigms including single-core and multi-core kernels, multicast communication, and synchronization via semaphores. The documentation includes comprehensive programming examples for operations such as matrix multiplication (Matmul), element-wise binary operations, and custom SFPU (Single-Format Processing Unit) operations. It also offers debugging and profiling tools such as DPRINT, Watcher, and tt-triage. TT-Metalium is distinct from TT-NN, a higher-level library that builds on Metalium for easier model deployment.

## Key Claims

- TT-Metalium provides a programmable interface to Tenstorrent's Tensix architecture, supporting DRAM and SRAM buffer allocation, circular buffers, and kernel creation for data movement and compute.
- It supports advanced multi-core features including multicast data reuse, semaphore-based synchronization, and double buffering for improved throughput.
- The stack includes a Device 2.0 Data Movement API with optimized async read/write operations and single-packet transfers.
- Compute APIs include matrix engine (FPU) and vector engine (SFPU) operations, covering arithmetic, transcendental, comparison, and integer operations.
- Debugging tools such as DPRINT (debug print), Watcher (hang debugging), and device profiling are integrated.
- TT-Metalium uses a tile-based architecture where data is stored and processed in 32x32 tiles, with conversion between tiles and row-major format.

## Relationships

- [[risc_v_vector_extension]]: Tenstorrent processors employ RISC-V cores; the TT-Metalium API includes RISC-V address space concepts and NoC memory access.
- Insufficient context for additional cross-links to entity pages in the current wiki.

## Sources

- https://docs.tenstorrent.com/tt-metal/latest/tt-metalium/index.html
