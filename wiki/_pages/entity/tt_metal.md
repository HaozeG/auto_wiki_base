---
cold_start: true
created: '2025-03-27'
inbound_links: 0
scorecard:
  bridge_score: null
  claim_density: null
  hub_potential: null
  novelty_delta: null
  self_containedness: null
sources:
- context7_tt_metal.md
tags:
- tenstorrent
- ai-hardware
- software-stack
- tt-nn
- tt-metalium
type: entity
updated: '2025-03-27'
---

# TT-Metal

TT-Metal is Tenstorrent's software stack for programming their AI accelerator hardware, providing both a high-level neural network operations library (TT-NN) and a low-level programming model (TT-Metalium) for kernel development. The stack is designed to enable efficient deployment of machine learning models on Tenstorrent's Tensix architecture, supporting both training and inference workflows. TT-NN offers a collection of pre-built neural network operators implemented in Python and C++, allowing developers to compose and optimize models without deep hardware knowledge. TT-Metalium, on the other hand, provides a metal-level abstraction for writing custom kernels that directly leverage the parallel processing capabilities of Tenstorrent cores. The software is hosted on GitHub under the tenstorrent/tt-metal repository and includes comprehensive documentation, API references, and code examples.

## Key Claims

- TT-Metal is the official software stack for Tenstorrent AI hardware.
- It consists of two main components: TT-NN (neural network operations library) and TT-Metalium (low-level programming model).
- TT-NN provides Python and C++ interfaces for building and optimizing neural network models.
- TT-Metalium enables direct kernel development for Tensix architecture cores.
- The stack supports both training and inference deployment.
- The software is available as an open-source repository on GitHub (tenstorrent/tt-metal).

## Relationships

- [[tensix_architecture]]: TT-Metal is the software layer that programs Tensix cores.
- [[tenstorrent]]: TT-Metal is developed by Tenstorrent as part of their AI hardware ecosystem.
- [[tt_nn]]: The high-level component of TT-Metal.
- [[tt_metalium]]: The low-level component of TT-Metal.

## Sources

- context7_tt_metal.md (Context7 documentation page for TT-Metal)
