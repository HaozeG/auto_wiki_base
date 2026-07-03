---
canonical_name: SiFive Intelligence 2nd Gen
aliases:
- SiFive X160 Gen 2
- SiFive X180 Gen 2
- SiFive X280 Gen 2
- SiFive X390 Gen 2
- SiFive XM Gen 2
- SiFive 2nd Gen Intelligence
subtype: null
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.6
  self_containedness: 0.8
  bridge_score: 0.2
  hub_potential: 0.3
sources:
- raw/cache/caa128f87dc6a453.md
- https://www.cnx-software.com/2025/09/08/sifive-introduces-2nd-gen-intelligence-risc-v-ai-cpus-x160-x180-x280-gen-2-x390-gen-2-and-xm-gen-2/
source_url: https://www.cnx-software.com/2025/09/08/sifive-introduces-2nd-gen-intelligence-risc-v-ai-cpus-x160-x180-x280-gen-2-x390-gen-2-and-xm-gen-2/
fetched_at: '2026-07-03T14:55:58.986723+00:00'
type: entity
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 0
---

# SiFive Intelligence 2nd Gen

SiFive Intelligence 2nd Gen is a family of RISC-V processor cores designed for AI workloads, announced by SiFive in September 2025. The family includes five products: the new X160 Gen 2 (32-bit) and X180 Gen 2 (64-bit) entry-level AIoT cores, and upgraded versions of the X280 Gen 2, X390 Gen 2, and XM Gen 2 processors. All cores feature scalar, vector, and (for the XM series) matrix processing capabilities. The X160 and X180 Gen 2 cores implement a dual-issue, in-order 8-stage superscalar pipeline with the RISC-V Vector Extension v1.0 (RVV 1.0), 128-bit vector registers, and a 64-bit datapath. They support Int8 and BFloat16 data types, and can perform integer operations at 2× 32-bit, 4× 16-bit, or 8× 8-bit per cycle, and floating-point operations at 2× single-precision or 4× half-precision per cycle. The cores include the SiFive Custom Instruction Extension (SCIE), SiFive Scalar Coprocessor Interface (SSCI), and Vector Coprocessor Interface eXtension (VCIX) for direct accelerator integration. The memory port provides full-duplex load/store bandwidth of 8 bytes read plus 8 bytes write. Up to 16 Physical Memory Protection (PMP) regions are supported, with optional SiFive WorldGuard security offering up to four security worlds. The X160 Gen 2 is optimized for power efficiency and severely area-constrained applications, while the X180 Gen 2 delivers higher performance and better integration with larger memory systems. The upgraded X280 Gen 2, X390 Gen 2, and XM Gen 2 add support for the RVA23 profile, additional vector datatypes (FP4 and FP8), wider cache options, and updated port interfaces. All five cores are available for licensing immediately, with the first silicon expected in Q2 2026.

## Key Claims

- X160 Gen 2 is a 32-bit RISC-V core (RV32I), while X180 Gen 2 is a 64-bit core (RV64I).
- Both X160 and X180 Gen 2 have a dual-issue, in-order 8-stage superscalar pipeline.
- Vector processing includes 128-bit vector registers (VLEN), a 64-bit datapath (DLEN), and full RISC-V Vector Extension v1.0 (RVV 1.0) support.
- Int8 and BFloat16 vector datatypes are supported; integer throughput: 2× 32-bit, 4× 16-bit, or 8× 8-bit per cycle; floating-point throughput: 2× single-precision or 4× half-precision per cycle.
- Single-core and multi-core configurations are available up to quad-cores.
- Custom accelerator integration is enabled via SiFive Custom Instruction Extension (SCIE), SiFive Scalar Coprocessor Interface (SSCI), and Vector Coprocessor Interface eXtension (VCIX).
- The memory port provides full-duplex bandwidth of 8B read and 8B write per cycle.
- Up to 16 Physical Memory Protection (PMP) regions and optional SiFive WorldGuard security up to four worlds.
- X160 Gen 2 is optimized for power efficiency and area-constrained use cases; X180 Gen 2 targets higher performance with larger memory systems.
- Upgraded X280 Gen 2, X390 Gen 2, and XM Gen 2 support the RVA23 profile, FP4 and FP8 datatypes, wider cache options, and port changes.
- First silicon is expected in Q2 2026.

## Relationships

No specific relationship to visible context pages in this wiki. The SiFive Intelligence 2nd Gen family represents a new vendor core family not yet covered; existing pages focus on T-Head cores such as the XuanTie C906 used in the Milk-V Duo board in the [[baby-llama2-milkv-duo-benchmark]] page.

## Sources

- https://www.cnx-software.com/2025/09/08/sifive-introduces-2nd-gen-intelligence-risc-v-ai-cpus-x160-x180-x280-gen-2-x390-gen-2-and-xm-gen-2/
