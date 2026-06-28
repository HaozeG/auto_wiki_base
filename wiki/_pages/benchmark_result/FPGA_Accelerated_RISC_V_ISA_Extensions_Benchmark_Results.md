---
cold_start: true
created: '2025-11-11'
datatypes: []
evidence_strength: measured
hardware_targets:
- PYNQ-Z2 (Xilinx Zynq-7020)
hardware_versions:
- PYNQ-Z2 (Xilinx Zynq-7020) at 50 MHz
inbound_links: 0
measurement_method: Physical hardware measurements on Xilinx PYNQ-Z2 FPGA at 50 MHz
  clock. Results are average over four benchmark models (MobileNet V2, ResNet-18,
  EfficientNet Lite, YOLO Tiny) compared against ARM Cortex-A9 software baseline.
metrics:
- average latency speedup
- energy reduction
- LUT utilization
- BRAM utilization
- DSP utilization
- worst negative slack
needs_summary_revision: false
scorecard:
  bridge_score: 0.9
  claim_density: 0.9
  hub_potential: 0.6
  novelty_delta: 0.9
  self_containedness: 0.8
software_versions: []
sources:
- https://arxiv.org/abs/2511.06955
tags:
- RISC-V
- FPGA
- ISA extensions
- PYNQ-Z2
- edge AI
toolchains: []
type: benchmark_result
updated: '2026-06-28'
workloads:
- MobileNet V2
- ResNet-18
- EfficientNet Lite
- YOLO Tiny
---

# FPGA-Accelerated RISC-V ISA Extensions Benchmark Results

Benchmark results for a custom RISC-V core with four neural network ISA extensions (FPGA.VCONV, FPGA.GEMM, FPGA.RELU, FPGA.CUSTOM) implemented on a Xilinx PYNQ-Z2 FPGA (Zynq-7020) at 50 MHz are reported in arXiv:2511.06955. The system was evaluated on MobileNet V2, ResNet-18, EfficientNet Lite, and YOLO Tiny models using physical hardware measurements. Against an ARM Cortex-A9 software baseline, the system achieves a 2.14x average latency speedup and 49.1% energy reduction. Hardware resource utilization includes 0.43% LUTs and 11.4% BRAM for the base core, and 38.8% DSPs when accelerators are active. Timing closure was verified with +12.793 ns worst negative slack at 50 MHz. All metrics are from actual FPGA deployment.

## Key Claims

- 2.14x average latency speedup across four benchmark models (MobileNet V2, ResNet-18, EfficientNet Lite, YOLO Tiny) relative to ARM Cortex-A9 software.
- 49.1% energy reduction compared to the same ARM baseline.
- Base core resource usage: 0.43% of available LUTs and 11.4% of available BRAM on PYNQ-Z2.
- Accelerator resource usage: 38.8% of available DSPs when active.
- Timing slack of +12.793 ns worst negative slack at 50 MHz clock.
- Hardware verification confirms successful FPGA deployment with 64 KB BRAM memory interface and AXI interconnect functionality.

## Measurement Context

- Hardware version: Xilinx PYNQ-Z2 (Zynq-7020) at 50 MHz clock.
- Software/toolchain version: Not specified in the available resource.
- Workload shape:
  - MobileNet V2: image classification.
  - ResNet-18: image classification.
  - EfficientNet Lite: image classification.
  - YOLO Tiny: object detection.
  (Exact input resolutions not specified in the available resource extract.)
- Metric:
  - Latency speedup (2.14x average).
  - Energy reduction (49.1%).
  - Resource utilization (LUTs, BRAM, DSPs as percentages).
  - Timing slack (ns).
- Method:
  - Physical hardware measurements on FPGA.
  - Comparison to ARM Cortex-A9 software execution on the same benchmark models, likely under similar power envelope.
  - Synthesis and implementation with Vivado toolchain (assumed).
- Evidence strength: measured (explicitly stated that all performance metrics are obtained from physical hardware measurements).

## Relationships

- [[DSC_Fused_Dataflow_Benchmark_Results]] – Another FPGA-based RISC-V benchmark for depthwise separable convolutions, presenting speedup and data movement reduction results.
- [[TVM_and_Gemmini_Accelerator_Benchmark_Results]] – Benchmark of a systolic array GEMM accelerator on Xilinx ZCU102, providing a contrast in FPGA acceleration approach and performance.

## Sources

- [arXiv:2511.06955](https://arxiv.org/abs/2511.06955)
