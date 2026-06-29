---
cold_start: true
created: '2025-07-07'
datatypes:
- ternary
evidence_strength: reported
hardware_targets:
- x86 CPU with AVX2
hardware_versions:
- x86 AVX2
inbound_links: 3
measurement_method: ASIC synthesis for power/area; performance estimates from simulation
  (paper does not specify exact simulator)
metrics:
- latency
- throughput
- power
- area
- energy
scorecard:
  bridge_score: 0.7
  claim_density: 0.8
  hub_potential: 0.7
  novelty_delta: 0.9
  self_containedness: 0.8
software_versions: []
sources:
- https://arxiv.org/html/2511.13676v1
tags:
- ternary
- LLM
- SIMD
- T-SAR
- CPU inference
- edge
toolchains: []
type: benchmark_result
updated: '2026-06-29'
workloads:
- Ternary LLM inference (GEMM/GEMV)
---

# T-SAR Benchmark Results

T-SAR (Ternary SIMD ALU Reorganization) is a full-stack co-design framework for ternary LLM inference on CPUs, targeting the x86 AVX2 ISA. The benchmark results reported in the paper demonstrate performance on GEMM and GEMV operations for ternary LLMs ranging from 125 million to 100 billion parameters. Measurements are derived from ASIC synthesis (for power and area overhead) and simulation (for latency and throughput). The hardware target is a generic x86 CPU with AVX2 SIMD units; specific CPU model is not disclosed. Compared to state-of-the-art CPU baselines (T-MAC and BitNet.cpp), T-SAR achieves large improvements while maintaining minimal hardware overhead.

## Key Claims

- T-SAR achieves 5.6–24.5× GEMM latency reduction over SOTA CPU baselines (T-MAC, BitNet.cpp).
- T-SAR achieves 1.1–86.2× GEMV throughput improvement over SOTA CPU baselines.
- T-SAR incurs only 3.2% power and 1.4% area overhead in SIMD units.
- T-SAR delivers 2.5–4.9× higher energy efficiency than NVIDIA Jetson AGX Orin GPU on Llama-8B and Falcon3-10B ternary models.
- T-SAR eliminates memory bottlenecks by generating ternary lookup tables (TLUTs) in SIMD registers, reducing TLUT memory accesses from over 75% of system memory requests to near zero.

## Measurement Context

- **Hardware version:** x86 CPU with AVX2 SIMD units (simulated in ASIC synthesis for power/area; CPU model unspecified).
- **Software/toolchain version:** Not specified in the available resource.
- **Workload shape:** Ternary LLM inference; GEMM and GEMV operations for models with 125M to 100B parameters. Specific models tested: Llama-8B (ternary variant), Falcon3-10B (ternary variant).
- **Metric:** GEMM latency, GEMV throughput, power (W), area (%), energy efficiency (relative).
- **Method:** Power and area overhead estimated from ASIC synthesis in a 28nm process. Performance improvements derived from simulation of the proposed ISA extensions and microarchitecture. Baselines T-MAC and BitNet.cpp are reimplemented and measured on the same simulated hardware.
- **Evidence strength:** reported (claims from the paper; source code or independent verification not available in extracted content).

## Relationships

- [[Chiplet_RISC_V_AI_SoC_Benchmark_Results]] – Another benchmark result page for RISC-V-based AI SoC, providing a comparison point for efficiency.
- [[Tenstorrent_Grayskull_MatMul_Efficiency]] – A benchmark for MatMul efficiency on Tenstorrent Grayskull, relevant for edge AI inference.

## Sources

- [T-SAR paper on arXiv](https://arxiv.org/html/2511.13676v1)

