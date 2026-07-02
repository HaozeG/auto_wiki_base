---
canonical_name: nncase ResNet50V2 K230 Benchmark
aliases: []
subtype: null
hardware_targets:
- K230
workloads:
- ResNet50V2
datatypes:
- u8
metrics:
- FPS
- top-1 accuracy
- top-5 accuracy
toolchains:
- nncase
constraints: []
evidence_strength: reported
hardware_versions:
- K230
software_versions:
- nncase v2.x.x (refer to nncase release page)
measurement_method: ImageNet 2012 validation set (50000 images)
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
type: benchmark_result
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# nncase ResNet50V2 K230 Benchmark

The nncase ResNet50V2 benchmark result reports measured inference performance for the ONNX implementation of ResNet50V2 when compiled with nncase and executed on the Canaan K230 RISC-V AI accelerator. The model uses input shape [1,3,224,224] and uint8 quantization for both weights and activations (u8/u8). On the K230 platform, the compiled model achieves 86.17 frames per second (FPS) with a top-1 accuracy of 75.11% and top-5 accuracy of 92.36% on the ImageNet 2012 validation set (50,000 images). The reference TensorFlow Lite inference on equivalent hardware yields 75.44% top-1 and 92.56% top-5, indicating an accuracy degradation of less than 0.3% due to quantization. The measurement method is reported in the nncase GitHub README under the K230 benchmark test section.

## Key Claims

- ResNet50V2 with input [1,3,224,224] quantized to u8/u8 achieves 86.17 FPS on K230.
- Top-1 accuracy: 75.11% on ImageNet 2012 validation set.
- Top-5 accuracy: 92.36% on ImageNet 2012 validation set.
- Accuracy loss relative to TFLite reference is less than 0.3%.

## Measurement Context

- Hardware version: K230 (Canaan Kendryte)
- Software/toolchain version: nncase v2.x.x (exact version not specified in source)
- Workload shape: ResNet50V2, ONNX model, input [1,3,224,224], u8 quantization
- Metric: FPS, top-1 accuracy, top-5 accuracy
- Method: Inference on ImageNet 2012 validation set, 50000 images
- Evidence strength: reported (from project README)

## Relationships

- [[nncase]]: This benchmark result demonstrates the performance of the nncase compiler.
- [[xuantie-c950]]: As a high-performance RISC-V AI chip, the C950 offers a potential target for similar nncase-compiled models, though no direct benchmark is provided.

## Sources

- [GitHub README: kendryte/nncase, benchmark test table](https://github.com/kendryte/nncase)
