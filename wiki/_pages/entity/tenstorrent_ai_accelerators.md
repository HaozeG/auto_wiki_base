---
cold_start: true
created: '2026-07-10'
inbound_links: 0
scorecard:
  bridge_score: null
  claim_density: null
  hub_potential: null
  novelty_delta: null
  self_containedness: null
sources:
- linkedin.com/posts/emi-andere_tenstorrent-ships-ai-accelerator-cards
- tenstorrent.com/cards
- tenstorrent.com/tt-forge
- awesome-agents.github.io/tenstorrent-blackhole-p150a
- github.com/tenstorrent/tt-forge
tags:
- risc-v
- ai-accelerator
- open-source
- tensix
- tenstorrent
type: entity
updated: '2026-07-10'
---

# Tenstorrent AI Accelerators

Tenstorrent is a company that designs AI accelerator cards which combine open RISC-V CPU cores with proprietary Tensix tensor compute units. Its current product line includes the Wormhole accelerator (already shipping) and the Blackhole accelerator (recently launched). These accelerators are supported by a fully open-source software stack, providing two SDKs: TT-Buda for high-level model deployment and TT-Metalium for low-level kernel development. Additionally, TT-Forge is an MLIR-based open-source compiler that accepts models from PyTorch, JAX, ONNX, and other frameworks, compiling them for Tenstorrent hardware. The processors can be networked into multichip mesh configurations for workstations and servers, such as the Galaxy system. Tenstorrent differentiates itself from other AI-accelerator vendors by using an open RISC-V instruction set architecture and by making its entire software stack publicly available, in contrast to proprietary ISAs and closed-source stacks from competitors. The company reports that over 800 model variants are tested in continuous integration and thousands more have been run internally, with the goal that any model fitting in memory will execute on their hardware.

## Key Claims

- Tenstorrent's AI accelerators combine RISC-V CPU cores with proprietary Tensix tensor compute units.
- Current product line: Wormhole (shipping) and Blackhole (recently launched).
- Two open-source SDKs: TT-Buda (high-level) and TT-Metalium (low-level).
- TT-Forge is an MLIR-based open-source compiler, in public beta, supporting PyTorch, JAX, ONNX, and more.
- The processors can be networked into a multichip mesh for workstations and servers (Galaxy).
- Over 800 model variants tested in CI, thousands more run internally; any model fitting memory should run.
- The entire software stack is open source.
- Tenstorrent uses open RISC-V CPU IP, differentiating from proprietary ISAs used by competitors.
- In TT-Metalium, developers write three separate kernels (reader, compute, writer) that move data through a Network-on-Chip.
- Two open-source SDKs enable either high-level (TT-Buda) or low-level (TT-Metalium) development.

## Relationships

- [[fpga_riscv_isa_extension_nn_inference]]: FPGA-based RISC-V ISA extensions for neural network inference represent a prototyping methodology; Tenstorrent provides a commercial production implementation of RISC-V-based AI acceleration with proprietary Tensix cores.
- [[riscv_ai_ecosystem]]: Tenstorrent is a key commercial actor in the RISC-V AI ecosystem, contributing open-source compilers and SDKs.
- [[sifive_intelligence_x280]]: While SiFive provides production RVV IP, Tenstorrent customizes its own CPU cores and tensor units rather than adopting off-the-shelf vector processors.
- [[risc_v_vector_extension]]: Tenstorrent's approach is complementary; it uses RISC-V cores for control while offloading tensor operations to Tensix compute units, rather than implementing vector ISA extensions directly.

## Sources

- LinkedIn post by Emi Andere (12 Feb 2026) describing TT-Metalium kernel structure.
- tenstorrent.com/cards: Product page for Wormhole and Blackhole cards, multichip networking, and open-source SDKs.
- tenstorrent.com/tt-forge: TT-Forge compiler page describing MLIR-based open-source compiler in public beta.
- Awesome Agents GitHub entry for Tenstorrent Blackhole p150a.
- github.com/tenstorrent/tt-forge: Repository for TT-Forge compiler.
- Qualcomm's Tenstorrent bid article (Mar 1, 2026) summarizing Tenstorrent's differentiation: RISC-V cores, open-source stack, 800+ model variants.

