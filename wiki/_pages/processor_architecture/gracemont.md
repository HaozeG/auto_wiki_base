---
canonical_name: Gracemont
aliases:
- Gracemont Atom Core
- Gracemont E-core
- Intel Gracemont
- Intel Gracemont E-core
subtype: null
hardware_targets:
- Gracemont
workloads:
- general-purpose computing
datatypes:
- INT8 (VNNI)
- FP32
metrics:
- die area (~1/4 of Skylake)
- power reduction (60% at iso-performance vs Skylake)
- performance increase (40% at iso-power vs Skylake)
toolchains: []
constraints:
- 4-core cluster
- shared L2 cache
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 0.7
  bridge_score: 0.6
  hub_potential: 0.7
sources:
- raw/cache/dbab3c0d1ddceccb.md
- https://silicon.redfire.dev/events/intel/architecture-day-2021/
- raw/cache/09b5bae249c0b0e9.md
- https://www.servethehome.com/intel-gracemont-architecture-day-2021/
source_url: https://silicon.redfire.dev/events/intel/architecture-day-2021/
fetched_at: '2026-07-17T12:56:19.407744+00:00'
type: processor_architecture
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 1
outbound_links:
- target: golden_cove
  reason: Gracemont is the efficiency core paired with Golden Cove as the performance
    core in Intel's Alder Lake hybrid architecture
---

# Gracemont

Gracemont is a high-efficiency processor microarchitecture designed by Intel as the energy-efficient core (E-core) in the Alder Lake and later hybrid processor families. It replaces the Skylake-based Atom cores and is built for improved performance-per-watt in mobile and desktop client segments. Gracemont cores are organized in clusters of four, each cluster sharing 2 or 4 MiB of L2 cache with 17-cycle latency. The core features a dual 3-wide decoder front-end, a 256-entry reorder buffer (up from 208), 5-wide allocation, 8-wide retirement, and 17 execution ports (up from 10) including 4 integer ALUs, 2 floating-point ALUs, and 3 vector ALUs. It supports Intel's AVX, AVX2, and VNNI-INT8 instructions, as well as Control-flow Enforcement Technology (CET) and virtualization technology (VT-rp). Compared to a Skylake core, a Gracemont core consumes approximately one-quarter the die area, delivers 40% more performance at the same power, or consumes 60% less power at the same performance level.

## Key Claims

- Gracemont is a 4-core cluster design with 2 or 4 MiB shared L2 cache (17-cycle latency).
- Decode is 2×3-wide (two decoders each three-wide).
- Reorder buffer size: 256 entries (up from 208 in previous Atom).
- 17 execution ports: 4 integer ALUs, 2 FP ALUs, 3 vector ALUs, 2 load AGUs, 2 store AGUs, 2 jump ports.
- Supports AVX, AVX2, VNNI-INT8, CET, VT-rp.
- Die area is ~1/4 of Skylake.
- At iso-power, Gracemont delivers +40% performance compared to Skylake.
- At iso-performance, Gracemont consumes -60% power compared to Skylake.
- A 4C/4T Gracemont cluster provides +80% performance at iso-power or -80% power at iso-performance relative to a 2C/4T Skylake.

## Relationships

- [[golden_cove]]: Gracemont is the efficiency core paired with Golden Cove as the performance core in Intel's Alder Lake hybrid architecture.

## Sources

- [Intel Architecture Day 2021 - Silicon](raw/cache/dbab3c0d1ddceccb.md)
