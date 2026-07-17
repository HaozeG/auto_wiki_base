---
canonical_name: Intel Xeon 6 SoC (Granite Rapids-D)
aliases:
- Granite Rapids-D
- Intel Granite Rapids-D
subtype: edge-optimized processor
hardware_targets:
- Edge devices
- Edge nodes
- Data centers (via optical interconnect)
workloads:
- Edge AI inference
- Video transcode
- Analytics
- Live OTT
- VOD
- Broadcast media
datatypes: []
metrics:
- power efficiency (improved vs previous)
- transistor density (improved)
toolchains: []
constraints:
- Extended operating temperature range
- Industrial-class reliability
evidence_strength: reported
scorecard:
  novelty_delta: 0.9
  claim_density: 0.5
  self_containedness: 0.85
  bridge_score: 0.3
  hub_potential: 0.2
sources:
- raw/cache/3c482d9fa49d09d7.md
- https://www.networkworld.com/article/3496955/intel-highlights-new-xeons-for-ai-at-hot-chips-2024.html
source_url: https://www.networkworld.com/article/3496955/intel-highlights-new-xeons-for-ai-at-hot-chips-2024.html
fetched_at: '2026-07-17T11:53:57.759695+00:00'
type: processor_architecture
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 0
---

# Intel Xeon 6 SoC (Granite Rapids-D)

The Intel Xeon 6 SoC, code-named Granite Rapids-D, is an edge-optimized processor scheduled for launch in the first half of 2025. It is built from the compute chiplet of Intel Xeon 6 processors combined with an edge-optimized I/O chiplet, delivering improvements in performance, power efficiency, and transistor density over previous generations. The SoC integrates AI acceleration and supports up to 32 lanes of PCIe 5.0, up to 16 lanes of CXL 2.0, and 2x100G Ethernet for high-throughput edge connectivity. It also features a co-packaged optical compute interconnect (OCI) chiplet capable of 64 channels of 32 Gbps data transmission over 100 meters of fiber, enabling coherent memory expansion and resource disaggregation for AI infrastructure. Edge-specific enhancements include extended operating temperature ranges, industrial-class reliability, and new media acceleration capabilities for video transcode and analytics in live OTT, VOD, and broadcast applications. This chip leverages telemetry from over 90,000 edge deployments to optimize its design for edge-to-node scaling.

## Key Claims

- Combines a fixed-function compute chiplet from Intel Xeon 6 with a custom edge-optimized I/O chiplet.
- Offers up to 32 lanes of PCIe 5.0, 16 lanes of CXL 2.0, and 2x100G Ethernet.
- Integrates an optical compute interconnect (OCI) chiplet with 64 channels at 32 Gbps per channel over 100 meters.
- Designed for extended temperature ranges and industrial reliability.
- Includes media acceleration for video transcode (live OTT, VOD, broadcast).
- Targets single-system architecture scaling from edge devices to edge nodes.
- Launch H1 2025.

## Relationships

Shares a focus on high-bandwidth memory interconnect technologies: Granite Rapids-D's OCI chiplet enables coherent memory expansion, while the [[alphawave_semi_hbm_subsystem]] provides HBM3/2E/2 memory subsystem IP for high-performance computing and AI workloads.

## Sources

- [Intel highlights new Xeons for AI at Hot Chips 2024](raw/cache/3c482d9fa49d09d7.md)
