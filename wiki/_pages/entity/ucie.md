---
canonical_name: UCIe
aliases:
- Universal Chiplet Interconnect Express
- UCIe Consortium
- UCIe Express
subtype: null
tags: []
scorecard:
  novelty_delta: 0.7
  claim_density: 0.4
  self_containedness: 0.6
  bridge_score: 0.5
  hub_potential: 0.5
sources:
- raw/cache/b595e507b22589f0.md
- https://www.uciexpress.org/specifications
- raw/cache/9104fcd06c0dbe02.md
- https://semiengineering.com/what-is-ucie/
source_url: https://www.uciexpress.org/specifications
fetched_at: '2026-07-02T12:37:27.552706+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# UCIe

UCIe (Universal Chiplet Interconnect Express) is an open specification for a die-to-die interconnect and serial bus between chiplets, co-developed by AMD, Arm, ASE Group, Google, and other industry partners. The specification defines the physical layer, protocol stack, and compliance testing requirements to ensure device interoperability across different chiplet designs. Version 1.1 of the specification extends reliability mechanisms to more protocols and supports broader usage models within the chiplet ecosystem. Version 2.0 introduced 32 GT/s data rates, while the 3.0 specification supports 48 GT/s and 64 GT/s, doubling the bandwidth of UCIe 2.0 to meet high-performance chiplet demands. The standard is governed by the UCIe Consortium, which includes board representatives from multiple semiconductor companies. By providing an open, interoperable standard, UCIe aims to enable a thriving chiplet ecosystem and facilitate integration of heterogeneous chiplets from different vendors.

## Key Claims

- UCIe is an open specification for die-to-die interconnect and serial bus between chiplets.
- It is co-developed by AMD, Arm, ASE Group, Google, and other partners.
- The specification includes architectural attributes for system setup, registers, test plans, and compliance testing.
- UCIe 1.1 extends reliability mechanisms and usage models.
- UCIe 3.0 supports data rates of 48 GT/s and 64 GT/s, doubling the bandwidth of UCIe 2.0 (32 GT/s).

## Relationships

- [[gemmini]]: UCIe enables chiplet-based designs that could integrate accelerator generators like Gemmini in multi-chiplet configurations.
- [[xuantie-c950]]: The XuanTie C950 server-class RISC-V processor may benefit from UCIe-based chiplet interconnects for scalable AI computing.
- (Insufficient context for additional cross-links to entity pages within the wiki.)

## Sources

- [UCIe Consortium Specifications](https://www.uciexpress.org/specifications)
- [UCIe - Wikipedia](https://en.wikipedia.org/wiki/UCIe)
