---
cold_start: true
constraints:
- zero intermediate buffer
- pixel-wise streaming
- implemented on Xilinx Artix-7 FPGA
created: '2025-03-04'
datatypes: []
evidence_strength: measured (FPGA), reported
hardware_targets:
- RISC-V processor with Custom Function Unit (CFU)
inbound_links: 4
metrics:
- data movement reduction
- speedup
scorecard:
  bridge_score: 0.6
  claim_density: 0.9
  hub_potential: 0.7
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://arxiv.org/abs/2511.21232
tags:
- TinyML
- DSC
- fused dataflow
- zero-buffer
- RISC-V
- CFU
toolchains:
- CFU-Playground
type: optimization_recipe
updated: '2026-06-28'
workloads:
- Depthwise Separable Convolution (DSC)
---

# Fused Pixel-wise Dataflow for TinyML Depthwise Separable Convolutions (DSC)

This optimization recipe describes the fused pixel-wise dataflow technique introduced in "RISC-V Based TinyML Accelerator for Depthwise Separable Convolutions in Edge AI" (arXiv:2511.21232). The transformation reorganizes the computation of a Depthwise Separable Convolution (DSC) block from a conventional layer-by-layer model to a pixel-by-pixel streaming model. By implementing the accelerator as a Custom Function Unit (CFU) on a RISC-V processor, the technique eliminates the need for intermediate buffers entirely, reducing data movement by up to 87% and achieving a 59.3x speedup on a Xilinx Artix-7 FPGA. The recipe is suitable for TinyML systems where memory bandwidth is the primary bottleneck.

## Key Claims

- Fused pixel-wise dataflow computes a single output pixel across all DSC stages without writing to memory.
- Eliminates intermediate buffer storage, reducing data movement up to 87%.
- Implemented as a CFU for RISC-V, enabling tight pipeline integration.
- Achieves 59.3x speedup over software baseline on Artix-7 FPGA.
- ASIC synthesis projects compact area and low power (0.284 mm²/910 mW at 2 GHz in 28nm; 1.20 mm²/233 mW at 300 MHz in 40nm).

## Transformation

- Prerequisites: RISC-V processor with CFU support; CFU-Playground toolchain; FPGA for hardware implementation.
- Steps:
  1. Stream input pixels one at a time through the pipeline.
  2. Perform expansion convolution (1x1) on the pixel.
  3. Apply depthwise convolution on the expanded features.
  4. Apply projection convolution (1x1) to produce a single output pixel.
  5. Pipeline stages are tightly coupled; no intermediate memory writes.
- Expected effect: Up to 87% reduction in memory traffic; up to 59.3x speedup over software.
- Failure modes: Not specified; likely limited to networks with DSC structure.
- Measurements: FPGA speedup 59.3x, data reduction 87% measured on Artix-7; ASIC numbers from synthesis.

## Relationships

- [[DSC_Fused_Dataflow_Benchmark_Results]] – The benchmark results page with detailed measurements.
- [[XuanTie_C908_SHL_GEMM_Optimization]] – Another RISC-V optimization recipe for GEMM/convolution, providing contrast with a vectorized approach.
- [[SiFive_P550_and_T-HEAD_C910_Benchmark_Comparison]] – Benchmark page for RISC-V cores, offering context on execution efficiency.
- Note: insufficient context for additional cross-links to entity pages.

## Sources

- [arXiv:2511.21232](https://arxiv.org/abs/2511.21232)

