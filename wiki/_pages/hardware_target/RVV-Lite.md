---
cold_start: true
constraints:
- Subset of RVV instructions
- Predefined subset of RVV
created: '2025-03-25'
hardware_targets:
- RVV-Lite
- RISC-V Vector Extension (RVV)
inbound_links: 0
scorecard:
  bridge_score: 0.7
  claim_density: 0.6
  hub_potential: 0.5
  novelty_delta: 0.9
  self_containedness: 0.8
sources:
- https://open.library.ubc.ca/media/stream/pdf/24/1.0431080/3
tags:
- RISC-V
- RVV
- vector
- ISA
- subset
- RVV-Lite
toolchains: []
type: hardware_target
updated: '2026-06-29'
---

# RVV-Lite

RVV-Lite is a proposed subset of the official RISC-V Vector Extension (RVV) that partitions the full instruction set of over 400 instructions into a smaller, predefined subset, enabling resource-constrained implementations without compromising compatibility with the standard. Developed as part of a layered approach to the RVV ISA, RVV-Lite reduces the hardware complexity required for vector processing by selecting a minimal set of essential operations, while retaining the ability to accelerate common workloads. The implementation described in the academic paper includes dedicated address generation units (AGUs) for vector load (VLD) and vector store (VST) operations within a direct memory access (DMA) engine, highlighting the hardware-level optimizations possible with a streamlined ISA.

## Key Claims

- RVV-Lite is a partitioning of the full RISC-V Vector Extension (RVV), which comprises over 400 instructions.
- The subset allows users to deploy a smaller implementation with a predefined subset of instructions, targeting lightweight and cost-sensitive devices.
- The proposed design includes additional AGUs in the DMA engine for vector load (VLD) and vector store (VST) operations.
- The concept was presented in the paper "A Layered Approach to the Official RISC-V Vector ISA" (Apr 18, 2023).
- RVV-Lite maintains compatibility with the standard RISC-V Vector ISA while reducing hardware overhead.

## Optimization-Relevant Details

- ISA/profile: RISC-V Vector Extension (RVV) subset, layered approach for smaller deployments.
- Vector/matrix/accelerator support: Focused on integer and floating-point vector operations, subset selected for essential workloads.
- Memory/cache/TLB/DMA: Enhanced DMA engine with separate AGUs for VLD and VST operations.
- Compiler/toolchain support: Not specified in available resource.

## Relationships

- [[GEMM_with_RISC-V_Vector_Extension]] – A workload kernel that leverages the full RVV, providing contrast to the lightweight RVV-Lite subset.
- [[Gemmini_Architecture]] – An open-source DNN accelerator generator integrated with RISC-V SoC that could benefit from a layered vector extension approach.

## Sources

- [A Layered Approach to the Official RISC-V Vector ISA (UBC Library)](https://open.library.ubc.ca/media/stream/pdf/24/1.0431080/3)

