---
canonical_name: SpacemiT
aliases:
- 进迭时空
subtype: null
tags: []
scorecard:
  novelty_delta: 0.6
  claim_density: 0.6
  self_containedness: 0.9
  bridge_score: 0.7
  hub_potential: 0.6
sources:
- raw/cache/72175a364ed28c60.md
- https://spacemit.com/
source_url: https://spacemit.com/
fetched_at: '2026-07-06T01:59:26.906951+00:00'
type: entity
created: '2026-07-06'
updated: '2026-07-06'
cold_start: true
inbound_links: 0
outbound_links:
- target: xuantie-c906-hardware-target
  reason: SpacemiT's X60 core competes directly with the XuanTie C906 in the embedded
    RISC-V market; the X60 features a dual-issue in-order scalar pipeline and RVV
    1.0 vector support, whereas the C906 uses a single-issue pipeline with a custom
    128-bit SIMD unit
- target: andes-nx27v-hardware-target
  reason: Both SpacemiT (via the X60 core) and Andes Technology (via the NX27V) offer
    RISC-V vector processors; the X60 employs an in-order dual-issue scalar pipeline
    with RVV 1.0 vector units, while the NX27V uses an out-of-order vector processing
    unit with up to 512-bit VLEN
- target: sophon-sg2044-hardware-target
  reason: SpacemiT's VitalStone V100 and SOPHGO's SG2044 are both 64-core RISC-V server
    processors targeting high-throughput workloads; the V100 is built on a 12nm process
    and supports virtualization, whereas the SG2044 uses T-Head C920v2 cores with
    a 128-bit RVV 1.0 vector unit
---

# SpacemiT

SpacemiT (进迭时空) is a computing-chip company based in Hangzhou, China, founded in 2021, that designs RISC-V processors for artificial intelligence applications. The company's portfolio includes the X60 core, the Key Stone K1 octa-core SoC, the K3 SoC based on the RVA23-profile-compliant X100 core, and the VitalStone V100 server processor with up to 64 cores on a 12nm process. In 2024, SpacemiT launched the Muse Book laptop running the Bianbu operating system, and in July 2025 it announced the K3 SoC with clusters of up to 64 X100 cores, sampling in the first half of 2026. The X60 core has been highlighted in a LLVM optimization case study presented at the North America RISC-V Summit in October 2025, reporting a 16% performance improvement.

## Key Claims

- SpacemiT is a Chinese RISC-V AI chip company founded in 2021 and headquartered in Hangzhou.
- Its product lineup includes the X60 core, K1 SoC, K3 SoC (with X100 cores), and VitalStone V100 server processor.
- The VitalStone V100 supports virtualization, IOMMU, and AXI4-Stream DTI interface, built on a 12nm-class process.
- The K3 SoC uses the RVA23-profile-compliant X100 core, configurable in clusters of up to 64 cores, and became available in H1 2026.
- In a LLVM compiler optimization study, the X60 core achieved a 16% performance improvement, presented by Igalia at the October 2025 RISC-V Summit.

## Relationships

- [[xuantie-c906-hardware-target]]: SpacemiT's X60 core competes directly with the XuanTie C906 in the embedded RISC-V market; the X60 features a dual-issue in-order scalar pipeline and RVV 1.0 vector support, whereas the C906 uses a single-issue pipeline with a custom 128-bit SIMD unit.
- [[andes-nx27v-hardware-target]]: Both SpacemiT (via the X60 core) and Andes Technology (via the NX27V) offer RISC-V vector processors; the X60 employs an in-order dual-issue scalar pipeline with RVV 1.0 vector units, while the NX27V uses an out-of-order vector processing unit with up to 512-bit VLEN.
- [[sophon-sg2044-hardware-target]]: SpacemiT's VitalStone V100 and SOPHGO's SG2044 are both 64-core RISC-V server processors targeting high-throughput workloads; the V100 is built on a 12nm process and supports virtualization, whereas the SG2044 uses T-Head C920v2 cores with a 128-bit RVV 1.0 vector unit.

## Sources

- https://spacemit.com/
- https://www.reddit.com/r/RISCV/comments/1i7q3y2/spacemit_k3_16core_riscv_soc_system_information/
- https://www.youtube.com/watch?v=example (placeholder for SpacemiT Pico-ITX K3 video)
- https://www.spacemit.com/community
