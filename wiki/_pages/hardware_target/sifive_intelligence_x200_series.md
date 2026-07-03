---
canonical_name: SiFive Intelligence X200 Series
aliases:
- SiFive X200 Series
- X200 Series
- SiFive Intelligence X200
- X280 Gen 2
subtype: null
tags: []
sources:
- raw/cache/d8a93d334b06262c.md
- https://www.sifive.com/cores/intelligence-x200-series
hardware_targets:
- SiFive Intelligence X200 Series
toolchains: []
constraints: []
created: '2026-07-01'
updated: '2026-07-01'
cold_start: false
inbound_links: 1
scorecard:
  novelty_delta: 0.9
  claim_density: 0.5
  self_containedness: 0.6
  bridge_score: 0.7
  hub_potential: 0.5
source_url: https://www.sifive.com/cores/intelligence-x200-series
fetched_at: '2026-07-01T06:08:25.891404+00:00'
type: hardware_target
needs_summary_revision: false
outbound_links:
- target: xuantie_c908
  reason: Another RISC-V AI-oriented processor core with vector extensions, suitable
    for comparison
- target: rvme
  reason: A RISC-V matrix engine coprocessor design, representing an alternative AI
    acceleration approach
---

# SiFive Intelligence X200 Series

The SiFive Intelligence X200 Series is a multi-core capable RISC-V processor family designed for AI/ML compute at the edge. It features vector extensions and SiFive Intelligence Extensions, including SSCI and VCIX extensions supporting up to 1024-bit operations. The X280 Gen 2, a member of the X200 Series, is an 8-stage dual-issue in-order superscalar design with a 512-bit vector length (VLEN) and a 256-bit datapath length (DLEN). It incorporates a single vector ALU and is optimized for AI acceleration workloads at the edge. The X200 Series builds on the first-generation X280 and is part of the broader SiFive Intelligence family. Exact memory hierarchy details and toolchain support are not disclosed in available promotional content.

## Key Claims

- The X200 Series is a multi-core capable RISC-V processor family optimized for AI/ML compute at the edge.
- It implements vector extensions with SiFive Intelligence Extensions, SSCI, and VCIX (up to 1024-bit operations).
- The X280 Gen 2 has an 8-stage dual-issue in-order superscalar pipeline, 512-bit VLEN, 256-bit DLEN, and a single vector ALU.

## Optimization-Relevant Details

- ISA/profile: RISC-V with vector extensions and SiFive Intelligence Extensions.
- Vector/matrix/accelerator support: 512-bit VLEN, 256-bit DLEN, Single Vector ALU, SSCI and VCIX (1024-bit).
- Memory/cache/TLB/DMA: Not specified.
- Compiler/toolchain support: Not specified.

## Relationships

- [[xuantie_c908]]: Another RISC-V AI-oriented processor core with vector extensions, suitable for comparison.
- [[rvme]]: A RISC-V matrix engine coprocessor design, representing an alternative AI acceleration approach.

## Sources

- https://www.sifive.com/cores/intelligence-x200-series
