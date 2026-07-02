---
canonical_name: Intel Core Ultra 7 256V ResNet-50 OpenVINO Inference Benchmark
aliases:
- ResNet-50 OpenVINO benchmark on Intel Lunar Lake
- Intel Arc 140V ResNet-50 latency
- Intel AI Boost NPU INT8 performance
subtype: null
tags: []
hardware_targets:
- Intel Core Ultra 7 256V
- Intel Arc 140V GPU
- Intel AI Boost NPU
workloads:
- ResNet-50 image classification
datatypes:
- FP32
- INT8
metrics:
- latency (ms)
- speedup factor
toolchains:
- OpenVINO 2026.1
- NNCF
- PyTorch 2.11
- ONNX
hardware_versions:
- Intel Core Ultra 7 256V (Lunar Lake)
- Intel Arc 140V (8GB VRAM)
- Intel AI Boost NPU (built-in)
software_versions:
- OpenVINO 2026.1
- NNCF (bundled with OpenVINO)
- PyTorch 2.11
- Python 3.11
measurement_method: Single-run latency measurements using OpenVINO benchmark script
  on CPU, GPU, and NPU. Results are self-reported and not independently verified.
evidence_strength: reported
scorecard:
  novelty_delta: 0.9
  claim_density: 0.7
  self_containedness: 1.0
  bridge_score: 0.3
  hub_potential: 0.2
sources:
- raw/cache/770f1a913d100356.md
- https://github.com/laharipriyakakarla/resnet-openvino-inference
source_url: https://github.com/laharipriyakakarla/resnet-openvino-inference
fetched_at: '2026-07-02T10:56:40.328990+00:00'
type: benchmark_result
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# Intel Core Ultra 7 256V ResNet-50 OpenVINO Inference Benchmark

This page reports latency measurements for ResNet-50 image classification (1000-class ImageNet) inference on an Intel Lunar Lake platform using the OpenVINO 2026.1 toolkit. The hardware includes an Intel Core Ultra 7 256V CPU, an Intel Arc 140V GPU (8GB), and an integrated Intel AI Boost Neural Processing Unit (NPU). The model was converted from PyTorch through ONNX to OpenVINO IR format. Baseline FP32 latency was measured on each device, and then INT8 quantization was applied using the Neural Network Compression Framework (NNCF). Speedups from quantization were computed as the ratio of FP32 latency to INT8 latency. The results show that the CPU benefits most from INT8 quantization (4.06x speedup), the NPU achieves a moderate 1.88x speedup, while the GPU shows no benefit (0.84x slowdown), consistent with the Arc GPU's optimization for FP32 graphics workloads. The NPU's architecture for low-precision AI inference is highlighted. All measurements are self-reported by the project author and have not been independently verified, classifying the evidence strength as reported.

## Key Claims

- FP32 baseline latency: CPU 30.27 ms, GPU 3.18 ms, NPU 3.31 ms.
- GPU is approximately 10x faster than CPU for FP32 inference (3.18 ms vs 30.27 ms).
- After INT8 quantization, CPU latency improves from 54.50 ms to 13.41 ms (4.06x speedup).
- NPU latency improves from 3.45 ms to 1.83 ms (1.88x speedup).
- GPU INT8 latency is 2.43 ms versus 2.05 ms FP32 (0.84x slowdown), showing no benefit from INT8.
- The NPU benefits from INT8 due to its purpose-built low-precision AI inference design.
- Software stack: OpenVINO 2026.1, NNCF, PyTorch 2.11, Python 3.11.

## Measurement Context

- Hardware version: Intel Core Ultra 7 256V (Lunar Lake), Intel Arc 140V GPU (8GB), Intel AI Boost NPU (integrated).
- Software/toolchain version: OpenVINO 2026.1, NNCF, PyTorch 2.11, Python 3.11.
- Workload shape: ResNet-50 (standard ImageNet model, 1000 classes). Input dimensions not specified.
- Metric: Latency in milliseconds (ms), speedup factor.
- Method: Single-run measurements using project-provided Python scripts (resnet_demo.py for baseline, quantize_demo.py for INT8). Not independently verified.
- Evidence strength: reported.

## Relationships

- [[kendryte-k230-neural-network-benchmarks]]: Another benchmark using ResNet-50 with INT8 quantization on a RISC-V NPU, providing a cross-architecture comparison point for inference efficiency.
- [[tenstorrent-wormhole-galaxy-llama-70b-benchmark]]: A benchmark on a different architecture (Tenstorrent) with large language model workloads, illustrating the diversity of AI accelerator benchmarks in the wiki.
- [[llvm-riscv-fptrunc-narrowing-optimization]]: An optimization recipe for RISC-V floating-point performance; while not directly related, both resources contribute to the theme of optimizing neural network inference on varying hardware.

## Sources

- [GitHub repository: laharipriyakakarla/resnet-openvino-inference](https://github.com/laharipriyakakarla/resnet-openvino-inference)
