---
cold_start: true
created: '2024-10-10'
inbound_links: 0
needs_summary_revision: false
scorecard:
  bridge_score: 0.7
  claim_density: 0.9
  hub_potential: 0.8
  novelty_delta: 0.8
  self_containedness: 0.8
sources:
- https://www.sifive.com/blog/llm-optimization-and-deployment-on-sifive-intellig
tags:
- sifive
- risc-v
- llm
- optimization
- software-stack
- x390
type: entity
updated: '2026-06-27'
---

# SiFive Intelligence X390

The SiFive Intelligence X390 is a RISC-V processor platform designed for AI/ML workloads, particularly large language model (LLM) inference and deployment. It is part of SiFive's Intelligence series, which also includes the X280, and leverages the RISC-V Vector Extension (RVV) for data-parallel computation. The X390 platform is supported by a comprehensive AI/ML software stack that integrates open-source components such as IREE (Intermediate Representation Execution Environment), a MLIR-based compiler and runtime, along with SiFive's proprietary optimizations including the SiFive LLVM compiler with advanced u-architecture optimizations, the SiFive Kernel Library (SKL) for tuned routines, and the VCIX MLIR dialect for offloading to custom TPUs. SiFive has demonstrated end-to-end LLM deployment on the X390 using a PyTorch workflow via SHARK-Turbine, converting Hugging Face models into IREE runtime-compatible formats. Performance profiling of TinyLlama on the X390 shows that matrix multiplication operations (matmul) consume over 95% of inference time, with the decode phase exhibiting General Matrix-Vector Multiply (GEMV) patterns. The software stack also supports lightweight frameworks such as customized TFLite with RVV optimizations, XNNPACK, and llama.cpp, enabling flexible deployment options for diverse AI workloads.

## Key Claims

- The SiFive Intelligence X390 is positioned as a future computing platform for AI/ML workloads, especially LLM inference and deployment.
- The SiFive AI/ML software stack includes SiFive Intelligence and High-Performance cores (X280, X390, P-series), SiFive accelerators (XM Series), SiFive LLVM compiler, SiFive System Software (FSFL, FSFM), and the SiFive Kernel Library (SKL).
- IREE is the primary ML compiler and runtime used, with SiFive contributing architecture-specific optimizations and patches, including VCIX MLIR dialect for custom TPU offloading.
- End-to-end LLM deployment on X390 uses a PyTorch workflow via SHARK-Turbine: `stateless_llm.py` compiles Hugging Face models into VMFB format, and `llm_runner.py` invokes the IREE runtime for inference.
- Performance profiling of TinyLlama during the decode phase shows matmul operations account for over 95% of inference time, with GEMV pattern (M=1) dominating.
- The platform also supports alternative inference frameworks: customized TFLite with RVV optimizations, XNNPACK with RVV, ONNXRuntime, and llama.cpp with additional RVV optimizations.

## Relationships

- [[risc_v_vector_extension]]: The X390 platform and its associated software stack heavily leverage the RISC-V Vector Extension (RVV) for vector processing, with components such as customized TFLite and XNNPACK implementing RVV optimizations.
- [[tvm_riscv_backend]]: IREE, the ML compiler used in the SiFive software stack, is closely related to Apache TVM as both are MLIR-based compilation frameworks targeting RISC-V backends for neural network inference.

## Sources

- https://www.sifive.com/blog/llm-optimization-and-deployment-on-sifive-intellig
