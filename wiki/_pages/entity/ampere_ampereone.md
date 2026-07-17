---
canonical_name: Ampere AmpereOne
aliases:
- AmpereOne
- AmpereOne A192
- AmpereOne A192-32X
- AmpereOne 2023
subtype: null
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.6
  self_containedness: 0.3
  bridge_score: 0.5
  hub_potential: 0.3
sources:
- raw/cache/a6dfd89980c119d5.md
- https://www.servethehome.com/ampere-ampereone-at-hot-chips-2024-arm/
- raw/cache/ab28ab896b759639.md
- https://www.servethehome.com/ampereone-with-192-cores-128x-pcie-gen5-lanes-and-ddr5-in-2023-arm/
source_url: https://www.servethehome.com/ampere-ampereone-at-hot-chips-2024-arm/
fetched_at: '2026-07-17T09:39:27.996613+00:00'
type: entity
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 0
outbound_links:
- target: amd_cdna
  reason: Ampere AmpereOne competes with AMD CDNA-based Instinct accelerators in the
    data center AI inference market, though AmpereOne uses a general-purpose Arm CPU
    approach rather than a dedicated GPU accelerator
---

# Ampere AmpereOne

Ampere AmpereOne is an Arm-based server processor architecture designed by Ampere Computing, first publicly detailed at Hot Chips 2024. It features up to 192 custom Arm cores manufactured on a TSMC 5nm process, with a chiplet design that separates compute, memory (MCU), and PCIe I/O dies. Each core includes a private 2MB L2 cache, and 64 distributed coherency engines each provide 1MB of L3 cache, totaling 64MB of shared L3. Memory support scales to 12-channel DDR5 via the memory controller die, and up to 128 PCIe Gen5 lanes are available through four PCIe I/O dies. The core employs a new branch prediction engine, eight schedulers feeding twelve execution pipelines, and universal TLBs. Memory tagging is built in for security and debugging, and adaptive traffic management minimizes noisy neighbor effects in cloud environments. AmpereOne targets cloud workloads, including AI inference, and supports common AI frameworks out of the box.

## Key Claims

- Current generation supports up to 192 cores with 8-channel DDR5; a 12-channel DDR5 192-core part on 5nm is expected to ship the following quarter (as of Hot Chips 2024).
- A 256-core 3nm part is planned for next year.
- Core microarchitecture: new branch prediction engine, eight schedulers, twelve execution pipelines, no separate TLB classes (all entries universal).
- Private 2MB L2 caches per core to ensure tenant isolation in cloud deployments; no conventional large L3, but 64MB distributed L3 via 64 coherency engines (1MB each).
- Compute chiplet built on TSMC 5nm, each core cluster contains four custom cores.
- Die-to-die interconnect achieves up to 2.8 TB/s bandwidth.
- PCIe I/O dies on TSMC 7nm, each providing 32 lanes of PCIe Gen5; four dies per package deliver 128 lanes.
- Memory controllers on TSMC 7nm support up to 12-channel DDR5.
- Memory tagging helps find software errors and mitigate buffer overflow attacks.
- Adaptive traffic management on the SoC reduces noisy neighbor effects.
- Supports AI inference with common frameworks; performance figures were shown but not detailed in the source.

## Relationships

- [[amd_cdna]]: Ampere AmpereOne competes with AMD CDNA-based Instinct accelerators in the data center AI inference market, though AmpereOne uses a general-purpose Arm CPU approach rather than a dedicated GPU accelerator.

## Sources

- [Ampere AmpereOne Architecture at Hot Chips 2024 - ServeTheHome](raw/cache/a6dfd89980c119d5.md)
