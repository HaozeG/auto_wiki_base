---
canonical_name: Semidynamics Tensor Unit
aliases:
- Semidynamics RISC-V Tensor Unit
- Semidynamics Tensor Unit (coherent)
subtype: null
tags:
- RISC-V
- tensor unit
- AI accelerator
- Semidynamics
- coherent
hardware_targets:
- Semidynamics Tensor Unit
toolchains:
- RISC-V vector-enabled Linux (implied)
constraints:
- RISC-V Vector Extension 1.0 (RVV1.0)
- Cache-coherent subsystem
- No new architecturally-visible state
scorecard:
  novelty_delta: 0.9
  claim_density: 0.75
  self_containedness: 0.75
  bridge_score: 0.5
  hub_potential: 0.4
sources:
- raw/cache/5ef450fb4fdde907.md
- https://semiwiki.com/forum/index.php?threads/semidynamics-launches-first-fully-coherent-risc-v-tensor-unit-to-supercharge-ai-applications.19065/
source_url: https://semiwiki.com/forum/index.php?threads/semidynamics-launches-first-fully-coherent-risc-v-tensor-unit-to-supercharge-ai-applications.19065/
fetched_at: '2026-07-02T05:13:28.668379+00:00'
type: hardware_target
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# Semidynamics Tensor Unit

The Semidynamics Tensor Unit is a fully-coherent RISC-V tensor accelerator announced by Semidynamics in October 2023. Designed to accelerate matrix multiplication workloads for AI applications such as large language models, the unit is built on top of the Semidynamics RVV1.0 Vector Processing Unit, leveraging existing vector registers to store matrices. It integrates with the Atrevido-423 core and the Gazzillion technology for data prefetching, avoiding the need for difficult-to-program DMAs. The Tensor Unit claims a 128x performance improvement over scalar core execution and does not introduce new architecturally-visible state, enabling seamless operation under standard RISC-V vector-enabled Linux without kernel modifications.

## Key Claims

- First fully-coherent RISC-V tensor unit (per Semidynamics announcement).
- 128x performance increase over executing AI software on the scalar core alone.
- Built on RVV1.0 Vector Processing Unit; leverages existing vector registers for matrix storage.
- No new architecturally-visible state; works with any RISC-V vector-enabled Linux without changes.
- Integrated with Gazzillion technology to fetch data at high rates, avoiding DMA programming overhead.
- Designed for matrix multiplication in Fully Connected and Convolution layers; Vector Unit handles activation functions.

## Optimization-Relevant Details

- ISA/profile: RISC-V Vector Extension 1.0 (RVV1.0).
- Vector/matrix/accelerator support: Tensor Unit for matrix multiplication, Vector Unit for activation functions; uses vector registers.
- Memory/cache/TLB/DMA: Cache-coherent subsystem with Gazzillion for data fetching; no separate DMA required.
- Compiler/toolchain support: Compatible with RISC-V vector-enabled Linux; no special OS changes.

## Relationships

- Compare to [[xuantie_c908]]: both are RISC-V accelerators for AI, but the Semidynamics Tensor Unit emphasizes cache coherence and no new architectural state, while the C908 uses instruction fusion and configurable VLEN.
- Contrast with [[k230]]: the K230 integrates a fixed-function KPU for AI acceleration, whereas the Semidynamics Tensor Unit is a more programmable solution integrated with a vector unit and coherent memory.

## Sources

- https://semiwiki.com/forum/index.php?threads/semidynamics-launches-first-fully-coherent-risc-v-tensor-unit-to-supercharge-ai-applications.19065/
