---
type: entity
tags: [process-node, TSMC, semiconductor, FinFET, GAA, transistor-density]
sources:
  - https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_3nm
  - https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_2nm
  - https://www.anandtech.com/show/17047/tsmc-details-3nm-class-n3-and-n3e-risk-production-in-2022
  - https://semianalysis.com/2023/06/07/tsmc-cowos-supply-shortage/
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

# TSMC N3 and N2 Process Nodes

TSMC N3 (3 nm class) and N2 (2 nm class) are successive generations of TSMC's leading-edge logic fabrication processes, representing the final maturation of FinFET transistors and the industry's transition to Gate-All-Around (GAA) nanosheet devices. N3 entered risk production in 2022 and volume production in late 2022/early 2023, initially serving Apple's A17 Pro (iPhone 15 Pro) and subsequently NVIDIA, AMD, and Qualcomm AI and CPU designs. N2 is TSMC's first GAA production node, with risk production beginning in 2024 and volume production targeted for 2025, delivering an additional ~10–15% power reduction or performance uplift at iso-power versus N3E. Both nodes are central to the AI semiconductor supply chain: N3 hosts the compute dies inside NVIDIA's Blackwell B100/B200 GPU and Apple's M-series SoCs, while N2 is positioned for the next generation of AI accelerators from Apple, NVIDIA, and AMD.

## Key Claims

- **N3 transistor density**: TSMC N3 achieves approximately 167–171 million transistors per mm² on high-density (HD) cell libraries, representing roughly a 1.6× density improvement over N5 (96 MTr/mm²). The N3E variant (optimized for broader customer adoption) relaxes some design rules, yielding ~167 MTr/mm² with improved yield and wider library support.

- **N3 vs N5 power/performance**: TSMC quantified N3 as delivering ~18% speed improvement at the same power, or ~32–34% power reduction at the same speed, compared to N5. These numbers apply to TSMC's standard cell benchmarks (SPECint-class logic paths) and vary by design; real-world AI accelerator gains depend heavily on the ratio of compute to memory.

- **FinFET → GAA transition at N2**: N2 replaces the FinFET transistor (used continuously from N16 through N3) with a Nanosheet GAA (Gate-All-Around) architecture. In GAA nanosheets, the gate electrode wraps all four sides of a horizontally stacked set of silicon sheets, improving electrostatic control and allowing the sheet width to be tuned per cell for power/performance optimization — a capability FinFETs lack. TSMC targets ~10–15% power reduction or ~10–15% speed gain at iso-power for N2 versus N3E.

- **N2 transistor density projection**: TSMC has indicated N2 targets approximately 200+ million transistors per mm², though published figures cite ~175–190 MTr/mm² for high-density cells, depending on the cell height. This is a more modest density scaling than prior node transitions, reflecting that GAA's primary benefit at N2 is power/performance efficiency rather than raw density.

- **CoWoS capacity crisis 2023**: TSMC's CoWoS advanced packaging capacity became a critical bottleneck for AI chip supply in 2023. The H100 GPU required a CoWoS-S interposer of approximately 820 mm² — close to the maximum reticle-field-limited interposer size — and production volume was constrained by TSMC's limited CoWoS substrate capacity. Analysts estimated TSMC could produce only ~400,000–500,000 H100-equivalent CoWoS packages in 2023, far below demand from hyperscalers. TSMC announced CoWoS capacity expansion investments exceeding $2.9 billion for 2024–2025.

- **AI chip customers on N3**: Apple (A17 Pro, M3 family), NVIDIA (Ada Lovelace consumer chips, Hopper H100 at N4 then Blackwell B100 at N3), AMD (Ryzen 7000 CPUs at N5, MI300X at N5/N6), and Qualcomm (Snapdragon 8 Gen 3) all qualified designs on TSMC's 3 nm class nodes. NVIDIA's Blackwell architecture (B100/B200) moved the GPU compute die to TSMC N3, while the B100 NVLink switch tile remained on N4P.

- **N3E vs N3B differentiation**: TSMC offers two primary N3 sub-nodes — N3B (performance-optimized, used by Apple A17 Pro, fewer customers due to complex design rules) and N3E (broader design-rule set, higher yield, targeted at high-volume fabless customers). N3P and N3X are further variants adding ~3–5% performance at the same power via enhanced gate and contact processing.

## Relationships

- [[nvidia_hopper_h100]] — H100 compute die (GH100) is fabricated on TSMC N4 (a 5 nm class refinement); NVIDIA's subsequent Blackwell generation (B100/B200) moves to N3, directly depending on this node's yield ramp.
- [[amd_mi300x]] — MI300X uses a mix of TSMC N5 (GPU compute dies) and N6 (I/O die), with future AMD instinct generations targeting N3/N2 for compute dies.
- [[chiplet_architecture_advanced_packaging]] — CoWoS capacity constraints (discussed in that page) are inseparable from N3 ramp timelines; both nodes require TSMC advanced packaging co-investment.
- [[apple_neural_engine]] — Apple's Neural Engine in A17 Pro and M3 is the first consumer deployment of N3B silicon; ANE throughput scaled roughly 2× generation-over-generation partly due to density gains from N5→N3.
- [[google_tpu]] — Google Trillium TPU v6e is reported to use TSMC N4P or N3 class processes for the tensor core tile.

## Sources

- TSMC N3 technology brief: https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_3nm
- TSMC N2 technology overview: https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_2nm
- AnandTech N3/N3E analysis (2022): https://www.anandtech.com/show/17047/tsmc-details-3nm-class-n3-and-n3e-risk-production-in-2022
- SemiAnalysis CoWoS supply shortage report (June 2023): https://semianalysis.com/2023/06/07/tsmc-cowos-supply-shortage/
- IEEE ISSCC 2023 TSMC N3 device characterization papers
- TechInsights process teardown of Apple A17 Pro (N3B, 2023)
