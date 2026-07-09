---
canonical_name: null
aliases: []
subtype: null
connected_entities:
- Blackhole
- Wormhole
synthesis_status: draft
scorecard:
  bridge_score: 0.7
  contradiction_potential: 0.0
  cross_domain_connection: null
sources:
- raw/cache/3d09296c100fdaa3.md
- https://deepwiki.com/tenstorrent/tt-isa-documentation
source_url: https://deepwiki.com/tenstorrent/tt-isa-documentation
fetched_at: '2026-07-09T09:59:53.532794+00:00'
type: synthesis
created: '2026-07-09'
updated: '2026-07-09'
cold_start: true
inbound_links: 1
outbound_links:
- target: wormhole
  reason: unlabeled
- target: blackhole
  reason: unlabeled
---

# Wormhole vs Blackhole Architecture Comparison

## RAG Summary

The Tenstorrent Wormhole B0 and Blackhole A0 AI accelerator ASICs share a common Tensix tile architecture and instruction set, with Blackhole introducing targeted hardware enhancements. Both chips are organized as a mesh of over 120 Tensix compute tiles interconnected by dual independent Network-on-Chip (NoC) fabrics, each tile containing five Baby RISC-V control cores, a low-precision (19-bit) Matrix Unit (FPU), a 32-lane FP32 Vector Unit (SFPU), and 1464 KiB of L1 SRAM. The documented ISA and programming model are identical across the two generations, covering RISC-V instructions, coprocessor operations, memory addressing, and NoC protocols. However, Blackhole A0 specifically enhances the SFPU with improved FMA capabilities, expands memory and register resources, and introduces specialized tile types such as Ethernet, PCIe, ARC, L2CPU, and DRAM tiles. These enhancements position Blackhole as a higher-performance chip while maintaining full software compatibility with Wormhole, making the unified documentation a valuable reference for developers targeting either generation.

---

## Full Synthesis

The documentation at tenstorrent/tt-isa-documentation provides a comprehensive technical reference covering both Wormhole B0 and Blackhole A0 ASICs. It details the hardware architecture from the ASIC level down to individual execution units, including the Tensix tile architecture, NoC communication, instruction pipeline, and data formats. The commonalities between the two chips are extensive: both use the same Tensix compute core design, the same Baby RISC-V control core layout, the same Matrix and Vector unit specifications, and the same memory hierarchy structure. The instruction set reference sections apply uniformly to both generations, enabling kernel code to be written once and run on either chip.

The key differences are highlighted in the "Blackhole A0 Enhancements" section, which lists SFPU and FMA improvements, memory and register enhancements, and the introduction of specialized tiles. Blackhole also includes an Ethernet tile architecture, edge tiles (PCIe, ARC, L2CPU), and DRAM tiles, whereas Wormhole likely lacks these. The "Architecture Comparison" page explicitly contrasts the two chips, though its full content is not extracted here. The documentation is particularly valuable because it provides a single source of truth for both chips, with separate sections for Wormhole B0 and Blackhole A0 subdirectories in the repository structure (e.g., WormholeB0/ vs BlackholeA0/).

## Open Questions

- What are the exact numerical performance differences (e.g., FLOPS, bandwidth) between Wormhole B0 and Blackhole A0? The documentation focuses on architectural features rather than benchmark results.
- Are there any instruction set differences between the two generations beyond coprocessor enhancements?
- What specific memory and register capacity increases does Blackhole offer over Wormhole?

## Connected Pages

- [[wormhole]]
- [[blackhole]]
