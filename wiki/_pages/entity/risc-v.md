---
canonical_name: RISC-V
aliases:
- risk-five
- RISC-Five
- Risk-Five
- RISC-V ISA
subtype: null
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 1.0
  bridge_score: 0.8
  hub_potential: 0.9
sources:
- raw/cache/ac89c67a6b8baf3d.md
- https://en.wikipedia.org/wiki/RISC-V
source_url: https://en.wikipedia.org/wiki/RISC-V
fetched_at: '2026-07-02T10:47:38.403890+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# RISC-V

RISC-V (pronounced "risk-five") is a free and open standard instruction set architecture (ISA) based on reduced instruction set computer (RISC) principles, first developed in 2010 at the University of California, Berkeley and made publicly available in 2014. Unlike proprietary ISAs such as x86 and ARM, RISC-V is released under permissive open-source licenses and can be used without royalty payments, which has spurred widespread adoption in embedded systems, microcontrollers, and increasingly in high-performance computing and AI acceleration. The ISA supports variable-length encoding (16-bit compressed instructions via the C extension, 32-bit, 64-bit, and 128-bit address spaces), and its modular extension scheme includes the M (multiplication), A (atomics), F/D/Q (floating-point), V (vector operations), and B (bit manipulation) extensions, among others. The vector extension (V) is particularly relevant for AI accelerators, as it provides data-level parallelism for workloads like matrix multiplication and convolution. RISC-V International, a non-profit organization based in Switzerland, now stewards the standard with over 4,500 members as of 2025. Commercial implementations include SoCs from SiFive, Andes Technology, SpacemiT, Alibaba (DAMO Academy), StarFive, Espressif Systems, and Raspberry Pi, many of which target AI and machine learning inference workloads.

## Key Claims

- RISC-V is a free and open standard ISA with permissive licensing, allowing royalty-free implementation.
- Developed at UC Berkeley in 2010, publicly introduced in 2014.
- Modular design with mandatory base integer ISA and optional extensions (M, A, F, D, Q, C, V, B, etc.).
- The V extension defines vector operations essential for AI and HPC workloads.
- Supported by major Linux distributions and a growing ecosystem of commercial hardware vendors.
- RISC-V International oversees continued development with 4,500+ members.

## Relationships

- [[llvm-riscv-fptrunc-narrowing-optimization]]: This optimization recipe targets RISC-V processors and demonstrates a compiler transformation that improves floating-point division performance on RISC-V hardware.
- [[spacemit-x60-processor]]: The SpacemiT X60 is a RISC-V processor implementing the RISC-V 64GCVB architecture and RVA22 profile, providing a concrete example of a RISC-V-based AI accelerator hardware target.

## Sources

- [RISC-V - Wikipedia](https://en.wikipedia.org/wiki/RISC-V)
