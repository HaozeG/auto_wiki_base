---
cold_start: false
created: '2025-03-04'
datatypes:
- int8
evidence_strength: measured, reported
hardware_targets:
- Xilinx Artix-7 FPGA
- ASIC 28nm
- ASIC 40nm
hardware_versions:
- Xilinx Artix-7
- 28nm ASIC
- 40nm ASIC
inbound_links: 14
measurement_method: FPGA measurements (speedup, data movement); ASIC synthesis (area,
  power)
metrics:
- speedup
- data movement reduction
- area
- power
needs_summary_revision: true
scorecard:
  bridge_score: 0.6
  claim_density: 0.9
  hub_potential: 0.4
  novelty_delta: 0.7
  self_containedness: 0.9
software_versions: []
sources:
- https://arxiv.org/abs/2511.21232
tags:
- TinyML
- DSC
- fused dataflow
- zero-buffer
- RISC-V
- CFU
- FPGA
toolchains:
- TFLite
- CFU-Playground
type: benchmark_result
updated: '2026-06-28'
workloads:
- Depthwise Separable Convolution (DSC)
---

# DSC Fused Dataflow Benchmark Results

Benchmark results for the fused pixel-wise dataflow accelerator for Depthwise Separable Convolutions (DSC) are measured on a Xilinx Artix-7 FPGA and projected via ASIC synthesis in 28nm and 40nm processes. The accelerator implements a pixel-wise streaming dataflow within a Custom Function Unit (CFU) for a RISC-V processor, targeting TinyML workloads. Metrics include speedup over baseline software execution, data movement reduction, area, and power consumption. These results are sourced from the paper "RISC-V Based TinyML Accelerator for Depthwise Separable Convolutions in Edge AI" (arXiv:2511.21232) and provide the primary quantitative evidence for the optimization recipe [[DSC_Fused_Dataflow_Optimization_Recipe]].

## Key Claims

- The accelerator achieves a **59.3x speedup** over baseline RISC-V software execution on the Xilinx Artix-7 FPGA.
- Data movement is reduced by **up to 87%** compared to conventional layer-by-layer execution due to elimination of intermediate buffers.
- ASIC synthesis at 28nm projects **0.284 mm² area** and **910 mW power** at 2 GHz.
- ASIC synthesis at 40nm projects **1.20 mm² area** and **233 mW power** at 300 MHz.
- The accelerator targets Depthwise Separable Convolutions as used in MobileNetV2 inverted residual blocks.

## Measurement Context

- **Hardware version:** Xilinx Artix-7 FPGA (measurement); 28nm and 40nm ASIC (synthesis projection).
- **Software/toolchain version:** Baseline TFLite software on RISC-V; CFU-Playground for accelerator integration.
- **Workload shape:** Depthwise Separable Convolution (inverted residual block: expansion 1x1, depthwise 3x3, projection 1x1). Input feature map size typical of MobileNetV2 layers (e.g., 38 KB intermediate map).
- **Metric:** Speedup (59.3x), data movement reduction (87%), area (mm²), power (mW).
- **Method:** FPGA measurements with timing analysis; ASIC synthesis using standard tool flows (not specified in detail in the paper).
- **Evidence strength:** measured (FPGA), reported (ASIC synthesis).

## Relationships

- [[DSC_Fused_Dataflow_Optimization_Recipe]] – The optimization recipe describing the fused pixel-wise dataflow technique.
- [[XuanTie_C908_SHL_GEMM_Optimization]] – Another RISC-V optimization recipe for GEMM/convolution, providing contrast with a vectorized approach.

## Sources

- [arXiv:2511.21232](https://arxiv.org/abs/2511.21232)

