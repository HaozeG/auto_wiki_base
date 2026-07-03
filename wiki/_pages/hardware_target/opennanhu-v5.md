---
canonical_name: OpenNanhu-V5
aliases:
- XiangShan Nanhu
subtype: hardware_target
tags: []
hardware_targets:
- OpenNanhu-V5
toolchains: []
constraints:
- '3 AXI interfaces: memory port, DMA port, peripheral port'
- clock, reset, JTAG interfaces
scorecard:
  novelty_delta: 0.9
  claim_density: 0.3
  self_containedness: 0.6
  bridge_score: 0.2
  hub_potential: 0.5
sources:
- raw/cache/9bf026872b6e0260.md
- https://github.com/OpenXiangShan-Nanhu/OpenNanhu-V5
source_url: https://github.com/OpenXiangShan-Nanhu/OpenNanhu-V5
fetched_at: '2026-07-03T14:39:39.634778+00:00'
type: hardware_target
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 0
---

# OpenNanhu-V5

OpenNanhu-V5 is an open-source high-performance RISC-V processor based on the XiangShan Nanhu microarchitecture. It is developed by the OpenXiangShan-Nanhu project and represents one implementation of the Nanhu microarchitecture, which is the second stable microarchitecture of the XiangShan family. The processor communicates with the uncore through three AXI interfaces: a memory port, a DMA port, and a peripheral port. It also provides clock, reset, and JTAG interfaces for debugging and functional verification. The XiangShan project as a whole practices agile development methodology for high-performance RISC-V processor design, with tools covering design, functional verification, debugging, and performance validation.

## Key Claims

- OpenNanhu-V5 is an open-source implementation of the XiangShan Nanhu microarchitecture.
- Uses three AXI interfaces for memory, DMA, and peripheral communication.
- Includes clock, reset, and JTAG interfaces.
- Developed under the OpenXiangShan-Nanhu organization.
- The Nanhu microarchitecture is the second stable microarchitecture in the XiangShan family.
- The XiangShan project employs agile development methodology for processor design.

## Optimization-Relevant Details

- ISA/profile: RISC-V (exact profile unspecified in source)
- Vector/matrix/accelerator support: Not specified
- Memory/cache/TLB/DMA: Communicates via AXI interfaces (memory port, DMA port, peripheral port)
- Compiler/toolchain support: Not specified

## Relationships

No specific relationship to visible context pages.

## Sources

- https://github.com/OpenXiangShan-Nanhu/OpenNanhu-V5
