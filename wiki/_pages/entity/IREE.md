---
cold_start: true
created: '2026-06-28'
inbound_links: 1
needs_summary_revision: false
scorecard:
  bridge_score: 0.8
  claim_density: 0.8
  hub_potential: 0.7
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://github.com/iree-org/iree
tags:
- MLIR
- compiler
- runtime
- AI
- machine learning
- RISC-V
type: entity
updated: '2026-06-28'
---

# IREE

IREE (Intermediate Representation Execution Environment, pronounced 'eerie') is an MLIR-based end-to-end compiler and runtime designed to lower machine learning models to a unified intermediate representation that scales from datacenter servers to mobile and edge devices. Developed under the LLVM project umbrella, IREE provides a retargetable compilation pipeline that maps high-level ML frameworks such as TensorFlow and PyTorch onto diverse hardware backends including CPUs, GPUs, and specialized accelerators. The project joined the LF AI & Data Foundation as a sandbox-stage project in May 2024 and maintains an active open-source community through GitHub, a Discord server, and mailing lists. IREE's architecture separates compilation into a compiler module (iree-compiler) and a lightweight runtime module (iree-runtime), supporting both ahead-of-time and just-in-time execution strategies.

## Key Claims

- IREE is an MLIR-based end-to-end compiler and runtime for machine learning models.
- It lowers models to a unified intermediate representation that scales to datacenter and edge deployments.
- Supports multiple hardware targets including CPUs, GPUs, and specialized accelerators.
- Separates compilation into iree-compiler and iree-runtime packages, available on PyPI.
- Joined the LF AI & Data Foundation as a sandbox-stage project on 2024-05-23.
- In 2025, AMD submitted an IREE-based SDXL implementation to the MLPerf inference benchmark.
- Stable and nightly releases are published on GitHub Releases.
- Community communication via GitHub issues, Discord server, and mailing lists.

## Relationships

- [[Sipeed_MAIX_series]] – A RISC-V edge AI platform that could benefit from IREE compilation for ML workloads.
- [[GEMM_with_RISC-V_Vector_Extension]] – A workload kernel that could be compiled and optimized using IREE, demonstrating the compiler's relevance to RISC-V vector architectures.
- Insufficient context for additional cross-links to entity pages.

## Sources

- [GitHub README: iree-org/iree](https://github.com/iree-org/iree)

