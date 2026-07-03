---
canonical_name: XuanTie C950 SPECint2006
aliases:
- XuanTie C950 SPECint2006 score
- C950 SPECint2006
subtype: null
tags:
- benchmark
- RISC-V
- XuanTie
- C950
- SPEC
hardware_targets:
- XuanTie C950
workloads:
- SPECint2006 single-core
datatypes: []
metrics:
- SPECint2006 single-core score
toolchains: []
hardware_versions:
- XuanTie C950 (5nm)
software_versions: []
measurement_method: Announcement by Damo Academy; no detailed methodology or system
  configuration provided.
evidence_strength: reported
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
type: benchmark_result
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# XuanTie C950 SPECint2006

According to an announcement by Alibaba Group's Damo Academy on March 24, 2026, the XuanTie C950 processor—a 64-bit multi-core RISC-V CPU fabricated on a 5nm process—surpassed 70 points in the SPECint2006 single-core benchmark. Damo Academy characterized this result as the first time a RISC-V processor has reached this performance level in general-purpose computing. The benchmark score positions the C950 for server-class AI workloads, including agentic AI and cloud computing. No detailed system configuration, clock speed, memory hierarchy, or power measurements were provided in the announcement; therefore the evidence strength is classified as reported rather than measured. The score was quoted by multiple industry outlets including EE Times and Nikkei Asia.

## Key Claims

- The XuanTie C950 achieved over 70 points in the SPECint2006 single-core benchmark.
- This is claimed as a first for RISC-V in general-purpose performance.
- The result supports the chip's positioning for server-class AI computing.

## Measurement Context

- Hardware version: XuanTie C950 (5nm process).
- Software/toolchain version: Not specified.
- Workload shape: SPECint2006 single-core (standardized integer benchmark suite).
- Metric: Score (points).
- Method: Reported by Damo Academy; no detailed methodology.
- Evidence strength: reported.

## Relationships

- [[xuantie-c950]]: The hardware target for which this benchmark result is reported.
- Insufficient context for additional cross-links; one optimization recipe page exists but is unrelated to the C950 benchmark.

## Sources

- [Alibaba Damo Academy Unveils XuanTie C950, Pushing RISC-V Into Server-Class AI Computing](https://chinabizinsider.com/alibabas-damo-academy-unveils-xuantie-c950-pushing-risc-v-into-server-class-ai-computing/)
- [EE Times: Alibaba Launches XuanTie C950 CPU for Agentic AI](https://www.eetimes.com/alibaba-launches-xuantie-c950-cpu-for-agentic-ai/)
- [Nikkei Asia: Alibaba unveils flagship RISC-V chip XuanTie C950 to meet AI demand](https://asia.nikkei.com/Business/Tech/Semiconductors/Alibaba-unveils-flagship-RISC-V-chip-XuanTie-C950-to-meet-AI-demand)
