---
cold_start: false
created: '2026-06-26'
inbound_links: 2
scorecard:
  bridge_score: 0.6
  claim_density: 0.6
  hub_potential: 0.5
  novelty_delta: 0.8
  self_containedness: 0.7
sources:
- raw/sources/tt_metalium_lab1_single_core_matmul.md
tags:
- tensix
- tenstorrent
- matrix-multiplication
- architecture
type: entity
updated: '2026-06-26'
------

# Tensix Architecture

The Tensix architecture is Tenstorrent's proprietary tile-based processor design optimized for AI and high-performance computing workloads. Each Tensix core integrates a RISC-V control processor, local SRAM memory, and a dedicated matrix multiplication engine, enabling efficient execution of tiled matrix operations. The architecture is programmed through the TT-Metalium software stack, which provides low-level APIs for direct core control and data movement. In a single-core configuration, matrix multiplication proceeds by loading tiles of input matrices (A and B) into the core's local SRAM, performing the multiply-accumulate (MAC) operations in the matrix engine, and writing the resulting partial sums back to DRAM. The design emphasizes data locality and loop tiling to maximize compute efficiency and minimize off-chip memory access, following the classical cache-friendly row-major memory layout. Tensix cores can be combined in a mesh to scale throughput for large neural network layers, making the architecture suitable for both edge and datacenter deployments.

## Key Claims

- Each Tensix core contains a RISC-V control processor, local SRAM (on-chip memory), and a matrix engine for high-throughput multiply-accumulate operations.
- Matrix multiplication on a single core uses a tiled approach: input matrices are divided into tiles, loaded into local SRAM, and processed tile-by-tile to improve data reuse and reduce DRAM bandwidth.
- The row-major memory layout is used for matrices, enabling cache-friendly sequential access patterns when traversing rows for inner products.
- Loop tiling is explicitly employed to fit working sets within the core's local SRAM, preventing cache thrashing and improving arithmetic intensity.
- The TT-Metalium software stack exposes programming interfaces to directly manage core operations, tile loading, and synchronization without an operating system.
- Single-core performance is limited by the compute capacity of a single matrix engine; multi-core scaling is achieved by distributing tiles across a grid of Tensix cores.

## Relationships

- [[tt_metalium_software_stack]]: TT-Metalium is the primary programming framework for Tensix cores, providing the APIs used to implement matrix multiplication and other kernels.
- [[risc_v_vector_extension]]: While Tensix uses RISC-V control processors, its matrix engine is a custom accelerator rather than a vector unit; however, both approaches target efficient linear algebra.
- [[fpga_riscv_isa_extension_nn_inference]]: FPGA-based RISC-V matrix accelerators share the goal of tile-based computation but use reconfigurable logic rather than fixed architecture.

## Sources

- tt_metalium_lab1_single_core_matmul.md: Tenstorrent official lab documentation describing single-core matrix multiplication, including algorithm details, row-major layout, loop tiling, and architectural overview of Tensix.
