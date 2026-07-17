---
canonical_name: Google Ironwood TPU
aliases:
- Ironwood
- Google TPU Ironwood
- Ironwood TPU
- TPU v7
- TPU7x (Ironwood)
- Google TPU7x
- TPU v7 Ironwood
- Google TPU v7 Ironwood
- Google Ironwood
subtype: null
hardware_targets:
- Google Ironwood TPU
workloads:
- AI inference
- large language models
- mixture-of-expert models
- reasoning models
datatypes:
- FP8
metrics:
- exaflops
- performance per watt
- memory bandwidth
- HBM capacity
toolchains: []
constraints:
- 10 MW power consumption per 9216-chip node
- liquid cooling required
evidence_strength: reported
tags:
- TPU
- Google
- AI inference
- Hot Chips 2025
- optical circuit switching
- HBM3e
scorecard:
  novelty_delta: 0.9
  claim_density: 0.85
  self_containedness: 0.9
  bridge_score: 0.4
  hub_potential: 0.2
sources:
- raw/cache/5cfb625430734699.md
- https://www.servethehome.com/google-ironwood-tpu-swings-for-reasoning-model-leadership-at-hot-chips-2025/
- raw/cache/f7f559569bd5b8bf.md
- https://techcrunch.com/2025/04/09/google-unveils-ironwood-a-new-ai-accelerator-chip/
- raw/cache/c5d9854149044f40.md
- https://docs.cloud.google.com/tpu/docs/tpu7x
- raw/cache/e2f0a899af98f5bc.md
- https://docs.cloud.google.com/tpu/docs/ironwood-performance
- raw/cache/86810d726576fc07.md
- https://www.nevsemi.com/blog/google-tpu-chip-ironwood-technology-explained
- raw/cache/be48c2942b36c9b4.md
- https://www.humai.blog/apple-m5-vs-nvidia-blackwell-vs-google-tpu-the-complete-post-ces-2025-ai-chip-comparison/
source_url: https://www.servethehome.com/google-ironwood-tpu-swings-for-reasoning-model-leadership-at-hot-chips-2025/
fetched_at: '2026-07-17T11:24:11.253159+00:00'
type: ai_accelerator_architecture
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 0
---

# Google Ironwood TPU

The Google Ironwood TPU (Tensor Processing Unit) is a custom AI accelerator designed by Google for large-scale artificial intelligence inference workloads. First revealed in 2025 and presented at Hot Chips 2025, Ironwood is the first Google TPU explicitly engineered for inference rather than training, targeting large language models, mixture-of-expert models, and reasoning models. Ironwood systems can scale to 9,216 chips in a single node (pod), achieving up to 42.5 exaflops of compute performance using FP8 precision. The system is interconnected via optical circuit switches (OCS) to share 1.77 petabytes of directly addressable HBM memory across the entire pod. Ironwood is Google's first TPU to use a multi-die chiplet architecture, with two compute dies per chip, and incorporates 8 stacks of HBM3e memory providing 192 GB of capacity and 7.3 TB/s of bandwidth per chip. Power consumption for a full 9,216-chip node is approximately 10 MW. Ironwood is used exclusively within Google's cloud infrastructure and is not available for external purchase.

## Key Claims

- Ironwood is the first Google TPU explicitly designed for large-scale AI inference, targeting LLMs, mixture-of-expert models, and reasoning models.
- A single pod can contain up to 9,216 chips connected via optical circuit switches (OCS), achieving 42.5 exaflops of FP8 compute performance.
- The pod offers 1.77 PB of directly addressable HBM shared memory, enabled by OCS.
- Ironwood claims 2x performance-per-watt improvement over the previous-generation Trillium TPU and 6x improvement over TPUv4.
- It is the first Google TPU to use multiple compute chiplets: two Ironwood compute dies per chip.
- Each chip includes 8 stacks of HBM3e memory, providing 192 GB capacity and 7.3 TB/s memory bandwidth.
- The system uses Google's third-generation liquid cooling infrastructure to manage heat.
- Ironwood integrates the 4th generation SparseCore for accelerating embeddings and collective communication.
- RAS (Reliability, Availability, Serviceability) features include integrated root of trust, built-in self-testing, silent data corruption detection, and in-flight arithmetic checking.
- AI was used in designing ALU circuits and optimizing floorplan, in collaboration with the Alph... (truncated in source).

## Relationships

No specific relationship to visible context pages in the current wiki.

## Sources

- [Google Ironwood TPU Swings for Reasoning Model... - ServeTheHome](raw/cache/5cfb625430734699.md)
