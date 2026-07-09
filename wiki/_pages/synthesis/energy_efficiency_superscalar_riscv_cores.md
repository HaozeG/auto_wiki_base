---
canonical_name: Energy Efficiency of Superscalar RISC-V Cores
aliases: null
subtype: null
connected_entities:
- CVA6S+
- XuanTie C910
synthesis_status: draft
scorecard:
  bridge_score: 0.7
  contradiction_potential: 0.0
  cross_domain_connection: null
sources:
- raw/cache/dd944bc005e8fc47.md
- https://arxiv.org/html/2505.24363v1
source_url: https://arxiv.org/html/2505.24363v1
fetched_at: '2026-07-09T07:56:39.240753+00:00'
type: synthesis
created: '2026-07-09'
updated: '2026-07-09'
cold_start: true
inbound_links: 0
outbound_links:
- target: CVA6S+
  reason: Enhanced dual-issue in-order core from the same study
- target: XuanTie C910
  reason: Superscalar out-of-order core compared in the study
---

# Energy Efficiency of Superscalar RISC-V Cores: CVA6, CVA6S+, and C910

## RAG Summary

This synthesis compares the energy efficiency of three open-source RISC-V cores—the scalar single-issue CVA6, the dual-issue in-order CVA6S+, and the superscalar out-of-order XuanTie C910—using a consistent methodology with identical 22nm FDX technology, SoC platform (Cheshire), and EDA toolchain. The CVA6S+, an enhanced derivative of CVA6, achieves a 34.4% IPC improvement with only a 6% area increase, making it the area efficiency leader (GOPS/mm²). The XuanTie C910, modified for full RISC-V standard compliance, delivers a 119.5% IPC uplift at a 75% area cost, yet demonstrates competitive energy efficiency (GOPS/W), countering the notion that out-of-order execution necessarily sacrifices power efficiency. The study, conducted by researchers from ETH Zurich and the University of Bologna, underscores that both modest in-order superscalar enhancements and aggressive out-of-order designs can be energy-efficient when implemented with a common technology and platform. These findings are relevant for designers selecting RISC-V cores for automotive, aerospace, and embedded applications where performance and efficiency are both critical.

---

## Full Synthesis

This synthesis draws on the paper by Fu et al. (2025) which presents a consistent comparison of the three cores. The study implements all cores in GF22FDX technology within the Cheshire SoC platform and uses the same RISC-V ISA (RV64GC) and toolchain. The key findings are that CVA6S+ offers the best area efficiency, while the XuanTie C910 provides competitive energy efficiency, challenging conventional trade-offs. The modified C910 achieves full standard compliance, addressing interoperability issues that previously hindered adoption. The comparison highlights that open-source RISC-V cores can achieve a range of performance-efficiency points suitable for diverse application domains.

## Open Questions

- How do these cores compare under specific workloads (e.g., Dhrystone, CoreMark)? The paper does not provide per-workload breakdowns.
- What impact do the C910's interface modifications have on portability across SoC integration environments?
- How do these results scale to smaller technology nodes or different foundry processes?

## Connected Pages

- [[CVA6S+]]: Enhanced dual-issue in-order core from the same study.
- [[XuanTie C910]]: Superscalar out-of-order core compared in the study.

## Sources

- [Ramping Up Open-Source RISC-V Cores: Assessing the Energy ...](raw/cache/dd944bc005e8fc47.md)
