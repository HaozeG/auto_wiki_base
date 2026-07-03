---
canonical_name: GAP9
aliases:
- GreenWaves GAP9
- GAP9 SoC
subtype: null
tags: []
hardware_targets:
- GAP9
toolchains: []
constraints:
- 150GOPS peak performance
- MIPI CSI2 interface
- ultra-low-power (<100mW for AI workloads)
- 8-core RISC-V PULP architecture
scorecard:
  novelty_delta: 1.0
  claim_density: 0.7
  self_containedness: 0.8
  bridge_score: 0.2
  hub_potential: 0.3
sources:
- raw/cache/1268f13c392a2dec.md
- https://arxiv.org/html/2407.13706v1
source_url: https://arxiv.org/html/2407.13706v1
fetched_at: '2026-07-03T14:43:04.554332+00:00'
type: hardware_target
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 3
---

# GAP9

The GAP9 is the latest Parallel-Ultra-Low-Power (PULP) processor from GreenWaves Technologies, designed for ultra-low-power edge AI and digital signal processing applications. It features an 8-core RISC-V architecture capable of up to 150GOPS, making it suitable for on-device inference tasks such as object detection, localization, and mapping. The SoC integrates a MIPI CSI2 interface to support high-definition cameras, a significant improvement over its predecessor GAP8. GAP9 is the core component of the GAP9Shield module for nano-drones, where it enables real-time AI workloads within a power envelope below 100 mW and latencies as low as 17 ms for object detection (YOLO). The processor is part of the PULP family and builds on open-source RISC-V ISA, providing a programmable platform for energy-constrained autonomous systems.

## Key Claims

- GAP9 achieves a peak performance of 150GOPS, as stated in the GAP9Shield paper.
- The SoC can run object detection (YOLO), localization, and mapping with a power envelope below 100 mW.
- Object detection latency is as low as 17 ms using YOLO on QVGA resolution.
- The GAP9Shield module, when compared to the Crazyflie AI-deck with GAP8, provides a 20% higher RGB image sample rate (7 FPS vs 5.8 FPS) and a 20% weight reduction.
- GAP9 supports streaming VGA images at 4 FPS and 3-channel RGB QVGA images at 7 FPS.
- The SoC integrates a MIPI CSI2 interface for high-definition camera connectivity.

## Optimization-Relevant Details

- ISA/profile: RISC-V (PULP family); specific extensions not detailed in source.
- Vector/matrix/accelerator support: Not explicitly specified beyond peak GOPS claim.
- Memory/cache/TLB/DMA: Not detailed in available source.
- Compiler/toolchain support: Not specified.

## Relationships

No specific relationship to visible context pages.

## Sources

- https://arxiv.org/html/2407.13706v1 (GAP9Shield paper)
