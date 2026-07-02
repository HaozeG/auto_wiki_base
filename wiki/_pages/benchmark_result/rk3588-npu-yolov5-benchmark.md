---
canonical_name: RK3588 NPU YOLOv5 Benchmark
aliases:
- YOLOv5 on RK3588 NPU
- 54 FPS RK3588 YOLOv5
subtype: null
tags: []
hardware_targets:
- Rockchip RK3588
workloads:
- YOLOv5
datatypes:
- INT8
metrics:
- FPS
toolchains:
- RKNN-Toolkit2
hardware_versions:
- Orange Pi 5 Max
software_versions:
- RKNN-Toolkit2
measurement_method: NPU inference benchmark via RKNN-Toolkit2
evidence_strength: reported
scorecard:
  novelty_delta: 0.8
  claim_density: 0.5
  self_containedness: 0.8
  bridge_score: 0.3
  hub_potential: 0.3
sources:
- raw/cache/2257e79ba149ffba.md
- https://tinycomputers.io/posts/rockchip-rk3588-npu-benchmarks.html
source_url: https://tinycomputers.io/posts/rockchip-rk3588-npu-benchmarks.html
fetched_at: '2026-07-02T11:09:04.630874+00:00'
type: benchmark_result
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# RK3588 NPU YOLOv5 Benchmark

The RK3588 NPU achieves 54+ frames per second (FPS) on the YOLOv5 object detection model using INT8 quantization via the RKNN-Toolkit2 software stack. This benchmark was reported from testing on the Orange Pi 5 Max single-board computer, which integrates the full RK3588 SoC. The result demonstrates the NPU's capability for real-time computer vision inference at the edge. The measurement is reported from the blog post "Rockchip RK3588 NPU Deep Dive: Real-World AI Performance ..." and corroborated by a separate source on accio.com. The evidence strength is classified as reported since the exact measurement methodology and per-run variability are not detailed.

## Key Claims

- YOLOv5 inference on the RK3588 NPU achieves 54+ FPS.
- Inference uses INT8 quantization and RKNN-Toolkit2.
- The benchmark is conducted on the Orange Pi 5 Max platform.

## Measurement Context

- Hardware version: Rockchip RK3588 NPU on Orange Pi 5 Max
- Software/toolchain version: RKNN-Toolkit2
- Workload shape: YOLOv5 (specific input size not specified)
- Metric: Frames per second (FPS)
- Method: NPU inference benchmark via RKNN-Toolkit2
- Evidence strength: reported

## Relationships

- [[gemmini]]: As a hardware accelerator, Gemmini represents a different approach to AI inference acceleration.
- [[nncase]]: Both target efficient AI inference, with nncase providing benchmarks on RISC-V platforms.
- Insufficient context for additional cross-links.

## Sources

- [Rockchip RK3588 NPU Deep Dive: Real-World AI Performance ...](https://tinycomputers.io/posts/rockchip-rk3588-npu-benchmarks.html)
- [RK3588 NPU Performance: What 6 TOPS Means for Industrial AI ...](https://accio.com)
