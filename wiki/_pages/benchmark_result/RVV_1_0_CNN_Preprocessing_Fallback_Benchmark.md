---
cold_start: false
created: '2026-07-07'
datatypes: []
evidence_strength: reported
hardware_targets:
- RISC-V SoC with DLA (NVDLA)
- RISC-V Vector 1.0
hardware_versions:
- unspecified RISC-V SoC (Chipyard framework)
- RVV 1.0
inbound_links: 0
measurement_method: Experimental results reported in paper; specific measurement platform
  not detailed in abstract. The paper states 'experimentally verify performance bottlenecks'
  but system-level simulation details are not provided.
metrics:
- speedup
needs_summary_revision: true
scorecard:
  bridge_score: 0.7
  claim_density: 0.75
  hub_potential: 0.5
  novelty_delta: 0.85
  self_containedness: 0.8
software_versions: []
sources:
- https://arxiv.org/html/2507.17771v1
tags:
- RVV 1.0
- CNN
- pre-processing
- YOLOv3
- NVDLA
- VecBoost
- DLA fallback
toolchains:
- VecBoost
type: benchmark_result
updated: '2026-06-28'
workloads:
- image pre-processing
- YOLOv3 fallback layers
---

# RVV-1.0 CNN Pre-processing and Fallback Acceleration Benchmark

This page reports benchmark results from the paper "Flexible Vector Integration in Embedded RISC-V SoCs for End-to-End CNN Inference Acceleration" (arXiv:2507.17771v1). The paper evaluates a RISC-V Vector 1.0 coprocessor integrated into a System-on-Chip (SoC) containing a Deep Learning Accelerator (DLA). The aim is to accelerate image pre-processing and fallback layer execution for convolutional neural networks (CNNs), specifically YOLOv3. According to the paper, the vector-based approach yields up to 9× speedup for image pre-processing and up to 3× speedup for YOLOv3 fallback layers compared to CPU-only execution. The authors introduce VecBoost, an open-source vector library of common fallback operations supporting RVV 1.0. The results highlight the potential of using the RISC-V Vector extension to reduce preprocessing bottlenecks and CPU fallback in accelerator-rich embedded SoCs.

## Key Claims

- Up to 9× speedup for image pre-processing using RVV 1.0 vector instructions compared to CPU-only execution.
- Up to 3× speedup for YOLOv3 fallback layer execution compared to CPU-only execution.
- The integration of a vector coprocessor within the Chipyard framework reduces pre-processing bottlenecks and CPU fallback processes.
- VecBoost, an open-source vector library of common fallback operations, supports RVV 1.0.
- The RISC-V Vector 1.0 extension is presented as a flexible target for balanced computation in accelerator-rich embedded SoCs.

## Measurement Context

- **Hardware version:** Unspecified RISC-V SoC with DLA (likely NVDLA) integrated via Chipyard; RISC-V Vector 1.0 extension assumed.
- **Software/toolchain version:** VecBoost library; no compiler or framework version specified in abstract.
- **Workload shape:** Image pre-processing operations (not further detailed) and YOLOv3 CNN inference (fallback layers).
- **Metric:** Speedup (ratio of execution time on CPU baseline vs. CPU+vector coprocessor).
- **Method:** Experimental results reported in the paper; likely simulation or FPGA emulation within Chipyard, but not confirmed.
- **Evidence strength:** reported (claims from paper abstract; full experimental setup not available in provided content).

## Relationships

- [[RVV_Autovectorization_Optimization_Insights]] – An optimization recipe for RVV autovectorization that provides broader context on RVV performance characteristics.
- [[Chiplet_RISC_V_AI_SoC_Benchmark_Results]] – A benchmark page for a chiplet-based RISC-V AI SoC with different acceleration approach.
- Note: insufficient context for additional cross-links to entity pages.

## Sources

- [arXiv:2507.17771v1](https://arxiv.org/html/2507.17771v1)
