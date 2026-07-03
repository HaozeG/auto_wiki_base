---
canonical_name: LLVM Auto-Vectorization
aliases:
- Loop Vectorizer
- SLP Vectorizer
- LLVM vectorizers
subtype: null
tags: []
scorecard:
  novelty_delta: 0.8
  claim_density: 0.6
  self_containedness: 0.9
  bridge_score: 0.7
  hub_potential: 0.7
sources:
- raw/cache/8622dc8d962d154f.md
- https://llvm.org/docs/Vectorizers.html
source_url: https://llvm.org/docs/Vectorizers.html
fetched_at: '2026-07-02T09:46:29.214958+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# LLVM Auto-Vectorization

LLVM Auto-Vectorization refers to the automatic transformation of scalar code into vectorized code by the LLVM compiler infrastructure. LLVM includes two vectorizers: the Loop Vectorizer, which operates on loops and widens instructions to operate on multiple consecutive iterations, and the SLP (Superword-Level Parallelism) Vectorizer, which merges multiple independent scalars into vectors. Both vectorizers are enabled by default in LLVM and can be controlled via command-line flags and pragmas. They support features such as unknown trip count loops, runtime pointer checks, and reduction detection. The vectorizers use a cost model to determine optimal vectorization and unroll factors, and they provide diagnostic optimization remarks to identify vectorization successes and failures. This documentation covers LLVM 23.0.0git version features.

## Key Claims

- LLVM has two vectorizers: the Loop Vectorizer and the SLP Vectorizer.
- Both vectorizers are enabled by default.
- The Loop Vectorizer can be disabled via the `-fno-vectorize` flag in Clang.
- Users can force vector width with `-force-vector-width` and unroll factor with `-force-vector-interleave`.
- The `#pragma clang loop` directive allows enabling/disabling vectorization and setting vector width and interleave count.
- Diagnostic optimization remarks are available: `-Rpass=loop-vectorize` for successful vectorization, `-Rpass-missed=loop-vectorize` for failed loops, and `-Rpass-analysis=loop-vectorize` for causes of failure.
- The Loop Vectorizer handles loops with unknown trip count by scalarizing the remainder.
- The Loop Vectorizer inserts runtime checks for pointer aliasing to ensure legality.
- The Loop Vectorizer detects reductions (addition, multiplication, XOR, AND, OR) and vectorizes them.

## Relationships

- [[llvm-auto-re-vectorization-to-riscv]]: related via shared auto, llvm, vectorization.

- [[auto-vectorization-in-rust]]: related via shared auto, llvm, vectorization.

- [[xuantie-c950]]: The XuanTie C950 RISC-V core can benefit from LLVM auto-vectorization for optimized code generation, especially when targeting AI workloads.
- [[sifive-intelligence-x160-gen-2]]: The SiFive Intelligence X160 Gen 2 supports the RISC-V Vector Extension v1.0, which can be directly targeted by LLVM's Loop Vectorizer for improved performance.

## Sources

- [LLVM Auto-Vectorization Documentation](https://llvm.org/docs/Vectorizers.html)
