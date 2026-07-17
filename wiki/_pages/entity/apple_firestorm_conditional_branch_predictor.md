---
canonical_name: Apple Firestorm Conditional Branch Predictor
aliases:
- Firestorm CBP
- Apple Firestorm branch predictor
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
inbound_links: 2
---

# Apple Firestorm Conditional Branch Predictor

The Apple Firestorm Conditional Branch Predictor (CBP) is the branch prediction unit used in Apple's high-performance Firestorm processor cores, which power chips such as the Apple M1 and A14 Bionic. It is a modern multi-level predictor that records path history and indexes multiple Pattern History Tables (PHTs) to predict the direction of conditional branches. Through a reverse engineering pipeline developed by researchers from Tsinghua University, the exact organization of the Firestorm CBP—including its path history register length, the address bits incorporated into the history, the associativity of each PHT, and the PC bits used in index and tag functions—was recovered for the first time. The study uncovered two previously undisclosed effects—the scatter effect and the annihilation effect—that degrade prediction accuracy under specific branch patterns. Leveraging the recovered model, optimizations were proposed that reduce MPKI by up to 14% and improve performance by up to 7% in representative applications.

## Key Claims

- The Firestorm CBP uses a path history register of measured length, with specific address bits mapped into the history.
- It employs a multi-PHT structure with recoverable associativity, index functions, and tag functions for each table.
- The scatter effect causes mispredictions when certain branch patterns interleave in the PHT indices.
- The annihilation effect causes mispredictions when conflicting branch history patterns cancel out useful history information.
- Optimizations based on the CBP model achieve up to 14% MPKI reduction and up to 7% performance improvement.
- The reverse engineering pipeline is more general than prior methods and does not assume a specific update function or index/tag structure.

## Relationships

- The [[qualcomm_oryon_conditional_branch_predictor]] was reverse-engineered using the same pipeline, enabling a direct structural comparison; both use path-history-indexed PHTs but differ in PHT associativity and tag function.

## Sources

- [[2411.13900] Dissecting Conditional Branch Predictors of Apple...](raw/cache/39d19dbbfefb6097.md)
