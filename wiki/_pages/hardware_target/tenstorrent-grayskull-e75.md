---
canonical_name: Tenstorrent Grayskull e75
aliases:
- Grayskull e75
- Grayskull
- Tenstorrent Grayskull e150
- Grayskull e150
- TT Grayskull e150
subtype: null
tags: []
hardware_targets:
- Tenstorrent Grayskull e75
toolchains: []
constraints: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.6
  self_containedness: 0.7
  bridge_score: 0.7
  hub_potential: 0.5
sources:
- raw/cache/0f397fff796e4aa1.md
- https://link.springer.com/chapter/10.1007/978-3-032-07612-0_10
- raw/cache/52612464b0ae26b5.md
- https://www.research.ed.ac.uk/en/publications/accelerating-stencils-on-the-tenstorrent-grayskull-risc-v-acceler
source_url: https://link.springer.com/chapter/10.1007/978-3-032-07612-0_10
fetched_at: '2026-07-02T10:04:18.333789+00:00'
type: hardware_target
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# Tenstorrent Grayskull e75

Tenstorrent Grayskull e75 is a commercial RISC-V-based accelerator designed for AI and high-performance computing workloads, built on a software-defined tensor streaming multiprocessor architecture. It features a dataflow execution model that enables efficient pipelining and reduced data movement for matrix multiplication and other linear algebra kernels. The accelerator supports multiple numerical precisions, including BF16, FP16, and INT8, and is optimized for workload-specific grid sizes and matrix dimensions. As characterized in a 2025 ISC High Performance conference paper by Pizzini Cavagna et al., the Grayskull e75 achieves a peak efficiency of 1.55 TFLOPs/Watt with BF16 precision on matrix multiplication workloads. The architecture competes with traditional GPU and CPU-based accelerators, offering a differentiated trade-off between computational throughput and power consumption. Initial evaluations highlight the importance of grid size, matrix dimensions, data format, and numerical precision on overall efficiency. The Grayskull e75 is part of Tenstorrent's line of RISC-V accelerators aimed at democratizing AI hardware.

## Key Claims

- Tenstorrent Grayskull e75 is a RISC-V accelerator with a dataflow execution model optimized for matrix operations.
- Supports BF16 precision and achieves 1.55 TFLOPs/Watt peak efficiency on matrix multiplication.
- Performance characterized through detailed study of grid size, matrix dimensions, data format, and numerical precision.
- Competitive power efficiency compared to NVIDIA V100 and A100 GPUs and Intel Sapphire Rapids processors, though raw throughput is lower than NVIDIA GPUs.

## Optimization-Relevant Details

- ISA/profile: RISC-V based; specifics of vector extensions not detailed in source.
- Vector/matrix/accelerator support: Dataflow execution model with configurable grid and matrix dimensions.
- Memory/cache/TLB/DMA: Not detailed in the available source.
- Compiler/toolchain support: Not detailed; paper references Tenstorrent's GitHub repository for software support.

## Relationships

- [[cpa-factored-gemmini-systolic-array]]: Comparison architecture for systolic array-based acceleration; both target ML workloads with different design philosophies.
- [[tenstorrent-grayskull-e75-matmul-bf16-benchmark]]: Benchmark result page for the peak efficiency measurement.

## Sources

- [Assessing Tenstorrent’s RISC-V MatMul Acceleration Capabilities](https://link.springer.com/chapter/10.1007/978-3-032-07612-0_10)
