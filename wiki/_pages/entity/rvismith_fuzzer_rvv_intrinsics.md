---
canonical_name: RVISmith
aliases:
- RVV intrinsics fuzzer
- RVISmith fuzzer
- 'RVISmith: Fuzzing Compilers for RVV Intrinsics'
subtype: null
tags:
- fuzzing
- compiler testing
- RVV
- RISC-V
- intrinsics
scorecard:
  novelty_delta: 0.9
  claim_density: 0.7
  self_containedness: 0.8
  bridge_score: 0.4
  hub_potential: 0.3
sources:
- raw/cache/67c8479b385ff24a.md
- https://arxiv.org/abs/2507.03773
source_url: https://arxiv.org/abs/2507.03773
fetched_at: '2026-07-01T04:26:15.192683+00:00'
type: entity
created: '2026-07-01'
updated: '2026-07-01'
cold_start: true
inbound_links: 0
needs_summary_revision: false
---

# RVISmith

RVISmith is a randomized fuzzer designed to detect bugs in compilers that handle RISC-V Vector (RVV) intrinsics. It automatically generates well-defined C programs containing diverse invocation sequences of RVV intrinsic functions, aiming to achieve high intrinsic coverage and sequence variety while avoiding known undefined behaviors. The tool is built upon the ratified RVV intrinsic specification and targets modern compilers including GCC, LLVM, and the XuanTie compiler. In experimental evaluation, RVISmith achieved 11.5 times higher intrinsic coverage compared to prior state-of-the-art fuzzers for RVV intrinsics. Through differential testing across different compilers, optimization levels, and equivalent programs, it identified 13 previously unknown compiler bugs, of which 10 have been confirmed and 3 fixed by compiler developers.

## Key Claims

- Achieves 11.5× higher intrinsic coverage than the state-of-the-art fuzzer for RVV intrinsics.
- Design objectives: high intrinsic coverage, improved sequence variety, avoidance of undefined behaviors.
- Implementation based on the ratified RVV intrinsic specification.
- Evaluation performed on three compilers: GCC, LLVM, and XuanTie.
- Discovered 13 previously unknown bugs; 10 confirmed and 3 fixed.
- Uses differential testing across compilers, optimizations, and equivalent programs.

## Relationships

- The RVISmith fuzzer targets the same RISC-V Vector Extension (RVV) intrinsics used in compilation pipelines such as [[mlir_xdsl_rvv_gemm_codegen_recipe]].
- Insufficient context for additional cross-links.

## Sources

- He, Y. "RVISmith: Fuzzing Compilers for RVV Intrinsics". arXiv:2507.03773 [cs.CR], Jul 2025. https://arxiv.org/abs/2507.03773
