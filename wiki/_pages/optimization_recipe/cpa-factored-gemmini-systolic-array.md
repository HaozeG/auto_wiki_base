---
canonical_name: CPA-Factored Gemmini Systolic Array
aliases:
- Carry-Propagation-Adder Factored Gemmini
- CPA-factored systolic array
- Carry-Propagation-Adder-Factored Gemmini Systolic Array for Machine Learning Acceleration
subtype: null
tags: []
hardware_targets:
- Gemmini
datatypes: []
metrics:
- area
- delay
- power
toolchains: []
constraints: []
evidence_strength: reported
scorecard:
  novelty_delta: 0.8
  claim_density: 0.6
  self_containedness: 0.5
  bridge_score: 0.7
  hub_potential: 0.4
sources:
- raw/cache/2d5227f41cf769c0.md
- https://www.researchgate.net/publication/349991230_Carry-Propagation-Adder-Factored_Gemmini_Systolic_Array_for_Machine_Learning_Acceleration
source_url: https://www.researchgate.net/publication/349991230_Carry-Propagation-Adder-Factored_Gemmini_Systolic_Array_for_Machine_Learning_Acceleration
fetched_at: '2026-07-02T09:32:28.676226+00:00'
type: optimization_recipe
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 32
---

# CPA-Factored Gemmini Systolic Array

The carry-propagation-adder (CPA)-factored Gemmini systolic array is a microarchitectural optimization that extracts the carry propagation adder and rounding logic from each processing element (PE) of the Gemmini systolic array generator. This factoring reduces the critical path within each PE, enabling area and delay improvements without altering the functional behavior or the software interface. The technique is transparent to applications and requires no modifications to the Gemmini baseline design's output-stationary dataflow. Preliminary measurements from the original publication report area reductions of up to 45.3% and delay reductions of up to 23.7% compared to the unmodified Gemmini baseline.

## Key Claims

- CPA-factoring reduces PE area by up to 45.3% compared to the Gemmini baseline.
- CPA-factoring reduces PE delay by up to 23.7%.
- The factoring does not change the functionality or software interface of the systolic array.
- The technique is transparent to applications.
- The optimization is demonstrated on the open-source Gemmini systolic array generator.

## Transformation

- Prerequisites: A baseline Gemmini systolic array design configured with output-stationary dataflow and two accumulation registers per PE.
- Steps: Extract the carry propagation adder used for accumulation and the rounding logic from each processing element. Route the partial sums to a shared CPA block external to the PE array.
- Expected effect: Area reduction up to 45.3% and delay reduction up to 23.7% compared to baseline Gemmini. Reductions in power consumption are also implied by reduced area and delay.
- Failure modes: The paper asserts no functional change; however, increased routing complexity may affect timing closure in physical design. The technique remains functionally transparent.
- Measurements: Area reduction of 45.3% and delay reduction of 23.7% reported in the original research paper (source snippets). Evidence strength: reported.

## Relationships

- [[gemmini]]: The CPA-factored optimization is applied to the Gemmini systolic array generator.
- Insufficient context for additional cross-links; no existing entity pages for systolic array architectures or low-power design techniques are present in the wiki.

## Sources

- [Carry-Propagation-Adder-Factored Gemmini Systolic Array for Machine Learning Acceleration](https://www.researchgate.net/publication/349991230_Carry-Propagation-Adder-Factored_Gemmini_Systolic_Array_for_Machine_Learning_Acceleration)
