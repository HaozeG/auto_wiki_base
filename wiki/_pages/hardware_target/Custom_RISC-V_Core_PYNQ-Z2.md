---
cold_start: true
constraints:
- 50 MHz clock
- 5-stage in-order pipeline
- 4KB I-cache
- 4KB D-cache
- Zynq-7020 resource limits (53,200 LUTs, 220 DSPs)
- AXI4-Lite control bus (1 MB/s)
- AXI4 data bus (850 MB/s)
- 64 KB BRAM memory interface
created: '2025-03-26'
hardware_targets:
- PYNQ-Z2 (Xilinx Zynq-7020)
- Custom RISC-V core (RV32IM + custom-0 space)
inbound_links: 2
scorecard:
  bridge_score: 0.8
  claim_density: 0.9
  hub_potential: 0.8
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://arxiv.org/html/2511.06955v1
tags:
- RISC-V
- FPGA
- PYNQ-Z2
- custom ISA
- edge AI
toolchains:
- GCC inline assembly
type: hardware_target
updated: '2026-06-28'
---

# Custom RISC-V Core PYNQ-Z2

This hardware target is a custom RISC-V core implementing the RV32IM base ISA (with multiplication extension) and four novel custom-0 space ISA extensions (FPGA.VCONV, FPGA.GEMM, FPGA.RELU, FPGA.CUSTOM) designed for FPGA-accelerated neural network inference on edge devices. The core features a 5-stage in-order pipeline with separate 4 KB direct-mapped instruction and data caches, a custom instruction decoder, and an accelerator interface memory-mapped at base address 0xA0000000 with a 64 KB address space. It is implemented and verified on the Xilinx PYNQ-Z2 platform (Zynq-7020 SoC) at a 50 MHz clock frequency, achieving +12.793 ns worst negative slack. The base core uses 0.43% LUTs and 11.4% BRAM of the Zynq-7020 resources, with an additional 38.8% DSPs when accelerators are active. Communication between the core and FPGA accelerators uses AXI4-Lite (32-bit, 1 MB/s) for control and AXI4 (32-bit, 850 MB/s measured) for data transfers, with a verified 64 KB BRAM memory interface.

## Key Claims

- RV32IM base ISA with custom-0 opcode space (0x0B) for accelerator instructions.
- 5-stage in-order pipeline with 4 KB I-cache and D-cache.
- Resource usage: 229 LUTs (0.43%), 253 FFs (0.24%), 0 DSPs for base core; 38.8% DSPs when accelerators active.
- Timing closure at 50 MHz with +12.793 ns slack.
- Peak memory bandwidth: 850 MB/s (AXI4 data bus).
- Custom instruction decoder recognizes FPGA.* opcodes.
- Accelerator interface with 64 KB address space at 0xA0000000.

## Optimization-Relevant Details

- ISA/profile: RV32IM + custom-0 space (4 custom instructions).
- Vector/matrix/accelerator support: FPGA.VCONV (systolic array), FPGA.GEMM (systolic array), FPGA.RELU (16 parallel units), FPGA.CUSTOM (extensible, up to 128 accelerators).
- Memory/cache/TLB/DMA: 4 KB I-cache, 4 KB D-cache, AXI4 data bus with DMA support (triple-buffering for convolution).
- Compiler/toolchain support: GCC inline assembly via `.insn r` directives.

## Relationships

- [[Parallel_GEMM_Convolution_on_GAP8]] – Alternative GEMM-based approach on a different RISC-V platform.
- [[GEMM_with_RISC-V_Vector_Extension]] – Contrasts vector-based GEMM with custom-0 space accelerated GEMM.

## Sources

- [FPGA-Accelerated RISC-V ISA Extensions for Efficient Neural Network Inference on Edge Devices – arXiv](https://arxiv.org/html/2511.06955v1)
