---
canonical_name: Alphawave Semi
aliases:
- Alphawave Semi
- 'LSE: AWE'
subtype: null
tags: []
scorecard:
  novelty_delta: 0.7
  claim_density: 0.8
  self_containedness: 0.9
  bridge_score: 0.5
  hub_potential: 0.6
sources:
- raw/cache/06107835f0be2880.md
- https://awavesemi.com/press-release/alphawave-semi-spearheads-chiplet-based-custom-silicon-for-generative-ai-and-data-center-workloads-with-successful-3nm-tapeouts-of-hbm3-and-ucie-ip/
source_url: https://awavesemi.com/press-release/alphawave-semi-spearheads-chiplet-based-custom-silicon-for-generative-ai-and-data-center-workloads-with-successful-3nm-tapeouts-of-hbm3-and-ucie-ip/
fetched_at: '2026-07-17T12:36:19.777056+00:00'
type: entity
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 0
outbound_links:
- target: alphawave_semi_hbm_subsystem
  reason: Alphawave Semi's HBM3 PHY IP described in this press release is a component
    of the company's HBM subsystem product line, which integrates a JEDEC-compliant
    HBM controller and PHY supporting HBM3, HBM2E, and HBM2
- target: meta_vistara_cxl_bridge
  reason: Alphawave Semi's IP portfolio includes CXL controller support for its UCIe
    PHY, the same Compute Express Link protocol used by Meta's Vistara CXL bridge
    chip to enable DDR4 memory tiering in DDR5 servers
- target: nvidia_blackwell_ultra
  reason: Both Alphawave Semi's HBM3 IP and NVIDIA Blackwell Ultra's HBM3E memory
    subsystem target high-bandwidth memory for AI workloads, with Alphawave providing
    the interface IP that can be deployed in custom silicon similar to Blackwell Ultra's
    use of HBM3E
---

# Alphawave Semi

Alphawave Semi is a global semiconductor company headquartered in London, United Kingdom and Toronto, Canada, specializing in high-speed connectivity IP for data center, AI, and high-performance computing applications. The company provides a comprehensive portfolio of custom silicon and chiplet-enabled platforms built on advanced process nodes such as TSMC 3nm. In July 2023, Alphawave Semi announced successful tapeouts of its High Bandwidth Memory 3 (HBM3) PHY and Universal Chiplet Interconnect Express (UCIe) PHY on TSMC's 3nm process, becoming the first company to tape out a UCIe PHY supporting 24Gbps per lane. Its IP subsystems are integrated with the TSMC 3DFabric ecosystem and support protocols including CXL, UCIe, HBMx, and Ethernet, enabling hyperscaler and data infrastructure customers to build custom chips and chiplets for generative AI and data center workloads.

## Key Claims

- Announced two successful 3nm tapeouts on TSMC's most advanced 3nm process: HBM3 PHY IP and UCIe PHY IP, enabling chiplet-based custom silicon platforms.
- The HBM3 PHY IP targets leading-edge memory interfaces up to 8.6 Gbps with 16 channels at very low power; it can be paired with a JEDEC-compliant configurable HBM controller for AI and HPC workloads.
- The UCIe PHY IP operates at 24 Gbps per wire, providing 7.9 Terabits per second of bandwidth over a 1 mm chip beachfront, with power consumption less than 0.3 picoJoules per bit.
- Alphawave Semi is the first company to announce a UCIe PHY supporting 24 Gbps per lane.
- The UCIe PHY can be configured with advanced packaging (CoWoS, InFO) or organic substrates and paired with PCIe, CXL, and streaming controllers to support the full UCIe protocol stack.
- The company offers application-optimized IP subsystems and experience with the TSMC 3DFabric ecosystem to integrate CXL, UCIe, HBMx, and Ethernet into custom chips and chiplets.
- Customers include hyperscaler and data infrastructure clients who mix and match custom SoCs with IO connectivity chiplets for AI-enabled systems.

## Relationships

- [[alphawave_semi_hbm_subsystem]]: Alphawave Semi's HBM3 PHY IP described in this press release is a component of the company's HBM subsystem product line, which integrates a JEDEC-compliant HBM controller and PHY supporting HBM3, HBM2E, and HBM2.
- [[meta_vistara_cxl_bridge]]: Alphawave Semi's IP portfolio includes CXL controller support for its UCIe PHY, the same Compute Express Link protocol used by Meta's Vistara CXL bridge chip to enable DDR4 memory tiering in DDR5 servers.
- [[nvidia_blackwell_ultra]]: Both Alphawave Semi's HBM3 IP and NVIDIA Blackwell Ultra's HBM3E memory subsystem target high-bandwidth memory for AI workloads, with Alphawave providing the interface IP that can be deployed in custom silicon similar to Blackwell Ultra's use of HBM3E.

## Sources

- [Alphawave Semi Spearheads Chiplet-Based... - Alphawave Semi](raw/cache/06107835f0be2880.md)
