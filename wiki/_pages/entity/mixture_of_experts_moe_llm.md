---
type: entity
tags: [architecture, efficiency, sparse-activation, parallelism]
sources:
  - "Shazeer et al. 2017 — Outrageously Large Neural Networks (Sparsely-Gated MoE)"
  - "Lepikhin et al. 2021 — GShard: Scaling Giant Models with Conditional Computation"
  - "Fedus et al. 2022 — Switch Transformers: Scaling to Trillion Parameter Models"
  - "Jiang et al. 2024 — Mixtral of Experts (mistral.ai technical report)"
  - "DeepSeek-AI 2024 — DeepSeek-V2: A Strong, Economical, and Efficient MoE Language Model"
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

# Mixture of Experts (MoE) for LLM Inference

Mixture of Experts (MoE) is a neural network architecture that partitions the feed-forward layers of a transformer into N independent sub-networks called "experts," activating only a sparse subset k of them per input token at inference time. Because most parameters remain idle for any given token, MoE models can scale total parameter count far beyond what a dense model could afford at the same computational cost: active FLOPs scale with k/N rather than with the full parameter budget. The gating network — typically a learned linear projection followed by top-k selection — routes each token to its k experts independently. GShard (2021) applied this principle to machine translation at 600 billion parameters, Switch Transformer (2022) reduced k to 1 for simplicity and reached 1.6 trillion parameters while matching dense T5-XXL quality at one-seventh the FLOPs, and Mixtral 8×7B (2024) demonstrated that k=2-of-8 experts with 46.7 billion total parameters matches or exceeds LLaMA-2 70B on most benchmarks while activating only ~12.9 billion parameters per forward pass. DeepSeek-V2 (2024) pushed the design further with 236 billion total parameters, 21 billion active, and introduced Multi-head Latent Attention (MLA) to compress the KV cache alongside MoE routing. The key hardware tension is that sparse activation reduces compute but creates irregular all-to-all communication across devices, making expert parallelism — where different devices host different experts — the dominant deployment strategy and a major source of interconnect pressure.

## Key Claims

- Mixtral 8×7B has 46.7 billion total parameters but activates only ~12.9 billion per token (k=2 of 8 experts), yielding roughly 2× the throughput of a dense 13B model at comparable quality to LLaMA-2 70B.
- Switch Transformer demonstrated that k=1 (single-expert routing) is sufficient for training stability and reached 1.6 trillion parameters while requiring the FLOPs of a 137-billion-parameter dense model.
- DeepSeek-V2 uses 236 billion total parameters with 21 billion active per token; its MLA mechanism compresses the per-token KV cache to 5–13% of the size required by standard Multi-Head Attention.
- Expert parallelism requires all-to-all collective communication at every MoE layer; at high expert counts (e.g., 64+ experts across 8 nodes), this communication can consume 30–40% of total step time on commodity interconnects.
- Load imbalance — where popular experts receive far more tokens than rare ones — is addressed through auxiliary load-balancing losses (GShard, Switch) and capacity-factor clipping, which drops tokens routed to over-capacity experts.
- SambaNova's Cards on Experts (CoE) feature on the SN40L allows multiple fine-tuned expert models to reside in HBM simultaneously and be selected per-request, extending MoE routing semantics to the full-model level without weight swapping latency.

## Relationships

- [[sambanova_sn40l]] — SambaNova's Cards on Experts extends MoE routing to full-model granularity, with multiple expert models co-resident in on-chip SRAM and HBM.
- [[groq_lpu]] — Groq's deterministic streaming architecture eliminates all-to-all communication jitter but requires full weight replication per chip, making large MoE models expensive to deploy.
- [[nvidia_hopper_h100]] — H100 NVLink 900 GB/s bisection bandwidth reduces all-to-all overhead for expert parallelism; NVIDIA's Tensor Parallelism + Expert Parallelism (TP+EP) strategy is the reference deployment pattern for Mixtral on H100 clusters.
- [[hbm_high_bandwidth_memory]] — Each expert's weights must be loaded from HBM when activated; HBM bandwidth, not compute, is the bottleneck when batch sizes are small (inference, not training).
- [[int8_fp8_quantization_llm_inference]] — MoE expert weights are prime candidates for FP8/INT8 quantization because expert parameters are read infrequently; quantization reduces HBM footprint without disproportionate quality loss.

## Sources

- Shazeer, N. et al. (2017). "Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer." ICLR 2017. https://arxiv.org/abs/1701.06538
- Lepikhin, D. et al. (2021). "GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding." ICLR 2021. https://arxiv.org/abs/2006.16668
- Fedus, W. et al. (2022). "Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity." JMLR 2022. https://arxiv.org/abs/2101.03961
- Jiang, A. et al. (2024). "Mixtral of Experts." Mistral AI Technical Report. https://arxiv.org/abs/2401.04088
- DeepSeek-AI (2024). "DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model." https://arxiv.org/abs/2405.04434
