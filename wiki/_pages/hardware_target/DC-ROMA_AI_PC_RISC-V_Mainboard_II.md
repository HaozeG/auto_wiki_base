---
cold_start: true
constraints:
- 8-core
- 1.8 GHz
- 32GB RAM
- 512GB SSD
created: '2025-10-10'
hardware_targets:
- DC-ROMA AI PC RISC-V Mainboard II
- SiFive P550
inbound_links: 0
scorecard:
  bridge_score: 0.7
  claim_density: 1.0
  hub_potential: 0.6
  novelty_delta: 1.0
  self_containedness: 1.0
sources:
- https://github.com/geerlingguy/sbc-reviews/issues/82
tags:
- RISC-V
- SiFive P550
- DC-ROMA
- AI PC
- Framework Laptop
toolchains: []
type: hardware_target
updated: '2026-06-28'
---

# DC-ROMA AI PC RISC-V Mainboard II

The DC-ROMA AI PC RISC-V Mainboard II is a mainboard designed for the Framework Laptop 13, powered by an 8-core 1.8 GHz SiFive P550 CPU with 32GB of RAM (16GB allocated to the CPU) and a 512GB ZHITAI TiPlus7100 SSD. It runs Ubuntu 24.04 with kernel 6.6.92-eic7x-2025.07 and includes a PowerVR A-Series AXM-8-256 GPU with OpenGL ES 3.2 and Vulkan support. The board is produced by DeepComputing and targets AI PC workloads with RISC-V architecture. The mainboard also features built-in WiFi 6 via Intel AX200 and provides a range of I/O including M.2 storage. The tested configuration achieved a Geekbench 6 score of 174 single-core and 640 multi-core, with a peak power draw of 32.9W during HPL benchmark.

## Key Claims

- 8-core SiFive P550 CPU at 1.8 GHz running RISC-V 64-bit.
- 32GB RAM (16GB for CPU), 512GB SSD.
- Ubuntu 24.04 with Linux kernel 6.6.92-eic7x-2025.07.
- PowerVR A-Series AXM-8-256 GPU with OpenGL ES 3.2 and Vulkan drivers.
- Glmark2 score of 936.
- WiFi 6 (Intel AX200) with iperf3 throughput up to 637 Mbps.
- Sleep power draw 2.2W, idle 25.1W, maximum load 32.9W.
- Mainboard starts at $349 (32GB/No SSD).

## Optimization-Relevant Details

- ISA/profile: RISC-V 64-bit (rv64gcv? not specified; kernel shows riscv64 with EIC7X extensions)
- Vector/matrix/accelerator support: CPU does not explicitly mention vector extension; GPU is PowerVR AXM-8-256.
- Memory/cache/TLB/DMA: 32GB DDR? Not specified; 512GB NVMe SSD.
- Compiler/toolchain support: Ubuntu default GCC; Geekbench 6 uses its own.

## Relationships

- [[T-HEAD_C910_SPEC_CPU_Benchmark]] – Both are high-performance RISC-V CPU benchmarks, though using different core architectures.
- [[Sipeed_MAIX_series]] – Both are RISC-V development platforms, but the Sipeed MAIX uses a lower-power K210 with NPU for edge AI.

## Sources

- [geerlingguy/sbc-reviews Issue #82 - DC-ROMA AI PC - RISC-V Mainboard II](https://github.com/geerlingguy/sbc-reviews/issues/82)
