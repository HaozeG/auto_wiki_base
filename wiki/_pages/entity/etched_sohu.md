---
type: entity
tags: [ai-accelerator, asic, transformer, inference, fixed-function]
sources:
  - https://www.theregister.com/2024/06/26/etched_asic_ai/
  - https://wafer.substack.com/p/breaking-down-etcheds-sohu
  - https://www.spheron.network/blog/etched-ai-sohu-vs-nvidia-transformer-asic-inference/
  - https://aiwiki.ai/wiki/etched_sohu
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

# Etched Sohu

The Etched Sohu is a fixed-function ASIC designed exclusively for transformer model inference, manufactured on TSMC's 4 nm process as a reticle-limited die. Unlike GPU or general AI accelerator designs, the Sohu does not execute transformer operations through a programmable instruction stream; instead, multi-head attention (including QKV projection and softmax), feed-forward network layers (with GELU/SiLU activations), and layer normalization are implemented as hardwired static circuits through which data flows in a fixed pipeline. This design eliminates the instruction-fetch, decode, and scheduling overhead that consumes die area and power on flexible processors. The chip pairs with 144 GB of HBM3E per chip, providing an estimated ~4,800 GB/s of memory bandwidth — exceeding the H100's ~3,350 GB/s — and Etched claims 90%+ FLOPS utilization because compute units are never idle waiting for a general-purpose scheduler. Etched raised $120 million in June 2024 to fund production. As of early 2026, the chip had not shipped to external customers and no third-party benchmark results had been published; all performance figures are from Etched's own materials.

## Key Claims

- The Sohu is fabricated on TSMC 4 nm as a reticle-limited die, meaning it occupies the maximum printable area per lithography exposure — the same strategy used by Cerebras WSE — to maximize on-die resources.
- Each chip is paired with 144 GB of HBM3E memory providing an estimated ~4,800 GB/s bandwidth, compared to 3,350 GB/s for the NVIDIA H100 SXM5.
- Etched claims an 8-chip Sohu server achieves 500,000 tokens/second on Llama 70B inference (~62,500 tok/s per chip), versus approximately 23,000 tok/s for an 8-GPU H100 server and ~45,000 tok/s for an 8-GPU B200 server under the same workload (all figures are Etched's own).
- Transformer-specific operations — multi-head attention (QKV projection, scaled dot-product, softmax), layer normalization, and FFN with nonlinear activations — are implemented as static hardwired circuits rather than executed via a programmable instruction set, eliminating instruction scheduling overhead.
- The chip cannot run non-transformer workloads; Etched's position is that future transformer variants will be supported via compiler and firmware updates, but any architecturally distinct successor to the transformer would require a new chip.
- Etched secured $120 million in Series A funding in June 2024 to fund TSMC tape-out and production; independent verification of performance claims had not been published as of March 2026.

## Relationships

- [[nvidia_hopper_h100]] — the primary competitive benchmark in Etched's marketing; Sohu targets a 20× throughput advantage on transformer inference specifically by eliminating general-purpose programmability.
- [[cerebras_wse]] — both use reticle-limited die strategy to maximize on-chip resources; WSE-3 retains programmability for arbitrary ML workloads whereas Sohu sacrifices all flexibility for transformer-only fixed-function execution.
- [[groq_lpu]] — Groq similarly targets deterministic, high-throughput LLM inference with a specialized chip; Groq retains a programmable dataflow ISA whereas Sohu uses purely hardwired circuits.
- [[graphcore_ipu]] — both are non-GPU AI accelerators with unconventional memory hierarchies; IPU uses 1,472 programmable tiles with on-chip SRAM whereas Sohu uses fixed-function transformer pipelines with HBM3E.

## Sources

- The Register — Etched scores $120M for an ASIC built for transformer models (June 2024): https://www.theregister.com/2024/06/26/etched_asic_ai/
- Peak FLOPS / Wafer Substack — Breaking down Etched's Sohu (technical analysis): https://wafer.substack.com/p/breaking-down-etcheds-sohu
- Spheron Blog — Etched AI Sohu vs NVIDIA: Transformer ASIC vs General-Purpose GPU for LLM Inference (2026): https://www.spheron.network/blog/etched-ai-sohu-vs-nvidia-transformer-asic-inference/
- AI Wiki — Etched Sohu: https://aiwiki.ai/wiki/etched_sohu
