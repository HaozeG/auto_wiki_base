---
canonical_name: AMD CDNA
aliases:
- CDNA
- Compute DNA
- CDNA 1
- CDNA 2
- CDNA 3
- AMD CDNA 3
- CDNA3
- MI300X GPU architecture
subtype: null
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 0.9
  bridge_score: 0.5
  hub_potential: 0.3
sources:
- raw/cache/9125f5a6c386787e.md
- https://en.wikipedia.org/wiki/CDNA_(microarchitecture)
- raw/cache/76e45c9ccb69f373.md
- https://zhaifeiyue.github.io/papers/amd-cdna3-whitepaper/detail.html
source_url: https://en.wikipedia.org/wiki/CDNA_(microarchitecture)
fetched_at: '2026-07-17T09:17:07.157726+00:00'
type: entity
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 10
---

# AMD CDNA

AMD CDNA (Compute DNA) is a compute-oriented GPU microarchitecture designed by AMD for data center and high-performance computing applications. First announced in March 2020, CDNA succeeded the Graphics Core Next (GCN) architecture while diverging from the consumer-focused RDNA line. CDNA removes all graphics-specific hardware such as render output units and display engines, focusing instead on matrix compute and memory bandwidth. The family consists of three generations: CDNA 1 (Arcturus, 2020), CDNA 2 (2021, using multi-chip module packaging), and CDNA 3 (MI300 series, 2023, with advanced 3D chiplet integration). These generations power the AMD Instinct accelerator line and have been manufactured on TSMC N7, N6, and N5 nodes.

## Key Claims

- CDNA 1 (Arcturus) die: 750 mm², 25.6 billion transistors on TSMC N7, with 120 compute units and a 4096-bit HBM2 memory bus delivering 32 GB of memory at just over 1200 GB/s bandwidth.
- CDNA 2 introduced a multi-chip module (MCM) design using an elevated fanout bridge (EFB) to connect dies, first featured in the Instinct MI250X and MI250.
- CDNA 3 switched to a chiplet design with 15 unique dies on multiple nodes, connected with advanced 3D packaging, used in the Instinct MI300X and MI300A.
- CDNA removed all graphics hardware (ROPs, display engine, graphics caches) while retaining the VCN media engine for HEVC, H.264, and VP9 decoding.
- CDNA added dedicated matrix compute hardware (4 matrix units per CU) and support for BF16, INT8, and INT4 datatypes.
- The compute units (CUs) are organized into 4 asynchronous compute engines (ACEs) per generation, each with independent command execution.
- CDNA 1 achieves a 20% HBM clock bump over Vega 20, resulting in a roughly 200 GB/s bandwidth increase, and includes a shared 4 MB L2 cache.
- In December 2022, Samsung demonstrated a Processing-In-Memory (PIM) variant of the MI100 using CDNA 1, achieving throughput improvements and power reduction in a 96-card cluster.

## Relationships

- This page covers the first three generations of the CDNA microarchitecture family, which serve as direct predecessors to [[amd_cdna_4]]. CDNA 4 (2025) builds on the chiplet approach of CDNA 3 while introducing new matrix formats and an AI-first focus, whereas CDNA 1–3 established the compute-only DNA, MCM packaging, and 3D chiplet integration that form the architectural foundation.

## Sources

- [CDNA (microarchitecture) - Wikipedia](raw/cache/9125f5a6c386787e.md)
