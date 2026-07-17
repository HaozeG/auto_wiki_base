---
canonical_name: RDNA 3
aliases:
- AMD RDNA 3
- RDNA3
- RDNA
- Radeon DNA
- RDNA 1
- RDNA 2
- RDNA 4
- AMD Radeon RX 9000 Series
- Radeon RX 9070
- Radeon RX 9000
- Radeon AI PRO R9700
subtype: gpu_architecture
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 0.7
  bridge_score: 0.6
  hub_potential: 0.5
sources:
- raw/cache/a3ae83af13d2e238.md
- https://en.wikipedia.org/wiki/RDNA_3
- raw/cache/c5bfb31c4b6a4a43.md
- https://www.wikiwand.com/en/RDNA_(microarchitecture)
- raw/cache/8502646ec6473c2f.md
- https://www.amd.com/en/products/graphics/radeon-ai.html
source_url: https://en.wikipedia.org/wiki/RDNA_3
fetched_at: '2026-07-17T10:15:59.469233+00:00'
type: entity
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 0
---

# RDNA 3

RDNA 3 is a GPU microarchitecture designed by AMD, released with the Radeon RX 7000 series on December 13, 2022. It is the successor to RDNA 2 and features a chiplet packaging design for the first time in a consumer GPU, utilizing TSMC N5 and N6 fabrication processes. The architecture includes up to 122.8 TFLOPS of FP16 compute performance and supports Direct3D 12.0 Ultimate, Vulkan 1.3, and OpenGL 4.6. RDNA 3 also powers the SoCs in handheld gaming devices like the Asus ROG Ally and Lenovo Legion Go. This microarchitecture achieves a 50% performance-per-watt improvement over RDNA 2 through architectural optimizations and the chiplet approach.

## Key Claims

- Compute performance: up to 122.8 TFLOPS (FP16), 61.42 TFLOPS (FP32), 1.919 TFLOPS (FP64).
- Clock rates range from 1500 MHz to 2500 MHz, with a shader clock of 2269 MHz.
- Cache hierarchy: 96 KB L0 per WGP (32 KB vector + 16 KB scalar), 256 KB L1 per array, up to 6 MB L2, and up to 96 MB L3 (16 MB per MCD).
- Memory subsystem: GDDR6 at up to 20 Gbps, supporting PCIe 4.0.
- Media engine encodes and decodes H.264, H.265, and AV1; supports 8/10/12-bit color depth.
- Display outputs include DisplayPort 2.1, HDMI 2.1a, and USB-C.
- Supports Direct3D 12.0 Ultimate (feature level 12_2), Shader Model 6.7, Vulkan 1.3, OpenGL 4.6, and OpenCL 2.1.
- Built using chiplet packaging with a Graphics Compute Die (GCD) on TSMC N5 and Memory Cache Dies (MCD) on TSMC N6.

## Relationships

- [[amd_cdna]] covers the compute-oriented CDNA architecture, which shares the chiplet packaging technology with RDNA 3 but targets datacenter workloads. CDNA 3 is listed as a datacenter variant of the RDNA 3 microarchitecture, sharing foundational design elements while removing graphics-specific hardware.

## Sources

- [RDNA 3 - Wikipedia](raw/cache/a3ae83af13d2e238.md)
