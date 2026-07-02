---
canonical_name: MobileNetV2 on Radxa A733 and T527 (Vivante VIP9000)
aliases:
- MobileNetV2 Radxa benchmark
- Radxa NPU MobileNetV2 inference
- MobileNetV2 on A733 and T527
subtype: null
tags:
- Radxa
- A733
- T527
- Vivante VIP9000
- MobileNetV2
- NPU
- inference
hardware_targets:
- Radxa A733
- Radxa T527
workloads:
- MobileNetV2 (224x224 input, ONNX model, post-training quantized to NBG format)
datatypes:
- FP32 (none-quant per driver output)
metrics:
- single-frame inference time (ms)
- FPS (frames per second)
- network creation time (ms)
- network prepare time (ms)
toolchains:
- gcc-arm-10.2-2020.11 (aarch64 cross-compiler)
- VIPLite driver v2.0.3.2-AW-2024-08-30 (A733)
- VIPLite driver v1.13.0.0-AW-2023-10-19 (T527)
- Pegasus toolchain (Docker-based model conversion)
hardware_versions:
- Radxa A733 (Vivante VIP9000 NPU)
- Radxa T527 (Vivante VIP9000 NPU)
software_versions:
- VIPLite driver 2.0.3.2 (A733)
- VIPLite driver 1.13.0.0 (T527)
- gcc-arm-10.2-2020.11
- Docker ubuntu-npu:v2.0.10.1 (A733) / ubuntu-npu:v1.8.11 (T527)
measurement_method: Single-frame inference using vendor demo application; inference
  time excludes pre-processing and post-processing overhead. Output captured from
  console logs.
evidence_strength: measured
scorecard:
  novelty_delta: 0.9
  claim_density: 0.5
  self_containedness: 0.8
  bridge_score: 0.6
  hub_potential: 0.3
sources:
- raw/cache/5f457818c9093dce.md
- https://docs.radxa.com/cubie/a5e/app-dev/npu-dev/model-zoo/mobilenetv2
source_url: https://docs.radxa.com/cubie/a5e/app-dev/npu-dev/model-zoo/mobilenetv2
fetched_at: '2026-07-02T07:15:53.365750+00:00'
type: benchmark_result
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# MobileNetV2 on Radxa A733 and T527 (Vivante VIP9000)

This benchmark result presents measured inference performance of the MobileNetV2 image classification model on the Radxa A733 and Radxa T527 single-board computers, both equipped with a Vivante VIP9000 NPU. The model, originally in ONNX format (mobilenetv2-12), is post-training quantized and compiled to a NBG file using the Pegasus toolchain within a Docker container. Inference is measured using the vendor-provided demo application, which reports network creation time, prepare time, and single-frame inference latency. On the Radxa A733 platform (VIPLite driver v2.0.3.2), the measured single-frame inference time is 2.028 ms, corresponding to 500 FPS. On the Radxa T527 platform (VIPLite driver v1.13.0.0), the inference time is 3.127 ms, corresponding to 322.6 FPS. These measurements exclude pre-processing and post-processing overhead. The hardware and software versions are documented as they appeared in the Radxa documentation at the time of capture.

## Key Claims

- Radxa A733 (Vivante VIP9000, VIPLite v2.0.3.2): MobileNetV2 (224x224) inference time 2.028 ms, 500 FPS.
- Radxa T527 (Vivante VIP9000, VIPLite v1.13.0.0): MobileNetV2 (224x224) inference time 3.127 ms, 322.6 FPS.
- Network creation time: 6.194 ms (A733), 6.479 ms (T527).
- Network prepare time: 1.502 ms (A733), 1.872 ms (T527).
- Total per-frame overhead (including creation and prepare) is higher than inference-only, but those are one-time costs.
- Measurements taken without pre/post processing, as stated in the source documentation.

## Measurement Context

- Hardware version:
  - Radxa A733 with Vivante VIP9000 NPU
  - Radxa T527 with Vivante VIP9000 NPU
- Software/toolchain version:
  - A733: VIPLite driver v2.0.3.2-AW-2024-08-30, Docker ubuntu-npu:v2.0.10.1
  - T527: VIPLite driver v1.13.0.0-AW-2023-10-19, Docker ubuntu-npu:v1.8.11
  - Cross-compiler: gcc-arm-10.2-2020.11 (aarch64)
- Workload shape:
  - MobileNetV2 ONNX model (mobilenetv2-12), input 224×224×3, output 1000 classes
  - Post-training quantized and converted to NBG format (mobilenetv2-12_pcq_a733.nb / mobilenetv2-12_pcq_t527.nb)
  - FP32 data format reported by driver (no quantization applied to input)
- Metric:
  - Single-frame inference time (measured from demo application run loop, excluding pre/post processing)
  - FPS derived as 1 / (inference time in seconds)
- Method:
  - Model compiled using Pegasus conversion scripts inside Docker container
  - Demo application executed on target board, output captured from stdout
  - Single loop count (loop_count=1)
  - Timing covers only the inference call, not network creation or preparation
- Evidence strength: measured

## Relationships

- The Vivante VIP9000 NPU used in these Radxa boards is a deep learning accelerator distinct from the RISC-V vector engines found in [[sifive_performance_p570_gen3]] and [[coral_npu_vector_execution_engine]], which also target AI workloads but use different ISA paradigms.
- This benchmark provides a data point for the MobileNetV2 workload, which could be compared with future [[workload_kernel]] pages for MobileNetV2 on other hardware.
- No existing wiki pages cover Radxa A733, Radxa T527, or the Vivante VIP9000; this page fills a gap for ARM‑based NPU inference benchmarks.

## Sources

- https://docs.radxa.com/cubie/a5e/app-dev/npu-dev/model-zoo/mobilenetv2
