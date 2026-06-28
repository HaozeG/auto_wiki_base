---
cold_start: true
created: '2025-03-26'
datatypes:
- int16
evidence_strength: measured
hardware_targets:
- PYNQ-Z2 (Xilinx Zynq-7020)
- Custom RISC-V core (RV32IM + custom-0 space)
hardware_versions:
- PYNQ-Z2 (Xilinx Zynq-7020 at 50 MHz)
inbound_links: 1
measurement_method: Physical hardware measurements on PYNQ-Z2 board comparing custom
  RISC-V core with FPGA accelerators against optimized ARM Cortex-A9 software baseline
  (666 MHz) under same power envelope.
metrics:
- latency speedup
- energy reduction
- resource utilization
- timing slack
needs_summary_revision: true
scorecard:
  bridge_score: 0.8
  claim_density: 0.9
  hub_potential: 0.8
  novelty_delta: 0.9
  self_containedness: 0.9
software_versions: []
sources:
- https://arxiv.org/html/2511.06955v1
tags:
- RISC-V
- FPGA
- PYNQ-Z2
- neural network inference
- edge AI
toolchains:
- GCC inline assembly
type: benchmark_result
updated: '2026-06-28'
workloads:
- MobileNet V2
- ResNet-18
- EfficientNet Lite
- YOLO Tiny
---

# FPGA RISC-V ISA Extensions Benchmark Results

Benchmark results for FPGA-accelerated RISC-V ISA extensions are measured on the PYNQ-Z2 platform (Xilinx Zynq-7020) at 50 MHz using a custom RV32IM core with four novel custom-0 space instructions (FPGA.VCONV, FPGA.GEMM, FPGA.RELU, FPGA.CUSTOM). The system is evaluated on four neural network models: MobileNet V2, ResNet-18, EfficientNet Lite, and YOLO Tiny. All results are obtained from physical hardware measurements and compared against an optimised ARM Cortex-A9 software baseline running at 666 MHz on the same Zynq-7020 SoC. The custom core achieves a 2.14× average latency speedup and 49.1% energy reduction across all models. Resource usage for the base core is 0.43% LUTs and 11.4% BRAM, with 38.8% DSPs utilized when accelerators are active. Timing closure is verified with +12.793 ns worst negative slack at 50 MHz. The accelerators deliver 0.8 GMAC/s peak throughput for convolution, 6.4 GOPS for INT16 GEMM, and a 3.00× speedup for activation functions.

## Key Claims

- 2.14× average latency speedup and 49.1% energy reduction across MobileNet V2, ResNet-18, EfficientNet Lite, and YOLO Tiny vs. ARM Cortex-A9 baseline.
- FPGA.VCONV achieves 7.20× speedup over ARM NEON-optimized convolution for 3×3 kernels.
- FPGA.GEMM achieves 4.20× speedup over ARM Cortex-A9 for matrix multiplication.
- FPGA.RELU achieves 3.00× speedup with 85% instruction reduction for 1024-element vectors.
- Base core uses 229 LUTs (0.43%), 253 FFs (0.24%), 0 DSPs; accelerators use 38.8% DSPs.
- Timing slack: +12.793 ns at 50 MHz.

## Measurement Context

- Hardware version: PYNQ-Z2 (Xilinx Zynq-7020, xc7z020clg400-1) with custom RV32IM core at 50 MHz; ARM Cortex-A9 dual-core at 666 MHz for baseline.
- Software/toolchain version: GCC inline assembly for custom instructions; baseline uses ARM NEON-optimized libraries.
- Workload shape: MobileNet V2, ResNet-18, EfficientNet Lite, YOLO Tiny (full models, input sizes not specified).
- Metric: Latency speedup (2.14× average), energy reduction (49.1%), resource utilization (LUTs, FFs, DSPs, BRAM), timing slack (ns).
- Method: Direct hardware measurements on FPGA; baseline executed on ARM Cortex-A9 with optimized NEON code.
- Evidence strength: measured (physical hardware results).

## Relationships

- [[Custom_RISC-V_Core_PYNQ-Z2]] – The hardware target page for this custom core.
- [[DSC_Fused_Dataflow_Benchmark_Results]] – Another FPGA-based benchmark on a different platform (Artix-7) for depthwise separable convolution.

## Sources

- [FPGA-Accelerated RISC-V ISA Extensions for Efficient Neural Network Inference on Edge Devices – arXiv](https://arxiv.org/html/2511.06955v1)
