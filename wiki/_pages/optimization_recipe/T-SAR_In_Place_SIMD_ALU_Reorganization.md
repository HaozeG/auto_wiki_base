---
cold_start: true
constraints:
- SIMD register file
- minimal hardware modifications
created: '2025-07-07'
datatypes:
- ternary
evidence_strength: reported
hardware_targets:
- x86 CPU with AVX2
inbound_links: 0
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
sources:
- https://arxiv.org/html/2511.13676v1
tags:
- ternary
- LLM
- SIMD
- T-SAR
- CPU inference
- edge
- quantization
toolchains: []
type: optimization_recipe
updated: '2026-06-29'
workloads:
- Ternary LLM inference (GEMM/GEMV)
---

# T-SAR: In-Place SIMD ALU Reorganization for Ternary LLM Inference

T-SAR (Ternary SIMD ALU Reorganization) is a full-stack co-design framework that repurposes the SIMD vector register file for in-register lookup table (LUT) generation, enabling scalable ternary LLM inference on CPUs. The transformation targets x86 AVX2 ISA but extends to ARM NEON and RISC-V Vector. Prerequisites include a CPU with SIMD units and minimal hardware modification capability (e.g., register file wiring adjustments). The expected effect is eliminating the memory bottleneck caused by frequent LUT accesses in state-of-the-art ternary CPU kernels, achieving 5.6–24.5× GEMM latency reduction and 1.1–86.2× GEMV throughput improvement at only 3.2% power and 1.4% area overhead. Failure modes are not explicitly discussed but may include constraints from SIMD register file size limiting LUT capacity. Measurements are based on simulation and ASIC synthesis reported in the paper; evidence strength is classified as reported.

## Key Claims

- T-SAR eliminates memory bottlenecks by generating ternary LUTs dynamically inside SIMD registers, reducing TLUT traffic from >75% of memory requests to near zero.
- The algorithmic layer uses ternary-to-binary decomposition and data packing to enable efficient LUT computing.
- The ISA layer adds minimal extensions for register-to-register LUT-based GEMM and GEMV.
- The microarchitecture layer requires only lightweight wiring and multiplexing adjustments, validated by ASIC synthesis to incur 3.2% power and 1.4% area overhead.
- The software layer provides an adaptive kernel dataflow that maximizes throughput across diverse ternary LLM models (125M to 100B parameters).

## Transformation

- **Prerequisites:** x86 CPU with AVX2 SIMD (conceptually extensible to ARM NEON or RISC-V Vector with parameter retuning). Minimal hardware modification access (e.g., ability to add register-to-register LUT instructions). Ternary LLM model with weights constrained to {-1,0,1}.
- **Steps:**
  1. **Algorithmic:** Decompose ternary operations into binary representations and pack data to fit SIMD register widths (256-bit for AVX2).
  2. **ISA:** Introduce new instructions that perform in-register LUT generation and GEMM/GEMV using the SIMD register file.
  3. **Microarchitecture:** Modifies SIMD datapath to support the new instructions via small wiring and multiplexer changes; no new compute arrays or complex datapath extensions.
  4. **Software:** Implement adaptive kernel dataflow that selects block sizes and scheduling to maximize parallelism across triple issue constraints.
- **Expected effect:** Ternary LLM inference on edge CPUs becomes compute-bound rather than memory-bound, enabling significant latency/throughput gains (5.6–24.5× GEMM latency reduction, 1.1–86.2× GEMV throughput improvement) with minimal hardware overhead.
- **Failure modes:** Not explicitly described. Potential limitations include (1) SIMD register file size restricts LUT dimensions, (2) ISA extension requires compiler or runtime support, (3) adaptive kernel may require per-model tuning.
- **Measurements:** Refer to [[T-SAR_Benchmark_Results]] for detailed performance measurements. Power and area overheads from ASIC synthesis: 3.2% power, 1.4% area.

## Relationships

- [[GEMM_with_RISC-V_Vector_Extension]] – A different GEMM implementation using RISC-V vector extensions; T-SAR provides an alternative approach for ternary LLM inference.
- [[XuanTie_C908_SHL_GEMM_Optimization]] – Another optimization recipe for GEMM on a specific RISC-V CPU; T-SAR targets x86 CPUs but shares similar goal of accelerating matrix operations.

## Sources

- [T-SAR paper on arXiv](https://arxiv.org/html/2511.13676v1)

