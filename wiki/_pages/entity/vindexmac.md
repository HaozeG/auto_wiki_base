---
canonical_name: vindexmac
aliases:
- vector index-multiply-accumulate
- vindexmac instruction
subtype: null
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.6
  self_containedness: 0.8
  bridge_score: 0.5
  hub_potential: 0.2
sources:
- raw/cache/7af6635f48aaad4a.md
- https://arxiv.org/abs/2501.10189
source_url: https://arxiv.org/abs/2501.10189
fetched_at: '2026-07-03T18:15:24.634309+00:00'
type: entity
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 0
---

# vindexmac

vindexmac (vector index-multiply-accumulate) is a proposed custom instruction for RISC-V vector processors that performs an indirect read from the vector register file followed by multiply-accumulate, enabling efficient structured-sparse matrix multiplication. The instruction is designed to reduce the number of instructions executed per iteration of sparse-dense matrix multiplication without introducing additional dependencies that would limit loop unrolling. It was proposed in a 2025 research paper by Titopoulos et al. from Democritus University of Thrace, supported by a research grant from Codasip. The instruction targets state-of-the-art Convolutional Neural Network (CNN) inference and training workloads, where structured sparsity is used to prune model complexity. Integration into a decoupled RISC-V vector processor requires negligible hardware cost, and experimental results show a 25% to 33% runtime improvement over highly-optimized vectorized kernels that use only the currently defined RISC-V vector instructions.

## Key Claims

- vindexmac adds a single instruction to the RISC-V vector ISA that allows indirect reads from the vector register file, enabling a fused index-load-multiply-accumulate operation.
- The instruction reduces the number of instructions executed per structured-sparse matrix multiplication iteration by eliminating separate address computation and load instructions without adding loop-carried dependencies.
- Integration into a decoupled RISC-V vector processor requires negligible hardware cost.
- Experimental evaluation on CNN execution shows runtime improvements of 25% and 33% compared to baseline vectorized kernels using only the standard RISC-V vector instruction set.

## Relationships

No specific relationship to visible context pages.

## Sources

- https://arxiv.org/abs/2501.10189
