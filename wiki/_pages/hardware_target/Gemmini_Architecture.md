---
cold_start: false
constraints:
- Configurable dataflow (output-stationary, weight-stationary, runtime-selectable)
- 'Datatypes: int8, int16, int32, float'
- 'Spatial array: systolic or vector'
- Full SoC integration with RISC-V
- Linux-capable SoC support
- Multi-level software stack (C, assembly, PyTorch, TVM)
created: '2026-07-02'
hardware_targets:
- Gemmini (hardware generator)
- TSMC 16nm FinFET (fabricated)
- Intel 22nm FFL (fabricated)
inbound_links: 12
needs_summary_revision: true
scorecard:
  bridge_score: 0.8
  claim_density: 0.9
  hub_potential: 0.7
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://arxiv.org/abs/1911.09925
tags:
- Gemmini
- DNN accelerator
- full-stack
- RISC-V
- systolic array
- vector array
- hardware generator
toolchains:
- C/C++
- assembly
- PyTorch
- TVM
type: hardware_target
updated: '2026-06-28'
---

# Gemmini Architecture

Gemmini is an open-source, full-stack DNN accelerator generator developed at UC Berkeley. It generates efficient ASIC accelerators from a flexible architectural template that supports both systolic and vector spatial arrays, multiple dataflows (output-stationary, weight-stationary, runtime-selectable), and a range of datatypes including int8 and float. Gemmini provides a multi-layered software stack with support for C/C++, assembly, PyTorch, and TVM, and integrates with a full RISC-V System-on-Chip (SoC) environment including Linux-capable OS support. The generated accelerators have been fabricated in TSMC 16nm FinFET and Intel 22nm FinFET Low Power process technologies, delivering up to 2670x speedups over high-performance CPUs on various DNN benchmarks and comparable performance to commercial DNN accelerators. Gemmini is designed to enable systematic, cross-stack evaluation of deep-learning architectures by capturing system-level effects such as SoC resource contention, OS overheads, and programming-stack inefficiencies.

## Key Claims

- Gemmini is open-source and generates a wide design-space of efficient ASIC accelerators from a flexible architectural template.
- Supports both systolic and vector spatial array architectures, enabling quantitative comparison.
- Supports multiple dataflows that can be configured at design time and run time: output-stationary, weight-stationary, and runtime-selectable.
- Supports integer (int8, int16, int32) and floating-point datatypes to handle training and inference workloads.
- Provides a multi-level software stack with programming interfaces for different developer needs: low-level C/assembly for expert control and high-level PyTorch/TVM for application practitioners.
- Integrates with a full RISC-V SoC including virtual memory, DMA, and Linux OS support, enabling execution of arbitrary software.
- Generated accelerators have been fabricated in TSMC 16nm FinFET and Intel 22nm FinFET Low Power (22FFL) processes.
- Achieves up to three orders-of-magnitude speedup over high-performance CPUs (specifically up to 2,670x) on DNN benchmarks.
- Delivers comparable performance to a state-of-the-art commercial DNN accelerator (NVDLA) with similar hardware configurations.
- Enables system-accelerator co-design, demonstrated through case studies optimizing virtual address translation and memory resource partitioning.

## Relationships

- [[TVM_and_Gemmini_Accelerator_Benchmark_Results]] – benchmark results from the integration of TVM with Gemmini for GEMM operations, measured on Xilinx ZCU102 FPGA.
- Insufficient context for additional cross-links to entity pages; Gemmini is associated with the RISC-V ecosystem, but no dedicated RISC-V entity page exists in the current wiki.

## Sources

- [arXiv:1911.09925](https://arxiv.org/abs/1911.09925)
