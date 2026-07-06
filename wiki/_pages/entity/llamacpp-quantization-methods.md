---
canonical_name: llama.cpp Quantization Methods
aliases:
- GGML quantization
- llama.cpp quantization types
- Q4_0
- Q4_1
- Q8_0
- K-quant
- GGML Quantization
- llama.cpp quantization
- GGML quantization techniques
- block-based quantization in llama.cpp
subtype: null
tags:
- quantization
- llama.cpp
- GGML
- LLM inference
- post-training quantization
scorecard:
  novelty_delta: 0.7
  claim_density: 0.6
  self_containedness: 0.8
  bridge_score: 0.2
  hub_potential: 0.5
sources:
- raw/cache/7ddb68c8b9c707cb.md
- https://jonathanding.github.io/llm-learning/en/articles/llama-cpp-quantization/
- raw/cache/65283fa9a554172c.md
- https://deepwiki.com/ggml-org/llama.cpp/7.3-quantization-techniques
source_url: https://jonathanding.github.io/llm-learning/en/articles/llama-cpp-quantization/
fetched_at: '2026-07-03T15:38:03.809314+00:00'
type: entity
created: '2026-07-03'
updated: '2026-07-06'
cold_start: true
inbound_links: 0
---

# llama.cpp Quantization Methods

llama.cpp quantization methods are post-training quantization techniques implemented in the llama.cpp library (built on the GGML tensor library) for reducing the precision of Large Language Model (LLM) weights. The quantization approach is block-based: tensors are divided into small chunks, and each block is assigned its own scale factor and optionally a minimum value to minimize precision loss. These methods include per-block symmetric quantization variants Q8_0 (8-bit), Q4_0 (4-bit symmetric), Q4_1 (4-bit with zero-point offset), and the later K-quant mixed-precision scheme (Q2_K through Q6_K). The system also supports importance quantization (IQ) formats, enabling compression down to 2-bit and even ternary representations. The core motivation is to enable local inference of large models (e.g., Llama 3.1 8B) on consumer hardware by reducing memory footprint and bandwidth pressure, trading off precision for speed and memory efficiency. Unlike calibration-based methods such as GPTQ and AWQ, llama.cpp's approach requires no model retraining or calibration data, using only numerical conversion and encoding of weights. The key design principles are per-block quantization (block size 32 for basic types, 256 for K-quant super-blocks) and mixed-precision allocation across layers, where higher bit-widths are used for sensitive parts like Attention projections and lower bit-widths for more robust FFN layers.

## Key Claims

- Compression ratio of 3.56x for Q4_0: 32 FP16 values (64 bytes) are packed into 32 INT4 values (16 bytes) plus one FP16 scale (2 bytes), totaling 18 bytes.
- Quantization errors for Q4_0 are typically in the range 0.01–0.1, with a perplexity increase of less than 0.2 for an 8B parameter model.
- Q4_1 adds a per-block FP16 min value as a zero-point offset to support asymmetric weight distributions, but in practice Transformer weight distributions are close to symmetric, so the improvement is limited.
- K-quant introduces super-block structure (256 weight values per super-block) and hierarchical encoding with mixed precision: high-precision portions use 6-bit quantization, low-precision portions use 4-bit or even 3-bit.
- K-quant allocates higher bit-widths to Attention Q/K/V projections (more sensitive) and lower bit-widths to FFN Gate/Up/Down projections (more robust).
- The design is sensitivity-aware mixed-precision based on the observation that Attention mechanisms are highly sensitive to weight perturbation while FFN activation functions (SwiGLU/GELU) have a smoothing effect.
- llama.cpp quantization does not require calibration data, unlike GPTQ and AWQ.
- The quantization system supports a spectrum of formats from Q8_0 down to 2-bit and ternary representations via importance quantization, providing a range of compression levels and accuracy trade-offs.

## Relationships

- [[auto-gemm-micro-kernel-c906-c910-benchmark]]: Both pages are part of the llama.cpp inference ecosystem; quantization reduces model weight precision to enable efficient LLM inference on the same RISC-V cores (C906, C910) that the auto-generated GEMM micro-kernels target.

## Sources

- https://jonathanding.github.io/llm-learning/en/articles/llama-cpp-quantization/
- https://deepwiki.com/ggml-org/llama.cpp/7.3-quantization-techniques
