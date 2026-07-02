---
canonical_name: NX27V
aliases:
- Andes NX27V
- RISC-V NX27V
- NX27V vector processor
subtype: null
tags: []
hardware_targets:
- NX27V
toolchains: []
constraints:
- RISC-V IMAFD
- RISC-V C extension
- RISC-V P extension
- RISC-V V extension
- RISC-V N extension
- 5-stage scalar pipeline
scorecard:
  novelty_delta: 0.9
  claim_density: 0.5
  self_containedness: 0.7
  bridge_score: 0.3
  hub_potential: 0.3
sources:
- raw/cache/36f294d4c1913440.md
- https://www.andestech.com/en/products-solutions/andescore-processors/riscv-nx27v/
source_url: https://www.andestech.com/en/products-solutions/andescore-processors/riscv-nx27v/
fetched_at: '2026-07-02T11:45:20.709203+00:00'
type: hardware_target
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# NX27V

The NX27V is a 64-bit vector processor core designed by Andes Technology, featuring a 5-stage scalar pipeline and support for the latest RISC-V specifications including IMAFD standard instructions, the 'C' 16-bit compression extension, the 'P' DSP extension, the 'V' vector extension, and the 'N' user-level interrupt extension. It is intended for computation-intensive applications across broad market segments, such as AI, IoT, and secure computing. The NX27V is integrated into systems like the Andes QiLai SoC alongside a quad-core AX45MP cluster. Andes' Custom Extension (ACE) framework allows customers to create domain-specific instructions for further acceleration.

## Key Claims

- Supports RISC-V IMAFD, C, P, V, and N extensions.
- 64-bit vector processor with a 5-stage scalar pipeline.
- Designed for computation-intensive applications (AI, IoT, secure computing).
- Integrated in the Andes QiLai SoC with a quad-core AX45MP cluster.
- Andes Custom Extension (ACE) framework enables creation of custom instructions for domain-specific acceleration.

## Optimization-Relevant Details

- ISA/profile: RISC-V with IMAFD, C, P, V, N.
- Vector/matrix/accelerator support: RISC-V V extension (vector).
- Memory/cache/TLB/DMA: Not specified.
- Compiler/toolchain support: Not specified.

## Relationships

- [[cpa-factored-gemmini-systolic-array]]: This optimization recipe targets the Gemmini systolic array, which could be deployed alongside Andes processors for ML acceleration.
- [[earth-shifting-based-vector-memory-access]]: This vector memory access optimization targets RISC-V vector units like the Saturn core, and techniques could potentially be adapted for NX27V-based systems.
- Insufficient context for additional cross-links to entity pages; no directly related entity pages are present in the wiki.

## Sources

- https://www.andestech.com/en/products-solutions/andescore-processors/riscv-nx27v/
