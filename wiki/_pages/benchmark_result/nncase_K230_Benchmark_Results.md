---
cold_start: true
created: '2025-03-04'
datatypes:
- u8
evidence_strength: measured
hardware_targets:
- K230
hardware_versions: []
inbound_links: 0
measurement_method: 'Models compiled with nncase v2.x and run on K230. Quantization:
  u8 for weights and activations. Datasets and model versions as specified per row.
  Reference results from TFLite/ONNX runtime.'
metrics:
- fps
- accuracy
- mAP50-95
- mAP50
- mAP75
scorecard:
  bridge_score: 0.6
  claim_density: 0.8
  hub_potential: 0.5
  novelty_delta: 0.9
  self_containedness: 0.8
software_versions: []
sources:
- https://github.com/kendryte/nncase
tags:
- nncase
- K230
- neural network compiler
- benchmark
toolchains:
- nncase
- TFLite
type: benchmark_result
updated: '2026-06-29'
workloads:
- mobilenetv2
- resnet50v2
- yolov8s_cls
- yolov5s_det
- yolov8s_det
- yolov8s_seg
- yolov8n_pose_320
- yolov8n_pose_640
- yolov8s_pose
---

# nncase K230 Benchmark Results

Benchmark results for nncase, the open deep learning compiler stack for Kendryte AI accelerators, tested on the K230 SoC. The benchmark suite includes image classification (MobileNetV2, ResNet50V2, YOLOv8s_cls), object detection (YOLOv5s_det, YOLOv8s_det), image segmentation (YOLOv8s_seg), and pose estimation (YOLOv8n_pose at 320 and 640 input sizes, YOLOv8s_pose). All models are quantized to u8 (weights and activations) and compiled with nncase. Frames per second (fps) and accuracy metrics (top-1/top-5 for classification, mAP for detection/segmentation/pose) are reported against reference results from TFLite or ONNX runtime on the same datasets. These results provide quantitative evidence for the nncase compiler's performance on K230.

## Key Claims

- **MobileNetV2 (1,224,224,3):** 600.24 fps, top-1 accuracy 71.1% (ref: 71.3%), top-5 accuracy 90.0% (ref: 90.1%). Dataset: ImageNet 2012 (50,000 images).
- **ResNet50V2 (1,3,224,224):** 86.17 fps, top-1 accuracy 75.11% (ref: 75.44%), top-5 accuracy 92.36% (ref: 92.56%). Dataset: ImageNet 2012.
- **YOLOv8s_cls (1,3,224,224):** 130.497 fps, top-1 accuracy 72.2% (ref: 72.2%), top-5 accuracy 90.8% (ref: 90.9%). Dataset: ImageNet 2012.
- **YOLOv5s_det (1,3,640,640):** 23.645 fps, mAP50-90 0.369 (ref: 0.374), mAP50 0.566 (ref: 0.567). Dataset: COCO val2017 (5,000 images). Model version: v7.0 tag.
- **YOLOv8s_det (1,3,640,640):** 9.373 fps, mAP50-90 0.404 (ref: 0.446), mAP50 0.593 (ref: 0.612), mAP75 0.45 (ref: 0.484). Dataset: COCO val2017.
- **YOLOv8s_seg (1,3,640,640):** 7.845 fps, bbox mAP50-90 0.444 (ref: 0.444), segm mAP50-90 0.371 (ref: 0.371). Dataset: COCO val2017.
- **YOLOv8n_pose_320 (1,3,320,320):** 36.066 fps, bbox mAP50-90 0.6 (ref: 0.6), keypoints mAP50-90 0.359 (ref: 0.358). Dataset: COCO val2017 (2,346 images).
- **YOLOv8n_pose_640 (1,3,640,640):** 10.88 fps, bbox mAP50-90 0.694 (ref: 0.694), keypoints mAP50-90 0.508 (ref: 0.509). Dataset: COCO val2017.
- **YOLOv8s_pose (1,3,640,640):** 5.568 fps, bbox mAP50-90 0.734 (ref: 0.733), keypoints mAP50-90 0.604 (ref: 0.605). Dataset: COCO val2017.

## Measurement Context

- **Hardware version:** K230 (RISC-V SoC with KPU). No specific chip revision or clock frequency provided.
- **Software/toolchain version:** nncase v2.x (from GitHub releases), pip-installed on Linux. Reference results from TFLite (for classification models with TFLite op support) and ONNX runtime (for detection/segmentation/pose models).
- **Workload shape:** As specified per model: input shapes vary (224x224, 640x640, 320x320) with batch size 1.
- **Metric:** Frames per second (fps), top-1/top-5 accuracy for classification, mAP50-90, mAP50, mAP75 for detection/segmentation, and keypoints mAP for pose estimation.
- **Method:** Models compiled by nncase and executed on K230. Fps measured as (time per frame)^-1. Accuracy evaluated on full validation sets (ImageNet 2012: 50,000 images; COCO val2017: 5,000 or 2,346 images as indicated). Reference results from TFLite or ONNX runtime on the same hardware configuration (presumably on a PC, not K230).
- **Evidence strength:** measured. The numbers are sourced from the nncase GitHub repository and are claimed as official benchmark results.

## Relationships

- [[DSC_Fused_Dataflow_Benchmark_Results]] – Another benchmark result page for a different RISC-V AI accelerator technique (DSC fused dataflow), providing contrast with the nncase compiler approach on K230.

## Sources

- https://github.com/kendryte/nncase (GitHub README, benchmark table section)
