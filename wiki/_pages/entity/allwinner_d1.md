---
cold_start: false
created: '2026-06-27'
inbound_links: 0
scorecard:
  bridge_score: 0.7
  claim_density: 0.9
  hub_potential: 0.8
  novelty_delta: 1.0
  self_containedness: 0.8
sources:
- https://linux-sunxi.org/D1
tags:
- allwinner
- risc-v
- soc
- xuantie-c906
type: entity
updated: '2026-06-27'
---

# Allwinner D1

The Allwinner D1 (also known as D1-H, sun20iw1p1) is the first system-on-chip (SoC) from Allwinner Technology to be based on a RISC-V instruction set architecture (ISA) core. Manufactured on a 22 nm process, the D1 integrates a single XuanTie C906 RISC-V core from T-Head Semiconductor (a subsidiary of Alibaba) running at up to 1 GHz with support for the RV64IMAFDCVU extensions, along with a 600 MHz Tensilica HiFi4 digital signal processor (DSP) for audio/voice processing. The SoC supports DDR2/DDR3 memory up to 2 GB and provides hardware video decoding up to 4K at 30 frames per second for H.265, H.264, MPEG, JPEG, VC1, and MJPEG formats. It includes a comprehensive set of connectivity interfaces: HDMI, MIPI DSI, LVDS, LCD, and CVBS video outputs; CSI and CVBS inputs; audio DAC/ADC and I2S-PCM interfaces; a 10/100/1000 Mbps Ethernet MAC; SDIO 3.0 and eMMC 5.0 storage; and USB 2.0 (one OTG and one host). The D1 was announced in August 2020 and released in April 2021, marking a significant milestone for RISC-V in the application processor market.

## Key Claims

- The Allwinner D1 is the first Allwinner SoC to use a RISC-V core, specifically the XuanTie C906, and is fabricated on a 22 nm process (linux-sunxi.org).
- The CPU supports the RV64IMAFDCVU extension set, indicating it supports scalar, integer, multiply-divide, atomic, single/double-precision floating-point, compressed, and vector operations (linux-sunxi.org).
- The SoC includes a Tensilica HiFi4 DSP clocked at 600 MHz for dedicated audio and signal processing tasks (linux-sunxi.org).
- Memory support covers DDR2 and DDR3 with a maximum capacity of 2 GB (linux-sunxi.org).
- Video decoding capabilities: 4K @ 30 FPS for H.265, H.264, MPEG, JPEG, VC1, and MJPEG; encoding at 1080p @ 60 FPS for JPEG and MJPEG (linux-sunxi.org).
- Connectivity includes HDMI, MIPI DSI, LVDS, LCD, CVBS outputs; CSI and CVBS inputs; audio interfaces (DAC, ADC, CODEC, I2S-PCM, DMIC); Gigabit Ethernet MAC; SDIO 3.0, eMMC 5.0, SPI NOR/NAND Flash; USB 2.0 OTG and Host (linux-sunxi.org).
- The D1 (D1-H) is distinguished from the D1s variant by the presence of HDMI output (linux-sunxi.org).
- Release date: April 2021, with cooperation announced in August 2020 between Allwinner and T-Head (PingTou) (linux-sunxi.org, CNX Software).

## Relationships

- [[ai_chip_export_controls]] — The Allwinner D1, as a Chinese-designed RISC-V SoC, contributes to China's semiconductor self-sufficiency efforts and is part of the landscape that motivates export control policies targeting advanced computing chips. While the D1 itself is not an AI accelerator, its development reflects the broader push of Chinese firms into RISC-V architecture as an alternative to ARM and x86.
- RISC-V Ecosystem — The D1 is a tangible example of a commercially available RISC-V application processor, supporting the growth of the RISC-V software ecosystem including Linux, SDKs, and toolchains.
- Allwinner — The D1 is a flagship product for Allwinner, showcasing their entry into RISC-V and expanding beyond their traditional ARM-based SoCs (such as A series and H series).
- XuanTie C906 — This core is a product of T-Head Semiconductor, a subsidiary of Alibaba, representing one of the early high-performance RISC-V cores used in production SoCs.

## Sources

- linux-sunxi.org: D1 — https://linux-sunxi.org/D1
- CNX Software: "A first look at Allwinner D1 Linux RISC-V SBC and Processor" — referenced in the linux-sunxi page
