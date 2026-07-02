---
canonical_name: RVME
aliases:
- GEM5-RVME
- RISC-V RVME
- RVME matrix engine
subtype: null
tags: []
hardware_targets:
- RVME
toolchains:
- gem5
- scons
- gdb
constraints:
- Supports Xuantie MME v0.3 instructions
- Systolic array connection (v0.6)
- SRAM occupy mechanism
- Memchecker
- gem5 simulator based
scorecard:
  novelty_delta: 0.9
  claim_density: 0.6
  self_containedness: 0.8
  bridge_score: 0.6
  hub_potential: 0.5
sources:
- raw/cache/47ff020e492697af.md
- https://github.com/superboy999/RVME
source_url: https://github.com/superboy999/RVME
fetched_at: '2026-07-02T11:05:55.160988+00:00'
type: hardware_target
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# RVME

RVME is an efficient matrix engine microarchitectural model based on the RISC-V matrix extension, implemented in the gem5 simulator. It provides a detailed simulation platform for evaluating matrix operations, supporting the Xuantie MME v0.3 instruction set with planned support for v0.6. The design features a compute unit array that initially computes one sub-matrix per cycle with non-systolic connections, later evolving to a systolic array topology in the v0.6 release. The memory subsystem includes an SRAM occupy mechanism and a register allocation table (RAT) for read protection, with a Memchecker for access validation. The work is described in a paper accepted by ICCD 2025.

## Key Claims

- RVME is a detailed microarchitectural model of a matrix engine for RISC-V matrix extensions.
- Implemented in the gem5 simulator, providing a configurable platform for matrix operation evaluation.
- Supports Xuantie MME v0.3 instructions; v0.6 release planned with full MME v0.6 support.
- Compute unit array evolved from non-systolic per-sub-matrix computation to a systolic array connection in v0.6.
- Includes SRAM occupy mechanism, RAT for read protection, and Memchecker.
- Accepted at ICCD 2025.

## Optimization-Relevant Details

- ISA/profile: RISC-V with matrix extension (Xuantie MME v0.3, planned v0.6)
- Vector/matrix/accelerator support: Matrix compute unit array (systolic in v0.6), matrix multiply/load/store
- Memory/cache/TLB/DMA: SRAM with occupy mechanism, RAT, Memchecker
- Compiler/toolchain support: gem5 simulator, built with scons, debug with gdb

## Relationships

- [[gemmini]]: Both are matrix acceleration designs for RISC-V, though Gemmini is a generator while RVME is a microarchitectural model.
- [[xuantie-c950]]: The XuanTie C950 is a server-class RISC-V AI chip that could potentially leverage matrix extensions such as those modeled by RVME.
- [[cpa-factored-gemmini-systolic-array]]: This optimization recipe for systolic arrays relates to the systolic array architecture adopted in RVME v0.6.

## Sources

- [GitHub README: superboy999/RVME](https://github.com/superboy999/RVME)
