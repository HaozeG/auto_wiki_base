---
type: entity
tags: [ml-framework, deep-learning, python, distributed-training]
sources:
  - https://pytorch.org/blog/pytorch-2.0-release/
  - https://arxiv.org/abs/2311.12699
  - https://pytorch.org/docs/stable/torch.compiler.html
created: 2026-06-26
updated: 2026-06-26
cold_start: false
inbound_links: 0
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# PyTorch 2.x Training Framework

PyTorch 2.x is the dominant open-source deep learning framework developed by Meta AI, used in over 70% of ML research papers as of 2024. The 2.0 release introduced `torch.compile`, a compiler stack that captures and optimizes Python-level model code without requiring users to rewrite their models. The compilation pipeline consists of three components: TorchDynamo, which intercepts Python bytecode at runtime to extract computation graphs; AOTAutograd, which traces both forward and backward passes ahead of time; and TorchInductor, which lowers the captured graphs to optimized GPU kernels via OpenAI Triton or CPU C++ code. This approach preserves PyTorch's define-by-run imperative programming model while enabling graph-level optimizations that were previously only available in static-graph frameworks like TensorFlow. The framework supports multiple capture modes — `eager` (default, no compilation), `reduce-overhead` (CUDA graph capture for small models), and `max-autotune` (exhaustive kernel search) — allowing users to trade compile time for runtime performance.

## Key Claims

- `torch.compile` achieves a dynamo capture rate of approximately 90% on production models, meaning 90% of the computational graph is successfully traced and compiled rather than falling back to eager execution.
- TorchInductor delivers 1.5× to 4× speedup over eager PyTorch on a broad benchmark suite (TorchBench), with the largest gains on transformer attention and convolution-heavy workloads when using `max-autotune` mode.
- PyTorch was used in over 70% of ML papers with public code as of 2024, measured across arXiv submissions, exceeding TensorFlow's share by roughly 3:1.
- Fully Sharded Data Parallel v2 (FSDP2) supports training models with hundreds of billions of parameters by sharding optimizer states, gradients, and parameters across GPU ranks, reducing per-device memory by approximately N× for N devices.
- The `torch.export` API (stable in PyTorch 2.3) captures a strict, serializable computation graph suitable for deployment to mobile, server inference, or exchange via ONNX/ExecuTorch, distinct from the flexible graph captured during training compilation.
- TorchDynamo uses Python bytecode analysis rather than tracing through tensor operations, making it compatible with arbitrary Python control flow via graph breaks — a key architectural difference from JAX's `jit` which requires static control flow.

## Relationships

- [[openai_triton]]: TorchInductor generates Triton kernels as its primary GPU backend; Triton's tile-level programming model is central to Inductor's auto-tuning strategy.
- [[mlir_llvm_ai]]: TorchInductor's CPU backend lowers through LLVM IR; the broader PyTorch compiler pipeline intersects with MLIR-based compiler infrastructure for hardware portability.
- [[onnx_tensorrt]]: `torch.export` and `torch.onnx.export` produce ONNX graphs that can be consumed by TensorRT for high-performance NVIDIA inference, connecting the training framework to inference deployment.
- [[nvidia_hopper_h100]]: PyTorch 2.x exposes FlashAttention-2 and FP8 training (via `torch.float8_e4m3fn`) targeting Hopper's Tensor Cores; FSDP2 and NCCL-based communication are tuned for NVLink/NVSwitch topologies present in H100 clusters.
- [[model_parallelism_llm_training_inference]]: FSDP2, tensor parallelism via `torch.distributed.tensor`, and pipeline parallelism primitives in `torchpippy` collectively implement the 3D parallelism strategies used for LLM training at scale.

## Sources

- PyTorch 2.0 release blog (Meta AI, 2023): https://pytorch.org/blog/pytorch-2.0-release/
- "PyTorch 2: Faster Machine Learning Through Dynamic Python Bytecode Transformation and Graph Compilation", Ansel et al., SOSP 2023: https://arxiv.org/abs/2311.12699
- TorchInductor design doc: https://dev-discuss.pytorch.org/t/torchinductor-a-pytorch-native-compiler-with-define-by-run-ir/747
- FSDP2 RFC: https://github.com/pytorch/pytorch/issues/114299
- torch.export documentation: https://pytorch.org/docs/stable/export.html
- "Trends in ML frameworks" analysis, Papers With Code 2024 State of AI Report
