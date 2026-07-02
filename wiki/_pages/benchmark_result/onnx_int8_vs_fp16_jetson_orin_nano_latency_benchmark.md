---
canonical_name: ONNX INT8 vs FP16 Latency on Jetson Orin Nano
aliases:
- Jetson Orin Nano ONNX INT8 FP16 latency comparison
- TildAlice ONNX INT8 FP16 benchmark
subtype: null
tags: []
hardware_targets:
- NVIDIA Jetson Orin Nano
workloads:
- YOLOv8n object detection inference
datatypes:
- INT8
- FP16
metrics:
- latency (ms)
- mAP (%)
toolchains:
- ONNX Runtime
hardware_versions:
- Jetson Orin Nano (15W, 1024 CUDA cores, 32 Tensor Cores)
software_versions: []
measurement_method: Standard inference latency measurement on Jetson Orin Nano using
  ONNX Runtime; exact methodology not specified.
evidence_strength: reported
scorecard:
  novelty_delta: 0.9
  claim_density: 0.7
  self_containedness: 0.8
  bridge_score: 0.5
  hub_potential: 0.3
sources:
- raw/cache/334bbd19999f96ee.md
- https://tildalice.io/onnx-int8-vs-fp16-jetson-orin-nano-latency-benchmark/
source_url: https://tildalice.io/onnx-int8-vs-fp16-jetson-orin-nano-latency-benchmark/
fetched_at: '2026-07-02T06:24:23.706287+00:00'
type: benchmark_result
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# ONNX INT8 vs FP16 Latency on Jetson Orin Nano

The NVIDIA Jetson Orin Nano is an edge AI computing platform featuring 1024 CUDA cores and 32 Tensor Cores within a 15W thermal design power envelope, targeting low-power AI inference at the edge. This benchmark result compares the inference latency and accuracy tradeoff for YOLOv8n object detection when using ONNX Runtime with INT8 quantization versus FP16 half-precision. On the Jetson Orin Nano, the INT8 quantized model achieves a 3x latency reduction from 47 milliseconds to 15 milliseconds compared to the FP16 variant, a significant improvement for real-time applications. However, this speedup comes at the cost of a 5.7 percentage point drop in mean average precision (mAP) for small objects, highlighting a classic tradeoff between inference speed and detection accuracy. The benchmark results are reported from the TildAlice blog and represent practical deployment considerations for edge AI systems.

## Key Claims

- YOLOv8n INT8 reduces inference latency from 47 ms to 15 ms (3x improvement) on the Jetson Orin Nano compared to FP16.
- Small-object mAP decreases by 5.7 percentage points when using INT8 quantization versus FP16.
- The Jetson Orin Nano hardware includes 1024 CUDA cores, 32 Tensor Cores, and a 15W TDP.
- The benchmark measurements originate from the TildAlice blog, providing real-world tradeoff data for edge AI deployment.

## Measurement Context

- Hardware version: NVIDIA Jetson Orin Nano (15W, 1024 CUDA cores, 32 Tensor Cores)
- Software/toolchain version: ONNX Runtime (exact version not specified)
- Workload shape: YOLOv8n object detection inference (model source and input resolution not specified)
- Metric: Inference latency (ms), small-object mean average precision (mAP, %)
- Method: Standard latency measurement using ONNX Runtime; exact measurement methodology and number of runs not disclosed
- Evidence strength: reported (from a blog post)

## Relationships

- [[k230]]: A RISC-V-based edge AI SoC with a dedicated KPU, serving as a competing platform for low-power AI inference; comparison of latency and accuracy profiles between the Jetson Orin Nano and the K230 could inform hardware selection for edge deployments.
- [[llama_cpp]]: An LLM inference framework with support for multiple quantization formats and hardware backends; while focused on LLMs, it represents a parallel inference optimization approach that can be contrasted with the ONNX-based YOLOv8n benchmark on edge hardware.
- Insufficient context for additional cross-links: The wiki currently lacks pages for NVIDIA Jetson hardware, ONNX Runtime, or YOLOv8, limiting the direct relationship links.

## Sources

- https://tildalice.io/onnx-int8-vs-fp16-jetson-orin-nano-latency-benchmark/
