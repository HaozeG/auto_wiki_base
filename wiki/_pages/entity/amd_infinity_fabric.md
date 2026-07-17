---
canonical_name: AMD Infinity Fabric
aliases:
- Infinity Fabric
- IFOP
- Infinity Fabric On-Package
- AMD Infinity Fabric Gen5
- Infinity Fabric Gen5
- Infinity Fabric Interconnect
- xGMI
- IFI
subtype: null
tags: []
scorecard:
  novelty_delta: 0.7
  claim_density: 0.8
  self_containedness: 0.6
  bridge_score: 0.4
  hub_potential: 0.2
sources:
- raw/cache/9e9c5aa1981c3222.md
- https://chipsandcheese.com/p/pushing-amds-infinity-fabric-to-its
- raw/cache/9624ea3ddebfd56a.md
- https://www.amd.com/en/blogs/2025/engineering-the-future-of-ai.html
- raw/cache/ca6e8e6a3ca4dd58.md
- https://cr0x.net/en/infinity-fabric-performance-bottlenecks/
- raw/cache/ac3caf1276aebd3b.md
- https://diversedaily.com/infinity-fabric-interconnect-scalability-and-performance-in-amd-chiplet-based-designs/
source_url: https://chipsandcheese.com/p/pushing-amds-infinity-fabric-to-its
fetched_at: '2026-07-17T09:35:41.375458+00:00'
type: entity
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 0
---

# AMD Infinity Fabric

AMD chips since Zen have used multiple levels of interconnects to create a modular system, letting AMD hit high core counts quickly and cheaply. Several Zen cores share a L3 cache within a cluster, called a Core Complex (CCX). CCX-es access the rest of the system through AMD's Infinity Fabric, a flexible interconnect that lets AMD adapt system topology to their needs. Since Zen 2, that meant putting CPU cores on Core Complex Dies (CCDs). CCDs connect to a separate IO die through an Infinity Fabric On-Package (IFOP) interface, which provides 32 bytes per cycle of read bandwidth and 16 bytes per cycle of write bandwidth at the Infinity Fabric clock (FCLK). Infinity Fabric is central to AMD's hub-and-spoke topology and has been carried through Zen generations, with later versions supporting higher bandwidth through DDR5.

## Key Claims

- The Infinity Fabric is a flexible interconnect used in AMD Zen-based CPUs to connect CCX/CCD clusters to the memory and I/O subsystem.
- On Zen 2 and later, each CCD connects to the IO die via an IFOP interface that supplies 32 bytes/cycle of read bandwidth and 16 bytes/cycle of write bandwidth at FCLK.
- On a Zen 4 Ryzen 9 7950X3D system with DDR5-5600, DRAM latency under minimal load measures 82-83 ns.
- When bandwidth-intensive threads are pinned to the same CCD as a latency-sensitive thread, latency can spike above 400 ns.
- Moving bandwidth load to the other CCD dramatically reduces latency for the latency-sensitive thread, suggesting effective queue management or bandwidth allocation between CCDs.
- A single CCD can achieve nearly 64 GB/s of sustained bandwidth when not contending with a latency thread on the same IFOP link.
- Contention at both the CCD memory controller and the IFOP interface can produce additive latency degradation.

## Relationships

No specific relationship to existing wiki pages is established by this source.

## Sources

- [Pushing AMD's Infinity Fabric to its Limits - Chips and Cheese](raw/cache/9e9c5aa1981c3222.md)
