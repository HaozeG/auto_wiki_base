# Source: Tenstorrent Blackhole RISC-V AI Chip (theregister.com/2024/08/27 + search results)
Fetched: 2026-06-26

## Blackhole Chip Specifications
- FP8 performance: 745 TFLOPS
- FP16 performance: 372 TFLOPS
- Memory: 32 GB GDDR6
- Networking: 10 × 400 Gbps Ethernet links = 1 TBps total bandwidth
- Total RISC-V cores: 768

## RISC-V Core Architecture
- 16 "Big RISC-V" cores: 64-bit, dual-issue, in-order, grouped in 4 clusters, capable of running Linux
- 752 "Baby RISC-V" cores: memory management, off-die communications, data processing
- 140 Tensix cores, each containing 5 Baby RISC-V cores + pair of routers + compute complex + L1 cache
- One of the largest RISC-V implementations in any shipping product at time of announcement (2024)

## Tensix Core Architecture (from Wormhole)
- Each Tensix core: 5 RISC-V baby cores + routers + compute complex
- Wormhole n150: 72 Tensix cores
- Designed for AI dataflow processing

## Product Positioning
- Blackhole designed as standalone AI computer (unlike Grayskull and Wormhole which were PCIe-based accelerators)
- Chiplet architecture in development; 2nm collaboration with LSTC

## Wormhole Specifications
- Up to 24 GB GDDR6
- Two configurations: n150 (single processor, 72 Tensix cores), n300
