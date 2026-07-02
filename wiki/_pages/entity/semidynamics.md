---
canonical_name: Semidynamics
aliases:
- SemidynamicsTM
- Semidynamics
subtype: null
tags: []
scorecard:
  novelty_delta: 0.5
  claim_density: 0.4
  self_containedness: 0.8
  bridge_score: 0.5
  hub_potential: 0.5
sources:
- raw/cache/5ded53d38c75f811.md
- https://semidynamics.com/en/blog-post/ai-runs-on-vectors
source_url: https://semidynamics.com/en/blog-post/ai-runs-on-vectors
fetched_at: '2026-07-02T11:20:32.338136+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# Semidynamics

Semidynamics is a Barcelona-based company founded in 2016 that specializes in fully customizable RISC-V processor IP with vector extensions. The company implements the RISC-V Vector Extension 1.0 (RVV 1.0) standard, enabling parallelism for AI, scientific computing, and data processing workloads. Unlike off-the-shelf CPUs, Semidynamics allows customers to tailor vector width, cache size, and memory bandwidth to fit exact application needs. The company has also launched a fully-coherent RISC-V Tensor unit for matrix multiplication, and its AI processing element combines a RISC-V CPU with vector and tensor units for integrated acceleration.

## Key Claims

- Semidynamics implements the RISC-V Vector Extension 1.0 standard in its processor IP.
- The company's cores offer customizable vector width, cache size, and memory bandwidth.
- Semidynamics launched a fully-coherent RISC-V Tensor unit for matrix multiplication.
- The AI processing element integrates a RISC-V CPU, vector unit, and tensor unit.

## Relationships

- [[earth-shifting-based-vector-memory-access]]: The EARTH optimization targets vector memory access on RISC-V vector units, which are a type of architecture that Semidynamics provides; improvements in vector memory access could benefit Semidynamics-based designs.
- [[pulp-nn-optimization-recipe]]: PULP-NN is a library for quantized neural networks on RISC-V clusters; Semidynamics' vector and tensor units could be targets for such software optimizations.

Note: insufficient context for additional cross-links to entity pages in the current relevant_pages set.

## Sources

- [AI runs on vectors - Semidynamics blog post](https://semidynamics.com/en/blog-post/ai-runs-on-vectors)
