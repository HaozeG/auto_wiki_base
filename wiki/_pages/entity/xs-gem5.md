---
canonical_name: XS-GEM5
aliases:
- XiangShan GEM5
- OpenXiangShan/GEM5
- xs-gem5
subtype: null
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 0.7
  bridge_score: 0.5
  hub_potential: 0.6
sources:
- raw/cache/70134d7b089934ef.md
- https://github.com/OpenXiangShan/GEM5
source_url: https://github.com/OpenXiangShan/GEM5
fetched_at: '2026-07-09T03:03:32.877543+00:00'
type: entity
created: '2026-07-09'
updated: '2026-07-09'
cold_start: true
inbound_links: 0
---

# XS-GEM5

XS-GEM5 is a gem5-based, full-system RISC-V simulator developed by the OpenXiangShan project. It is the only open-source RISC-V simulator that is strictly calibrated against high-performance RTL (XiangShan Nanhu and Kunminghu), achieving over 95% correlation on SPECCPU 2006 benchmarks. The simulator supports multiple configuration variants reflecting different stages of the Kunminghu microarchitecture: kmhv2 (V2 baseline), kmhv3 (RTL-aligned mainline), and idealkmhv3 (performance-tuned with aggressive settings). In SPECCPU06 checkpoint evaluation, idealkmhv3 exceeds 20 points/GHz, making XS-GEM5 one of the highest-performance open-source simulators, while kmhv3 exceeds 15 points/GHz. XS-GEM5 diverged from upstream gem5 in June 2022 and focuses on cycle-accurate alignment with XiangShan RTL.

## Key Claims

- Claim: XS-GEM5 is the only open-source RISC-V simulator strictly calibrated against high-performance RTL (XiangShan Nanhu/Kunminghu). Evidence: readme states "the ONLY open-source RISC-V simulator strictly calibrated against high-performance RTL (XiangShan Nanhu/Kunminghu), achieving >95% correlation on SPECCPU 2006."
- Claim: idealkmhv3 configuration exceeds 20 points/GHz on SPECCPU06 checkpoints. Evidence: readme states "`idealkmhv3.py` exceeds 20 points/GHz."
- Claim: kmhv3 configuration exceeds 15 points/GHz and is RTL-aligned. Evidence: readme states "`kmhv3.py`, the RTL-aligned configuration, exceeds 15 points/GHz."
- Claim: Features include decoupled frontend with TAGESC, ITTAGE, optional Loop predictor, instruction latency calibrated to Kunminghu, distributed scheduler, RVV calibration, and multiple prefetching algorithms. Evidence: readme Feature list.
- Claim: Tencent Penglai Laboratory contributed the MGSC predictor (reduced MPKI by 10%, improved performance by 0.3-0.4 points/GHz) and L2 Next Prefetcher (improved MCF performance by 23%, overall by 1.7%). Evidence: readme Thanks section.

## Relationships

No specific relationship to visible context pages.

## Sources

- [OpenXiangShan/GEM5 - GitHub](raw/cache/70134d7b089934ef.md)
