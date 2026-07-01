---
canonical_name: XuanTie C950
aliases:
- C950
- T-Head XuanTie C950
- XuanTie C950 CPU
subtype: null
tags:
- risc-v
- alibaba
hardware_targets:
- XuanTie C950
toolchains: []
constraints:
- RISC-V
- 5nm process
scorecard:
  novelty_delta: 0.9
  claim_density: 0.85
  self_containedness: 0.9
  bridge_score: 0.7
  hub_potential: 0.8
sources:
- raw/cache/dcc45dab08ba2e7b.md
- https://www.trendforce.com/news/2026/03/25/news-alibaba-unveils-risc-v-xuantie-c950-cpu-for-ai-agents-5nm-chip-reportedly-made-by-tsmc/
source_url: https://www.trendforce.com/news/2026/03/25/news-alibaba-unveils-risc-v-xuantie-c950-cpu-for-ai-agents-5nm-chip-reportedly-made-by-tsmc/
fetched_at: '2026-07-01T04:27:57.215503+00:00'
type: hardware_target
created: '2026-07-01'
updated: '2026-07-01'
cold_start: true
inbound_links: 0
needs_summary_revision: false
---

# XuanTie C950

The XuanTie C950 is a RISC-V CPU developed by Alibaba's T-Head Semiconductor, unveiled in March 2026 and designed for AI agent applications. It is fabricated on a 5nm process, reportedly by TSMC, and integrates a self-developed AI acceleration engine that natively supports large-scale models with hundreds of billions of parameters such as Qwen3 and DeepSeek V3. The C950 features an 8-instruction decode, a 16-stage pipeline, and an out-of-order window exceeding 1,000 instructions, achieving a maximum clock speed of 3.2 GHz. In single-core SPECint2006 benchmark, it surpasses a score of 70, positioning it against mainstream server-grade products. The chip is based on the open RISC-V architecture, offering flexibility for customization in inference patterns, and is part of Alibaba's push into high-end computing and supply chain resilience.

## Key Claims

- Verified on a 5nm process (manufacturing partner not disclosed but reported as TSMC).
- Uses the RISC-V open-source architecture.
- Integrates a self-developed AI acceleration engine.
- Natively supports large-scale models (Qwen3, DeepSeek V3) with hundreds of billions of parameters.
- 8-instruction decode, 16-stage pipeline, out-of-order window exceeding 1,000 instructions.
- Maximum clock speed of 3.2 GHz.
- Single-core SPECint2006 score surpasses 70.
- Delivers more than 30% performance gain over some mainstream products for targeted use cases (per Alibaba DAMO Academy).
- T-Head has shipped 470,000 chips as of February 2026 with annualized revenue exceeding RMB 10 billion.
- IPO of T-Head remains possible according to CEO comments.

## Optimization-Relevant Details

- ISA/profile: RISC-V (open-source architecture)
- Vector/matrix/accelerator support: Integrated AI acceleration engine; no specific vector extension details disclosed.
- Memory/cache/TLB/DMA: Not disclosed.
- Compiler/toolchain support: Not specified in source.

## Relationships

- Related hardware target: [[xuantie_c908]]
- Related coprocessor design from Alibaba DAMO Academy: [[rvme]]

## Sources

- https://www.trendforce.com/news/2026/03/25/news-alibaba-unveils-risc-v-xuantie-c950-cpu-for-ai-agents-5nm-chip-reportedly-made-by-tsmc/
