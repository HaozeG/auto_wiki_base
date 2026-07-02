---
canonical_name: preDRAC
aliases: []
subtype: null
tags: []
scorecard:
  novelty_delta: 0.8
  claim_density: 0.6
  self_containedness: 0.6
  bridge_score: 0.3
  hub_potential: 0.2
sources:
- raw/cache/473e7fa631f60e39.md
- https://upcommons.upc.edu/server/api/core/bitstreams/d56fe6f1-b90e-4358-877f-403ba87b96e4/content
source_url: https://upcommons.upc.edu/server/api/core/bitstreams/d56fe6f1-b90e-4358-877f-403ba87b96e4/content
fetched_at: '2026-07-02T13:22:19.467269+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# preDRAC

preDRAC is a RISC-V general purpose processor capable of booting Linux, jointly developed by BSC, CIC-IPN, IMB-CNM (CSIC), and UPC. It adapts an open-source system-on-chip platform from lowRISC originally designed for the Berkeley Rocket RISC-V core, but replaces the core with Lagarto, a RISC-V processor core developed at CIC-IPN in Mexico. The design employs triple modular redundancy (TMR) with an asynchronous majority voter to achieve fault tolerance. According to the published research, this TMR implementation reduces cycle time by 25.1%, silicon area by 7.5%, and average power dissipation by 7.8% compared to existing implementations, demonstrating that efficient fault-tolerant RISC-V designs are feasible using open-source components.

## Key Claims

- preDRAC is a general purpose RISC-V processor that boots Linux.
- It is based on the lowRISC open-source SoC platform.
- The core used is Lagarto, a RISC-V core from CIC-IPN.
- The design uses triple modular redundancy (TMR) with an asynchronous majority voter.
- The TMR implementation reduces cycle time by 25.1%, area by 7.5%, and power by 7.8% compared to existing implementations.

## Relationships

- Insufficient context for additional cross-links; no entity pages exist in the wiki for related concepts. The wiki currently contains optimization_recipe pages such as [[cpa-factored-gemmini-systolic-array]] which targets RISC-V hardware efficiency but is not an entity page.

## Sources

- [An Academic RISC-V Silicon Implementation](https://upcommons.upc.edu/server/api/core/bitstreams/d56fe6f1-b90e-4358-877f-403ba87b96e4/content)
