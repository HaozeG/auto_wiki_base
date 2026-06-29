---
cold_start: true
created: '2025-03-04'
inbound_links: 0
scorecard:
  bridge_score: 0.6
  claim_density: 0.3
  hub_potential: 0.5
  novelty_delta: 0.5
  self_containedness: 0.8
sources:
- https://sites.google.com/berkeley.edu/gemminitutorialiiswc2021/
tags:
- RISC-V
- DNN accelerator
- hardware generator
- Chipyard
- full-stack evaluation
type: entity
updated: '2026-06-29'
---

# Gemmini

Gemmini is a platform for full-system, full-stack DNN accelerator evaluation developed at UC Berkeley. It enables users to generate custom DNN hardware accelerators within a RISC-V System-on-Chip (SoC) environment, integrated with the Chipyard framework. Gemmini provides a multi-level programming stack that spans high-level ONNX model compilation, a mid-level hand-tuned kernel library, and low-level direct machine configuration via C and assembly. The platform exposes system-level effects such as cache hierarchy, virtual memory translation, and operating system interactions, allowing architects to evaluate how these components impact end-to-end performance and efficiency. Gemmini supports various datatypes, dataflow modes (output-stationary, weight-stationary, runtime-selectable), and systolic array configurations. It was presented at DAC 2021 and tutorials were held at IISWC 2021 and MLSys 2022.

## Key Claims

- Gemmini allows users to generate a variety of different DNN hardware accelerators with configurable system, SoC, and programming stack components.
- It provides a full-system evaluation environment that captures system-level effects like cache hierarchy, virtual address translation, and OS overhead.
- The platform offers a multi-level software stack: high-level ONNX model compilation, mid-level hand-tuned kernel library, and low-level direct machine configuration.
- Gemmini integrates with the Chipyard framework for RISC-V SoC generation.
- The project is open-source and available on GitHub (ucb-bar/gemmini).

## Relationships

- [[DSC_Fused_Dataflow_Benchmark_Results]] — a benchmark for a different RISC-V DNN accelerator, providing context for alternative approaches to DNN acceleration on RISC-V.
- [[Chiplet_RISC_V_AI_SoC_Benchmark_Results]] — benchmark results for a chiplet-based RISC-V AI SoC, which is another approach to RISC-V AI acceleration that Gemmini can generate and evaluate.

Note: Insufficient context for additional cross-links; only benchmark result pages were available in the wiki context.

## Sources

- [Gemmini Tutorial IISWC 2021](https://sites.google.com/berkeley.edu/gemminitutorialiiswc2021/)
