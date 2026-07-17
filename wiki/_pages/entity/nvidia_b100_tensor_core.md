---
canonical_name: NVIDIA B100
aliases:
- B100
- NVIDIA B100 Tensor Core
- Blackwell B100
subtype: null
tags:
- gpu
- nvidia
- blackwell
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
source_url: https://thegioimaychu.vn/blog/ai-hpc/so-sanh-cac-gpu-tensor-core-cua-nvidia-b200-b100-h200-h100-a100-p20268/
fetched_at: '2026-07-17T12:40:45.945156+00:00'
type: entity
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 1
outbound_links:
- target: nvidia_b200_tensor_core
  reason: Shares the Blackwell architecture with the B200, which provides higher peak
    performance and larger memory (192 GB HBM3e with 8 TB/s bandwidth)
- target: nvidia_h200_tensor_core
  reason: The B100 outperforms the H200 in FP16 Tensor Core (3.5 vs. 1.98 petaFLOPS)
    and memory bandwidth (4.8 vs. 3.2 TB/s)
- target: nvidia_h100_tensor_core
  reason: The B100 provides approximately 5.6× the FP32 Tensor Core performance of
    the H100
---

# NVIDIA B100

The NVIDIA B100 is a Tensor Core GPU built on the Blackwell architecture, launched in 2025 as a slightly lower-spec sibling of the B200. It achieves 30 teraFLOPS FP64, 1.8 petaFLOPS FP32 Tensor Core, 3.5 petaFLOPS FP16/BF16 Tensor Core, 7 petaOPS INT8, 7 petaFLOPS FP8 Tensor Core, and 14 petaFLOPS FP4 Tensor Core. The B100 is equipped with 141 GB of HBM3e memory providing 4.8 TB/s bandwidth, and supports up to 7 MIG partitions at 16.5 GB each. It includes 5 NVDEC and 5 JPEG decoders and an NVLink interconnect of 900 GB/s. The B100 is designed for enterprise AI deployments, balancing raw performance with memory capacity.

## Key Claims

- FP64 performance: 30 teraFLOPS
- FP32 Tensor Core performance: 1.8 petaFLOPS
- FP16/BF16 Tensor Core performance: 3.5 petaFLOPS
- INT8 Tensor Core performance: 7 petaOPS
- FP8 Tensor Core performance: 7 petaFLOPS
- FP4 Tensor Core performance: 14 petaFLOPS
- Memory: 141 GB HBM3e
- Memory bandwidth: 4.8 TB/s
- MIG support: up to 7 instances at 16.5 GB each
- Decoders: 5 NVDEC, 5 JPEG
- NVLink speed: 900 GB/s

## Relationships

- [[nvidia_b200_tensor_core]]: Shares the Blackwell architecture with the B200, which provides higher peak performance and larger memory (192 GB HBM3e with 8 TB/s bandwidth).
- [[nvidia_h200_tensor_core]]: The B100 outperforms the H200 in FP16 Tensor Core (3.5 vs. 1.98 petaFLOPS) and memory bandwidth (4.8 vs. 3.2 TB/s).
- [[nvidia_h100_tensor_core]]: The B100 provides approximately 5.6× the FP32 Tensor Core performance of the H100.

## Sources

- [So sánh các thế hệ GPU Tensor Core đầu bảng của NVIDIA: B200...](raw/cache/0dd8e54681229db2.md)
