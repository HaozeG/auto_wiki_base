---
canonical_name: PULP-NN
aliases:
- PULP-NN library
- PULP Neural Network library
- PULP_NN
- pulp-nn
subtype: null
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.85
  self_containedness: 0.9
  bridge_score: 0.5
  hub_potential: 0.5
sources:
- raw/cache/4b0071cc05f9850c.md
- https://arxiv.org/abs/1908.11263
- raw/cache/b23970a7f296e294.md
- https://github.com/pulp-platform/pulp-nn
source_url: https://arxiv.org/abs/1908.11263
fetched_at: '2026-07-02T04:53:43.278716+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: false
inbound_links: 2
needs_summary_revision: false
---

# PULP-NN

PULP-NN is an optimized computing library for quantized neural network inference on parallel ultra-low-power tightly coupled clusters of RISC-V processors. It provides kernels for byte and sub-byte data types down to INT-1, exploiting the digital signal processing (DSP) extensions available in PULP RISC-V processors and cluster parallelism. On an octa-core cluster running a CIFAR-10 network, PULP-NN achieves 30x and 19.6x fewer clock cycles than the ARM CMSIS-NN library on STM32L4 and STM32H7 respectively. On the GAP-8 processor, PULP-NN outperforms STM32L4 by 36.8x and STM32H7 by 7.45x at maximum frequency, with energy efficiency 14.1x higher than STM32L4 and 39.5x higher than STM32H7 at the maximum efficiency operating point. The library can achieve up to 15.5 MACs/cycle on INT-8 and improves performance by up to 63x relative to a sequential single-core RISC-V baseline implementing the RV32IMC ISA.

## Key Claims

- Provides optimized kernels for quantized neural network inference on PULP RISC-V clusters.
- Supports data types from INT-8 down to INT-1.
- Achieves up to 15.5 MACs/cycle on INT-8.
- Performance improvement up to 63x over a sequential single-core RV32IMC baseline.
- On CIFAR-10, an octa-core cluster runs in 30x fewer clock cycles than CMSIS-NN on STM32L4, and 19.6x fewer than on STM32H7.
- On GAP-8, outperforms STM32L4 by 36.8x and STM32H7 by 7.45x at maximum frequency.
- Energy efficiency on GAP-8 is 14.1x higher than STM32L4 and 39.5x higher than STM32H7 at the maximum efficiency point.

## Relationships

- [[k230]]: Another RISC-V SoC with AI acceleration, representing a different approach to quantized neural network deployment.
- [[xuantie_c908]]: A RISC-V processor core with vector extensions and instruction fusion, used for similar AI inference workloads.
- [[mlir_xdsl_rvv_gemm_codegen_recipe]]: A compiler-based optimization recipe for RISC-V GEMM kernels, complementary to PULP-NN's hand-tuned library approach.
- [[pulp_nn_gap8_cifar10_benchmark]]: the detailed GAP-8/STM32 speedup and energy-efficiency measurements referenced above.
- [[pulp_platform]]: the parent open-source PULP hardware ecosystem that PULP-NN's target clusters are built on.

## Sources

- https://arxiv.org/abs/1908.11263
