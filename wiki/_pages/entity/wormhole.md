---
canonical_name: Wormhole
aliases:
- Wormhole n150
- Wormhole n300
- TT-Wormhole
- Wormhole B0
- Tenstorrent Wormhole
- Tenstorrent Wormhole architecture
subtype: chip
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 1.0
  bridge_score: 0.7
  hub_potential: 0.7
sources:
- raw/cache/4c02d9bff7e9fb25.md
- https://blog.gpu.net/posts/2026/june/new-blog-june11/
- raw/cache/3d09296c100fdaa3.md
- https://deepwiki.com/tenstorrent/tt-isa-documentation
- raw/cache/7d7d8748cedceac4.md
- https://clehaxze.tw/gemlog/2025/04-21-programming-tensotrrent-processors.gmi
- raw/cache/3fcb31a29588b582.md
- https://arxiv.org/html/2603.23343v1
source_url: https://blog.gpu.net/posts/2026/june/new-blog-june11/
fetched_at: '2026-07-09T09:56:51.857773+00:00'
type: entity
created: '2026-07-09'
updated: '2026-07-09'
cold_start: false
inbound_links: 2
outbound_links:
- target: wormhole-vs-blackhole-architecture
  reason: The Wormhole-vs-Blackhole synthesis page provides a detailed architectural
    comparison between this chip and its Blackhole successor.
needs_summary_revision: false
---

# Wormhole

Wormhole (B0) is Tenstorrent's second-generation AI accelerator ASIC, released mid-2024. It comes in two PCIe card variants: the n150 (single-chip) with 72 Tensix cores, 108 MB SRAM, 12 GB GDDR6 at 288 GB/s, 160 W TDP, and 262 FP8 TFLOPS at 1 GHz, and the n300 (dual-chip) with 128 Tensix cores, 192 MB SRAM, 24 GB GDDR6 at 576 GB/s aggregate, 300 W TDP, and 466 FP8 TFLOPS. The chip is designed with a many-tile architecture comprising over 120 Tensix compute tiles interconnected by dual independent Network-on-Chip (NoC) fabrics in a 2D torus topology. Each Tensix tile is a heterogeneous compute unit containing five Baby RISC-V cores (RV32IM ISA) for instruction dispatch and control, a specialized Tensor Coprocessor with a low-precision (19-bit) Matrix Unit (FPU) for high-throughput multiply-accumulate operations and a 32-lane Vector Unit (SFPU) for FP32 computations, and 1464 KiB of L1 SRAM organized into 16 banks for parallel data access. The chip provides comprehensive instruction set documentation covering the RISC-V cores, the Matrix and Vector units, data movement instructions (UNPACR, PACR), and configuration registers. Memory-mapped interfaces at defined base addresses (e.g., INSTRN_BUF_BASE, TENSIX_MOP_CFG_BASE) enable software to program the hardware directly. As of Q1 2026, Wormhole has the most mature TT-Metal documentation, tutorials, and verified model support among Tenstorrent products. It succeeded Grayskull as the primary evaluation and deployment platform and has been superseded by Blackhole in the product lineup; Wormhole B0 is the direct predecessor of the Blackhole A0 chip, which retains the same foundational architecture while introducing targeted enhancements to the vector unit, FMA, memory, and registers.

## Key Claims

- Wormhole n150: 72 Tensix cores, 108 MB SRAM, 12 GB GDDR6 at 288 GB/s, 160 W TDP, 262 FP8 TFLOPS at 1 GHz.
- Wormhole n300: 128 Tensix cores, 192 MB SRAM, 24 GB GDDR6 at 576 GB/s aggregate, 300 W TDP, 466 FP8 TFLOPS.
- The chip features over 120 Tensix tiles organized in three functional categories, interconnected by dual independent NoCs (NoC #0 with X-major routing, NoC #1 with Y-major routing).
- Each Tensix tile contains five Baby RISC-V cores (RV32IM): RISC-V B (data mover) and RISC-V T0/T1/T2 for UNPACK/MATH/PACK phases, plus a Tensor Coprocessor with a low-precision (19-bit) Matrix Unit (FPU) for high-throughput multiply-accumulate and a 32-lane Vector Unit (SFPU) for FP32 computations.
- Each tile has 1464 KiB of L1 SRAM organized into 16 banks for parallel data access.
- The MOP Expander at TENSIX_MOP_CFG_BASE can expand single instructions into thousands of micro-operations.
- The Wait Gate at 0xFFE80020 synchronizes instructions via semaphores.
- Supports floating-point models including FMA, and data formats like BFP (compressed block floating point).
- Comprehensive instruction set documentation covers RISC-V cores, Matrix and Vector units, data movement instructions (UNPACR, PACR), and configuration registers. Memory-mapped interfaces at base addresses enable direct hardware programming.
- As of Q1 2026, Wormhole has the most mature TT-Metal documentation, tutorials, and verified model support among Tenstorrent products.
- Blackhole A0, the successor, retains the same foundational architecture while introducing targeted enhancements to the SFPU, FMA, memory, and registers.

## Relationships

- [[tensix-core]] is the fundamental compute unit used in Wormhole.
- [[blackhole]] is the next-generation chip that extends the architecture with larger RISC-V cores and higher throughput, specifically enhancing the SFPU, FMA, memory, and registers over Wormhole B0.

- [[wormhole-vs-blackhole-architecture]]: The Wormhole-vs-Blackhole synthesis page provides a detailed architectural comparison between this chip and its Blackhole successor.

## Sources

- https://blog.gpu.net/posts/2026/june/new-blog-june11/
- https://deepwiki.com/tenstorrent/tt-isa-documentation
