---
cold_start: true
created: YYYY-MM-DD
inbound_links: 0
needs_summary_revision: false
scorecard:
  bridge_score: 0.6
  claim_density: 0.8
  hub_potential: 0.5
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://github.com/kendryte/k230_sdk
tags:
- RISC-V
- AI
- SoC
- Kendryte
- K230
- AIoT
type: entity
updated: '2026-06-28'
---

# Kendryte K230

The Kendryte K230 is a System-on-Chip (SoC) from Canaan (Kendryte) targeting AIoT applications, introduced as the latest generation in the Kendryte series. It integrates two RISC-V high-performance computing cores and a new generation Knowledge Process Unit (KPU) intelligent computing unit, which supports multi-precision AI computing and achieves over 70% utilization for typical inference networks. The SoC includes a range of dedicated hardware accelerators for 2D, 2.5D, scalar, vector, and graphics tasks, enabling low-latency full-process acceleration for image, video, audio, and AI workloads, while offering low power consumption, fast boot, and high security. The K230 is supported by an official SDK (k230_sdk) hosted on GitHub, which provides a complete development environment including a Linux and RT-Smart dual-core heterogeneous system, toolchains, and board support packages for reference hardware platforms such as the K230-USIP-LP3-EVB and the CanMV-K230 development boards.

## Key Claims

- K230 SoC integrates two RISC-V high-performance computing cores as the primary compute elements.
- Features a new generation KPU (Knowledge Process Unit) for AI inference with multi-precision support (e.g., INT8/INT16) and over 70% network utilization for typical models.
- Includes hardware acceleration for 2D, 2.5D graphics, scalar and vector operations, providing full-pipeline acceleration for image, video, audio, and AI tasks.
- Rich peripheral interfaces including MIPI CSI, MIPI DSI, USB, SD/eMMC, Ethernet, HDMI (on CanMV-K230), and serial interfaces.
- The K230 SDK provides a Linux & RT-Smart dual-core heterogeneous system with source code in `src/big`, `src/little`, and `src/common` directories.
- Two reference development boards are documented: K230-USIP-LP3-EVB (with LPDDR3 512MB, 32Mbit QSPI NOR Flash, 4GB eMMC, MIPI CSI/DSI, and FT2232 debug) and CanMV-K230 (with HDMI, Ethernet, WiFi/BT, OV5647 sensor interface).
- SDK compilation is performed in a Docker environment using the provided image `ghcr.io/kendryte/k230_sdk`, with pre-compiled images available from the [Kendryte developer community](https://developer.canaan-creative.com/resource).
- The SDK supports configs for different boards, e.g., `k230_evb_defconfig` and `k230_canmv_defconfig`.

## Relationships

- [[Sipeed_MAIX_series]]: Both are Kendryte-family SoC-based development platforms; the Sipeed MAIX series uses the earlier Kendryte K210, while K230 targets more advanced AIoT applications.
- (Insufficient context for additional cross-links to entity pages; the wiki_context contains only one entity page suitable for this relationship.)

## Sources

- [Kendryte K230 SDK GitHub Repository](https://github.com/kendryte/k230_sdk)

