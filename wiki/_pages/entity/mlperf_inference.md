---
canonical_name: MLPerf Inference
aliases:
- MLPerf Inference Benchmark Suite
- MLPerf Inference v6.0
- MLPerf Inference Benchmark
- MLPerf
- MLPerf Inference Benchmarks
subtype: null
scorecard:
  novelty_delta: 0.9
  claim_density: 0.9
  self_containedness: 1.0
  bridge_score: 0.8
  hub_potential: 0.8
sources:
- raw/cache/b891aaef874ab17a.md
- https://docs.mlcommons.org/inference/index_gh/
- raw/cache/52b8915814d8c477.md
- https://docs.mlcommons.org/inference/
source_url: https://docs.mlcommons.org/inference/index_gh/
fetched_at: '2026-07-17T10:03:30.801055+00:00'
type: entity
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 0
outbound_links:
- target: amd_cdna
  reason: MLPerf Inference is the standard benchmark suite used to evaluate inference
    performance of AMD CDNA-based Instinct accelerators in data center machine learning
    workloads
---

# MLPerf Inference

MLPerf Inference is a benchmark suite for measuring how fast systems can run models in a variety of deployment scenarios. It is part of the MLCommons consortium and provides standard benchmarks for evaluating inference performance across different hardware platforms, including edge and datacenter categories. The suite supports various models such as ResNet-50, BERT, DLRM, Llama 2, Llama 3.1, Mixtral, and many others, across frameworks like TensorFlow, PyTorch, ONNX, TVM, and NCCN. Each benchmark includes a reference implementation and specifies a dataset (e.g., ImageNet, SQuAD, COCO, OpenOrca, KiTS19). The benchmark suite has evolved through multiple versions, with the latest being v6.0 (submission deadline February 13, 2026), which added models such as YOLOv11, Wan2.2 text-to-video, and DeepSeek R1.

## Key Claims

- MLPerf Inference v6.0 includes benchmarks for vision (resnet50-v1.5, YOLOv11), language (BERT, Llama 2-70b, Llama 3.1-405b, Llama 3.1-8b, DeepSeek R1, Mixtral-8x7b), recommendation (DLRM-v3), medical imaging (3D-UNet), text-to-video (Wan2.2), text-to-image (Stable Diffusion XL), graph (RGAT), automotive (PointPainting), speech (Whisper), and VLM.
- Supported frameworks in reference implementations include TensorFlow, PyTorch, ONNX, TVM, and NCCN; submitters may use their own frameworks.
- The suite has been updated regularly: v1.1 (2021), v2.0, v2.1, v3.0, v3.1, v4.0, v4.1, v5.0, v5.1, v6.0 (2026).
- Power submissions for v6.0 require SPEC PTD 1.11.1.
- The benchmark suite is described in the MLPerf Inference benchmark paper (Reddi et al., 2019, arXiv:1911.02549).

## Relationships

- [[amd_cdna]]: MLPerf Inference is the standard benchmark suite used to evaluate inference performance of AMD CDNA-based Instinct accelerators in data center machine learning workloads.

## Sources

- [MLPerf® Inference Benchmark Suite - MLPerf Inference Documentation](raw/cache/b891aaef874ab17a.md)
