---
cold_start: true
created: '2025-03-25'
inbound_links: 0
scorecard:
  bridge_score: 0.3
  claim_density: 0.5
  hub_potential: 0.2
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B-Instruct-GGUF
tags:
- Qwen
- code model
- LLM
- GGUF
- llama.cpp
- Alibaba Cloud
type: entity
updated: '2026-06-29'
---

# Qwen2.5-Coder-1.5B-Instruct-GGUF

Qwen2.5-Coder-1.5B-Instruct-GGUF is a GGUF-quantized variant of the Qwen2.5-Coder-1.5B-Instruct model, a code-specific large language model developed by Alibaba Cloud. It is part of the Qwen2.5-Coder series, which includes six model sizes ranging from 0.5 to 32 billion parameters, designed to meet the needs of different developers. The GGUF format enables efficient inference on consumer hardware using llama.cpp, with installation via Homebrew on macOS and WinGet on Windows. This model builds upon the earlier CodeQwen1.5 with significant improvements in code generation, reasoning, and assistance capabilities. The series provides both base and instruct variants to suit various programming tasks.

## Key Claims

- The Qwen2.5-Coder series covers six parameter sizes: 0.5B, 1.5B, 3B, 7B, 14B, and 32B.
- This variant is packaged in the GGUF quantization format, optimized for use with llama.cpp.
- The series delivers significant improvements over CodeQwen1.5 in code generation and reasoning.
- For the 32B variant, a score of 73.7 was achieved on the Aider code repair benchmark, comparable to GPT-4o (source: resource snippet).
- The model can be run locally via llama-server or llama-cli commands after installing llama.cpp.

## Relationships

- [[Sipeed_MAIX_series]] – Both are AI-focused, but Sipeed targets RISC-V edge AI while Qwen is a cloud-scale LLM. Insufficient context for additional cross-links to entity pages.

## Sources

- [Qwen/Qwen2.5-Coder-1.5B-Instruct-GGUF on Hugging Face](https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B-Instruct-GGUF)

