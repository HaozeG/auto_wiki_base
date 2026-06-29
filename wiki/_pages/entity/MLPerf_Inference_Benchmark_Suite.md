---
cold_start: false
created: '2026-07-02'
inbound_links: 0
needs_summary_revision: false
scorecard:
  bridge_score: 0.8
  claim_density: 0.7
  hub_potential: 0.7
  novelty_delta: 0.8
  self_containedness: 1.0
sources:
- https://docs.mlcommons.org/inference/index_gh/
tags:
- MLPerf
- inference
- benchmark
- RISC-V AI accelerator
type: entity
updated: '2026-06-29'
---

# MLPerf® Inference Benchmark Suite

MLPerf Inference is a benchmark suite for measuring how fast systems can run machine learning models in a variety of deployment scenarios, including edge and datacenter environments. It provides a standardized framework for evaluating inference performance across diverse tasks such as image classification, object detection, natural language processing, recommendation, speech recognition, medical imaging, text-to-image, and text-to-video. The benchmark suite is defined by a committee of industry and academic partners and evolves through numbered rounds (e.g., v0.5 through v6.0), each introducing new models, datasets, and constraints. Submissions must follow strict rules regarding reference implementations, allowed frameworks, and measurement protocols. The suite is widely used to compare hardware and software stacks, including RISC-V AI accelerators, on a level playing field. The official MLPerf Inference documentation provides automated commands to run benchmarks using different implementations.

## Key Claims

- MLPerf Inference covers multiple model categories: vision (ResNet-50-v1.5, YOLO v11, RetinaNet, SSD-MobileNet, SSD-ResNet34), language (BERT, GPT-J, Llama2-70b, Llama3.1-405b, Mixtral-8x7b, DeepSeek-R1), recommendation (DLRM-v3, DLRM-v2), medical imaging (3D U-Net), speech (RNNT, Whisper), text-to-image (Stable Diffusion XL), graph (RGAT), automotive (PointPainting), and general language models (GPT-OSS, VLM).
- Benchmarks are categorized as edge or datacenter based on system class, with scenarios including offline, server, and single-stream.
- The suite has evolved from v0.5 (2019) to v6.0 (submission deadline February 13, 2026), with each round adding new models and refinements.
- Reference implementations are provided in frameworks such as TensorFlow, PyTorch, ONNX, TVM, and NCNN; submitters may use their own frameworks.
- Power measurements require SPEC PTD 1.10/1.11.1 and a dedicated power-dev repository.
- The benchmark is intended to drive innovation in inference performance across a wide range of hardware, including RISC-V-based AI accelerators.

## Relationships

- [[Chiplet_RISC_V_AI_SoC_Benchmark_Results]] – This benchmark result page uses MLPerf models ResNet-50 and MobileNetV2, demonstrating the application of the MLPerf Inference suite on a RISC-V SoC.
- [[DSC_Fused_Dataflow_Benchmark_Results]] – This benchmark result page uses Depthwise Separable Convolution, a core component of MobileNetV2 which is an MLPerf model, showing the relevance of MLPerf workloads to RISC-V accelerator evaluation.
- Insufficient context for additional cross-links to entity pages; the current wiki contains only benchmark_result, hardware_target, and optimization_recipe pages, not standalone entity pages.

## Sources

- [MLPerf Inference Documentation](https://docs.mlcommons.org/inference/index_gh/)
