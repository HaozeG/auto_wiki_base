---
cold_start: false
created: '2026-06-27'
datatypes:
- quantized int8
evidence_strength: measured
hardware_targets:
- greenwaves_gap9
hardware_versions:
- GAP9 MCU (22nm FD-SOI)
inbound_links: 0
measurement_method: Real-time measurement on custom smart glasses prototype with GAP9
  MCU, 154mAh battery, OV5642 camera; latency measured as inference start to detection
  output; power measured across entire system (camera, MCU, wireless module).
metrics:
- inference latency (ms)
- energy per inference (mJ)
- end-to-end latency (ms)
- frames per second (FPS)
- system power (mW)
- battery runtime (hours)
needs_summary_revision: false
scorecard:
  bridge_score: 0.8
  claim_density: 1.0
  hub_potential: 0.7
  novelty_delta: 1.0
  self_containedness: 0.9
software_versions:
- TinyissimoYOLO v3 (paper version)
sources:
- https://arxiv.org/html/2311.01057v3
tags:
- object-detection
- yolo
- smart-glasses
- tinyissimoyolo
- gap9
- greenwaves
toolchains:
- GAPflow SDK
- AutoTiler
- NNTool
type: benchmark_result
updated: '2026-06-28'
workloads:
- TinyissimoYOLO object detection on MS-COCO (80 classes)
---

# TinyissimoYOLO Object Detection Benchmark on GAP9 Smart Glasses

This benchmark measures the inference and end-to-end performance of the TinyissimoYOLO object detection network deployed on a custom smart glasses prototype built around the Greenwaves GAP9 multi-core RISC-V MCU. The network is a sub-million parameter quantized YOLO architecture capable of detecting up to 80 classes from the MS-COCO dataset with a memory footprint below 1MB. Evaluation was conducted on actual hardware: the GAP9 MCU integrated with a low-power camera and wireless module in a glasses form factor powered by a 154mAh battery. The benchmark demonstrates state-of-the-art energy efficiency for on-device object detection on a microcontroller-class platform.

## Key Claims

- TinyissimoYOLO achieved an inference latency of 17ms and energy consumption of 1.59mJ per inference on the GAP9-based smart glasses prototype.
- The end-to-end pipeline from image capture through object detection post-processing ran at 56ms per frame, corresponding to 18 FPS.
- Total system power during continuous inference was measured at 62.9mW, including camera, MCU, and wireless subsystems.
- The prototype ran continuously for 9.3 hours on a 154mAh battery.
- TinyissimoYOLO can differentiate up to 80 classes on MS-COCO while fitting within 1MB memory.
- The system outperforms MCUNet (TinyNAS+TinyEngine) which runs a simpler image classification task at only 7.3 FPS on comparable hardware.

## Measurement Context

- Hardware version: GAP9 MCU (Greenwaves Technologies) integrated into custom smart glasses prototype with 154mAh battery.
- Software/toolchain version: TinyissimoYOLO open-source code (github.com/ETH-PBL/TinyissimoYOLO); GAPflow SDK for model deployment.
- Workload shape: Object detection using TinyissimoYOLO family on MS-COCO dataset, 80 output classes, sub-million parameters, quantized weights.
- Metric: Inference latency (17ms), energy per inference (1.59mJ), end-to-end latency (56ms), throughput (18 FPS), system power (62.9mW), battery runtime (9.3 hours).
- Method: Real-time measurement on hardware prototype; inference latency measured as single-shot detection time on GAP9; end-to-end includes image capture from OV5642 camera, DMA transfer, inference, and software post-processing with corner detection; power measured as average consumption over a 60-second inference window using bench power supply current monitoring.
- Evidence strength: measured.

## Relationships

- [[greenwaves_gap9]]: This benchmark directly evaluates the GAP9 MCU performance for object detection workloads.
- [[tvm_riscv_backend]]: The TVM RISC-V backend can be used to compile and optimize models for GAP9-like RISC-V targets; future comparisons between TVM-optimized kernels and the proprietary GAPflow deployment may reveal optimization opportunities.

## Sources

- https://arxiv.org/html/2311.01057v3 — Ultra-Efficient On-Device Object Detection on AI-Integrated Smart Glasses With TinyissimoYOLO
