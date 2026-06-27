---
cold_start: false
created: '2024-12-09'
inbound_links: 0
scorecard:
  bridge_score: 0.9
  claim_density: 0.8
  hub_potential: 0.8
  novelty_delta: 1.0
  self_containedness: 0.7
sources:
- https://www.sifive.com/blog/sifive-accelerates-risc-v-vector-integration-in-xnnpack-for-optimized-ai-inference
tags:
- risc-v
- xnnpack
- ai-inference
- sifive
- machine-learning
type: entity
updated: '2026-06-27'
---

# SiFive XNNPACK RISC-V Vector Integration

SiFive has contributed a set of RISC-V Vector (RVV) optimized microkernels to XNNPACK, a low-level acceleration backend for neural network inference used by frameworks such as TensorFlow Lite, PyTorch, and ONNX Runtime. These microkernels, including F32-GEMM, F32-IGEMM, and numerous element-wise operations, target single-precision floating-point operations and are designed to leverage the RISC-V Vector extension to improve inference performance on RISC-V platforms. Prior to these contributions, XNNPACK's support for RVV was limited, with few optimized kernels and reliance on generic C implementations or auto-vectorization. SiFive's contributions aim to make RISC-V a more viable architecture for AI inference by providing efficient, hand-tuned microkernels that exploit vector hardware capabilities. The company also published a step-by-step guide for developers to contribute additional RVV microkernels to XNNPACK, using F32-GEMM as a concrete example.

## Key Claims

- SiFive contributed 17 RVV-optimized floating-point microkernels to XNNPACK, enumerated in the blog post: F32-GEMM, F32-IGEMM, X32-PackW, F32-rmin, F32-rmax, F32-rminmax, F32-vadd, F32-vsub, F32-vrsub, F32-vmul, F32-vdiv, F32-vrdiv, F32-vmax, F32-vmin, F32-vsqrdiff, X32_transpose, and F32_raddstoreexpminusmax.
- These microkernels cover general matrix multiplication (GEMM), indirect GEMM for convolutions, weight packing, reduction operations, binary arithmetic, squared difference, transpose, and softmax exponent computation.
- XNNPACK is a low-level acceleration backend used by TensorFlow Lite, PyTorch, ONNX Runtime, and MediaPipe.
- Prior to SiFive's contributions, RISC-V support in XNNPACK was limited, with only a few RVV-optimized microkernels available, forcing reliance on generic C or auto-vectorization.
- The contributions significantly improve AI inference performance on RISC-V hardware by utilizing vector extensions.
- SiFive provided a step-by-step contribution guide: identify operation and relevant microkernels, analyze microkernel requirements, plan vectorization strategy, select microkernel parameters, and implement target-specific templates.

## Relationships


## Sources

- SiFive Blog: "SiFive Accelerates RISC-V Vector Integration in XNNPACK for Optimized AI Inference" (December 9, 2024): https://www.sifive.com/blog/sifive-accelerates-risc-v-vector-integration-in-xnnpack-for-optimized-ai-inference
