---
cold_start: false
constraints:
- PCI Express Gen 5.0 x16
- GDDR6 DRAM
- 12x 400G Ethernet
- 2D Torus NoC
- 300W TBP (P150)
- 600W TBP (P300)
- Active or passive cooling
- 2xAMD EPYC CPU support
created: '2025-10-27'
hardware_targets:
- Blackhole
- Blackhole P150a
- Blackhole P150b
- Blackhole P300c
- TT-LoudBox
- TT-QuietBox
inbound_links: 2
needs_summary_revision: false
scorecard:
  bridge_score: 0.7
  claim_density: 0.8
  hub_potential: 0.8
  novelty_delta: 0.9
  self_containedness: 0.85
sources:
- https://speakerdeck.com/tenstorrent_japan/blackhole-architecture
tags:
- Tenstorrent
- Blackhole
- AI accelerator
- RISC-V
- Tensix
- Ethernet
toolchains: []
type: hardware_target
updated: '2026-06-29'
---

# Blackhole Architecture

Blackhole is a standalone AI computer architecture developed by Tenstorrent, fabricated on a 6nm process and offered as a PCIe Gen 5 accelerator. It integrates 700 Tensix compute cores, each containing a baby RISC-V processor and a floating-point unit that uses approximately 85% of core power, alongside 16 SiFive x280 big RISC-V cores that run Linux for on-device host capabilities. The chip features 210 MB of SRAM distributed across Tensix cores, an additional 32 MB SRAM for the x280 cores, and 32 GB of GDDR6 DRAM providing 512 GB/s of bandwidth. A 2D Torus network-on-chip (NoC) with two NoC interfaces per core and 64-byte per clock throughput connects all cores, while 12 ports of 400 Gb Ethernet enable scale-out connectivity. Blackhole products include the P150 family (active-cooled P150a and passive-cooled P150b, 300W TBP, 774 TOPS FP8) and the P300c liquid-cooled dual-chip variant (600W TBP), as well as integrated systems such as the TT-LoudBox (8x P150b) and TT-QuietBox (2x P300c) which pair with AMD EPYC CPUs for server and desktop deployments.

## Key Claims

- Peak compute: 745 TFLOPS (8-bit), 372 TFLOPS (16-bit); planned/projected performance.
- On-chip SRAM: 210 MB (Tensix cores) and 32 MB (SiFive x280 cores).
- DRAM: 32 GB GDDR6 with 512 GB/s bandwidth.
- Ethernet: 12x 400 Gb ports for 1 TB/s total scale-out bandwidth.
- NoC: 2 NoC interfaces per core, 2D Torus topology, 64 bytes per clock.
- PCIe: Gen 5.0 x16, 128 GB/s.
- Processor cores: 700 baby RISC-V cores (Tensix) + 52 controller cores + 16 SiFive x280 big RISC-V cores (4 clusters of 4, 64-bit dual-issue in-order, 2 MB L3/core, 128 KB L2/core).
- Baby RISC-V cores: 32-bit, INT multiplier/divider, FP32/BFLOAT16, 128-bit vector, 4 KB I-Cache, 8 KB D-Scratch.
- Products: P150a (active, 300W, 774 TOPS FP8, 194 TFLOPS FP16), P150b (passive, 300W, same compute), P300c (liquid-cooled, 600W, dual chip).
- Galaxy server: 32 chips in 4x8 mesh, 11.2 TB/s aggregate I/O, supports 3D torus.
- TT-LoudBox: 8 x P150b, 2x AMD EPYC 9124P, 768 GB DDR5, 4 TB NVMe.
- TT-QuietBox: 2 x P300c (4 chips), AMD EPYC 8124P, 512 GB DDR5, 4 TB NVMe, operates on 100V.
- Silicon-proven with Tenstorrent Galaxy, Wormhole, and Blackhole.
- Supports multiple data formats: FP8/16/32, BFLOAT16, BLOCKFP2/4/8, INT8/32, TF32.
- General purpose SIMD engine (SFPU) with fast transcendental instructions (Gelu, exponential, softmax) and C++ compiler.

## Optimization-Relevant Details

- ISA/profile: RISC-V (big cores: 64-bit dual-issue in-order; baby cores: 32-bit integer/floating-point with 128-bit vector).
- Vector/matrix/accelerator support: Tensix cores with MMUL (4096 ops/cycle), SIMD (64 ops/cycle), SFPU.
- Memory/cache/TLB/DMA: GDDR6 DRAM (512 GB/s), SRAM (210+32 MB), L1 I/D cache per type (e.g., baby: 4 KB I-Cache, 8 KB D-Scratch; big: 32 KB L1 each, 128 KB L2, 2 MB L3).
- Compiler/toolchain support: TT-Metalium (implied), SFPU C++ compiler.

## Relationships

- [[Tenstorrent_Grayskull_MatMul_Efficiency]] – Another Tenstorrent accelerator architecture providing a comparison point for compute and efficiency.
- Insufficient context for additional cross-links: the wiki currently lacks entity pages for Wormhole, Galaxy, or the SiFive x280 core separately.

## Sources

- [Blackhole Architecture – Speaker Deck](https://speakerdeck.com/tenstorrent_japan/blackhole-architecture)

