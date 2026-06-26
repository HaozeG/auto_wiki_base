---
type: entity
tags: [economics, TCO, inference, GPU, cost-analysis]
sources:
  - https://epoch.ai/data-insights/ai-datacenter-cost-breakdown
  - https://intuitionlabs.ai/articles/nvidia-ai-gpu-pricing-guide
  - https://introl.com/blog/cost-per-token-llm-inference-optimization
  - https://introl.com/blog/inference-unit-economics-true-cost-per-million-tokens-guide
  - https://newsletter.semianalysis.com/p/groq-inference-tokenomics-speed-but
  - https://markaicode.com/pricing/amazon-ec2-self-hosted-llm-inference-cost-analysis/
  - https://siliconanalysts.com/tools/frontier
created: 2026-06-26
updated: 2026-06-26
cold_start: false
inbound_links: 0
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# AI Hardware TCO (Total Cost of Ownership)

Total cost of ownership for AI hardware encompasses capital expenditure (CapEx) on accelerators, servers, and facility construction, plus operating expenditure (OpEx) on energy, cooling, networking, and staff over a multi-year deployment horizon. At the scale of a one-gigawatt AI data center, Epoch AI's 2025 analysis estimated approximately $38 billion in up-front CapEx — with servers alone accounting for roughly $5 billion per year, or 60% of ongoing cost — against only $0.9 billion per year in total OpEx. Energy, the largest single OpEx item, costs between $41 million and $131 million per year for a 100 MW facility depending on electricity prices ($0.047–$0.15/kWh). At the chip level, list prices have diverged significantly between vendors: NVIDIA H100 80GB SXM5 has ranged from $25,000 to $40,000 per unit since launch, while AMD MI300X carried a list price approximately 50–60% lower, estimated at $12,000–$20,000, exploiting its 192 GB HBM3 capacity advantage for large-model inference. Cloud rental prices for H100 averaged approximately $3.11 per GPU-hour in early 2026, down from peaks above $8/hr in mid-2023, with spot pricing as low as $1.25/hr; MI300X cloud median was approximately $2.72/hr. The cost-per-token metric has emerged as the canonical unit for comparing inference economics across hardware platforms and cloud providers.

## Key Claims

- A one-gigawatt AI data center requires approximately $38 billion in CapEx, with servers representing ~60% of ongoing annual cost at roughly $5 billion/year; energy OpEx is $0.6 billion/year at median US electricity prices.
- NVIDIA H100 list price is $25,000–$40,000 per GPU; AMD MI300X is priced at approximately $12,000, yielding a 2–3× price differential that is the primary driver of MI300X adoption for memory-bound large-model inference.
- NVIDIA H100 delivers inference at approximately $0.09 per million tokens for a 120B-parameter model using vLLM; NVIDIA B200 reduces this to approximately $0.02 per million tokens — roughly 4.5× cheaper — as of April 2026.
- AWS EC2 self-hosted inference (inf2 instances or GPU instances) delivers approximately $0.033 per million tokens for supported models, with inf2.xlarge offering 25–40% lower cost per inference than equivalent GPU instances for compiled models.
- Groq LPU pricing for Llama 4 Scout was $0.11 per million input tokens and $0.34 per million output tokens as of late 2025, competitive on cost while delivering substantially higher throughput than GPU providers due to its Language Processing Unit architecture.
- Cloud H100 rental rates fell 64–75% from 2023 peaks to approximately $3.11/GPU-hour average in early 2026, with spot pricing as low as $1.25/hr; MI300X cloud median is $2.72/hr (range: $1.99 on DigitalOcean to $7.86 on Microsoft Azure).
- NVIDIA H100 bill of materials is approximately $3,320; H200 ~$4,800; B200 ~$6,400; AMD MI300X ~$5,300 — indicating H100 list price represents a roughly 8–12× markup over manufacturing cost.
- The combined hyperscaler capex commitment for AI infrastructure (Microsoft, Google, Meta, Amazon) is approximately $725 billion in 2026, up 77% from $410 billion in 2025, suggesting AI gross margins remain high enough to justify aggressive reinvestment.

## Relationships

- [[nvidia_hopper_h100]] — H100 is the baseline for TCO benchmarks; $25K–$40K list price and $0.09/million-token inference cost define the reference point against which all other AI accelerators are evaluated.
- [[amd_mi300x]] — MI300X's ~$12K–$20K price and 192 GB HBM3 capacity position it as the cost-competitive alternative to H100, particularly for memory-bound inference of large models; cloud median rental $2.72/hr.
- [[nvidia_blackwell_b200]] — B200 reduces H100 inference cost by approximately 4.5× to ~$0.02 per million tokens; manufacturing cost ~$6,400 versus H100's ~$3,320, but delivers roughly double the compute density.
- [[aws_inferentia]] — AWS Inferentia2 (inf2 instances) delivers 25–40% lower cost per inference than equivalent GPUs for compiled/supported models, at approximately $0.033/million tokens for self-hosted LLM inference on EC2.
- [[ai_datacenter_power_and_cooling]] — Energy OpEx ($0.6B/year per GW at median US rates) and cooling infrastructure CapEx are the fastest-growing components of AI hardware TCO as rack densities increase.
- [[hbm_high_bandwidth_memory]] — HBM capacity (192 GB on MI300X vs 80 GB on H100) is a primary differentiator affecting which models can run without tensor-parallelism, directly influencing effective cost-per-token for large models.

## Sources

- Epoch AI one-gigawatt data center TCO breakdown: https://epoch.ai/data-insights/ai-datacenter-cost-breakdown
- H100 and B200 list pricing and cost-per-token analysis: https://intuitionlabs.ai/articles/nvidia-ai-gpu-pricing-guide
- H100 vs B200 inference cost ($0.09 vs $0.02/million tokens): https://introl.com/blog/cost-per-token-llm-inference-optimization
- Groq Llama 4 Scout pricing ($0.11 input / $0.34 output per million tokens): https://newsletter.semianalysis.com/p/groq-inference-tokenomics-speed-but
- AWS EC2 self-hosted inference $0.033/million tokens; inf2 cost advantage: https://markaicode.com/pricing/amazon-ec2-self-hosted-llm-inference-cost-analysis/
- H100/H200/B200/MI300X bill of materials; cloud rental price index: https://siliconanalysts.com/tools/frontier
- Cloud H100 average $3.11/hr early 2026; MI300X $2.72/hr median: https://aimultiple.com/gpu-index
- Combined hyperscaler capex 2025–2026 ($410B → $725B): https://futurumgroup.com/insights/ai-capex-2026-the-690b-infrastructure-sprint/
