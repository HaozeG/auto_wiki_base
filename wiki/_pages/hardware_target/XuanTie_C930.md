---
cold_start: true
constraints:
- 16-stage integer pipeline
- instruction fusion support
- RVA23 profile compliance
- Designed for AI-HPC workloads
- Server-grade processor
created: '2026-07-02'
hardware_targets:
- XuanTie C930
inbound_links: 0
scorecard:
  bridge_score: 0.5
  claim_density: 0.6
  hub_potential: 0.3
  novelty_delta: 0.9
  self_containedness: 0.8
sources:
- https://telegra.ph/Anons-Xuantie-C930-S908X-i-C920V3-03-02
- https://www.tomshardware.com/news/alibaba-launches-risc-v-based-xuantie-c930
- https://www.golem.de/news/xuantie-c930-alibabas-neuer-risc-v-prozessor-ist-eine-
tags:
- RISC-V
- XuanTie
- T-Head
- Alibaba
- C930
- AI-HPC
- server
toolchains:
- RISC-V GNU toolchain (assumed)
type: hardware_target
updated: '2026-06-29'
---

# XuanTie C930

The XuanTie C930 is a high-performance 64-bit RISC-V processor core developed by Alibaba's T-Head (Damo Academy), announced in early 2025 as the company's first server-grade RISC-V processor. It features a 16-stage integer pipeline and supports instruction fusion, a technique that combines multiple instructions into one for improved throughput. The core is compliant with the RVA23 profile, indicating support for vector extensions and other advanced ISA features, and is primarily targeted at AI-HPC workloads. Compared to its predecessor XuanTie C920 (which reached up to 2.5 GHz), the C930's clock frequency has not been publicly disclosed, but its deeper pipeline architecture suggests potential for higher operating frequencies. The C930 is part of Alibaba's broader XuanTie series and reflects the company's push towards indigenous high-performance RISC-V silicon for data center and edge AI applications.

## Key Claims

- XuanTie C930 is a 64-bit RISC-V core with a 16-stage integer pipeline.
- Supports instruction fusion for improved execution efficiency.
- Compliant with the RVA23 profile, enabling vector and other modern ISA extensions.
- Announced as Alibaba's first server-grade RISC-V processor, targeting AI-HPC workloads.
- Uses a significantly longer pipeline than the prior C920 (which had a shallower pipeline and achieved 2.5 GHz); C930 clock frequency not yet specified.
- Part of the XuanTie series from T-Head/Damo Academy, including the C908X and C920V3 variants mentioned in the same announcement.

## Optimization-Relevant Details

- ISA/profile: RVA23 (includes vector extension 1.0, hypervisor, and other profiles).
- Vector/matrix/accelerator support: Implied by RVA23 compliance; specific vector unit width not disclosed.
- Memory/cache/TLB/DMA: Not specified in available sources.
- Compiler/toolchain support: Assumed RISC-V GNU toolchain; vendor-specific Xuantie-900-gcc toolchain likely applicable.

## Relationships

- [[Gemmini_Architecture]] – Both are RISC-V hardware targets; Gemmini is an open-source DNN accelerator generator that can integrate with cores like the C930.
- [[Sipeed_MAIX_series]] – Another RISC-V-based hardware platform, though aimed at edge AI and using the Kendryte K210 core, contrasting with the server-grade C930.
- Insufficient context for additional cross-links; the C930 is a new entry in the wiki without existing sibling pages for the XuanTie product family.

## Sources

- [Telegraph article (Russian): Anons Xuantie C930, S908X i C920V3](https://telegra.ph/Anons-Xuantie-C930-S908X-i-C920V3-03-02)
- [Tom's Hardware: Alibaba launches RISC-V-based XuanTie C930](https://www.tomshardware.com/news/alibaba-launches-risc-v-based-xuantie-c930)
- [Golem.de: Xuantie C930 – Alibabas neuer RISC-V-Prozessor ist eine ...](https://www.golem.de/news/xuantie-c930-alibabas-neuer-risc-v-prozessor-ist-eine-)

