---
cold_start: true
constraints:
- 120 Tensix cores
- 10x12 core grid
- Torus NoC topology
- 1 MB SRAM per core
- 120 MB total SRAM
- Bfloat16 data format
- 32x32 tile operations
- 1.2 GHz clock
- 200 W power
- 8 GB LPDDR4 memory
- 118.4 GB/s DRAM bandwidth
- 192 GB/s NoC bandwidth per core
- 384 GB/s SRAM bandwidth per core
- PCIe 4.0 x16
- 12 nm process node
- 477 mm^2 core grid area
created: '2025-04-09'
hardware_targets:
- Tenstorrent Grayskull e150
inbound_links: 2
scorecard:
  bridge_score: 0.6
  claim_density: 0.9
  hub_potential: 0.5
  novelty_delta: 0.9
  self_containedness: 0.8
sources:
- https://arxiv.org/abs/2407.13885
tags:
- Tenstorrent
- Grayskull
- RISC-V
- dataflow
- AI accelerator
toolchains:
- TT-Buda
- TT-Metalium
- PyTorch
- TensorFlow
- Apache TVM
type: hardware_target
updated: '2026-06-29'
---

# Tenstorrent Grayskull e150

The Tenstorrent Grayskull e150 is a PCIe 4.0 x16 dataflow accelerator card built on the Tenstorrent Grayskull architecture, designed for AI workloads such as Transformer self-attention. It features a 10×12 grid of 120 Tensix cores, each containing 1 MB of SRAM for a total of 120 MB of on-chip SRAM, with a peak SRAM bandwidth of 384 GB/s per core and an aggregate bandwidth of approximately 46 TB/s when all cores access their local SRAM in parallel. The cores are interconnected via a two-dimensional torus Network-on-Chip (NoC) with a per-core bandwidth of 192 GB/s. The Grayskull e150 operates at a maximum clock speed of 1.2 GHz and a thermal design power of 200 W. It supports tiled computations using 32×32 scalar tiles in Bfloat16 format and employs a dataflow architecture where each Tensix core executes instructions based on data availability. The card includes 8 GB of LPDDR4 DRAM with 118.4 GB/s bandwidth and is fabricated using a 12 nm process with a core grid area of 477 mm². The Tenstorrent Grayskull e150 is approximately 30× cheaper than the Nvidia H100 PCIe, while offering 1.5× more SRAM than the H100's 80 MB combined L1/L2.

## Key Claims

- The Grayskull e150 provides 120 MB of distributed SRAM across 120 Tensix cores, significantly larger than the 80 MB of combined L1 and L2 SRAM on the Nvidia H100 PCIe.
- Each Tensix core includes 1 MB of SRAM with 384 GB/s bandwidth and is connected to the torus NoC at 192 GB/s.
- The architecture is a dataflow design where five RISC-V cores per Tensix drive data movement and computation in parallel.
- The Bfloat16 format is natively supported with tiled 32×32 operations.
- The card is commercially available as a PCIe 4.0 x16 form factor at a cost approximately 30× lower than the H100 PCIe.

## Optimization-Relevant Details

- ISA/profile: Each Tensix core includes five RISC-V cores (RV32IM? not specified), two routers, a data movement engine, and a compute engine with FPU and SFPU.
- Vector/matrix/accelerator support: Tiled 32×32 Bfloat16 operations; matrix engine (FPU) and vector engine (SFPU) per core.
- Memory/cache/TLB/DMA: 1 MB SRAM per core with 384 GB/s bandwidth; 8 GB LPDDR4 at 118.4 GB/s; no traditional cache hierarchy; data movement via packer/unpacker routers and circular buffers in SRAM.
- Compiler/toolchain support: TT-Buda (high-level, PyTorch/TensorFlow via Apache TVM) and TT-Metalium (low-level C++).

## Relationships

- [[Gemmini_Architecture]] – Another RISC-V-based DNN accelerator, highlighting different architectural approaches (systolic array vs. dataflow grid).
- [[Parallel_GEMM_Convolution_on_GAP8]] – An optimization recipe targeting a different RISC-V processor, illustrating alternative memory hierarchy strategies (scratchpad vs. distributed SRAM).

## Sources

- arXiv:2407.13885 – Attention in SRAM on Tenstorrent Grayskull

Note: Insufficient context for additional cross-links to entity pages; no entity pages exist in the current wiki.
