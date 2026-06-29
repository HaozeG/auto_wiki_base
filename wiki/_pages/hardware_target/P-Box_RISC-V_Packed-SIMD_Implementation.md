---
cold_start: true
constraints:
- edge device resource constraints
- scalar core baseline
- configurable design
created: '2026-07-14'
hardware_targets:
- RISC-V Packed-SIMD (RVP v0.9.11)
inbound_links: 1
scorecard:
  bridge_score: 0.7
  claim_density: 0.4
  hub_potential: 0.7
  novelty_delta: 0.9
  self_containedness: 0.6
sources:
- https://www.semanticscholar.org/paper/P-Box:-A-RISC-V-Packed-SIMD-Approach-of-Edge-on-Sukumaran-BabuP./fd5987ec0bf207a57f81690564a1d60ccdfb3c55
tags:
- RISC-V
- Packed-SIMD
- RVP
- edge AI
- DSP
- CV
- P-Box
toolchains: []
type: hardware_target
updated: '2026-06-29'
---

# P-Box: RISC-V Packed-SIMD Implementation

P-Box is the first modular and fully compliant implementation of the RISC-V Packed-SIMD (RVP v0.9.11) extension. It is designed to accelerate edge workloads on scalar cores by providing data-parallel processing capabilities for Digital Signal Processing (DSP), computer vision (CV), and lightweight AI inference. The implementation is configurable, allowing adaptation to different edge device requirements. P-Box demonstrates that the RISC-V Packed-SIMD extension offers a practical and efficient pathway for edge acceleration with relatively low hardware cost, making it suitable for resource-constrained edge devices where full vector extensions may be overkill. Initial evaluations indicate that P-Box enables significant performance improvements on DSP and CV tasks compared to scalar-only execution, though specific numerical benchmark results are not detailed in the available source.

## Key Claims

- First modular and fully compliant implementation of the RISC-V Packed-SIMD (RVP v0.9.11) extension.
- Configurable design tailored for edge workloads (DSP, CV, deep learning inference).
- Provides data-level parallelism on scalar cores without requiring full vector extensions.
- Demonstrates a practical and efficient acceleration pathway with relatively low hardware cost.

## Optimization-Relevant Details

- ISA/profile: RISC-V Packed-SIMD extension (RVP v0.9.11)
- Vector/matrix/accelerator support: Packed-SIMD sub-word parallelism within machine word
- Memory/cache/TLB/DMA: Not specified in available source; inferred to be scalar-core memory hierarchy
- Compiler/toolchain support: Not specified; likely requires compiler support for RVP intrinsics or auto-vectorization

## Relationships

- [[Chiplet_RISC_V_AI_SoC_Benchmark_Results]] – An example of a RISC-V AI accelerator benchmark on different hardware (chiplet-based), contrasting with the scalar-core approach of P-Box.
- [[Parallel_GEMM_Convolution_on_GAP8]] – An optimization recipe for edge AI on a different RISC-V platform (GAP8), illustrating alternative edge acceleration strategies.

## Sources

- [P-Box: A RISC-V Packed-SIMD Approach of Accelerating Edge ... – Semantic Scholar](https://www.semanticscholar.org/paper/P-Box:-A-RISC-V-Packed-SIMD-Approach-of-Edge-on-Sukumaran-BabuP./fd5987ec0bf207a57f81690564a1d60ccdfb3c55)
