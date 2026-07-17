---
canonical_name: Nvidia NVLink and NVSwitch
aliases:
- Nvidia NVLink
- Nvidia NVSwitch
- NVLink 5.0
- NVSwitch 4.0
- NvLink
- NvSwitch
- NVLink
- NVIDIA NVLink
subtype: null
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.4
  self_containedness: 0.9
  bridge_score: 0.3
  hub_potential: 0.5
sources:
- raw/cache/191e6ce867a48d35.md
- https://www.fibermall.com/blog/nvidia-nvlink-and-nvswitch-evolution.htm
- raw/cache/1bb25d6ea84c0446.md
- https://intuitionlabs.ai/articles/nvidia-nvlink-gpu-interconnect
source_url: https://www.fibermall.com/blog/nvidia-nvlink-and-nvswitch-evolution.htm
fetched_at: '2026-07-17T11:45:50.773919+00:00'
type: entity
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 0
---

# Nvidia NVLink and NVSwitch

Nvidia NVLink is a high-bandwidth, low-latency point-to-point interconnect protocol designed for GPU-to-GPU and GPU-to-CPU communication, while Nvidia NVSwitch is a switch fabric that enables all-to-all connectivity among multiple GPUs using NVLink links. Together, they form the backbone of Nvidia's multi-GPU systems for high-performance computing and AI workloads. As of the Blackwell architecture introduced in 2024, NVLink reached version 5.0, offering a per-link unidirectional bandwidth of 50 GB/s across 18 links per GPU, resulting in a total bidirectional interconnect bandwidth of 1.8 TB/s. The corresponding NVSwitch version 4.0 features 18 NVLink ports, with 8 ports connecting to local GPUs and 8 ports connecting to another NVSwitch chip on a different baseboard; each baseboard contains six NVSwitch chips. This evolution, building on the initial NVLink introduction in the Pascal architecture, significantly improves GPU communication efficiency.

## Key Claims

- NVLink version 5.0 provides 50 GB/s per-link unidirectional bandwidth.
- Each GPU supported by NVLink 5.0 has 18 NVLink links, yielding 1.8 TB/s total bidirectional bandwidth.
- NVSwitch version 4.0 integrates 18 NVLink ports, with 8 ports for GPU attachment and 8 for cross-switch connectivity on separate baseboards.
- Each baseboard houses six NVSwitch chips.
- The NVLink and NVSwitch technologies address the need for high-speed, low-latency point-to-point and point-to-multipoint communication in multi-GPU systems.

## Relationships

No specific relationship to visible context pages in the current wiki.

## Sources

- [Understanding Nvidia's NvLink and NvSwitch Evolution... - fibermall.com](raw/cache/191e6ce867a48d35.md)
