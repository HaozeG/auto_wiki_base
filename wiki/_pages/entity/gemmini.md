---
canonical_name: Gemmini
aliases:
- Gemmini accelerator
- Gemmini systolic array generator
- gemmini
- Gemmini generator
- Gemmini systolic array
- Chipyard Gemmini
subtype: null
tags: []
scorecard:
  novelty_delta: 0.8
  claim_density: 0.9
  self_containedness: 0.9
  bridge_score: 0.7
  hub_potential: 0.5
sources:
- raw/cache/af71d82151f46792.md
- https://chipyard.readthedocs.io/en/1.2.0/Generators/Gemmini.html
- raw/cache/985ce15e462dd7e4.md
- https://chipyard.readthedocs.io/en/1.5.0/Generators/Gemmini.html
- raw/cache/2c1d8369e61c2065.md
- https://mikutyan4.github.io/chipyard-linux-nexys/ch06-gemmini-matrix-operations.html
source_url: https://chipyard.readthedocs.io/en/1.2.0/Generators/Gemmini.html
fetched_at: '2026-07-09T02:53:29.960997+00:00'
type: entity
created: '2026-07-09'
updated: '2026-07-09'
cold_start: true
inbound_links: 0
outbound_links:
- target: ara2
  reason: Both Gemmini and Ara2 are open-source RISC-V accelerators for ML workloads,
    but Gemmini uses a systolic array with custom instructions while Ara2 implements
    the standard RVV 1.0 vector extension
---

## Gemmini

Gemmini is an open-source systolic-array based matrix multiplication unit generator designed for the investigation of software and hardware implications of integrating machine learning accelerators into System-on-Chip (SoC) designs. Developed as part of the Chipyard framework, Gemmini is implemented as a RoCC (Rocket Custom Coprocessor) accelerator using non-standard RISC-V custom instructions and interfaces with the RoCC port of a Rocket or BOOM tile. It connects to the memory system through the System Bus directly to the L2 cache. Gemmini is highly configurable, with parameters including systolic array dimensions (tileRows, tileColumns, meshRows, meshColumns), dataflow options (output-stationary, weight-stationary, or runtime-dynamic), scratchpad and accumulator memory sizes and banking, input/output/accumulator data types, access-execute queue sizes, and DMA transaction parameters. It also generates a C header file for software tuning and provides a C matrix multiplication library along with support for the Spike functional simulator via a custom extension.

## Key Claims

- Gemmini is a systolic-array based matrix multiplication unit generator for RISC-V SoCs.
- It uses the RoCC interface with non-standard RISC-V custom instructions.
- Configurable parameters include systolic array dimensions (2-level hierarchy with tiles and mesh), dataflow modes (output-stationary, weight-stationary, or both), scratchpad capacity (sp_capacity) and number of banks (sp_banks), accumulator capacity (acc_capacity), data types (inputType, outputType, accType), queue lengths (ld_queue_length, st_queue_length, ex_queue_length), ROB entries, and DMA parameters (dma_maxbytes, dma_buswidth, mem_pipeline).
- Gemmini implements access-execute decoupling via separate load, store, and execute instruction queues and a reorder buffer.
- DMA parameters are tightly coupled with Rocket Chip SoC system parameters (beatBytes and cacheblockbytes).
- The software side includes a C matrix multiplication library and generates a gemmini_params.h header file for tuning based on generator parameters.
- Spike simulator supports Gemmini via the --extension=gemmini flag using a custom non-standard Spike implementation in the esp-tools toolchain.

## Relationships

- [[ara2]]: Both Gemmini and Ara2 are open-source RISC-V accelerators for ML workloads, but Gemmini uses a systolic array with custom instructions while Ara2 implements the standard RVV 1.0 vector extension.

## Sources

- [3.5. Gemmini - Chipyard's documentation - Read the Docs](raw/cache/af71d82151f46792.md)
