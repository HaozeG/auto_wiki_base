---
type: entity
tags: [compiler, runtime, onnx, tensorrt, nvidia, inference, optimization]
sources:
  - https://onnx.ai/
  - https://developer.nvidia.com/tensorrt
  - https://arxiv.org/abs/2302.00173
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

# ONNX / TensorRT

ONNX (Open Neural Network Exchange) is an open interchange format for machine learning models, maintained by the Linux Foundation AI & Data since 2017, originally co-developed by Microsoft and Facebook. ONNX defines a standardized computation graph with typed operators (Conv, MatMul, LayerNorm, etc.) and a protobuf-based serialization so that models trained in PyTorch, TensorFlow, scikit-learn, or JAX can be exported once and deployed on any compliant runtime. TensorRT is NVIDIA's closed-source inference optimizer and runtime that ingests ONNX graphs (and its own native format) and applies a multi-stage optimization pipeline: layer fusion (combining Conv+BN+ReLU into a single kernel), kernel auto-selection (choosing the fastest CUDA kernel for a given input shape from a library of hand-tuned and auto-generated variants), precision calibration (FP32 → FP16 → INT8 with per-tensor or per-channel scale factors), and graph-level constant folding. On NVIDIA GPUs, TensorRT typically delivers 2–5× latency reduction over PyTorch eager mode for transformer inference workloads, and up to 8× for convolutional networks at INT8 precision. TensorRT is the standard inference backend for NVIDIA Jetson (edge), NVIDIA A100/H100 data center GPUs, and NVIDIA Drive (automotive), and is integrated into frameworks including ONNX Runtime, Triton Inference Server, and DeepStream.

## Key Claims

- ONNX opset versioning (opset 1 through opset 21 as of 2024) provides backward-compatible operator semantics; opset 17 added `LayerNormalization` and `BlackmanWindow` operators to better support transformer and audio models natively.
- TensorRT's INT8 calibration requires a representative calibration dataset (typically 500–1000 samples); it computes per-tensor dynamic range and selects quantization scales that minimize KL divergence between FP32 and INT8 activation distributions, achieving within 1% top-1 accuracy on ResNet-50 and BERT compared to FP32 baselines.
- NVIDIA publishes TensorRT benchmark results showing 3–5× latency improvement over PyTorch FP32 for BERT-Large inference on A100 at batch size 1, and up to 8× for ResNet-50 at INT8 vs. PyTorch FP32.
- TensorRT's layer fusion engine merges multi-head attention (QKV projection, scaled dot-product, output projection) into a single `fMHA` kernel on Ampere and Hopper GPUs using FlashAttention-style IO-optimal algorithms, reducing memory traffic and improving latency by 1.5–2× relative to unfused attention.
- ONNX Runtime (ORT), Microsoft's open-source inference engine for ONNX models, supports execution providers for CUDA (via CUDAExecutionProvider), TensorRT (TensorRTExecutionProvider), DirectML, OpenVINO, and CoreML, enabling the same ONNX model to target diverse hardware through a unified API.
- ONNX model export from PyTorch uses `torch.onnx.export` (tracing-based, now also via `torch.export` + `torch.onnx.dynamo_export`); the dynamo-based exporter, introduced in PyTorch 2.0, handles dynamic control flow and data-dependent shapes that the tracing exporter cannot capture.

## Relationships

- [[nvidia_hopper_h100]] — TensorRT uses Hopper-specific CUDA kernels (wgmma, FlashMHA) when targeting H100, with the H100-optimized TensorRT engine delivering materially lower latency than the A100 engine on the same model.
- [[flash_attention]] — TensorRT's fused multi-head attention kernel adopts the FlashAttention IO-optimal tiling algorithm to reduce HBM bandwidth usage during transformer inference.
- [[mlir_llvm_ai]] — Models compiled through MLIR pipelines (e.g., via torch-mlir) can be serialized to ONNX for deployment via ONNX Runtime or TensorRT, bridging research compilers and production inference stacks.
- [[openai_triton]] — ONNX Runtime's CUDA execution provider can optionally use Triton-generated kernels for certain ops (via contrib ops), but TensorRT remains the primary high-performance backend for NVIDIA GPU inference.
- [[aws_inferentia]] — AWS Neuron SDK supports ONNX model import for deployment on Inferentia and Trainium, competing with TensorRT on the inference optimization front.

## Sources

- ONNX specification and operator reference: https://onnx.ai/onnx/operators/
- NVIDIA TensorRT documentation and performance benchmarks: https://developer.nvidia.com/tensorrt
- NVIDIA TensorRT 8.x developer guide (INT8 calibration): https://docs.nvidia.com/deeplearning/tensorrt/developer-guide/index.html
- ONNX Runtime documentation: https://onnxruntime.ai/
- PyTorch 2.0 ONNX dynamo exporter: https://pytorch.org/docs/stable/onnx_dynamo.html
