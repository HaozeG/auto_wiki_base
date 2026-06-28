---
cold_start: true
constraints:
- Configurable 2-level systolic array hierarchy (tileRows, tileColumns, meshRows,
  meshColumns)
- 'Dataflow modes: output-stationary, weight-stationary, runtime-selectable'
- 'Scratchpad memory: sp_banks, sp_capacity'
- 'Accumulator memory: acc_capacity'
- 'Datatypes: inputType, outputType, accType (e.g., int8, int32)'
- 'Access-execute queues: ld_queue_length, st_queue_length, ex_queue_length, rob_entries'
- 'DMA parameters: dma_maxbytes, dma_buswidth, mem_pipeline'
- Chipyard version 0.1
created: '2025-03-04'
hardware_targets:
- Gemmini (systolic array GEMM accelerator)
inbound_links: 6
scorecard:
  bridge_score: 0.7
  claim_density: 0.8
  hub_potential: 0.6
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://chipyard.readthedocs.io/en/1.1.0/Generators/Gemmini.html
tags:
- Gemmini
- systolic array
- GEMM
- RoCC
- Chipyard
- RISC-V accelerator
toolchains:
- GNU
type: hardware_target
updated: '2026-06-28'
---------------------

# Gemmini (systolic array GEMM accelerator)

Gemmini is a systolic-array-based matrix multiplication (GEMM) unit generator designed for integration into RISC-V SoCs via the RoCC (Rocket Custom Coprocessor) interface within the Chipyard framework. It targets edge and mobile machine learning workloads by providing a configurable hardware accelerator that handles matrix multiplications with data movement managed through a dedicated DMA engine. The systolic array is organized as a two-level hierarchy: fully combinational tiles are assembled into a pipelined mesh, and parameters such as tile dimensions (tileRows, tileColumns), mesh dimensions (meshRows, meshColumns), dataflow (output-stationary, weight-stationary, or runtime), scratchpad and accumulator capacities, data types (input, output, accumulation), and queue sizes for load, store, and execute operations are all configurable. The accelerator connects to the memory system via the System Bus (L2 cache) and is programmed through non-standard RISC-V custom instructions exposed via C macros and a matrix multiplication library.

## Key Claims

- Implements a systolic array GEMM accelerator for RISC-V SoCs using the RoCC interface.
- Configurable 2-level systolic array hierarchy: tiles (combinational) and mesh (pipelined).
- Supports output-stationary, weight-stationary, or runtime-selectable dataflow.
- Configurable scratchpad (sp_banks, sp_capacity) and accumulator memory (acc_capacity).
- Supports different data types for input, output, and accumulation (e.g., input: int8, acc: int32).
- Implements access-execute decoupling with load, store, execute queues and reorder buffer (ROB).
- DMA engine for data movement between main memory and scratchpad/accumulators; parameters include dma_maxbytes and dma_buswidth tied to Rocket Chip system parameters.
- Generates a C header file (gemmini_params.h) based on generator parameters for software tuning.
- Software includes C macros for constructing custom instruction encodings and a matrix multiplication library.
- Example SoC configuration GemminiRocketConfig demonstrates integration with a Rocket core.

## Optimization-Relevant Details

- ISA/profile: RISC-V custom instructions via RoCC; no vector extension required.
- Vector/matrix/accelerator support: Dedicated systolic array accelerator; not a vector unit.
- Memory/cache/TLB/DMA: Connects via System Bus to L2 cache; DMA engine with configurable max bytes and bus width; closely tied to cache block size and bus parameters.
- Compiler/toolchain support: GNU binutils (custom instructions not directly exposed; C macros provided to encode instructions).

## Relationships

- [[GEMM_with_RISC-V_Vector_Extension]] – Both implement GEMM on RISC-V but using different approaches: a dedicated systolic array accelerator (Gemmini) versus a vector extension kernel. (Insufficient context for additional cross-links)

## Sources

- [Gemmini – Chipyard documentation](https://chipyard.readthedocs.io/en/1.1.0/Generators/Gemmini.html)
