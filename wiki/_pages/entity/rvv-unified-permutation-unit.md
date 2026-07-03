---
canonical_name: RVV Unified Permutation Unit
aliases:
- RVV unified permutation microarchitecture
- unified vector permutation unit
- RVV VPU permutation unit
subtype: null
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.5
  self_containedness: 0.7
  bridge_score: 0.6
  hub_potential: 0.2
sources:
- raw/cache/652cc1d4ad8824ac.md
- https://arxiv.org/html/2505.07112v2
source_url: https://arxiv.org/html/2505.07112v2
fetched_at: '2026-07-03T18:19:13.009810+00:00'
type: entity
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 0
---

# RVV Unified Permutation Unit

The RVV Unified Permutation Unit is a hardware microarchitecture designed to execute all RISC-V Vector (RVV) permutation instructions with a fixed, data-independent latency, addressing the diverse control information structures of instructions such as vcompress and vrgather. Proposed by Titopoulos et al. (2025), the design targets short-vector-length machines with vector registers up to 256 bits and supports element widths of 8, 16, and 32 bits. The unified datapath eliminates the need for separate datapaths for different permutation classes, thereby minimizing area and hardware cost while meeting the fixed-latency requirement critical for preventing side-channel timing attacks in cryptographic accelerators. The unit achieves single-cycle execution for short vectors and can be pipelined for longer vectors using register grouping. Implemented in an open-source RISC-V vector processor using the ASAP7 7nm technology library and the OpenRoad physical synthesis flow, the permutation unit incurs only 1.5% area overhead relative to the total vector processor, with the overhead approaching 0% as the minimum supported element width increases.

## Key Claims

- Unified hardware architecture executes all RVV permutation instructions (e.g., vcompress, vrgather) regardless of control information semantics.
- Fixed, data-independent execution latency to protect against side-channel timing attacks in cryptographic accelerators.
- Single-cycle execution for vector lengths up to 256 bits; pipelined execution for longer vectors via register grouping.
- Supports element widths of 8, 16, and 32 bits.
- Integrated into an open-source RISC-V vector processor and synthesized at 7nm (ASAP7) using OpenRoad.
- Area overhead measured at 1.5% of total vector processor area.
- Area overhead decreases to near-0% as the minimum supported element width for permutations increases.

## Relationships

- Both this unit and the Q4X quantization kernel in [[q4x-quantization-llamacpp-rvv]] rely on the RVV extension; the permutation unit provides the microarchitectural capability to execute the vector permutation instructions that a dequantization kernel may use for flexible data rearrangement during inference on RVV-capable CPUs.

## Sources

- https://arxiv.org/html/2505.07112v2
