---
canonical_name: Ara
aliases:
- PULP Ara
- ara vector unit
subtype: null
tags: []
scorecard:
  novelty_delta: 0.7
  claim_density: 0.5
  self_containedness: 0.7
  bridge_score: 0.6
  hub_potential: 0.2
sources:
- raw/cache/17056a1b282319be.md
- https://github.com/pulp-platform/ara
source_url: https://github.com/pulp-platform/ara
fetched_at: '2026-07-09T03:09:54.042584+00:00'
type: entity
created: '2026-07-09'
updated: '2026-07-09'
cold_start: true
inbound_links: 4
outbound_links:
- target: ara2
  reason: Ara is the first-generation vector unit from the PULP project, while Ara2
    is its successor with improvements including 22nm implementation, higher clock
    frequency (1.35 GHz), and better energy efficiency (37.8 DP-GFLOPS/W). Both implement
    the RISC-V Vector Extension version 1.0
---

# Ara

Ara is a 64-bit vector processing unit designed as a coprocessor for the CVA6 RISC-V core, supporting the RISC-V Vector Extension version 1.0. Developed by the PULP platform at ETH Zurich and the University of Bologna, Ara is an open-source, modular vector unit that accelerates data-parallel workloads. It is configurable in terms of lane count and memory system parameters, and it operates with a RISC-V LLVM toolchain. Ara serves as the predecessor to Ara2, which is a more advanced version implemented in 22nm technology. The Ara system can be simulated with the Spike ISA simulator and synthesized with Verilator for RTL simulations. It also supports an ideal dispatcher mode where the CVA6 core is replaced by a FIFO to isolate Ara’s performance from scalar core bottlenecks.

## Key Claims

- Ara is a vector unit coprocessor for the CVA6 core.
- Supports the RISC-V Vector Extension version 1.0.
- Open-source and modular design from the PULP platform.
- Configurable via centralized configuration folder (lane count, memory system).
- Requires a RISC-V LLVM toolchain for compilation.
- Supports simulation with Spike ISA simulator and Verilator for RTL simulation.
- Includes an ideal dispatcher mode replacing CVA6 with a FIFO to measure Ara’s performance independently.

## Relationships

- [[ara2]]: Ara is the first-generation vector unit from the PULP project, while Ara2 is its successor with improvements including 22nm implementation, higher clock frequency (1.35 GHz), and better energy efficiency (37.8 DP-GFLOPS/W). Both implement the RISC-V Vector Extension version 1.0.

## Sources

- [GitHub - pulp-platform/ara: The PULP Ara is a 64-bit Vector ...](raw/cache/17056a1b282319be.md)
