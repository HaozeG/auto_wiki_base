---
canonical_name: RVV-Lite
aliases:
- RVV Lite
- RVV-Lite (layered approach)
subtype: null
tags:
- risc-v
- vector
- iot
- rvv
scorecard:
  novelty_delta: 0.8
  claim_density: 0.5
  self_containedness: 0.9
  bridge_score: 0.3
  hub_potential: 0.3
sources:
- raw/cache/fc824b199a1bc5d2.md
- https://open.library.ubc.ca/media/stream/pdf/24/1.0431080/3
source_url: https://open.library.ubc.ca/media/stream/pdf/24/1.0431080/3
fetched_at: '2026-07-02T05:24:44.059302+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# RVV-Lite

RVV-Lite is a reduced implementation of the RISC-V Vector Extension (RVV) proposed for resource-constrained IoT devices. The design eliminates instructions that are less frequently used or have high hardware cost, and organizes the remaining instructions into 12 groups of related functionality. It retains full support for all reduction instructions, mask operations, and permutation instructions. The proposal is presented in "A Layered Approach to the Official RISC-V Vector ISA" from the University of British Columbia, aiming to reduce the area overhead of a full RVV implementation while maintaining vector processing capability for common IoT workloads.

## Key Claims

- RVV-Lite eliminates less frequently used or very costly instructions from the full RVV specification.
- The remaining instructions are subdivided into 12 groups of related functionality.
- Full support is provided for all reduction instructions, mask instructions, and permutation instructions.
- The design targets IoT devices where a complete RVV implementation would be area-prohibitive.

## Relationships

No suitable entity pages are available in the current wiki context for cross-linking. RVV-Lite is a design variant on the RISC-V Vector Extension, which is a foundational component of many hardware targets in this wiki.

## Sources

- https://open.library.ubc.ca/media/stream/pdf/24/1.0431080/3
