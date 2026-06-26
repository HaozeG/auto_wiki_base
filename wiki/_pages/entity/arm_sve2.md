---
type: entity
tags: [arm, isa-extension, vector-processing, ai-acceleration, armv9]
sources:
  - https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/sve2
  - https://developer.arm.com/Architectures/Scalable%20Vector%20Extensions
  - https://arxiv.org/pdf/2505.09462
  - https://chipsandcheese.com/p/arms-neoverse-v2-in-awss-graviton-4
created: 2026-06-26
updated: 2026-06-26
cold_start: false
inbound_links: 0
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# ARM SVE2 (Scalable Vector Extension 2)

ARM Scalable Vector Extension 2 (SVE2) is a vector ISA extension introduced with Armv9-A that generalises the original SVE (introduced for HPC in Armv8) to a broader set of domains including multimedia, computer vision, wireless baseband, and general-purpose software. SVE2 is mandatory for all Armv9-A cores. Its defining characteristic is a vector-length-agnostic (VLA) programming model: vector registers are architecturally variable in width from 128 bits to 2048 bits in 128-bit increments, with the hardware implementation choosing a fixed width. Software compiled once runs correctly on any compliant implementation without recompilation, scaling throughput automatically with the hardware vector width. SVE2 provides 32 scalable vector Z registers and 16 scalable predicate P registers; predicates allow per-element masking without branch divergence. New instruction classes added over SVE include complex number arithmetic, polynomial multiplication over GF(2^n), bit-permutation instructions, and widening/narrowing integer operations — capabilities targeted at multimedia codecs and 5G signal processing workloads.

## Key Claims

- SVE2 vector registers range from 128 to 2048 bits wide (in 128-bit increments), with the width fixed at silicon design time; the Fujitsu A64FX implements 512-bit vectors, the AWS Graviton3 (Neoverse V1) implements 256-bit vectors, and the AWS Graviton4 (Neoverse V2) implements 128-bit vectors.
- SVE2 is mandatory for all Armv9-A processor implementations, making it the baseline SIMD capability for the entire Armv9 product family including Cortex-X, Cortex-A, and Neoverse server cores.
- SVE2 adds polynomial multiplication (PMULLB/PMULLT) over GF(2^128), enabling efficient AES-GCM and CRC hardware acceleration without dedicated crypto instructions.
- The VLA model means the same binary scales from a 128-bit embedded Cortex-A core to a 512-bit HPC processor; no ISA fragmentation or separate library builds are required.
- SVE2 includes complex-number dot product instructions (CDOT) targeting wireless signal processing (LTE/5G baseband) where IQ arithmetic is central.
- AWS Graviton5 (Neoverse V3, Armv9.2-A) implements SVE2 with 192 cores per socket and runs at 3.3 GHz on TSMC 3 nm.

## Relationships

- [[arm_sme]] — SME builds on SVE2; the Streaming SVE mode within SME is a reconfigured SVE2 execution context used for matrix operations.
- [[arm_sme2]] — SME2 (Armv9.2) extends both SME and SVE2 with multi-vector and lookup table instructions.
- [[risc_v_vector_extension]] — RISC-V RVV 1.0 shares the same VLA design philosophy as SVE/SVE2 but is an independent specification with different register file and encoding conventions.
- [[rva23_profile]] — RVA23 mandates RISC-V RVV 1.0, the closest analogue on the RISC-V side to SVE2.
- [[sifive_intelligence_x280]] — SiFive X280 implements RVV 1.0 with 512-bit vectors, a direct competitor implementation to SVE2 cores such as Neoverse V1.

## Sources

- ARM Developer Blog: "Evolution of SIMD architecture with SVE2" — https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/sve2
- ARM Architecture Reference: https://developer.arm.com/Architectures/Scalable%20Vector%20Extensions
- arxiv 2505.09462: "ARM SVE Unleashed: Performance and Insights Across HPC Applications on Nvidia Grace" — benchmarks on Neoverse V2 (128-bit SVE2 vectors)
- Chips and Cheese: "Arm's Neoverse V2, in AWS's Graviton 4" — confirms 128-bit SVE2 vector width
- AWS Graviton Wikipedia / About Amazon: Graviton4 = Neoverse V2 = Armv9.0-A; Graviton5 = Neoverse V3 = Armv9.2-A
