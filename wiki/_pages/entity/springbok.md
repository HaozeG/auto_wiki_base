---
canonical_name: Springbok
aliases:
- Springbok ML accelerator
- Google Springbok
- AmbiML Springbok
subtype: null
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.6
  self_containedness: 0.8
  bridge_score: 0.7
  hub_potential: 0.6
sources:
- raw/cache/a53d2fb9f92636bb.md
- https://riscv.org/blog/co-developing-machine-learning-with-a-risc-v-vector-core-using-renode-for-google-research-antmicro-2/
source_url: https://riscv.org/blog/co-developing-machine-learning-with-a-risc-v-vector-core-using-renode-for-google-research-antmicro-2/
fetched_at: '2026-07-02T10:18:37.384054+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# Springbok

Springbok is a RISC-V-based machine learning (ML) accelerator developed by Google Research in collaboration with Antmicro. It is part of the AmbiML project, an open-source ML development ecosystem focused on privacy and security. The accelerator leverages the RISC-V Vector (RVV) extensions to parallelize matrix multiply and accumulate operations typical of ML inference workloads. A defining characteristic of the Springbok development process is its reliance on Renode, an open-source simulation framework from Antmicro, which enables hardware-software co-design before silicon fabrication. Using Renode, the team can rapidly explore architectural trade-offs, profile performance, and test ML workloads such as MobileNetv1 in a heterogeneous multi-core environment (one core running the Springbok payload, another running Zephyr). The software toolchain around Springbok includes IREE, an ML compiler and runtime based on LLVM and MLIR, which converts models from TensorFlow/TensorFlow Lite into optimized code for the target hardware. Springbok was first publicly demonstrated at the Spring 2022 RISC-V Week in Paris, showcasing a complete flow from model loading to inference execution with custom instruction support via Renode. The accelerator exemplifies an open, simulation-driven approach to co-developing specialized ML hardware with software, reducing iteration cycles from days to minutes.

## Key Claims

- Springbok is a RISC-V-based ML accelerator developed by Google Research and Antmicro, part of the AmbiML project.
- It uses the RISC-V Vector (RVV) extensions for efficient matrix multiply and accumulate operations.
- The accelerator is co-developed using Renode simulation, allowing iterative architectural exploration without physical silicon.
- A heterogeneous multi-core demo was shown: one core running Springbok for ML inference (MobileNetv1), another running Zephyr as the application core.
- Custom instructions are added and modified in Renode via Python, C#, or RTL co-simulation.
- The ML software stack uses IREE for model compilation and deployment, supporting TensorFlow/TensorFlow Lite models.
- Performance measurement capabilities include opcode counting, execution metrics logging, and execution trace generation.
- The development flow was open-sourced as part of the Spring 2022 RISC-V Week presentation.

## Relationships

- [[mlir-xdsl-rvv-lowering-pipeline]]: Related compilation approach for RVV code generation, relevant to the software toolchain used with Springbok.
- [[cpa-factored-gemmini-systolic-array]]: Another RISC-V ML accelerator optimization, providing a contrasting design strategy focused on systolic array microarchitecture.
- [[kendryte-k230-neural-network-benchmarks]]: Benchmark results on a different RISC-V ML platform (Kendryte K230), offering context for comparing Springbok's potential performance.
- Insufficient context for additional entity page cross-links; the existing relevant pages are optimization recipes and benchmark results rather than entity pages.

## Sources

- [Co-developing Machine Learning with a RISC-V vector core using Renode for Google Research | Antmicro - RISC-V International](https://riscv.org/blog/co-developing-machine-learning-with-a-risc-v-vector-core-using-renode-for-google-research-antmicro-2/)
