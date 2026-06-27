---
cold_start: false
created: '2026-06-26'
inbound_links: 0
scorecard:
  bridge_score: 0.7
  claim_density: 0.6
  hub_potential: 0.8
  novelty_delta: 0.9
  self_containedness: 0.8
sources:
- https://aiadda.online/blog/state-space-models-mamba
- Gu, A., Goel, K., & Ré, C. (2021). Efficiently Modeling Long Sequences with Structured
  State Spaces. ICLR 2022.
- 'Gu, A., & Dao, T. (2023). Mamba: Linear-Time Sequence Modeling with Selective State
  Spaces. arXiv:2312.00752.'
tags:
- state-space-models
- mamba
- s4
- selective-state-spaces
- sequence-modeling
type: entity
updated: '2026-06-26'
---

# State Space Models and Mamba

State space models (SSMs) are a class of sequence modeling architectures that originate from control theory and have been adapted for deep learning by the Structured State Space (S4) model introduced by Gu et al. (2021). SSMs represent a system's dynamics through hidden state variables that evolve over time according to a linear differential equation, updated recurrently at each time step. This allows them to process sequences in linear time with respect to sequence length, a significant advantage over the quadratic self-attention mechanism in Transformers. Mamba, proposed by Gu and Dao (2023), improves upon S4 by introducing a selective state space mechanism: the transition matrices A, B, and C become input-dependent, enabling the model to selectively remember or forget information based on context. Mamba also incorporates a hardware-efficient parallel scan algorithm that makes training as fast as Transformers while maintaining linear-time inference. These models have demonstrated strong performance on long-range sequence tasks including language modeling, DNA sequence analysis, and time-series forecasting, often matching or exceeding Transformer baselines while using less compute.

## Key Claims

- Structured State Space (S4) models achieve linear-time complexity (O(L)) for sequence length L, compared to the quadratic O(L²) of self-attention.
- Mamba's selective state space mechanism makes the transition matrices input-dependent, allowing the model to dynamically control information retention and forgetting.
- Mamba uses a hardware-efficient parallel scan (associative scan) to compute the state update efficiently on GPUs, enabling training speeds comparable to Transformer counterparts.
- On the Long Range Arena (LRA) benchmark, S4 achieves state-of-the-art average accuracy (85.7%) among non-Transformer models, and Mamba further improves on language modeling perplexity.
- Mamba scales effectively to large language models: a 2.8B-parameter Mamba model matches or exceeds the performance of similarly-sized Transformers (e.g., Pythia-2.8B) on downstream tasks while consuming 2x-3x less tokens during training.
- The selective SSM architecture in Mamba naturally handles length generalization: it can be trained on fixed-length sequences and applied to arbitrarily long sequences during inference.
- SSMs are well-suited for applications with long context requirements, including document classification, genome modeling, and continuous control tasks.
- The Mamba codebase is open-source and implemented in PyTorch, with CUDA kernels for the selective scan operation.

## Relationships

This page is a standalone seed; no other wiki pages currently reference this topic. Expected future connections include Transformer architecture, S4, linear attention, and long-range sequence benchmarks.

## Sources

- https://aiadda.online/blog/state-space-models-mamba
- Gu, A., Goel, K., & Ré, C. (2021). Efficiently Modeling Long Sequences with Structured State Spaces. ICLR 2022.
- Gu, A., & Dao, T. (2023). Mamba: Linear-Time Sequence Modeling with Selective State Spaces. arXiv:2312.00752.
