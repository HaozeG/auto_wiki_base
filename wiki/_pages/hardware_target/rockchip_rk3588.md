---
canonical_name: Rockchip RK3588
aliases:
- RK3588
- Rockchip RK3588 SoC
- Radxa Rock 5B
subtype: null
tags: []
hardware_targets:
- Rockchip RK3588
- Rockchip RK3566
- Rockchip RK3576
- Rockchip RK3568
- Rockchip RK3562
- Rockchip RK2118
- Rockchip RV1126B
- Rockchip RV1103
- Rockchip RV1106
- Rockchip RV1103B
- Rockchip RV1106B
toolchains:
- rknn-toolkit2
- Ultralytics YOLO
constraints:
- ARM-based architecture
- Built-in Neural Processing Unit (NPU)
- FP16 and INT8 quantization support via RKNN format
- Requires x86 Linux for model export (RKNN toolkit)
- ARM64 devices run inference only
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
type: hardware_target
created: '2026-07-02'
updated: '2026-07-02'
cold_start: false
inbound_links: 2
needs_summary_revision: false
---

# Rockchip RK3588

The Rockchip RK3588 is a flagship system-on-chip (SoC) designed by Rockchip for embedded and edge AI applications, featuring an ARM-based architecture with a built-in Neural Processing Unit (NPU) optimized for deep learning inference. The SoC is manufactured with advanced process technology and supports a range of compute-intensive tasks including computer vision, object detection, and multimedia processing. The RK3588 is the primary target used in the Radxa Rock 5B development board, where it has been validated for running Ultralytics YOLO26 models via the RKNN export format. Key features include support for both FP16 and INT8 quantization through the Rockchip Neural Network (RKNN) toolkit, enabling efficient deployment on edge devices with low latency and power consumption. The RK3588 is part of a broader Rockchip family that includes models such as the RK3566, RK3576, and entry-level RV1103/RV1106 series, which share the RKNN ecosystem but vary in NPU capability (FP16-capable vs. INT8-only).

## Key Claims

- ARM-based architecture with integrated NPU for AI acceleration.
- Supported by RKNN toolkit for model export and deployment; tested on Radxa Rock 5B (RK3588) and Radxa Zero 3W (RK3566).
- FP16-capable targets: RK3588, RK3576, RK3566, RK3568, RK3562, RK2118, RV1126B.
- INT8-only targets: RV1103, RV1106, RV1103B, RV1106B.
- Model export must be performed on an x86 Linux machine; inference runs on ARM64 Rockchip devices.
- RKNN format minimizes inference latency and power consumption by leveraging the NPU.

## Optimization-Relevant Details

- **ISA/profile:** ARM architecture (specific core microarchitecture not documented in source).
- **Vector/matrix/accelerator support:** Integrated NPU for AI tasks; RKNN runtime offloads operations to NPU.
- **Memory/cache/TLB/DMA:** Not detailed in the source; standard Rockchip memory hierarchy (assumed).
- **Compiler/toolchain support:** rknn-toolkit2 for model conversion (supports FP16 and INT8); Ultralytics YOLO Python API for model loading and inference.

## Relationships

- The Rockchip RK3588 is a hardware target for the [[yolo26_rknn_export]] optimization recipe, which details how to convert and deploy YOLO26 models.
- Benchmark results for YOLO26 models on this platform are recorded in [[yolo26_rknn_rockchip_rk3588_benchmark]].
- Comparable AI SoCs include the [[k230]] (Canaan Kendryte K230) and [[allwinner_v853]], both of which integrate NPUs for edge AI but differ in architecture (RISC-V vs. ARM) and toolchain ecosystems.

## Sources

- https://docs.ultralytics.com/integrations/rockchip-rknn
