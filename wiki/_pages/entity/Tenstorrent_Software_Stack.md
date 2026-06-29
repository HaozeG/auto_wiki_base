---
cold_start: true
created: '2026-07-02'
inbound_links: 1
scorecard:
  bridge_score: 0.8
  claim_density: 0.7
  hub_potential: 0.9
  novelty_delta: 0.8
  self_containedness: 0.9
sources:
- https://deepwiki.com/tenstorrent/tenstorrent.github.io/3.2-software-stack
- core/getting-started/tt-software-stack.md
- https://deepwiki.com/tenstorrent/tt-forge
tags:
- Tenstorrent
- TT-Forge
- TT-Metalium
- TT-NN
- MLIR
- RISC-V
- AI compiler
type: entity
updated: '2026-06-29'
---

# Tenstorrent Software Stack

The Tenstorrent software stack is a multi-layered platform for programming, optimizing, and running AI workloads on Tenstorrent hardware. At the lowest level, TT-Metalium provides a low-level software stack—analogous to CUDA or ROCm—that exposes the RISC-V processors and Network-on-Chip (NoC) within each Tensix core for direct bare-metal programming. Building on TT-Metalium, TT-Forge is an open-source, MLIR-based compiler that integrates with high-level machine learning frameworks such as PyTorch, JAX, and ONNX. The stack also includes TT-NN, an operator library, and a User-Mode Driver (TT-UMD) for hardware access from user-space applications. This layered design enables development from low-level C kernels running on the RISC-V baby cores to high-level model compilation targeting the entire device.

## Key Claims

- TT-Forge is an open-source, MLIR-based compiler that serves as a central hub for integrating AI/ML frameworks with Tenstorrent hardware.
- TT-Forge exposes the RISC-V processors and the Network-on-Chip (NoC) within each Tensix core, allowing direct control of data movement and computation.
- TT-Metalium is the foundational low-level stack, described as the CUDA or ROCm equivalent for Tenstorrent hardware.
- TT-Forge is built on top of TT-Metalium and works with PyTorch, JAX, ONNX, and other frameworks.
- The stack includes TT-NN operator library and TT-UMD (User-Mode Driver) for low-level hardware interaction.
- The software stack consists of multiple layers that enable developers to program, optimize, and run workloads on Tenstorrent hardware.
- TT-Forge is in public beta and open to community contributions via pull requests and Discord.

## Relationships

- [[Tenstorrent_Grayskull_e150]] – The Grayskull e150 accelerator card is programmed through the Tenstorrent software stack, with TT-Metalium providing direct hardware access and TT-Buda (a precursor) supporting high-level framework integration. The stack abstracts the 120 Tensix core grid and torus NoC for both low-level and compiler-driven workflows.
- [[Gemmini_Architecture]] – Gemmini is a different DNN accelerator generator with its own multi-level software stack (C, assembly, PyTorch, TVM). Comparing Gemmini’s approach—using a systolic array with TVM integration—against Tenstorrent’s dataflow grid with TT-Forge/MLIR highlights contrasting strategies for accelerating neural networks on custom hardware.

## Sources

- [DeepWiki: Software Stack | tenstorrent/tenstorrent.github.io](https://deepwiki.com/tenstorrent/tenstorrent.github.io/3.2-software-stack)
- [Tenstorrent design documentation: core/getting-started/tt-software-stack.md](core/getting-started/tt-software-stack.md)
- [DeepWiki: tenstorrent/tt-forge](https://deepwiki.com/tenstorrent/tt-forge)
- [TT-Metal: Programming Tenstorrent Hardware (Reddit summary)](https://www.reddit.com/.../gpu_ttmetal_programming_tenstorrent_hardware_from_a/)

