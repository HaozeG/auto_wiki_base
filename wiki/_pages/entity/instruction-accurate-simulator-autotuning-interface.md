---
canonical_name: Instruction-Accurate Simulator Autotuning Interface
aliases:
- TVM gem5 Autotuning
- ISS-based autotuning
- Score Predictor for Autotuning on Simulators
subtype: null
tags: []
scorecard:
  novelty_delta: 0.6
  claim_density: 0.5
  self_containedness: 0.3
  bridge_score: 0.6
  hub_potential: 0.5
sources:
- raw/cache/3cfe2c9d2588c53f.md
- https://arxiv.org/html/2505.13357v1
source_url: https://arxiv.org/html/2505.13357v1
fetched_at: '2026-07-06T02:43:14.485429+00:00'
type: entity
created: '2026-07-06'
updated: '2026-07-06'
cold_start: true
inbound_links: 0
outbound_links:
- target: mlir-xdsl-rvv-codegen-pipeline
  reason: The simulator interface can be used to evaluate the MLIR-xDSL RVV Code Generation
    Pipeline's GEMM kernels on simulated RISC-V targets, providing performance predictions
    before hardware is available
- target: mlir-xdsl-gemm-benchmark-k230-banana-pi
  reason: The score predictor approach could be applied to predict benchmark results
    for GEMM workloads on platforms like K230 and BananaPi F3, potentially reducing
    dependence on physical hardware
- target: c908-wino-gemm-optimization
  reason: The interface could evaluate the SHL-based optimization recipes for the
    XuanTie C908 on simulated cores, enabling early performance estimation before
    C908 hardware is accessible
---

# Instruction-Accurate Simulator Autotuning Interface

The instruction-accurate simulator autotuning interface is a methodology developed by researchers at RWTH Aachen University that enables the execution of TVM autotuning workloads on instruction-accurate simulators such as gem5 and QEMU, rather than on real hardware. This approach addresses the challenges of limited hardware availability and non-determinism in native benchmarking by extracting TVM tasks and running them as executables in parallel simulator instances. Additionally, a score predictor is trained using simulation statistics—such as instruction counts and cache metrics—to forecast the runtime performance of ML workload implementations on the target hardware. The tuned predictors have proven highly effective: the best implementation in terms of actual runtime on real hardware is always within the top 3% of predictions for tested x86, ARM, and RISC-V architectures.

## Key Claims

- The interface extracts TVM tasks and provides them as executables for the target architecture via a configurable number of parallel simulator instances.
- The approach offers high scalability when target hardware availability is limited, as many simulations can run in parallel on any accessible hardware.
- A predictor is trained on simulation statistics (e.g., from gem5 or QEMU) to estimate real-hardware performance.
- The best workload implementation based on runtime is always within the top 3% of predictions for x86, ARM, and RISC-V-based architectures.
- In the best case, the approach outperforms native execution on embedded architectures when running as few as three samples on three simulators in parallel.

## Relationships

- [[mlir-xdsl-rvv-codegen-pipeline]]: The simulator interface can be used to evaluate the MLIR-xDSL RVV Code Generation Pipeline's GEMM kernels on simulated RISC-V targets, providing performance predictions before hardware is available.
- [[mlir-xdsl-gemm-benchmark-k230-banana-pi]]: The score predictor approach could be applied to predict benchmark results for GEMM workloads on platforms like K230 and BananaPi F3, potentially reducing dependence on physical hardware.
- [[c908-wino-gemm-optimization]]: The interface could evaluate the SHL-based optimization recipes for the XuanTie C908 on simulated cores, enabling early performance estimation before C908 hardware is accessible.

## Sources

- https://arxiv.org/html/2505.13357v1
