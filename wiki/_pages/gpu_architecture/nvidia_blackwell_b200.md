---
canonical_name: NVIDIA Blackwell B200
aliases:
- Blackwell B200
- NVIDIA B200
- B200
- NVIDIA B200 Tensor Core
- NVIDIA HGX B200
- Blackwell
subtype: null
type: gpu_architecture
hardware_targets:
- NVIDIA Blackwell B200
workloads:
- AI training
- AI inference
datatypes:
- FP4
- FP8
- FP16
- BF16
metrics:
- PetaFLOPS
- memory bandwidth
- interconnect bandwidth
toolchains:
- CUDA
- PyTorch
constraints:
- TSMC 4NP
- dual-die design
- NVLink 5
- HBM3e
- ~1000W TDP
evidence_strength: reported
tags: []
sources:
- raw/cache/be48c2942b36c9b4.md
- https://www.humai.blog/apple-m5-vs-nvidia-blackwell-vs-google-tpu-the-complete-post-ces-2025-ai-chip-comparison/
- raw/cache/0dd8e54681229db2.md
- https://thegioimaychu.vn/blog/ai-hpc/so-sanh-cac-gpu-tensor-core-cua-nvidia-b200-b100-h200-h100-a100-p20268/
- raw/cache/2ab98716c4d0d6e2.md
- https://www.gmicloud.ai/en/blog/nvidia-b200-inference-throughput
- raw/cache/5b2f2622c26a524e.md
- https://arxiv.org/abs/2512.02189v3
created: YYYY-MM-DD
updated: '2026-07-17'
cold_start: true
inbound_links: 1
scorecard:
  novelty_delta: 0.8
  claim_density: 0.7
  self_containedness: 0.9
  bridge_score: 0.9
  hub_potential: 0.8
source_url: https://www.humai.blog/apple-m5-vs-nvidia-blackwell-vs-google-tpu-the-complete-post-ces-2025-ai-chip-comparison/
fetched_at: '2026-07-17T12:32:31.354078+00:00'
outbound_links:
- target: nvidia_blackwell_ultra
  reason: Both are based on the Blackwell architecture but differ in memory capacity
    (192GB vs 288GB) and compute capability (20 PFLOPS sparse FP4 vs 15 PFLOPS dense
    NVFP4), targeting different performance tiers within the same product family
- target: google_tpu_v7_ironwood
  reason: Both the NVIDIA Blackwell B200 and [[google_tpu_v7_ironwood]] use 192GB
    HBM3e memory, though with different bandwidth configurations (8TB/s vs 7.2-7.4
    TB/s), reflecting their shared reliance on high-bandwidth memory for AI workloads
---

# NVIDIA Blackwell B200

The NVIDIA Blackwell B200 is a graphics processing unit based on the Blackwell architecture, announced at GTC in March 2024 and shipping to cloud providers throughout 2025. Built on TSMC's custom 4NP process with 208 billion transistors across a dual-die design, it delivers up to 20 petaFLOPS of sparse FP4 compute. It features 192GB of HBM3e memory with 8TB/s bandwidth and a 1.8TB/s NVLink 5 interconnect. The B200 has a thermal design power of approximately 1000W. All 2025 production units were sold out before shipping. The B200 is intended for large-scale AI training and inference workloads in data centers, leveraging the mature CUDA ecosystem and frameworks like PyTorch.

## Key Claims

- Announced at GTC March 2024, shipping to cloud providers 2025.
- 208 billion transistors, dual-die design.
- 20 PFLOPS sparse FP4 compute.
- 192GB HBM3e memory with 8TB/s bandwidth.
- 1.8TB/s NVLink 5 interconnect.
- ~1000W TDP.
- Entire 2025 production sold out before units shipped.

## Relationships

- [[nvidia_blackwell_ultra]]: Both are based on the Blackwell architecture but differ in memory capacity (192GB vs 288GB) and compute capability (20 PFLOPS sparse FP4 vs 15 PFLOPS dense NVFP4), targeting different performance tiers within the same product family.
- [[google_tpu_v7_ironwood]]: Both the NVIDIA Blackwell B200 and [[google_tpu_v7_ironwood]] use 192GB HBM3e memory, though with different bandwidth configurations (8TB/s vs 7.2-7.4 TB/s), reflecting their shared reliance on high-bandwidth memory for AI workloads.

## Sources

- [Apple M5 vs NVIDIA Blackwell vs Google TPU: The Complete...](raw/cache/be48c2942b36c9b4.md)
