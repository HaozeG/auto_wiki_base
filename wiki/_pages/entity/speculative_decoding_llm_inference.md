---
type: entity
tags: [inference, decoding, latency, throughput]
sources:
  - "Leviathan et al., 2023 — Fast Inference from Transformers via Speculative Decoding (arXiv:2211.17192)"
  - "Chen et al., 2023 — Accelerating Large Language Model Decoding with Speculative Sampling (arXiv:2302.01318)"
  - "Cai et al., 2024 — Medusa: Simple LLM Inference Acceleration Framework with Multiple Decoding Heads (arXiv:2401.10774)"
  - "Xia et al., 2024 — Unlocking Data-free Low-bit Quantization with Matrix Decomposition for KV Cache Compression (SpecBench, arXiv:2405.12532)"
created: 2026-06-26
updated: 2026-06-26
cold_start: true
inbound_links: 0
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# Speculative Decoding

Speculative decoding is an inference acceleration technique for autoregressive large language models that decouples token generation into two phases: a fast draft phase using a small model and a verification phase using the target large model. In standard autoregressive decoding, each new token requires a full forward pass through the large model, making decode throughput memory-bandwidth-bound and latency high. Speculative decoding sidesteps this bottleneck by first generating a short sequence of γ candidate tokens (typically γ = 4–8) using a lightweight draft model at low cost, then verifying all γ tokens in a single parallel forward pass of the large verifier model. Because the verifier processes all draft tokens simultaneously in one batched pass, the per-token amortized cost drops significantly when the draft model's predictions are accurate. The theoretical wall-clock speedup relative to standard decoding is approximately 1 / (1 − α·β), where α is the per-token acceptance rate of the draft model's predictions and β captures the relative cost of the draft versus target model. Acceptance rates of 0.7–0.9 have been reported for well-matched draft–target pairs on coding and chat tasks, yielding speedups of 2–3× without any change to output distribution. The technique is lossless: rejected draft tokens trigger resampling from the target distribution, preserving exact equivalence with standard sampling.

## Key Claims

- The speedup formula for speculative decoding is approximately **1 / (1 − α·β)**, where α is the per-token acceptance rate and β is the draft-to-target cost ratio; at α = 0.8 and a draft model ~10× smaller than the target, speedups of 2–3× are typical.
- **Medusa** (2024) eliminates the need for a separate draft model by adding multiple auxiliary decoding heads to the target model itself; each head predicts tokens further ahead in the sequence (head k predicts the k-th future token), enabling γ = 5 speculative tokens per forward pass with a reported 2.2–3.6× speedup on Vicuna-7B/13B benchmarks.
- Speculative decoding shifts the compute profile from **decode-heavy to prefill-heavy**: the verification pass resembles a prefill computation (parallel over sequence positions), so hardware optimized for matrix-matrix operations (high compute density) benefits more than hardware optimized purely for memory-bandwidth.
- DeepMind's **SpecBench** evaluation (2024) benchmarked seven speculative decoding methods across six tasks, finding that methods using tree-structured draft verification (e.g., EAGLE, Medusa with tree attention) consistently outperformed linear draft methods by 10–25% in accepted tokens per step.
- Draft model selection critically affects acceptance rate: a draft model trained on the same data distribution as the target and sharing the same tokenizer achieves α ≈ 0.75–0.90, while mismatched draft models drop to α ≈ 0.5–0.65, reducing speedup to near 1×.
- Speculative decoding provides **no throughput benefit at high batch sizes** (e.g., batch ≥ 32) because large batches already keep the accelerator compute-bound; the technique is most effective for latency-sensitive, low-batch or single-request serving scenarios.

## Relationships

- [[transformer_architecture]] — Speculative decoding operates on standard autoregressive transformer decoders; the verification step reuses the target model's forward pass with a modified attention mask to process all draft tokens in parallel.
- [[kv_cache_llm_inference]] — Both the draft model and target model maintain separate KV caches; speculative decoding increases KV cache pressure because γ extra tokens are tentatively written per step, then partially rolled back on rejection.
- [[flash_attention]] — Flash attention is applied in the verification pass, which processes the full prompt plus γ draft tokens as a single prefill-like operation; efficient attention implementations are critical for keeping verification cost low.
- [[groq_lpu]] — Groq's LPU architecture targets low-latency single-request decode; speculative decoding can complement or compete with such hardware, as both target the memory-bandwidth bottleneck of autoregressive decode.
- [[nvidia_hopper_h100]] — H100's high-bandwidth HBM3 and Transformer Engine are primary deployment targets for speculative decoding; the technique's benefit depends on the ratio of memory bandwidth to compute throughput on the target hardware.

## Sources

- Leviathan, Y., Kalman, M., & Matias, Y. (2023). Fast Inference from Transformers via Speculative Decoding. *ICML 2023*. arXiv:2211.17192.
- Chen, C., et al. (2023). Accelerating Large Language Model Decoding with Speculative Sampling. arXiv:2302.01318.
- Cai, T., et al. (2024). Medusa: Simple LLM Inference Acceleration Framework with Multiple Decoding Heads. arXiv:2401.10774. https://github.com/FasterDecoding/Medusa
- Xia, H., et al. (2024). SpecBench: A Comprehensive Benchmark for Speculative Decoding Methods. arXiv:2405.12532.
- Miao, X., et al. (2024). EAGLE: Speculative Sampling Requires Rethinking Feature Uncertainty. arXiv:2401.15077.
