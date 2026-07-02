---
canonical_name: SiFive Intelligence Family
aliases:
- SiFive Intelligence
- Intelligence Family
- SiFive Intelligence 2nd Gen
- SiFive X series
subtype: null
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.5
  self_containedness: 0.8
  bridge_score: 0.8
  hub_potential: 0.7
sources:
- raw/cache/110ff4c712c0d37b.md
- https://www.sifive.com/cores/intelligence
source_url: https://www.sifive.com/cores/intelligence
fetched_at: '2026-07-01T06:06:13.760396+00:00'
type: entity
created: '2026-07-01'
updated: '2026-07-01'
cold_start: false
inbound_links: 1
needs_summary_revision: false
---

# SiFive Intelligence Family

SiFive Intelligence Family is a line of RISC-V processor IP cores from SiFive that integrate scalar, vector, and matrix compute capabilities for AI inference and machine learning workloads. The family adopts a software-first approach, providing a scalable platform from ultra-low-power edge devices to high-performance data center applications. The vector engine within these cores handles data processing tasks such as filters, transforms, convolutions, and AI inference without requiring additional processing elements. The second generation, announced in September 2025, includes five new products: X160 Gen 2, X180 Gen 2, X280 Gen 2, and X390 Gen 2. These cores target a broad range of AI compute from far-edge IoT to data centers, combining scalar, vector, and matrix compute in a unified processor design.

## Key Claims

- Software-first approach to processor design, addressing deployment of machine learning and AI at the edge.
- Integrated scalar, vector, and matrix compute in a scalable platform from extremely low power to high-performance compute.
- Second Generation (2025) family includes five new RISC-V-based products spanning IoT to data center AI workloads.
- Vector engine provides data processing abilities for filters, transforms, convolutions, and AI inference without additional processing elements.
- The processor design allows customers to focus on data processing capabilities of accelerators rather than integration.

## Relationships

- [[xuantie_c908]]: Another RISC-V processor core targeting AI inference with vector extensions, developed by T-Head Semiconductor, representing a different vendor approach in the same market space.
- [[rvme]]: A matrix engine coprocessor design for RISC-V, representing a research-oriented approach to accelerating GEMM for deep learning, complementary to SiFive's commercial IP.
- [[sifive_intelligence_x280]] and [[sifive_intelligence_x200_series]]: specific cores within this Intelligence product family.

## Sources

- SiFive official product page: https://www.sifive.com/cores/intelligence
- Business Wire press release: https://www.businesswire.com/news/home/20250908512334/en/
- ServeTheHome coverage: SiFive 2nd Gen Intelligence Family Launched
- RISC-V International blog: SiFive Intelligence Family – RISC-V
