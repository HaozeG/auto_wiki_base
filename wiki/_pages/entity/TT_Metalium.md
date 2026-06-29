---
cold_start: false
created: '2025-03-27'
inbound_links: 2
needs_summary_revision: false
scorecard:
  bridge_score: 0.5
  claim_density: 0.4
  hub_potential: 0.5
  novelty_delta: 0.9
  self_containedness: 0.8
sources:
- https://github.com/tenstorrent/tt-tutorial/blob/main/tt-metalium/README.md
tags:
- Tenstorrent
- TT-Metalium
- low-level programming
- kernel development
- AI accelerator
type: entity
updated: '2026-06-29'
---

# TT-Metalium

TT-Metalium is Tenstorrent's low-level programming model and runtime that enables direct kernel development for Tenstorrent hardware, providing programmers with direct access to the architecture's Tensix cores, Ethernet cores, and Network-on-Chip (NoC). It is part of a broader software stack that includes the TT-NN operator library for high-level neural network operations, the TT-SMI (System Management Interface) for device interaction and telemetry, and the TT-Exalens (TT-Lensium) low-level debugging tool. Installation options range from pre-built binaries to source builds, with documented support for various deployment scenarios. TT-Metalium is central to custom kernel development for Tenstorrent AI accelerators, allowing fine-grained control over data movement and computation.

## Key Claims

- TT-Metalium is a low-level programming model and runtime for Tenstorrent hardware.
- It provides direct access to Tensix cores, Ethernet cores, and the Network-on-Chip (NoC).
- Accompanied by TT-NN (operator library), TT-SMI (system management), and TT-Exalens (debugging) tools.
- Installation supports binary, source, and other deployment options.
- Enables kernel development for AI acceleration tasks.

## Relationships

- [[Chiplet_RISC_V_AI_SoC_Benchmark_Results]] – Another AI accelerator benchmark, providing context for comparing Tenstorrent performance with chiplet-based RISC-V AI SoCs.
- [[DSC_Fused_Dataflow_Benchmark_Results]] – A benchmark for a RISC-V TinyML accelerator, relevant for contrasting acceleration approaches.

## Sources

- [tt-tutorial/tt-metalium/README.md](https://github.com/tenstorrent/tt-tutorial/blob/main/tt-metalium/README.md)
