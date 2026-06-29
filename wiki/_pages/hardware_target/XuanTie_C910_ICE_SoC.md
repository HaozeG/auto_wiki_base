---
cold_start: true
constraints:
- dual-core 1.2GHz
- RV64GCV
- 12-stage pipeline
- 3-issue superscalar out-of-order
- up to 64KB I-cache and D-cache per core
- up to 8MB L2 cache
- Vivante GC8000UL GPU
- DPU (NPU)
- 4GB LPDDR4
- 16GB eMMC
- Gigabit Ethernet
- WiFi/Bluetooth
- Android 10
- Debian 11
created: '2021-10-13'
hardware_targets:
- XuanTie C910 ICE SoC
inbound_links: 0
scorecard:
  bridge_score: 0.5
  claim_density: 0.6
  hub_potential: 0.5
  novelty_delta: 0.9
  self_containedness: 0.8
sources:
- https://linuxgizmos.com/dev-kit-debuts-risc-v-xuantie-c910-soc-with-a-3d-gpu-and-android-and-linux-support/
tags:
- RISC-V
- XuanTie
- C910
- GPU
- NPU
- Alibaba T-Head
toolchains: []
type: hardware_target
updated: '2026-06-29'
---

# XuanTie C910 ICE SoC

The XuanTie C910 ICE SoC is a RISC-V-based system-on-chip developed by Alibaba T-Head, featuring dual XuanTie C910 cores clocked at 1.2 GHz with RV64GCV vector extensions, a Vivante GC8000UL 3D GPU, and a deep-learning processor unit (DPU) for AI acceleration. The SoC supports Android 10 and Debian 11 and is integrated into the RVB-ICE development kit, which includes 4GB LPDDR4 RAM, 16GB eMMC storage, Gigabit Ethernet, WiFi/Bluetooth, and a 7-inch touchscreen display. The C910 core is a 12-stage pipelined, 3-issue superscalar out-of-order design with up to 64KB instruction and data caches and up to 8MB L2 cache. The SoC represents a commercially available RISC-V platform with integrated 3D GPU capability, enabling Android AOSP support on RISC-V hardware.

## Key Claims

- Dual-core XuanTie C910 processor at 1.2 GHz with RV64GCV extensions.
- Vivante GC8000UL GPU for 3D graphics acceleration.
- DPU (NPU) for deep learning and AI/ML tasks (TOPS not specified).
- Supports Android 10 and Debian 11 operating systems.
- First commercially available RISC-V SoC with an integrated 3D GPU.
- C910 core: 12-stage pipeline, 3-issue superscalar out-of-order, up to 64KB I/D cache, up to 8MB L2 cache.
- RVB-ICE dev kit includes 4GB LPDDR4, 16GB eMMC, microSD slot, GbE, WiFi/BT, 7-inch 1024x600 touchscreen.

## Optimization-Relevant Details

- **ISA/profile:** RV64GCV (RISC-V 64-bit with general, compression, atomic, double-precision floating-point, and vector extensions).
- **Vector/matrix/accelerator support:** RVV vector extensions, Vivante GC8000UL GPU, DPU (NPU) for neural processing.
- **Memory/cache/TLB/DMA:** 64KB L1 I/D cache per core, up to 8MB L2 cache, 4GB LPDDR4, 16GB eMMC, microSD, AXI4 bus.
- **Compiler/toolchain support:** Linux (Debian 11), Android 10; no specific toolchain version detailed in the source.

## Relationships

- [[Chiplet_RISC_V_AI_SoC_Benchmark_Results]] – Benchmark results for another RISC-V AI accelerator on a chiplet architecture.
- [[Parallel_GEMM_Convolution_on_GAP8]] – Optimization recipe targeting a different RISC-V platform (GAP8) for convolution workloads.
- *Insufficient context for additional cross-links to entity pages; only these related pages are available in the wiki context.*

## Sources

- [Dev kit debuts RISC-V XuanTie C910 SoC with a 3D GPU and Android and Linux support – LinuxGizmos](https://linuxgizmos.com/dev-kit-debuts-risc-v-xuantie-c910-soc-with-a-3d-gpu-and-android-and-linux-support/)
