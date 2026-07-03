---
canonical_name: Nuclei NA900
aliases:
- NA900
- Nuclei NA900 processor
subtype: null
tags: []
hardware_targets:
- Nuclei NA900
toolchains: []
constraints:
- 9-stage dual-issue pipeline
- RISC-V RV32IMACFDPB ISA
- ISO 26262 ASIL-D certified
- Configurable SEooC design
- Hardware safety integrity and systematic capability at ASIL D
scorecard:
  novelty_delta: 0.9
  claim_density: 0.7
  self_containedness: 0.9
  bridge_score: 0.5
  hub_potential: 0.2
sources:
- raw/cache/44097d9c2d87c792.md
- https://www.design-reuse-embedded.com/news/202308139/nuclei-the-world-s-first-risc-v-cpu-ip-vendor-accomplishes-iso-26262-asil-d-product-certificate/
source_url: https://www.design-reuse-embedded.com/news/202308139/nuclei-the-world-s-first-risc-v-cpu-ip-vendor-accomplishes-iso-26262-asil-d-product-certificate/
fetched_at: '2026-07-03T18:28:28.933914+00:00'
type: hardware_target
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 0
outbound_links:
- target: andes-ax45mpv-hardware-target
  reason: Both are commercial RISC-V CPU IP cores from different vendors (Nuclei and
    Andes Technology). The NA900 focuses on automotive functional safety with ISO
    26262 ASIL-D certification, while the AX45MPV targets data-intensive workloads
    with a vector processing unit and multicore support. Both implement RISC-V standard
    extensions but target different application domains
---

# Nuclei NA900

Nuclei NA900 is a configurable 32-bit RISC-V CPU IP core developed by Nuclei System Technology, a Chinese RISC-V CPU IP vendor. It features a 9-stage dual-issue pipeline and supports the RISC-V RV32IMACFDPB ISA, covering integer, multiply, atomic, compression, single/double-precision floating-point, and packed SIMD extensions. The NA900 achieved the world's first ISO 26262 ASIL-D product certificate for a RISC-V CPU IP, certified for both systematic fault and hardware random fault capabilities. It was developed as a hardware SEooC (Safety Element out of Context) according to ISO 26262-10, meeting ASIL D design, implementation, verification, and functional safety management requirements. The core targets automotive applications requiring the highest functional safety integrity level.

## Key Claims

- World's first RISC-V CPU IP vendor to achieve ISO 26262 ASIL-D product certificate.
- NA900 is ASIL-D certified for both systematic capability and hardware safety integrity.
- 9-stage, dual-issue pipeline.
- Supports RV32IMACFDPB ISA.
- Related core NA300D (3-stage, single-issue, RV32IMACFDPB/Zc) obtained ASIL D Ready certificate for hardware safety integrity.
- NA300D assessed according to ISO 26262-5:2018, meeting SPFM and LFM with ASIL D target values.

## Optimization-Relevant Details

- ISA/profile: RV32IMACFDPB
- Vector/matrix/accelerator support: Not documented in source.
- Memory/cache/TLB/DMA: Not documented.
- Compiler/toolchain support: Not documented.

## Relationships

- [[andes-ax45mpv-hardware-target]]: Both are commercial RISC-V CPU IP cores from different vendors (Nuclei and Andes Technology). The NA900 focuses on automotive functional safety with ISO 26262 ASIL-D certification, while the AX45MPV targets data-intensive workloads with a vector processing unit and multicore support. Both implement RISC-V standard extensions but target different application domains.

## Sources

- https://www.design-reuse-embedded.com/news/202308139/nuclei-the-world-s-first-risc-v-cpu-ip-vendor-accomplishes-iso-26262-asil-d-product-certificate/
