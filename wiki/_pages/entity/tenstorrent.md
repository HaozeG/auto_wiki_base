---
canonical_name: Tenstorrent
aliases:
- Tenstorrent AI
- TT (Tenstorrent)
subtype: null
tags: []
scorecard:
  novelty_delta: 0.8
  claim_density: 0.6
  self_containedness: 0.9
  bridge_score: 0.8
  hub_potential: 0.9
sources:
- raw/cache/e705f3dbec0a731a.md
- https://github.com/tenstorrent
source_url: https://github.com/tenstorrent
fetched_at: '2026-07-09T10:03:59.018648+00:00'
type: entity
created: '2026-07-09'
updated: '2026-07-09'
cold_start: true
inbound_links: 1
outbound_links:
- target: blackhole
  reason: Tenstorrent develops the Blackhole AI accelerator, which is built on the
    Tensix core architecture and is the latest generation chip in the Tenstorrent
    product lineup. The TT-Metal and TT-NN software stacks provide the programming
    interface for Blackhole hardware
---

# Tenstorrent

Tenstorrent is a company that builds computers for AI, bringing together experts in computer architecture, chip design, systems, software, and compilers to develop next-generation computing hardware and open-source software. Its GitHub organization hosts several key projects: TT-Forge, an MLIR-based compiler for deploying AI models on Tenstorrent hardware; TT-NN, an operator library for neural networks; TT-Metal, a tile-native programming model for low-level kernel development; and TT-LLK, a low-level kernel library. Tenstorrent also contributes to the RISC-V ecosystem with projects including Riescue (a directed test framework and library), RISC-V architecture tests, the Whisper instruction set simulator, and a RISC-V core design verification kit. The company provides toolchains (GCC, LLVM), developer tools (QEMU), and open specifications for its Tensix AI IP, including an open ISA specification and a high-level simulator. The Tenstorrent hardware lineup features the Blackhole third-generation AI accelerator chip and the earlier Wormhole generation, all built around the Tensix core architecture. This open-source ecosystem enables researchers and developers to program Tenstorrent hardware at multiple levels of the software stack.

## Key Claims

- Tenstorrent builds AI computers and develops open-source software stacks including TT-Forge (MLIR-based compiler), TT-NN (operator library), TT-Metal (tile-native programming model), and TT-LLK (low-level kernel library).
- The company contributes RISC-V projects: Riescue (directed test framework), RISC-V architecture tests, Whisper (instruction set simulator), and RISC-V core design verification kit.
- Tenstorrent provides GCC and LLVM toolchains, QEMU emulation, and open specifications for its Tensix AI IP (ISA specification and high-level simulator).
- Tenstorrent hardware includes the Blackhole chip (third-generation AI accelerator with up to 120 Tensix cores on Samsung 6nm) and the earlier Wormhole generation.

## Relationships

- [[blackhole]]: Tenstorrent develops the Blackhole AI accelerator, which is built on the Tensix core architecture and is the latest generation chip in the Tenstorrent product lineup. The TT-Metal and TT-NN software stacks provide the programming interface for Blackhole hardware.

## Sources

- https://github.com/tenstorrent
