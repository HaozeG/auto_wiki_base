---
canonical_name: Semidynamics Tensor Unit
aliases:
- Semidynamics RISC-V Tensor Unit
- Semidynamics Tensor Unit IP
subtype: null
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.7
  self_containedness: 0.85
  bridge_score: 0.3
  hub_potential: 0.3
sources:
- raw/cache/b5c8b662d211f4bf.md
- https://us.design-reuse.com/news/55074/semidynamics-fully-coherent-risc-v-tensor-unit-ai.html
source_url: https://us.design-reuse.com/news/55074/semidynamics-fully-coherent-risc-v-tensor-unit-ai.html
fetched_at: '2026-07-03T18:09:55.553699+00:00'
type: entity
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 0
---

# Semidynamics Tensor Unit

The Semidynamics Tensor Unit is a RISC-V-based hardware accelerator designed for matrix multiplication workloads central to large language models and other AI applications. Announced in October 2023 by Semidynamics—a Barcelona-based provider of fully customisable RISC-V processor IP—the Tensor Unit is built on top of the company's RVV 1.0 Vector Processing Unit and leverages the existing vector registers to store matrices, avoiding the introduction of new architecturally-visible state. This design allows the Tensor Unit to be used for fully-connected and convolutional layers while the accompanying Vector Unit handles activation functions (ReLU, Sigmoid, Softmax). The Tensor Unit is integrated into a cache-coherent subsystem using Semidynamics' Gazzillion technology, which fetches data at high bandwidth to sustain the unit's consumption rate without requiring difficult-to-program DMAs. The unit works with standard RISC-V vector-enabled Linux without modifications, as it does not add new architectural state. Semidynamics claims a 128x performance increase for AI software compared to running on the scalar core alone.

## Key Claims

- First fully-coherent RISC-V Tensor unit for AI acceleration.
- Built on top of Semidynamics' RVV 1.0 Vector Processing Unit, using existing vector registers for matrix storage.
- No new architecturally-visible state; works seamlessly with standard RISC-V Linux.
- Integrated with cache-coherent subsystem using Gazzillion technology for high-bandwidth data feeding.
- Designed for matrix multiplication in fully-connected and convolutional layers; Vector Unit handles activation functions.
- Performance increase of 128x compared to AI software running on the scalar core alone (claimed by Semidynamics CEO).
- Targeted at workloads like LLaMa-2 and ChatGPT-scale models.

## Relationships

No specific relationship to visible context pages: the Semidynamics Tensor Unit is a new product concept not directly comparable to existing hardware targets like the AndesCore AX45MPV, which is a full CPU core with integrated VPU rather than a tensor accelerator attached via vector registers.

## Sources

- https://us.design-reuse.com/news/55074/semidynamics-fully-coherent-risc-v-tensor-unit-ai.html
