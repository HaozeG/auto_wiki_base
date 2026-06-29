---
cold_start: false
constraints:
- VCIX technology
- multi-cluster support
- WorldGuard trusted protection
- RISC-V Vector ISA
- SiFive Intelligence Extensions
created: '2025-03-08'
hardware_targets:
- SiFive Intelligence X280
inbound_links: 0
needs_summary_revision: true
scorecard:
  bridge_score: 0.6
  claim_density: 0.7
  hub_potential: 0.5
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://www.sifive.com/blog/introducing-the-latest-sifive-intelligence-x280-processor
tags:
- RISC-V
- SiFive
- AI
- vector
- VCIX
toolchains: []
type: hardware_target
updated: '2026-06-28'
---

# SiFive Intelligence X280

The SiFive Intelligence X280 is a RISC-V processor core designed for AI inference, image processing, and datacenter workloads, released by SiFive in June 2022. It integrates the RISC-V Vector ISA and SiFive Intelligence Extensions to provide combined scalar and vector compute capabilities, and introduces the Vector Coprocessor Interface Extension (VCIX), which enables a direct instruction-mapped connection between the processor's vector ALU and custom accelerators. The X280 also supports multi-cluster configurations and SiFive WorldGuard trusted protection for system security. By allowing custom vector instructions to be executed from the standard SiFive software flow, VCIX reduces design complexity, improves power and area efficiency, and eliminates the need for separate accelerator memory systems or proprietary toolchains. The processor is positioned both as a standalone core and as a companion processor for custom accelerators, consolidating DSP accelerator functionality into a single RISC-V design.

## Key Claims

- Released in June 2022 as an enhanced version of the SiFive Intelligence X280 processor.
- Includes the Vector Coprocessor Interface Extension (VCIX), a vector instruction-mapped interface between the X280 vector ALU and custom accelerators.
- Supports multi-cluster configurations and SiFive WorldGuard trusted protection.
- VCIX enables custom vector instructions executed from the standard SiFive software flow, with access to the full vector register set.
- Custom accelerators connected via VCIX share the processor's vector register bank, caching architecture, and memory system, reducing design and test effort.
- Benefits include higher system performance, improved power and area efficiency, and easier programmability compared to separate accelerator designs.
- Targets AI inference, image processing, and datacenter applications.

## Optimization-Relevant Details

- ISA/profile: 64-bit RISC-V ISA with RISC-V Vector ISA and SiFive Intelligence Extensions.
- Vector/matrix/accelerator support: Vector compute via standard RISC-V Vector ISA; VCIX for custom vector instruction acceleration.
- Memory/cache/TLB/DMA: Not specified in source; VCIX allows sharing of processor memory system.
- Compiler/toolchain support: Standard SiFive software flow (no specific toolchain versions mentioned).

## Relationships

- [[SiFive_Intelligence_X390]] – A later SiFive AI processor with 512-bit vector registers and VCIX technology.
- [[T-HEAD_C910_SPEC_CPU_Benchmark]] – A competing high-performance RISC-V core with benchmark results.
- [[GEMM_with_RISC-V_Vector_Extension]] – A workload kernel that could be accelerated on the X280's vector units.

## Sources

- [SiFive Blog: Introducing the Latest SiFive Intelligence X280 Processor](https://www.sifive.com/blog/introducing-the-latest-sifive-intelligence-x280-processor)
