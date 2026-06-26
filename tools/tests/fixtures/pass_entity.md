---
type: entity
tags: [machine-learning, transformers]
sources: [raw/sources/attention_paper.md]
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

# Transformer Attention Mechanism

The transformer attention mechanism is a neural network building block that computes weighted relationships between all positions in a sequence simultaneously, enabling parallel processing and long-range dependency capture. Introduced in the 2017 paper "Attention Is All You Need" by Vaswani et al., it replaced recurrent layers as the dominant sequence modeling approach. The mechanism computes attention weights using query, key, and value matrices, with a scaling factor of 1/√d_k applied to stabilize gradients in high-dimensional spaces (typical d_k values range from 64 to 512). Its O(n²) memory complexity with respect to sequence length remains its primary limitation for very long sequences.

## Key Claims

- Attention weights are computed as softmax(QKᵀ/√d_k)V, where Q, K, V are learned linear projections of the input.
- Multi-head attention with h=8 heads was used in the original transformer, allowing the model to attend to different representation subspaces simultaneously.
- Transformer models replaced LSTM-based architectures in machine translation, achieving a BLEU score of 28.4 on WMT 2014 English-to-German, up from 26.4 for the previous best model.
- Self-attention enables O(1) path length between any two positions, whereas recurrent networks require O(n) sequential operations.
- The computational cost is O(n²·d) per layer, making it quadratic in sequence length n and linear in model dimension d.

## Relationships

- [[positional_encoding]]: Transformer attention is position-agnostic; positional encodings are added to provide sequence order information.
- [[bert]]: BERT uses bidirectional self-attention (encoder-only) pre-trained on masked language modeling.
- [[gpt]]: GPT uses causal (unidirectional) self-attention masked to prevent attending to future tokens.

## Sources

- Vaswani et al. (2017), "Attention Is All You Need" — cited in raw/sources/attention_paper.md for all Key Claims above.
