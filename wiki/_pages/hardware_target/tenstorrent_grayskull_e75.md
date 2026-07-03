---
canonical_name: Tenstorrent Grayskull e75
aliases:
- Grayskull e75
- Grayskull
- Tenstorrent Grayskull
- Grayskull e75 accelerator
- Grayskull e150
- Tenstorrent Grayskull Dev Kit
subtype: null
tags: []
hardware_targets:
- Tenstorrent Grayskull e75
toolchains: []
constraints:
- 12nm process
- 1 GHz clock
- 8 GB LPDDR4 memory
- 102.4 GB/s memory bandwidth
- 55 TFLOPs FP16 peak
- 96 Tensix cores
- RISC-V (proprietary baby cores)
scorecard:
  novelty_delta: 0.9
  claim_density: 0.85
  self_containedness: 0.9
  bridge_score: 0.6
  hub_potential: 0.7
sources:
- raw/cache/2bb619b763be17f7.md
- https://arxiv.org/html/2505.06085v1
- raw/cache/f44e7b65c26d8ecf.md
- https://arxiv.org/html/2505.06085
- raw/cache/df18e54edc7608f6.md
- https://www.techradar.com/pro/firm-headed-by-legendary-chip-architect-behind-amd-zen-finally-releases-first-hardware-days-after-being-selected-to-build-the-future-of-ai-in-japan-tenstorrent-unveils-grayskull-its-risc-v-answer-to-gpus
- raw/cache/1a940b93ad0e4c31.md
- https://gigazine.net/gsc_news/en/20240311-jim-keller-tenstorrent-grayskull-e75-e150/
source_url: https://arxiv.org/html/2505.06085v1
fetched_at: '2026-07-02T05:05:34.906383+00:00'
type: hardware_target
created: '2026-07-02'
updated: '2026-07-02'
cold_start: false
inbound_links: 1
needs_summary_revision: false
outbound_links:
- target: xuantie_c908
  reason: A RISC-V core with vector extensions for AI inference, representing an alternative
    microarchitecture compared to Grayskull's Tensix grid approach
- target: k230
  reason: An SoC integrating RISC-V C908 cores with a KPU, offering a different balance
    of CPU and dedicated AI accelerator for edge AI
- target: grayskull_e75_matmul_benchmark
  reason: the matmul-kernel measurement results (tiling, kernel-compile, data-transfer
    time breakdown) for this card
- target: tile_language
  reason: a Pythonic, TVM-based DSL for GPU/CPU AI kernel authoring, illustrating
    a compiler-driven alternative to Grayskull's custom kernel-compilation path
- target: edge_ai_soc_design_space
  reason: a synthesis page comparing Grayskull's tile-grid-with-embedded-RISC-V-control
    approach against K230's fixed-function KPU, ET-SoC-1's many-core design, Semidynamics'
    vector extension, and Rockchip RK3588's ARM+NPU alternatives
---

# Tenstorrent Grayskull e75

The Tenstorrent Grayskull e75 is a RISC-V based AI accelerator card designed to efficiently execute matrix multiplication and other linear algebra kernels common in large language model inference. It employs a grid of 96 Tensix processing cores, each integrating five programmable RISC-V baby cores, a 1 MB local SRAM, a SIMD Matrix & Vector engine, and Network-on-Chip (NoC) routers for inter-core communication. Fabricated on a 12 nm process, the card operates at 1 GHz and is equipped with eight LPDDR4 memory channels providing 8 GB of capacity and a bandwidth of 102.4 GB/s. The architecture separates communication from computation to maximize overlap, achieving a peak performance of 55 TFLOPs for FP16 operations. The Grayskull e75 supports reduced-precision formats such as BF16, and its energy efficiency has been measured at 1.55 TFLOPs/Watt, making it competitive with contemporary GPU and CPU solutions for AI workloads.

## Key Claims

- 96 Tensix cores operating at 1 GHz, each with 5 RISC-V baby cores.
- Peak FP16 throughput: 55 TFLOPs.
- Memory subsystem: 8 GB LPDDR4, 102.4 GB/s bandwidth.
- Peak energy efficiency: 1.55 TFLOPs/Watt with BF16.
- First-run execution time is dominated by tiling (31%) and kernel compilation (66%); subsequent runs are dominated by data transfer (62%).

## Optimization-Relevant Details

- ISA/profile: RISC-V (proprietary baby cores)
- Vector/matrix/accelerator support: SIMD Matrix & Vector engine per core
- Memory/cache/TLB/DMA: 1 MB SRAM per core, 8 GB LPDDR4 global DRAM, NoC routers
- Compiler/toolchain support: Not specified in source; paper uses custom kernel compilation; likely uses Tenstorrent's software stack (TT-Metalium or TT-BUDA) but not confirmed.

## Relationships

- [[xuantie_c908]]: A RISC-V core with vector extensions for AI inference, representing an alternative microarchitecture compared to Grayskull's Tensix grid approach.
- [[k230]]: An SoC integrating RISC-V C908 cores with a KPU, offering a different balance of CPU and dedicated AI accelerator for edge AI.
- [[grayskull_e75_matmul_benchmark]]: the matmul-kernel measurement results (tiling, kernel-compile, data-transfer time breakdown) for this card.
- [[tile_language]]: a Pythonic, TVM-based DSL for GPU/CPU AI kernel authoring, illustrating a compiler-driven alternative to Grayskull's custom kernel-compilation path.
- [[edge_ai_soc_design_space]]: a synthesis page comparing Grayskull's tile-grid-with-embedded-RISC-V-control approach against K230's fixed-function KPU, ET-SoC-1's many-core design, Semidynamics' vector extension, and Rockchip RK3588's ARM+NPU alternatives.

## Sources

- https://arxiv.org/html/2505.06085v1
