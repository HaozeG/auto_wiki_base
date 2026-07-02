---
canonical_name: SiFive Intelligence X280
aliases:
- X280
- SiFive X280
- X280 processor
- SiFive Intelligence X280 processor
- SiFive Intelligence X280 Gen 2
- sifive-x280
- Intelligence X280
subtype: null
tags: []
hardware_targets:
- SiFive Intelligence X280
toolchains:
- SiFive software flow (GCC/LLVM with VCIX support)
constraints:
- RISC-V Vector ISA
- SiFive Intelligence Extensions
- Vector Coprocessor Interface Extension (VCIX)
- Multi-cluster up to 16 cores with cache coherence
- WorldGuard trusted protection
scorecard:
  novelty_delta: 0.9
  claim_density: 0.6
  self_containedness: 0.8
  bridge_score: 0.4
  hub_potential: 0.5
sources:
- raw/cache/0511d3d7b9e055f3.md
- https://www.sifive.com/blog/introducing-the-latest-sifive-intelligence-x280-processor
- raw/cache/29cf19162f245d8c.md
- https://www.sifive.com/blog/introduction-to-the-sifive-intelligence-x280
- raw/cache/fd13acf13f078e64.md
- https://reviews.llvm.org/D149710
- raw/cache/705b81f79d7fcde0.md
- https://www.sifive.com/press/tenstorrent-selects-sifive-intelligence-x280-for-next-generation1
- raw/cache/bdb96edcc418d8f4.md
- https://www.datacenterdynamics.com/en/news/google-deploys-sifives-intelligence-x280-processor-for-ai-workloads/
- raw/cache/eed8cc37f6bf1af7.md
- https://diversedaily.com/sifive-intelligence-x280-risc-v-core-optimized-for-ai-workloads/
source_url: https://www.sifive.com/blog/introducing-the-latest-sifive-intelligence-x280-processor
fetched_at: '2026-07-01T06:05:01.331347+00:00'
type: hardware_target
created: '2026-07-01'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
needs_summary_revision: false
---

# SiFive Intelligence X280

The SiFive Intelligence X280 is a RISC-V processor core developed by SiFive, designed for AI inference, image processing, and datacenter applications. It implements the standard RISC-V Vector ISA along with SiFive Intelligence Extensions, and introduces the Vector Coprocessor Interface Extension (VCIX), which allows custom accelerators to be directly attached to the vector register file. The X280 supports multi-cluster configurations up to 16 cores with cache coherence, includes SiFive WorldGuard trusted protection, and offers a standard software flow that enables custom vector instructions to be executed from the pipeline with full access to the vector register set. The processor is positioned as a way to consolidate DSP accelerator functionality into a single core while still allowing heavily optimized custom accelerators for intensive workloads.

## Key Claims

- VCIX allows custom coprocessors to access the vector register file directly, enabling seamless integration of user-defined accelerators.
- Custom vector instructions execute within the standard SiFive software flow, leveraging the vector pipeline.
- Supports multi-cluster configurations with up to 16 cores in a cache-coherent complex.
- Includes WorldGuard trusted protection for security.
- Built on the standard RISC-V Vector ISA and SiFive Intelligence Extensions, consolidating DSP functionality.
- VCIX reduces system complexity and improves ease of programming compared to dedicated accelerators.
- Intended for AI inference, image processing, and datacenter workloads requiring intensive vector computation.

## Optimization-Relevant Details

- ISA/profile: RISC-V Vector ISA, SiFive Intelligence Extensions, VCIX.
- Vector/matrix/accelerator support: VCIX enables custom vector coprocessors; vector register file exposed to accelerators.
- Memory/cache/TLB/DMA: Not specified in source.
- Compiler/toolchain support: Standard SiFive software flow (GCC/LLVM with VCIX support).

## Relationships

- Related RISC-V processor core with similar AI focus: [[xuantie_c908]]
- Decoupled matrix engine design for GEMM: [[rvme]]
- Optimization recipe leveraging RISC-V Vector instructions: [[mlir_xdsl_rvv_gemm_codegen_recipe]]
- [[sifive_intelligence_family]]: the product family this core belongs to.
- [[sifive_intelligence_x390]]: the successor core, claiming a fourfold vector-performance improvement via doubled VLEN (1024-bit) over the X280.

## Sources

- https://www.sifive.com/blog/introducing-the-latest-sifive-intelligence-x280-processor
