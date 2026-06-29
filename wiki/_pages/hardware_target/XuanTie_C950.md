---
cold_start: true
constraints:
- 5nm
- 3.2GHz
- RISC-V
- AI acceleration engine
created: '2026-07-09'
hardware_targets:
- XuanTie C950
inbound_links: 0
scorecard:
  bridge_score: 0.6
  claim_density: 0.5
  hub_potential: 0.5
  novelty_delta: 0.9
  self_containedness: 0.6
sources:
- https://www.pchardwarepro.com/en/Features-of-the-Alibaba-Xuantie-C950-chip-and-its-role-in-AI/
tags:
- RISC-V
- Alibaba
- Xuantie
- AI
- data_center
- CPU
- 5nm
toolchains: []
type: hardware_target
updated: '2026-06-29'
---

# XuanTie C950

The XuanTie C950 is a 5 nanometer, 3.2 gigahertz, 64-bit multi-core RISC-V CPU core designed by Alibaba's DAMO Academy (via its T-Head semiconductor arm) for inference and agentic AI workloads in data centers. Announced in March 2026, it employs an open-standard RISC-V instruction set architecture, allowing customized instructions for AI workloads. It integrates a self-developed AI acceleration engine and is reported to achieve triple the performance compared to the prior-generation XuanTie C920, positioning it as a competitive option in the RISC-V server space.

## Key Claims

- 5 nanometer process technology.
- 3.2 GHz clock speed.
- 64-bit multi-core RISC-V CPU design.
- Designed for inference and agentic AI workloads in data centers.
- Open RISC-V architecture enables custom instructions for AI workloads.
- Integrated self-developed AI acceleration engine.
- Claims triple performance improvement over XuanTie C920.
- Announced in March 2026.

## Optimization-Relevant Details

- ISA/profile: RISC-V (open standard).
- Vector/matrix/accelerator support: Self-developed AI acceleration engine described in sources.
- Memory/cache/TLB/DMA: Not specified in available resource.
- Compiler/toolchain support: Not specified.

## Relationships

- [[Chiplet_RISC_V_AI_SoC_Benchmark_Results]] – Both are RISC-V based AI acceleration platforms, though targeting different architectures.
- [[Gemmini_Architecture]] – Both are RISC-V based AI accelerators; Gemmini focuses on DNN acceleration, while the C950 targets agentic AI inference.

## Sources

- [Alibaba XuanTie C950 Chip: Features and AI Strategy – PC Hardware Pro](https://www.pchardwarepro.com/en/Features-of-the-Alibaba-Xuantie-C950-chip-and-its-role-in-AI/)
- [Alibaba Launches XuanTie C950 CPU for Agentic AI – EE Times](https://www.eetimes.com/) (mentioned in snippets)
- [Alibaba reveals new AI CPU chip designed for 'agents' – CNBC](https://www.cnbc.com/) (mentioned in snippets)
- [Alibaba unveils next-gen chip for agentic AI – Reuters](https://www.reuters.com/) (mentioned in snippets)
