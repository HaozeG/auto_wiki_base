---
cold_start: false
created: '2026-06-26'
inbound_links: 1
scorecard:
  bridge_score: 0.8
  claim_density: 0.8
  hub_potential: 0.9
  novelty_delta: 0.9
  self_containedness: 0.7
sources:
- https://internet-pros.com/blog/risc-v-open-source-cpu-architecture-2026/
tags:
- risc-v
- open-source
- isa
- cpu-architecture
type: entity
updated: '2026-06-27'
------

# RISC-V

RISC-V (pronounced "risk-five") is a free and open instruction set architecture (ISA) that defines the contract between software and silicon, specifying what instructions a CPU understands. Unlike proprietary architectures such as x86 (controlled by Intel and AMD) and ARM (licensed for a fee from Arm Holdings), RISC-V is governed as an open standard by RISC-V International, a Swiss-based non-profit with over 4,500 member organizations including Google, NVIDIA, Qualcomm, Intel, Samsung, Alibaba, and the Linux Foundation. The ISA is royalty-free, meaning anyone can design, manufacture, and ship a RISC-V chip without paying license fees or signing non-disclosure agreements. Initially created at UC Berkeley in 2010 as a teaching project, RISC-V was deliberately designed to be modular: a small mandatory base integer instruction set (RV32I or RV64I) is supplemented by optional extensions for floating-point, atomic operations, vector processing, bit manipulation, cryptography, and many others. This modularity allows implementations ranging from tiny microcontrollers for smart light bulbs to out-of-order server CPUs, all sharing a common software ecosystem.

## Key Claims

- By January 2026, cumulative RISC-V cores shipped worldwide exceeded 25 billion, surpassing Apple's total chip shipments.
- Rhea, the first European-designed server CPU to reach silicon, is built around RISC-V, developed by the European Processor Initiative.
- Google confirmed its newest Pixel modem runs RISC-V firmware cores.
- NVIDIA disclosed that its GPU management controllers run RISC-V firmware cores.
- Meta's MTIA-2 AI accelerator runs RISC-V firmware cores.
- RISC-V International has more than 4,500 member organizations.
- The ISA is published under a permissive license, eliminating per-chip royalties.
- RISC-V supports modular extensions: base integer (RV32I/RV64I) plus optional extensions for floating point (F/D), atomic (A), vector (V), bit manipulation (B), cryptography (K), hypervisor (H), and others.
- The same compiler and operating system can target a 1,000x performance range across different microarchitectures.

## Relationships

No existing wiki pages are directly referenced in the source material. This entity is foundational to many upcoming pages on RISC-V extensions (e.g., VCIX, Matrix Extensions) and implementations (e.g., Rhea server CPU, Pixel modem firmware).

## Sources

- https://internet-pros.com/blog/risc-v-open-source-cpu-architecture-2026/
