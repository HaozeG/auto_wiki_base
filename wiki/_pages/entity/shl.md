---
canonical_name: SHL
aliases:
- Structure of Heterogeneous Library
- ShiHulan
- openvinotoolkit/shl
subtype: null
tags: []
scorecard:
  novelty_delta: 0.8
  claim_density: 0.3
  self_containedness: 0.9
  bridge_score: 0.5
  hub_potential: 0.4
sources:
- raw/cache/5561b8e467b4209b.md
- https://github.com/openvinotoolkit/shl
source_url: https://github.com/openvinotoolkit/shl
fetched_at: '2026-07-02T06:17:07.668810+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# SHL

SHL (Structure of Heterogeneous Library, Chinese name: ShiHulan) is a high-performance heterogeneous computing library developed by T-HEAD for neural network inference on XuanTie CPU platforms. The library provides a series of optimized binary libraries for common neural network operators. Its interface uses the CSI-NN2 API, the T-HEAD neural network library API for XuanTie CPUs. SHL can be integrated with the HHB tool for quantization and compilation of neural networks, allowing automatic invocation of SHL-optimized routines when deploying models on RISC-V devices. SHL is hosted under the OpenVINO toolkit organization on GitHub.

## Key Claims

- SHL is a high-performance heterogeneous computing library provided by T-HEAD.
- Its interface uses the CSI-NN2 API for XuanTie CPU platforms.
- SHL provides a series of optimized binary libraries for neural network operators.
- It can be automatically invoked by the HHB tool when running quantized and compiled neural networks on RISC-V.

## Relationships

- The [[k230]] SoC integrates XuanTie C908 cores, which are targets for SHL-optimized routines.
- The [[allwinner_v853]] SoC includes a Xuantie E907 core, another RISC-V core in the XuanTie family that may benefit from SHL.

## Sources

- https://github.com/openvinotoolkit/shl
