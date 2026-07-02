---
canonical_name: Coral NPU Vector Execution Engine
aliases:
- Coral NPU RVV engine
- Coral Zve32x vector engine
- Google Coral RVV vector execution engine
- Coral NPU Zve32x
subtype: null
tags:
- Coral
- Google
- RISC-V
- RVV
- NPU
- Zve32x
hardware_targets:
- Coral NPU Vector Execution Engine
toolchains:
- GCC
- LLVM
constraints:
- RISC-V Vector Extension 1.0 (RVV)
- Zve32x subset
- VLEN >= 128 bits
- TCM memory interface
- Separate SIMD instruction queue and decode unit
scorecard:
  novelty_delta: 0.8
  claim_density: 0.6
  self_containedness: 0.8
  bridge_score: 0.3
  hub_potential: 0.3
sources:
- raw/cache/c1f7129db820ded3.md
- https://developers.google.com/coral/guides/hardware/rvv-vector-engine
source_url: https://developers.google.com/coral/guides/hardware/rvv-vector-engine
fetched_at: '2026-07-02T05:23:54.107226+00:00'
type: hardware_target
created: '2026-07-02'
updated: '2026-07-02'
cold_start: false
inbound_links: 5
needs_summary_revision: false
---

# Coral NPU Vector Execution Engine

The Coral NPU Vector Execution Engine is a RISC-V vector processing unit designed by Google as part of the Coral edge AI platform. It implements the Zve32x subset of the RISC-V Vector Extension version 1.0, providing SIMD vector capabilities for machine learning and other data-parallel workloads. The scalar RISC-V core within the Coral NPU handles initial instruction fetch, decode, and dispatch, including the dispatching of vector instructions to the vector execution engine. The vector engine maintains its own SIMD instruction queue, decoding unit, register file with scoreboard, and sub-computation units (ALU, multiply, divide, MAC). Apart from the TCM memory interface, the vector unit operates independently of the scalar core once instructions have been enqueued. This architectural separation allows the vector engine to process data in parallel while the scalar core continues other work. Keeping the instruction queue full is identified as key to achieving peak performance. The engine supports the standard RVV features including 32 vector registers (V0-V31) each VLEN bits wide (minimum 128 bits), configurable vector length via vsetvli, length-agnostic programming, and a comprehensive set of vector instructions for integer and floating-point arithmetic.

## Key Claims

- Coral NPU implements the Zve32x subset of RISC-V Vector Extension 1.0.
- The vector execution engine has its own instruction queue, decode unit, register file with scoreboard, and dedicated ALU/multiply/divide/MAC units.
- The vector unit operates independently of the scalar core after instructions are enqueued, only sharing the TCM memory interface.
- Vector instructions are dispatched from the scalar core to the vector engine's separate instruction queue.
- Keeping the vector instruction queue full is critical for performance.
- The engine supports dynamic vector length configuration and length-agnostic code.
- Toolchain support includes auto-vectorization in GCC and LLVM compilers.

## Optimization-Relevant Details

- ISA/profile: RISC-V Vector Extension 1.0, Zve32x subset (minimum 128-bit VLEN).
- Vector/matrix/accelerator support: 32 vector registers, configurable VLEN, chaining support, mask registers with v0 as mask operand.
- Memory/cache/TCM: Interface via TCM (Tightly Coupled Memory); unit-stride, strided, indexed, and segment vector loads/stores.
- Compiler/toolchain support: GCC and LLVM with RVV auto-vectorization and intrinsic support.

## Relationships

- Coral NPU's vector engine is a hardware target for optimization recipes such as [[mlir_xdsl_rvv_gemm_codegen_recipe]], which leverages RVV intrinsics and auto-vectorization for GEMM workloads.
- The engine runs code compiled by the [[llvm_riscv_target]] backend, which provides LLVM support for RVV 1.0 including Zve32x.
- As an RVV 1.0 implementation, it is comparable to other RVV hardware targets like [[sifive_performance_p570_gen3]] (which uses a 128-bit vector pipeline) though the Coral engine is purpose-built for edge AI inference.

## Sources

- https://developers.google.com/coral/guides/hardware/rvv-vector-engine
