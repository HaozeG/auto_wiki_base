---
cold_start: true
created: 2026-06-27
inbound_links: 15
needs_summary_revision: false
scorecard:
  bridge_score: null
  claim_density: null
  hub_potential: null
  novelty_delta: null
  self_containedness: null
sources:
- https://chipsandcheese.com/p/alibabat-heads-xuantie-c910
- https://riscv.org/blog/alibaba-open-sources-four-risc-v-cores-xuantie-e902-e906-c906-and-c910-jean-luc-aufranc-cnx-software/
tags:
- risc-v
- processor
- alibaba
- out-of-order
- open-source
type: entity
updated: 2026-06-27
---

# Alibaba XuanTie C910 and C920

The Alibaba XuanTie C910 and C920 are high-performance out-of-order RISC-V cores developed by T-Head, Alibaba's chip design subsidiary, targeting applications in AI inference, edge servers, industrial control, and ADAS. The C910 was open-sourced by Alibaba under a permissive license, making it one of the highest-performance publicly available RISC-V core designs. The C920 is an incremental update that upgrades the vector extension support from RVV 0.7.1 to the ratified RVV 1.0 standard while otherwise preserving the C910 microarchitecture. Both cores are manufactured on TSMC 12nm FinFET.

## Key Claims

- The C910 is a 3-wide out-of-order superscalar core with a 12-stage pipeline, targeted at 2.0–2.5 GHz on TSMC 12nm FinFET, where a single core occupies 0.8 mm².
- The C910 implements RVV 0.7.1 (a pre-ratification draft of the RISC-V Vector Extension) with masking and variable vector length support, making it an early production adopter of RISC-V vector processing.
- C910 cores are deployed in clusters of up to four cores sharing a unified L2 cache, enabling scalable SoC integration for edge AI and server workloads.
- The C920 preserves the C910's 3-wide out-of-order pipeline and 12nm target process but upgrades vector support to RVV 1.0, ensuring software compiled for the ratified standard runs without modification.
- Alibaba open-sourced the C910 RTL alongside three other cores (E902, E906, C906) under permissive licensing, enabling third-party SoC integration and academic research.
- The C950, released in 2026, delivers over 3× the SPECint2006 single-core score of the C920 and 4× the memory bandwidth, representing a generational leap in RISC-V CPU performance.

## Relationships

- [[alibaba_xuantie_c950]] — C950 is the successor, built on 5nm with proprietary matrix extensions and native LLM inference support
- [[risc_v_vector_extension]] — C910 adopted RVV draft 0.7.1; C920 upgraded to ratified RVV 1.0

## Sources

- Chips and Cheese architectural analysis: https://chipsandcheese.com/p/alibabat-heads-xuantie-c910
- Alibaba open-source announcement: https://riscv.org/blog/alibaba-open-sources-four-risc-v-cores-xuantie-e902-e906-c906-and-c910-jean-luc-aufranc-cnx-software/
