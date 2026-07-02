---
canonical_name: D1-H
aliases:
- Allwinner D1-H
- Nezha development board
- Allwinner D1
- sun20iw1p1
subtype: null
tags: []
hardware_targets:
- D1-H
toolchains: []
constraints:
- RISC-V 64-bit
- RVV
scorecard:
  novelty_delta: 0.9
  claim_density: 0.7
  self_containedness: 0.9
  bridge_score: 0.3
  hub_potential: 0.5
sources:
- raw/cache/40ba030947b35b05.md
- https://d1.docs.aw-ol.com/en/
- raw/cache/af92e96d7e638346.md
- https://linux-sunxi.org/D1
source_url: https://d1.docs.aw-ol.com/en/
fetched_at: '2026-07-02T10:55:31.740728+00:00'
type: hardware_target
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# D1-H

The D1-H is Allwinner's first system-on-chip (SoC) based on the RISC-V ISA, integrating a 64-bit T-Head XuanTie C906 core operating at up to 1 GHz with support for the RISC-V Vector Extension (RVV). It includes 32 KB each of I-cache and D-cache, a HiFi4 DSP at 600 MHz with 64 KB each of I-ram and D-ram, and supports up to 2 GB of DDR2 or DDR3 memory via a 22 nm process. The SoC features a video engine capable of H.265 decoding up to 4K@30fps and H.264 up to 4K@24fps, as well as JPEG/MJPEG encoding. Display outputs include RGB LCD, dual-link LVDS, MIPI DSI, HDMI 1.4 up to 4K@30fps, and CVBS. Connectivity includes USB 2.0 OTG/Host, SDIO 3.0, SPI, UART, TWI, PWM, GPADC, LRADC, TPADC, IR TX/RX, and a 10/100/1000 Mbps EMAC with RMII and RGMII interfaces. The D1-H is designed for applications in smart cars, HMI, smart home, and education, and runs Linux and RTOSes.

## Key Claims

- Supports RISC-V 64-bit with RVV, 1 GHz frequency.
- 32 KB I-cache + 32 KB D-cache.
- HiFi4 DSP at 600 MHz with 64 KB I-ram and 64 KB D-ram.
- Up to 2 GB DDR2/DDR3 memory.
- H.265 decode up to 4K@30fps, H.264 decode up to 4K@24fps.
- HDMI 1.4 output up to 4K@30fps.
- 10/100/1000 EMAC with RMII and RGMII.
- 22 nm process, LFBGA BGA13x13/0.35/0.65mm, 337 pins package.

## Optimization-Relevant Details

- ISA/profile: RISC-V 64-bit with RVV (vector extension).
- Vector/matrix/accelerator support: C906 core with RVV, HiFi4 DSP for audio/signal processing.
- Memory/cache/TLB/DMA: 32 KB I-cache + 32 KB D-cache, external DDR2/DDR3 up to 2 GB, SD/eMMC/SPI flash.
- Compiler/toolchain support: Linux, RTOS (no specific compiler version mentioned).

## Relationships

- [[cpa-factored-gemmini-systolic-array]]: This optimization recipe targets area and delay reduction in a Gemmini systolic array, which is an AI accelerator design that could potentially target RISC-V SoCs like the D1-H for machine learning inference, but the D1-H itself does not include a systolic array.
- [[earth-shifting-based-vector-memory-access]]: This recipe improves vector memory access for RISC-V vector units; the D1-H's C906 core with RVV could benefit from such optimizations.
- Insufficient context for additional cross-links; no existing entity pages in the wiki_context.

## Sources

- [D1-H Development Board Documentation](https://d1.docs.aw-ol.com/en/)
