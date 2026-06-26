---
cold_start: true
created: 2026-06-26
inbound_links: 3
scorecard:
  bridge_score: null
  claim_density: null
  hub_potential: null
  novelty_delta: null
  self_containedness: null
sources:
- raw/sources/tenstorrent_blackhole_riscv.md
tags:
- risc-v
- ai-accelerator
- chip
- tenstorrent
- tensix
type: entity
updated: 2026-06-26
------

# Tenstorrent Blackhole

Tenstorrent Blackhole is a RISC-V-based AI accelerator chip designed to function as a standalone AI computer rather than a PCIe-attached peripheral, distinguishing it from Tenstorrent's prior Grayskull and Wormhole parts. The chip contains 768 RISC-V processors across two tiers: 16 "Big RISC-V" 64-bit dual-issue in-order cores capable of running Linux, and 752 "Baby RISC-V" cores embedded within 140 Tensix compute tiles. At announcement in August 2024, Blackhole was one of the largest RISC-V processor count implementations in any shipping product. The Tensix architecture, developed by Tenstorrent, treats RISC-V not as the primary compute engine but as a programmable control and dataflow processor surrounding a dedicated compute complex.

## Key Claims

- Blackhole delivers 745 TFLOPS at FP8 and 372 TFLOPS at FP16, with 32 GB GDDR6 memory and 1 TBps total off-chip bandwidth across 10 × 400 Gbps Ethernet links.
- The chip contains 768 RISC-V processors: 16 Big RISC-V (64-bit, dual-issue, in-order, runs Linux) grouped in 4 clusters, plus 752 Baby RISC-V cores.
- Each of the 140 Tensix cores contains 5 Baby RISC-V cores, a pair of routers, a compute complex, and L1 cache; the RISC-V cores handle memory management and communications, not matrix math.
- Wormhole, the predecessor chip, used 72 Tensix cores per card (n150 configuration) with up to 24 GB GDDR6.
- Blackhole is designed for standalone operation, whereas Grayskull and Wormhole required host CPU attachment via PCIe.
- Tenstorrent is developing a chiplet architecture using 2 nm process in collaboration with LSTC.

## Relationships

- [[tensix_architecture]]: The Tensix core is Tenstorrent's fundamental compute tile; Blackhole scales it to 140 tiles with RISC-V baby cores as programmable controllers.
- [[risc_v_vector_extension]]: Blackhole uses RISC-V for control/dataflow rather than vector arithmetic; contrasts with SiFive/Arrow approaches where RVV is the compute primitive.
- [[sifive_intelligence_x280]]: Alternative RISC-V AI approach — RVV-centric rather than Tensix dataflow.
- [[riscv_ai_ecosystem]]: Blackhole is the largest-count RISC-V implementation among shipping AI chips as of 2024.

## Sources

- tenstorrent_blackhole_riscv.md: All performance numbers, core counts, Tensix decomposition, comparison with Wormhole, standalone positioning.
