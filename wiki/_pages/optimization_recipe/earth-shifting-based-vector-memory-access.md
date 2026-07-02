---
canonical_name: EARTH Shifting-Based Vector Memory Access
aliases:
- EARTH shifting network optimization
- EARTH LSDO
- EARTH RCVRF
subtype: null
tags: []
hardware_targets:
- Saturn RISC-V Vector Unit
workloads:
- const-stride memory access
- segment memory access
datatypes: []
metrics:
- latency
- throughput
- power
- area
toolchains: []
constraints:
- RISC-V Vector Extension (RVV)
evidence_strength: reported
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
type: optimization_recipe
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 15
---

# EARTH Shifting-Based Vector Memory Access Optimization

EARTH (Efficient Architecture for RISC-V Vector Memory Access) is a microarchitectural optimization for vector load/store units that replaces high-overhead crossbars with specialized shift networks for data routing. For const-stride accesses, a Load/Store Data Organization (LSDO) module coalesces multiple cache line accesses into a single memory request and uses a shift network for gather/scatter. For segment operations, a Row/Column-access Vector Register File (RCVRF) provides direct column-wise access, enabling in-place bulk transposition. The optimization was implemented on FPGA using Chisel HDL based on the open-source Saturn RISC-V vector unit and evaluated against a conventional design. Reported measurements show 4x–8x speedups in const-stride dominated benchmarks, 9% area reduction, and 41% power reduction.

## Key Claims

- Shifting-based data routing in LSDO eliminates the need for large crossbar interconnects for gather/scatter operations in const-stride accesses.
- RCVRF enables column-wise access without dedicated segment buffers, reducing area.
- The combined optimization yields 4x–8x performance improvement in const-stride dominated benchmarks.
- Area is reduced by 9% and power by 41% compared to conventional vector memory access designs.

## Transformation

- Prerequisites: A RISC-V vector unit with a baseline vector load/store unit that uses crossbar-based routing or issues multiple cache line requests for strided accesses. The Saturn open-source RISC-V vector unit serves as the base implementation.
- Steps: Replace the crossbar-based gather/scatter logic with a layered shift network (LSDO). Integrate a Row/Column-access Vector Register File (RCVRF) that supports both row-wise and column-wise access patterns. For const-stride accesses, implement coalescing logic to combine multiple accesses to the same cache line into a single memory request. For segment operations, use the RCVRF to perform bulk transposition without dedicated buffers.
- Expected effect: Const-stride memory accesses achieve 4x–8x speedup proportionally to their prevalence in workloads. Segment operations become area-efficient without throughput loss. Overall hardware area reduces by 9% and power consumption by 41%.
- Failure modes: The shifting network may introduce additional latency for non-stride patterns, though the paper indicates minimal overhead. The RCVRF adds complexity to register file design; timing closure may be impacted.
- Measurements: Speedup of 4x–8x on benchmarks dominated by const-stride operations; 9% area reduction; 41% power reduction. Evidence strength: reported (from research paper).

## Relationships

- [[cpa-factored-gemmini-systolic-array]]: Both recipes target hardware efficiency improvements in RISC-V related designs, with EARTH focusing on vector memory access and the CPA factoring focusing on systolic array PE optimization.
- [[llvm-riscv-fptrunc-narrowing-optimization]]: This compiler optimization targets floating-point performance on RISC-V; combined with EARTH's memory access improvements, vectorized workloads could benefit synergistically.

## Sources

- [Efficient Architecture for RISC-V Vector Memory Access](https://arxiv.org/html/2504.08334v2)
