---
canonical_name: MLIR+xDSL Lowering Pipeline for RISC-V Vector GEMM Micro-kernels
aliases:
- MLIR-xDSL RVV codegen
- Custom xDSL lowerings for RVV
- Enabling RISC-V Vector Code Generation in MLIR through Custom xDSL Lowerings
subtype: null
tags:
- MLIR
- xDSL
- RISC-V
- RVV
- GEMM
- code generation
hardware_targets:
- K230
- BananaPi F3
workloads:
- gemm
datatypes:
- fp32
metrics:
- GFLOPS
- speedup vs OpenBLAS
toolchains:
- MLIR
- xDSL
- LLVM
constraints:
- RISC-V Vector Extension (RVV) with vector-length-agnostic execution
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
type: optimization_recipe
created: '2026-07-01'
updated: '2026-07-01'
cold_start: true
inbound_links: 40
needs_summary_revision: true
---

# MLIR+xDSL Lowering Pipeline for RISC-V Vector GEMM Micro-kernels

This optimization recipe describes a compilation approach that combines the MLIR compiler infrastructure with the xDSL Python-native toolkit to bridge missing lowering stages for generating RISC-V Vector (RVV)‑intrinsic‑based C code. The pipeline transforms high‑level tensor operations into specialized, hardware‑aware micro‑kernels for the General Matrix Multiplication (gemm). The method avoids hand‑tuning by systematic code generation, enabling portable C functions that can be integrated into existing applications. The generated code exploits RVV vector‑length‑agnostic programming, intrinsic selection, and tile sizing, and has been validated on real RISC‑V platforms. When used in a gemm kernel following the GotoBLAS algorithm, the output consistently outperforms OpenBLAS, delivering up to 12.2 GFLOPS (a 10‑35% improvement) on the evaluated workloads.

## Key Claims

- MLIR distributions lack practical end‑to‑end lowering paths that map high‑level vector abstractions to RVV intrinsics; xDSL fills this gap with custom dialects and transformation passes.
- The pipeline systematically translates high‑level operations into hardware‑aware C code that calls RVV intrinsics, emitted as standalone portable functions.
- The generated micro‑kernels, when integrated into a Goto‑style gemm, outperform OpenBLAS on K230 and BananaPi F3 by 10–35%, achieving up to 12.2 GFLOPS versus the baseline’s 5.1 GFLOPS.
- The approach enables generation of a complete collection of micro‑kernel variants that can be fine‑tuned per layer for deep learning models such as BERT‑Large.

## Transformation

- Prerequisites: MLIR ecosystem, xDSL toolkit, LLVM with RVV support, a RISC‑V target with RVV hardware, GotoBLAS‑style macro‑kernel structure.
- Steps:
  1. Model the gemm micro‑kernel in MLIR’s tensor/affine dialects.
  2. Define custom xDSL IRs that explicitly represent RVV semantics (vector length, register blocking, memory layout).
  3. Implement xDSL lowering passes that progressively refine the IR from high‑level operations to RVV‑intrinsic calls and memory packing.
  4. Emit C code with RVV intrinsics that realises the micro‑tile outer‑product updates.
  5. Integrate the generated C function into the macro‑kernel loops.
- Expected effect: Portable, performance‑portable micro‑kernels that exploit RVV hardware and deliver 10‑35% speedup over OpenBLAS on real RISC‑V platforms.
- Failure modes: Mis‑sized tiles that degrade cache or register reuse; wrong intrinsic selection for a specific VLEN configuration; insufficient prefetching causing memory latency; lack of adaptation to different memory hierarchies leading to lower performance than hand‑tuned code.
- Measurements: On K230 and BananaPi F3, the generated gemm reaches 12.2 GFLOPS vs OpenBLAS 5.1; speedup between 10% and 35% across square‑matrix benchmarks and BERT‑Large transformer workloads.

## Relationships

- Validated by benchmark results on the same pipeline: [[mlir_xdsl_gemm_benchmark_k230_bananapi_f3]]
- The micro‑kernel shape follows the GotoBLAS algorithm and relates to workload kernels like [[xuantie_c908_fp16_gemm_kernel]] (note: different hardware).
- [[opengemm]]: a Chisel-based hardware GeMM accelerator generator for RISC-V edge devices — a hardware-acceleration alternative to this compiler-generated software micro-kernel approach.
- [[banana_pi_gemm_optimization_benchmark]]: hand-tuned/auto-vectorized RISC-V GEMM results on similar Banana Pi-class hardware, useful as an independent baseline comparison point.
- [[generic_micro_kernel_templates_gemm]]: a non-RISC-V (ARM/x86) template-based micro-kernel generation approach, offering a cross-architecture contrast to this RISC-V-specific MLIR+xDSL pipeline.
- [[mlir]]: the underlying LLVM compiler infrastructure this pipeline builds on, extended here with custom xDSL lowerings for RVV.

## Sources

- arXiv:2603.17800v1, "Enabling RISC-V Vector Code Generation in MLIR through Custom xDSL Lowerings"
