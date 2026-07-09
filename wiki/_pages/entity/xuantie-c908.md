---
canonical_name: XuanTie C908
aliases:
- C908
- T-Head XuanTie C908
subtype: null
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.9
  self_containedness: 0.8
  bridge_score: 0.6
  hub_potential: 0.2
sources:
- raw/cache/ea9a8780b4178053.md
- https://riscv.org/blog/xuantie-c908-accelerates-ai-with-software-and-hardware-fusion/
source_url: https://riscv.org/blog/xuantie-c908-accelerates-ai-with-software-and-hardware-fusion/
fetched_at: '2026-07-09T03:12:47.689294+00:00'
type: entity
created: '2026-07-09'
updated: '2026-07-09'
cold_start: true
inbound_links: 0
outbound_links:
- target: ara
  reason: Both XuanTie C908 and Ara implement the RISC-V Vector Extension version
    1.0, but XuanTie C908 is a commercial processor from T-Head with integrated AI
    acceleration features, while Ara is an open-source research vector unit from the
    PULP platform
---

# XuanTie C908

XuanTie C908 is a RISC-V processor developed by T-Head Semiconductor, designed for AI inference workloads at the edge. Operating at a frequency of up to 2 GHz, it is compliant with the RISC-V Vector Extension version 1.0 and supports configurable vector register widths of 128 or 256 bits. The processor includes vector execution units for FP16, BFP16, FP32, INT8, INT32, and INT64 operations, as well as INT8 and INT4 vector dot product instructions for integer neural network acceleration. It is accompanied by the Structure of Heterogeneous Library (SHL) for optimized neural network operators and the Heterogeneous Honey Badger (HHB) deployment tool for model quantization and code generation. XuanTie C908 targets visual AI, intelligent interaction, and other advanced AIoT applications.

## Key Claims

- Operates at a maximum frequency of 2 GHz.
- Fully compliant with the RISC-V Vector Extension version 1.0.
- Configurable vector register width: supports either 128-bit or 256-bit VLEN.
- Vector execution unit supports FP16, BFP16, FP32, INT8, INT32, and INT64 operations, plus INT8 and INT4 vector dot product instructions.
- SHL (Structure of Heterogeneous Library) provides assembly-optimized neural network operators including conv2d, depthwise conv2d, maxpool2d, avgpool2d, fullyconnected, relu, softmax, elementwise ops, and more.
- HHB (Heterogeneous Honey Badger) supports int8 asymmetric weight/activation quantization and fp16 quantization, with a simple command-line interface to generate C code for inference.
- Performance numbers: INT8 vector dot product yields 3.35x speedup on MobileNet; extending vector length to 256 bits yields an additional 1.55–1.68x speedup; XuanTie C908 at VLEN128 is 3.75–4.57x faster than the previous-generation XuanTie C906.

## Relationships

- [[ara]]: Both XuanTie C908 and Ara implement the RISC-V Vector Extension version 1.0, but XuanTie C908 is a commercial processor from T-Head with integrated AI acceleration features, while Ara is an open-source research vector unit from the PULP platform.

## Sources

- [XuanTie C908 Accelerates AI with Software and Hardware Fusion](raw/cache/ea9a8780b4178053.md)
