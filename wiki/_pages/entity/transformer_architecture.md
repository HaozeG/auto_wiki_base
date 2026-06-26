---
type: entity
tags: [ml-architecture, attention, deep-learning, nlp]
sources:
  - "Vaswani et al. (2017). Attention Is All You Need. NeurIPS. https://arxiv.org/abs/1706.03762"
  - "Brown et al. (2020). Language Models are Few-Shot Learners (GPT-3). https://arxiv.org/abs/2005.14165"
  - "Touvron et al. (2023). Llama 2. https://arxiv.org/abs/2307.09288"
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

# Transformer Architecture

The Transformer is a neural network architecture introduced by Vaswani et al. in "Attention Is All You Need" (NeurIPS 2017) that replaced recurrent layers with a mechanism called self-attention, enabling fully parallel processing of token sequences. Unlike RNNs, which process tokens sequentially and struggle to capture long-range dependencies, the Transformer computes pairwise relationships between all tokens simultaneously. The core operation—scaled dot-product attention—takes queries (Q), keys (K), and values (V) as inputs and produces outputs via softmax(QKᵀ/√d_k)V. This pairwise computation scales quadratically in both time and memory with sequence length n, i.e., O(n²) complexity, which becomes the dominant bottleneck for long-context inference. Multi-head attention runs h independent attention heads in parallel, each projecting into a lower-dimensional subspace, then concatenates and projects the results; the original paper used h=8 heads. Two architectural variants dominate: encoder-decoder models (used in the original paper for translation, e.g., T5) and decoder-only models (used in GPT-series and LLaMA for autoregressive generation). Feed-forward sublayers (two linear projections with a nonlinearity, typically applied position-wise) account for roughly two-thirds of parameter count in large models. Positional encodings—either sinusoidal (original) or learned rotary embeddings (RoPE, used in LLaMA)—inject sequence-order information absent from attention's permutation-invariant computation.

## Key Claims

- The original Transformer (Vaswani et al. 2017) used 6 encoder and 6 decoder layers, 8-head attention, model dimension d_model=512, and ~65M parameters for the base model.
- GPT-3 (Brown et al. 2020) scales the decoder-only design to 175 billion parameters across 96 layers, 96 attention heads, and d_model=12288, trained on ~300 billion tokens.
- LLaMA-2 70B (Touvron et al. 2023) uses grouped-query attention (GQA) with 8 KV heads vs. 64 query heads, reducing KV cache memory by 8× relative to multi-head attention at the same model size.
- GPT-4 is estimated at approximately 1.8 trillion parameters in a mixture-of-experts configuration, though OpenAI has not officially confirmed parameter counts.
- Self-attention's O(n²) memory cost means a sequence of 32,768 tokens requires ~4 GB of attention matrix storage in FP16 for a single layer, before KV caching.
- Feed-forward layers in a standard Transformer use a hidden dimension 4× the model dimension (e.g., 4×12288=49152 for GPT-3), making them the majority of per-layer parameter count.
- Rotary positional embedding (RoPE), introduced by Su et al. (2021) and adopted by LLaMA, encodes position as a rotation in query/key space, enabling better length generalization than learned absolute embeddings.

## Relationships

- [[flash_attention]] — IO-aware algorithm that reduces the memory and runtime cost of the O(n²) self-attention computation.
- [[nvidia_hopper_h100]] — H100 Tensor Cores and HBM3 bandwidth are specifically sized to accelerate Transformer matrix multiplications; H100 SXM5 delivers 989 TFLOPS BF16.
- [[nvidia_blackwell_b200]] — Blackwell FP4 Tensor Cores and 5th-generation NVLink target the large matrix multiplications in Transformer feed-forward and attention layers.
- [[int8_fp8_quantization_llm_inference]] — Quantization techniques applied to Transformer weight matrices and activations to reduce memory and increase throughput.
- [[hbm_high_bandwidth_memory]] — KV cache for long-context Transformer inference is the primary consumer of HBM capacity on modern AI accelerators.

## Sources

- Vaswani, A. et al. (2017). "Attention Is All You Need." NeurIPS 2017. https://arxiv.org/abs/1706.03762
- Brown, T. et al. (2020). "Language Models are Few-Shot Learners." NeurIPS 2020. https://arxiv.org/abs/2005.14165
- Touvron, H. et al. (2023). "Llama 2: Open Foundation and Fine-Tuned Chat Models." https://arxiv.org/abs/2307.09288
- Su, J. et al. (2021). "RoFormer: Enhanced Transformer with Rotary Position Embedding." https://arxiv.org/abs/2104.09864
