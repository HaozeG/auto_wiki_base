---
type: entity
tags: [nvidia, gpu, ai-hardware, inference, training, hpc]
sources:
  - https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/
  - https://www.nvidia.com/en-us/data-center/gb200-nvl72/
  - https://developer.nvidia.com/blog/nvidia-gb200-nvl72-delivers-trillion-parameter-llm-training-and-real-time-inference/
  - https://www.serversimply.com/blog/technical-analysis-of-the-blackwell-b200
  - https://radiant.co/blog/a-deep-dive-into-nvidias-blackwell-platform
created: 2026-06-26
updated: 2026-06-26
cold_start: false
inbound_links: 0
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# NVIDIA Blackwell B200 / GB200

NVIDIA Blackwell is a GPU microarchitecture announced at GTC 2024 (March 18, 2024), succeeding the Hopper generation and represented in the datacenter primarily by the B200 GPU and the GB200 Grace Blackwell Superchip. The B200 is a dual-die GPU containing 208 billion transistors fabricated on TSMC 4NP, paired with 192 GB of HBM3e memory delivering 8 TB/s of on-package memory bandwidth. Blackwell's most significant architectural additions over Hopper are: fifth-generation Tensor Cores with native FP4 hardware acceleration (enabling 20 PFLOPS peak FP4 performance per GPU), the NVLink-C2C die-to-die interconnect that bonds the Grace CPU to the Blackwell GPU die at 900 GB/s with cache coherence, a dedicated hardware decompression engine supporting LZ4/Deflate/Snappy at up to 800 GB/s, and an AI-powered Reliability, Availability, and Serviceability (RAS) engine. The rack-scale product, the GB200 NVL72, integrates 72 B200 GPUs into a single NVLink domain that acts as one logical device, delivering 1.44 exaFLOPS at FP8 precision and 13.5 TB of aggregate HBM3e memory — 30× the real-time inference throughput of an equivalent H100 rack for trillion-parameter models. The next planned generation after Blackwell is the Rubin architecture (R200), targeting enterprise deployment in the second half of 2026.

## Key Claims

- The B200 GPU reaches **20 PFLOPS peak FP4** (dense) via fifth-generation Tensor Cores, which is the first NVIDIA GPU generation to offer native FP4 tensor operations in hardware.
- **NVLink-C2C** connects the Grace CPU and Blackwell GPU dies at **900 GB/s** bidirectional with cache coherence; standard NVLink 5.0 between GPUs in the same NVLink domain runs at 1.8 TB/s bidirectional per GPU.
- The **GB200 NVL72** rack houses 36 Grace Blackwell Superchips (72 B200 GPUs + 36 Grace CPUs) in a single 72-GPU NVLink domain, providing **13.5 TB aggregate HBM3e** and **576 TB/s aggregate memory bandwidth**.
- The GB200 NVL72 delivers **1.44 exaFLOPS at FP8** — 30× the real-time inference throughput NVIDIA claims for a comparable H100 system on trillion-parameter LLMs.
- The dedicated **hardware decompression engine** natively handles LZ4, Deflate, and Snappy formats at up to **800 GB/s**, reported as 18× faster than Intel Sapphire Rapids CPUs and 6× faster than H100 for analytics query benchmarks.
- The **RAS engine** monitors thousands of operational parameters using an on-chip AI model to predict hardware faults, migrate workloads off failing cards preemptively, and enable weeks-long uninterrupted cluster operation.
- The B200 contains **208 billion transistors** across two dies (roughly 2× the transistor count of the H100 SXM5 at 80 billion), manufactured on TSMC 4NP.
- DGX B200 (8× B200 GPUs) delivers approximately **3× training throughput** and **15× inference throughput** relative to DGX H100 on comparable workloads per NVIDIA benchmarks.

## Relationships

- [[nvidia_hopper_h100]] — Blackwell succeeds Hopper; B200 provides roughly 3× training and 15× inference gains over H100, and replaces the SXM5 form factor in datacenter racks.
- [[nvidia_tensor_cores]] — Blackwell introduces fifth-generation Tensor Cores adding FP4 precision; prior generations supported FP16/BF16/FP8/INT8 but not FP4.
- [[nvlink_nvswitch]] — GB200 uses NVLink 5.0 (1.8 TB/s bidirectional per GPU) and NVSwitch to build the 72-GPU NVL72 NVLink domain; NVLink-C2C is a separate, cache-coherent variant connecting CPU and GPU dies.
- [[hbm_high_bandwidth_memory]] — B200 uses HBM3e at 192 GB per GPU / 8 TB/s; the NVL72 rack aggregates 13.5 TB of HBM3e across 72 GPUs.

## Sources

- NVIDIA Blackwell Architecture overview: https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/
- GB200 NVL72 product page: https://www.nvidia.com/en-us/data-center/gb200-nvl72/
- NVIDIA Developer Blog — GB200 NVL72 technical deep dive: https://developer.nvidia.com/blog/nvidia-gb200-nvl72-delivers-trillion-parameter-llm-training-and-real-time-inference/
- ServerSimply B200 technical analysis: https://www.serversimply.com/blog/technical-analysis-of-the-blackwell-b200
- Radiant deep dive — decompression engine and RAS: https://radiant.co/blog/a-deep-dive-into-nvidias-blackwell-platform
- Rubin roadmap: https://www.storagereview.com/news/nvidia-unveils-roadmap-at-ai-infra-summit-from-blackwell-ultra-to-vera-rubin-cpx-architecture
