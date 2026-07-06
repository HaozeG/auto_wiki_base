---
canonical_name: XuanTie AI Benchmark Suite
aliases:
- xtai-benchmark
- XUANTIE-RV/xtai-benchmark
subtype: null
tags: []
scorecard:
  novelty_delta: 0.7
  claim_density: 0.3
  self_containedness: 0.9
  bridge_score: 0.5
  hub_potential: 0.3
sources:
- raw/cache/c299f70f63c853c6.md
- https://github.com/XUANTIE-RV/xtai-benchmark
source_url: https://github.com/XUANTIE-RV/xtai-benchmark
fetched_at: '2026-07-03T13:17:10.119298+00:00'
type: entity
created: '2026-07-03'
updated: '2026-07-06'
cold_start: true
inbound_links: 3
outbound_links:
- target: xuantie-c908
  reason: The benchmark suite provides precompiled model binaries specifically targeting
    the XuanTie C908 core, leveraging the HHB toolchain for inference deployment
---

# XuanTie AI Benchmark Suite

The XuanTie AI Benchmark Suite (xtai-benchmark) is an open-source GitHub repository maintained by XUANTIE-RV that provides a collection of precompiled benchmark binaries for evaluating AI algorithm performance on XuanTie RISC-V CPUs with RVV/RVM. The suite includes popular models such as BERT, EfficientNet, and MobileNetV2, each compiled for both the C907 and C908 cores under multiple quantization formats including float32, float16, int8 asymmetric weights with symmetric activations, and in select cases a mixed float16 weights with int8 format. The benchmark binaries use the ONNX model format and are designed to be deployed using T-Head's HHB neural network inference deployment tool. No actual performance measurements are included; the repository serves as a resource for developers to obtain precompiled models for benchmarking on their own hardware.

## Key Claims

- Provides precompiled benchmark binaries for BERT, EfficientNet, and MobileNetV2 for XuanTie C907 and C908.
- Supports quantization formats: float32, float16, int8_asym_w_sym, and float16_w_int8.
- Binaries are in ONNX format and intended for use with the HHB deployment tool.
- No performance measurements are included; only precompiled model binaries are provided.

## Relationships

- [[xuantie-c908]]: The benchmark suite provides precompiled model binaries specifically targeting the XuanTie C908 core, leveraging the HHB toolchain for inference deployment.
- [[xuantie-gnu-compiler-toolchain]]: The XuanTie GNU Compiler Toolchain provides the cross-compiler used to build the precompiled model binaries in this benchmark suite.

## Sources

- https://github.com/XUANTIE-RV/xtai-benchmark
