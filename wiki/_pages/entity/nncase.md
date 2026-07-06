---
canonical_name: nncase
aliases:
- Kendryte nncase
- nncase compiler
- kendryte/nncase
- K230 nncase
- nncase neural network compiler
subtype: null
tags: []
scorecard:
  novelty_delta: 0.8
  claim_density: 0.7
  self_containedness: 0.9
  bridge_score: 0.3
  hub_potential: 0.5
sources:
- raw/cache/5f54c2e0a3d7f793.md
- https://github.com/kendryte/nncase
- raw/cache/8a25a6210cad536f.md
- https://github.com/kendryte/k230_docs/blob/main/en/01_software/board/ai/K230_nncase_Development_Guide.md
- raw/cache/528ec419e451c3b3.md
- https://gitee.com/kendryte/nncase
source_url: https://github.com/kendryte/nncase
fetched_at: '2026-07-03T16:33:29.350822+00:00'
type: entity
created: '2026-07-03'
updated: '2026-07-06'
cold_start: true
inbound_links: 0
---

# nncase

nncase is an open-source neural network compiler (deep learning compiler stack) developed by Kendryte (a Canaan Creative / Canaan Inc. subsidiary) for AI accelerators. Licensed under Apache-2.0, it targets multiple platforms including CPU, K210, K510, and K230 RISC-V SoCs, with primary focus on the K230. It compiles models trained in frameworks such as TensorFlow Lite, Caffe, and ONNX into optimized kmodel files that can be executed on the supported hardware. The compiler provides static memory allocation (no heap memory required), operator fusion and optimization, and support for both float and uint8/int8 quantized inference (8-bit quantization for both weights and activations). Post-training quantization (PTQ) is supported using floating-point models and quantization calibration sets. The nncase software stack consists of a compiler component (running on a PC) and a runtime library that integrates into user applications to load models, set input data, execute KPU inference, and retrieve outputs. Distributed via pip as the `nncase` and `nncase-kpu` packages, nncase provides command-line tools for model conversion and compilation. The project includes benchmark results on the K230 platform demonstrating real-time inference performance on models like MobileNetV2, ResNet50V2, YOLOv5s, YOLOv8s, and YOLOv8n-pose, with FPS and accuracy comparisons against TFLite and ONNX runtimes. nncase is a key software component in the K230 SDK and is essential for deploying AI applications on Kendryte’s hardware. The repository maintains versioned releases with active development across multiple branches (release/3.0, release/2.0, and various feature branches) and documented version mappings between nncase releases and SDK versions.

## Key Claims

- nncase is a neural network compiler for AI accelerators, supporting TFLite, Caffe, and ONNX models with detailed operator support documented for each frontend.
- Supports multi-input multi-output networks and multi-branch structures.
- Static memory allocation, no heap memory required.
- Operator fusion and optimization.
- Supports float and uint8/int8 quantized inference (u8 for both input features and weights).
- Post-training quantization using floating-point models and calibration sets.
- Flat model format supporting zero-copy loading.
- Compiler modules include: Importer, IR (Neutral IR and Target IR), Evaluator, Quantize, Transform optimization, Tiling, Partition, Schedule, and Codegen.
- Runtime provides kmodel loading, input setting, KPU execution, and output retrieval.
- Currently supported targets: CPU, K210, K510, K230.
- Provides installation via pip on Linux (`pip install nncase nncase-kpu`) and Windows (`pip install nncase` plus manual whl for `nncase-kpu`).
- Integrated with the K230 SDK, with documented version mapping between nncase releases and SDK versions.
- Delivers inference performance on K230 with u8/u8 quantization:
  - MobileNetV2 (1,224,224,3): 600.24 FPS, top-1 accuracy 71.1% vs TFLite 71.3%.
  - ResNet50V2 (1,3,224,224): 86.17 FPS, top-1 accuracy 75.11% vs ONNX 75.44%.
  - YOLOv5s_det (1,3,640,640): 23.645 FPS, mAP50-90 0.369 vs ONNX 0.374.
  - YOLOv8s_det (1,3,640,640): 9.373 FPS (reference not provided).
  - YOLOv8s_seg (1,3,640,640): 7.845 FPS, segmentation mAP50-90 0.371 vs ONNX 0.371.
  - YOLOv8n_pose (1,3,320,320): 36.066 FPS (reference not provided).
- Benchmarks use ImageNet 2012 (50,000 images) and COCO val2017 (5,000 images for detection/segmentation, 2,346 for pose) as validation datasets.
- Accuracy of nncase-compiled models closely matches the reference TFLite/ONNX runtimes: within 0.5% for most measured metrics, and within 0.1–0.3% on ImageNet top-1.
- The repository has 246 branches and 77 tags, indicating active development.

## Relationships

No specific relationship to visible context pages.

## Sources

- https://github.com/kendryte/nncase
- https://github.com/kendryte/k230_docs/blob/main/en/01_software/board/ai/K230_nncase_Development_Guide.md
- https://gitee.com/kendryte/nncase
