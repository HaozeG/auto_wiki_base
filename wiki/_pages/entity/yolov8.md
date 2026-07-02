---
canonical_name: YOLOv8
aliases:
- YOLO v8
- Ultralytics YOLOv8
- YOLOv8 model
subtype: null
tags:
- object detection
- computer vision
- YOLO
- real-time inference
scorecard:
  novelty_delta: 0.6
  claim_density: 0.3
  self_containedness: 0.6
  bridge_score: 0.5
  hub_potential: 0.7
sources:
- raw/cache/8f51424c0b19d248.md
- https://yolov8.org/what-is-yolov8/
source_url: https://yolov8.org/what-is-yolov8/
fetched_at: '2026-07-02T06:23:24.910469+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: false
inbound_links: 1
needs_summary_revision: false
---

# YOLOv8

YOLOv8 is the eighth major version of the YOLO (You Only Look Once) series of real-time object detection models, developed by Ultralytics. It is a state-of-the-art computer vision model that builds upon the success of previous YOLO versions, introducing new features and improvements for enhanced performance and flexibility. YOLOv8 maintains real-time inference capabilities even with increased accuracy, making it suitable for applications such as autonomous vehicles, surveillance systems, and robotics. The model is available in five sizes—nano (n), small (s), medium (m), large (l), and extra-large (x)—to accommodate different performance and resource constraints. As of the available information, YOLOv8 does not yet have a published research paper describing its architecture and ablation studies, limiting direct insight into its design trade-offs.

## Key Claims

- YOLOv8 is a real-time object detection model that achieves improved accuracy while maintaining real-time performance.
- It is offered in five model sizes: nano, small, medium, large, and extra-large.
- YOLOv8 has no published paper, restricting understanding of its research methodology and ablation studies.
- The model is a state-of-the-art (SOTA) developement from Ultralytics, building on earlier YOLO versions.

## Relationships

- [[xuantie_c908]]: a RISC-V AI accelerator core that can execute YOLOv8 inference workloads, leveraging vector extensions for convolutional operations.
- [[k230]]: a RISC-V SoC integrating the C908 core and a Knowledge Process Unit (KPU) capable of running YOLO-family models, relevant for YOLOv8 deployment on edge devices.
- [[llama_cpp]]: an inference library supporting GGML quantization and RVV instructions, potentially applicable to running YOLOv8 inference on RISC-V hardware.

## Sources

- https://yolov8.org/what-is-yolov8/
