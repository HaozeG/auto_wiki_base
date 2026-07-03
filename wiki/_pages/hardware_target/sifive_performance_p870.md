---
canonical_name: SiFive Performance P870
aliases:
- P870
- SiFive P870
subtype: null
tags:
- RISC-V
- SiFive
- out-of-order
hardware_targets:
- SiFive Performance P870
toolchains:
- Linux
- Android
constraints:
- RISC-V 64-bit out-of-order superscalar
- six-wide dispatch
- dual 128-bit vector units
- IOMMU
- hypervisor support
- WorldGuard
- up to 32 cores in eight four-core clusters
scorecard:
  novelty_delta: 0.9
  claim_density: 0.85
  self_containedness: 0.85
  bridge_score: 0.6
  hub_potential: 0.5
sources:
- raw/cache/29110787b8f23bbd.md
- https://www.jonpeddie.com/news/sifive-performance-p870-and-the-sifive-intelligence-x390/
source_url: https://www.jonpeddie.com/news/sifive-performance-p870-and-the-sifive-intelligence-x390/
fetched_at: '2026-07-02T04:25:16.741148+00:00'
type: hardware_target
created: '2026-07-02'
updated: '2026-07-02'
cold_start: false
inbound_links: 1
needs_summary_revision: false
outbound_links:
- target: k230
  reason: An SoC integrating a different RISC-V core (C908) for AIoT, providing a
    contrast in target application
- target: xuantie_c907
  reason: Another RISC-V core with matrix extension, offering an alternative approach
    to vector acceleration
---

# SiFive Performance P870

The SiFive Performance P870 is a 64-bit out-of-order superscalar RISC-V processor core designed for high-performance computing applications. It complies with the open-standard RISC-V instruction set architecture and is fully compatible with Linux and Android operating systems. The core features a six-wide instruction dispatch, an I/O memory management unit (IOMMU), hardware support for hypervisors, and SiFive's WorldGuard technology for critical code and data isolation within system-on-chip designs. Compared to its predecessor, the P670, the P870 delivers a 50% improvement in performance, achieving a SPECint2K6 benchmark score of 18 per MHz. While SiFive has not disclosed the maximum clock frequency, company representative Brad Burgess indicated at Hot Chips that the core could reach frequencies well into the 3GHz range. The performance gain is attributed to the wider six-wide out-of-order dispatch over the P670's four-wide configuration. The P870 retains dual 128-bit vector units. The core design supports integration into SoCs with up to 32 cores, organized into eight four-core clusters that share an L2 cache pool. These clusters need not be homogeneous; the P870 can be paired with low-power efficiency cores like the P470 or with SiFive's Intelligence family of vector-optimized cores.

## Key Claims

- 64-bit out-of-order superscalar RISC-V core with six-wide dispatch.
- 50% performance uplift over predecessor P670.
- SPECint2K6 score of 18 per MHz.
- Expected clock frequencies exceeding 3 GHz.
- IOMMU, hypervisor support, and WorldGuard isolation.
- Dual 128-bit vector units.
- Supports up to 32 cores in eight four-core clusters with shared L2 cache.
- Heterogeneous cluster support (e.g., pairing with P470 or Intelligence cores).

## Optimization-Relevant Details

- ISA/profile: RISC-V 64-bit out-of-order superscalar.
- Vector/matrix/accelerator support: Dual 128-bit vector units.
- Memory/cache/TLB/DMA: IOMMU; shared L2 cache in clusters (details not fully disclosed).
- Compiler/toolchain support: Compatible with Linux and Android ecosystems.

## Relationships

- Related RISC-V core for comparison: [[xuantie_c908]]
- Earlier-generation SiFive Performance core: [[xuantie_c906]] (not SiFive, but a reference point for RISC-V performance cores).
- [[k230]]: An SoC integrating a different RISC-V core (C908) for AIoT, providing a contrast in target application.
- [[xuantie_c907]]: Another RISC-V core with matrix extension, offering an alternative approach to vector acceleration.

## Sources

- https://www.jonpeddie.com/news/sifive-performance-p870-and-the-sifive-intelligence-x390/
