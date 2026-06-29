---
cold_start: true
created: YYYY-MM-DD
inbound_links: 0
scorecard:
  bridge_score: 0.3
  claim_density: 0.6
  hub_potential: 0.3
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://unsloth.ai/docs/models/qwen3.6
tags:
- LLM
- Qwen
- Alibaba
- multimodal
- hybrid-thinking
type: entity
updated: '2026-06-29'
---

# Qwen3.6

Qwen3.6 is a large language model series developed by Alibaba, including the 27B dense model and the 35B-A3B mixture-of-experts model. It features multimodal hybrid-thinking capabilities, supporting vision, agentic coding, and chat tasks with a 256K context window across 201 languages. The 27B model runs on 18GB RAM setups, while the 35B-A3B requires 22GB RAM. Unsloth reports benchmark results showing Qwen3.6 27B MTP achieving 160 tokens/s and Qwen3.6 35B-A3B achieving 240 tokens/s on an RTX 6000 GPU using GGUF quantizations. The models can be run locally via Unsloth Studio or llama.cpp, and they are described as the strongest mid-sized LLMs on nearly all benchmarks.

## Key Claims

- Qwen3.6 is a family of multimodal hybrid-thinking models by Alibaba, with 27B dense and 35B-A3B MoE variants.
- Supports 256K token context window across 201 languages.
- Excels in agentic coding, vision, and chat tasks.
- Qwen3.6 27B requires 18GB RAM; Qwen3.6 35B-A3B requires 22GB RAM.
- Qwen3.6 27B MTP achieves 160 tokens/s generation speed on an RTX 6000 GPU.
- Qwen3.6 35B-A3B achieves 240 tokens/s generation speed on an RTX 6000 GPU.
- Models can be run locally using Unsloth Studio or llama.cpp with GGUF quantizations.
- Considered the strongest mid-sized LLM on nearly all benchmarks.

## Relationships

- [[Sipeed_MAIX_series]] – Both are AI-related hardware/software platforms, though Sipeed MAIX series focuses on edge RISC-V AI, while Qwen3.6 is a cloud-scale LLM; insufficient context for additional cross-links.

## Sources

- [Unsloth Documentation: Qwen3.6 - How to Run Locally](https://unsloth.ai/docs/models/qwen3.6)

