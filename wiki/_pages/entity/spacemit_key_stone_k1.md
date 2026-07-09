---
canonical_name: SpacemiT Key Stone K1
aliases:
- K1
- Key Stone K1
- SpacemiT K1
- SpacemiT M1
- M1
subtype: null
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 0.9
  bridge_score: 0.6
  hub_potential: 0.2
sources:
- raw/cache/7425cd2ca5e86dc2.md
- https://github.com/spacemit-com/docs-chip/blob/main/en/key_stone/k1/k1_docs/k1_ds.md
- raw/cache/3fbc156ba94261a9.md
- https://github.com/spacemit-com/docs-chip/blob/main/en/key_stone/k1/k1_docs/k1_usermanual/1.Overview.md
- raw/cache/2fa3ccc6aed9005e.md
- https://www.spacemit.com/products/keystone/k1
- raw/cache/9b39243f31bf206f.md
- https://wiki.postmarketos.org/wiki/SpacemiT_Key_Stone_K1
source_url: https://github.com/spacemit-com/docs-chip/blob/main/en/key_stone/k1/k1_docs/k1_ds.md
fetched_at: '2026-07-09T03:23:50.567385+00:00'
type: entity
created: '2026-07-09'
updated: '2026-07-09'
cold_start: true
inbound_links: 0
outbound_links:
- target: ara
  reason: The SpacemiT X60 core in the K1 implements the RISC-V Vector Extension,
    which is the same extension specification supported by the Ara vector unit from
    the PULP project. Ara implements RISC-V V 1.0 as a coprocessor for CVA6, while
    the X60 integrates vector processing directly into the core pipeline
---

# SpacemiT Key Stone K1

The SpacemiT Key Stone K1 is a high-performance and ultra-low-power system-on-chip (SoC) developed by SpacemiT, integrating eight RISC-V CPU cores based on the company's self-innovated X60 core microarchitecture. The X60 core adheres to the RISC-V 64GCVB architecture and the RVA22 standard, supporting 256-bit vector extensions and delivering up to 2.0 TOPS of AI computing power through customized RISC-V instructions that enable CPU AI fusion computing. The SoC is organized into two clusters of four cores each, with Cluster 0 featuring AI acceleration capabilities. The K1 includes a range of memory interfaces such as LPDDR4/LPDDR4x and LPDDR3, multiple peripheral controllers including USB 3.0, PCIe Gen2, GMAC, MIPI CSI and DSI, and an IMG BXE-2-32 GPU. It is designed for industrial-grade applications with an operating temperature range of -40°C to +85°C.

## Key Claims

- The K1 integrates eight SpacemiT X60 RISC-V processor cores adhering to RISC-V 64GCVB and RVA22.
- Cluster 0 provides 2.0 TOPS AI computing power with 256-bit vector extension, 512 KB L2 cache, and 512 KB TCM.
- Cluster 1 includes four cores with 512 KB L2 cache and 256-bit vector extension without AI acceleration.
- Supports LPDDR4/LPDDR4x at 2666 Mbps up to 16 GB and LPDDR3 at 1866 Mbps up to 4 GB.
- Includes an IMG BXE-2-32 GPU at 819 MHz supporting OpenCL 3.0, OpenGL ES 3.2, and Vulkan 1.3.
- VPU supports H.265/H.264/VP8/VP9/MPEG4/MPEG2 decode at 4K@60fps and encode at 4K@30fps.
- Peripherals include 128 GPIO, 10 UART, 10 I2C, 4 SPI, 3 USB, 3 PCIe Gen2, 2 GMAC, SDIO, SD, eMMC, MIPI CSI-2, and MIPI DSI.
- Security features include secure boot, secure eFuse, cryptographic engine (TRNG, AES, RSA, ECC, SHA2, HMAC), and RISC-V PMP.
- Operates at -40°C to +85°C industrial temperature range.

## Relationships

- [[ara]]: The SpacemiT X60 core in the K1 implements the RISC-V Vector Extension, which is the same extension specification supported by the Ara vector unit from the PULP project. Ara implements RISC-V V 1.0 as a coprocessor for CVA6, while the X60 integrates vector processing directly into the core pipeline.

## Sources

- [docs-chip/en/key_stone/k1/k1_docs/k1_ds.md at main · spacemit ... - GitHub](raw/cache/7425cd2ca5e86dc2.md)
