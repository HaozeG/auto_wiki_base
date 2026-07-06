---
canonical_name: AndesCore AX45MPV
aliases:
- AX45MPV
- Andes AX45MPV
subtype: null
tags: []
hardware_targets:
- AndesCore AX45MPV
toolchains: []
constraints:
- 8-stage superscalar pipeline
- Multicore support
- VPU up to 1024-bit VLEN/DLEN
- RISC-V standard extensions: G (IMA-FD), C, B, P (draft), V
- Andes custom performance enhancements
- AndeStar V5 architecture
scorecard:
  novelty_delta: 0.7
  claim_density: 0.5
  self_containedness: 0.8
  bridge_score: 0.4
  hub_potential: 0.2
sources:
- raw/cache/1a6f6e310ba00991.md
- https://www.andestech.com/en/products-solutions/andescore-processors/riscv-ax45mpv/
source_url: https://www.andestech.com/en/products-solutions/andescore-processors/riscv-ax45mpv/
fetched_at: '2026-07-03T15:53:36.798803+00:00'
type: hardware_target
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 6
outbound_links:
- target: andes-nx27v-hardware-target
  reason: Both are commercial RISC-V vector processor IP cores from Andes Technology
    based on the AndeStar V5 architecture. However, the AX45MPV provides a larger
    VPU (1024-bit VLEN/DLEN) and multicore support, while the NX27V implements RVV
    1.0 with 512-bit VLEN (extendable to 4096-bit via LMUL) and an out-of-order VPU
    in a single-core configuration
---

# AndesCore AX45MPV

AndesCore AX45MPV is a 64-bit multicore RISC-V CPU IP core developed by Andes Technology Corporation, featuring an 8-stage superscalar pipeline and a vector processing unit (VPU) with support for up to 1024-bit vector length (VLEN) and data width (DLEN). It is based on the AndeStar V5 architecture and implements the RISC-V standard extensions 'G' (IMA-FD), 'C' (16-bit compression), 'B' (bit manipulation), 'P' (DSP/SIMD, draft), and 'V' (vector), along with Andes custom performance enhancements. The core targets high-bandwidth data-intensive applications such as computer vision, digital signal processing, image processing, machine learning, deep learning, and scientific computing. It is designed for use in ADAS, AI inference and training, AR/VR, multimedia, robotics, and signal processing SoCs.

## Key Claims

- 8-stage superscalar pipeline with multicore support.
- Vector processing unit (VPU) capable of up to 1024-bit VLEN and DLEN.
- Supports RISC-V standard extensions G, C, B, P (draft), and V.
- Based on AndeStar V5 architecture with Andes custom performance enhancements.
- Targets data-intensive workloads: computer vision, DSP, image processing, ML/DL, scientific computing.
- General availability announced in September 2023 for SoCs in ADAS, AI, AR/VR, multimedia, robotics, and signal processing.

## Optimization-Relevant Details

- ISA/profile: RISC-V with extensions G, C, B, P (draft), V
- Vector/matrix/accelerator support: VPU with up to 1024-bit VLEN/DLEN
- Memory/cache/TLB/DMA: Not specified in source
- Compiler/toolchain support: Not specified in source

## Relationships

- [[andes-nx27v-hardware-target]]: Both are commercial RISC-V vector processor IP cores from Andes Technology based on the AndeStar V5 architecture. However, the AX45MPV provides a larger VPU (1024-bit VLEN/DLEN) and multicore support, while the NX27V implements RVV 1.0 with 512-bit VLEN (extendable to 4096-bit via LMUL) and an out-of-order VPU in a single-core configuration.

## Sources

- https://www.andestech.com/en/products-solutions/andescore-processors/riscv-ax45mpv/
