---
canonical_name: Golden Cove
aliases:
- Golden Cove Core
- Golden Cove P-core
- Intel Golden Cove
- Alder Lake P-core
- ADL P-core
subtype: null
hardware_targets:
- Golden Cove
workloads:
- general-purpose computing
- matrix operations (AMX)
datatypes:
- INT8 (AMX)
- BFLOAT16 (AMX)
- FP16 (AVX512_FP16)
- FP32
metrics:
- IPC (19% over Cypress Cove)
- reorder buffer size (512)
- L2 cache (1.25 MiB client, 2 MiB server)
- AMX throughput (2048 INT8 ops/cycle, 1024 BLOAT16 ops/cycle)
toolchains: []
constraints: []
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
- raw/cache/7fa9f612569e3589.md
- https://chipsandcheese.com/p/popping-the-hood-on-golden-cove
source_url: https://silicon.redfire.dev/events/intel/architecture-day-2021/
fetched_at: '2026-07-17T12:56:19.407744+00:00'
type: processor_architecture
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 0
outbound_links:
- target: gracemont
  reason: Golden Cove is the performance core paired with Gracemont efficiency core
    in Intel Alder Lake hybrid architecture
---

# Golden Cove

Golden Cove is a high-performance processor microarchitecture designed by Intel as the performance core (P-core) in the Alder Lake client and Sapphire Rapids server processors. It succeeds the Cypress Cove core and delivers a 19% IPC improvement measured across SPEC CPU 2017, SYSmark 25, Crossmark, PCMark 10, WebXPRT3, and Geekbench 5.4.1. The core features a 6-wide decoder (6 simple, 1 complex) with a μop cache of 4K μops (up from 2.5K), a 512-entry reorder buffer (up from 352), 12 execution ports, and merged 5 integer ALUs and 3 floating-point/vector ALUs. It includes 1.25 MiB L2 cache for client and 2 MiB for server variants, with L1 iTLB increased to 256 entries for 4K pages and 32 entries for 2M/4M pages. Golden Cove introduces Advanced Matrix Extensions (AMX) supporting 2048 INT8 operations per cycle and 1024 BLOAT16 operations per cycle at three times lower power than VNNI-INT8, and adds FP16 support for AVX-512 (AVX512_FP16).

## Key Claims

- 19% IPC improvement over Cypress Cove across multiple benchmarks.
- 512-entry reorder buffer (vs 352 in Cypress Cove, 256 in Zen 3).
- 6-wide decode (6 simple + 1 complex).
- 1.25 MiB (client) / 2 MiB (server) L2 cache.
- AMX: 2048 INT8 ops/cycle, 1024 BLOAT16 ops/cycle, 3× lower power than VNNI-INT8.
- AVX512_FP16 support.
- L1 iTLB: 256 entries (4K), 32 entries (2M/4M).
- L2 BTB: 12K branch targets (up from 5K).
- Mispredict penalty: 17 cycles (up from 16).

## Relationships

- [[gracemont]]: Golden Cove is the performance core paired with Gracemont efficiency core in Intel Alder Lake hybrid architecture.

## Sources

- [Intel Architecture Day 2021 - Silicon](raw/cache/dbab3c0d1ddceccb.md)
