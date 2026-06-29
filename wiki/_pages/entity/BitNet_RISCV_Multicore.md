---
cold_start: true
created: '2025-08-11'
inbound_links: 0
scorecard:
  bridge_score: 0.8
  claim_density: 0.7
  hub_potential: 0.6
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://github.com/VedantPahariya/BitNet-RISCV-Multicore
tags:
- RISC-V
- BitNet
- 1-bit LLM
- Ara
- CVA6
- Gemmini
- multicore
- vector accelerator
type: entity
updated: '2026-06-29'
---

# BitNet-RISCV-Multicore

BitNet-RISCV-Multicore is an open-source hardware-software co-design project that implements 1-bit Large Language Model (BitNet) inference on multi-core RISC-V vector accelerators. The project enhances the PULP Ara multicore vector processor architecture and the CVA6 RISC-V CPU with custom extensions to natively execute BitNet algorithms at ultra-low precision. It integrates the Gemmini systolic array accelerator with a custom Processing Element (PE) designed for ternary weights (`{-1, 0, +1}`), replacing multiplier-based MAC paths with mux-based selection logic to reduce area and power while preserving ternary compute accuracy. The system is organized as a set of submodules for Ara, CVA6, and Gemmini modifications, along with documentation and an upstream community engagement issue on the Ara repository. The project was developed as part of a 'Hardware for AI' course and demonstrates a full-stack approach for 1-bit LLM orchestration on RISC-V, spanning from hardware architecture changes to software kernel mapping.

## Key Claims

- Custom accelerator extensions for 1-bit LLM (BitNet) orchestration on multi-core RISC-V vector cores based on the Ara architecture.
- Vectorized architecture enhancements to the CVA6 core and Ara vector processor to support rapid 1-bit MAC (Multiply-Accumulate) and bit-serial operations under RVV 1.0.
- A custom Gemmini Processing Element (PE) for ternary weights, using mux-based selection logic (`+activation`, `0`, `-activation`) instead of multiplier-heavy MAC, reducing overhead while preserving ternary compute accuracy.
- Tighter CVA6-Ara coupling for BitNet-oriented vector execution, with decode/dispatch integration and multicore CVA6-Ara pairs to mitigate the single-issue bottleneck of one scalar core.
- Scalable orchestration of workload distribution across a multi-core paradigm, leveraging Gemmini for dense matrix operations complementing vector-level optimizations.
- Upstream community engagement via a structured guidance issue in the Ara repository documenting integration gaps and reproducibility paths.

## Relationships

- [[Gemmini_systolic_array_GEMM_accelerator]] – The Gemmini accelerator is used in this project with a custom ternary PE modification for 1-bit LLM inference.
- [[Chiplet_RISC_V_AI_SoC_Benchmark_Results]] – Both projects target RISC-V-based AI acceleration; this project focuses on 1-bit LLM inference on multicore vector systems.

## Sources

- [GitHub: VedantPahariya/BitNet-RISCV-Multicore](https://github.com/VedantPahariya/BitNet-RISCV-Multicore)
- [Ara upstream issue #430](https://github.com/pulp-platform/ara/issues/430)

