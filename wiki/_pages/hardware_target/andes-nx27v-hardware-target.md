---
canonical_name: AndesCore NX27V
aliases:
- NX27V
- Andes NX27V
subtype: null
tags: []
hardware_targets:
- AndesCore NX27V
toolchains:
- LLVM
- OpenCL
constraints:
- RVV 1.0 support
- 512-bit VLEN, extendable to 4096-bit via LMUL
- Fractional LMUL options
- Out-of-order Vector Processing Unit (VPU)
- Up to 512-bit results per cycle
- Streaming Port via ACE framework
- ISA: RISC-V with RVV 1.0
scorecard:
  novelty_delta: 0.85
  claim_density: 0.8
  self_containedness: 0.85
  bridge_score: 0.5
  hub_potential: 0.6
sources:
- raw/cache/6fe9adad4bc59e28.md
- https://us.design-reuse.com/news/?id=49087&print=yes
source_url: https://us.design-reuse.com/news/?id=49087&print=yes
fetched_at: '2026-07-03T15:52:48.190918+00:00'
type: hardware_target
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 3
outbound_links:
- target: xuantie-c906-hardware-target
  reason: Both are commercial RISC-V cores with vector processing capabilities; however,
    the NX27V implements the RISC-V Vector Extension (RVV) 1.0 standard with a 512-bit
    VLEN and out-of-order VPU, while the XuanTie C906 uses a custom 128-bit SIMD unit
    and an in-order pipeline
---

# AndesCore NX27V

The AndesCore NX27V is a commercial RISC-V vector processor IP core developed by Andes Technology Corporation, announced in December 2020 as the first commercial RISC-V vector processor upgraded to support the RISC-V Vector Extension (RVV) version 1.0. It implements a Cray-like full vector compute engine with 512-bit vector registers extendable to 4,096 bits through LMUL settings, and supports fractional LMUL options for configuration flexibility. The NX27V contains a scalar unit and an out-of-order vector processing unit (VPU) with multiple functional units capable of generating up to 512-bit results per cycle. It supports standard RVV data types (integer, fixed-point, floating-point) and Andes-enhanced data types for AI representations. The core is designed for high-data-rate applications such as AI, AR/VR, computer vision, cryptography, and multimedia.

## Key Claims

- Supports RISC-V Vector Extension (RVV) version 1.0 with new instructions including vector floating-point reciprocal and reciprocal square-root estimate.
- Vector registers are 512 bits wide, extendable to 4,096 bits via LMUL setting, with fractional LMUL options for reduced register usage.
- Contains an out-of-order vector processing unit (VPU) with multiple functional units achieving up to 512-bit results per cycle.
- Achieves over 26x speedup on the MobileNet v1 convolutional neural network with 512-bit VLEN and SIMD width (vendor-reported).
- Includes a Streaming Port based on the Andes Custom Extension (ACE) framework for efficient data exchange between registers and external modules.
- Provides standard development tools, RVV compute libraries, AndesClarity visualization and analysis tool, and OpenCL with integrated LLVM compiler for heterogeneous computing.
- NX27V won the 2020 ASPENCORE World Electronics Achievement Award in the category of Outstanding Product Performance of the Year.
- Available in configurations of 256-bit or 512-bit VLEN and SIMD width.

## Optimization-Relevant Details

- ISA/profile: RISC-V with RVV 1.0 extension, LMUL fractional options
- Vector/matrix/accelerator support: Out-of-order VPU with 512-bit VLEN, up to 4096-bit via LMUL; supports integer, fixed-point, floating-point and AI-optimized data types
- Memory/cache/TLB/DMA: Streaming Port interface (ACE-based) for decoupled command/data channels, DMA-capable external hardware interface
- Compiler/toolchain support: LLVM, OpenCL, AndesClarity, RVV compute libraries

## Relationships

- [[xuantie-c906-hardware-target]]: Both are commercial RISC-V cores with vector processing capabilities; however, the NX27V implements the RISC-V Vector Extension (RVV) 1.0 standard with a 512-bit VLEN and out-of-order VPU, while the XuanTie C906 uses a custom 128-bit SIMD unit and an in-order pipeline.

## Sources

- https://us.design-reuse.com/news/?id=49087&print=yes
