---
canonical_name: Snapdragon X Elite
aliases:
- X Elite
- Snapdragon X Elite Oryon
- Qualcomm Snapdragon X Elite
- Oryon
subtype: mobile_pc_processor
hardware_targets:
- Snapdragon X Elite
- Qualcomm Oryon CPU
- Adreno GPU
- Hexagon NPU
workloads:
- single-threaded
- multi-threaded
- GPU graphics
- AI inference
datatypes:
- FP32
- INT8
metrics:
- Geekbench 6 single-core score
- Geekbench 6 multi-core score
- 3DMark Wild Life Extreme score
- TFLOPs
- TOPs
- power consumption
toolchains: []
constraints:
- TSMC 4nm process
- LPDDR5x-8533 memory
- PCIe Gen 4.0
- Snapdragon X65 5G modem
- Wi-Fi 7
- Bluetooth 5.4
evidence_strength: reported
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.9
  self_containedness: 0.9
  bridge_score: 0.2
  hub_potential: 0.6
sources:
- raw/cache/95e156228920593f.md
- https://wccftech.com/qualcomm-snapdragon-x-elite-cpu-pc-benchmarks-oryon-faster-intel-13th-gen-apple-m2-max-gpu-faster-amd-rdna-3/
- raw/cache/7115879833a0822b.md
- https://cputronic.com/cpu/qualcomm-snapdragon-x-elite
source_url: https://wccftech.com/qualcomm-snapdragon-x-elite-cpu-pc-benchmarks-oryon-faster-intel-13th-gen-apple-m2-max-gpu-faster-amd-rdna-3/
fetched_at: '2026-07-17T12:05:44.635030+00:00'
type: processor_architecture
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 0
---

# Snapdragon X Elite

The Qualcomm Snapdragon X Elite is a 12-core processor designed for Windows PCs, announced by Qualcomm in October 2023. It features the custom Oryon CPU cores fabricated on TSMC's 4nm process, with a maximum boost clock of 4.3 GHz on one or two cores and an all-core boost of 3.8 GHz. The chip includes 42 MB of total cache, an Adreno GPU rated at up to 4.6 TFLOPs, and a Hexagon AI accelerator delivering 75 TOPS. It supports up to 64 GB of LPDDR5x-8533 memory, PCIe Gen 4.0 NVMe storage, and integrated Snapdragon X65 5G modem with Wi-Fi 7 and Bluetooth 5.4. Qualcomm positions the Snapdragon X Elite to compete with Intel's 13th-gen Core processors, AMD's Ryzen 7000 series, and Apple's M2 Max chip, claiming significant performance-per-watt advantages.

## Key Claims

- Single-core Geekbench 6 score of 3227 points, claimed to be 14% faster than Apple M2 Max (2841 points) while consuming 30% less power.
- Single-core Geekbench 6 score leads Intel Core i9-13980HX (3192 points) by 1% while consuming 70% less power.
- Multi-threaded Geekbench 6 performance up to 2x faster than Intel 13th Gen 12-core CPU at the same power, and matches peak performance while consuming 68% less power.
- Multi-threaded performance 60% faster than Intel Core i7-13800H at the same power, matching its peak with 65% less power.
- Multi-threaded performance 50% better than Apple M2 (non-Max) in unspecified test.
- Integrated Adreno GPU (4.6 TFLOPs) claimed to be 2x faster than Intel Core i7-13800H iGPU at same power, and 80% faster than AMD Ryzen 9 7940HS RDNA 3 iGPU at same power.
- CPU cores arranged in three clusters of four, total 42 MB cache.
- Hexagon AI accelerator delivers 75 TOPS as a Micro NPU.
- Supports LPDDR5x-8533 memory up to 64 GB.
- Planned launch mid-2024.

## Relationships

None.

## Sources

- [Qualcomm Unveils Snapdragon X Elite CPU PC Benchmarks: Oryon...](raw/cache/95e156228920593f.md)
