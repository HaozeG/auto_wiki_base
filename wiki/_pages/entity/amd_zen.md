---
canonical_name: AMD Zen
aliases:
- Zen
- Zen+
- Zen 2
- Zen 3
- Zen 3+
- Zen 4
- Zen 4c
- Zen 5
- Zen 5c
- Zen Core
subtype: null
tags:
- cpu
- amd
- x86
- chiplet
scorecard:
  novelty_delta: 0.9
  claim_density: 0.5
  self_containedness: 0.8
  bridge_score: 0.6
  hub_potential: 0.3
sources:
- raw/cache/39cf99e1b8b3d730.md
- https://www.amd.com/en/technologies/zen-core.html
source_url: https://www.amd.com/en/technologies/zen-core.html
fetched_at: '2026-07-17T09:57:03.881370+00:00'
type: entity
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 1
---

# AMD Zen

The AMD Zen core architecture is a hybrid, multi-chip x86 processor microarchitecture designed by AMD, first introduced in 2017 with the Ryzen 1000 series desktop processors. It is a scalable chiplet-based design that decouples core and I/O development, allowing AMD to produce a range of processors from desktop Ryzen to server EPYC chips across multiple process nodes. Zen employs simultaneous multi-threading, a leading-edge cache hierarchy with neural-net branch prediction, and a chiplet interconnect (Infinity Fabric) to combine multiple CPU dies on a single package. The architecture has evolved through several generations—Zen, Zen+, Zen 2, Zen 3, Zen 3+, Zen 4, and Zen 5—each bringing IPC gains, process node shrinks (from 14nm down to 4nm), and new features such as doubled L2 cache in Zen 4 and wider pipelines in Zen 5.

## Key Claims

- Zen is a chiplet-based architecture: instead of monolithic dies, it uses processor building blocks called chiplets, each housing multiple Zen cores, enabling scalability across core counts.
- IPC improvements per generation (measured by AMD): Zen+ ~3%, Zen 2 ~15%, Zen 3 ~19%, Zen 4 ~13%, Zen 5 ~16% (desktop) and ~37% for ML/HPC (EPYC).
- Zen 5 is manufactured on 4nm node, includes improved branch prediction, wider pipelines and vectors, and deeper window size.
- Zen 4 (Ryzen 7000 series) uses 5nm process, reaches up to 5.7 GHz, has doubled L2 cache per core, and delivers up to 13% IPC increase and up to 29% more single-thread performance when combined with clock speed increases.
- Zen 3 introduced a "unified complex" design reducing core-to-core and core-to-cache latencies, with direct access to twice as much L3 cache as Zen 2.
- Zen 2 doubled L3 cache to 32 MB, provided 256-bit floating-point throughput, and introduced TAGE branch predictor.
- Original Zen (2017) was on 14nm, up to 4 GHz; Zen+ die-shrunk to 12nm with about 3% IPC improvement.
- Zen 3+ (Ryzen 6000 mobile) uses 6nm process and focuses on efficiency, with up to 29 hours of video playback.
- EPYC server variants include both standard Zen cores and dense "c" variants (e.g., Zen 4c, Zen 5c) for higher core counts in the same thermal envelope.

## Relationships

- Both the AMD Zen core architecture and the [[amd_cdna]] GPU architecture use chiplet-based multi-chip module packaging—Zen uses chiplets for CPU cores and I/O, while CDNA 3 uses advanced 3D chiplet integration for its compute dies. This shared design philosophy allows AMD to scale performance and optimize for different workloads.

## Sources

- [AMD "Zen" Core Architecture](raw/cache/39cf99e1b8b3d730.md)
