---
canonical_name: EARTH (Vector Memory Access Architecture)
aliases:
- EARTH
- Efficient Architecture for RISC-V Vector Memory Access
subtype: null
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 0.9
  bridge_score: 0.7
  hub_potential: 0.5
sources:
- raw/cache/34adfd5830c6afe2.md
- https://arxiv.org/html/2504.08334v2
source_url: https://arxiv.org/html/2504.08334v2
fetched_at: '2026-07-02T10:44:58.571562+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# EARTH (Vector Memory Access Architecture)

EARTH (Efficient Architecture for RISC-V Vector Memory Access) is a novel vector memory access architecture that uses shifting-based optimizations to handle const-stride and segment memory access patterns in RISC-V vector processors. It was introduced in a 2024 research paper by Hongyi Guan et al. EARTH integrates specialized shift networks for gathering and scattering strided elements, enabling coalescing of multiple cache line accesses into a single memory request. For segment operations, it employs a shifted register bank called RCVRF (Row/Column-access Vector Register File) that provides direct column-wise access, eliminating the need for dedicated segment buffers while supporting in-place bulk transposition. The design was implemented on FPGA using Chisel HDL, based on the open-source Saturn RISC-V vector unit. EARTH demonstrates performance improvements of 4x–8x in benchmarks dominated by const-stride operations, along with a 9% reduction in hardware area and 41% reduction in power consumption compared to conventional vector memory access designs.

## Key Claims

- EARTH achieves 4x–8x speedups in benchmarks dominated by const-stride memory access operations.
- The architecture reduces hardware area by 9% and power consumption by 41% compared to conventional designs.
- The RCVRF (Row/Column-access Vector Register File) enables column-wise access without dedicated segment buffers.
- The LSDO (Load/Store Data Organization) design allows coalescing multiple accesses within the same cache line into a single memory request.
- EARTH is implemented on FPGA using Chisel HDL and is based on the open-source Saturn RISC-V vector unit.

## Relationships

- [[cpa-factored-gemmini-systolic-array]]: Both EARTH and the CPA-factored Gemmini optimization target hardware efficiency improvements in RISC-V related accelerators, though EARTH focuses on vector memory access while Gemmini targets systolic array processing elements.
- [[llvm-riscv-fptrunc-narrowing-optimization]]: This LLVM optimization improves floating-point performance on RISC-V vector processors, which could complement EARTH's memory access improvements in vectorized workloads.

## Sources

- [Efficient Architecture for RISC-V Vector Memory Access](https://arxiv.org/html/2504.08334v2)
