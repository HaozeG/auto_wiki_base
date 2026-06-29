---
cold_start: false
constraints:
- 12-stage pipeline
- out-of-order
- superscalar 3-to-8 decoder
- multi-channel data prefetch
- RVV vector extension
created: '2026-07-12'
hardware_targets:
- T-HEAD Xuantie C910
inbound_links: 0
scorecard:
  bridge_score: 0.5
  claim_density: 0.6
  hub_potential: 0.4
  novelty_delta: 0.7
  self_containedness: 0.9
sources:
- https://chipsandcheese.com/p/alibabat-heads-xuantie-c910
tags:
- RISC-V
- T-HEAD
- Xuantie
- C910
- out-of-order
- vector extension
toolchains: []
type: hardware_target
updated: '2026-06-29'
---

# T-HEAD Xuantie C910

The Xuantie C910 is a 64-bit high-performance out-of-order RISC-V processor core developed by Alibaba's T-HEAD division, designed to fill the high-performance category within the Xuantie processor lineup. It features a 12-stage pipeline, a superscalar architecture with a 3-to-8 line decoder capable of decoding up to eight instructions per cycle, and multi-channel data prefetch for improved memory access efficiency. The C910 is an early adopter of the RISC-V Vector Extension (RVV), joining a small number of out-of-order RISC-V cores that have been implemented in hardware. It is fully based on the RV64GCV instruction set and includes custom extensions for arithmetic operations, bit manipulation, load/store, TLB, and cache operations. The design has been open-sourced as OpenC910, with its RTL and user manual available on GitHub, enabling community evaluation and customization.

## Key Claims

- 64-bit out-of-order RISC-V core with 12-stage pipeline.
- Superscalar microarchitecture with a 3-to-8 line decoder (decode up to eight instructions per cycle).
- Multi-channel data prefetch mechanism.
- Early support for the RISC-V Vector Extension (RVV).
- Based on the RV64GCV instruction set with custom extensions (bit manipulation, atomic, load/store, TLB, cache).
- Open-sourced as OpenC910 (RTL available on GitHub under XUANTIE-RV/openc910).
- Designed for high-performance embedded and computing applications.

## Optimization-Relevant Details

- ISA/profile: RV64GCV (base plus vector extensions plus custom T-HEAD extensions).
- Vector/matrix/accelerator support: RISC-V Vector Extension (version not specified in available resource).
- Memory/cache/TLB/DMA: Multi-channel data prefetch; TLB and cache operation custom instructions.
- Compiler/toolchain support: Vendor-provided toolchains (e.g., Xuantie-900-gcc) are known from the ecosystem; specific support for the C910 is documented on the OpenC910 repository.

## Relationships

- [[Sipeed_MAIX_series]] – Both are RISC-V based platforms, though the MAIX series uses the Kendryte K210 core rather than the C910.
- Insufficient context for additional cross-links to entity pages; the current wiki context includes only one entity page (Sipeed MAIX series) that can be directly related.

## Sources

- [Chips and Cheese: Alibaba/T-HEAD's Xuantie C910](https://chipsandcheese.com/p/alibabat-heads-xuantie-c910)
- [GitHub: XUANTIE-RV/openc910](https://github.com/XUANTIE-RV/openc910)
- [XuanTie-Openc910-UserManual](https://occ-intl-prod.oss-ap-southeast-1.aliyuncs.com/XuanTie-Openc910-UserManual.pdf)
- [Paper: Xuantie-910: A Commercial Multi-Core 12-Stage Pipeline Out-of-Order RISC-V Processor](https://ieeexplore.ieee.org/document/xxx) (source inferred from search snippets)
