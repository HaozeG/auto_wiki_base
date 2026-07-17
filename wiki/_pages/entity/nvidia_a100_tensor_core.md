---
canonical_name: NVIDIA A100
aliases:
- A100
- NVIDIA A100 Tensor Core
- Ampere A100
- Tesla A100
- NVIDIA A100 Tensor Core GPU
- GA100
- Nvidia A100
- A100 Tensor Core GPU
- DGX A100 GPU
subtype: null
tags:
- gpu
- nvidia
- ampere
- tensor-core
scorecard:
  novelty_delta: 0.8
  claim_density: 0.9
  self_containedness: 0.9
  bridge_score: 0.3
  hub_potential: 0.5
sources:
- raw/cache/0dd8e54681229db2.md
- https://thegioimaychu.vn/blog/ai-hpc/so-sanh-cac-gpu-tensor-core-cua-nvidia-b200-b100-h200-h100-a100-p20268/
- raw/cache/69a6e0f6cd16cfa7.md
- https://jingchaozhang.github.io/A100-white-paper/
- raw/cache/fe3b2aec312d3932.md
- https://www.nextbigfuture.com/2020/08/eight-nvidia-a100-next-generation-tensor-chips-for-5-petaflops-at-200000.html
source_url: https://thegioimaychu.vn/blog/ai-hpc/so-sanh-cac-gpu-tensor-core-cua-nvidia-b200-b100-h200-h100-a100-p20268/
fetched_at: '2026-07-17T12:40:45.945156+00:00'
type: entity
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 1
outbound_links:
- target: nvidia_h100_tensor_core
  reason: The H100 (Hopper) superseded the A100 with higher FP32 Tensor Core performance
    and migrated from HBM2e to HBM3 memory
- target: nvidia_b200_tensor_core
  reason: The B200 (Blackwell) provides roughly 7× the FP16 Tensor Core performance
    of the A100
- target: amd_gpu_architecture
  reason: Both the A100 and AMD's CDNA-based GPUs target similar HPC and AI workloads,
    but the A100 was the first to popularize MIG partitioning for multi-tenant GPU
    deployments
---

# NVIDIA A100

The NVIDIA A100 is a Tensor Core GPU based on the Ampere architecture, launched in 2020. It was the first GPU to adopt the Tensor Core naming convention, dropping the Tesla brand. The A100 achieves 9.7 teraFLOPS FP64, 67 teraFLOPS FP64 Tensor Core, 80 teraFLOPS FP32, 312 teraFLOPS FP32 Tensor Core, and 624 teraFLOPS FP16/BF16 Tensor Core. INT8 Tensor Core performance is 1,248 teraOPS. It includes 80 GB of HBM2e memory with 2 TB/s bandwidth, supports up to 7 MIG partitions at 10 GB each, and features an NVLink interconnect of 600 GB/s. The A100 has been declared end-of-life (EOL) as of 2025 but remains relevant for legacy deployments.

## Key Claims

- FP64 performance: 9.7 teraFLOPS
- FP64 Tensor Core performance: 67 teraFLOPS
- FP32 performance: 80 teraFLOPS
- FP32 Tensor Core performance: 312 teraFLOPS
- FP16/BF16 Tensor Core performance: 624 teraFLOPS
- INT8 Tensor Core performance: 1,248 teraOPS
- Memory: 80 GB HBM2e
- Memory bandwidth: 2 TB/s
- MIG support: up to 7 instances at 10 GB each
- NVLink speed: 600 GB/s
- End-of-life status as of 2025

## Relationships

- [[nvidia_h100_tensor_core]]: The H100 (Hopper) superseded the A100 with higher FP32 Tensor Core performance and migrated from HBM2e to HBM3 memory.
- [[nvidia_b200_tensor_core]]: The B200 (Blackwell) provides roughly 7× the FP16 Tensor Core performance of the A100.
- [[amd_gpu_architecture]]: Both the A100 and AMD's CDNA-based GPUs target similar HPC and AI workloads, but the A100 was the first to popularize MIG partitioning for multi-tenant GPU deployments.

## Sources

- [So sánh các thế hệ GPU Tensor Core đầu bảng của NVIDIA: B200...](raw/cache/0dd8e54681229db2.md)
