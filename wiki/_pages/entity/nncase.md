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
updated: '2026-07-03'
cold_start: true
inbound_links: 0
---

# nncase

nncase is an open-source neural network compiler developed by Kendryte (Canaan Inc.) for AI accelerators, specifically targeting the Kendryte K230 RISC-V SoC. It takes models trained in frameworks such as TensorFlow Lite, Caffe, and ONNX and compiles them into optimized inference code for the K230 platform, which features a dual-core RISC-V CPU with a neural processing unit (NPU). The compiler supports a range of operator sets from TFLite, Caffe, and ONNX, enabling deployment of image classification, object detection, segmentation, and pose estimation models. nncase is distributed via pip as the `nncase` and `nncase-kpu` packages and provides command-line tools for model conversion and compilation. The project includes benchmark results on the K230 platform demonstrating real-time inference performance on models like MobileNetV2, ResNet50V2, YOLOv5s, YOLOv8s, and YOLOv8n-pose, with FPS and accuracy comparisons against TFLite and ONNX runtimes. nncase is a key software component in the K230 SDK and is essential for deploying AI applications on Kendryte’s hardware.

## Key Claims

- nncase is a neural network compiler for AI accelerators, supporting TFLite, Caffe, and ONNX models.
- Supports operator sets for TFLite, Caffe, and ONNX (via separate documentation pages).
- Provides installation via pip on Linux (pip install nncase nncase-kpu) and Windows (pip install nncase plus manual whl for nncase-kpu).
- Delivers inference performance on K230: 
  - MobileNetV2 (1,224,224,3): 600.24 FPS, top-1 accuracy 71.1% vs TFLite 71.3%.
  - ResNet50V2 (1,3,224,224): 86.17 FPS, top-1 accuracy 75.11% vs ONNX 75.44%.
  - YOLOv5s_det (1,3,640,640): 23.645 FPS, mAP50-90 0.369 vs ONNX 0.374.
  - YOLOv8s_seg (1,3,640,640): 7.845 FPS, segmentation mAP50-90 0.371 vs ONNX 0.371.
- Benchmarks use ImageNet 2012 (50,000 images) and COCO val2017 (5,000 images for detection/segmentation, 2,346 for pose) as validation datasets.
- Accuracy of nncase-compiled models closely matches the reference TFLite/ONNX runtimes: within 0.5% for most measured metrics.

## Relationships

No specific relationship to visible context pages.

## Sources

- https://github.com/kendryte/nncase
