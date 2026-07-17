---
canonical_name: Intel Clearwater Forest
aliases:
- Clearwater Forest Xeon
- Intel Xeon Clearwater Forest
- Clearwater Forest
subtype: null
hardware_targets:
- Intel Clearwater Forest
workloads:
- high-density scale-out workloads
- cloud computing
datatypes: []
metrics:
- IPC (17% increase in SpecIntRate'17)
- memory bandwidth (up to 1300 GB/s dual-socket)
- L2 cache bandwidth (400 GB/s per cluster)
- core count (288 Darkmont cores)
- L2 cache size (288 MB total)
- LLC size (576 MB)
toolchains: []
constraints:
- Intel 18A process node
- Foveros Direct 3D packaging
- EMIB interconnect
- 12-channel DDR5-8000 memory
- PCIe Gen5 (2 x 96 lanes)
- CXL 64 lanes
- UPI (576 GB/s)
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.9
  self_containedness: 0.9
  bridge_score: 0.2
  hub_potential: 0.6
sources:
- raw/cache/d0e9f2a25d381066.md
- https://wccftech.com/intel-clearwater-forest-e-core-xeon-cpu-12-cpu-chiplets-18a-node-288-darkmont-cores-17-ipc-increase-2x-l2-cache-bandwidth-ddr5-8000-support/
- raw/cache/c1eec18a570c53bb.md
- https://www.servethehome.com/intel-clearwater-forest-is-set-to-be-a-tech-breakthrough-server-chip/
source_url: https://wccftech.com/intel-clearwater-forest-e-core-xeon-cpu-12-cpu-chiplets-18a-node-288-darkmont-cores-17-ipc-increase-2x-l2-cache-bandwidth-ddr5-8000-support/
fetched_at: '2026-07-17T11:36:58.900914+00:00'
type: processor_architecture
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 0
---

# Intel Clearwater Forest

Intel Clearwater Forest is a next-generation Xeon server CPU family built on the Intel 18A process node, featuring up to 288 Darkmont efficiency cores (E-cores) across 12 compute chiplets. Designed for high-density, scale-out workloads in cloud and enterprise datacenters, Clearwater Forest introduces a modular architecture with 4 MB of unified L2 cache per four-core cluster, a claimed 17% IPC increase over prior E-core designs (Sierra Glen), and support for 12-channel DDR5-8000 memory delivering up to 1300 GB/s bandwidth in a dual-socket configuration. The CPU leverages Intel's Foveros Direct 3D packaging technology and EMIB interconnects to integrate compute chiplets on a base tile with shared last-level cache (LLC) and I/O, while the monolithic mesh coherent fabric provides up to 35 GB/s per cluster interconnect bandwidth.

## Key Claims

- Fabricated on Intel's 18A process node with backside power delivery and gate-all-around transistors, improving core logic power efficiency and reducing power delivery losses by 4-5%.
- Contains 12 E-core compute chiplets (Intel 18A), 3 base tile packages (Intel 3), and 2 I/O chiplets (Intel 7), interconnected via EMIB.
- Darkmont E-core architecture includes a smarter front-end with 64 kB instruction cache and three 3-wide decoders providing nine decodes per cycle (50% more instruction bandwidth), a deeper out-of-order engine with 8-wide allocation (60% increase) and 16-wide retire (2x increase), and 26 execution ports (50% increase).
- Integer and vector execution units are 2x wider, with load address generation at 1.5x and store address generation at 2x.
- L1 data cache with ECC, data poisoning support, recoverable machine check, and 52 physical address bits.
- Each four-core cluster shares 4 MB of unified L2 cache with 17-cycle latency, providing up to 400 GB/s bandwidth per cluster.
- IPC improvement of 17% measured on SpecIntRate'17.
- Supports 12-channel DDR5-8000 memory with up to 3 TB capacity per socket in dual-socket (2S) server configurations.
- 2 x 96 PCIe Gen5 lanes, 64 CXL lanes, 144 UPI lanes (576 GB/s).
- Total 288 cores with 576 MB of LLC across 72 quad-core clusters.

## Relationships

No specific relationship to visible context pages in the current wiki.

## Sources

- [Intel's Next-Gen Clearwater Forest "E-Core" Xeon CPU Unveiled: 12...](raw/cache/d0e9f2a25d381066.md)
