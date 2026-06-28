---
cold_start: false
created: '2025-11-01'
inbound_links: 0
needs_summary_revision: false
scorecard:
  bridge_score: 0.7
  claim_density: 0.9
  hub_potential: 0.6
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://arxiv.org/html/2511.21232
tags:
- risc-v
- accelerator
- tinyML
- deep-learning
- FPGA
- ASIC
- custom-function-unit
type: entity
updated: '2026-06-27'
---

# RISC-V Based TinyML Accelerator for Depthwise Separable Convolutions

The RISC-V based TinyML Accelerator for Depthwise Separable Convolutions is a custom hardware design that implements a fused pixel-wise dataflow to eliminate intermediate feature map buffering in depthwise separable convolution (DSC) blocks. It is realized as a Custom Function Unit (CFU) attached to a RISC-V processor core, enabling tightly-coupled acceleration without modifying the CPU pipeline. The architecture computes one output pixel completely across all DSC stages—expansion, depthwise convolution, and projection—by streaming data through a dedicated three-stage pipeline, thereby avoiding writing intermediate results to on-chip SRAM or DRAM. Evaluated on a Xilinx Artix-7 FPGA, it achieves a 59.3× speedup over baseline RISC-V software execution, and ASIC synthesis projects a compact 0.284 mm² footprint at 2 GHz in 28 nm technology. This design specifically targets TinyML and edge AI scenarios where memory bandwidth and power consumption are critical constraints.

## Key Claims

- The fused pixel-wise dataflow reduces data movement by up to 87% compared to conventional layer-by-layer DSC execution.
- FPGA prototyping on Xilinx Artix-7 achieves a 59.3× speedup over a baseline RISC-V software implementation.
- ASIC synthesis in 28 nm technology shows a footprint of 0.284 mm² and power consumption of 910 mW at 2 GHz.
- ASIC synthesis in 40 nm technology shows a footprint of 1.20 mm² and power consumption of 233 mW at 300 MHz.
- The accelerator implements a three-stage pipeline covering expansion convolution, depthwise convolution, and projection convolution in a single pass.
- An on-the-fly padding logic handles input boundary conditions without pre-padded buffers.
- A heterogeneous on-chip memory architecture supplies operands to the pipeline with minimal local storage, eliminating large intermediate feature map buffers.
- The design is implemented as a Custom Function Unit (CFU) using the CFU-Playground framework, enabling integration with open-source RISC-V cores.

## Relationships

- [[gemmini]] — Both are RISC-V accelerator designs for deep learning; Gemmini uses systolic arrays for general DNN acceleration, while this accelerator optimizes specifically for depthwise separable convolutions with a zero-buffer dataflow.
- [[risc_v_vector_extension]] — RVV provides a general vector SIMD approach to data-parallel computation, whereas this CFU-based accelerator offers a fixed-function alternative specialized for DSC blocks, aiming for higher efficiency under TinyML constraints.
- [[tvm_riscv_backend]] — TVM's compiler infrastructure could target this accelerator via CFU-specific intrinsics, enabling automated deployment of TinyML models onto the hardware.

## Sources

- [arXiv paper](https://arxiv.org/html/2511.21232)
