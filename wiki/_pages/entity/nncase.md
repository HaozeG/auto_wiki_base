---
canonical_name: nncase
aliases:
- Kendryte nncase
- kendryte/nncase
subtype: null
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.7
  self_containedness: 0.8
  bridge_score: 0.7
  hub_potential: 0.8
sources:
- raw/cache/5f54c2e0a3d7f793.md
- https://github.com/kendryte/nncase
source_url: https://github.com/kendryte/nncase
fetched_at: '2026-07-02T10:01:41.997251+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 10
---

# nncase

nncase is an open-source neural network compiler stack developed by Kendryte (a Canaan brand) for RISC-V AI accelerators. It converts models from popular frameworks such as TensorFlow Lite, Caffe, and ONNX into optimized executables for AI inference on edge devices. The project provides Python packages (pip install nncase nncase-kpu) for Linux and Windows, and includes extensive documentation covering operator support, usage guides, and a version relationship table linking nncase releases to the K230 SDK. Benchmark results published in the repository demonstrate competitive inference throughput—for example, 600 FPS on MobileNetV2 and 86 FPS on ResNet50V2—with minimal accuracy loss against the original model inference on ImageNet.

## Key Claims

- Supports TFLite, Caffe, and ONNX model formats.
- Compiles neural network models for RISC-V AI accelerators, specifically the K230.
- Provides pip-installable Python packages for Linux and Windows.
- Includes a benchmark suite with measured FPS and accuracy for common computer vision models (MobileNetV2, ResNet50V2, YOLOv5s, YOLOv8 variants) on the K230 platform.
- Achieves up to 600 FPS on MobileNetV2 (224x224) and 86 FPS on ResNet50V2 (3x224x224) with u8 quantization.
- Maintains accuracy within 0.3% of original model inference on ImageNet validation set.

## Relationships

- [[gemmini]]: Both nncase and Gemmini target efficient AI inference acceleration, though Gemmini is a hardware generator and nncase is a compiler stack.
- [[xuantie-c950]]: As a benchmark for RISC-V AI chips, the XuanTie C950 represents a server-class target; nncase could potentially be used with such chips in the future, as it is designed for RISC-V accelerators.
- Insufficient context for additional cross-links; no existing entity pages for K230 or other Kendryte tools in the wiki.

## Sources

- [GitHub README: kendryte/nncase](https://github.com/kendryte/nncase)
