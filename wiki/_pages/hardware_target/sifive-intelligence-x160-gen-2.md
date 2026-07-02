---
canonical_name: SiFive Intelligence X160 Gen 2
aliases:
- SiFive X160 Gen 2
- X160 Gen 2
subtype: null
tags: []
hardware_targets:
- SiFive Intelligence X160 Gen 2
toolchains: []
constraints:
- 32-bit RISC-V ISA (RV32I)
- In-order 8-stage superscalar
- Single and multi-core up to quad-cores
- 128-bit vector registers (vlen)
- 64-bit datapath (dlen)
- Int8 and BFloat16 support
- RVV1.0
- SCIE, SSCI, VCIX interfaces
- Memory port: 8B read + 8B write
- Up to 16 PMP regions
- Optional WorldGuard security with up to 4 worlds
scorecard:
  novelty_delta: 0.8
  claim_density: 0.7
  self_containedness: 0.9
  bridge_score: 0.3
  hub_potential: 0.6
sources:
- raw/cache/ec1a2fd17edc46d7.md
- https://www.cnx-software.com/2025/09/08/sifive-introduces-2nd-gen-intelligence-risc-v-ai-cpus-x160-x180-x280-gen-2-x390-gen-2-and-xm-gen-2/
source_url: https://www.cnx-software.com/2025/09/08/sifive-introduces-2nd-gen-intelligence-risc-v-ai-cpus-x160-x180-x280-gen-2-x390-gen-2-and-xm-gen-2/
fetched_at: '2026-07-02T09:44:10.311162+00:00'
type: hardware_target
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 9
---

# SiFive Intelligence X160 Gen 2

The SiFive Intelligence X160 Gen 2 is a 32-bit RISC-V CPU core from SiFive's 2nd Generation Intelligence family, designed for AIoT and edge computing workloads. It features a dual-issue, in-order 8-stage superscalar pipeline with support for the RISC-V Vector Extension v1.0 (RVV1.0) using 128-bit wide vector registers and a 64-bit datapath. The core supports Int8 and BFloat16 datatypes, integer operations at 2x 32-bit/4x 16-bit/8x 8-bit per cycle, and floating-point operations at 2x single precision and 4x half precision per cycle. It includes interfaces for custom instructions (SCIE), scalar coprocessor (SSCI), and vector coprocessor (VCIX). The core is optimized for power efficiency and area-constrained applications, with single and multi-core configurations up to quad-cores.

## Key Claims

- Dual-issue in-order 8-stage superscalar pipeline.
- 32-bit RISC-V ISA (RV32I).
- Vector processing with 128-bit vlen, 64-bit dlen.
- Int8 and BFloat16 support.
- Integer: 2x 32-bit, 4x 16-bit, 8x 8-bit per cycle.
- Floating point: 2x single precision, 4x half precision per cycle.
- RISC-V Vector Extension v1.0.
- Single and multi-core configurations up to quad-cores.
- SiFive Custom Instruction Extension (SCIE).
- SiFive Scalar Coprocessor Interface (SSCI) for driving accelerators via custom instructions.
- Vector Coprocessor Interface eXtension (VCIX) for vector instruction mapped acceleration.
- Full duplex load/store bandwidth: 8B read + 8B write.
- Up to 16 Physical Memory Protection (PMP) regions.
- Optional SiFive WorldGuard security, up to 4 worlds.
- Optimized for power efficiency and area-constrained applications.

## Optimization-Relevant Details

- ISA/profile: RISC-V RV32I with RVV1.0.
- Vector/matrix/accelerator support: 128-bit VLEN, 64-bit DLEN; vector ALU with SCIE, SSCI, VCIX interfaces.
- Memory/cache/TLB/DMA: Not specified in source beyond memory port.
- Compiler/toolchain support: Not specified (expected RISC-V GCC/LLVM with vector extension support).

## Relationships

- [[sifive-intelligence-x180-gen-2]]: The 64-bit counterpart in the same 2nd Generation Intelligence family.
- [[cpa-factored-gemmini-systolic-array]]: A related RISC-V AI accelerator optimization, though targeting a different hardware platform.

## Sources

- [CNX Software article on SiFive 2nd Gen Intelligence CPUs](https://www.cnx-software.com/2025/09/08/sifive-introduces-2nd-gen-intelligence-risc-v-ai-cpus-x160-x180-x280-gen-2-x390-gen-2-and-xm-gen-2/)
