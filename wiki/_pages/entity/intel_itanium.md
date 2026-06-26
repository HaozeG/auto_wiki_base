---
cold_start: false
created: '2026-12-03'
inbound_links: 1
scorecard:
  bridge_score: '~'
  claim_density: '~'
  hub_potential: '~'
  novelty_delta: '~'
  self_containedness: '~'
sources:
- the-architecture-that-was-right-about-everything.md
tags:
- itanium
- epic
- vliw
- architecture
type: entity
updated: '2026-06-26'
---

# Intel Itanium

Intel Itanium is a 64-bit processor architecture based on EPIC (Explicitly Parallel Instruction Computing), co-developed by Intel and HP and commercially released in 2001. EPIC extracted instruction-level parallelism at compile time rather than at runtime: programs were compiled into 128-bit bundles of three instructions each, with explicit stop bits encoding dependency information between bundles. Key architectural features included predicated execution (conditional execution of both branch paths without a branch predictor), speculative loads (prefetching data before it was needed to hide memory latency), register rotation (enabling software pipelining without explicit register renaming), and a large register file of 128 integer and 128 floating-point registers. Despite these innovations, Itanium failed commercially: compilers could not consistently extract EPIC-level parallelism from real programs, power consumption was high, and x86-64 from AMD offered a simpler path to 64-bit computing. Peak deployment was in high-end HP servers. Intel shipped the final Itanium 9700 series in 2017 and ended sales by 2021.

## Key Claims

- Itanium used 128-bit instruction bundles containing three instructions, with explicit stop bits encoding inter-bundle dependencies for compiler-directed scheduling.
- Predicated execution encoded branch conditions on every instruction, allowing both branch paths to execute and eliminating branch misprediction penalties.
- Speculative loads prefetched data before it was confirmed needed, with explicit hardware support for tolerating late memory exceptions.
- Register rotation enabled software pipelining for loops by cycling through a register window automatically, without explicit renaming in compiler-generated code.
- The register file comprised 128 integer and 128 floating-point registers, designed to keep multiple threads of computation staged simultaneously.
- Compiler immaturity was the primary cause of Itanium's performance shortfall relative to dynamically scheduled superscalar processors.
- Intel discontinued Itanium with the 9700 series (2017); sales ended in 2021 after two decades of niche server use.

## Relationships

- [[risc_v_vector_extension]]: RVV's vector length agnostic design and compiler-managed parallelism share conceptual roots with EPIC's approach to exposing parallelism explicitly to the toolchain.
- [[fpga_riscv_isa_extension_nn_inference]]: FPGA-based RISC-V AI extensions explore compiler-managed custom ISA parallelism, following goals similar to EPIC for domain-specific workloads.
- [[epic_vliw_ai_accelerator_legacy]]: Synthesis page tracing how Itanium's EPIC design principles — predication, wide parallelism, large register files — were independently rediscovered in NVIDIA GPUs, Google TPU, and RISC-V accelerators.

## Sources

- the-architecture-that-was-right-about-everything.md: Source for all claims about Itanium's features, commercial failure, and architectural description.
