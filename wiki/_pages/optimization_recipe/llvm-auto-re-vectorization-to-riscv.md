---
canonical_name: Auto-Re-Vectorization via LLVM IR Transformation to RISC-V Vector
aliases:
- LLVM Auto-Re-Vectorization
- RISC-V Vector re-vectorization tool
- auto-re-vectorization from x86/ARM to RVV
subtype: null
tags: []
hardware_targets:
- x86 AVX
- ARM Neon
- RISC-V Vector (RVV)
workloads:
- matrix multiplication (implied evaluation)
datatypes: []
metrics:
- latency
- throughput
- power
toolchains:
- LLVM
- clang
- llc
- llvm-mca
constraints:
- RISC-V Vector Extension (RVV)
evidence_strength: reported
scorecard:
  novelty_delta: 0.7
  claim_density: 0.5
  self_containedness: 0.7
  bridge_score: 0.6
  hub_potential: 0.3
sources:
- raw/cache/a68687448a1c2429.md
- https://nisanthmp.wordpress.com/2025/04/25/auto-re-vectorization-into-riscv-vector-code-from-vector-simd-intrinsics-code-written-for-other-architectures-like-x86-avx-or-arm-vector-neon-using-llvm-infrastructure/
source_url: https://nisanthmp.wordpress.com/2025/04/25/auto-re-vectorization-into-riscv-vector-code-from-vector-simd-intrinsics-code-written-for-other-architectures-like-x86-avx-or-arm-vector-neon-using-llvm-infrastructure/
fetched_at: '2026-07-02T13:09:05.932315+00:00'
type: optimization_recipe
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# Auto-Re-Vectorization via LLVM IR Transformation to RISC-V Vector

This optimization recipe describes a method to automatically re-vectorize existing hand-optimized SIMD intrinsics (originally written for x86 AVX, AVX2, AVX512, or ARM Neon/Vector) into RISC-V Vector (RVV) assembly code by using LLVM intermediate representation (IR) transformations. The approach converts the input intrinsic code to LLVM IR, substitutes x86/ARM-specific target attributes with RISC-V Vector attributes, applies LLVM vector optimizer passes (default<O2>, loop-vectorize, slp-vectorizer, load-store-vectorizer), and finally lowers the optimized IR to RVV assembly. The method aims to produce more efficient machine code than compiling high-level C/C++ while requiring less manual effort than full hand-tuning. The tool and source code are released to the RISC-V community. Preliminary evaluation on a matrix multiplication kernel compares cycle counts against generic auto-vectorization, but detailed numeric results are pending publication at the RISC-V Europe Summit 2025.

## Key Claims

- The method leverages existing hand-optimized kernel patterns from x86 AVX and ARM Neon, avoiding the performance gap of generic auto-vectorization.
- Using LLVM IR as an intermediate representation allows reuse of LLVM's architecture-independent optimization passes.
- The transformation steps are: compile intrinsics to LLVM IR, replace target attributes, apply vector passes, and lower to RVV assembly via llc.
- The tool can also handle RISC-V Vector intrinsics with differing microarchitectures, enabling cross-microarchitecture re-vectorization.
- Cycle-based performance analysis is performed with llvm-mca using processor scheduling models.
- The approach outperforms header-based translations and a proprietary vendor tool on the matrix multiplication kernel (specific speedup values not yet disclosed).

## Transformation

- Prerequisites: Input source code with x86 AVX or ARM Neon intrinsic calls. LLVM/clang toolchain installed with RISC-V backend support (target riscv64). A RISC-V Vector processor model available for llvm-mca analysis.
- Steps:
  1. Compile the C/C++ intrinsic code to LLVM IR using clang with the appropriate target (e.g., `clang -target x86_64-unknown-linux-gnu -S -emit-llvm -mfma`).
  2. Modify the generated LLVM IR: replace `target triple`, `target-cpu`, `target-features`, and `tune-cpu` attributes from x86 to RISC-V Vector-specific values.
  3. Remove any `optnone` attribute from functions.
  4. Apply LLVM optimizer passes: `default<O2>`, `loop-vectorize`, `slp-vectorizer`, `load-store-vectorizer` using `opt` with `-mtriple=riscv64 -mcpu=<target CPU>`.
  5. Lower the optimized IR to RVV assembly using `llc -march=riscv64 -mattr=<target-features> -mcpu=<target CPU>`.
  6. Analyze the assembly with `llvm-mca` to estimate cycle counts and performance.
- Expected effect: Generated RVV code is expected to be more efficient than compiling high-level C/C++ for the same kernels, with structure that is easier to further hand-optimize. The method enables quick porting of existing vectorized libraries (e.g., BLIS, OpenBLAS, Eigen) to RISC-V Vector processors.
- Failure modes: The transformation may not preserve correctness if the LLVM IR passes alter semantics beyond what is intended (though validation is expected). Dependence on specific LLVM version; compatibility across LLVM releases may require adjustments. Performance is bounded by the quality of the LLVM backend for the target RISC-V Vector processor.
- Measurements: The authors report cycle-based comparisons for a matrix multiplication kernel against generic auto-vectorization and existing approaches. Detailed numeric results (speedup ratios, cycle counts) are to be published at the RISC-V Europe Summit 2025. Evidence strength: reported.

## Relationships

- [[vectrans]]: VecTrans is a related LLM-assisted compiler auto-vectorization framework; both target improved vectorization on RISC-V but use different approaches (LLM refactoring vs. IR attribute transplant and pass recycling).
- [[llvm-riscv-fptrunc-narrowing-optimization]]: This LLVM pass optimization for RISC-V FPTrunc narrowing demonstrates the kind of target-specific IR tuning that could complement the auto-re-vectorization method.
- [[earth-shifting-based-vector-memory-access]]: The EARTH optimization targets RISC-V vector memory access hardware; combined with efficient code generation from this recipe, vectorized workloads can achieve better overall performance.

## Sources

- [Auto-re-vectorization into RISCV Vector Code – Nisanth's Blog](https://nisanthmp.wordpress.com/2025/04/25/auto-re-vectorization-into-riscv-vector-code-from-vector-simd-intrinsics-code-written-for-other-architectures-like-x86-avx-or-arm-vector-neon-using-llvm-infrastructure/)
- RISC-V Europe Summit 2025 paper (to be published)
