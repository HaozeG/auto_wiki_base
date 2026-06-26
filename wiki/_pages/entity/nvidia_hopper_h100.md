---
type: entity
tags: [nvidia, gpu, hardware, ai-accelerator, hopper, h100, data-center]
sources:
  - https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/
  - https://www.advancedclustering.com/wp-content/uploads/2022/03/gtc22-whitepaper-hopper.pdf
  - https://www.nvidia.com/en-us/data-center/h100/
  - https://www.spheron.network/blog/nvidia-h100-specs/
created: 2026-06-26
updated: 2026-06-26
cold_start: true
inbound_links: 0
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# NVIDIA Hopper Architecture (H100)

The NVIDIA H100 Tensor Core GPU, released in 2022, is NVIDIA's ninth-generation data-center GPU and the first implementation of the Hopper microarchitecture (compute capability SM90a). Built on TSMC's 4N process node customized for NVIDIA, the full GH100 die integrates 80 billion transistors across 814 mm² and includes 144 streaming multiprocessors (SMs). The H100 is designed primarily for large-scale AI training and inference, delivering an order-of-magnitude performance improvement over the prior-generation A100 through four architectural pillars: fourth-generation Tensor Cores with FP8 support, a Transformer Engine that automates mixed-precision selection, fourth-generation NVLink providing 900 GB/s bidirectional bandwidth, and HBM3 memory delivering over 3 TB/s bandwidth. The H100 SXM5 configuration — the high-power variant used in DGX H100 and HGX H100 servers — achieves 3,958 TFLOPS peak FP8 throughput (with structured sparsity) and 1,979 TFLOPS peak FP16 throughput, making it the primary compute substrate for training frontier large language models through 2024–2025.

## Key Claims

- **Process and die:** TSMC 4N (customized for NVIDIA); 80 billion transistors; 814 mm² die; 144 SMs in the full GH100; 128 FP32 CUDA cores per SM (18,432 total); 4 fourth-generation Tensor Cores per SM (576 total).
- **Peak throughput (H100 SXM5):** 3,958 TFLOPS FP8 with structured 2:4 sparsity; 3,026 TFLOPS FP8 dense; 1,979 TFLOPS FP16/BF16 with sparsity; 1,513 TFLOPS FP16/BF16 dense.
- **HBM3 memory:** H100 SXM5 carries 80 GB HBM3 at over 3.35 TB/s bandwidth — approximately 2× the bandwidth of A100's HBM2e; the H100 NVL dual-GPU variant carries 94 GB per GPU at 3,900 GB/s.
- **Fourth-generation NVLink:** 900 GB/s total bidirectional bandwidth per GPU; 7× the bandwidth of PCIe Gen 5; NVLink Switch System enables GPU-to-GPU communication across up to 256 GPUs in a single cluster, providing 57.6 TB/s all-to-all bandwidth at that scale.
- **Transformer Engine:** Hardware unit that automatically selects FP8 or FP16 precision per layer during training without user tuning; demonstrated 4× faster training throughput on GPT-3 (175B parameters) compared to A100 BF16 training.
- **Confidential Computing:** H100 introduces hardware-based Trusted Execution Environment (TEE) support for GPUs, enabling encrypted computation for sensitive workloads — a capability absent in prior-generation data-center GPUs.
- **DGX H100 system:** Eight H100 SXM5 GPUs connected via NVLink Switch; 640 GB total HBM3; aggregate ~32 PFLOPS FP8 (with sparsity); four NVLink Switches providing full GPU mesh at 900 GB/s per GPU.

## Relationships

- [[nvidia_tensor_cores]] — Hopper contains fourth-generation Tensor Cores; the Transformer Engine is built directly on top of FP8 Tensor Core instructions introduced in this architecture
- [[google_tpu]] — Google Trillium TPU v6 and H100 compete directly as the primary training platforms for frontier LLMs; TPU uses systolic arrays rather than SM-based MMA units
- [[intel_amx]] — Intel AMX tiles in Sapphire Rapids target inference workloads that H100 also addresses, but at CPU socket rather than discrete accelerator level

## Sources

- NVIDIA Hopper Architecture In-Depth technical blog (2022): SM count, NVLink 4.0, Transformer Engine, FP8, GPT-3 speedup — https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/
- NVIDIA H100 Architecture Whitepaper v1.01: transistor count, die area, HBM3 bandwidth — https://www.advancedclustering.com/wp-content/uploads/2022/03/gtc22-whitepaper-hopper.pdf
- NVIDIA H100 product page: SXM5 vs PCIe vs NVL configurations, DGX H100 system specs — https://www.nvidia.com/en-us/data-center/h100/
- Spheron H100 specs breakdown (2026): per-precision TFLOPS table with/without sparsity — https://www.spheron.network/blog/nvidia-h100-specs/
