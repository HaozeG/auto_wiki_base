---
type: entity
tags: [ai-hardware, inference, lpu, sram, deterministic]
sources:
  - https://groq.com/lpu-architecture
  - https://groq.com/blog/inside-the-lpu-deconstructing-groq-speed
  - https://cdn.sanity.io/files/chol0sk5/production/908a9db1814f76a4a5c16ac63cc064058460376b.pdf
  - https://arxiv.org/html/2408.07326v1
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

# Groq LPU (Language Processing Unit)

The Groq Language Processing Unit (LPU) is a purpose-built AI inference accelerator designed by Groq Inc. to minimize token generation latency for large language models. Its core innovation is the Tensor Streaming Processor (TSP) architecture, which eliminates off-chip DRAM entirely and relies on a large on-chip SRAM array as the sole weight store. The first-generation GroqChip1 integrates 230 MB of on-chip SRAM with an internal bandwidth of 80 TB/s, fabricated in a 14 nm process on a 25×29 mm die. Because all model weights reside in SRAM during inference, the memory-access bottleneck that limits GPU throughput is structurally avoided. The compiler pre-computes the full execution graph — including inter-chip communication — down to individual clock cycles, producing deterministic, jitter-free execution with no runtime arbitration or hardware queues. This static scheduling means every token generation event takes a predictable, fixed number of cycles, making latency guarantees possible in cloud deployments (GroqCloud). The trade-off is that model weight capacity is bounded by on-chip SRAM; large models require multi-chip systems connected via 16 chip-to-chip links per device.

## Key Claims

- GroqChip1 integrates 230 MB on-chip SRAM with 80 TB/s internal bandwidth, versus roughly 8 TB/s for GPU HBM systems, a ~10x bandwidth advantage.
- GroqChip1 delivers 750 TOPS at INT8 and 188 TFLOPS at FP16, with 5,120 vector ALUs and a 320×320 fused dot-product matrix unit, at a 900 MHz clock.
- Groq's compiler performs fully static scheduling: execution timing including inter-chip data transfer is fixed at compile time, eliminating runtime dispatchers and producing deterministic latency.
- On GroqCloud, Llama 3 8B reaches over 1,300 tokens/second and Llama 4 Scout exceeds 460 tokens/second, compared to ~100 tokens/second for equivalent NVIDIA H100 deployments.
- The LPU uses 16 chip-to-chip interconnects per chip to scale model capacity across multiple devices without off-chip DRAM.
- Groq's second-generation LPX system (for NVIDIA Vera Rubin platform integration) raises on-chip SRAM bandwidth to 40 PB/s per system.

## Relationships

- [[nvidia_hopper_h100]] — primary architectural competitor; LPU achieves ~10x higher memory bandwidth by replacing HBM with SRAM, at the cost of smaller per-chip weight capacity.
- [[aws_inferentia]] — both are inference-only ASICs targeting cloud deployments; Inferentia uses HBM while LPU uses SRAM.
- [[tenstorrent_blackhole]] — contrasting architecture: Tenstorrent uses RISC-V cores with dynamic scheduling, whereas LPU uses static compiler-scheduled TSP execution.
- [[cerebras_wse]] — comparable SRAM-centric philosophy; WSE uses an entire wafer-scale die for SRAM while LPU scales via multi-chip interconnect.
- [[google_tpu]] — both avoid GPU-style HBM latency; TPU uses systolic arrays while LPU uses streaming dataflow.

## Sources

- Groq LPU Architecture page: https://groq.com/lpu-architecture
- "Inside the LPU: Deconstructing Groq's Speed" blog post: https://groq.com/blog/inside-the-lpu-deconstructing-groq-speed
- GroqChip Processor Product Brief (v1.7): https://cdn.sanity.io/files/chol0sk5/production/908a9db1814f76a4a5c16ac63cc064058460376b.pdf
- "LPU: A Latency-Optimized and Highly Scalable Processor for LLM Inference" (arXiv 2408.07326): https://arxiv.org/html/2408.07326v1
- NVIDIA Technical Blog on LPX integration: https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/
