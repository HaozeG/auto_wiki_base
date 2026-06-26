---
type: entity
tags: [ai-hardware, wafer-scale, inference, training, chip-architecture]
sources:
  - https://www.cerebras.ai/press-release/cerebras-announces-third-generation-wafer-scale-engine
  - https://www.cerebras.ai/blog/cerebras-cs3
  - https://www.cerebras.ai/blog/cerebras-cs-3-vs-nvidia-dgx-b200-blackwell
  - https://arxiv.org/html/2503.11698v1
  - https://hc2024.hotchips.org/assets/program/conference/day2/72_HC2024.Cerebras.Sean.v03.final.pdf
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

# Cerebras WSE-3 (Wafer Scale Engine 3)

The Cerebras WSE-3 is the third-generation Wafer Scale Engine, announced on March 13, 2024, and manufactured by TSMC on a 5 nm process node. It is the largest semiconductor ever fabricated, occupying 46,225 mm² — an entire 300 mm silicon wafer — and integrates 4 trillion transistors across 900,000 AI-optimized compute cores. Unlike conventional accelerators that package multiple discrete dies with off-chip interconnects, the WSE-3 eliminates die-to-die communication latency by building the entire compute substrate monolithically. The chip includes 44 GB of on-chip SRAM distributed uniformly across the wafer, delivering 21 petabytes per second (PB/s) of memory bandwidth — approximately 2,600× more bandwidth than NVIDIA's Blackwell B200 GPU. A 2D mesh fabric interconnect with 214 petabits per second aggregate peak bandwidth links all cores. The WSE-3 is the compute engine of the Cerebras CS-3 system, which can scale to clusters of up to 2,048 units via the SwarmX interconnect, enabling the entire cluster to program as a single logical chip. A single CS-3 system demonstrated training of a 1 trillion parameter model in December 2024 — a workload that conventionally requires thousands of GPUs.

## Key Claims

- **4 trillion transistors, 900,000 cores:** The WSE-3 contains 4× 10¹² transistors on 46,225 mm², making it 57× larger in transistor count than the largest single GPU die available at its launch.
- **44 GB on-chip SRAM at 21 PB/s bandwidth:** All SRAM is on-wafer and accessible at 21 petabytes per second, eliminating HBM stacks and off-chip DRAM bandwidth bottlenecks that constrain GPU-based accelerators.
- **125 petaflops peak AI performance:** The WSE-3 delivers 125 PFLOPS of peak AI compute, doubling the performance of its predecessor WSE-2 at the same power envelope and price point.
- **Llama 3.1 70B at 2,100 tokens/second per user:** In single-user latency benchmarks, CS-3 ran Llama 3.1 70B at 2,100 tokens per second — roughly 8× faster than NVIDIA H200 and more than 21× faster than the Blackwell B200 on Llama 3 70B.
- **Trillion-parameter training on a single node:** In December 2024, Cerebras demonstrated training a 1 trillion parameter model on a single CS-3 system; an equivalent GPU cluster would require thousands of accelerators and complex parallelism strategies.
- **2,048-node SwarmX clusters:** Multiple CS-3 systems link via SwarmX interconnect, with a full 2,048-system cluster capable of training Llama2-70B from scratch in under one day versus approximately one month on Meta's GPU cluster.
- **Weight streaming via MemoryX:** When a model is too large to fit in on-chip SRAM, weights stream layer-by-layer from external MemoryX DRAM servers, enabling models far larger than 44 GB to run without model-parallel complexity visible to the programmer.
- **Dataflow execution model:** Computation on the WSE-3 is data-triggered: the 2D mesh fabric delivers both data and associated control signals to cores, which fetch and execute instructions upon data arrival, enabling fine-grained pipeline parallelism without explicit synchronization barriers.

## Relationships

- [[nvidia_hopper_h100]] — The H100 SXM5 delivers 3.35 TB/s HBM3 bandwidth and 989 TFLOPS BF16; the WSE-3's 21 PB/s on-chip SRAM bandwidth exceeds it by roughly 6,000×, at the cost of requiring a fundamentally different programming and scaling model.
- [[google_tpu]] — Google TPUs use systolic-array matrix units with HBM; Cerebras WSE-3 uses a distributed 2D mesh of small cores with on-wafer SRAM, representing a competing approach to eliminating memory bottlenecks in large-model inference and training.
- [[amd_mi300x]] — AMD MI300X integrates 192 GB of HBM3 per module at 5.3 TB/s bandwidth; the WSE-3 trades total capacity for dramatically higher bandwidth on 44 GB of on-chip SRAM, favoring latency-sensitive single-batch inference over memory-capacity-limited workloads.

## Sources

- Cerebras press release, WSE-3 announcement (March 13, 2024): https://www.cerebras.ai/press-release/cerebras-announces-third-generation-wafer-scale-engine
- Cerebras CS-3 product blog: https://www.cerebras.ai/blog/cerebras-cs3
- Cerebras vs. NVIDIA DGX B200 Blackwell benchmark comparison: https://www.cerebras.ai/blog/cerebras-cs-3-vs-nvidia-dgx-b200-blackwell
- arXiv technical comparison, Cerebras WSE vs. NVIDIA GPU systems (March 2025): https://arxiv.org/html/2503.11698v1
- Hot Chips 2024 presentation, Cerebras wafer-scale AI: https://hc2024.hotchips.org/assets/program/conference/day2/72_HC2024.Cerebras.Sean.v03.final.pdf
- Business Wire, trillion parameter training demonstration (December 2024): https://www.businesswire.com/news/home/20241210241089/en/Cerebras-Demonstrates-Trillion-Parameter-Model-Training-on-a-Single-CS-3-System
