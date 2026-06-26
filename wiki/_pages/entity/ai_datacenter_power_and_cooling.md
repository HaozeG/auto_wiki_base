---
type: entity
tags: [infrastructure, power, cooling, data-center, AI-hardware]
sources:
  - https://nextwavesinsight.com/ai-data-center-liquid-cooling-infrastructure/
  - https://techplustrends.com/ai-data-center-power-requirements-2026-guide/
  - https://www.datacenterdynamics.com/en/opinions/how-liquid-cooling-is-redefining-data-center-efficiency-beyond-pue/
  - https://introl.com/blog/nuclear-power-ai-data-centers-microsoft-google-amazon-2025
  - https://smrintel.com/nuclear-data-center-deals/
  - https://ibinterviewquestions.com/guides/energy-investment-banking/data-center-power-boom-ai-demand-hyperscaler
created: 2026-06-26
updated: 2026-06-26
cold_start: true
inbound_links: 0
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# AI Data Center Power and Cooling

AI data centers hosting GPU clusters for training and inference are undergoing a fundamental infrastructure transition driven by GPU power density. A single NVIDIA H100 GPU draws approximately 700 W TDP, and a full DGX H100 server draws roughly 10,200 W; when networking, storage, and management overhead are included, the effective per-GPU power requirement rises to approximately 1,389 W. At rack level, traditional air-cooled facilities peak at 10–15 kW per rack, whereas modern AI GPU racks already reach 40–80 kW, and NVIDIA GB200 NVL72 racks draw 120–132 kW at full load, with projections reaching 370 kW per rack by 2026. The threshold at which air cooling becomes impractical is widely cited at approximately 100 W per chip — a level already exceeded by every current high-end AI accelerator. The dominant efficiency metric for data centers, Power Usage Effectiveness (PUE), measures total facility power divided by IT equipment power; a PUE of 1.0 is ideal. Conventional air-cooled hyperscale facilities achieve PUE of 1.50–1.80, direct-to-chip liquid cooling systems achieve 1.10–1.35, and two-phase immersion cooling achieves 1.01–1.03 — the best currently demonstrated. Hyperscalers are responding by committing to multi-gigawatt power supply agreements and pursuing nuclear energy to underpin long-term AI infrastructure expansion.

## Key Claims

- NVIDIA GB200 NVL72 racks draw 120–132 kW at full load, and next-generation AI racks could reach 370 kW by 2026, making liquid cooling structurally mandatory rather than optional.
- Goldman Sachs estimated that 76% of AI servers deployed by end of 2026 will require liquid cooling, up from 15% in 2024.
- Two-phase immersion cooling achieves PUE of 1.01–1.03 and supports rack densities of 150–250+ kW; direct-to-chip liquid cooling achieves PUE of 1.10–1.35 versus 1.50–1.80 for air-cooled facilities.
- Retrofitting air-cooled data center floor space to support liquid cooling requires 12–18 months of civil construction work, making cooling infrastructure — not chip supply or grid capacity — the near-term binding constraint on AI capacity expansion through 2027–2028.
- As of May 2026, every major hyperscaler has signed at least one nuclear power deal for AI capacity; across 13 announced projects, over 9.8 GW of nuclear capacity has been committed, including Microsoft's 20-year PPA for the Three Mile Island Unit 1 restart (835 MW) and Google's fleet deal with Kairos Power for 500 MW of small modular reactors.
- The IEA projects global data center electricity consumption to reach 945 TWh by 2030, with AI data center annual consumption reaching approximately 90 TWh by 2026 — roughly a tenfold increase from 2022 levels.
- Dell'Oro Group forecasts worldwide data center liquid cooling manufacturer revenue at approximately $6 billion in 2026, growing to nearly $7 billion by 2029, with Vertiv holding over 11% market share.
- Combined hyperscaler capex from Microsoft, Google, Meta, and Amazon is projected at approximately $725 billion in 2026, up 77% from roughly $410 billion in 2025.

## Relationships

- [[nvidia_hopper_h100]] — H100 GPU draws 700 W TDP; effective rack-level requirement rises to 1,389 W per GPU when accounting for full system overhead; exemplifies the power density threshold forcing liquid cooling adoption.
- [[nvidia_blackwell_b200]] — GB200 NVL72 rack draws 120–132 kW at full load, the primary driver of the 2025–2026 transition to mandatory liquid cooling.
- [[amd_mi300x]] — MI300X draws 750 W TDP, operating above the ~100 W/chip air-cooling threshold; rack integration follows the same liquid cooling requirements as H100.
- [[microsoft_azure_maia_100]] — Microsoft's Maia 100 ASIC (700 W TDP) is deployed in Azure data centers that will be partly powered by the Three Mile Island nuclear PPA.
- [[hbm_high_bandwidth_memory]] — HBM stacks contribute significantly to per-chip power draw on AI accelerators; power density of the memory subsystem is a co-driver of liquid cooling requirements.

## Sources

- Goldman Sachs liquid cooling adoption estimate (76% of AI servers by end 2026): https://ibinterviewquestions.com/guides/energy-investment-banking/data-center-power-boom-ai-demand-hyperscaler
- PUE ranges by cooling technology (Schneider Electric analysis cited in): https://techplustrends.com/ai-data-center-power-requirements-2026-guide/
- GB200 NVL72 rack power draw and 370 kW 2026 projection (Deloitte): https://nextwavesinsight.com/ai-data-center-liquid-cooling-infrastructure/
- Nuclear power deals overview (Microsoft TMI, Google Kairos, 9.8 GW committed): https://smrintel.com/nuclear-data-center-deals/
- IEA 945 TWh 2030 projection and 90 TWh AI 2026 estimate: https://introl.com/blog/nuclear-power-ai-data-centers-microsoft-google-amazon-2025
- Dell'Oro liquid cooling revenue forecast and Vertiv market share: https://nextwavesinsight.com/ai-data-center-liquid-cooling-infrastructure/
- 12–18 month retrofit timeline as binding constraint: https://nextwavesinsight.com/ai-data-center-liquid-cooling-infrastructure/
- Combined hyperscaler capex 2025–2026: https://futurumgroup.com/insights/ai-capex-2026-the-690b-infrastructure-sprint/
