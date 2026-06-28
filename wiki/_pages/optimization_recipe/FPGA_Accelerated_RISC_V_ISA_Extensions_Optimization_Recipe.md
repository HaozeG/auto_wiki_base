---
cold_start: true
constraints:
- 50 MHz clock
- 64 KB BRAM memory interface
- AXI interconnect functionality
- Zynq-7020 resource limits (53,200 LUTs, 220 DSPs)
created: '2025-11-11'
datatypes: []
evidence_strength: measured
hardware_targets:
- PYNQ-Z2 (Xilinx Zynq-7020)
inbound_links: 0
metrics:
- latency speedup
- energy reduction
- resource utilization
- timing slack
scorecard:
  bridge_score: 0.9
  claim_density: 0.9
  hub_potential: 0.6
  novelty_delta: 0.9
  self_containedness: 0.8
sources:
- https://arxiv.org/abs/2511.06955
tags:
- RISC-V
- FPGA
- ISA extensions
- edge AI
toolchains: []
type: optimization_recipe
updated: '2026-06-28'
workloads:
- MobileNet V2
- ResNet-18
- EfficientNet Lite
- YOLO Tiny
---

# FPGA-Accelerated RISC-V ISA Extensions Optimization Recipe

This optimization recipe describes the design and implementation of four custom RISC-V ISA extensions (FPGA.VCONV, FPGA.GEMM, FPGA.RELU, FPGA.CUSTOM) that offload neural network compute kernels to FPGA-implemented datapaths on a Xilinx PYNQ-Z2 platform. The prerequisites include a Zynq-7020 SoC, a custom RISC-V core (RV32IM with custom-0 opcode space), and an AXI memory interface for data movement. The expected effect is a 2.14x average latency speedup and 49.1% energy reduction compared to an ARM Cortex-A9 software baseline across MobileNet V2, ResNet-18, EfficientNet Lite, and YOLO Tiny models. Failure modes may include memory bandwidth limitations; the paper notes that memory bottlenecks limit the attainable speedup. Measurements were obtained from physical hardware deployment with verified timing closure at 50 MHz.

## Key Claims

- Four custom ISA extensions (FPGA.VCONV, FPGA.GEMM, FPGA.RELU, FPGA.CUSTOM) are implemented in a custom RISC-V core.
- 2.14x average latency speedup and 49.1% energy reduction versus an ARM Cortex-A9 software baseline.
- Timing closure achieved with +12.793 ns worst negative slack at 50 MHz.
- Resource usage: 0.43% LUTs and 11.4% BRAM for the base core; 38.8% DSPs when accelerators are active.
- Performance metrics are obtained from physical hardware measurements on the Xilinx PYNQ-Z2 platform.

## Transformation

- Prerequisites:
  - Xilinx PYNQ-Z2 (Zynq-7020) platform with available FPGA resources.
  - Custom RISC-V core supporting custom instruction encoding in custom-0 opcode space.
  - FPGA development tools for synthesis, implementation, and timing closure.
  - Neural network inference software framework capable of utilizing custom instructions.
- Steps:
  1. Design FPGA-accelerated datapaths for convolution (FPGA.VCONV), matrix multiplication (FPGA.GEMM), activation (FPGA.RELU), and custom operations (FPGA.CUSTOM).
  2. Integrate these datapaths with a RISC-V CPU core via custom instructions that trigger the accelerators.
  3. Implement an AXI-attached memory interface with 64 KB BRAM to buffer data between CPU and accelerators.
  4. Synthesize and implement the system on PYNQ-Z2, ensuring timing closure at 50 MHz.
  5. Deploy four neural network benchmarks (MobileNet V2, ResNet-18, EfficientNet Lite, YOLO Tiny) using the custom instructions.
  6. Measure latency and power consumption against an ARM Cortex-A9 software baseline under the same power envelope.
- Expected effect: 2.14x average latency speedup and 49.1% energy reduction across all four models.
- Failure modes:
  - Memory bandwidth and DMA overhead are identified as primary bottlenecks that limit the maximum attainable speedup.
  - The use of INT8 quantization, if applied, may introduce accuracy degradation (accuracy impact not measured in the available resource).
- Measurements:
  - Physical hardware measurements on the PYNQ-Z2 FPGA at 50 MHz.
  - Resource utilization percentages reported.
  - Timing slack +12.793 ns confirms timing closure.

## Relationships

- [[DSC_Fused_Dataflow_Benchmark_Results]] – An alternative FPGA-based RISC-V accelerator for depthwise separable convolutions, providing a different approach via a custom function unit.
- [[TVM_and_Gemmini_Accelerator_Benchmark_Results]] – A benchmark of a systolic array GEMM accelerator integrated with TVM, demonstrating another FPGA-based RISC-V acceleration method.

## Sources

- [arXiv:2511.06955](https://arxiv.org/abs/2511.06955)
