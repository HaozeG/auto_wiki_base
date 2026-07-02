---
canonical_name: RV-WINO
aliases:
- RV-WINO processor
- RISC-V Winograd accelerator
subtype: null
tags: []
hardware_targets:
- RV-WINO
toolchains: []
constraints:
- 55-nm CMOS process
scorecard:
  novelty_delta: 0.9
  claim_density: 0.6
  self_containedness: 0.8
  bridge_score: 0.5
  hub_potential: 0.3
sources:
- raw/cache/219979666a24476a.md
- https://www.researchgate.net/scientific-contributions/Xingbo-Wang-2197937289
source_url: https://www.researchgate.net/scientific-contributions/Xingbo-Wang-2197937289
fetched_at: '2026-07-02T12:09:04.006653+00:00'
type: hardware_target
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# RV-WINO

RV-WINO is a RISC-V neural network inference accelerator chip fabricated in a 55-nm CMOS process that implements the Winograd algorithm for convolution and general matrix multiplication (GEMM) acceleration. It is the first silicon implementation of a RISC-V processor leveraging Winograd-based convolution to reduce multiplication operations and energy consumption. The processor incorporates a dedicated Winograd module and a matrix multiplication module that reuses multipliers from the Winograd module, enabling efficient fully connected and dot product operations. RV-WINO achieves peak computational performance of 0.95 GOPS in INT32 mode and 2.39 GOPS in INT8 mode, with peak energy efficiencies of 112 GOPS/W and 237 GOPS/W respectively. Compared to a baseline RISC-V processor, RV-WINO reduces CNN inference execution time by over 80%.

## Key Claims

- First silicon implementation of a RISC-V processor based on the Winograd algorithm for convolution and GEMM acceleration.
- Peak performance: 0.95 GOPS (INT32), 2.39 GOPS (INT8).
- Peak energy efficiency: 112 GOPS/W (INT32), 237 GOPS/W (INT8).
- CNN inference execution time reduced by over 80% compared to a baseline RISC-V processor.
- Fabricated in a 55-nm CMOS process.

## Optimization-Relevant Details

- ISA/profile: RISC-V (specific profile not disclosed in source).
- Vector/matrix/accelerator support: Dedicated Winograd module for convolution; matrix multiplication module for GEMM that reuses Winograd multipliers.
- Memory/cache/TLB/DMA: Not specified in source.
- Compiler/toolchain support: Not specified in source.

## Relationships

- [[earth-shifting-based-vector-memory-access]]: As a RISC-V accelerator, RV-WINO could benefit from optimized vector memory access techniques such as EARTH’s LSDO and RCVRF for improved data movement.
- [[llvm-riscv-fptrunc-narrowing-optimization]]: Compiler optimizations for RISC-V, such as FPTrunc narrowing, may improve code generation for workloads running on RV-WINO. Insufficient context for additional cross-links; no other existing entity or hardware target pages are directly related in the current wiki.

## Sources

- [Xingbo Wang's research works on ResearchGate](https://www.researchgate.net/scientific-contributions/Xingbo-Wang-2197937289)
