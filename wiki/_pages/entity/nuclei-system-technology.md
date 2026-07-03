---
canonical_name: Nuclei System Technology
aliases:
- Nuclei
- Nuclei System Technology
subtype: null
tags: []
scorecard:
  novelty_delta: 0.6
  claim_density: 0.3
  self_containedness: 0.8
  bridge_score: 0.5
  hub_potential: 0.2
sources:
- raw/cache/d4a0c8ff3a653039.md
- https://www.eetimes.com/nuclei-the-worlds-first-risc-v-cpu-ip-vendor-to-accomplish-iso-26262-asil-d-product-certificate/
source_url: https://www.eetimes.com/nuclei-the-worlds-first-risc-v-cpu-ip-vendor-to-accomplish-iso-26262-asil-d-product-certificate/
fetched_at: '2026-07-03T18:27:07.799595+00:00'
type: entity
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 0
outbound_links:
- target: andes-ax45mpv-hardware-target
  reason: Both are commercial RISC-V CPU IP cores targeting different market segments;
    the NA900 is distinguished by its ASIL-D functional safety certification, whereas
    the AX45MPV focuses on high-performance vector computing with a superscalar pipeline
    and up to 1024-bit VPU, but lacks functional safety certification
---

# Nuclei System Technology

Nuclei System Technology is a Chinese RISC-V CPU IP vendor founded in 2018, specializing in high-performance and low-power processor cores and associated SoC platforms. The company's NA900 processor core, based on the RISC-V architecture with a dual-issue 9-stage in-order execution pipeline, achieved ISO 26262 ASIL-D product certification in August 2023, becoming the first RISC-V CPU IP to receive such certification for both systematic and random hardware faults. This certification, conducted in partnership with Exida, marks a significant milestone for open-standard processor architectures in automotive and safety-critical semiconductor design, demonstrating that RISC-V-based IP can meet the highest automotive safety integrity levels.

## Key Claims

- Founded in 2018, Nuclei System Technology is a leading RISC-V CPU IP vendor in China.
- The NA900 core is a high-performance processor featuring a dual-issue 9-stage in-order execution pipeline based on the RISC-V architecture.
- The NA900 is the first RISC-V CPU IP to obtain ISO 26262 ASIL-D product certification, covering both systematic and random hardware faults.
- Certification was awarded in August 2023 in collaboration with Exida, a recognized functional safety certification body.

## Relationships

- [[andes-ax45mpv-hardware-target]]: Both are commercial RISC-V CPU IP cores targeting different market segments; the NA900 is distinguished by its ASIL-D functional safety certification, whereas the AX45MPV focuses on high-performance vector computing with a superscalar pipeline and up to 1024-bit VPU, but lacks functional safety certification.

## Sources

- https://www.eetimes.com/nuclei-the-worlds-first-risc-v-cpu-ip-vendor-to-accomplish-iso-26262-asil-d-product-certificate/
- https://nucleisys.com (NA900 Product Brief)
