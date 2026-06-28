---
cold_start: true
created: '2026-07-14'
inbound_links: 0
scorecard:
  bridge_score: 0.7
  claim_density: 0.6
  hub_potential: 0.6
  novelty_delta: 0.9
  self_containedness: 0.8
sources:
- https://joursbleu.github.io/llm-perf-model/
tags:
- LLM inference
- roofline model
- prefill
- decode
- performance estimation
type: entity
updated: '2026-06-28'
---

# LLM Performance Model — Prefill & Decode Estimator

The LLM Performance Model — Prefill & Decode Estimator is a Roofline-based analytical tool that estimates key inference performance metrics for large language models (LLMs) on various GPU hardware. It distinguishes between the prefill phase (processing the input prompt in one forward pass, which is compute-bound) and the decode phase (generating tokens one by one, which is memory-bandwidth-bound). The model accounts for quantization formats (FP16/BF16, INT8/FP8, INT4/GPTQ/AWQ, 3-bit, 2-bit), KV cache precision, device utilization percentages (FLOPS, memory, network BW), and runtime parameters such as prompt length, output length, batch size, and tensor parallelism. It also incorporates FlashAttention and IO-aware tiling optimizations. The output includes prefill latency, time to first token (TTFT), decode speed, total time, and memory breakdown for weights, KV cache, and activations.

## Key Claims

- Prefill latency is compute-bound and approximated by (Linear FLOPs + Attn FLOPs) / (Effective TFLOPS × 10¹²).
- Decode throughput is memory-bandwidth-bound, limited by model size in bytes divided by effective memory bandwidth.
- FlashAttention reduces O(N²) HBM traffic by keeping attention scores in SRAM, otherwise utilization drops to ~40%.
- KV cache size = 2 × layers × kv_heads × head_dim × seq_len × bytes per element; GQA/MLA significantly reduces KV cache.
- Arithmetic intensity (FLOPs/Byte) determines compute-bound vs memory-bound: prefill has high AI (~sequence length), decode has low AI (~1).
- Prefill is compute-intensive (FLOPs ≈ 2 × Params × SeqLen + Attention O(n²); for MoE only active parameters).
- Decode time per token = Model Size (bytes) / (Memory BW × TP × BW Utilization).

## Relationships

- [[RVV_Autovectorization_Optimization_Insights]] – An optimization recipe for RISC-V Vector Extension that demonstrates measurement-driven methodology; the LLM performance model could be applied to RISC-V hardware when LLM inference is targeted.

Insufficient context for additional cross-links: only one relevant page exists in the current wiki context.

## Sources

- [LLM Performance Model — Prefill & Decode Estimator](https://joursbleu.github.io/llm-perf-model/)
