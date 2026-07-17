---
canonical_name: NVIDIA Hopper Architecture
aliases:
- Hopper
- NVIDIA Hopper GPU
- H100
- H200
- NVIDIA Hopper architecture
- Nvidia Hopper GPU
- NVIDIA H200
- NVIDIA H200 Tensor Core
- Hopper H200
- NVIDIA H100
- NVIDIA H100 Tensor Core
- Hopper H100
- HGX H200
subtype: null
hardware_targets:
- H100
- H200
workloads:
- AI training
- AI inference
- transformer workloads
datatypes:
- FP16
- FP8
- TF32
- FP32
metrics:
- TFLOPs
- memory bandwidth
- throughput
toolchains:
- CUDA
constraints:
- HBM3
- HBM3e
- NVLink-4
- Transformer Engine
tags: []
scorecard:
  novelty_delta: 0.6
  claim_density: 0.8
  self_containedness: 1.0
  bridge_score: 0.5
  hub_potential: 0.5
sources:
- raw/cache/70d47a6d919b3e37.md
- https://blog.prompt20.com/posts/nvidia-datacenter-gpus/
- raw/cache/04d6b461ade29969.md
- https://arxiv.org/abs/2501.12084
- raw/cache/a1f77160184ba76d.md
- https://arxiv.org/abs/2402.13499
- raw/cache/0dd8e54681229db2.md
- https://thegioimaychu.vn/blog/ai-hpc/so-sanh-cac-gpu-tensor-core-cua-nvidia-b200-b100-h200-h100-a100-p20268/
- raw/cache/220ce116aa2bb8a7.md
- https://convly.ai/ar/h100-vs-h200-for-ai/
source_url: https://blog.prompt20.com/posts/nvidia-datacenter-gpus/
fetched_at: '2026-07-17T11:48:49.233882+00:00'
type: gpu_architecture
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 3
outbound_links:
- target: nvidia_blackwell_ultra
  reason: The NVIDIA Hopper architecture is the predecessor to the NVIDIA Blackwell
    Ultra architecture; Blackwell Ultra succeeded Hopper in the datacenter GPU lineup
    and introduced FP4 precision and a dual-reticle design
---

# NVIDIA Hopper Architecture

The NVIDIA Hopper architecture is a GPU microarchitecture for datacenter AI workloads, introduced in 2022 as the successor to the Ampere architecture. It is implemented in two GPUs: the H100 and the H200. The H100 features 80 GB of HBM3 memory with 3.0 TB/s bandwidth, delivering up to 1979 TFLOPs FP16, 989 TFLOPs FP32, and 3958 TFLOPs FP8. It introduced the Transformer Engine for optimized transformer workload processing and NVLink-4 at 900 GB/s inter-GPU bandwidth. The H200 is an inference-focused refresh with 141 GB of HBM3e memory at 4.8 TB/s while maintaining the same compute capabilities as the H100. The Hopper architecture addresses the arithmetic intensity wall through a combination of larger and faster HBM, lower-precision tensor cores (FP8), and fatter NVLink interconnects.

## Key Claims

- H100: 80 GB HBM3 at 3.0 TB/s bandwidth.
- H100: 1979 TFLOPs FP16, 989 TFLOPs FP32, 3958 TFLOPs FP8.
- H200: 141 GB HBM3e at 4.8 TB/s bandwidth; same compute as H100.
- Introduced the Transformer Engine for transformer workloads.
- NVLink-4 provides 900 GB/s bidirectional bandwidth per GPU.
- Hopper was the first GPU generation explicitly designed for transformer workloads.
- The architecture achieved roughly 660 flops per byte loaded (FP16), defining memory-bound vs compute-bound regimes.

## Relationships

- [[nvidia_blackwell_ultra]]: The NVIDIA Hopper architecture is the predecessor to the NVIDIA Blackwell Ultra architecture; Blackwell Ultra succeeded Hopper in the datacenter GPU lineup and introduced FP4 precision and a dual-reticle design.

## Sources

- [NVIDIA Datacenter GPUs for AI: The Complete Guide — Prompt20 Blog](raw/cache/70d47a6d919b3e37.md)
