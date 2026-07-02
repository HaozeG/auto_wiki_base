---
canonical_name: SpacemiT X60
aliases:
- Spacemit X60
- X60
- SpacemiT X60 RISC-V Processor
subtype: null
tags: []
hardware_targets:
- SpacemiT X60
toolchains:
- GCC
- Phoronix Test Suite
constraints:
- RISC-V 64GCVB architecture
- RVA22 profile
- 1.6 GHz clock speed
- PCIe 2.0 x2 connectivity
- Three M.2 slots for expansion
- 32KB L1 cache per core
- 512KB L2 cache per core
- 512KB tightly coupled memory (TCM) per core
scorecard:
  novelty_delta: 0.8
  claim_density: 0.6
  self_containedness: 0.6
  bridge_score: 0.5
  hub_potential: 0.4
sources:
- raw/cache/e421ad7acd23c02a.md
- https://www.diyelectronics.us/2025/02/spacemit-x60-risc-v-processor-powers-ai.html
source_url: https://www.diyelectronics.us/2025/02/spacemit-x60-risc-v-processor-powers-ai.html
fetched_at: '2026-07-02T10:30:20.605904+00:00'
type: hardware_target
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# SpacemiT X60

The SpacemiT X60 is a RISC-V processor designed for AI acceleration and high-speed storage applications, featuring a dual-cluster octa-core architecture. Cluster 0 contains four cores with dedicated AI acceleration, each equipped with a 32KB L1 cache, a 512KB L2 cache, and 512KB of tightly coupled memory (TCM), while the overall chip adheres to the RISC-V 64GCVB architecture and the RVA22 profile. The processor operates at a clock speed of 1.6 GHz and includes support for local interrupt controller CLINT and platform interrupt controller PLIC. For high-speed peripherals and storage, it provides PCIe 2.0 x2 connectivity and three M.2 slots. The X60 powers the SpacemiT K1 SoC, which is used in platforms such as the Bit-Brick K1 and Banana Pi BPI-F3. The processor has been benchmarked via the Phoronix Test Suite and has GCC tuning available for optimized code generation.

## Key Claims

- Dual-cluster octa-core design with dedicated AI acceleration in Cluster 0.
- Each core in Cluster 0 has 32KB L1, 512KB L2, and 512KB TCM.
- Supports RISC-V 64GCVB and RVA22 profile, including CLINT and PLIC interrupt controllers.
- Operates at 1.6 GHz with 8 threads.
- Provides PCIe 2.0 x2 and three M.2 slots for high-speed storage and peripherals.
- Used in Bit-Brick K1 and Banana Pi BPI-F3 platforms.
- Benchmarked via OpenBenchmarking.org (Phoronix Test Suite).

## Optimization-Relevant Details

- **ISA/profile**: RISC-V 64GCVB, RVA22.
- **Vector/matrix/accelerator support**: Dedicated AI acceleration in Cluster 0 (specific accelerator architecture not detailed in available sources).
- **Memory/cache/TLB/DMA**: Per-core L1 32KB, L2 512KB, TCM 512KB; memory hierarchy details beyond cache not specified.
- **Compiler/toolchain support**: GCC tuning exists for the X60 core; Phoronix Test Suite used for benchmarking.

## Relationships

- [[cpa-factored-gemmini-systolic-array]]: As a RISC-V AI accelerator, Gemmini may be compared or integrated with the SpacemiT X60 for machine learning workloads.
- [[llvm-risc-v-fptrunc-narrowing-optimization]]: The SpacemiT X60, as a RISC-V target, could benefit from LLVM compiler optimizations including floating-point narrowing passes.

## Sources

- [SpacemiT X60 RISC-V Processor Powers AI and High-Speed Storage...](https://www.diyelectronics.us/2025/02/spacemit-x60-risc-v-processor-powers-ai.html)
- [Banana Pi BPI-F3 SpacemiT K1 RISC-V chip documentation](https://docs.banana-pi.org/en/BPI-F3/BPI-F3)
