---
canonical_name: YOLO26 RKNN on Rockchip RK3588
aliases:
- YOLO26 RKNN Radxa Rock 5B benchmarks
- YOLO26 RK3588 RKNN performance
subtype: null
tags: []
hardware_targets:
- Rockchip RK3588
workloads:
- YOLO26n
- YOLO26s
- YOLO26m
- YOLO26l
- YOLO26x
datatypes:
- FP16
metrics:
- model size (MB)
- mAP50-95(B)
- inference time (ms/im)
toolchains:
- Ultralytics YOLO 8.4.23
- rknn
hardware_versions:
- Radxa Rock 5B (Rockchip RK3588)
software_versions:
- ultralytics 8.4.23
- rknn-toolkit2 (version not specified)
measurement_method: Benchmarks were run by Ultralytics team on Radxa Rock 5B with
  RKNN format, using COCO128 validation dataset. Inference time does not include pre/post-processing.
evidence_strength: measured
scorecard:
  novelty_delta: 0.9
  claim_density: 0.9
  self_containedness: 0.9
  bridge_score: 0.8
  hub_potential: 0.7
sources:
- raw/cache/4b7115f77243bab6.md
- https://docs.ultralytics.com/integrations/rockchip-rknn
source_url: https://docs.ultralytics.com/integrations/rockchip-rknn
fetched_at: '2026-07-02T07:18:28.238392+00:00'
type: benchmark_result
created: '2026-07-02'
updated: '2026-07-02'
cold_start: false
inbound_links: 1
needs_summary_revision: false
---

# YOLO26 RKNN on Rockchip RK3588

The Ultralytics team benchmarked five YOLO26 model variants (YOLO26n through YOLO26x) on a Radxa Rock 5B development board powered by the Rockchip RK3588 SoC, using the RKNN model format. The models were exported with FP16 precision (default for RK3588) and evaluated on the COCO128 dataset to measure model size, mean average precision (mAP50-95(B)), and inference latency. The measurements were conducted with ultralytics version 8.4.23; inference time reported excludes image pre-processing and post-processing overhead. These benchmark results demonstrate the performance trade-offs between model size, accuracy, and speed when deploying YOLO26 on Rockchip NPU hardware, providing a reference for selecting the appropriate variant for edge AI applications.

## Key Claims

- YOLO26n: size 7.1 MB, mAP50-95(B) 0.479, inference time 65.7 ms/im.
- YOLO26s: size 20.9 MB, mAP50-95(B) 0.571, inference time 99.2 ms/im.
- YOLO26m: size 42.5 MB, mAP50-95(B) 0.610, inference time 235.3 ms/im.
- YOLO26l: size 52.1 MB, mAP50-95(B) 0.630, inference time 280.5 ms/im.
- YOLO26x: size 112.2 MB, mAP50-95(B) 0.666, inference time 669.1 ms/im.
- All models were exported to RKNN format and inferenced on Radxa Rock 5B (RK3588) with ultralytics 8.4.23.
- Validation dataset: COCO128; inference time excludes pre/post-processing.

## Measurement Context

- **Hardware version:** Radxa Rock 5B (Rockchip RK3588).
- **Software/toolchain version:** ultralytics 8.4.23; rknn-toolkit2 (version not specified).
- **Workload shape:** YOLO26 detection models with input size 640 (default).
- **Metric:** model size (MB), mAP50-95(B), inference time (ms/im).
- **Method:** Benchmarked by Ultralytics team using COCO128 dataset; time excludes pre/post-processing.
- **Evidence strength:** measured (directly reported by the development team).

## Relationships

- The hardware platform is documented on [[rockchip_rk3588]].
- The model export recipe used to generate these benchmarks is described in [[yolo26_rknn_export]].
- Comparable benchmark results on other NPU platforms include [[k230]] (YOLOv5S performance) and [[allwinner_v853]] (NPU inference).

## Sources

- https://docs.ultralytics.com/integrations/rockchip-rknn
