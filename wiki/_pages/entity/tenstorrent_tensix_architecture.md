---
cold_start: true
created: '2026-06-27'
inbound_links: 0
needs_summary_revision: false
scorecard:
  bridge_score: 0.6
  claim_density: 0.8
  hub_potential: 0.5
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://github.com/tenstorrent/tt-metal/blob/main/METALIUM_GUIDE.md
tags:
- tenstorrent
- ai-accelerator
- tensix
- tt-metalium
- hardware-architecture
type: entity
updated: '2026-06-28'
---

# Tenstorrent Tensix Architecture

The Tenstorrent Tensix Architecture is a non-GPU AI accelerator design that organizes compute resources as a grid of specialized Tensix cores interconnected by a 2D torus Network-on-Chip (NoC). Unlike traditional GPU architectures that rely on massive thread-level parallelism, each Tensix core contains five small RISC-V processors for instruction dispatch, dedicated matrix (FPU) and vector (SFPU) compute units, data packing/unpacking hardware, and 1.5 MB of local SRAM. The architecture prioritizes efficient data movement and local memory utilization through a pipeline of reader, compute, and writer kernels that operate on 32×32 native tiles, reducing reliance on DRAM accesses. Programming is done via TT-Metalium, a low-level framework that requires three kernel types per core and coordinate through circular buffers in SRAM.

## Key Claims

- Each Tensix core contains five "Baby" RISC-V CPUs: Data Movement 0, Data Movement 1, Unpack, Math, and Pack, which handle instruction dispatch and control flow rather than executing computations directly.
- Each Tensix core has 1.5 MB of local SRAM (called L1) to hold transient data and facilitate data exchange between local components.
- The NoC operates in a quasi-full-duplex configuration using two unidirectional, wraparound 2D torus networks (NoC 0 and NoC 1) that traverse the chip in opposite directions, enabling simultaneous send and receive.
- The architecture natively operates on 32×32 tiles, optimized for deep learning operations.
- Programming via TT-Metalium requires three kernel types per Tensix core: a reader kernel for data input, a compute kernel for calculations, and a writer kernel for data output, coordinating through circular buffers in SRAM.
- The typical data flow pipeline is: NoC 0 reads data from DRAM or other Tensixes → Unpacker unpacks data into processable format → Matrix/tensor unit performs computation → Packer packs results → NoC 1 sends results to DRAM or other Tensixes.
- The RISC-V cores are deliberately minimal, sharing architectural similarity with classic RISC processors like the MIPS R3000.
- The chip includes DRAM nodes, Ethernet nodes, ARC/management nodes, and PCIe nodes in addition to Tensix cores.
- The architecture replaces the traditional cache hierarchy with explicit local SRAM management.

## Relationships

- [[risc_v_vector_extension]] — The Tensix cores use small RISC-V processors that, while minimal rather than vector-capable, are part of the broader RISC-V ecosystem for AI acceleration.
- [[gemmini]] — Gemmini is a systolic-array-based AI accelerator generator, representing a contrasting design approach to Tensix's multi-kernel NoC-based architecture.

## Sources

- https://github.com/tenstorrent/tt-metal/blob/main/METALIUM_GUIDE.md
