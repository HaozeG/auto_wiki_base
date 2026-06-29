---
cold_start: true
created: '2026-06-29'
inbound_links: 1
scorecard:
  bridge_score: 0.8
  claim_density: 0.85
  hub_potential: 0.9
  novelty_delta: 0.9
  self_containedness: 0.8
sources:
- https://github.com/tenstorrent/tt-forge
tags:
- Tenstorrent
- TT-Forge
- MLIR
- compiler
- AI
- open-source
type: entity
updated: '2026-06-29'
---

# TT-Forge

TT-Forge is Tenstorrent's open-source MLIR-based compiler stack designed to enable efficient execution of AI workloads on Tenstorrent hardware, including both inference and training. Built on TT-Metalium, TT-Forge integrates multiple frontends—TT-XLA for PyTorch and JAX, TT-Forge-ONNX for ONNX, TensorFlow, and PaddlePaddle—a core MLIR compiler (TT-MLIR) that defines TTIR, TTNN, and TTKernel dialects and applies optimization passes such as fusion, sharding, and layout, a Python DSL for custom high-performance kernels (TT-Lang), and a model library (TT-Forge-Models) that continuously tests over 800 model variants in CI. The stack supports a wide range of models including GPT-OSS 120B, Llama 3 70B, Stable Diffusion XL, Whisper, and YOLOv12, and provides a streamlined workflow from high-level frameworks to optimized hardware execution. TT-Forge is in public beta and is designed for community contribution.

## Key Claims

- TT-Forge is built on TT-Metalium and provides a complete AI compiler stack for Tenstorrent hardware.
- Supports frontends for PyTorch (via TT-XLA using PJRT), JAX, ONNX, TensorFlow, and PaddlePaddle.
- TT-MLIR compiler defines TTIR, TTNN, and TTKernel dialects and applies optimizations including fusion, sharding, and layout lowering to TT-Metalium.
- TT-Lang provides a Python DSL for custom high-performance kernels with built-in simulation, profiling, and AI-assisted translation from Triton-class DSLs (early preview).
- TT-Blacksmith offers optimized training recipes and experiments for 40+ models spanning PyTorch, JAX, and Lightning.
- TT-Forge-Models continuously tests over 800 model variants in CI across LLMs, vision, NLP, multimodal, detection, segmentation, speech, and more.
- Models such as GPT-OSS 120B, Llama 3 70B, Stable Diffusion XL, Whisper, and YOLOv12 are runnable today.
- Supports both inference and training workloads with single and multi-chip configurations.

## Relationships

- [[Tenstorrent_Grayskull_e150]] – TT-Forge compiles AI workloads for Tenstorrent Grayskull hardware, which provides the TT-Metalium runtime that TT-Forge builds upon.
- [[TVM_and_Gemmini_Accelerator_Benchmark_Results]] – TT-Forge uses TVM in its TT-Forge-ONNX frontend; this benchmark page documents TVM integration with another accelerator (Gemmini), offering comparative context for compiler-based acceleration approaches.
- Insufficient context for additional cross-links to entity pages; the two links provided are to specialized pages (hardware_target and benchmark_result) that are directly related to TT-Forge.

## Sources

- https://github.com/tenstorrent/tt-forge
