---
cold_start: false
created: '2026-06-26'
inbound_links: 0
scorecard:
  bridge_score: 0.8
  claim_density: 0.8
  hub_potential: 0.6
  novelty_delta: 0.9
  self_containedness: 0.7
sources:
- https://www.sifive.com/blog/llm-optimization-and-deployment-on-sifive-intellig
tags:
- RISC-V
- Machine Learning
- SiFive
- LLM
type: entity
updated: '2026-06-27'
---

# SiFive AI/ML Software Stack

The SiFive AI/ML Software Stack is a comprehensive software platform for deploying machine learning models, particularly large language models, on SiFive RISC-V Intelligence processors. It integrates multiple layers: SiFive core processors (including the Intelligence X280 and X390), accelerators like the XM Series, a proprietary LLVM compiler with RISC-V vector extensions (RVV) optimizations, system software (Freedom SDK for Linux and Metal), the SiFive Kernel Library (SKL) for optimized routines, and open-source components such as the IREE MLIR compiler and runtime and the VCIX MLIR dialect for custom tensor processing units. The stack also supports frameworks like PyTorch via SHARK-Turbine and offers lightweight inference through customized TFLite, XNNPACK, ONNXRuntime, and Llama.cpp with RVV optimizations. This stack aims to enable real-time LLM inference on RISC-V hardware.

## Key Claims

- The SiFive AI/ML Software Stack includes SiFive Intelligence cores (X280/X390), SiFive accelerators (XM Series), SiFive LLVM Compiler with RVV optimizations, SiFive System Software (Freedom SDK for Linux and Metal), and SiFive Kernel Library (SKL) for maximizing algorithm throughput.
- Open-source components leveraged include IREE (an MLIR-based compiler and runtime), VCIX MLIR dialect for lowering models to custom TPUs, and optimized versions of TFLite, XNNPACK, ONNXRuntime, and Llama.cpp with RVV optimizations.
- For LLM deployment, SiFive uses SHARK-Turbine to convert PyTorch Hugging Face models into VMFB files using IREE compiler with SiFive-specific patches, then loads them via IREE runtime on SiFive cores.
- Performance profiling of TinyLLama during the decode phase showed that matrix multiplication (matmul) operations consume over 95% of inference time, with operations following the GEMV pattern (M=1) in decode and GEMM pattern in prefill.
- The SiFive Kernel Library offloads hotspot operations from IREE to optimized routines tuned for SiFive processors.
- The stack provides two execution paths: a full ML framework path using IREE and a lightweight path using llama.cpp or other lightweight interpreters.

## Relationships

- This page fills concept gaps related to VCIX (Vector Coprocessor Interface Extension) and RISC-V Matrix Extensions by documenting SiFive's VCIX MLIR dialect and XM Series accelerators.
- No existing wiki pages directly relate to this entity; it stands as a new addition covering SiFive's AI/ML software stack.

## Sources

- SiFive Blog: "LLM Optimization and Deployment on SiFive RISC-V Intelligence Products" (October 10, 2024)
