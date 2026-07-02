---
canonical_name: OpenGeMM
aliases:
- OpenGeMM Accelerator Generator
- OpenGeMM platform
- OpenGeMM accelerator generator
- OpenGeMM GeMM Accelerator Generator
- OpenGeMM accelerator platform
subtype: null
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 0.85
  bridge_score: 0.7
  hub_potential: 0.6
sources:
- raw/cache/2755e5333eb7a96e.md
- https://arxiv.org/html/2411.09543
- raw/cache/641c22a3fb55fe2d.md
- https://hub.baai.ac.cn/paper/7fd2589c-86b3-40ee-a921-83653897137e
- raw/cache/139c70528d55cca1.md
- https://www.researchgate.net/publication/385823001_OpenGeMM_A_High-Utilization_GeMM_Accelerator_Generator_with_Lightweight_RISC-V_Control_and_Tight_Memory_Coupling
source_url: https://arxiv.org/html/2411.09543
fetched_at: '2026-07-02T11:24:51.105524+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# OpenGeMM

OpenGeMM is an open-source, parameterized GeMM (general matrix multiplication) accelerator generator platform designed for high utilization and tight coupling with a lightweight RISC-V processor and multi-banked scratchpad memory. Developed at KU Leuven, it targets resource-constrained edge AI deployments by addressing control overhead and utilization challenges common in existing platforms like Gemmini. The generator is coded in Chisel and includes mechanisms such as configuration pre-loading, input pre-fetching with output buffering, and programmable strided memory access to boost core utilization. Experimental results report hardware utilization ranging from 81.89% to 99.34% across diverse CNN and Transformer workloads, and a 3.58x to 16.40x speedup on normalized throughput compared to Gemmini, achieving 4.68 TOPS/W system efficiency.

## Key Claims

- OpenGeMM is an open-source, parameterized GeMM accelerator generator with tight RISC-V control and memory coupling.
- Achieves 81.89%-99.34% hardware utilization across diverse CNN and Transformer workloads.
- Demonstrates 3.58x-16.40x normalized throughput speedup over the Gemmini accelerator.
- Achieves 4.68 TOPS/W system efficiency.
- Three key mechanisms: configuration pre-loading, input pre-fetching with output buffering, and programmable strided memory access.
- The GeMM core and RISC-V processor are both generated in Chisel, enabling design-time flexibility.

## Relationships

- [[cpa-factored-gemmini-systolic-array]]: Both OpenGeMM and the CPA-factored optimization target the Gemmini-style systolic array, with OpenGeMM proposing an alternative platform for higher utilization.
- [[earth-shifting-based-vector-memory-access]]: OpenGeMM's tight memory coupling with programmable strided access relates to efficient vector memory access optimizations.
- [[pulp-nn-optimization-recipe]]: Both address efficient DNN inference on RISC-V-based platforms, with OpenGeMM focusing on hardware acceleration and PULP-NN on software library optimization.

## Sources

- [OpenGeMM: A High-Utilization GeMM Accelerator Generator with Lightweight RISC-V Control and Tight Memory Coupling](https://arxiv.org/html/2411.09543)
- [OpenGeMM GitHub Repository](https://github.com/KULeuven-MICAS/snax_cluster)
