---
cold_start: true
constraints:
- 5-stage in-order pipeline
- 4KB I-cache and D-cache
- AXI4-Lite/ AXI4 buses
- 50 MHz clock
- Zynq-7020 resource limits (53,200 LUTs, 220 DSPs)
created: '2025-03-04'
datatypes:
- int16
- int8
evidence_strength: measured
hardware_targets:
- PYNQ-Z2 (Xilinx Zynq-7020)
- Custom RISC-V core (RV32IM + custom-0 space)
inbound_links: 1
metrics:
- latency speedup
- energy reduction
- resource utilization
- timing slack
scorecard:
  bridge_score: 0.8
  claim_density: 0.9
  hub_potential: 0.7
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://arxiv.org/abs/2511.06955
tags:
- RISC-V
- FPGA
- PYNQ-Z2
- CNN
- ISA extension
- neural network
- edge AI
- custom instruction
toolchains:
- GCC inline assembly
type: optimization_recipe
updated: '2026-06-28'
workloads:
- MobileNet V2
- ResNet-18
- EfficientNet Lite
- YOLO Tiny
- Convolution
- GEMM
- Activation functions
---

# FPGA-Accelerated RISC-V ISA Extensions for CNN Inference

This optimization recipe describes the design and implementation of four custom instruction set architecture (ISA) extensions (FPGA.VCONV, FPGA.GEMM, FPGA.RELU, FPGA.CUSTOM) for a RISC-V core to accelerate convolutional neural network inference on resource-constrained FPGAs. The transformation involves profiling CNN workloads to identify compute-intensive kernels (convolution 60-85%, matrix multiplication 10-25%, activation functions 5-10%), then designing custom instructions that trigger FPGA-based systolic array and vector accelerators. Prerequisites include a RISC-V core with support for the custom-0 opcode space, a Xilinx PYNQ-Z2 board, and GCC toolchain for inline assembly. Expected effect is 2.14x average latency speedup and 49.1% energy reduction across four benchmark models (MobileNet V2, ResNet-18, EfficientNet Lite, YOLO Tiny). Failure modes are not detailed but likely involve memory bandwidth bottlenecks (e.g., DMA overhead). Measurements are from physical hardware deployment on the PYNQ-Z2 platform at 50 MHz.

## Key Claims

- Four custom ISA extensions are defined in the RISC-V custom-0 space (opcode 0001011): FPGA.VCONV (vectorized convolution), FPGA.GEMM (matrix multiplication), FPGA.RELU (vectorized activation), and FPGA.CUSTOM (extensible escape for batch norm, depthwise separable conv, NMS).
- The extensions are implemented as FPGA accelerators: 4x4 systolic array for convolution (16 DSP48E1 slices, 0.8 GMAC/s peak), 8x8 systolic array for GEMM (64 MACs/cycle, weight-stationary), and 16-lane activation unit (LUT-based with 256-entry tables).
- The convolution accelerator delivers 7.20x speedup over ARM NEON-optimized 3x3 convolution, utilizing 35% of 220 DSP slices.
- The GEMM accelerator achieves 4.20x speedup, 6.4 GOPS (INT16), utilizing 50% of DSP slices when active.
- The activation accelerator achieves 3.00x speedup and 85% instruction reduction for 1024-element vectors.
- The FPGA.CUSTOM extension provides a 7-bit function code space for up to 128 custom accelerators, with intrinsics via GCC inline assembly.
- Triple-buffering overlays computation with DMA transfers, attaining 87% hardware utilization for convolution.
- The design is fully implemented and timing-closed on PYNQ-Z2 with +12.793 ns slack at 50 MHz.

## Transformation

- **Prerequisites:** RISC-V core with custom-0 decoder; Xilinx PYNQ-Z2 board; Vivado for synthesis; GCC with inline assembly support; profiled CNN workload to identify hot spots.
- **Steps:**
  1. Profile baseline CNN inference on ARM Cortex-A9 to identify convolution (60-85%), GEMM (10-25%), and activation (5-10%) as hotspots.
  2. Design custom instructions for each hotspot: FPGA.VCONV, FPGA.GEMM, FPGA.RELU, and FPGA.CUSTOM for remaining operations.
  3. Implement FPGA accelerators: systolic arrays for convolution and GEMM, LUT-based activation units.
  4. Integrate accelerators with the RISC-V core via AXI4-Lite control bus and AXI4 data bus.
  5. Develop software intrinsics using GCC inline assembly (`.insn r 0x0B, 0, 0, %0, %1, %2, %3`).
  6. Build complete embedded system on PYNQ-Z2, synthesize, implement, and deploy.
  7. Measure inference latency, energy, and resource usage against ARM baseline.
- **Expected effect:** Average 2.14x latency speedup and 49.1% energy reduction over optimized ARM software baseline for CNN inference. Individual kernel speedups: 7.20x (3x3 conv), 4.20x (GEMM), 3.00x (activation).
- **Failure modes:** Not specified. Potential bottlenecks include DMA transfer overhead, limited FPGA resource, and memory bandwidth contention. The paper notes that memory bandwidth and DMA overhead limit attainable speedup.
- **Measurements:** All metrics obtained from physical hardware on PYNQ-Z2 at 50 MHz. Resource usage: 0.43% LUTs, 11.4% BRAM for base core; 38.8% DSPs when accelerators active. Timing closed with +12.793 ns slack.

## Relationships

- [[PYNQ-Z2_RISC-V_CNN_ISA_Extensions_Benchmark]] – The benchmark result page for the same design, providing detailed measurement context.
- [[DSC_Fused_Dataflow_Optimization_Recipe]] – Another RISC-V-based CNN acceleration recipe using CFU, contrasting custom ISA vs. custom function unit approach.
- [[GEMM_with_RISC-V_Vector_Extension]] – A general-purpose RISC-V vector GEMM kernel; this recipe uses custom instructions instead of standard vector extension.

## Sources

- [arXiv:2511.06955](https://arxiv.org/abs/2511.06955)

