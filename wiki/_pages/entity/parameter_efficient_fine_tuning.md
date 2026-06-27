---
cold_start: false
created: '2025-04-07'
inbound_links: 0
scorecard:
  bridge_score: 0.3
  claim_density: 0.5
  hub_potential: 0.5
  novelty_delta: 0.8
  self_containedness: 0.6
sources:
- https://abvijaykumar.medium.com/fine-tuning-llm-parameter-efficient-fine-tuning-peft-lora-qlora-part-1-571a472612c4
tags:
- llm
- fine-tuning
- peft
- lora
- qlora
type: entity
updated: '2025-04-07'
---

# Parameter Efficient Fine Tuning (PEFT)

Parameter Efficient Fine Tuning (PEFT) is a set of techniques that enable the adaptation of large language models (LLMs) to specific tasks without updating all model parameters, thereby reducing computational and memory requirements significantly. Two widely adopted PEFT methods are Low-Rank Adaptation (LoRA) and its quantized variant QLoRA. LoRA works by freezing the pre-trained model weights and injecting trainable low-rank matrices into the model's layers, typically the attention layers, reducing the number of trainable parameters by orders of magnitude. QLoRA further improves memory efficiency by quantizing the frozen model weights to 4-bit precision while applying LoRA adapters, enabling fine-tuning of models with billions of parameters on a single consumer GPU. These techniques have become essential for practitioners who lack access to large-scale compute clusters and wish to customize LLMs for domain-specific applications without the overhead of full fine-tuning.

## Key Claims

- LoRA and QLoRA are two of the most emerging and widely used techniques for Parameter Efficient Fine Tuning.
- LoRA employs low-rank matrix decomposition to represent weight updates, significantly reducing the number of trainable parameters.
- QLoRA introduces quantization (typically 4-bit) to enhance parameter efficiency, allowing fine-tuning of large models on limited hardware.

The resource consists of a multi-part blog series; Part 1 covers the conceptual foundations of LoRA and QLoRA, and Part 2 covers implementation using QLoRA.

## Relationships

- [[large_language_models]] — PEFT methods like LoRA and QLoRA are applied to adapt LLMs to downstream tasks.
- [[full_fine_tuning]] — Unlike full fine-tuning, PEFT updates only a small subset of parameters, reducing memory and compute requirements.

## Sources

- Vijaykumar, A. B. (2023, August 9). *Parameter Efficient Fine Tuning (PEFT) — LoRA & QLoRA — Part 1*. Medium. https://abvijaykumar.medium.com/fine-tuning-llm-parameter-efficient-fine-tuning-peft-lora-qlora-part-1-571a472612c4
