---
canonical_name: NVIDIA Blackwell Ultra GPU
aliases:
- Blackwell Ultra
- NVIDIA Blackwell Ultra
subtype: null
hardware_targets:
- NVIDIA Blackwell Ultra
workloads:
- AI training
- AI inference
- large-batch pre-training
- reinforcement learning
- low-batch inference
datatypes:
- NVFP4
- FP8
- FP6
- FP16
- BF16
- FP32
metrics:
- PetaFLOPS
- throughput
- memory bandwidth
- latency
toolchains:
- CUDA
constraints:
- TSMC 4NP
- dual-reticle design
- NV-HBI interconnect
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.9
  self_containedness: 0.9
  bridge_score: 0.5
  hub_potential: 0.8
sources:
- raw/cache/a8235ec5e736f7e5.md
- https://developer.nvidia.com/blog/inside-nvidia-blackwell-ultra-the-chip-powering-the-ai-factory-era/
source_url: https://developer.nvidia.com/blog/inside-nvidia-blackwell-ultra-the-chip-powering-the-ai-factory-era/
fetched_at: '2026-07-17T11:47:17.606759+00:00'
type: gpu_architecture
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 9
outbound_links:
- target: amd_gpu_architecture
  reason: Both the NVIDIA Blackwell Ultra and AMD GPU Architecture use a hierarchical
    compute unit organization for parallel processing—NVIDIA with Streaming Multiprocessors
    and AMD with Compute Units—each designed to maximize throughput for data-parallel
    workloads
- target: alphawave_semi_hbm_subsystem
  reason: Blackwell Ultra's HBM3E memory subsystem shares the same JEDEC-standard
    high-bandwidth memory interface concept as the Alphawave Semi HBM Subsystem, both
    targeting AI and HPC workloads using 2.5D/3D integration
- target: amd_matrix_cores
  reason: Like the AMD Matrix Cores on CDNA architectures, Blackwell Ultra's fifth-generation
    Tensor Cores are specialized matrix-multiply-accumulate units supporting low-precision
    datatypes (FP4, FP6, FP8) for mixed-precision AI compute
---

# NVIDIA Blackwell Ultra GPU

The NVIDIA Blackwell Ultra GPU is a high-performance graphics processing unit built on the NVIDIA Blackwell architecture, targeting AI training and inference workloads in large-scale data centers. It features a dual-reticle design with two dies connected via the NVIDIA High-Bandwidth Interface (NV-HBI), providing 10 TB/s of die-to-die bandwidth. The chip is manufactured on TSMC 4NP and contains 208 billion transistors. It includes 160 Streaming Multiprocessors (SMs) totaling 640 fifth-generation Tensor Cores, capable of 15 PetaFLOPS dense NVFP4 compute. Blackwell Ultra introduces the NVFP4 precision format, reducing memory footprint by approximately 1.8x compared to FP8 while maintaining nearly equivalent accuracy. The GPU also features 288 GB of HBM3E memory and accelerated softmax execution for attention layers, enabling faster AI reasoning and lower compute costs.

## Key Claims

- Contains 208 billion transistors, 2.6x more than the NVIDIA Hopper GPU.
- Uses a dual-reticle design with two dies connected via NV-HBI, providing 10 TB/s of die-to-die bandwidth.
- Has 160 Streaming Multiprocessors (SMs) and 640 fifth-generation Tensor Cores.
- Delivers 15 PetaFLOPS dense NVFP4 compute.
- NVFP4 precision format reduces memory footprint by ~1.8x compared to FP8 while maintaining nearly FP8-equivalent accuracy.
- Includes 288 GB HBM3E memory (varies by SKU).
- Accelerated softmax execution and doubled Special Function Unit (SFU) throughput improve AI kernel performance.
- Fully backward compatible with the CUDA programming model.

## Relationships

- [[amd_gpu_architecture]]: Both the NVIDIA Blackwell Ultra and AMD GPU Architecture use a hierarchical compute unit organization for parallel processing—NVIDIA with Streaming Multiprocessors and AMD with Compute Units—each designed to maximize throughput for data-parallel workloads.
- [[alphawave_semi_hbm_subsystem]]: Blackwell Ultra's HBM3E memory subsystem shares the same JEDEC-standard high-bandwidth memory interface concept as the Alphawave Semi HBM Subsystem, both targeting AI and HPC workloads using 2.5D/3D integration.
- [[amd_matrix_cores]]: Like the AMD Matrix Cores on CDNA architectures, Blackwell Ultra's fifth-generation Tensor Cores are specialized matrix-multiply-accumulate units supporting low-precision datatypes (FP4, FP6, FP8) for mixed-precision AI compute.

## Sources

- [Inside NVIDIA Blackwell Ultra: The Chip Powering the AI Factory Era](raw/cache/a8235ec5e736f7e5.md)
