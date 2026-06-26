---
type: entity
tags: [arm, isa-extension, matrix-extension, ai-acceleration, armv9, sme2]
sources:
  - https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/part4-arm-sme2-introduction
  - https://developer.arm.com/documentation/109246/0101/SME-Overview/SME2-multi-vector-operands
  - https://developer.arm.com/documentation/109246/0101/SME-Overview/SME-and-SME2/SME2-lookup-table
  - https://learn.arm.com/learning-paths/cross-platform/multiplying-matrices-with-sme2/overview/
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

# ARM SME2 (Scalable Matrix Extension 2)

ARM SME2 is the second generation of ARM's Scalable Matrix Extension, introduced with Armv9.2-A. SME2 extends the original SME specification with two major capabilities: multi-vector instructions that can operate on groups of 2 or 4 SVE Z registers simultaneously, and a new 512-bit architectural register ZT0 that provides a 16-entry lookup table for efficient quantized inference. Where SME's outer-product instructions work with single vector operands, SME2 allows a single instruction to consume or produce two or four consecutive (or stride-spaced) Z registers in a single operation, multiplying the effective data throughput for algorithms that keep multiple partial results in flight simultaneously. The lookup table facility accelerates activation function evaluation and dequantization — common bottlenecks in low-precision neural network inference — by enabling packed 8-bit or 16-bit index lookups into 32-bit table entries, with LUTI2 (2-bit indices, 4-entry access) and LUTI4 (4-bit indices, full 16-entry access) instructions. ARM Cortex-X925 and AWS Graviton5 (Neoverse V3, Armv9.2-A) are among the first widely available implementations. Apple's M4 chip, implementing Armv9.4, also supports SME2.

## Key Claims

- ZT0 is a 512-bit (64-byte) register organised as a 16-entry table with 32-bit entries; each entry can hold an 8-bit, 16-bit, or 32-bit value, enabling lookup-based dequantization for INT8/INT4 inference.
- LUTI2 instructions use 2-bit indices from a source Z register to perform table lookups into ZT0, accessing up to 4 table entries per lookup; LUTI4 instructions use 4-bit indices to access all 16 entries, with results written to 1 or 2 destination Z registers.
- Multi-vector operands in SME2 support groups of 1, 2, or 4 SVE Z registers, specified as either consecutive registers (Z0–Z3) or strided registers (Z0, Z4, Z8, Z12), providing 2× or 4× the per-instruction data throughput of SME.
- AWS Graviton5 (Neoverse V3) implements Armv9.2-A with SME2, 192 cores per socket, 3.3 GHz clock, and TSMC 3 nm manufacturing — the first broadly available cloud server with SME2.
- ARM Cortex-X925 (Armv9.2-A) implements both SVE2 and SME2, serving as the high-performance application core in Qualcomm Snapdragon and MediaTek platforms targeting on-device AI inference.
- SME2 adds widened outer-product instructions (e.g., FMOPA variants accumulating from BF16 pairs into FP32) that further reduce the round-trips between ZA and Z registers for transformer attention kernels.
- ZT0 state is managed independently from ZA; SMSTART/SMSTOP control Streaming SVE mode, while SMSTART ZA / SMSTOP ZA specifically enable or disable ZA and ZT0 state.

## Relationships

- [[arm_sme]] — SME2 is a strict superset of SME; all SME instructions remain valid in Armv9.2-A, with ZT0 and multi-vector instructions added.
- [[arm_sve2]] — SME2 multi-vector instructions operate on SVE2 Z registers and are only available in Streaming SVE mode.
- [[risc_v_matrix_extensions]] — RISC-V AME matrix tile proposals target the same outer-product GEMM pattern as SME2, with analogous tile storage and multi-vector accumulation concepts.

## Sources

- ARM Developer Blog Part 4: "Arm SME2 Introduction" — https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/part4-arm-sme2-introduction
- ARM Documentation: "SME2 multi-vector operands" — https://developer.arm.com/documentation/109246/0101/SME-Overview/SME2-multi-vector-operands
- ARM Documentation: "SME2 lookup table" — https://developer.arm.com/documentation/109246/0101/SME-Overview/SME-and-SME2/SME2-lookup-table
- ARM Learning Path: "Accelerate Matrix Multiplication Performance with SME2" — https://learn.arm.com/learning-paths/cross-platform/multiplying-matrices-with-sme2/overview/
- Wikipedia: AWS Graviton — Graviton5 = Neoverse V3 = Armv9.2-A
