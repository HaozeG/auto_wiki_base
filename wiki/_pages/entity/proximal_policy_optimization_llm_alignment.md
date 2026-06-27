---
cold_start: false
created: '2025-03-24'
inbound_links: 1
scorecard:
  bridge_score: 0.1
  claim_density: 0.7
  hub_potential: 0.6
  novelty_delta: 0.9
  self_containedness: 0.8
sources:
- https://arxiv.org/abs/2404.10719
tags:
- LLM
- RLHF
- alignment
- PPO
type: entity
updated: '2025-03-24'
---

# Proximal Policy Optimization (PPO) for LLM Alignment

Proximal Policy Optimization (PPO) is a reinforcement learning algorithm widely used for fine-tuning large language models (LLMs) to align with human preferences, forming the core of reward-based RLHF systems. In this context, PPO optimizes a language model policy by maximizing a reward signal from a separately trained reward model while constraining the policy update via a clipped surrogate objective. PPO was employed in the training of ChatGPT and Claude, demonstrating its effectiveness in real-world applications. Despite its success, PPO has been perceived as less competitive than reward-free alternatives like Direct Preference Optimization (DPO) in academic benchmarks. However, a comprehensive study by Xu et al. (2024) shows that with proper tuning of key hyperparameters—such as reward model quality, KL penalty coefficient, and advantage normalization—PPO consistently surpasses DPO and achieves state-of-the-art results, particularly in code competition tasks. The study attributes PPO's superior performance to its ability to incorporate rich reward shaping and its on-policy nature, which better handles complex, multi-faceted objectives.

## Key Claims

- PPO is a reward-based RLHF algorithm that uses a separate reward model and on-policy sampling for alignment.
- PPO was used to train production systems like ChatGPT and Claude, demonstrating scalability.
- With careful hyperparameter tuning (reward model quality, KL penalty coefficient, advantage normalization), PPO outperforms DPO across all tested benchmarks.
- PPO achieves state-of-the-art results in code competition tasks, a domain where alignment often proves challenging.
- PPO can incorporate non-differentiable reward signals and complex reward shaping due to its reward model infrastructure.

## Relationships

- [[direct_preference_optimization]] — Compared method; PPO demonstrates superior performance when properly tuned.

## Sources

- https://arxiv.org/abs/2404.10719
