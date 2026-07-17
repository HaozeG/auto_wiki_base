---
canonical_name: Pioneering Chiplet Technology and Design for the AMD EPYC and Ryzen
  Processor Families
aliases:
- AMD Chiplet Paper
- Naffziger2021
subtype: null
tags: []
scorecard:
  novelty_delta: 0.6
  claim_density: 0.3
  self_containedness: 0.7
  bridge_score: 0.4
  hub_potential: 0.2
sources:
- raw/cache/1b9fa7b56cd89669.md
- https://www.semanticscholar.org/paper/Pioneering-Chiplet-Technology-and-Design-for-the-:-Naffziger-Beck/32f196e26d13dfe90f482b7ffd3ae2f812de08ca
source_url: https://www.semanticscholar.org/paper/Pioneering-Chiplet-Technology-and-Design-for-the-:-Naffziger-Beck/32f196e26d13dfe90f482b7ffd3ae2f812de08ca
fetched_at: '2026-07-17T10:30:34.101784+00:00'
type: source_note
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 0
---

# Pioneering Chiplet Technology and Design for the AMD EPYC and Ryzen Processor Families

This industrial product paper, presented at the 48th Annual International Symposium on Computer Architecture (ISCA) in 2021, details the technology challenges, technical solutions, and design methodology that enabled AMD to deploy chiplet-based integration across its EPYC server and Ryzen consumer processor families. The authors, including Samuel Naffziger, describe how Moore's Law scaling motivated a shift from monolithic dies to multiple smaller chiplets interconnected via advanced packaging, and how this approach was extended from individual processors to multiple product families. The paper covers the 4th generation AMD EPYC server processor family based on the "Zen 4" core, which leverages chiplet architecture to optimize processors for specific data center and cloud market segments.

## Key Claims

- AMD pioneered chiplet technology for high-volume CPU products, addressing cost and yield challenges of large monolithic dies.
- The paper describes systematic technical solutions for chiplet interconnect, power delivery, and thermal management across AMD EPYC and Ryzen families.
- The 4th gen EPYC family uses the Zen 4 core with an advanced chiplet architecture tailored to data center and cloud workloads.
- Chiplet technology was expanded from individual processors to cover multiple product families, demonstrating scalability.

## Relationships

- Describes chiplet technology for AMD EPYC and Ryzen CPUs, which shares a multi-chip module packaging strategy with the [[amd_cdna]] GPU architecture, though targeted at CPU rather than GPU workloads.

## Sources

- [[PDF] Pioneering Chiplet Technology and Design for the AMD EPYC...](raw/cache/1b9fa7b56cd89669.md)
