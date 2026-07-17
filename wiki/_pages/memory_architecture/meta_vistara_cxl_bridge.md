---
canonical_name: Vistara
aliases:
- Meta Vistara
- Meta CXL bridge chip
subtype: null
hardware_targets:
- DDR4
- DDR5
- CXL
workloads:
- AI server memory expansion
datatypes: []
metrics:
- latency
- bandwidth
toolchains: []
constraints:
- CXL protocol
- DDR4 compatibility
- DDR5 host system
evidence_strength: reported
tags:
- CXL
- memory tiering
- DDR4 reuse
scorecard:
  novelty_delta: 0.8
  claim_density: 0.6
  self_containedness: 0.9
  bridge_score: 0.3
  hub_potential: 0.2
sources:
- raw/cache/5bba1c5a4c780a09.md
- https://www.youngju.dev/blog/2026-07-11-meta-cxl-ram-reuse.en
source_url: https://www.youngju.dev/blog/2026-07-11-meta-cxl-ram-reuse.en
fetched_at: '2026-07-17T11:59:57.195699+00:00'
type: memory_architecture
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 3
outbound_links:
- target: alphawave_semi_hbm_subsystem
  reason: 'Both Vistara and the Alphawave Semi HBM Subsystem address memory hierarchy
    challenges in data centers, but at opposite ends of the performance-cost spectrum:
    Vistara sacrifices bandwidth for capacity using recycled DDR4, while Alphawave''s
    HBM subsystem targets maximum bandwidth for compute-intensive workloads'
- target: nvidia_blackwell_ultra
  reason: Blackwell Ultra uses HBM3E for high-bandwidth memory, whereas Vistara uses
    CXL-attached DDR4 as a lower-cost capacity tier, representing two complementary
    approaches to memory system design in AI servers
---

# Vistara

Meta's Vistara is a custom CXL bridge chip designed to enable the reuse of retired DDR4 memory modules in modern DDR5-only servers. Presented at ISCA 2026, Vistara addresses memory supply chain constraints by creating a second-tier memory pool that is slower but far cheaper than local DDR5. The chip uses the Compute Express Link (CXL) protocol to attach old DDR4 memory to a DDR5 host system, providing expanded capacity at the cost of higher latency and lower bandwidth compared to directly attached DDR5. According to Meta's ISCA 2026 paper, the CXL-attached DDR4 memory exhibits approximately 60 percent higher latency (around 250 ns idle latency vs. 130 ns for local DDR5) and roughly 10x lower bandwidth than local memory.

## Key Claims

- Vistara is a custom ASIC designed in-house by Meta to bridge DDR4 memory modules to DDR5-only servers via CXL.
- The CXL-attached DDR4 memory tier has approximately 250 ns idle latency, compared to 130 ns for local DDR5 (60% higher latency).
- The expanded memory pool has roughly 10x lower bandwidth than local memory.
- Vistara repurposes retired DDR4 modules that would otherwise be decommissioned, reducing e-waste and memory procurement costs.
- The design targets AI server scenarios where memory capacity is a bottleneck even if bandwidth is reduced.

## Relationships

- [[alphawave_semi_hbm_subsystem]]: Both Vistara and the Alphawave Semi HBM Subsystem address memory hierarchy challenges in data centers, but at opposite ends of the performance-cost spectrum: Vistara sacrifices bandwidth for capacity using recycled DDR4, while Alphawave's HBM subsystem targets maximum bandwidth for compute-intensive workloads.
- [[nvidia_blackwell_ultra]]: Blackwell Ultra uses HBM3E for high-bandwidth memory, whereas Vistara uses CXL-attached DDR4 as a lower-cost capacity tier, representing two complementary approaches to memory system design in AI servers.

## Sources

- [Reviving Retired DDR4 — Meta's CXL Bridge Chip, Vistara](raw/cache/5bba1c5a4c780a09.md)
