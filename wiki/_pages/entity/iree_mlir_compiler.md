---
type: entity
tags:
  - mlir
  - compiler
  - risc-v
  - rvv
  - embedded-ai
  - runtime
  - google
sources:
  - https://github.com/iree-org/iree
created: 2026-06-27
updated: 2026-06-27
cold_start: false
inbound_links: 0
scorecard:
  novelty_delta: 0.7
  claim_density: 0.7
  self_containedness: 0.85
  bridge_score: 0.6
  hub_potential: 0.5
---

# IREE (Intermediate Representation Execution Environment)

IREE (Intermediate Representation Execution Environment) is an open-source ML compiler and runtime stack developed by Google, built on MLIR (Multi-Level Intermediate Representation). It performs ahead-of-time (AOT) compilation of ML models into efficient native code for diverse hardware targets including x86, ARM, RISC-V (via RVV vector extension), GPU (Vulkan, Metal, CUDA), and bare-metal microcontrollers. IREE's RISC-V backend leverages LLVM's RVV code generation to produce vectorized kernels for RISC-V Vector Extension 1.0 targets, achieving 2–5× speedup over non-vectorized implementations on RVV-capable cores in benchmark microkernels. The runtime is designed for minimal binary footprint, making IREE a primary deployment path for ML inference on resource-constrained RISC-V devices—from embedded SoCs to mobile application processors. IREE integrates with TensorFlow Lite (TFLite) as a runtime backend, enabling deployment of quantized INT8 and FP16 models on RISC-V platforms without a dedicated NPU, and serves as the compilation backbone for Google's on-device ML strategy for open-ISA hardware.

## Key Claims

- IREE generates AOT-compiled ML kernels for RISC-V RVV 1.0 via its LLVM backend, with benchmark speedups of 2–5× over scalar (non-vectorized) implementations on RVV-capable cores.
- Supports multiple hardware backends in a single runtime: x86 (AVX2/AVX-512), ARM (NEON/SVE), RISC-V (RVV), Vulkan GPU, Metal GPU, CUDA.
- Integrates with TFLite Micro for embedded RISC-V deployment, enabling INT8 quantized model inference on systems with as little as 512 KB SRAM.
- Built on MLIR, allowing custom ML dialects and optimization passes to be inserted into the compilation pipeline before RISC-V code generation.
- IREE's minimal runtime binary can target bare-metal RISC-V environments (no OS), enabling deployment on MCU-class RISC-V cores like SiFive E-series.
- Google uses IREE as the compilation target for Pixel device on-device ML workloads on ARM; the same pipeline applies to RISC-V targets.

## Relationships

- [[risc_v_vector_extension]] — IREE's RISC-V backend targets RVV 1.0 to generate vectorized ML kernels.
- [[openai_triton]] — Complementary ML compiler; Triton targets GPU PTX/ROCm while IREE targets CPU/RISC-V and GPU via Vulkan.
- [[tinyml_mcu_inference]] — IREE serves as a compilation path for TinyML models on RISC-V MCU targets.
- [[zephyr_rtos_tflite_micro]] — IREE complements TFLite Micro on Zephyr for RISC-V; TFLite Micro uses IREE's compiled kernels.
- [[riscv_zvfh_extension]] — IREE's FP16 inference on RISC-V benefits from the Zvfh FP16 vector extension.

## Sources

- IREE GitHub repository: https://github.com/iree-org/iree
- IREE RISC-V backend documentation and benchmarks
- MLIR project: https://mlir.llvm.org/
