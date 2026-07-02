---
canonical_name: Esperanto Technologies
aliases:
- Esperanto Technologies, Inc.
- Esperanto
subtype: null
tags: []
scorecard:
  novelty_delta: 0.8
  claim_density: 0.7
  self_containedness: 0.8
  bridge_score: 0.6
  hub_potential: 0.5
sources:
- raw/cache/909f03f2ae42d42b.md
- https://www.eetimes.com/esperanto-pivots-to-hpc-and-generative-ai/
source_url: https://www.eetimes.com/esperanto-pivots-to-hpc-and-generative-ai/
fetched_at: '2026-07-02T12:00:50.641723+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# Esperanto Technologies

Esperanto Technologies is a fabless semiconductor company that develops massively parallel, energy-efficient processors based on the open-standard RISC-V instruction set architecture (ISA). Originally focused on accelerating machine learning recommendation workloads, the company pivoted to target high-performance computing (HPC) and generative AI applications. Esperanto's first-generation product, the ET-SoC-1 system-on-chip, integrates 1088 ET-Minion RISC-V tensor processors and four ET-Maxion general-purpose RISC-V cores, fabricated in TSMC 7nm technology. The chip delivers 100-200 TOPS at under 20 watts. In 2025, Esperanto introduced a GPU-class software stack and a PCIe card form factor for HPC users to write custom kernels, along with an AI software development kit (SDK) optimized for partitioning large language model (LLM) layers efficiently. The company has demonstrated Meta's OPT-13B LLM running on a single ET-SoC-1 chip operating in the 15-50 watt power envelope with typical consumption around 25 watts, and plans to scale to 30B-parameter and larger models including Llama.

## Key Claims

- Esperanto originally targeted recommendation acceleration but pivoted to generative AI and HPC.
- The ET-SoC-1 chip remains the same silicon, but the form factor changed to a PCIe card with a GPU-class software stack.
- The AI SDK handles partitioning of LLM layers efficiently.
- Esperanto demonstrated Meta's OPT-13B LLM on a single ET-SoC-1 chip consuming 15-50 W (typical 25 W).
- The company plans to scale to OPT up to 30B parameters and other models including Llama.

## Relationships

- [[et-soc-1]]: The ET-SoC-1 is the hardware platform powering Esperanto's pivot to HPC and generative AI.
- [[earth-shifting-based-vector-memory-access]]: The EARTH optimization targets RISC-V vector memory access, relevant to Esperanto's ET-Minion processors which rely on vector memory access patterns.

## Sources

- [Esperanto Pivots to HPC and Generative AI - EE Times](https://www.eetimes.com/esperanto-pivots-to-hpc-and-generative-ai/)
