---
cold_start: true
created: '2025-03-04'
datatypes:
- int16
- int8
evidence_strength: measured
hardware_targets:
- PYNQ-Z2 (Xilinx Zynq-7020)
- ARM Cortex-A9
hardware_versions:
- PYNQ-Z2 with Zynq-7020 (xc7z020clg400-1)
- ARM Cortex-A9 at 650 MHz (sustained 666 MHz)
inbound_links: 1
measurement_method: Physical hardware measurements on PYNQ-Z2 board; performance counters
  and power monitoring. Baseline ARM Cortex-A9 software with NEON-optimized implementations.
metrics:
- latency speedup
- energy reduction
- resource utilization
- timing slack
needs_summary_revision: true
scorecard:
  bridge_score: 0.8
  claim_density: 0.9
  hub_potential: 0.7
  novelty_delta: 0.9
  self_containedness: 0.9
software_versions:
- unspecified ARM software baseline
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
toolchains:
- GCC inline assembly
- ARM NEON
type: benchmark_result
updated: '2026-06-28'
workloads:
- MobileNet V2
- ResNet-18
- EfficientNet Lite
- YOLO Tiny
---

# PYNQ-Z2 RISC-V CNN ISA Extensions Benchmark

This page documents benchmark results for a custom RISC-V core with four novel ISA extensions (FPGA.VCONV, FPGA.GEMM, FPGA.RELU, FPGA.CUSTOM) implemented on the Xilinx PYNQ-Z2 platform (Zynq-7020 SoC) for neural network inference on edge devices. The system uses a 5-stage in-order RV32IM pipeline with integrated systolic array accelerators for convolution (4x4, 16 DSP slices), matrix multiplication (8x8, 64 MACs/cycle), and vector activation functions (16 parallel units). All measurements are obtained from physical hardware deployment on a single PYNQ-Z2 board. The baseline is an aggressively optimized ARM Cortex-A9 software baseline running the same models with NEON intrinsics. Four representative CNN models are benchmarked: MobileNet V2, ResNet-18, EfficientNet Lite, and YOLO Tiny. Key metrics include average latency speedup, energy reduction, FPGA resource utilization, and timing closure slack.

## Key Claims

- The complete system achieves a **2.14x average latency speedup** and **49.1% energy reduction** across all four benchmark models compared to the ARM Cortex-A9 software baseline.
- FPGA resource utilization for the base core: 0.43% of LUTs (229 of 53,200), 0.24% of FFs (253 of 106,400), 11.4% of BRAM.
- When accelerators are active, 38.8% of available DSP48E1 slices (85 of 220) are used.
- Timing closure is achieved with **+12.793 ns worst negative slack** at a 50 MHz clock frequency.
- The FPGA.VCONV instruction delivers a **7.20x speedup** over ARM NEON-optimized 3x3 convolution, utilizing 35% of DSP slices.
- The FPGA.GEMM instruction delivers **4.20x speedup** over ARM Cortex-A9, achieving 6.4 GOPS (INT16).
- The FPGA.RELU instruction achieves **3.00x speedup** and 85% instruction reduction for 1024-element vectors.
- The design uses a triple-buffering scheme to overlap computation with DMA transfers, achieving 87% hardware utilization in the convolution accelerator.
- The custom RISC-V core interfaces with accelerators via AXI4-Lite (control, 1 MB/s) and AXI4 (data, 850 MB/s measured bandwidth) buses.

## Measurement Context

- **Hardware version:** PYNQ-Z2 board with Xilinx Zynq-7020 SoC (xc7z020clg400-1). ARM Cortex-A9 dual-core at 650 MHz (measured sustained 666 MHz). FPGA fabric clocked at 50 MHz.
- **Software/toolchain version:** ARM baseline: unspecified OS and NEON-optimized libraries. RISC-V toolchain: GCC with inline assembly for custom instruction intrinsics.
- **Workload shape:** Four CNN models: MobileNet V2 (depthwise separable convolutions), ResNet-18 (standard 3x3 and 1x1 convolutions), EfficientNet Lite (depthwise separable and grouped convolutions), YOLO Tiny (small object detection with 3x3 convolutions). Input sizes as per standard model definitions (not specified).
- **Metric:** Average latency speedup (ratio of ARM baseline inference time to FPGA-accelerated time), energy reduction (percentage reduction in energy consumption per inference), FPGA resource utilization (LUTs, FFs, BRAM, DSPs), timing slack (worst negative slack).
- **Method:** Physical hardware measurements: inference time measured via cycle counters and external oscilloscope; power measured via current shunt on PYNQ-Z2 power rail; resource utilization from Vivado synthesis reports; timing analysis from Vivado static timing analysis. All measurements taken on a single board at room temperature.
- **Evidence strength:** measured

## Relationships

- [[DSC_Fused_Dataflow_Benchmark_Results]] – Both benchmark results target edge AI inference on FPGAs, but this work uses custom ISA extensions rather than a CFU-based dataflow approach.
- [[GEMM_with_RISC-V_Vector_Extension]] – Both involve RISC-V-based GEMM acceleration; this work uses custom instructions and FPGAs, while that page focuses on vector extensions for general-purpose CPUs.
- [[XuanTie_C908_SHL_GEMM_Optimization]] – Another RISC-V optimization for GEMM/convolution, but on a vendor core (XuanTie C908) rather than a custom FPGA-based core.

## Sources

- [arXiv:2511.06955](https://arxiv.org/abs/2511.06955)

