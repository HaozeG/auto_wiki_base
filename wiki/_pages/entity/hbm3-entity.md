---
canonical_name: HBM3
aliases:
- High Bandwidth Memory 3
- HBM3 specification
subtype: null
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.7
  self_containedness: 0.9
  bridge_score: 0.6
  hub_potential: 0.4
sources:
- raw/cache/0aa839fc710a67a5.md
- https://www.tomshardware.com/news/hbm3-spec-reaches-819-gbps-of-bandwidth-and-64gb-of-capacity
source_url: https://www.tomshardware.com/news/hbm3-spec-reaches-819-gbps-of-bandwidth-and-64gb-of-capacity
fetched_at: '2026-07-03T17:04:48.342582+00:00'
type: entity
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 0
---

# HBM3

HBM3 (High Bandwidth Memory 3) is a JEDEC solid-state memory standard finalized and published in January 2022, succeeding HBM2 and HBM2E. The specification defines a per-pin data rate of 6.4 Gbps, delivering up to 819 GBps of bandwidth from a memory stack. It supports capacities ranging from 4 GB (using 8 Gb dies in a 4-high stack) to 64 GB (with future 32 Gb dies in a 16-high stack, though the initial spec limits stacks to 12-high for 48 GB maximum). HBM3 doubles the number of independent memory channels to 16 compared to HBM2, and introduces two pseudo channels per channel for virtual support of 32 channels. The standard also features 0.4V signaling and 1.1V operating voltage for energy efficiency, along with enhanced platform-level RAS (reliability, availability, serviceability), on-die ECC, and real-time error reporting, targeting HPC and AI workloads.

## Key Claims

- 6.4 Gbps per-pin data rate providing 819 GBps aggregate bandwidth.
- 16 independent memory channels, with two pseudo channels per channel (totaling 32 virtual channels).
- Memory capacities from 4 GB (8 Gb die, 4-high) up to 64 GB (future 32 Gb die, 16-high); initial maximum 48 GB using 12-high stacks.
- Operating voltage of 1.1V with 0.4V signaling for improved energy efficiency.
- On-die ECC and real-time error reporting for high platform-level RAS.
- Designed for HPC (high-performance computing) and AI processing workloads.

## Relationships

No specific relationship to the visible context pages ([[andes-ax45mpv-hardware-target]]) can be stated; HBM3 is a memory standard independent of any particular processor core.

## Sources

- https://www.tomshardware.com/news/hbm3-spec-reaches-819-gbps-of-bandwidth-and-64gb-of-capacity
