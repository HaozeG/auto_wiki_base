---
canonical_name: Alchemist Xe-HPG
aliases:
- Alchemist
- Intel Xe-HPG
- Intel Arc Alchemist
subtype: null
hardware_targets:
- Alchemist
workloads:
- gaming
- ray tracing
- AI upscaling (XeSS)
datatypes:
- INT8 (DP4a, XMX)
- FP16
metrics:
- performance per watt (1.5× vs DG1)
- frequency (1.5× iso-voltage vs DG1)
- process density (N6 +18% vs N7)
toolchains:
- XeSS SDK
constraints:
- TSMC N6 process
- up to 8 render slices
- DP4a fallback for cross-vendor compatibility
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 0.7
  bridge_score: 0.6
  hub_potential: 0.7
sources:
- raw/cache/dbab3c0d1ddceccb.md
- https://silicon.redfire.dev/events/intel/architecture-day-2021/
source_url: https://silicon.redfire.dev/events/intel/architecture-day-2021/
fetched_at: '2026-07-17T12:56:19.407744+00:00'
type: gpu_architecture
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 0
outbound_links:
- target: nvidia_blackwell_ultra
  reason: Alchemist's XMX (matrix engines) serve a similar purpose to Blackwell Ultra's
    Tensor Cores, accelerating AI and matrix-heavy computations in graphics pipelines
- target: amd_gpu_architecture
  reason: Alchemist's Xe-core organization (vector engines + matrix engines into slices)
    is architecturally analogous to AMD's compute units aggregated into shader engines
---

# Alchemist Xe-HPG

Alchemist Xe-HPG is a discrete graphics microarchitecture developed by Intel, targeting the gaming and AI upscaling market. It is the first architecture in the Intel Arc GPU family, succeeding the Xe-LP integrated graphics. Alchemist is built on the TSMC N6 process node, offering 1.5× the performance-per-watt and 1.5× the frequency at iso-voltage compared to Intel's DG1 (Iris Xe MAX). The architecture is organized into Xe-cores (XC), each containing 16 vector engines (256-bit) and 16 matrix engines (1024-bit) for high-throughput compute. A render slice combines four Xe-cores, four ray tracing units, and fixed-function units; Alchemist can scale up to eight render slices with a large shared L2 cache. Key features include hardware-accelerated ray tracing and Intel Xe Super Sampling (XeSS), an AI-based upscaling technique that can use Xe Matrix Extensions (XMX) or fall back to DP4a INT8 operations for cross-vendor compatibility.

## Key Claims

- 1.5× performance-per-watt and 1.5× frequency at iso-voltage versus DG1.
- Built on TSMC N6 process (+18% density over N7).
- Each Xe-core has 16 vector engines (256b) and 16 matrix engines (1024b).
- Render slice: 4 Xe-cores, 4 RT units, fixed-function units.
- Up to 8 render slices per Alchemist GPU.
- XeSS upscaling: uses XMX (Xe Matrix Extensions) for optimal performance, or DP4a (INT8 packing) for compatibility with non-Intel GPUs.
- XeSS DP4a adds ~2.5× latency compared to XMX.
- Future architectures: Battlemage, Celestial, Druid.

## Relationships

- [[nvidia_blackwell_ultra]]: Alchemist's XMX (matrix engines) serve a similar purpose to Blackwell Ultra's Tensor Cores, accelerating AI and matrix-heavy computations in graphics pipelines.
- [[amd_gpu_architecture]]: Alchemist's Xe-core organization (vector engines + matrix engines into slices) is architecturally analogous to AMD's compute units aggregated into shader engines.

## Sources

- [Intel Architecture Day 2021 - Silicon](raw/cache/dbab3c0d1ddceccb.md)
