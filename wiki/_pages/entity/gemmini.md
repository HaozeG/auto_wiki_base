---
cold_start: false
created: '2026-06-26'
inbound_links: 1
scorecard:
  bridge_score: null
  claim_density: null
  hub_potential: null
  novelty_delta: null
  self_containedness: null
sources:
- https://deepwiki.com/ucb-bar/gemmini/2-architecture
- https://arxiv.org/abs/1911.09913
tags:
- risc-v
- gemmini
- systolic-array
- rocc
- deep-learning
- accelerator
type: entity
updated: '2026-06-26'
---

# Gemmini

Gemmini is an open-source, full-stack deep neural network (DNN) accelerator generator developed by the Berkeley Architecture Research group. It is implemented as a RoCC (Rocket Custom Coprocessor), enabling seamless integration with a RISC-V CPU core within the Chipyard ecosystem. The accelerator employs a systolic array architecture to efficiently execute matrix multiplication and convolution operations, which are fundamental to deep learning inference and training workloads. Gemmini is designed to allow architects to rapidly explore a wide design space of ASIC accelerators by varying parameters such as array dimensions, dataflow, memory hierarchy, and precision. As part of the ucb-bar/gemmini project, it provides a complete hardware-software stack, including a custom instruction interface, a programming model, and a compilation flow, making it a versatile platform for DNN hardware evaluation and research.

## Key Claims

- Gemmini is a systolic array-based accelerator implemented as a RoCC (Rocket Custom Coprocessor) that connects to a RISC-V CPU core via the TileLink protocol.
- The accelerator is specifically optimized for matrix multiplication and convolution operations in deep learning workloads.
- Gemmini is part of the ucb-bar/gemmini project, which is a full-system, full-stack DNN hardware exploration and evaluation platform.
- The project enables architects to systematically explore design trade-offs in accelerator parameters such as array size, memory bandwidth, and dataflow.
- Gemmini generates efficient ASIC accelerators and is fully open-source, allowing reproduction and extension of research results.
- The original Gemmini paper was published on arXiv in November 2019 (arXiv:1911.09913v1).

## Relationships

- [[fpga_riscv_isa_extension_nn_inference]]: Both explore RISC-V based acceleration for neural networks; Gemmini uses a systolic array RoCC approach while the FPGA page covers custom ISA extensions.
- [[risc_v_vector_extension]]: Gemmini's RoCC interface is complementary to the RISC-V vector extension for ML workloads.
- [[sifive_intelligence_x280]]: Production RVV IP that contrasts with the academic, open-source Gemmini generator.
- [[riscv_ai_ecosystem]]: Gemmini is a key component in the open-source RISC-V AI accelerator landscape.

## Sources

- https://deepwiki.com/ucb-bar/gemmini/2-architecture
- https://arxiv.org/abs/1911.09913
