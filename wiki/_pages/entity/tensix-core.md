---
canonical_name: Tensix Core
aliases:
- Tensix
- Tensix core
- Tensix processor
- Tenstorrent Tensix core
- Tensix compute core
- Tensix compute node
- Tensix tile
subtype: architecture
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 1.0
  bridge_score: 0.7
  hub_potential: 0.7
sources:
- raw/cache/4c02d9bff7e9fb25.md
- https://blog.gpu.net/posts/2026/june/new-blog-june11/
- raw/cache/8a04855274dd9c94.md
- https://github.com/tenstorrent/tt-metal/blob/main/METALIUM_GUIDE.md
- raw/cache/23c98a2f8571e57a.md
- https://github.com/afuller-TT/tt-metalium/blob/main/METALIUM_GUIDE.md
source_url: https://blog.gpu.net/posts/2026/june/new-blog-june11/
fetched_at: '2026-07-09T09:56:51.857773+00:00'
type: entity
created: '2026-07-09'
updated: '2026-07-09'
cold_start: false
inbound_links: 4
outbound_links:
- target: tenstorrent
  reason: The Tensix core is the fundamental compute unit designed by Tenstorrent,
    the company whose open-source hardware/software stack (TT-Metal, TT-Forge, TT-LLK)
    targets this architecture.
needs_summary_revision: false
---

# Tensix Core

The Tensix Core is the fundamental compute unit in Tenstorrent's chip architecture, used in the Grayskull, Wormhole, and Blackhole processors. Each core contains five small RISC-V CPUs (called Baby RISC-V cores): Data Movement 0 (NoC input), Data Movement 1 (NoC output), Unpack, Math, and Pack. These cores handle distinct stages of the compute pipeline: operand ingestion, unpacking, matrix or vector compute, packing, and output to the network-on-chip. The core includes a matrix engine (FPU) and a vector engine (SFPU), along with data pack/unpack units and 1.5 MB of dedicated local SRAM (also referred to as L1 memory). The RISC-V CPUs primarily handle instruction dispatch and control flow, while the matrix and vector units perform the actual computation. The architecture eschews SIMT execution, a cache hierarchy, and hardware multithreading in favor of software-managed memory and explicit DMA data movement. It operates on native 32x32 tile granularity, optimized for matrix multiplication and convolution. This design allows deterministic memory access latency and precise scheduling by compilers, making it distinct from traditional GPU warp-based architectures.

Data flows through a dual Network-on-Chip (NoC) interface into the core. The NoC operates in a quasi-full-duplex configuration: NoC 0 and NoC 1 traverse the chip in opposite directions in a wraparound 2D torus topology, enabling bidirectional communication with unidirectional links while optimizing power and area. Typical data flow: NoC 0 reads data from DRAM or other cores; the Unpacker reformats data into 32×32 tiles; the Matrix/Vector units compute; the Packer compresses results; and NoC 1 sends results to DRAM or other cores. Programming a Tensix Core typically requires three kernel types per core: a reader kernel for data input, a compute kernel for calculations, and a writer kernel for data output, which coordinate through circular buffers in the SRAM. [[TT-Metalium]] is the programming model that orchestrates these reader, compute, and writer kernels mapped to Tensix cores.

## Key Claims

- Each Tensix Core contains five special-purpose RISC-V CPUs (Data Movement 0, Data Movement 1, Unpack, Math, Pack) that coordinate matrix and vector units. These are sometimes called Baby RISC-V cores.
- It includes a matrix engine (FPU), a vector engine (SFPU), unpack/pack units, and 1.5 MB of software-managed local L1 SRAM, with no cache hierarchy.
- No SIMT execution model; no hardware multithreading; latency hidden via software pipelining.
- Operates natively on 32×32 tile granularity for matrix and convolution operations.
- Data movement is explicit via DMA operations over the network-on-chip.
- The NoC operates in a quasi-full-duplex configuration: two unidirectional wraparound rings (NoC 0 and NoC 1) traverse opposite directions, enabling simultaneous send and receive while optimizing power and area.
- Typical data flow: NoC 0 reads data; Unpacker prepares data into 32×32 tiles; Matrix/Vector units compute; Packer packs results; NoC 1 sends results.
- Programming requires three kernel types per core (reader, compute, writer) coordinated via circular buffers in SRAM, orchestrated by the [[TT-Metalium]] programming model.

## Relationships

- [[grayskull]], [[wormhole]], and [[blackhole]] all implement the Tensix Core architecture in their compute arrays. The Blackhole chip uses 120 cores (reduced from 140 via firmware) in its p100a/p150 variants, while other chips use between 72 and 120 cores per chip.
- [[TT-Metalium]] is the programming model that orchestrates the reader, compute, and writer kernels mapped to Tensix cores.

- [[tenstorrent]]: The Tensix core is the fundamental compute unit designed by Tenstorrent, the company whose open-source hardware/software stack (TT-Metal, TT-Forge, TT-LLK) targets this architecture.

## Sources

- https://blog.gpu.net/posts/2026/june/new-blog-june11/
- https://github.com/tenstorrent/tt-metal/blob/main/METALIUM_GUIDE.md
