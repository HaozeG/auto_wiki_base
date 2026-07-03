---
canonical_name: K230
aliases:
- Kendryte K230
- K230 SoC
- CanMV-K230
- CanMV K230
- K230 CanMV
- Kendryte K230 CanMV
- CanMV K230 development board
subtype: hardware_target
type: hardware_target
tags: []
sources:
- raw/cache/ad5bac76fff61d4e.md
- https://www.kendryte.com/ai_docs/en/main/Introduction_to_This_Document.html
- raw/cache/8dc1b8fc652db78e.md
- https://deepwiki.com/kendryte/k230_canmv_docs
- raw/cache/e6bdd614ff99edbc.md
- https://owhinata.github.io/canmv-k230/en/
- raw/cache/f9558347e39a510f.md
- https://www.kendryte.com/en/proDetail/230
hardware_targets:
- K230
toolchains:
- K230_SDK
- nncase
- AI Cube
- KTS (k230_training_scripts)
- CanCollectorPlus
constraints:
- multi-precision AI computing
- utilization >70% for some typical networks
- low latency
- low power consumption
- quick startup
- high security
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 0
scorecard:
  novelty_delta: 0.8
  claim_density: 0.5
  self_containedness: 0.7
  bridge_score: 0.2
  hub_potential: 0.3
source_url: https://www.kendryte.com/ai_docs/en/main/Introduction_to_This_Document.html
fetched_at: '2026-07-03T13:35:08.582836+00:00'
---

# K230

The K230 is a system-on-chip (SoC) from Canaan Technology's Kendryte series, designed for AIoT applications. It features a multi-heterogeneous unit accelerated computing architecture that integrates two high-efficiency RISC-V computing cores and a new generation KPU (Knowledge Process Unit) intelligent computing unit. The KPU supports multi-precision AI computing and achieves utilization rates exceeding 70% for some typical networks. Additionally, the chip includes specialized hardware acceleration units for scalar, vector, and graphic computations, such as 2D and 2.5D units, enabling full-process acceleration of image, video, audio, and AI tasks. Documentation and development tools provided include the K230_SDK, nncase model converter, AI Cube, and KTS training scripts.

## Key Claims

- Multi-heterogeneous unit architecture with two RISC-V cores and KPU.
- Multi-precision AI computing with >70% utilization for some typical networks.
- Hardware acceleration for 2D/2.5D graphics.
- Low latency, high performance, low power, quick startup, high security.
- AI development flow: data preparation, model training, model conversion, KModel generation, image burning, board operation.
- Supports general AI computing frameworks.
- Tools: K230_SDK, nncase, AI Cube, KTS, CanCollectorPlus, online cloud training platform.
- Over 50 AI demo examples for different scenarios.

## Optimization-Relevant Details

- ISA/profile: RISC-V (version not specified)
- Vector/matrix/accelerator support: KPU for AI, 2D/2.5D units for graphics
- Memory/cache/TLB/DMA: Not specified
- Compiler/toolchain support: K230_SDK, nncase, AI Cube, KTS, CanCollectorPlus

## Relationships

No specific relationship to visible context pages.

## Sources

- https://www.kendryte.com/ai_docs/en/main/Introduction_to_This_Document.html
