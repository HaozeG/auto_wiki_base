---
type: entity
tags: [parallelism, distributed-training, inference, tensor-parallelism, pipeline-parallelism]
sources:
  - "Shoeybi et al., 2019 — Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism (arXiv:1909.08053)"
  - "Huang et al., 2019 — GPipe: Efficient Training of Giant Neural Networks using Pipeline Parallelism (arXiv:1811.06965)"
  - "Narayanan et al., 2021 — Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM (arXiv:2104.04473)"
  - "Rajbhandari et al., 2020 — ZeRO: Memory Optimizations Toward Training Trillion Parameter Models (arXiv:1910.02054)"
  - "Jacobs et al., 2023 — DeepSpeed Ulysses: System Optimizations for Enabling Training of Extreme Long Sequence Transformer Models (arXiv:2309.14509)"
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

# Model Parallelism

Model parallelism refers to a family of distributed computing strategies that partition a neural network model across multiple accelerators (GPUs or other hardware) to overcome per-device memory limits and to exploit aggregate compute bandwidth. As LLM parameter counts grew from billions to trillions, no single GPU could hold a full model in HBM, making model parallelism a prerequisite for both training and serving frontier systems. The three primary strategies are tensor parallelism (TP), pipeline parallelism (PP), and sequence parallelism (SP), each targeting a different axis of the computation. These are typically combined with data parallelism and with optimizer-level sharding (ZeRO) to form the 3D or 4D parallelism configurations used in large-scale clusters. For mixture-of-experts models, a fourth axis — expert parallelism — distributes expert FFN blocks across devices. Megatron-LM (NVIDIA, 2019/2021) pioneered the practical combination of tensor and pipeline parallelism for transformer training, demonstrating near-linear scaling to thousands of GPUs on A100 clusters with NVLink interconnects. Choosing the right parallelism strategy requires balancing communication overhead (all-reduce for TP, point-to-point for PP), memory savings, and hardware topology (NVLink bandwidth vs. InfiniBand latency).

## Key Claims

- **Tensor parallelism (Megatron-LM)** splits individual weight matrices column-wise and row-wise across devices: in a two-layer MLP, the first linear layer is column-partitioned (each GPU holds W/N columns) and the second is row-partitioned, requiring a single all-reduce per layer; with **8-way TP on NVLink**, Megatron-LM achieves ~76% of linear scaling (linear would be 8×) due to all-reduce communication cost.
- **Pipeline parallelism bubble fraction** with the naive GPipe schedule is (p−1)/m, where p is the number of pipeline stages and m is the number of microbatches; the **1F1B (one-forward-one-backward) schedule** used in PipeDream and Megatron-LM reduces the pipeline bubble to approximately **(p−1)/(m + p − 1)**, which converges to ~5% at m = 8, p = 4, making large p practical.
- **ZeRO optimizer** (DeepSpeed) has three stages: Stage 1 partitions optimizer states across data-parallel ranks (4× memory reduction per device), Stage 2 additionally partitions gradients (8× reduction), and Stage 3 partitions model parameters as well, enabling training of models with **>1 trillion parameters** on commodity GPU clusters at the cost of additional all-gather communication.
- **Sequence parallelism** (DeepSpeed Ulysses, 2023) distributes the sequence dimension across devices during self-attention computation, enabling context lengths up to **1 million tokens** on 64 A100 GPUs by partitioning the Q, K, V projections along the sequence axis and using all-to-all collectives instead of all-reduce.
- **Expert parallelism** for mixture-of-experts models routes each token's top-k expert activations across devices holding different expert FFN blocks; this requires an all-to-all dispatch and gather per MoE layer, adding latency proportional to expert count but keeping per-device memory constant as the number of experts grows.
- In the Megatron-LM paper (2021), a **3D parallelism** configuration of TP=8, PP=8, DP=512 trained a 1-trillion parameter model on 3072 A100 GPUs, achieving 163 TFLOPS per GPU (52% of peak A100 FP16 throughput of 312 TFLOPS).

## Relationships

- [[nvidia_hopper_h100]] — Tensor parallelism within a node requires high-bandwidth intra-node interconnects; the H100 SXM offers NVLink 4.0 with 900 GB/s bidirectional bandwidth per GPU, which is critical for sustaining efficient 8-way TP all-reduces.
- [[nvlink_nvswitch]] — NVSwitch fabric enables full all-to-all connectivity within a DGX node, enabling tensor and expert parallelism with near-uniform bandwidth; cross-node pipeline parallelism relies on InfiniBand or RoCE, which is 10–50× lower bandwidth.
- [[mixture_of_experts_moe_llm]] — Expert parallelism is the natural extension of model parallelism to MoE architectures; each expert resides on a different device, and the routing mechanism's all-to-all dispatch determines the load balance and communication overhead.
- [[transformer_architecture]] — Model parallelism is applied at the transformer layer level: TP splits attention heads and FFN weight matrices, PP assigns transformer layers to pipeline stages, and SP distributes the sequence dimension within attention.
- [[kv_cache_llm_inference]] — During inference with tensor parallelism, the KV cache is partitioned across TP ranks (each rank holds KV entries for its subset of attention heads), reducing per-device memory but requiring all-gather during multi-head attention output combination.

## Sources

- Shoeybi, M., et al. (2019). Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism. arXiv:1909.08053.
- Huang, Y., et al. (2019). GPipe: Efficient Training of Giant Neural Networks using Pipeline Parallelism. *NeurIPS 2019*. arXiv:1811.06965.
- Narayanan, D., et al. (2021). Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM. *SC 2021*. arXiv:2104.04473.
- Rajbhandari, S., et al. (2020). ZeRO: Memory Optimizations Toward Training Trillion Parameter Models. *SC 2020*. arXiv:1910.02054.
- Jacobs, S., et al. (2023). DeepSpeed Ulysses: System Optimizations for Enabling Training of Extreme Long Sequence Transformer Models. arXiv:2309.14509.
- Narayanan, D., et al. (2019). PipeDream: Generalized Pipeline Parallelism for DNN Training. *SOSP 2019*. arXiv:1806.03377.
