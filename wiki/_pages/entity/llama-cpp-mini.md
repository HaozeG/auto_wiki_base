---
cold_start: true
created: YYYY-MM-DD
inbound_links: 1
scorecard:
  bridge_score: 0.5
  claim_density: 0.9
  hub_potential: 0.4
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://github.com/yiquanlin212/llama-cpp-mini
tags:
- LLM
- inference
- GGUF
- Apple_Silicon
- C++
type: entity
updated: '2026-06-28'
------


# llama-cpp-mini

llama-cpp-mini is a from-scratch C++20 inference engine designed to load GGUF weights and run a decoder-only transformer for Llama-3.2-1B-Instruct models on Apple Silicon. The engine implements the full inference pipeline including GGUF metadata parsing, dequantization, grouped-query attention (GQA) with rotary position embeddings (RoPE), a key-value (KV) cache, SwiGLU activation, RMSNorm, and byte-level BPE tokenization. It is open-source and available on GitHub. The project provides a compact implementation that prioritizes clarity and educational value, with a float32 row-major tensor container and a straightforward forward pass. Performance measurements on an Apple M4 chip with the Q4_K_M quantized model show a prefill speed of 4.51 tok/s and a decode speed of 11.50 tok/s, with a model load time of 1056 ms.

## Key Claims

- Implements full Llama inference in C++20: GGUF loader, transformer forward pass, and byte-level BPE tokenizer.
- Supports Q4_K, Q6_K, and Q8_0 quantization formats.
- Measured load time of the 770MB model file on Apple M4: 1056 ms.
- Measured prefill speed: 4.51 tok/s.
- Measured decode speed: 11.50 tok/s.
- Single-threaded, no batching, no speculative decoding (limitations acknowledged).
- Architecture includes RMSNorm, GQA + RoPE, SwiGLU MLP, and KV cache.

## Relationships

- [[Sipeed_MAIX_series]] – Both are AI acceleration platforms, though targeting different hardware architectures (RISC-V vs. Apple Silicon).
- [[Chiplet_RISC_V_AI_SoC_Architecture]] – Represents an alternative approach to AI inference with chiplet-based RISC-V design, contrasting with the monolithic software approach of llama-cpp-mini.

## Sources

- [GitHub repository: yiquanlin212/llama-cpp-mini](https://github.com/yiquanlin212/llama-cpp-mini)

