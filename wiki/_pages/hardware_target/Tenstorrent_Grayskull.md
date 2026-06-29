---
cold_start: false
constraints:
- 32x32 tile operation
- explicit tile register management
- circular buffer communication
- requires batch=32 for full utilization
- 5 RISC-V cores per Tensix
- no hardware protection for code/data SRAM
- explicit acquire/release of tile registers
created: '2025-04-08'
hardware_targets:
- Tenstorrent Grayskull
inbound_links: 1
needs_summary_revision: false
scorecard:
  bridge_score: 0.6
  claim_density: 0.8
  hub_potential: 0.5
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://clehaxze.tw/gemlog/2024/06-02-thoughts-and-logs-after-messing-with-tenstorrent-grayskull.gmi
tags:
- Tenstorrent
- Grayskull
- AI accelerator
- TT-Metalium
- TT-BUDA
toolchains:
- TT-Metalium
- TT-BUDA
type: hardware_target
updated: '2026-06-29'
---

# Tenstorrent Grayskull

Tenstorrent Grayskull is an AI accelerator architecture designed by Tenstorrent, featuring a grid of Tensix cores each containing five single-issue RISC-V cores. Two of these RISC-V cores handle data movement while three control a SIMD and tensor engine that operates on 32x32 matrix tiles. The hardware uses explicit tile registers and circular buffers for intra-Tensix communication, requiring developers to manually manage data flow between SRAM, tile registers, and the compute units. This programming model, exposed through the low-level TT-Metalium framework and the higher-level TT-BUDA stack, prioritizes software-pipelined parallelism over traditional GPU-style dynamic warp scheduling. The Grayskull architecture also includes no hardware protection between code and data in SRAM, making hangs and deadlocks common during development. This hands-on experience report describes the setup, programming model, and limitations encountered while working with the Grayskull card on an Arch Linux system, including dependency workarounds for TT-BUDA.

## Key Claims

- Metalium provides complete, low-level access to Grayskull hardware, enabling custom kernel development.
- The programming model requires explicit tile register management: load, compute, store, with acquire/release semantics.
- Software pipelining is achieved by decoupling data movement and compute across the five RISC-V cores per Tensix.
- The architecture operates on 32x32 matrix tiles, which forces language model inference to run at batch=32 for full utilization (batch=1 yields 1/32 utilization).
- TT-BUDA is a high-level stack that loads models from PyTorch, TensorFlow, and ONNX, analogous to NVIDIA TensorRT.
- Hangs are common due to lack of hardware SRAM protection; bad memory writes can corrupt instructions and require board reset.
- Circular buffer misconfiguration leads to deadlocks.
- Official support is limited to Ubuntu 20.04; using Arch Linux required patching and custom package builds.

## Optimization-Relevant Details

- ISA/profile: Custom RISC-V cores (5 per Tensix) with SIMD and tensor engine.
- Vector/matrix/accelerator support: Tile-based matrix operations on 32x32 tiles.
- Memory/cache/TLB/DMA: SRAM per Tensix, DRAM shared across grid, explicit data movement via NOC and DMA.
- Compiler/toolchain support: TT-Metalium (low-level), TT-BUDA (high-level, supports PyTorch/TF/ONNX).

## Relationships

- [[Gemmini_Architecture]] – A contrasting open-source DNN accelerator generator for RISC-V, using systolic arrays and configurable dataflows.
- [[Parallel_GEMM_Convolution_on_GAP8]] – A different approach to AI acceleration on multicore RISC-V with scratchpad memory and explicit DMA, providing a comparison point for programming models.

## Sources

- [Thoughts and logs after messing with Tenstorrent Grayskull](https://clehaxze.tw/gemlog/2024/06-02-thoughts-and-logs-after-messing-with-tenstorrent-grayskull.gmi)
