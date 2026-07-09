---
canonical_name: Single-Core Matmul (TT-Metalium)
aliases:
- matmul_single_core
- TT-Metalium matmul example
- single-core matmul Tenstorrent
subtype: null
tags:
- matmul
- tenstorrent
- tt-metalium
- single-core
workloads:
- matmul
datatypes:
- bfloat16
constraints:
- Single Tensix core at physical coordinates (0,0)
- Tile-based processing on 32×32 tiles
- DRAM buffers with page size equal to tile size (single_tile_size)
- Circular buffers with double buffering (num_input_tiles=2, num_output_tiles=2)
- Row-major input must be tiled before device transfer
scorecard:
  novelty_delta: 0.9
  claim_density: 0.6
  self_containedness: 0.7
  bridge_score: 0.8
  hub_potential: 0.4
sources:
- raw/cache/69f1de07d0493669.md
- https://docs.tenstorrent.com/tt-metal/latest/tt-metalium/tt_metal/examples/matmul_single_core.html
source_url: https://docs.tenstorrent.com/tt-metal/latest/tt-metalium/tt_metal/examples/matmul_single_core.html
fetched_at: '2026-07-09T11:12:47.748203+00:00'
type: workload_kernel
created: '2026-07-09'
updated: '2026-07-09'
cold_start: false
inbound_links: 2
needs_summary_revision: false
---

# Single-Core Matmul (TT-Metalium)

The single-core matrix multiplication workload on Tenstorrent hardware demonstrates the basic programming model of the TT-Metalium API. It implements a matmul operation with user-defined dimensions M, K, N (example: 640×640×640) using the bfloat16 datatype. The computation is performed on a single Tensix core at physical coordinates (0,0). Data is transferred between DRAM and the core using dedicated reader and writer kernels, while a compute kernel uses the matrix engine to perform tile-wise multiplication on 32×32 tiles. Circular buffers with double buffering enable overlap of data movement and computation. This workload serves as a foundational example for understanding the TT-Metalium data movement and compute kernel paradigm.

## Key Claims

- Single-core matmul implementation using TT-Metalium API uses separate reader, writer, and compute kernels.
- Data tilization (conversion from row-major to 32×32 tiled layout) is performed on the host before device transfer.
- Three DRAM buffers allocate space for input matrices A (M×K), B (K×N), and output matrix C (M×N), with page size set to the size of one 32×32 bfloat16 tile.
- Three circular buffers orchestrate data pipelining: cb_src0 (matrix A tiles), cb_src1 (matrix B tiles), cb_output (matrix C tiles), each configured with double buffering (num_input_tiles=2 or num_output_tiles=2).
- A golden reference matrix multiplication on the CPU (golden_matmul function) verifies correctness by comparing against the device output.
- The hardware matrix engine (FPU) performs efficient tile-wise inner products during the compute kernel execution.

## Kernel Shape

- Operation: matrix multiplication (MatMul)
- Shapes: M, K, N (example 640×640×640)
- Datatypes: bfloat16
- Layout: Input data in row-major format is tilized into 32×32 tiles before device upload; output from device is detilized back to row-major for verification.
- Sparsity: dense (no sparsity handling)
- Baseline implementation: CPU golden reference (golden_matmul) that computes the same matmul in double precision? The reference uses the same bfloat16 vectors for comparison, but the CPU implementation likely runs in higher precision; details of golden_matmul are not provided in the documented example.

## Relationships

- [[blackhole]] is the Tenstorrent chip generation that this example targets; the workload runs on Blackhole's Tensix cores.
- [[tensix-core]] (if that page exists) shares the architecture of the compute core: a Tensix tile includes the matrix engine and RISC-V baby cores used for the reader/writer kernels.
- This workload is a prerequisite for understanding multi-core or optimized matmul variants in the TT-Metalium programming model.

## Sources

- https://docs.tenstorrent.com/tt-metal/latest/tt-metalium/tt_metal/examples/matmul_single_core.html
