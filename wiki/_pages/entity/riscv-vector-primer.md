---
canonical_name: RISC-V Vector Primer
aliases:
- riscv-vector-primer
- RVV Primer
subtype: null
tags: []
scorecard:
  novelty_delta: 0.8
  claim_density: 0.3
  self_containedness: 0.9
  bridge_score: 0.7
  hub_potential: 0.4
sources:
- raw/cache/3a037113c9c1b081.md
- https://github.com/simplex-micro/riscv-vector-primer/blob/main/chapter-01.md
source_url: https://github.com/simplex-micro/riscv-vector-primer/blob/main/chapter-01.md
fetched_at: '2026-07-02T11:25:43.608581+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# RISC-V Vector Primer

The RISC-V Vector Primer is a tutorial-style introduction to the RISC-V Vector Extension (RVV) written by a veteran microprocessor architect with over 40 years of experience designing x86, Arm, PowerPC, ARC, and RISC-V processors. Chapter 1 provides the foundational concepts necessary to understand RVV, including the distinction between vector processors and classic SIMD, the motivation for RVV's scalable design, and core terminology such as vector register length, element width, grouping, masks, vector length (VL), strip mining, and chaining. The primer emphasizes mental models over line-by-line specification commentary, aiming to make RVV digestible for engineers who have found the official specification forbidding. It also explains why RVV matters now for AI/ML workloads, signal processing, cryptography, and scientific computing.

## Key Claims

- RVV defines a scalable vector ISA that can work for small embedded cores or wide data center engines without recompilation.
- RVV keeps the RISC philosophy: load/store design, simple fixed-field encoding, and clear separation between scalar and vector state.
- A single RVV binary can run on implementations with different vector register widths, a key advantage over fixed-width SIMD extensions.
- Vector processors differ from SIMD in that they treat a single instruction as a stream of operations over many elements, using deep pipelines and chaining for sustained throughput.
- The Cray-1 architecture serves as a conceptual precedent, separating scalar and vector execution with dedicated register files and deeply pipelined functional units.
- Under Flynn's taxonomy, both SIMD extensions (SSE, AVX, NEON) and vector processors belong to the SIMD category, but the execution model differs.
- The primer introduces core RVV terminology: vector register length, element width, grouping, masks, vector length (VL), strip mining, and chaining.

## Relationships

- [[earth-shifting-based-vector-memory-access]]: The EARTH optimization uses RVV and benefits from the conceptual foundation provided by this primer for understanding vector memory access.
- [[pulp-nn-optimization-recipe]]: PULP-NN targets quantized neural networks on RISC-V clusters with RVV support; the primer explains the vector execution model that underlies such optimizations.

## Sources

- [riscv-vector-primer Chapter 1 on GitHub](https://github.com/simplex-micro/riscv-vector-primer/blob/main/chapter-01.md)
