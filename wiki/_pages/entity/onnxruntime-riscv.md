---
cold_start: true
created: '2025-01-27'
inbound_links: 1
scorecard:
  bridge_score: 0.7
  claim_density: 0.2
  hub_potential: 0.3
  novelty_delta: 0.6
  self_containedness: 0.7
sources:
- https://github.com/ucb-bar/onnxruntime-riscv
tags:
- ONNX Runtime
- RISC-V
- Gemmini
- inference
type: entity
updated: '2026-06-28'
---

# onnxruntime-riscv

onnxruntime-riscv is a fork of ONNX Runtime developed by the UC Berkeley ASPIRE Laboratory (ucb-bar) that modifies the upstream onnxruntime project to work on RISC-V platforms with primary focus on supporting the Gemmini DNN accelerator. The fork provides cross-compilation and usage instructions via the `systolic_runner` subdirectory and is designed especially for running quantized neural networks. Although Gemmini is not required, CPU-only inference on RISC-V is less thoroughly tested and may not be performant because the `sgemm` kernel is implemented via naive matmul and has not yet been linked with a proper BLAS library. The project leverages ONNX Runtime's graph optimizations and hardware accelerator interfaces, enabling compatibility with models from PyTorch, TensorFlow/Keras, scikit-learn, and other frameworks.

## Key Claims

- onnxruntime-riscv is a fork of upstream ONNX Runtime specifically modified for RISC-V platforms.
- The fork is particularly focused on supporting the Gemmini DNN accelerator.
- It can also run CPU-only inference on RISC-V, but performance may be limited due to a naive `sgemm` kernel and lack of a proper BLAS library.
- The project is primarily designed for running quantized neural networks.
- Cross-compilation and usage instructions are provided in the `systolic_runner` subdirectory.

## Relationships

- [[Gemmini_Architecture]] – Gemmini is the primary hardware target of this fork.

Note: Insufficient context for additional cross-links to entity pages; the only relevant entity page available in the wiki is Gemmini_Architecture.

## Sources

- [GitHub - ucb-bar/onnxruntime-riscv](https://github.com/ucb-bar/onnxruntime-riscv)
