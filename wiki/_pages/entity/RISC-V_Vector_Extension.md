---
cold_start: false
created: '2025-03-04'
inbound_links: 0
needs_summary_revision: true
scorecard:
  bridge_score: 0.7
  claim_density: 0.8
  hub_potential: 0.8
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://grokipedia.com/page/RISC-V_Vector_Extension
tags:
- RISC-V
- vector extension
- ISA
- RVV 1.0
type: entity
updated: '2026-06-28'
---

# RISC-V Vector Extension

The RISC-V Vector Extension (RVV 1.0) is a ratified standard extension to the open-source RISC-V instruction set architecture (ISA), designed to enable scalable vector processing capabilities for high-performance computing (HPC) and data-intensive workloads. Ratified by RISC-V International in November 2021, it provides a flexible framework for vector operations that can scale with hardware resources, supporting vector lengths up to hardware limits without fixed maximum sizes, unlike traditional SIMD extensions. Building on the base RV32I or RV64I ISA, RVV 1.0 introduces dedicated vector registers and instructions for parallel data processing, making it suitable for applications in machine learning, scientific simulations, and embedded systems.

## Key Claims

- Ratified by RISC-V International in November 2021 after a structured draft and release candidate process (draft v0.10 in January 2021, rc1 in June 2021, rc2 in September 2021, frozen September 20, 2021).
- Introduces over 400 instructions supporting masked operations, gather-scatter memory access, and multiple data types (integer, floating-point, fixed-point).
- Vector length (VLEN) configurable up to 2^16 bits (65,536 bits) and element widths (SEW) from 8 to 64 bits.
- Predication via dedicated mask register v0 for element-level conditional execution.
- Vector configuration state managed via vtype register (SEW, LMUL, tail/mask policies: undisturbed or agnostic).
- Supports unit-stride, strided, indexed, and scatter-gather memory access patterns.
- Origins in 2015 with formal proposals at the 5th RISC-V Workshop in 2016; key contributors include Krste Asanović (chair) and Roger Espasa (co-chair).
- Adopted in commercial hardware such as SiFive Intelligence X280 and incorporated into the RVA23 profile.

## Relationships

- [[DSC_Fused_Dataflow_Optimization_Recipe]] – A TinyML optimization recipe that uses a RISC-V CFU, demonstrating RVV relevance in edge AI.
- [[XuanTie_C908_SHL_GEMM_Optimization]] – An optimization recipe for the XuanTie C908 processor which supports RVV 1.0, illustrating practical vectorization.
- Note: insufficient context for additional cross-links to entity pages.

## Sources

- https://grokipedia.com/page/RISC-V_Vector_Extension (the page includes internal citations [1]–[13] to various RISC-V specification documents and workshop presentations)
