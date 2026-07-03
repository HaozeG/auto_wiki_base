---
canonical_name: XuanTie C950
aliases:
- Alibaba XuanTie C950
- C950
- Damo Academy C950
subtype: null
tags:
- RISC-V
- Alibaba
- XuanTie
- server
- AI
hardware_targets:
- XuanTie C950
toolchains: []
constraints:
- 5nm process
- 64-bit
scorecard:
  novelty_delta: 0.9
  claim_density: 0.7
  self_containedness: 0.8
  bridge_score: 0.7
  hub_potential: 0.6
sources:
- raw/cache/50b1221e64e86cf6.md
- https://chinabizinsider.com/alibabas-damo-academy-unveils-xuantie-c950-pushing-risc-v-into-server-class-ai-computing/
source_url: https://chinabizinsider.com/alibabas-damo-academy-unveils-xuantie-c950-pushing-risc-v-into-server-class-ai-computing/
fetched_at: '2026-07-02T09:38:46.830031+00:00'
type: hardware_target
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 16
---

# XuanTie C950

The XuanTie C950 is a 64-bit multi-core central processing unit designed by Alibaba Group's Damo Academy, using the open-standard RISC-V instruction set architecture. Fabricated on a 5nm semiconductor process, the chip targets server-class AI computing and agentic AI workloads, positioning RISC-V for cloud infrastructure. Damo Academy reported that the C950 achieved over 70 points in the SPECint2006 single-core benchmark, a score it framed as a first for RISC-V in general-purpose performance. The launch signals RISC-V's move from edge devices into server-class AI, which could reshape China's chip supply chain and cloud procurement. Alibaba has stated the chip is ready to power cloudy servers and aims to challenge proprietary Western architectures with open-source competition.

## Key Claims

- The XuanTie C950 is built on a 5nm process.
- It is a 64-bit multi-core CPU designed for agentic AI and cloud computing workloads.
- Damo Academy claims it is the most powerful RISC-V processor to date.
- It surpassed 70 points in the SPECint2006 single-core benchmark, a first for RISC-V general-purpose performance.
- The chip is intended to compete with proprietary Western architectures.

## Optimization-Relevant Details

- ISA/profile: RISC-V (open-standard).
- Vector/matrix/accelerator support: Not explicitly detailed in available sources; target workloads suggest AI acceleration capabilities.
- Memory/cache/TLB/DMA: Not specified in available sources.
- Compiler/toolchain support: Not specified in available sources.

## Relationships

- [[xuantie-c950-specint2006]]: related via shared c950, risc-v, xuantie, xuantie c950.

- [[ventana-veyron-v2]]: related via shared risc-v, server.

- [[xuantie-c910-ice-board]]: related via shared xuantie.

- [[xuantie-c950-specint2006]]: The SPECint2006 benchmark result for this hardware target.
- [[cpa-factored-gemmini-systolic-array]]: A related optimization recipe for an AI accelerator, though not directly connected to the C950 architecture.
- Insufficient context for additional cross-links to entity pages within the wiki.

## Sources

- [Alibaba Damo Academy Unveils XuanTie C950, Pushing RISC-V Into Server-Class AI Computing](https://chinabizinsider.com/alibabas-damo-academy-unveils-xuantie-c950-pushing-risc-v-into-server-class-ai-computing/)
- [EE Times coverage](https://www.eetimes.com/alibaba-launches-xuantie-c950-cpu-for-agentic-ai/)
- [Nikkei Asia coverage](https://asia.nikkei.com/Business/Tech/Semiconductors/Alibaba-unveils-flagship-RISC-V-chip-XuanTie-C950-to-meet-AI-demand)
