---
type: synthesis
connected_entities:
- blackhole-quietbox
- tt-quietbox-2
- blackhole
synthesis_status: draft
sources:
- https://www.theregister.com/on-prem/2025/11/27/blackhole-quietbox-tenstorrents-ai-workstation-reviewed/2113269
- https://wccftech.com/tenstorrent-tt-quietbox-2-risc-v-ai-workstation-128-gb-memory-liquid-cooling-9999-usd/
- https://docs.tenstorrent.com/tt-quietbox2-guide/
tags: []
created: '2026-07-09'
updated: '2026-07-09'
cold_start: true
inbound_links: 1
scorecard:
  bridge_score: 0.6
  contradiction_potential: 0.5
  cross_domain_connection: 0.4
needs_summary_revision: true
outbound_links:
- target: blackhole-quietbox
  reason: the earlier (Nov 2025) four-chip Blackhole workstation, EPYC-based
- target: tt-quietbox-2
  reason: the later (Mar 2026) four-chip Blackhole workstation, Ryzen-based, cheaper
- target: blackhole
  reason: the accelerator chip both workstations are built around
---

# Tenstorrent Workstation Lineup: Blackhole QuietBox vs. TT-QuietBox 2

## RAG Summary

Tenstorrent has shipped two four-chip, liquid-cooled desktop AI workstations built around its Blackhole accelerator: the Blackhole QuietBox and the TT-QuietBox 2, and the two pages describing them in this wiki reflect a real generational tradeoff rather than a duplicate listing. The Blackhole QuietBox, reviewed in November 2025, pairs four liquid-cooled Blackhole P150 accelerators with a server-class ASRock Rack EPYC board (AMD EPYC Siena 8124P, 16 Zen4C cores), 512 GB of DDR5-4800 across eight RDIMMs (~200 GB/s), and a large chimney-style dual-radiator cooling system, at a launch price of $11,999. The TT-QuietBox 2, announced March 2026, instead pairs four Blackhole chips (as two dual-chip p300c cards, 480 Tensix cores) with a consumer AMD Ryzen 7 9700X host, 256 GB of DDR5-5600, and ships pre-loaded with Qwen3-32B for out-of-the-box inference, at a lower $9,999. The consistent pattern across both — same chip count, same liquid-cooling approach, same open-source TT-Forge/TT-Metalium/TT-LLK software stack, falling price, and a shift from a server-grade to a consumer-grade host — reads as Tenstorrent moving the QuietBox line from a developer/lab dev-kit toward a cheaper out-of-the-box inference appliance. This reading is not fully confirmed: the evidence for "two generations" is a spec delta across two independent secondary-source articles, not an explicit Tenstorrent statement distinguishing "QuietBox 1" from "QuietBox 2" as named products.

---

## Full Synthesis

The Blackhole QuietBox (covered on [[blackhole-quietbox]]) and the TT-QuietBox 2 (covered on [[tt-quietbox-2]]) both describe a liquid-cooled workstation built around four [[blackhole]] accelerators, and on first pass they read as the same product captured from two different sources — that was in fact the initial working hypothesis for this pair of pages, flagged for merge during identity resolution. Closer comparison of the two source articles instead supports treating them as sequential products in the same product line:

| | Blackhole QuietBox | TT-QuietBox 2 |
|---|---|---|
| Source / date | The Register, Nov 2025 | wccftech / Tenstorrent docs, Mar 2026 |
| Price | $11,999 | $9,999 |
| Chip config | 4× Blackhole P150 | 4× Blackhole (2× p300c dual-chip cards) |
| Host CPU | AMD EPYC Siena 8124P (16 Zen4C, server board) | AMD Ryzen 7 9700X (8-core, consumer board) |
| System RAM | 512 GB DDR5-4800 | 256 GB DDR5-5600 |
| Cooling | Custom chimney case, 2× 400mm radiators, 4× 200mm fans, >1300 W dissipated | Liquid-cooled, 38 dBA max noise, ~1500 W peak draw |
| Positioning | "Development platform" for Blackhole, immature software stack noted | Pre-loaded models (Qwen3-32B), positioned for out-of-the-box inference |

The direction of every changed spec is consistent with a deliberate second-generation cost-down: halving system RAM, swapping a server CPU for a consumer one, and cutting price by ~$2,000, while keeping the chip count and liquid-cooling value proposition fixed. That consistency is the main evidence for treating these as genuinely distinct products rather than the same hardware misreported twice — a coincidental misreport would be more likely to produce contradictory rather than uniformly-directional deltas.

### Open Questions

- Is there a Tenstorrent-published name for the first-generation product (i.e., does "Blackhole QuietBox" without a version number correspond to an actual SKU, or is it informal naming used by the reviewing outlet)? Neither source page cites an official Tenstorrent product page for the first generation.
- If the two products are confirmed identical (e.g., the EPYC Siena configuration was a pre-release/reviewer unit later respecified before the "QuietBox 2" retail launch), `blackhole-quietbox.md` and `tt-quietbox-2.md` should be merged rather than kept as separate pages — this synthesis should be revisited if primary-source evidence resolves the question either way.
- Neither page has pricing/availability confirmation independent of the originating article; both are single-sourced.

## Connected Pages

- [[blackhole-quietbox]] — the earlier (Nov 2025) four-chip Blackhole workstation, EPYC-based.
- [[tt-quietbox-2]] — the later (Mar 2026) four-chip Blackhole workstation, Ryzen-based, cheaper.
- [[blackhole]] — the accelerator chip both workstations are built around.
