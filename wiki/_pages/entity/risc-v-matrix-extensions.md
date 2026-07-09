---
canonical_name: RISC-V Matrix Extensions
aliases:
- IME
- AME
- VME
- Zvma
- Integrated Matrix Extension
- Attached Matrix Extension
- Vector-Matrix Extension
- RISC-V matrix extension family
- Attached Matrix Extension (AME)
- RISC-V AME
subtype: null
tags: []
scorecard:
  novelty_delta: 0.7
  claim_density: 0.3
  self_containedness: 0.6
  bridge_score: 0.5
  hub_potential: 0.2
sources:
- raw/cache/b43be6f2d2a6a7f8.md
- https://zhuanlan.zhihu.com/p/23884812048
- raw/cache/a6588fba1f2c11f6.md
- https://github.com/riscv-admin/attached-matrix-extension/blob/main/charter.adoc
source_url: https://zhuanlan.zhihu.com/p/23884812048
fetched_at: '2026-07-09T02:46:16.676627+00:00'
type: entity
created: '2026-07-09'
updated: '2026-07-09'
cold_start: true
inbound_links: 0
outbound_links:
- target: ara2
  reason: VME is designed to be closely coupled with the RISC-V Vector Extension (RVV),
    the same vector extension standard implemented by the Ara2 open-source vector
    processor
---

# RISC-V Matrix Extensions

RISC-V Matrix Extensions represent a set of proposed instruction set extensions designed to accelerate matrix compute operations within the RISC-V ecosystem. Three major approaches have emerged: the Integrated Matrix Extension (IME) from Spacemit, the Attached Matrix Extension (AME) developed by Xuantie, Stream Computing, and SiFive under the designation Zvma, and the Vector-Matrix Extension (VME) which is based on an outer product formulation of matrix multiply. VME is designed to be closely coupled with the RISC-V Vector Extension (RVV) and aims to provide high performance, high power efficiency, and architectural simplicity. As of mid-2026, IME and VME are reported to be converging on specification freeze, indicating progress towards standardization. These extensions represent an important step for RISC-V in competing with other ISAs like ARM and x86 in matrix compute workloads.

## Key Claims

- Integrated Matrix Extension (IME) is proposed by Spacemit.
- Attached Matrix Extension (AME) is proposed by Xuantie, Stream Computing, and SiFive under the name Zvma.
- Vector-Matrix Extension (VME) is based on an outer product formulation of matrix multiply and is closely coupled with RVV.
- VME aims for high performance, high power efficiency, and architectural simplicity (similar to ARM's approach for matrix compute).
- AME is similar to the approach adopted by x86 for matrix compute.
- As of mid-2026, IME and VME are converging on specification freeze.

## Relationships

- [[ara2]]: VME is designed to be closely coupled with the RISC-V Vector Extension (RVV), the same vector extension standard implemented by the Ara2 open-source vector processor.

## Sources

- [From Vector to Matrix: The Future of RISC-V Matrix Extensions](raw/cache/b43be6f2d2a6a7f8.md)
