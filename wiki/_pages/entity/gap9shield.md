---
canonical_name: GAP9Shield
aliases:
- GAP9 Shield
- GAP9Shield module
- GAP9Shield nano-drone module
subtype: null
tags: []
scorecard:
  novelty_delta: 0.6
  claim_density: 0.7
  self_containedness: 0.8
  bridge_score: 0.3
  hub_potential: 0.3
sources:
- raw/cache/1268f13c392a2dec.md
- https://arxiv.org/html/2407.13706v1
- raw/cache/a854f8e41a4fef93.md
- https://github.com/pulp-platform/gap9-shield
source_url: https://arxiv.org/html/2407.13706v1
fetched_at: '2026-07-03T16:21:46.959884+00:00'
type: entity
created: '2026-07-03'
updated: '2026-07-06'
cold_start: true
inbound_links: 0
---

# GAP9Shield

The GAP9Shield is a nano-drone-compatible pluggable shield module powered by the GAP9 System-on-Chip (SoC), a 150GOPS-capable ultra-low-power processor from GreenWaves Technologies. The GAP9 SoC features a 9-core RISC-V cluster with a dedicated NE16 AI accelerator, providing 15.6 GOPs for DSP workloads and 32.2 GMACs for ML tasks, with an energy efficiency of 330 µW/GOP and a sleep power as low as 45 µW. Operating at frequencies up to 370 MHz, the module consumes under 100 mW for most AI workloads. Designed for the Crazyflie (CF) quadcopter platform, the GAP9Shield integrates a 5MP OV5647 camera (supporting QSXGA to QVGA, up to 120 fps at QVGA via CSI2), a WiFi-BLE NINA W102 module (ESP32, 2.4 GHz, up to 12 Mbps UDP), and a 5D VL53L1-based ranging subsystem (five Time-of-Flight sensors covering front, back, left, right, and upward, range up to 400 cm at 60 Hz) for omnidirectional obstacle avoidance. Compared to the existing AI-deck and Multi-ranger shield combination, the GAP9Shield achieves a 20% weight reduction while providing a 20% higher RGB image sample rate (7 FPS at QVGA resolution; also streams VGA images at 4 FPS). The module enables real-time AI workloads including object detection (YOLO), localization (MCL), and mapping (SLAM) within a power envelope below 100 mW, with object detection latency as low as 17 ms for QVGA frames. Physically, the board measures 50 mm × 27 mm, weighs approximately 6 g, and uses a 6-layer PCB. The complete platform schematics and PCB diagrams are planned as open-source resources to foster next-generation nano-drone applications.

## Key Claims

- GAP9Shield is powered by the GAP9 SoC, providing 150GOPS peak performance.
- The GAP9 SoC integrates a 9-core RISC-V cluster with NE16 AI accelerator (15.6 GOPs DSP, 32.2 GMACs ML).
- Energy efficiency is 330 µW/GOP, with sleep power as low as 45 µW and frequency up to 370 MHz.
- Memory: 1.6 MB L2 RAM, 2 MB embedded non-volatile memory, plus 256 Mbit PSRAM and 512 Mbit Flash.
- Includes a 5MP OV5647 camera (QSXGA to QVGA, up to 120 fps at QVGA via CSI2 interface).
- Includes a WiFi-BLE NINA W102 module (ESP32, 2.4 GHz, up to 12 Mbps UDP).
- Ranging system: 5D VL53L1 ToF array covering right, left, front, back, and upward directions, range up to 400 cm at 60 Hz.
- 20% weight reduction compared to the combined AI-deck and Multi-ranger shield setup.
- 20% higher image sample rate: transmits 3-channel RGB QVGA images at 7 FPS vs. the AI-deck's monochrome QVGA at an effective lower rate; also streams VGA images at 4 FPS.
- Runs object detection (YOLO), localization (MCL), and mapping (SLAM) with a power envelope below 100 mW.
- Object detection latency as low as 17 ms for YOLO on QVGA resolution.
- Physical: 50 mm × 27 mm, approx. 6 g, 6-layer PCB.
- Platform schematics and PCB diagrams are planned for open-source release.

## Relationships

- Integrates the GAP9 SoC as its primary processor, inheriting its 150GOPS capability, MIPI CSI2 camera interface, and ultra-low-power characteristics. [[gap9]]

## Sources

- https://arxiv.org/html/2407.13706v1
- https://github.com/pulp-platform/gap9-shield
