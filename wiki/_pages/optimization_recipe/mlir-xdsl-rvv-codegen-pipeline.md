---
canonical_name: MLIR-xDSL RVV Code Generation Pipeline
aliases:
- MLIR-xDSL GEMM Pipeline
- xDSL RVV lowerings
subtype: null
tags: []
hardware_targets:
- K230
- BananaPi F3
workloads:
- GEMM
datatypes: []
metrics:
- GFLOPS
- performance improvement
toolchains:
- MLIR
- xDSL
- OpenBLAS
constraints: []
evidence_strength: measured
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 0.9
  bridge_score: 0.7
  hub_potential: 0.6
sources:
- raw/cache/5452ac649cad6750.md
- https://arxiv.org/html/2603.17800v1
source_url: https://arxiv.org/html/2603.17800v1
fetched_at: '2026-07-03T13:55:59.001087+00:00'
type: optimization_recipe
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 2
outbound_links:
- target: c908-wino-gemm-optimization
  reason: Both pipelines target GEMM on RISC-V platforms, but the MLIR-xDSL approach
    prioritizes portability across different RVV implementations through compiler-driven
    code generation, while the C908 optimization is a hand-tuned library recipe specific
    to the XuanTie C908 core
---

# MLIR-xDSL RVV Code Generation Pipeline

The MLIR-xDSL RVV Code Generation Pipeline is a compilation approach that combines the MLIR compiler infrastructure with the xDSL Python-native toolkit to bridge missing lowering stages for RISC-V Vector (RVV) code generation. The pipeline uses custom intermediate representations and transformation passes implemented in xDSL to systematically translate high-level operations into specialized, hardware-aware C code that invokes RVV intrinsics. This approach enables portable, optimized kernel generation for RISC-V platforms without requiring hand-tuned assembly, targeting platforms such as K230 and BananaPi F3. The pipeline was evaluated on the General Matrix Multiplication (GEMM) kernel and produced performance up to 12.2 GFLOPS, outperforming OpenBLAS by 10–35% across square-matrix and transformer-based workloads derived from the BERT-Large model. Failure modes are not documented; the approach is designed for incremental adoption without modifying surrounding software stacks.

## Key Claims

- Current MLIR distributions lack complete end-to-end lowering paths for RVV targets, particularly for mapping high-level vector abstractions to RVV intrinsics.
- The pipeline implements missing lowering stages using custom xDSL dialects and transformation passes.
- Generated kernels are emitted as portable C functions invoking RVV intrinsics, enabling integration into existing applications.
- On the GEMM kernel, the approach achieves up to 12.2 GFLOPS, compared to OpenBLAS baseline of 5.1 GFLOPS, a performance improvement of 10–35%.
- Evaluation was conducted on two real RISC-V platforms: the K230 and the BananaPi F3.
- Workloads include square-matrix benchmarks and transformer-based workloads derived from the BERT-Large model.

## Transformation

- Prerequisites: MLIR compiler infrastructure, xDSL toolkit, RISC-V platform with RVV support (e.g., K230 or BananaPi F3).
- Steps:
  1. Analyze MLIR's missing lowering stages for RVV code generation.
  2. Design and implement custom xDSL dialects that model RVV semantics and vector-length-agnostic programming.
  3. Implement xDSL transformation passes for vector-length-aware code generation.
  4. Generate specialized C code that invokes RVV intrinsics for the target kernel (e.g., GEMM).
  5. Emit the generated code as portable C functions that can be directly integrated into existing applications.
- Expected effect: Performance improvements of 10–35% over OpenBLAS on GEMM, reaching up to 12.2 GFLOPS on supported platforms.
- Failure modes: Not specified; the approach assumes correct IR representation and transformation pass correctness.
- Measurements: Peak throughput of 12.2 GFLOPS vs 5.1 GFLOPS baseline; relative improvement of 10–35%.

## Relationships

- [[c908-wino-gemm-optimization]]: Both pipelines target GEMM on RISC-V platforms, but the MLIR-xDSL approach prioritizes portability across different RVV implementations through compiler-driven code generation, while the C908 optimization is a hand-tuned library recipe specific to the XuanTie C908 core.

## Sources

- https://arxiv.org/html/2603.17800v1
