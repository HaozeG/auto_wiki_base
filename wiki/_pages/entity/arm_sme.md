---
type: entity
tags: [arm, isa-extension, matrix-extension, ai-acceleration, armv9]
sources:
  - https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/scalable-matrix-extension-armv9-a-architecture
  - https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/arm-scalable-matrix-extension-introduction
  - https://newsroom.arm.com/blog/scalable-matrix-extension
  - https://arxiv.org/pdf/2512.21473
created: 2026-06-26
updated: 2026-06-26
cold_start: true
inbound_links: 0
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# ARM SME (Scalable Matrix Extension)

ARM Scalable Matrix Extension (SME) is an ISA extension introduced with Armv9-A that adds dedicated matrix tile storage and outer-product instructions to the ARM architecture. SME targets the dominant compute pattern in neural network inference and training — the general matrix multiply (GEMM) — by accumulating the outer product of two vectors directly into a 2D on-chip tile register, reducing memory bandwidth pressure relative to purely vector-based GEMM implementations. SME introduces three new architectural elements: a square 2D register called ZA, a Streaming SVE (SSVE) mode that reconfigures the SVE2 vector pipeline at a potentially different vector length, and a set of outer-product accumulation instructions (FMOPA, SMOPA, UMOPA, etc.) that fuse multiply-accumulate across rows and columns. The Streaming Vector Length (SVL) selectable by the hardware ranges from 128 to 2048 bits; for an SVL of S bits, the ZA storage is (S/8)×(S/8) bytes, yielding a matrix throughput that grows as SVL^2 — quadratic scaling relative to vector length, giving a strong incentive for wider silicon implementations.

## Key Claims

- ZA is a 2D square tile of (SVL/8) × (SVL/8) bytes; at SVL=256 bits (32 bytes), ZA is 32×32=1024 bytes; at SVL=512 bits, ZA is 64×64=4096 bytes — giving 4× the storage for 2× the SVL increase.
- Outer-product throughput scales as SVL^2: doubling SVL quadruples the number of multiply-accumulate operations per FMOPA instruction, making SME uniquely bandwidth-efficient compared to vector ISAs where throughput scales linearly with width.
- SME provides outer-product instructions across four numerical precisions: FP64/FP32 (FMOPA), signed integer 32-bit (SMOPA), unsigned integer 32-bit (UMOPA), and BF16-to-FP32 accumulation — the last being the primary format for ML inference.
- The ZA storage is subdivided into named tile slices (ZA0H/ZA0V through ZA7H/ZA7V at 8-bit element size), enabling independent load/store of individual tile rows or columns via the LDR/STR ZA instructions.
- Streaming SVE mode is a separate execution context from normal execution; on entering streaming mode (via SMSTART), the processor may switch to a different SVL, and the Z and P register file contents are zeroed.
- Apple's M4 (Armv9.4) and the ARM Cortex-X925 (Armv9.2-A) both implement SME; Apple's implementation is notable for supporting SME/SSVE while omitting full SVE2 in normal execution mode — Apple had previously implemented a proprietary AMX (Apple Matrix Extensions) coprocessor prior to SME adoption.
- Linux kernel support for SME (context save/restore of ZA, PSTATE.SM/PSTATE.ZA) landed in Linux 5.19.

## Relationships

- [[arm_sve2]] — SVE2 is the foundation of SME; Streaming SVE mode re-uses the SVE2 instruction encoding with ZA as an additional accumulator target.
- [[arm_sme2]] — SME2 (Armv9.2) extends SME with multi-vector operands, ZT0 lookup table storage, and widened outer-product variants.
- [[risc_v_matrix_extensions]] — RISC-V AME/IME proposals serve the same GEMM acceleration role as SME, using a similar tile-based accumulator strategy.
- [[gemmini]] — Gemmini's systolic array targets the same outer-product/GEMM kernel that SME's FMOPA instruction is designed for, but as a decoupled RoCC accelerator rather than an in-core ISA extension.

## Sources

- ARM Developer Blog Part 1: "Arm Scalable Matrix Extension (SME) Introduction" — https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/arm-scalable-matrix-extension-introduction
- ARM Newsroom: "Scalable Matrix Extension (SME) for Armv9 Architecture Enables AI Innovation on the Arm CPU" — https://newsroom.arm.com/blog/scalable-matrix-extension
- arxiv 2512.21473: "Demystifying ARM SME to Optimize General Matrix Multiplications" — concrete analysis of FMOPA throughput and ZA tile layout
- ARM Developer Blog: "Scalable Matrix Extension (SME) for the Armv9-A architecture" — https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/scalable-matrix-extension-armv9-a-architecture
- LWN.net: "arm64/sme: Initial support for the Scalable Matrix Extension" — Linux 5.19 kernel SME support — https://lwn.net/Articles/882580/
