---
cold_start: true
created: 2026-06-27
inbound_links: 1
scorecard:
  bridge_score: null
  claim_density: null
  hub_potential: null
  novelty_delta: null
  self_containedness: null
sources:
- https://arxiv.org/abs/2010.08678
- https://github.com/AI-Vector-Accelerator/tinymlperf
- https://arxiv.org/pdf/2306.08951
- https://dl.acm.org/doi/10.1007/978-3-031-78459-0_24
tags:
- risc-v
- tinyML
- TensorFlow-Lite-Micro
- embedded
- inference
- benchmark
type: entity
updated: 2026-06-27
---

# TinyML on RISC-V

TinyML on RISC-V refers to the deployment of sub-milliwatt machine learning inference on microcontroller-class RISC-V processors, primarily using TensorFlow Lite for Microcontrollers (TFLM) and the MLPerf Tiny benchmark suite as the evaluation framework. RISC-V is increasingly competitive for TinyML because its open ISA allows custom extensions (RVV embedded sub-extensions, P-extension packed SIMD) to be added without licensing restrictions, while a growing ecosystem of libraries such as muRISCV-NN, IREE, and CMSIS-NN ports provides optimized kernel implementations. The MLPerf Tiny benchmark — covering keyword spotting, image classification, anomaly detection, and person detection — accepts TFLM as the open-source inference framework and has been used to characterize RISC-V performance on tasks ranging from ARM Cortex-M comparisons to RVV-vectorized inference on embedded cores.

## Key Claims

- TensorFlow Lite for Microcontrollers (TFLM) supports RISC-V RV64 builds and is the primary framework for MLPerf Tiny open-source submissions.
- MLPerf Tiny benchmark v1.0 defines four tasks: visual wake words (person detection, MobileNet), image classification (ResNet), keyword spotting (DS-CNN), and anomaly detection (toy-car).
- The AI-Vector-Accelerator project demonstrated RVV-accelerated TinyMLPerf inference achieving speedups on RISC-V cores with the Zve32x/64f vector sub-extensions.
- MLonMCU (2023) is a retargeting framework that automatically maps TinyML models (via TFLite, TVM) to RISC-V targets, reducing portability effort.
- muRISCV-NN achieves 3.85× speedup on ResNet inference vs. non-vectorized RISC-V, demonstrating the value of RVV for TinyML workloads.
- RISC-V Zve32x and Zve64f sub-extensions, ratified in 2023, define minimal vector hardware needed for TinyML without requiring full RVV 1.0.
- xTern (2024) demonstrates ternary neural network inference on RISC-V edge systems achieving energy-efficient classification without dedicated accelerators.

## Relationships

- [[muriscv_nn]]: muRISCV-NN is the primary CMSIS-NN drop-in library for RISC-V TinyML inference.
- [[riscv_zve_sub_extensions]]: Zve sub-extensions are the minimal RISC-V vector hardware needed for TinyML acceleration.
- [[risc_v_p_extension]]: P-extension packed SIMD provides an alternative to RVV for DSP-style TinyML kernels on MCU-class RISC-V.
- [[greenwaves_gap8_gap9]]: GAP8/GAP9 are leading commercial RISC-V targets for battery-powered TinyML inference.
- [[tvm_riscv_backend]]: TVM's RISC-V backend is used by MLonMCU to auto-generate optimized kernels for TinyML targets.

## Sources

- https://arxiv.org/abs/2010.08678
- https://github.com/AI-Vector-Accelerator/tinymlperf
- https://arxiv.org/pdf/2306.08951
- https://dl.acm.org/doi/10.1007/978-3-031-78459-0_24
