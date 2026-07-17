---
canonical_name: Qualcomm Oryon Conditional Branch Predictor
aliases:
- Oryon CBP
- Qualcomm Oryon branch predictor
subtype: null
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 0.8
  bridge_score: 0.3
  hub_potential: 0.2
sources:
- raw/cache/39d19dbbfefb6097.md
- https://arxiv.org/abs/2411.13900
source_url: https://arxiv.org/abs/2411.13900
fetched_at: '2026-07-17T12:08:37.780727+00:00'
type: entity
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 1
---

# Qualcomm Oryon Conditional Branch Predictor

The Qualcomm Oryon Conditional Branch Predictor (CBP) is the branch prediction component used in Qualcomm's Oryon CPU cores, which are custom-designed high-performance cores for platforms like the Snapdragon X series. Like the Apple Firestorm CBP, Oryon's predictor is a multi-level design that incorporates path history and indexes Pattern History Tables (PHTs) to predict conditional branch directions. A reverse engineering study by researchers from Tsinghua University successfully recovered the Oryon CBP's detailed organization—including path history register length, address bit mapping, PHT associativity, and the PC and history bits used in index and tag functions. The study applied the same general pipeline to both microarchitectures and identified the scatter and annihilation effects as common deficiencies that degrade prediction accuracy across modern designs. Optimizations derived from the model yield up to 14% MPKI reduction and 7% performance improvement in representative workloads.

## Key Claims

- The Oryon CBP employs a path history register with a distinct length and address bit mapping compared to the Apple Firestorm CBP.
- Its PHT structure has measurable associativity and recoverable index/tag functions.
- The scatter and annihilation effects, also present in Apple Firestorm, impair Oryon's prediction accuracy.
- The same optimizations that mitigate these effects provide up to 14% MPKI reduction and up to 7% performance improvement.
- The reverse engineering methodology does not require vendor-specific assumptions and is applicable to other processors.

## Relationships

- The [[apple_firestorm_conditional_branch_predictor]] shares the same reverse engineering pipeline and general PHT-based design paradigm but differs in detailed parameters such as PHT associativity and tag function.

## Sources

- [[2411.13900] Dissecting Conditional Branch Predictors of Apple...](raw/cache/39d19dbbfefb6097.md)
