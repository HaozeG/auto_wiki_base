---
cold_start: false
created: '2026-07-02'
inbound_links: 0
needs_summary_revision: false
scorecard:
  bridge_score: 0.5
  claim_density: 0.6
  hub_potential: 0.7
  novelty_delta: 0.9
  self_containedness: 1.0
sources:
- https://github.com/mlcommons/training
tags:
- MLPerf
- training benchmark
- reference implementation
- MLCommons
type: entity
updated: '2026-06-29'
---

# MLPerf Training Reference Implementations

The MLPerf Training Reference Implementations repository is the official source of reference implementations for the MLPerf training benchmarks. These implementations are intended as valid starting points for benchmark submitters but are not fully optimized and should not be used for real performance measurements of software frameworks or hardware. The repository provides code for each benchmark model, Dockerfiles for containerized execution, instructions for dataset download via mlcommons-storage, and timing scripts that run until target quality is reached. It tracks multiple submission rounds including v5.1 (deadline October 10, 2025) and v6.0 (deadline May 15, 2026). Supported models include Flux.1 for text-to-image, Llama 3.1 8B and 405B for LLM pretraining, Llama 2 70B LoRA, DLRM DCNv2 for recommendation, GPT OSS 20B MoE, DeepSeek-v3 MoE, RetinaNet, and RGAT. Implementations use frameworks such as PyTorch, NeMo, torchrec, Primus, and TorchTitan.

## Key Claims

- The repository contains reference implementations for MLPerf training benchmarks v5.1 and v6.0.
- These implementations are not fully optimized and are not intended for real performance measurements.
- Each implementation includes code, a Dockerfile, dataset download instructions, and a timing script that stops when target quality is reached.
- Benchmarks cover diverse workloads: text-to-image (Flux.1), LLM pretraining (Llama 3.1 8B, Llama 3.1 405B), LoRA fine-tuning (Llama 2 70B), recommendation (DLRM DCNv2), mixture-of-experts (GPT OSS 20B, DeepSeek-v3), object detection (RetinaNet), and graph neural networks (RGAT).
- Supported frameworks include PyTorch, NeMo, torchrec, Primus, and TorchTitan.
- Reference implementations are documented with model parameter counts and dataset details (e.g., C4, CC12M, Criteo 3.5TB, OpenImages, IGBH-Full, SCROLLS GovReport).

## Relationships

- [[Gemmini_Architecture]] – Gemmini is an open-source DNN accelerator generator that could potentially be used to accelerate MLPerf training benchmark workloads.
- Insufficient context for additional cross-links to entity pages; only one relevant page exists in the current wiki.

## Sources

- [GitHub - mlcommons/training](https://github.com/mlcommons/training)
