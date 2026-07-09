---
canonical_name: Blackhole
aliases:
- Blackhole p100a
- Blackhole p150a
- Blackhole p150b
- Blackhole (Tenstorrent)
- Tenstorrent Blackhole
subtype: chip
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 1.0
  bridge_score: 0.7
  hub_potential: 0.7
sources:
- raw/cache/4c02d9bff7e9fb25.md
- https://blog.gpu.net/posts/2026/june/new-blog-june11/
- raw/cache/31f0a5f77141e654.md
- https://aiwiki.ai/wiki/blackhole_tenstorrent
source_url: https://blog.gpu.net/posts/2026/june/new-blog-june11/
fetched_at: '2026-07-09T09:56:51.857773+00:00'
type: entity
created: '2026-07-09'
updated: '2026-07-09'
cold_start: true
inbound_links: 9
---

# Blackhole

Blackhole is Tenstorrent's third-generation AI accelerator chip, manufactured on Samsung 6nm and released in 2025. It is available in multiple PCIe board variants: the P100A at USD 999 (no Ethernet, active-cooled, 28 GB GDDR6, 120 Tensix cores), P150A at USD 1,399 (with Ethernet, active-cooled, 32 GB GDDR6), and P150B at USD 1,399 (passive-cooled for rack servers, 32 GB GDDR6, full chip grid). Each board includes four QSFP-DD 800G ports. The chip contains 16 general-purpose RISC-V cores in addition to the Tensix mesh of 120 cores (originally 140, reduced via firmware v19.5.0). Published peak compute is 745 TFLOPS FP8 (later revised to 664 TFLOPS for P150 boards after the firmware update). The Galaxy Blackhole rack system builds on this chip with 32 Blackhole processors providing 23 PFLOPS FP8, 6.2 GB on-chip SRAM, 1 TB DRAM, and 56 Ethernet ports for scale-out, starting at USD 110,000 per unit. The toolchain is almost fully open source, ranging from kernel-mode driver (tt-kmd) and user-mode driver (tt-umd) through low-level kernel libraries (tt-llk) to the high-level runtime (tt-metal and TTNN), with the Tensix SFPI toolchain (sfpi) for custom kernel compilation.

## Architecture

The Blackhole chip uses a shared Tensix tile architecture. The architecture employs a grid of Tensix tiles interconnected by two Networks-on-Chip (NoCs) that operate in opposite directions: noc0 originates at the top-left corner and allows packets to move downward or to the right, while noc1 originates at the bottom-right corner and allows movement upward or to the left. This bidirectional separation of read (noc0) and write (noc1) traffic avoids head-of-line blocking. Communication with the host is routed through the PCIe tile (PCIe 0 on the P100A, PCIe 1 on the P150B). The P100A variant harvests two rightmost columns of Tensix tiles and one DRAM bank (4 GB) due to binning, with the fused-off coordinates varying per board. On the P150B the grid is 17 columns × 12 rows; on the P100A it is 14 columns × 12 rows. Each Tensix tile features a dual Network-on-Chip (NoC) with X/Y major routing, five Baby RISC-V cores, a Matrix Unit with 19-bit precision, a Vector Unit with 32-lane FP32, and 1464 KiB of L1 RAM. The architecture also includes a MOP expander. The instruction set documentation is available at https://deepwiki.com/tenstorrent/tt-isa-documentation. The chip integrates 140 Tensix++ compute cores (120 enabled on shipping cards), sixteen SiFive Intelligence X280 RISC-V cores for general-purpose processing, 32 GB of GDDR6 memory, a Gen5 PCI Express interface, and ten 400 Gbps Ethernet links on a single die. This allows the Blackhole to function as a standalone AI computer, capable of running machine learning workloads without host CPU intervention for many tasks. Multicast writes (broadcasting to multiple tiles simultaneously) are imperative for performance when uploading firmware or kernel binaries to many cores; unicast writes to every core sequentially would incur considerable slowdown.

## Key Claims

- Blackhole chip: manufactured on Samsung 6nm, up to 120 Tensix cores (reduced from 140 via firmware v19.5.0 in February 2026).
- Board variants: P100A (USD 999, 28 GB GDDR6, no Ethernet), P150A (USD 1,399, 32 GB GDDR6, 800G Ethernet), P150B (USD 1,399, 32 GB GDDR6, 800G Ethernet, passive-cooled).
- Peak compute: 745 TFLOPS FP8 initial spec; after firmware change, 664 TFLOPS.
- Galaxy Blackhole rack: 32 chips, 23 PFLOPS FP8, 6.2 GB SRAM, 1 TB DRAM, 56 × 800G ports, from USD 110,000.
- The chip contains 140 Tensix++ compute cores, with 120 cores enabled on shipping cards.
- It includes sixteen SiFive Intelligence X280 RISC-V cores for control and general-purpose processing.
- The chip has 32 GB of GDDR6 memory on-package.
- Interfaces: Gen5 PCI Express and ten 400 Gbps Ethernet links (die-level). Each board provides four 800G QSFP-DD ports (board-level).
- The Blackhole P150 PCIe board is marketed as infinitely scalable for AI workloads, acting as a standalone AI computer capable of executing models without host CPU intervention for many tasks.
- The NoC architecture separates read and write traffic (noc0/noc1) to avoid head-of-line blocking.
- The open-source toolchain covers drivers (tt-kmd, tt-umd), low-level kernels (tt-llk), and runtime (tt-metal/TTNN), plus the sfpi compiler for custom kernels.
- The fan can be controlled dynamically by sending a message to the ARC tile; the idle fan curve can be lowered via firmware modifications (e.g., in tt-zephyr-platforms).
- Matmul performance is reported to be approximately equal to an NVIDIA RTX 5090 (reported claim, without detailed measurement context).

## Relationships

- [[tensix-core]] is the compute core used in Blackhole. [[wormhole]] is the previous generation chip; Blackhole offers more Tensix cores, higher memory bandwidth, and integrated Ethernet.
- [[blackhole-quietbox]] uses four Blackhole P150 accelerator chips in a liquid-cooled workstation configuration, providing a development platform that scales to the Galaxy rack systems.
- [[single-core-matmul-tt-metalium]] implements a basic bfloat16 matmul kernel on a single Tensix core of the Blackhole architecture, demonstrating the TT-Metalium programming model that runs on this hardware.

## Sources

- https://blog.gpu.net/posts/2026/june/new-blog-june11/
- https://deepwiki.com/tenstorrent/tt-isa-documentation
- https://aiwiki.ai/wiki/blackhole_tenstorrent
- https://tenstorrent.com/cards (PCIe board details)
- https://nixos.wiki/wiki/Tenstorrent (Tenstorrent platform overview)
- https://anuraagw.me/blog/blackhole-architecture
