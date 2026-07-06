---
canonical_name: MLIR-xDSL GEMM Benchmark on K230 and BananaPi F3
aliases:
- MLIR-xDSL K230 GEMM Benchmark
- MLIR-xDSL BananaPi F3 GEMM
subtype: null
tags: []
hardware_targets:
- K230
- BananaPi F3
workloads:
- GEMM
- BERT-Large derived transformer workloads
datatypes: []
metrics:
- GFLOPS
- performance improvement
toolchains:
- MLIR
- xDSL
- OpenBLAS
hardware_versions: []
software_versions: []
measurement_method: Compared auto-generated GEMM micro-kernels against OpenBLAS on
  square-matrix benchmarks and transformer-based workloads derived from the BERT-Large
  model
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
type: benchmark_result
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 5
outbound_links:
- target: c908-wino-gemm-optimization
  reason: Both benchmarks measure GEMM performance on RISC-V platforms, but this benchmark
    evaluates a compiler-generated kernel from the MLIR-xDSL pipeline on K230/BananaPi
    F3, whereas the C908 benchmark measures a hand-tuned SHL library kernel on the
    XuanTie C908
---

# MLIR-xDSL GEMM Benchmark on K230 and BananaPi F3

The MLIR-xDSL GEMM Benchmark evaluates the performance of the MLIR-xDSL RVV code generation pipeline on two RISC-V platforms: the Canaan K230 and the Banana Pi F3. The benchmark compares auto-generated GEMM micro-kernels against the OpenBLAS library using square-matrix benchmarks and transformer-based workloads derived from the BERT-Large model. The primary metric is peak floating-point throughput (GFLOPS). On these platforms, the MLIR-xDSL generated kernels achieve up to 12.2 GFLOPS, compared to the OpenBLAS baseline of 5.1 GFLOPS, representing a performance improvement of 10–35% across the evaluated workloads. The measurement was conducted by the authors of the paper and is reported as a measured result; hardware and software version details beyond platform names are not specified in the available source.

## Key Claims

- MLIR-xDSL generated GEMM kernels achieve up to 12.2 GFLOPS on K230 and BananaPi F3.
- OpenBLAS baseline achieves 5.1 GFLOPS on the same platforms and workloads.
- Performance improvement ranges from 10% to 35% across square-matrix and BERT-Large derived transformer workloads.
- The benchmark demonstrates that compiler-generated code can outperform a highly optimized library like OpenBLAS for GEMM on these RISC-V platforms.

## Measurement Context

- Hardware version: K230 (Canaan, exact version not specified), BananaPi F3 (exact SoC version not specified).
- Software/toolchain version: MLIR (version not specified), xDSL (version not specified), OpenBLAS (version not specified).
- Workload shape: GEMM with square matrices and transformer-based workloads derived from the BERT-Large model.
- Metric: GFLOPS (peak throughput) and relative performance improvement (10–35%).
- Method: Comparison of auto-generated micro-kernels against OpenBLAS, likely running on the target hardware in a controlled environment.
- Evidence strength: measured (claimed and described as experimental evaluation in the paper).

## Relationships

- [[c908-wino-gemm-optimization]]: Both benchmarks measure GEMM performance on RISC-V platforms, but this benchmark evaluates a compiler-generated kernel from the MLIR-xDSL pipeline on K230/BananaPi F3, whereas the C908 benchmark measures a hand-tuned SHL library kernel on the XuanTie C908.

## Sources

- https://arxiv.org/html/2603.17800v1
