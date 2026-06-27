---
type: entity
tags: [risc-v, LLVM, compiler, clang, RVV, auto-vectorization, toolchain]
sources:
  - https://arxiv.org/html/2605.10860
  - https://arxiv.org/pdf/2309.16509
  - http://riscv.epcc.ed.ac.uk/issues/compiling-vector/
  - https://link.springer.com/book/10.1007/979-8-8688-2169-1
created: 2026-06-27
updated: 2026-06-27
cold_start: true
inbound_links: 0
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# RISC-V LLVM Backend

The RISC-V LLVM backend is the official Clang/LLVM compiler infrastructure for generating RISC-V machine code, covering both scalar and vector (RVV) code generation and auto-vectorization. Upstream LLVM has supported RISC-V since LLVM 7 (2018), with RVV 1.0 support (C API intrinsics, auto-vectorization via VPlan Loop Vectorizer and SLP Vectorizer) fully integrated in Clang 15 (2022). The backend implements Vector Length Agnostic (VLA) code generation using LLVM's scalable vector types, and Vector Length Specific (VLS) code generation when target hardware capabilities are known. SiFive, Barcelona Supercomputing Center (BSC), and Codeplay contributed core pieces of the RVV intrinsic and codegen infrastructure. As of 2024–2025, evaluation shows LLVM/GCC RVV codegen trails ARM SVE compiler maturity, particularly for irregular loop patterns and inter-lane reduction operations, but is closing the gap.

## Key Claims

- Clang 15 (2022) provides full RISC-V RVV 1.0 C API intrinsic support, enabling portable hand-vectorized RVV code without inline assembly.
- LLVM's VPlan-based Loop Vectorizer generates scalable (VLA) vector code for RISC-V, targeting any VLEN without recompilation.
- Programmers can force vector-length-specific code with `-riscv-v-vector-bits-min=N` or enable VLA via `-scalable-vectorization=on`.
- The SIMD Everywhere (SIMDe) library enables automatic translation from ARM NEON intrinsics to RISC-V RVV intrinsics via LLVM.
- A 2024–2025 study of GCC 15 and LLVM 21 on six HPC/ML proxy applications found that both compilers underperform compared to ARM SVE codegen maturity.
- IntrinTrans (2025) uses LLMs to translate existing SIMD intrinsic code to RVV intrinsics, addressing the portability bottleneck for existing vectorized codebases.
- LLVM provides both auto-vectorization and explicit RVV intrinsics; benchmarks show explicit intrinsics outperform auto-vectorization by ~35% for convolution-heavy ML workloads.

## Relationships

- [[gnu_toolchain_riscv_vector]]: GCC's RVV support competes with LLVM's; combined they form the primary open-source RISC-V compiler stack; LLVM generally leads on intrinsic coverage.
- [[mlir_riscv_backend]]: MLIR uses LLVM as its final lowering backend; MLIR's vector dialect ultimately compiles to RISC-V through LLVM's RVV codegen.
- [[tvm_riscv_backend]]: TVM can use either LLVM or custom code generation for RISC-V; its 46% latency improvement over GCC benchmarks via custom schedule passes.
- [[risc_v_vector_extension]]: RVV 1.0 is the ISA target for LLVM's RISC-V vector code generation infrastructure.
- [[muriscv_nn]]: muRISCV-NN shows that hand-tuned intrinsics achieve ~60% improvement over LLVM auto-vectorization on convolutional layers.

## Sources

- https://arxiv.org/html/2605.10860
- https://arxiv.org/pdf/2309.16509
- http://riscv.epcc.ed.ac.uk/issues/compiling-vector/
- https://link.springer.com/book/10.1007/979-8-8688-2169-1
