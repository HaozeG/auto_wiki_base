---
type: entity
tags: [inference, memory, attention, systems]
sources:
  - "Vaswani et al. 2017 — Attention Is All You Need"
  - "Kwon et al. 2023 — Efficient Memory Management for Large Language Model Serving with PagedAttention (SOSP 2023)"
  - "Ainslie et al. 2023 — GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints"
  - "Yu et al. 2022 — Orca: A Distributed Serving System for Transformer-Based Generative Models (OSDI 2022)"
  - "Touvron et al. 2023 — Llama 2: Open Foundation and Fine-Tuned Chat Models"
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

# KV Cache in LLM Inference

The KV cache is a memory structure that stores the key and value tensors computed by each transformer attention layer for all previously generated tokens, avoiding their recomputation on every new decoding step. During autoregressive generation, a transformer must attend over all prior context; without caching, each new token would require O(n²) attention operations as the sequence grows. With the KV cache, the cost per step is O(n·d·L) in memory — where n is the current sequence length, d is the per-head dimension, and L is the number of layers — and O(n) in compute per new token. At the scales typical of production LLMs, this memory cost dominates: a 70-billion-parameter model with 80 transformer layers, 64 attention heads, and head dimension 128 running at 16-bit precision accumulates roughly 0.5 MB of KV cache per token per batch entry; a batch of 512 sequences at 4096 tokens each requires ~1 TB of KV cache, far exceeding what any single GPU can hold. Hardware memory bandwidth rather than FLOPs becomes the primary throughput bottleneck during the decode phase because each decoding step reads the full KV cache from HBM with minimal compute reuse. Three techniques directly reduce this bottleneck: Multi-Query Attention (MQA) and Grouped Query Attention (GQA), which share key/value heads across multiple query heads; PagedAttention, which eliminates KV cache fragmentation through virtual memory paging; and continuous batching, which reclaims KV cache slots from completed sequences in real time.

## Key Claims

- KV cache memory scales as 2 × n_layers × seq_len × n_kv_heads × head_dim × bytes_per_element; for LLaMA-2 70B (80 layers, 8 KV heads via GQA, head_dim=128, FP16) this is approximately 0.32 MB per token per sequence, versus ~2.56 MB for the full 64-head MHA variant.
- GQA, introduced for LLaMA-2 70B and adopted in LLaMA-3, groups multiple query heads to share a single key/value head; LLaMA-2 70B uses 8 KV heads (GQA-8) instead of 64, reducing KV cache size by 8× with minimal quality degradation on standard benchmarks.
- PagedAttention (vLLM, SOSP 2023) partitions the KV cache into fixed-size blocks (pages) analogous to OS virtual memory, reducing memory waste from fragmentation and reservation by up to 55% compared to contiguous allocation, and enabling copy-on-write sharing for parallel sampling.
- Continuous batching (Orca, OSDI 2022) replaces static batching by inserting new requests into a running batch as soon as sequence slots free up, increasing GPU utilization from ~30–40% (static) to ~70–90% in throughput benchmarks.
- At decode time on an H100 SXM5 (3.35 TB/s HBM3e bandwidth), reading the KV cache for a 4096-token sequence across 80 layers takes ~400 µs independent of batch size; arithmetic intensity during decode is typically below 10 FLOP/byte, far below the H100's hardware ridge point of ~140 FLOP/byte.
- DeepSeek-V2's Multi-head Latent Attention (MLA) compresses the KV cache into a low-rank latent representation, reducing KV cache memory to approximately 5–13% of standard MHA at equivalent model scale, at the cost of additional projection operations during prefill.

## Relationships

- [[hbm_high_bandwidth_memory]] — KV cache reads from HBM dominate decode-phase latency; HBM bandwidth is the primary bottleneck, making bandwidth-per-FLOP the key metric for KV cache-bound inference.
- [[nvidia_hopper_h100]] — H100's 80 GB HBM3e capacity and 3.35 TB/s bandwidth set the practical ceiling on KV cache size per GPU; NVLink allows KV cache sharding across GPUs for long-context workloads.
- [[groq_lpu]] — Groq LPU eliminates KV cache DRAM reads by holding the cache in on-chip SRAM across the full sequence, at the cost of limited sequence length; this removes the bandwidth bottleneck entirely for supported context windows.
- [[sambanova_sn40l]] — SambaNova SN40L's 520 MB on-chip SRAM enables KV cache storage for short to medium sequences without HBM access, substantially reducing decode latency versus HBM-resident caches.
- [[mixture_of_experts_moe_llm]] — MoE architectures amplify KV cache pressure per active parameter, since the attention layers (which generate KV cache) remain dense while only feed-forward experts are sparse; DeepSeek-V2 addresses this with MLA compression.
- [[int8_fp8_quantization_llm_inference]] — KV cache quantization to INT8 or FP8 halves cache memory footprint; techniques like KVQuant (2024) demonstrate <1% quality degradation at INT4 KV compression for many models.

## Sources

- Vaswani, A. et al. (2017). "Attention Is All You Need." NeurIPS 2017. https://arxiv.org/abs/1706.03762
- Kwon, W. et al. (2023). "Efficient Memory Management for Large Language Model Serving with PagedAttention." SOSP 2023. https://arxiv.org/abs/2309.06180
- Ainslie, J. et al. (2023). "GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints." EMNLP 2023. https://arxiv.org/abs/2305.13245
- Yu, G. et al. (2022). "Orca: A Distributed Serving System for Transformer-Based Generative Models." OSDI 2022. https://www.usenix.org/conference/osdi22/presentation/yu
- Touvron, H. et al. (2023). "Llama 2: Open Foundation and Fine-Tuned Chat Models." https://arxiv.org/abs/2307.09288
- DeepSeek-AI (2024). "DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model." https://arxiv.org/abs/2405.04434
