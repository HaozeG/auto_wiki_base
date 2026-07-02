---
canonical_name: Kendryte K230 Neural Network Benchmarks
aliases:
- K230 NN benchmarks
- CanMV-K230 benchmarks
subtype: null
tags: []
hardware_targets:
- Kendryte K230
workloads:
- Resnet50
- Mobilenet_v2
- YoloV5S
datatypes:
- INT8
metrics:
- throughput (fps)
toolchains:
- TVM
- TensorFlow
- PyTorch
- ONNX
hardware_versions: []
software_versions: []
measurement_method: Typical network performance reported on product specification
  page, not independently verified.
evidence_strength: reported
scorecard:
  novelty_delta: 0.9
  claim_density: 0.7
  self_containedness: 0.8
  bridge_score: 0.5
  hub_potential: 0.3
sources:
- raw/cache/6022331efb0961c4.md
- https://www.youyeetoo.com/products/canmv-k230-kendryte-k230-risc-v64-board
source_url: https://www.youyeetoo.com/products/canmv-k230-kendryte-k230-risc-v64-board
fetched_at: '2026-07-02T10:00:57.613767+00:00'
type: benchmark_result
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 11
---

# Kendryte K230 Neural Network Benchmarks

This page summarizes reported neural network inference throughput for the Kendryte K230 SoC as deployed on the CanMV-K230 development board. The measurements were performed using INT8 quantization on the integrated KPU (neural processing unit) and are sourced from the product specification page. Three common deep learning networks were benchmarked: Resnet50 achieved at least 85 frames per second (fps), Mobilenet_v2 achieved at least 670 fps, and YoloV5S achieved at least 38 fps. These results are classified as reported evidence, as they come from a vendor specification rather than an independent third-party evaluation. The benchmarks provide a baseline for comparing the KPU's performance on image classification and object detection workloads typical of edge AI applications.

## Key Claims

- Resnet50 (INT8): ≥85 fps.
- Mobilenet_v2 (INT8): ≥670 fps.
- YoloV5S (INT8): ≥38 fps.
- All measurements performed on Kendryte K230 KPU with INT8 quantization.

## Measurement Context

- Hardware version: Kendryte K230 (dual-core RISC-V, KPU).
- Software/toolchain version: Not explicitly specified; compatible with TVM, TensorFlow, PyTorch, ONNX for model conversion.
- Workload shape: Standard Resnet50, Mobilenet_v2, and YoloV5S network architectures; input dimensions not specified.
- Metric: Throughput in frames per second (fps).
- Method: Typical network performance reported on product specification page, not independently verified.
- Evidence strength: reported.

## Relationships

- [[kendryte-k230]]: The hardware target on which these benchmarks were measured.
- [[xuantie-c950]]: A higher-performance RISC-V SoC with different benchmark metrics (SPECint2006); comparison may highlight trade-offs between general-purpose CPU and dedicated NPU performance.
- [[sifive-intelligence-x160-gen-2]]: Another RISC-V AI core; its vector and DSP capabilities provide context for contrasting KPU-based inference.

## Sources

- [Youyeetoo CanMV-K230 product page](https://www.youyeetoo.com/products/canmv-k230-kendryte-k230-risc-v64-board)
