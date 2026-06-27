---
cold_start: false
created: '2025-08-07'
inbound_links: 0
scorecard:
  bridge_score: 0.1
  claim_density: 0.9
  hub_potential: 0.8
  novelty_delta: 0.8
  self_containedness: 0.9
sources:
- https://www.meta-intelligence.tech/en/insight-lora-finetuning
tags:
- LoRA
- QLoRA
- DoRA
- fine-tuning
- PEFT
- quantization
type: entity
updated: '2025-08-07'
---

# LoRA & QLoRA Fine-Tuning

LoRA (Low-Rank Adaptation) is a parameter-efficient fine-tuning (PEFT) technique that drastically reduces the number of trainable parameters required to adapt large language models (LLMs) to specific tasks. Instead of updating all model weights during fine-tuning, LoRA freezes the pre-trained weights and injects trainable low-rank decomposition matrices into attention layers. This approach reduces the memory and computational footprint, enabling fine-tuning of models with billions of parameters on a single consumer GPU. QLoRA extends LoRA by applying 4-bit NormalFloat4 (NF4) quantization to the base model, further reducing memory requirements—a 7B parameter model can be fine-tuned with only 6-8 GB of VRAM. DoRA (Weight-Decomposed Low-Rank Adaptation) improves upon LoRA by incorporating magnitude and direction updates separately. These methods have become standard in the open-source LLM ecosystem, supported by libraries such as Hugging Face PEFT and Unsloth.

## Key Claims

- LoRA reduces trainable parameters to less than 1% of full fine-tuning while retaining comparable performance on downstream tasks.
- QLoRA with 4-bit NF4 quantization enables fine-tuning of 7B models on consumer GPUs with 6-8 GB VRAM and 13B models with 12-16 GB VRAM.
- DoRA (Weight-Decomposed Low-Rank Adaptation) separates magnitude and direction updates, leading to more stable training and improved final accuracy compared to standard LoRA.
- The Hugging Face PEFT library provides a unified API for LoRA, QLoRA, and DoRA, allowing easy switching between techniques.
- Unsloth is a fine-tuning framework that optimizes memory usage and training speed, achieving up to 2x faster training than standard PEFT implementations.
- LoRA can be applied to any transformer-based model by injecting low-rank matrices into query, key, value, and output projection matrices.

## Relationships

No direct relationships with existing wiki pages are currently identified.

## Sources

- https://www.meta-intelligence.tech/en/insight-lora-finetuning
