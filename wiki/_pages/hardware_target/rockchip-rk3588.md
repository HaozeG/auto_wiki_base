---
canonical_name: Rockchip RK3588
aliases:
- RK3588
- RK3588 NPU
- Orange Pi 5 Max SoC
- RK3588 SoC
subtype: null
tags: []
hardware_targets:
- Rockchip RK3588
toolchains:
- RKNN-Toolkit2
constraints:
- 6 TOPS peak performance
- INT8/FP16 precision support
scorecard:
  novelty_delta: 0.8
  claim_density: 0.5
  self_containedness: 0.8
  bridge_score: 0.3
  hub_potential: 0.3
sources:
- raw/cache/2257e79ba149ffba.md
- https://tinycomputers.io/posts/rockchip-rk3588-npu-benchmarks.html
- raw/cache/77948476b4c60c66.md
- https://ieeker.com/rk3588-npu-performance-industrial-edge-ai/
- raw/cache/3125158825dd2707.md
- https://github.com/choushunn/awesome-RK3588
source_url: https://tinycomputers.io/posts/rockchip-rk3588-npu-benchmarks.html
fetched_at: '2026-07-02T11:09:04.630874+00:00'
type: hardware_target
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# Rockchip RK3588

The Rockchip RK3588 is an ARM-based system-on-chip (SoC) that integrates a neural processing unit (NPU) capable of delivering up to 6 TOPS of integer-8 (INT8) performance with support for mixed-precision INT8/FP16 computation. The NPU is designed for edge AI inference workloads, including computer vision and large language models, and is accessible through the RKNN-Toolkit2 software stack. The RK3588 NPU has been benchmarked on platforms such as the Orange Pi 5 Max, achieving over 54 frames per second on YOLOv5 object detection models. It is positioned as a competitive solution for industrial edge AI applications, leveraging its 6 TOPS performance as a balance between power efficiency and compute capability.

## Key Claims

- The RK3588 NPU delivers up to 6 TOPS peak performance at INT8 precision.
- Supports INT8 and FP16 precision for AI inference.
- Achieves 54+ FPS on YOLOv5 object detection benchmarks using RKNN-Toolkit2.
- Targeted at edge AI and computer vision applications.

## Optimization-Relevant Details

- ISA/profile: ARM (NPU is independent of CPU ISA)
- Vector/matrix/accelerator support: Dedicated NPU with 6 TOPS INT8/FP16
- Memory/cache/TLB/DMA: Not specified in available sources
- Compiler/toolchain support: RKNN-Toolkit2 for model conversion and quantization

## Relationships

- [[rk3588-npu-yolov5-benchmark]]: related via shared rk3588, rknn-toolkit2, rockchip rk3588.

- [[rknn-toolkit2]]: related via shared rockchip.

- [[gemmini]]: Both are hardware accelerators for AI, though Gemmini is a systolic array generator and the RK3588 NPU is a fixed-function NPU.
- [[nncase]]: Both have compiler stacks for neural network inference (RKNN-Toolkit2 vs nncase).
- Insufficient context for additional cross-links; no existing pages for ARM-based SoCs or RKNN-Toolkit2 are present in the wiki.

## Sources

- [Rockchip RK3588 NPU Deep Dive: Real-World AI Performance ...](https://tinycomputers.io/posts/rockchip-rk3588-npu-benchmarks.html)
- [RK3588 NPU: Edge AI Performance in 2026 - accio.com](https://accio.com)
