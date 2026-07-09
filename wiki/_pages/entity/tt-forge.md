---
canonical_name: TT-Forge
aliases:
- tt-forge
- Tenstorrent Forge
- Tenstorrent's MLIR based compiler
- Forge compiler stack
- TT-Forge Software Stack
- Forge
- TT-Forge compiler
- Tenstorrent-Forge
subtype: null
tags: []
scorecard:
  novelty_delta: 0.5
  claim_density: 0.2
  self_containedness: 0.8
  bridge_score: 0.5
  hub_potential: 0.3
sources:
- raw/cache/ba00f84ee6d2dca4.md
- https://github.com/tenstorrent/tt-forge
- raw/cache/adc599aaa4aec6ac.md
- https://tenstorrent.com/en/software/tt-forge
- raw/cache/06170cbedf69b42c.md
- https://deepwiki.com/tenstorrent/tt-forge/2-tt-forge-software-stack
- raw/cache/108f743495674ed6.md
- https://github.com/tenstorrent/tt-quietbox2-guide/blob/main/src/content/shared/tt-forge-intro.md
- raw/cache/becc43ea25b301c4.md
- https://github.com/tenstorrent/tt-forge/blob/main/README.md
source_url: https://github.com/tenstorrent/tt-forge
fetched_at: '2026-07-09T10:03:31.716141+00:00'
type: entity
created: '2026-07-09'
updated: '2026-07-09'
cold_start: true
inbound_links: 1
outbound_links:
- target: blackhole
  reason: TT-Forge is the software compiler stack that enables running AI models on
    Tenstorrent hardware such as the Blackhole chip. Blackhole provides the Tensix
    core mesh and RISC-V control cores that TT-Forge targets via its MLIR compilation
    pipeline and TT-Metalium runtime
- target: tt-forge-onnx
  reason: TT-Forge-ONNX is the TVM-based ONNX/TensorFlow/PaddlePaddle frontend sub-project
    within the TT-Forge compiler stack, complementing the TT-XLA PyTorch/JAX frontend.
---

# TT-Forge

TT-Forge is Tenstorrent's open-source MLIR-based AI compiler stack, built on TT-Metalium. It brings together frontends, an MLIR compiler, a kernel DSL, and a model library to make running AI workloads on Tenstorrent hardware straightforward. It compiles models from multiple frontends (PyTorch via TT-XLA/PJRT/StableHLO, JAX, ONNX, TensorFlow, PaddlePaddle, OpenXLA, TVM) into native executables for Tensix-core-based accelerators. The compiled model runs directly on Tenstorrent hardware without needing a separate inference server or runtime, and retains the original module interface for drop-in replacement. Over 800 model variants are continuously tested in CI, accessible via a standardized `ModelLoader` interface (tt-forge-models zoo); thousands more have been tested internally, covering LLMs, vision, multimodal, detection, segmentation, speech, and more. Installation requires setting up a Python virtual environment and installing the `pjrt-plugin-tt` package from Tenstorrent's private package index, followed by `tt-forge-install`; public PyPI availability is pending. The project includes tools such as TT-Explorer (visual performance analyzer), TT-NPE (network-on-chip simulator and profiler), TT-Blacksmith (40+ ready-to-run training recipes), and TT-Lang (a Python DSL for custom kernels with AI-assisted translation from Triton-class DSLs). TT-Forge supports both inference and training on all Tenstorrent hardware configurations, from single-chip to multi-chip systems. The stack comprises several sub-projects: TT-XLA (PJRT-based PyTorch/JAX frontend), TT-Forge-ONNX (TVM-based ONNX/TensorFlow/PaddlePaddle frontend, single-chip), TT-MLIR (core MLIR compiler defining TTIR, TTNN, and TTKernel dialects), TT-Lang (Python kernel DSL, early preview), TT-Blacksmith (training recipes with 40+ experiments), and TT-Forge-Models (model library with standardized loaders).

## Key Claims

- TT-Forge is an open-source MLIR-based compiler stack for Tenstorrent hardware, built on TT-Metalium.
- It provides two primary frontends: TT-XLA (using `torch.compile(backend="tt")` for PyTorch and `jax.jit` for JAX/Flax) and TT-Forge-ONNX (using `forge.compile` for ONNX, TensorFlow, and PaddlePaddle models, targeted at single-chip projects). Additional frontends include OpenXLA and TVM.
- Both frontends lower through the same TT-MLIR compiler, which defines three dialects (TTIR, TTNN, TTKernel) and applies optimization passes for fusion, sharding, and layout lowering.
- TT-Lang is a Python DSL for custom kernels, with simulation, profiling, fusion, and AI-assisted translation from Triton-class DSLs (early preview).
- TT-Blacksmith provides 40+ ready-to-run training recipes for models including Llama, Gemma, Qwen, ViT, and NeRF, using PyTorch, JAX, and Lightning.
- TT-Forge-Models maintains over 800 model variants continuously tested in CI (including ResNet, BERT, CLIP, DINOv2, BLOOM, Llama, GPT-OSS 120B, Llama 3 70B, Stable Diffusion XL, Whisper, YOLOv12) with a standardized `ModelLoader` interface; thousands have been run internally, covering LLMs, vision, multimodal, detection, segmentation, speech, and more.
- Models can be run through standard PyTorch with `torch.compile(backend="tt")` and minimal code changes; the compiled model retains the original PyTorch module interface for drop-in replacement.
- Included tools: TT-Explorer (visual performance analyzer), TT-NPE (network-on-chip simulator and profiler).
- TT-XLA is a PJRT-based bridge for JAX and PyTorch with multi-chip support.
- TT-Forge-ONNX is a TVM-based, framework-agnostic frontend for ONNX and TensorFlow single-chip projects.
- Hardware-aware compilation achieves high utilization, efficient memory access, and scalable performance across chips.
- Installation via pip with an extra index URL (`pjrt-plugin-tt`) followed by `tt-forge-install`; wheels are hosted on Tenstorrent's private package index.
- Supports inference and training on all Tenstorrent hardware configurations, from single-chip to multi-chip.

## Relationships

- [[blackhole]]: TT-Forge is the software compiler stack that enables running AI models on Tenstorrent hardware such as the Blackhole chip. Blackhole provides the Tensix core mesh and RISC-V control cores that TT-Forge targets via its MLIR compilation pipeline and TT-Metalium runtime.
- [[tt-xla-performance-optimization-techniques]]: TT-Forge is the overarching compiler stack that includes the TT-XLA frontend. The optimization techniques documented on that page (optimization levels, warmup, data formats, runtime trace, batch tuning) are applied when compiling models with the TT-XLA component of TT-Forge.

- [[tt-forge-onnx]]: TT-Forge-ONNX is the TVM-based ONNX/TensorFlow/PaddlePaddle frontend sub-project within the TT-Forge compiler stack, complementing the TT-XLA PyTorch/JAX frontend.

## Sources

- https://github.com/tenstorrent/tt-forge/blob/main/README.md
- https://github.com/tenstorrent/tt-forge
- https://tenstorrent.com/en/software/tt-forge
- https://github.com/tenstorrent/tt-quietbox2-guide/blob/main/src/content/shared/tt-forge-intro.md
