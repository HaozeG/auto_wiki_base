---
canonical_name: Intel Alder Lake
aliases:
- Alder Lake
- Alder Lake hybrid architecture
subtype: null
tags: []
scorecard:
  novelty_delta: 0.8
  claim_density: 0.6
  self_containedness: 0.8
  bridge_score: 0.3
  hub_potential: 0.4
sources:
- raw/cache/489c6a4d130a0ade.md
- https://chipsandcheese.com/p/alder-lakes-caching-and-power-efficiency
source_url: https://chipsandcheese.com/p/alder-lakes-caching-and-power-efficiency
fetched_at: '2026-07-17T13:02:41.367223+00:00'
type: entity
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 0
outbound_links:
- target: meta_vistara_cxl_bridge
  reason: 'Both Alder Lake and Vistara address memory hierarchy challenges: Alder
    Lake optimizes on-chip cache energy efficiency, while Vistara expands off-chip
    memory capacity using CXL-attached DDR4'
---

# Intel Alder Lake

Intel Alder Lake is a hybrid x86 microprocessor architecture introduced by Intel in 2021, combining high-performance Golden Cove cores with power-efficient Gracemont cores in a single die. This article analyzes the caching hierarchy and power efficiency of Alder Lake using memory bandwidth benchmarks that read package power counters. The cache hierarchy consists of three levels: L1, L2, and L3 cache. Golden Cove cores feature a 48 KB L1D cache, a 1280 KB private L2 cache, and share a 30 MB L3 cache across the entire chip. Gracemont cores, designed for efficiency, share a 2 MB L2 cache per quad-core cluster. Power measurements reveal that accessing DRAM costs nearly five times more energy per bit than accessing the L3 cache, and that Golden Cove's micro-op cache provides significant power savings for instruction fetch compared to fetching from L2 cache.

## Key Claims

- Alder Lake uses a hybrid core design with Golden Cove (performance) and Gracemont (efficiency) cores.
- Golden Cove L1D cache is 48 KB, L2 cache is 1280 KB, and shared L3 is 30 MB.
- Gracemont has a 2 MB L2 cache shared across a quad-core cluster.
- DRAM access costs nearly 5X energy per bit compared to L3 cache access.
- Instruction fetch from L2 cache costs 77% more energy per instruction than from L1 cache.
- The micro-op cache reduces instruction fetch energy; hitting micro-op cache costs only 6.5% more power than L1i fetch.
- Gracemont does not achieve overall power efficiency over Golden Cove for cache hits; it wins efficiency only when accessing DRAM.
- Measurements were conducted with DDR4-3200 memory due to DDR5 board issues.

## Relationships

- [[meta_vistara_cxl_bridge]]: Both Alder Lake and Vistara address memory hierarchy challenges: Alder Lake optimizes on-chip cache energy efficiency, while Vistara expands off-chip memory capacity using CXL-attached DDR4.

## Sources

- [Alder Lake’s Caching and Power Efficiency - Chips and Cheese](raw/cache/489c6a4d130a0ade.md)
