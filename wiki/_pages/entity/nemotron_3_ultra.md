---
canonical_name: NVIDIA Nemotron-3-Ultra
aliases:
- Nemotron-3-Ultra
- NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4
subtype: null
scorecard:
  novelty_delta: 0.9
  claim_density: 0.9
  self_containedness: 0.8
  bridge_score: 0.2
  hub_potential: 0.2
sources:
- raw/cache/3d5e8e048c49c940.md
- https://build.nvidia.com/explore/discover
source_url: https://build.nvidia.com/explore/discover
fetched_at: '2026-07-17T12:10:48.642963+00:00'
type: entity
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 0
---

# NVIDIA Nemotron-3-Ultra

**Nemotron-3-Ultra** is a frontier-scale large language model developed by NVIDIA, featuring a hybrid Latent Mixture-of-Experts (LatentMoE) architecture that interleaves Mamba-2, MoE, and attention layers. With 55 billion active parameters out of 550 billion total, it supports a context length of up to 1 million tokens and is optimized for complex reasoning, agentic workloads, long-context analysis, and multilingual tasks across English, French, Spanish, Italian, German, Japanese, Korean, Hindi, Brazilian Portuguese, and Chinese. The model incorporates Multi-Token Prediction (MTP) for faster generation and is trained using NVFP4 pre-training for compute efficiency. It is deployable on NVIDIA GPU configurations such as GB200, B200, and H100, and its reasoning mode can be toggled via a chat template.

## Key Claims

- Architecture: Hybrid LatentMoE with interleaved Mamba-2, MoE, and attention layers, plus Multi-Token Prediction.
- Parameters: 55B active, 550B total.
- Context length: up to 1M tokens.
- Supported languages: English, French, Spanish, Italian, German, Japanese, Korean, Hindi, Brazilian Portuguese, and Chinese.
- Minimum GPU requirement: 4xGB200, 4xB200, 4xGB300, 4xB300, 8xH100.
- Configurable reasoning mode via chat template (`enable_thinking=True/False`).
- Benchmark results (BF16): SWE-Bench Verified 71.9%, GPQA 87.0%, HLE 26.7%, IOI 2025 570.0.
- NVFP4 variant maintains close performance (e.g., SWE-Bench Verified 69.7%, GPQA 87.9%).
- Licensed under OpenMDW-1.1.

## Relationships

No specific relationship to visible context pages in the current wiki.

## Sources

- [Try NVIDIA NIM APIs](raw/cache/3d5e8e048c49c940.md)
