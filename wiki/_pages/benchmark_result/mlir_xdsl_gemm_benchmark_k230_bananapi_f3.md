---
canonical_name: MLIR+xDSL RISC-V Vector GEMM Benchmark on K230 and BananaPi F3 vs
  OpenBLAS
aliases:
- RVV GEMM 12.2 GFLOPS
- MLIR-xDSL GEMM performance
- K230 BananaPi F3 matrix multiplication benchmark
subtype: null
tags:
- GEMM
- RVV
- MLIR
- xDSL
- OpenBLAS
hardware_targets:
- K230
- BananaPi F3
workloads:
- gemm - square‑matrix benchmarks - BERT‑Large transformer workloads
datatypes:
- fp32
metrics:
- GFLOPS
- speedup vs OpenBLAS
toolchains:
- MLIR+xDSL generated C (RVV intrinsics)
- OpenBLAS (baseline)
hardware_versions:
- K230 (RISC‑V platform with RVV)
- BananaPi F3 (RISC‑V platform with RVV)
software_versions:
- MLIR+xDSL pipeline (2026‑03 submission)
- OpenBLAS version unspecified (presumably latest)
measurement_method: Measured on physical hardware; benchmarks included square matrix
  sizes and BERT‑Large model layers; GFLOPS derived from execution time.
evidence_strength: reported
scorecard:
  novelty_delta: 0.9
  claim_density: 0.85
  self_containedness: 0.85
  bridge_score: 0.7
  hub_potential: 0.6
sources:
- raw/cache/5452ac649cad6750.md
- https://arxiv.org/html/2603.17800v1
source_url: https://arxiv.org/html/2603.17800v1
fetched_at: '2026-07-01T03:46:09.006884+00:00'
type: benchmark_result
created: '2026-07-01'
updated: '2026-07-01'
cold_start: true
inbound_links: 0
needs_summary_revision: true
---

# MLIR+xDSL RISC-V Vector GEMM Benchmark on K230 and BananaPi F3 vs OpenBLAS

This benchmark result reports the performance of auto‑generated GEMM micro‑kernels produced by an MLIR+xDSL compilation pipeline on two RISC‑V platforms – the K230 and the BananaPi F3. The kernels implement a GotoBLAS‑style micro‑tile of outer‑product operations using RVV intrinsics. The comparison baseline is OpenBLAS on the same hardware. Across square‑matrix benchmarks and transformer‑based workloads (BERT‑Large), the generated code consistently outperforms OpenBLAS by 10–35%. The best measured result reaches 12.2 GFLOPS, exceeding the baseline’s 5.1 GFLOPS. The measurement was physically taken on the two boards; detailed methodology (matrix sizes, layer profiling) is drawn from the companion paper (arXiv:2603.17800v1).

## Key Claims

- On K230 and BananaPi F3, the MLIR+xDSL‑generated gemm micro‑kernel achieves up to 12.2 GFLOPS.
- OpenBLAS baseline on the same platforms reaches 5.1 GFLOPS.
- Speedup ranges from 10% to 35% across evaluated workloads, including square‑matrix benchmarks and BERT‑Large operations.
- The results validate the generated code’s ability to outperform a highly hand‑tuned library (OpenBLAS) without manual tuning.

## Measurement Context

- Hardware version: K230 (RISC‑V SoC with RVV), BananaPi F3 (RISC‑V board with RVV); no further microarchitectural details provided in the source.
- Software/toolchain version: MLIR+xDSL pipeline version as submitted in March 2026; OpenBLAS version unspecified but represents a production‑ready baseline.
- Workload shape: gemm (matrix multiplication) with varied square sizes; also transformer layers from BERT‑Large.
- Metric: GFLOPS (millions of floating‑point operations per second).
- Method: Physical execution on both boards; GFLOPS derived from execution time and operation count.
- Evidence strength: reported (paper claims results from physical measurements, but raw data not replicated here).

## Relationships

- Derived from the optimization recipe: [[mlir_xdsl_rvv_gemm_codegen_recipe]]
- The workload kernel is a GEMM micro‑kernel; see also [[xuantie_c908_fp16_gemm_kernel]] for a different hardware‑specific hand‑optimized kernel.

## Sources

- arXiv:2603.17800v1, "Enabling RISC-V Vector Code Generation in MLIR through Custom xDSL Lowerings"
