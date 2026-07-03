---
canonical_name: meta-andes
aliases:
- Andes BSP Layer
- Andes OpenEmbedded Layer
- Andes Yocto Layer
subtype: null
tags:
- RISC-V
- BSP
- Yocto
- Andes Technology
scorecard:
  novelty_delta: 0.9
  claim_density: 0.5
  self_containedness: 0.8
  bridge_score: 0.2
  hub_potential: 0.2
sources:
- raw/cache/9a18c1d42a529c76.md
- https://github.com/andestech/meta-andes
source_url: https://github.com/andestech/meta-andes
fetched_at: '2026-07-03T15:55:36.115886+00:00'
type: entity
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 0
outbound_links:
- target: xuantie-c906-hardware-target
  reason: Both meta-andes and the XuanTie C906 ecosystem provide Yocto-based Linux
    builds for RISC-V embedded platforms, but target different vendor core families
    (Andes Technology vs. Alibaba T-Head) and different SoC integrations
---

# meta-andes

meta-andes is the official OpenEmbedded/Yocto BSP layer provided by Andes Technology Corporation for building bootable disk images targeting AndesCore processor-based platforms, specifically the AE350 series. The layer supplies machine configuration files, recipes, and kas-container build workflows for supported AndesCore processors including the AX45MP, AX45MPV, and AX65, and bundles pre-configured versions of OpenSBI, U-Boot, and Linux kernel. The build output includes a compressed root filesystem image (wic.gz), a Flattened Image Tree (FIT) containing the kernel and device tree, and bootloader binaries (U-Boot SPL and U-Boot ITB) for flash programming. The layer also provides tooling to update bootloaders via the SPI_burn utility over JTAG using an ICEman debugger.

## Key Claims

- The meta-andes layer supports AE350-series platforms with ten AndesCore processor options: A25MP, A27L2, A45MP, AX25MP, AX27L2, AX45MP, AX45MPV, AX46MPV, AX65, and AX66.
- Builds are driven via kas-container, providing a reproducible Yocto development environment.
- The layer bundles OpenSBI v1.5.1, U-Boot v2024.07, and Linux kernel 6.6.49 from Andes' own forks.
- The accompanying toolchain is GCC 13.2.0 with Binutils 2.42.
- Build artifacts include core-image-base rootfs images (.wic.gz), fitImage (kernel+DTB), device tree blobs, U-Boot SPL, and U-Boot ITB.
- Bootloader and DTB updates on target hardware require the SPI_burn tool connected via an ICEman JTAG debugger.

## Relationships

- [[xuantie-c906-hardware-target]]: Both meta-andes and the XuanTie C906 ecosystem provide Yocto-based Linux builds for RISC-V embedded platforms, but target different vendor core families (Andes Technology vs. Alibaba T-Head) and different SoC integrations.

## Sources

- https://github.com/andestech/meta-andes
- https://github.com/andestech/opensbi/tree/ast-v5_4_0-branch
- https://github.com/andestech/uboot/tree/ast-v5_4_0-branch
- https://github.com/andestech/linux/tree/ast-v5_4_0-branch
