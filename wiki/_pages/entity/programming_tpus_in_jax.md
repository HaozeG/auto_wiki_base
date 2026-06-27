---
cold_start: false
created: '2025-02-06'
inbound_links: 0
scorecard:
  bridge_score: 0.9
  claim_density: 0.8
  hub_potential: 0.8
  novelty_delta: 0.9
  self_containedness: 0.8
sources:
- https://jax-ml.github.io/scaling-book/jax-stuff/
tags:
- jax
- tpu
- google
- scaling
- parallelism
- hardware-programming
type: entity
updated: '2025-02-06'
---

# Programming TPUs in JAX

Programming TPUs in JAX refers to the set of techniques and APIs within the Google JAX library that enable efficient execution of numerical computations on Tensor Processing Units (TPUs). JAX provides a NumPy-like interface with automatic differentiation and just-in-time compilation via XLA. To leverage TPUs, developers use specialized APIs such as `pmap`, `pjit`, and the more recent `shard_map` for explicit sharding of computations across TPU cores. The `shard_map` API, introduced in JAX version 0.4.10 and detailed in JEP 14273, allows users to define per-core computations with explicit data partitioning, enabling fine-grained control over memory layout and communication patterns on TPU v3, v4, and v5e/v5p accelerator pods. This approach is critical for scaling large models like transformers and LLMs, as it minimizes communication overhead and maximizes compute utilization. The resource "Programming TPUs in JAX" is part of the "How To Scale Your Model" book authored by researchers from Google DeepMind and includes code examples that can be run on free TPUs available via Google Colab. It covers practical aspects of sharding strategies, mesh configuration, and optimization tips for TPU-efficient training and inference.

## Key Claims

- The `shard_map` API (JEP 14273) is the primary method for explicit per-core TPU programming in JAX, allowing developers to define computations with explicit data partitioning.
- Free TPU access for running JAX code is available through Google Colab, enabling hands-on learning without dedicated hardware.
- The resource is authored by a team of researchers including Jacob Austin, Sholto Douglas, Roy Frostig, Anselm Levskaya, Charlie Chen, Sharad Vikram, Federico Lebron, Peter Choy, and Vinay Ramasesh, affiliated with Google DeepMind.
- The content is derived from JEP 14273, providing a distilled, practical guide to using `shard_map` for scaling model training on TPU pods.

## Relationships

- No direct relationships currently exist with other pages in this wiki. The topic of TPU programming in JAX is orthogonal to the existing page on AI chip export controls ([[ai_chip_export_controls.md]]), which focuses on semiconductor trade regulations rather than software-level programming techniques.

## Sources

- JAX Scaling Book: Programming TPUs in JAX – https://jax-ml.github.io/scaling-book/jax-stuff/
