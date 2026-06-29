---
cold_start: false
constraints:
- 64 Tensix cores
- 12 GB GDDR6 memory via 192-bit bus
- QSFP-DD ports (up to 200 Gbps each)
- PCIe 4.0 x16 interface
- 5 RISC-V baby cores per Tensix core
- 1.5 MB SRAM per Tensix core
- 'Baby RISC-V clock: 1 GHz'
- NoC for inter-tile communication
created: '2025-09-01'
hardware_targets:
- Tenstorrent Wormhole n300
inbound_links: 5
needs_summary_revision: false
scorecard:
  bridge_score: 0.7
  claim_density: 0.7
  hub_potential: 0.6
  novelty_delta: 0.8
  self_containedness: 0.8
sources:
- https://arxiv.org/html/2509.19294v1
tags:
- RISC-V
- Tenstorrent
- Wormhole
- AI accelerator
toolchains:
- TT-Metalium
type: hardware_target
updated: '2026-06-29'
---

# Tenstorrent Wormhole n300

The Tenstorrent Wormhole n300 is a RISC-V-based AI accelerator ASIC designed for high-performance computing and artificial intelligence workloads. It features 64 Tensix processing cores arranged in a grid, each containing five embedded 32-bit RISC-V baby cores for control and coordination, a high-throughput tensor math unit (FPU), a wide SIMD engine (SFPU), and 1.5 MB of SRAM. The chip connects to 12 GB of GDDR6 memory via a 192-bit memory bus, provides two QSFP-DD ports for up to 200 Gbps bidirectional data transfer, and uses a PCIe 4.0 x16 interface for host connectivity. The architecture is optimized for efficient data movement through a Network-on-Chip (NoC) and supports the TT-Metalium low-level programming interface. This hardware has been used to accelerate astrophysical N-body simulations, achieving over 2Ã speedup and approximately 2Ã energy savings compared to optimized CPU implementations.

## Key Claims

- The Wormhole n300 integrates 64 Tensix cores, each with 5 RISC-V baby cores (32-bit, in-order, single-issue, 1 GHz) for data movement and compute control.
- Each Tensix core has 1.5 MB SRAM, a tensor FPU, and a SIMD engine (SFPU).
- Memory subsystem: 12 GB GDDR6 via 192-bit bus, high-bandwidth access.
- I/O: dual QSFP-DD (200 Gbps each), PCIe 4.0 x16.
- Programming via TT-Metalium SDK, which exposes data movement and compute kernels.
- Demonstrated >2Ã speedup and ~2Ã energy savings for gravitational N-body simulations relative to CPU.

## Optimization-Relevant Details

- ISA/profile: RISC-V (baby cores are 32-bit RV32, but main compute via FPU/SFPU).
- Vector/matrix/accelerator support: Tensor FPU for matrix arithmetic, SFPU for vector operations.
- Memory/cache/TLB/DMA: SRAM per core, GDDR6 via NoC, DMA via data movement cores.
- Compiler/toolchain support: TT-Metalium SDK (low-level), also supports C++ kernels compiled to the baby RISC-V cores.

## Relationships

- [[N_Body_Simulation_on_Tenstorrent_Wormhole_Benchmark]] – Benchmark results for N-body simulation on this hardware.
- [[Parallel_GEMM_Convolution_on_GAP8]] – Another RISC-V accelerator optimization recipe for comparison.

## Sources

- [Accelerating Gravitational N-Body Simulations Using the RISC-V-Based Tenstorrent Wormhole (arXiv:2509.19294)](https://arxiv.org/html/2509.19294v1)

