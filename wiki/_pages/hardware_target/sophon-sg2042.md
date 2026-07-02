---
canonical_name: Sophon SG2042
aliases:
- SG2042
- SOPHON SG2042
- Sophon SG2042 CPU
- SG2042 RISC-V CPU
- Sophgo SG2042
- T-head C920
- Sophon 64-core RISC-V CPU
- Milk-V Pioneer (contains SG2042)
subtype: null
tags:
- RISC-V
- SOPHON
- HPC
- 64-core
hardware_targets:
- Sophon SG2042
toolchains: []
constraints:
- 64-core
- 2GHz
- XuanTie C920 cores
- 12-stage out-of-order superscalar
- RVV v0.7.1
scorecard:
  novelty_delta: 0.9
  claim_density: 0.6
  self_containedness: 0.7
  bridge_score: 0.7
  hub_potential: 0.6
sources:
- raw/cache/7cd9c0eb3256236c.md
- https://www.researchgate.net/publication/381517668_Performance_characterisation_of_the_64-core_SG2042_RISC-V_CPU_for_HPC
- raw/cache/f40f095c46ded0be.md
- https://www.themoonlight.io/en/review/performance-characterisation-of-the-64-core-sg2042-risc-v-cpu-for-hpc
- raw/cache/5b1c2c5ef89a99ef.md
- https://arxiv.org/abs/2406.12394
- raw/cache/b2afaa549d2d36a1.md
- https://api.emergentmind.com/papers/2406.12394
- raw/cache/2fb82d8696c94aff.md
- https://link.springer.com/content/pdf/10.1007/978-3-031-73716-9_25
- raw/cache/28c41456c7807192.md
- https://milkv.io/docs/pioneer/resources/gcc
- raw/cache/f027de9f838085f3.md
- https://www.research.ed.ac.uk/en/publications/is-risc-v-ready-for-hpc-prime-time-evaluating-the-64-core-sophon-/
- raw/cache/439ac77e161d2083.md
- https://arxiv.org/html/2406.12394
source_url: https://www.researchgate.net/publication/381517668_Performance_characterisation_of_the_64-core_SG2042_RISC-V_CPU_for_HPC
fetched_at: '2026-07-02T10:38:16.305096+00:00'
type: hardware_target
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 2
---

# Sophon SG2042

The Sophon SG2042 is a 64-core RISC-V central processing unit designed by SOPHON Technology, targeting high-performance computing workloads. It runs at 2 GHz and organizes its 64 cores in clusters of four XuanTie C920 cores, each a 64-bit out-of-order superscalar design by T-Head. The SG2042 provides a commodity-available RISC-V platform with significantly higher core count than prior RISC-V CPUs, making it a potential game changer for HPC. Positioned for server-class and HPC applications, the SG2042 enables evaluation of RISC-V readiness for prime-time HPC through benchmark studies.

## Key Claims

- The Sophon SG2042 is a 64-core RISC-V processor running at 2 GHz.
- Cores are organized in clusters of four XuanTie C920 cores, each a 64-bit 12-stage out-of-order superscalar design from T-Head.
- In single-core benchmarks, the SG2042 delivers 2.6× to 16.7× performance improvement over other RISC-V solutions tested.
- The SG2042 is a commodity-available high-core-count RISC-V CPU suitable for HPC workloads.
- LLM inference on BERT and GPT-2 has been assessed on the SG2042 with the RVV v0.7.1 vector extension.

## Optimization-Relevant Details

- ISA/profile: RISC-V 64-bit, with silicon-enabled RVV v0.7.1.
- Vector/matrix/accelerator support: RVV v0.7.1 vector extension (pre-ratification).
- Memory/cache/TLB/DMA: Not specified in available sources.
- Compiler/toolchain support: Not specified (expected GNU/Linux toolchain with RVV support).

## Relationships

- [[xuantie-c950]]: A high-performance RISC-V core from the same ecosystem (T-Head/Alibaba), representing a later generation than the C920.
- [[nncase]]: An open-source neural network compiler for RISC-V AI accelerators; relevant for software support on RISC-V platforms like the SG2042.
- Insufficient context for additional cross-links; no existing entity pages for XuanTie C920 or other Sophon products in the wiki.

## Sources

- [Performance characterisation of the 64-core SG2042 RISC-V CPU for HPC](https://www.researchgate.net/publication/381517668_Performance_characterisation_of_the_64-core_SG2042_RISC-V_CPU_for_HPC)
