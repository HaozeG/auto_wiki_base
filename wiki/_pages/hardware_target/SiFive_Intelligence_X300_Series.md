---
cold_start: true
constraints:
- 1024-bit vector length (VLEN)
- dual vector ALU
- in-order superscalar pipeline (8-stage dual-issue for X390 variant)
- SSCI interface
- VCIX interface (2048-bit)
- 4x vector compute improvement over previous generation
created: '2025-07-09'
hardware_targets:
- SiFive Intelligence X300 Series
inbound_links: 0
scorecard:
  bridge_score: 0.6
  claim_density: 0.6
  hub_potential: 0.6
  novelty_delta: 0.8
  self_containedness: 0.7
sources:
- https://www.sifive.com/cores/intelligence-x300-series
tags:
- RISC-V
- SiFive
- AI accelerator
- vector processing
- second generation
toolchains: []
type: hardware_target
updated: '2026-06-29'
---

# SiFive Intelligence X300 Series

The SiFive Intelligence X300 Series is a second-generation RISC-V processor family designed for AI/ML acceleration, offering 1024-bit vector length (VLEN) and dual vector ALUs to achieve a 4x improvement in vector compute throughput compared to the prior generation. The series targets mobile, infrastructure, and automotive applications requiring high-performance neural network inference. It includes variants such as the X390, which features an 8-stage dual-issue in-order superscalar pipeline with dual 1024-bit VLEN/512-bit DLEN vector units, and the XM series, which integrates four X300 cores with a matrix engine for large-scale AI acceleration. The X300 family supports SSCI and VCIX interfaces for extended vector operations, enabling flexible integration into SoCs. This processor line represents SiFive's continued advancement in RISC-V AI IP.

## Key Claims

- Second-generation SiFive Intelligence family offering 4x vector compute improvement over previous generation.
- Up to 1024-bit vector length with dual vector ALUs.
- Targets mobile, infrastructure, and automotive AI/ML use cases.
- X390 variant has an 8-stage dual-issue in-order superscalar pipeline with dual 1024-bit VLEN/512-bit DLEN vector units.
- XM variant integrates four X300 cores with a dedicated matrix engine.
- Supports SSCI and VCIX interfaces (VCIX up to 2048-bit).

## Optimization-Relevant Details

- ISA/profile: RISC-V with Sifive vector extensions (VCIX).
- Vector/matrix/accelerator support: 1024-bit vector length, dual vector ALUs, optional matrix engine in XM variant.
- Memory/cache/TLB/DMA: Not specified in available resource.
- Compiler/toolchain support: Not specified; likely supported by SiFive toolchain.

## Relationships

- [[Chiplet_RISC_V_AI_SoC_Benchmark_Results]] – A benchmark of a RISC-V AI chiplet accelerator that provides a comparison point for AI SoC performance.
- [[Tenstorrent_Grayskull_MatMul_Efficiency]] – Another RISC-V-based AI accelerator benchmark demonstrating alternative design choices for matrix multiplication.
- Insufficient context for additional cross-links to entity pages; no entity pages were available in the current wiki context.

## Sources

- [https://www.sifive.com/cores/intelligence-x300-series](https://www.sifive.com/cores/intelligence-x300-series)
