---
cold_start: true
created: YYYY-MM-DD
inbound_links: 0
scorecard:
  bridge_score: 0.6
  claim_density: 0.7
  hub_potential: 0.7
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://www.kendryte.com/k230_rtos/en/main/app_develop_guide/ai/usage_kpu.html
tags:
- RISC-V
- AI
- accelerator
- K230
- Kendryte
- edge_computing
type: entity
updated: '2026-06-28'
---

# KPU (Knowledge Processing Unit)

The KPU (Knowledge Processing Unit) is a hardware acceleration engine designed for edge artificial intelligence (AI) inference on the Kendryte K230 system-on-chip. It is a highly optimized deep learning accelerator that efficiently executes dense computation tasks for neural network models, supporting various mainstream visual neural network architectures. The KPU works in conjunction with the AI2D hardware image preprocessor and an Interpreter software component to perform end-to-end model inference, from input preprocessing through model execution to output post-processing. The inference pipeline includes steps such as loading the model, setting input and output tensors, preprocessing data, running KPU inference, and post-processing results. The KPU Runtime API provides functions for model loading and execution, with host_runtime_tensor as the data exchange format between components.

## Key Claims

- The KPU is a hardware accelerator that executes dense neural network computations efficiently.
- It supports mainstream visual neural network model architectures (e.g., YOLOv8).
- The inference flow consists of: LoadModel, SetInput, SetOutput, GetFrame, SetPreprocessParam, PreProcess, KPURun, GetOutput, PostProcess, DrawResult.
- AI2D is a hardware module for image preprocessing that improves runtime efficiency.
- AI2D's output tensor can be bound to the Interpreter's input tensor to avoid intermediate copies and save memory.
- The Interpreter component manages model inference execution on the KPU.
- The KPU is part of the K230 RTOS SDK and can be used with both image files and camera frames.

## Relationships

- [[Sipeed_MAIX_series]] – Both are RISC-V edge AI platforms, with the MAIX series using the earlier K210 SoC while the KPU is from the newer K230.
- Insufficient context for additional cross-links to other entity pages in the wiki.

## Sources

- [Kendryte K230 KPU Application Development Guide](https://www.kendryte.com/k230_rtos/en/main/app_develop_guide/ai/usage_kpu.html)
