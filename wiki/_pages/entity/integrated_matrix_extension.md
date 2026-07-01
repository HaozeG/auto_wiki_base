---
canonical_name: Integrated Matrix Extension
aliases:
- IME
- RISC-V IME
- Integrated Matrix Extension
- RISC-V Integrated Matrix Extension
subtype: null
tags:
- RISC-V
- ISA
- Matrix Extension
scorecard:
  novelty_delta: 0.9
  claim_density: 0.85
  self_containedness: 0.9
  bridge_score: 0.7
  hub_potential: 0.8
sources:
- raw/cache/625d7add9a61f380.md
- https://riscv.atlassian.net/wiki/spaces/IMEX/pages/480149572/Strawman+for+an+IME+extension
source_url: https://riscv.atlassian.net/wiki/spaces/IMEX/pages/480149572/Strawman+for+an+IME+extension
fetched_at: '2026-07-01T03:49:43.066247+00:00'
type: entity
created: '2026-07-01'
updated: '2026-07-01'
cold_start: true
inbound_links: 1
needs_summary_revision: false
---

# Integrated Matrix Extension (IME)

The Integrated Matrix Extension (IME) is a strawman proposal for a RISC‑V ISA extension that accelerates dense linear algebra computations, particularly the General Matrix Multiplication (GEMM) micro‑kernel, **without introducing new architected state for matrix data**. IME reuses the existing 32 vector registers of the “V” vector extension to store matrix tiles, treating them as accumulators and operand storage. It defines custom instructions for packing matrix panels, accumulating outer products, and scaling/accumulating results, while allowing use of general‑purpose and floating‑point scalar registers and possibly new control registers. The design centres on a portable micro‑kernel template parameterised by datatypes (e.g., fp32, bfloat16) and geometry (µ, ν, Λ) and can be expressed with a small set of intrinsics such as `__riscv_vmzeroacc`, `__riscv_v{f}mmacc`. IME aims to serve as a discussion draft to identify requirements, constraints, and concrete implementations before formal standardisation.

## Key Claims

- IME operates exclusively on the vector register file (32 × VLEN) and does not add new matrix registers.
- The primary accelerated operation is C ← α(A×B)+βC (GEMM) with support for mixed precision (e.g., SBGEMM, SGEMM).
- GEMM micro‑kernel follows a packed‑panel layout: A panel (µ×K) stored in row‑major blocks of size µ×Λ, B panel (K×ν) stored in column‑major blocks of size Λ×ν, and C panel (µ×ν) stored in row‑major with leading dimension γ.
- Intrinsics: `__riscv_vmzeroacc()` zeroes the internal µ×ν accumulator T; `__riscv_v{f}mmacc(A, B)` performs T ← T + A_κ×Λ × B_κ×ν for each κ; `__riscv_v{f}mmacc(C, α, γ)` scales T by α and accumulates into C.
- The micro‑kernel’s type properties ⟨τ(A), τ(B), τ(C)⟩ and geometric properties ⟨µ, ν, Λ⟩ are fixed per instantiation; call‑time arguments include K, α, and panel pointers.
- Edge cases (when K not a multiple of Λ or when outer dimensions exceed µ, ν) are handled outside the micro‑kernel by the macro‑kernel.

## Relationships

- This extension could be instantiated on hardware targets that support the RISC‑V vector extension, such as the [[xuantie_c908_fp16_gemm_kernel]] workload kernel which illustrates a manual outer‑product GEMM using the existing vector registers.
- Compiler pipelines like [[mlir_xdsl_rvv_gemm_codegen_recipe]] that generate RVV intrinsics for GEMM micro‑kernels could be extended to target IME instructions once an implementation is available.

## Sources

- https://riscv.atlassian.net/wiki/spaces/IMEX/pages/480149572/Strawman+for+an+IME+extension
