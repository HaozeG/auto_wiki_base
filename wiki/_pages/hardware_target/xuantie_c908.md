---
canonical_name: XuanTie C908
aliases:
- C908
- T-Head XuanTie C908
- XuanTie C908 processor
hardware_targets:
- XuanTie C908
toolchains:
- SHL
- HHB
constraints:
- VLEN 128 or 256 configurable
- RISC-V Vector Extension 1.0
scorecard:
  novelty_delta: 0.9
  claim_density: 0.85
  self_containedness: 0.9
  bridge_score: 0.3
  hub_potential: 0.8
sources:
- raw/cache/73bedd2221cd9a03.md
- https://riscv.org/blog/xuantie-c908-accelerates-ai-with-software-and-hardware-fusion/
source_url: https://riscv.org/blog/xuantie-c908-accelerates-ai-with-software-and-hardware-fusion/
fetched_at: '2026-07-01T02:54:06.948603+00:00'
type: hardware_target
created: '2026-07-01'
updated: '2026-07-01'
cold_start: true
inbound_links: 7
needs_summary_revision: false
---

# XuanTie C908

The XuanTie C908 is a RISC-V processor core developed by T-Head Semiconductor, targeting AIoT applications such as visual AI and intelligent interaction. It is based on the RV32GCB[V] or RV64GCB[V] architecture with support for the RISC-V Vector Extension 1.0, configurable vector register width (VLEN) of 128 or 256 bits, and instruction fusion technology. The core can operate at up to 2 GHz and provides hardware support for FP16, BFP16, FP32 floating-point operations, as well as INT8, INT32, INT64 integer operations, including INT8 and INT4 vector dot product instructions. The processor is designed for energy-efficient AI inference, with a focus on software-hardware co-optimization through libraries like the Heterogeneous Library (SHL) and the Heterogenous Honey Badger (HHB) deployment tool. Detailed memory hierarchy and cache configuration are not publicly disclosed, but the platform integrates high-speed cache technology to accelerate neural network operators.

## Key Claims

- Implements RISC-V Vector Extension 1.0 with VLEN 128/256 configurable.
- Supports FP16/BFP16/FP32 and INT8/INT32/INT64 operations, plus INT8/INT4 dot product.
- Instruction fusion technology optimizes pipeline.
- Achieves up to 2 GHz clock frequency.
- Demonstrates 3.75–4.57× AI inference speedup over previous-generation XuanTie C906 when combined with SHL library and HHB quantization.
- Deployed for convolution-heavy CNN models with optimized GEMM outer product kernels.

## Optimization-Relevant Details

- ISA/profile: RISC-V RV32GCB[V]/RV64GCB[V] with Vector Extension 1.0.
- Vector/matrix/accelerator support: 128/256-bit vector, FP16 and INT8 dot product, instruction fusion.
- Memory/cache/TLB/DMA: (not specified)
- Compiler/toolchain support: SHL neural network library, HHB model deployment toolchain.

## Relationships

- Optimized convolution recipe: [[xuantie_c908_shl_convolution_acceleration]]
- GEMM kernel: [[xuantie_c908_fp16_gemm_kernel]]
- Benchmark results: [[xuantie_c908_ai_inference_performance]]
- Related DNN accelerator generator: [[gemmini]]

## Sources

- https://riscv.org/blog/xuantie-c908-accelerates-ai-with-software-and-hardware-fusion/
