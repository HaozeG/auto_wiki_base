---
cold_start: true
created: '2026-07-02'
datatypes:
- FP32
- FP16
- INT8
evidence_strength: measured
hardware_targets:
- Jetson Orin Nano (8GB)
hardware_versions:
- Jetson Orin Nano 8GB
inbound_links: 0
measurement_method: Benchmark function from ultralytics.utils.benchmarks with model='yolov8n.pt',
  data='coco8.yaml', imgsz=640, device=0. FP32/FP16/INT8 configurations were tested
  by setting the `int8` parameter.
metrics:
- inference time
- model size
- mAP50-95
needs_summary_revision: false
scorecard:
  bridge_score: 0.7
  claim_density: 0.8
  hub_potential: 0.6
  novelty_delta: 0.9
  self_containedness: 0.8
software_versions:
- JetPack 5.1.2
- TensorRT 8.5.2
sources:
- https://forums.developer.nvidia.com/t/benchmarck-int8-similar-to-fp32-on-yolov8-from-ultralytics/276023
tags:
- yolo
- yolov8
- tensorrt
- ultralytics
- jetson orin nano
- int8 quantization
toolchains:
- Ultralytics
- TensorRT 8.5.2
- PyTorch with CUDA
- JetPack 5.1.2
type: benchmark_result
updated: '2026-06-28'
workloads:
- YOLOv8n inference (ultralytics)
---

# Jetson Orin Nano YOLOv8n INT8 vs FP32 Benchmark

This benchmark result reports the inference performance of a YOLOv8n model from Ultralytics on a Jetson Orin Nano 8GB developer kit running JetPack 5.1.2 with TensorRT 8.5.2 and PyTorch with CUDA. The model was benchmarked using the Ultralytics benchmark utility at 640x640 input size on the COCO8 dataset. The FP32 configuration achieved an inference time of 12.63 ms per image with a model size of 13.6 MB and mAP50-95 of 0.6117. The FP16 configuration was approximately half the latency at 7.04 ms with a smaller model size (8.2 MB) and similar accuracy (mAP50-95 0.6092). The key finding is that the INT8 configuration produced inference times (12.61 ms) nearly identical to FP32, with the same mAP50-95 (0.6117) and a model size of 13.5 MB, indicating that INT8 quantization did not provide a speedup on this platform for this workload.

## Key Claims

- FP32 inference time: 12.63 ms, model size 13.6 MB, mAP50-95 0.6117.
- FP16 inference time: 7.04 ms, model size 8.2 MB, mAP50-95 0.6092.
- INT8 inference time: 12.61 ms, model size 13.5 MB, mAP50-95 0.6117.
- INT8 and FP32 show nearly identical performance on Jetson Orin Nano with YOLOv8n, possibly due to calibration issues or hardware support limitations.

## Measurement Context

- Hardware version: Jetson Orin Nano 8GB.
- Software/toolchain version: JetPack 5.1.2, TensorRT 8.5.2, PyTorch with CUDA, Ultralytics.
- Workload shape: YOLOv8n model, 640x640 input, COCO8 validation dataset.
- Metric: Inference time (ms per image), model size (MB), mAP50-95.
- Method: Automated benchmark from Ultralytics package; single run reported.
- Evidence strength: measured.

## Relationships

- [[Gemmini_Architecture]] – Another DNN accelerator architecture with INT8 support, but on a different platform (RISC-V based).
- [[llama-cpp_rtx3090_27b_benchmark]] – A benchmark result on a different NVIDIA GPU (RTX 3090) for LLM inference, demonstrating the range of NVIDIA hardware profiling.

## Sources

- [NVIDIA Developer Forums: Benchmark int8 similar to fp32 on yolov8 from ultralytics](https://forums.developer.nvidia.com/t/benchmarck-int8-similar-to-fp32-on-yolov8-from-ultralytics/276023)
