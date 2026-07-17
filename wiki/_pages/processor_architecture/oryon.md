---
canonical_name: Oryon
aliases:
- Qualcomm Oryon
- Qualcomm Oryon Core
- Oryon Core
- Snapdragon X Elite core
- Snapdragon X Elite Oryon
- Qualcomm Oryon CPU
subtype: null
hardware_targets:
- Snapdragon X Elite
- Snapdragon X Plus
- Snapdragon 8 Elite
- Snapdragon X2 Elite
- Snapdragon 8 Gen 5
workloads:
- laptops
- smartphones
- tablets
datatypes: []
metrics:
- core count
- max multithread frequency
- boost frequency
- cache size
- memory type
toolchains: []
constraints:
- ARMv8.7-A (1st/2nd generation)
- ARMv9.3-A (3rd generation)
evidence_strength: derived
tags:
- ARM
- Qualcomm
- Nuvia
- CPU
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 0.9
  bridge_score: 0.5
  hub_potential: 0.8
sources:
- raw/cache/acd782c1c03a49b6.md
- https://en.wikipedia.org/wiki/Oryon
- raw/cache/b750a8e8016e8d62.md
- https://chipsandcheese.com/p/hot-chips-2024-qualcomms-oryon-core
- raw/cache/3e337307a4c4f507.md
- https://www.servethehome.com/snapdragon-x-elite-qualcomm-oryon-cpu-design-and-architecture-hot-chips-2024-arm/
source_url: https://en.wikipedia.org/wiki/Oryon
fetched_at: '2026-07-17T12:02:29.766991+00:00'
type: processor_architecture
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 0
---

# Oryon

Oryon is a series of custom CPU cores implementing the ARMv8.7-A and ARMv9.3-A instruction set architectures, designed by Qualcomm through its acquisition of Nuvia in 2021. First released in June 2024 with the Snapdragon X Elite platform, Oryon represents Qualcomm's first fully custom microarchitecture for PC and mobile SoCs since the original Kryo. The core series spans three generations to date: the first generation powers Snapdragon X-series laptop processors with up to 12 cores and 42 MB of total cache; the second generation targets smartphones via the Snapdragon 8 Elite platform with up to 8 cores and 32 MB of cache; and the third generation introduces both X2 Elite and 8 Gen 5 variants with up to 6 Prime cores and 53 MB of cache. Oryon cores are designed for high-performance computing in laptops, tablets, and smartphones, leveraging a custom microarchitecture developed from Nuvia's Phoenix core design.

## Key Claims

- Custom ARM CPU core microarchitecture developed by Qualcomm, originally from Nuvia.
- First generation (Snapdragon X series): up to 12 cores, 42 MB cache, boost up to 4.3 GHz (dual-core), LPDDR5x-8448 memory.
- Second generation (Snapdragon 8 Elite): 2 performance cores + 6 efficiency cores, 32 MB cache, boost up to 4.47 GHz (dual-core), LPDDR5x-10600 memory.
- Third generation: Snapdragon X2 Elite with up to 6 Prime cores, 53 MB cache, boost up to 5.0 GHz; Snapdragon 8 Gen 5 with 2 Prime cores, boost up to 4.61 GHz.
- Implements ARMv8.7-A for 1st and 2nd generations, ARMv9.3-A for 3rd generation.
- Used in Snapdragon X series (laptops, Q2 2024), Snapdragon 8 Elite (smartphones, Q4 2024), Snapdragon X2 Elite (Q1 2026), and Snapdragon 8 Gen 5 (Q4 2025).

## Relationships

No specific relationship to visible context pages in the current wiki.

## Sources

- [Oryon - Wikipedia](raw/cache/acd782c1c03a49b6.md)
