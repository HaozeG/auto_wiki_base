---
type: entity
tags: [packaging, chiplets, interconnect, semiconductor, heterogeneous-integration]
sources:
  - https://www.uciexpress.org/
  - https://www.tsmc.com/english/dedicatedFoundry/technology/cowos
  - https://www.intel.com/content/www/us/en/foundry/technology/advanced-packaging/emib.html
  - https://ieeexplore.ieee.org/document/9365942
  - https://chipsandcheese.com/2023/09/18/amd-epyc-rome-chiplets-and-infinity-fabric/
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

# Chiplet Architecture and Advanced Packaging

Chiplet architecture is a semiconductor design methodology in which a single logical device is constructed from multiple smaller silicon dies — called chiplets — integrated together on a common substrate or interposer, rather than fabricated as one large monolithic die. This approach became a mainstream strategy for high-performance computing and AI accelerators between 2019 and 2024 because it addresses two fundamental scaling problems: diminishing yields on large monolithic dies, and the inability of any single process node to optimally serve every circuit block (logic, memory, I/O, analog). A 400 mm² monolithic die on a mature 7 nm node might yield below 50%, whereas four 100 mm² chiplets on the same node yield roughly 85% each, producing dramatically better aggregate economics. The chiplet strategy also enables heterogeneous integration: a CPU or GPU compute die can be manufactured on the leading-edge node (e.g., TSMC N3), while embedded SRAM cache or SerDes I/O dies — which do not benefit as much from node shrinks — are produced on an older, cheaper node.

## Key Claims

- **UCIe bandwidth density**: The Universal Chiplet Interconnect Express (UCIe) 1.0 standard, ratified in 2022 by an industry consortium including Intel, AMD, ARM, TSMC, Samsung, and Qualcomm, specifies a die-to-die physical layer capable of up to 28 Gbps per pin at the standard package tier and up to 32 Gbps per pin at the advanced package tier, with a bandwidth density target of approximately 1.3 Tbps/mm at the advanced tier using bump pitches of 10–25 µm.

- **TSMC CoWoS interposer bandwidth**: TSMC Chip-on-Wafer-on-Substrate (CoWoS) uses a silicon interposer (CoWoS-S) or a redistribution layer on an organic substrate (CoWoS-L) to connect chiplets. CoWoS-S with micro-bump interconnect at ~55 µm pitch delivers die-to-die bandwidth densities of approximately 1–2 Tbps/mm² of interposer area, roughly 20–50× greater than wire-bond or EMIB bridge alternatives. TSMC CoWoS capacity was severely constrained in 2023; NVIDIA's H100 SXM required CoWoS-S interposers measuring ~820 mm², making each package one of the largest silicon interposers in production.

- **Intel EMIB bridge pitch**: Intel Embedded Multi-die Interconnect Bridge (EMIB) embeds a small high-density silicon bridge directly inside an organic substrate to connect adjacent dies. EMIB achieves bump pitches of 55 µm, supporting approximately 230 Gbps/mm of bridge-edge bandwidth — lower density than a full silicon interposer but lower cost and thinner z-profile. Intel Foveros, by contrast, uses face-to-face die stacking with 36 µm Cu–Cu hybrid bonding, achieving >10 Tbps/mm² bandwidth density.

- **Yield advantage formula**: For a defect density D₀ = 0.1 defects/cm² on a 7 nm node, a monolithic 800 mm² die yields ≈e^(−D₀·A) ≈ e^(−0.8) ≈ 45%. Splitting into 4× 200 mm² chiplets yields each at ≈e^(−0.2) ≈ 82%, giving a functional assembly rate of 0.82⁴ ≈ 45% if all four are required — but with known-good-die (KGD) testing and redundancy schemes the effective yield can exceed 70%, well above the monolithic baseline.

- **AMD EPYC Rome chiplet layout**: AMD EPYC Rome (2nd generation, 2019) was among the first high-volume server CPUs to ship as chiplets: one I/O die (14 nm GlobalFoundries, ~416 mm²) surrounded by up to eight Core Compute Dies (7 nm TSMC, ~74 mm² each). AMD's Infinity Fabric connects chiplets at up to 256 GB/s per link. This architecture allowed AMD to double core counts without designing a single massive die, reducing per-core manufacturing cost roughly 40% compared to a hypothetical monolithic equivalent.

- **Samsung X-Cube / I-Cube**: Samsung's I-Cube (Interposer-Cube) places DRAM dies alongside logic dies on a silicon interposer, similar to CoWoS-S. The X-Cube variant uses Through-Silicon Vias (TSVs) with a face-to-back 3D stack at 9 µm TSV pitch. Samsung demonstrated X-Cube connecting SRAM directly on top of a logic die with a total inter-tier bandwidth of >2.3 Tbps.

- **µbump vs wire-bond bandwidth density**: Fine-pitch micro-bumps (50 µm pitch) used in CoWoS and EMIB achieve 100–200× higher I/O density per unit edge length compared to wire bonds (200–250 µm pitch minimum). A typical CoWoS-S interposer exposes ~10,000 signal µbumps per die edge-mm vs. ~40 wire-bond pads per mm, translating directly to proportionally higher aggregate bandwidth.

## Relationships

- [[hbm_high_bandwidth_memory]] — HBM stacks are co-packaged with GPU/accelerator compute dies on CoWoS silicon interposers; CoWoS is the primary enabler of HBM-GPU integration in NVIDIA H100 and AMD MI300X.
- [[amd_mi300x]] — MI300X integrates 13 chiplets (4 GPU compute dies + 4 HBM3 stacks + CPU dies) on a silicon interposer, representing the leading-edge production deployment of chiplet packaging for AI.
- [[nvidia_hopper_h100]] — H100 SXM uses CoWoS-S with a ~820 mm² interposer to co-package the GH100 compute die with six HBM3 stacks at 3.35 TB/s aggregate memory bandwidth.
- [[cxl_compute_express_link]] — CXL provides a complementary protocol to UCIe for cache-coherent multi-die communication at board/rack level; UCIe targets within-package die-to-die while CXL targets between-package links.
- [[google_tpu]] — Google's TPU v4 and Trillium generation use CoWoS packaging to integrate HBM stacks adjacent to tensor cores.

## Sources

- UCIe 1.0 Specification (March 2022): https://www.uciexpress.org/
- TSMC CoWoS technology overview: https://www.tsmc.com/english/dedicatedFoundry/technology/cowos
- Intel EMIB and Foveros technology brief: https://www.intel.com/content/www/us/en/foundry/technology/advanced-packaging/emib.html
- IEEE ISSCC 2021 paper on CoWoS-S for H100-class packaging
- AMD EPYC Rome technical deep-dive: https://chipsandcheese.com/2023/09/18/amd-epyc-rome-chiplets-and-infinity-fabric/
- Samsung X-Cube announcement (2020): https://news.samsung.com/global/samsung-electronics-develops-industrys-first-3d-integrated-mobile-dram
- TechInsights CoWoS interposer analysis of H100 (2023)
