---
cold_start: true
created: '2026-06-27'
inbound_links: 0
needs_summary_revision: false
scorecard:
  bridge_score: 0.5
  claim_density: 0.3
  hub_potential: 0.5
  novelty_delta: 0.7
  self_containedness: 0.6
sources:
- https://docs.tenstorrent.com/tt-metal/latest/tt-metalium/tt_metal/labs/matmul/lab1/lab1.html
tags:
- tenstorrent
- tt-metalium
- tensix
- accelerator
- programming-model
type: entity
updated: '2026-06-28'
---

# Tenstorrent TT-Metalium

TT-Metalium is a C++ programming framework developed by Tenstorrent for programming its Tensix processor, an AI accelerator delivered as a PCIe card. The framework allows developers to configure the accelerator, allocate memory on the device, and dispatch kernels to Tensix cores from a standard host C++ program. A Tenstorrent device consists of one or more Tensix processors, each with dedicated DRAM separate from host system memory, and a network on chip (NoC) that connects Tensix cores to DRAM and on-chip SRAM (L1 memory). The on-chip SRAM acts as working memory rather than a cache, and each Tensix core contains a dedicated compute unit optimized for matrix and vector operations on tensors. Data movement is explicit and carefully orchestrated: the host transfers input tensors to device DRAM, Tensix cores move data to on-chip SRAM, perform computation, and results are moved back to host memory. This design emphasizes on-device computation with minimal host-device communication overhead over PCIe.

## Key Claims

- TT-Metalium provides a C++ API for configuring the accelerator, allocating device memory, and dispatching kernels to Tensix cores.
- Tensix cores have dedicated compute hardware specifically optimized for matrix and vector operations on tensors.
- On-chip SRAM (L1 memory) serves as explicit working memory, not as a cache, requiring programmer-directed data movement.
- Data transfer between host and device DRAM happens over PCIe; most computation steps occur entirely on the device.
- The architecture supports tiled operations, making loop tiling an important optimization for Tensix cores.
- A single Tensix core can be programmed with TT-Metalium; multi-core and multi-device scaling is described in subsequent labs.

## Relationships

Insufficient context for additional cross-links: no directly related existing wiki pages were identified from the source material.

## Sources

- https://docs.tenstorrent.com/tt-metal/latest/tt-metalium/tt_metal/labs/matmul/lab1/lab1.html
