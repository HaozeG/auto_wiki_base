---
cold_start: true
created: '2026-06-28'
inbound_links: 0
scorecard:
  bridge_score: 0.2
  claim_density: 0.3
  hub_potential: 0.5
  novelty_delta: 0.7
  self_containedness: 0.8
sources:
- https://docs.tenstorrent.com/tt-awesome/
tags:
- tenstorrent
- awesome-list
- community
type: entity
updated: '2026-06-29'
---

# tt-awesome

The Tenstorrent Awesome List (tt-awesome) is a community-curated directory of projects, tools, models, and research for Tenstorrent hardware. It aggregates 108 projects across 12 categories including AI & Models, Custom Kernels & Low-Level, Compilers & Frontends, and Cloud & Orchestration, providing a comprehensive overview of the Tenstorrent ecosystem. The list is maintained as an open-source repository on GitHub and includes both official Tenstorrent projects and community contributions. Projects are categorized by type, with entries for getting-started resources, AI agent frameworks, hardware system tools, RISC-V architecture experiments, and academic papers, making it a valuable entry point for developers new to Tenstorrent hardware. The list also highlights significant community contributions such as the Boltzmann-2 biomolecular model, low-level Python drivers for Blackhole, and various kernel experiments.

## Key Claims

- Contains 108 projects as of the snapshot date.
- Organized into 12 categories: Getting Started, AI & Models, AI Agents, Custom Kernels & Low-Level, Compilers & Frontends, Dev Tools & Debugging, Hardware & System, Cloud & Orchestration, RISC-V & Architecture, Research & Papers, Games & Demos, and Guides, Tutorials & Education.
- Includes both official Tenstorrent SDK projects (tt-metal, TT-NN) and community-contributed tools (tt-tiny, blackhole-py, tt-sim).
- Provides a broad view of the Tenstorrent software ecosystem, spanning from low-level kernel programing to high-level AI model serving.

## Relationships

- [[Gemmini_Architecture]] – Another open-source RISC-V accelerator ecosystem; comparing community tooling approaches highlights different development environments.
- [[XuanTie_C908_SHL_GEMM_Optimization]] – Represents a vendor-specific RISC-V AI optimization; the tt-awesome list includes compilers and kernels that target similar workloads on Tenstorrent hardware.

## Sources

- https://docs.tenstorrent.com/tt-awesome/
