---
cold_start: false
created: '2026-06-26'
inbound_links: 0
scorecard:
  bridge_score: 0.8
  claim_density: 0.8
  hub_potential: 0.7
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://aman.ai/primers/ai/state-space-models/
tags:
- state-space-models
- deep-learning
- sequence-modeling
type: entity
updated: '2026-06-26'
---

# State Space Models

State Space Models (SSMs) are a class of sequence modeling architectures inspired by classical control theory, which represent a system's dynamics through a set of first-order differential or difference equations linking an input signal to a latent state and then to an output. In the context of deep learning, SSMs have been adapted to process long sequences with linear-time complexity in the sequence length, offering a compelling alternative to the quadratic self-attention mechanism in Transformers. Modern deep SSMs, particularly the Structured State Space (S4) model and its successors like Mamba, achieve strong performance on benchmark tasks such as the Long Range Arena (LRA) and language modeling, while maintaining computational efficiency during both training and autoregressive inference. These models encode the recurrent dynamics using structured parameterizations—such as diagonal or low-rank plus diagonal state matrices—that enable fast convolution-based training and efficient recurrence-based inference. SSMs bridge the gap between recurrent neural networks (RNNs) and convolutional operations, and they have been extended to modalities beyond text, including vision and audio, through architectures like vision SSMs and diffusion backbones. The recent Mamba model introduces a selection mechanism that makes the state transition parameters input-dependent, enabling content-aware reasoning while preserving linear-time efficiency.

## Key Claims

- SSMs achieve O(L) time complexity in sequence length L during training (via convolution) and O(1) per step during autoregressive inference, compared to O(L²) for Transformers.
- The S4 model (Structured State Space) introduced a diagonal plus low-rank (DPLR) parameterization that enables efficient computation and achieves state-of-the-art results on the Long Range Arena benchmarks.
- Mamba (2023) introduces selective SSMs where the state transition matrices A, B, and C depend on the input, allowing the model to ignore irrelevant tokens and attend to relevant ones, solving a key limitation of prior SSMs.
- MambaByte extends the Mamba architecture to byte-level tokenization, achieving competitive perplexity on language modeling without a fixed vocabulary, demonstrating the flexibility of SSMs for token-free modeling.
- Hybrid architectures such as Jamba combine SSM layers with attention layers, exploiting the efficiency of SSMs for long contexts and the retrieval capability of attention for short-term dependencies.
- SSMs have been applied beyond language, including diffusion models for image generation (Scalable Diffusion Models with State Space Backbone) and multimodal models (Cobra), indicating broad applicability.

## Relationships

- Related concept: Transformers – SSMs are often compared to transformers as a more efficient alternative for long sequences.
- Related concept: Recurrent Neural Networks – SSMs share the recurrence structure but are trained with parallelizable convolutions.
- Related model: Mamba – a selective SSM that achieves linear-time reasoning and has been integrated into hybrid models like Jamba.
- Related model: S4 – the foundational structured state space model that introduced efficient computation through structured parameterization.

## Sources

- Aman's AI Journal: State Space Models Primer. https://aman.ai/primers/ai/state-space-models/
