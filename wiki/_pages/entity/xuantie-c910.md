---
canonical_name: XuanTie C910
aliases:
- C910
- T-HEAD XuanTie C910
- Xuantie C910
- OpenC910
- T-HEAD C910
- T-Head Xuantie C910
- C920 (vector extension version)
- Alibaba Xuantie C910
- T-Head XuanTie C910
- T-HEAD Xuantie C910
subtype: null
scorecard:
  novelty_delta: 0.85
  claim_density: 0.65
  self_containedness: 0.9
  bridge_score: 0.25
  hub_potential: 0.7
sources:
- raw/cache/d259cf05ce140dc4.md
- https://www.riscvschool.com/2023/03/09/t-head-xuantie-c910-risc-v/
- raw/cache/2653baa6434ac0da.md
- https://github.com/XUANTIE-RV/buildroot
- raw/cache/33ce295c0ab2ac0a.md
- https://chipsandcheese.com/p/alibabat-heads-xuantie-c910
- raw/cache/eb10b88383dee0c3.md
- raw/cache/6fb87a3cec8bb808.md
- raw/cache/7706f0f87d4138ff.md
source_url: https://www.riscvschool.com/2023/03/09/t-head-xuantie-c910-risc-v/
fetched_at: '2026-07-01T02:48:58.954759+00:00'
type: entity
tags: []
created: 2023-03-09
updated: '2026-07-02'
cold_start: true
inbound_links: 1
needs_summary_revision: true
---

# XuanTie C910

The XuanTie C910 (also known as C910, T-HEAD XuanTie C910, Xuantie C910, or OpenC910) is a 64-bit high-performance RISC-V processor core designed by T-Head Semiconductor (Alibaba). It implements the RV64GCV instruction set architecture, which combines the standard RV64IMAFDC base with the vector extension (V). The microarchitecture is superscalar and out-of-order, built around a 12-stage pipeline to achieve competitive control flow throughput, compute density, and operating frequency. Custom extensions enrich the ISA with specialized operations for arithmetic, bit manipulation, load/store, and TLB/cache management. The core targets embedded and high-performance application domains and is publicly available as the open-source OpenC910 project on GitHub, enabling community adoption, evaluation, and integration into system-on-chip designs.

## Key Claims

- 64-bit RISC-V superscalar, out-of-order core.
- 12-stage pipeline microarchitecture.
- RV64GCV ISA: base RV64GC plus vector extension (V).
- Custom extensions for arithmetic, bit manipulation, load/store, and TLB/cache operations.
- Industry-leading performance in control flow, computing, and frequency (claimed by T-HEAD).
- Open-source release as OpenC910 on GitHub.
- Early adopter of the RISC-V vector extension among out-of-order cores available in hardware.

## Relationships

The C910 can act as a host processor in SoCs that integrate domain-specific accelerators such as [[gemmini]]. At present, the wiki does not contain other pages that would provide additional direct cross-links (insufficient context for additional cross-links).

## Sources

- [T-HEAD XuanTie C910 – RISC-V](https://www.riscvschool.com/2023/03/09/t-head-xuantie-c910-risc-v/)
- [XUANTIE-RV/openc910 GitHub repository](https://github.com/XUANTIE-RV/openc910)
