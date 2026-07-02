---
canonical_name: StarFive VisionFive2
aliases:
- VisionFive2
- VisionFive 2
- JH7110 VisionFive2
- StarFive JH7110 VisionFive2
subtype: null
tags:
- risc-v
- jh7110
- starfive
- sdk
hardware_targets:
- StarFive VisionFive2
toolchains:
- RISC-V cross-compile toolchain
- U-boot
- OpenSBI
- Linux kernel
- Buildroot
constraints:
- RV64IMAFDCBX (from boot log rv64imafdcbx)
- 5 HARTs (from OpenSBI boot log)
- DDR memory (version dc2e84f0)
- SPI boot
- UART8250 console
scorecard:
  novelty_delta: 0.4
  claim_density: 0.6
  self_containedness: 0.8
  bridge_score: 0.3
  hub_potential: 0.5
sources:
- raw/cache/e4bd9be96a3200d5.md
- https://github.com/starfive-tech/VisionFive2
source_url: https://github.com/starfive-tech/VisionFive2
fetched_at: '2026-07-01T04:11:41.122129+00:00'
type: hardware_target
created: '2026-07-01'
updated: '2026-07-01'
cold_start: false
inbound_links: 1
needs_summary_revision: false
---

# StarFive VisionFive2

The StarFive VisionFive2 is a RISC-V development board powered by the StarFive JH7110 SoC. It is designed for a range of embedded and general-purpose computing applications. The official SDK provided by StarFive builds a complete software stack from source, including a RISC-V cross-compile toolchain, U-boot SPL (2021.10), U-boot, OpenSBI firmware (v1.0), a Linux kernel version 5.15, device tree binaries (such as jh7110-starfive-visionfive-2-v1.3b.dtb), and initramfs/rootfs images (image.fit, initramfs.cpio.gz). The board boots via SPI and supports network boot over TFTP. The OpenSBI boot log reveals a platform name of "StarFive VisionFive V2", with 5 HARTs (hart IDs 0-4), base ISA rv64imafdcbx, and a UART8250 console. The SDK also provides multiple device tree overlays for different hardware revisions (A10, A11, v1.3b) and an AC108 or WM8960 audio codec variant. This hardware target enables developers to build and run a full RISC-V Linux environment for experimentation and development.

## Key Claims

- Builds a complete RISC-V cross-compile toolchain for the JH7110 SoC.
- Produces U-boot SPL (u-boot-spl.bin.normal.out), U-boot, OpenSBI firmware (visionfive2_fw_payload.img), and a flattened image tree (image.fit) containing Linux kernel 5.15, device tree, ramdisk, and rootfs.
- Boot process: SPI -> U-boot SPL -> OpenSBI v1.0 -> Linux kernel.
- Platform has 5 HARTs, base ISA rv64imafdcbx, UART8250 console.
- Multiple device tree variants support different board revisions (A10, A11, v1.3b) and audio codec options (AC108, WM8960).
- The build consumes approximately 18 GB of disk space and requires Ubuntu 16.04/18.04/20.04/22.04 x86_64 as the recommended host OS.

## Optimization-Relevant Details

- ISA/profile: RV64IMAFDCBX (base ISA with M, A, F, D, C, B, X extensions; no standard vector extension detected from boot log).
- Vector/matrix/accelerator support: Not publicly documented in this resource; no AI or vector acceleration specifically highlighted.
- Memory/cache/TLB/DMA: DDR memory controller version dc2e84f0; exact cache hierarchy not disclosed.
- Compiler/toolchain support: RISC-V GNU toolchain (built by SDK), U-boot, OpenSBI, Linux kernel, Buildroot.

## Relationships

- [[xuantie_c908]]: Another RISC-V hardware target with AI acceleration features; contrasts with the general-purpose orientation of the VisionFive2.
- [[rvme]]: A RISC-V matrix engine coprocessor design; shows how RISC-V platforms can incorporate custom accelerators, whereas the VisionFive2 relies on software-based workloads.

## Sources

- https://github.com/starfive-tech/VisionFive2 (README, boot log excerpts)
