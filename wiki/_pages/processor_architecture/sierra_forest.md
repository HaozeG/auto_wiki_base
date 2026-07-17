---
canonical_name: Sierra Forest
aliases:
- SRF
- Xeon 6 (Sierra Forest)
- Intel Sierra Forest
- Sierra Forest Xeon
- Sierra Forest (Crestmont E-cores)
- Intel Xeon (Sierra Forest and Granite Rapids)
- Granite Rapids
- Emerald Rapids
- Intel Xeon 6700E Sierra Forest
- Intel Xeon 6 Sierra Forest
- Xeon 6780E
- Xeon 6700E
subtype: null
hardware_targets:
- Sierra Forest (Crestmont E-cores)
workloads:
- cloud server
- heavily multi-threaded workloads
datatypes: []
metrics:
- core count (up to 288)
- peak clock speed (3.2 GHz)
- memory channels (8 or 12 with Sierra Forest-AP)
toolchains: []
constraints:
- Intel 3 fabrication process
- LGA 4710 socket
- LGA 7529 socket
- PCIe 5.0 (88 lanes)
- CXL 2.0
- DDR5 memory
- DMI 4.0
scorecard:
  novelty_delta: 0.8
  claim_density: 0.8
  self_containedness: 0.9
  bridge_score: 0.3
  hub_potential: 0.2
sources:
- raw/cache/2d8c35938e7c7c6b.md
- https://en.wikipedia.org/wiki/Sierra_Forest
- raw/cache/9adf13f4e7d491af.md
- https://wccftech.com/intel-next-gen-xeon-cpus-2024-granite-rapids-redwood-cove-p-cores-sierra-forest-sierra-glen-e-cores/
- raw/cache/2d7c6f8579aeaa96.md
- https://www.techbloat.com/hot-chips-2023-intel-granite-rapids-and-sierra-forest-xeons.html
- raw/cache/1c0c0c2be8cd6488.md
- https://www.techpowerup.com/312952/intel-unveils-future-generation-xeon-with-robust-performance-and-efficiency-architectures
- raw/cache/0b439e7095159e2e.md
- https://wccftech.com/intel-xeon-6700e-sierra-forest-cpus-144-e-cores-330w-tdp-more-efficient-vs-amd-epyc/
source_url: https://en.wikipedia.org/wiki/Sierra_Forest
fetched_at: '2026-07-17T11:57:18.423163+00:00'
type: processor_architecture
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 0
---

# Sierra Forest

Sierra Forest is the codename for Intel's sixth-generation Xeon Scalable server processors, launched on June 4, 2024. It is the first Xeon generation to exclusively use density-optimized E-cores, specifically the Crestmont architecture, to achieve high core counts of up to 288 cores. The processors are fabricated on the Intel 3 process and target cloud server customers who prioritize core density, energy efficiency, and performance in heavily multi-threaded workloads. Sierra Forest supports up to eight DDR5 memory channels (twelve in the Sierra Forest-AP variant), PCIe 5.0 with 88 lanes, and Compute Express Link (CXL) 2.0. It is available in two socket types: LGA 4710 and LGA 7529. The instruction set includes x86-64 with extensions such as AVX, AVX2, AVX-VNNI, AVX-IFMA, FMA3, and TSX, along with virtualization and security features.

## Key Claims

- First generation of Xeon processors to exclusively feature density-optimized E-cores.
- Uses the Crestmont E-core microarchitecture.
- Offers up to 288 cores in a single processor.
- Fabricated on the Intel 3 process node.
- Supports DDR5 memory with up to 8 channels (12 channels on Sierra Forest-AP) and up to 1 TB capacity.
- Supports 88 lanes of PCI Express 5.0.
- Supports Compute Express Link (CXL) 2.0.
- Peak core clock up to 3.2 GHz.
- L1 cache: 64 KB instructions + 32 KB data per core; L2 cache: 4 MB per cluster; L3 cache: 3 MB per cluster.
- Instruction set extensions: MMX, SSE, SSE2, SSE3, SSSE3, SSE4.1, SSE4.2, AVX, AVX2, FMA3, AVX-VNNI, AVX-IFMA, TSX, VT-x, VT-d, AES-NI, SHA, RDRAND.
- Replaces the Xeon Scalable branding with the simplified Xeon 6 brand.
- Launched on June 4, 2024, with the initial Xeon 6700E series (Sierra Forest-SP) using LGA 4710.
- Targeted at cloud server customers, contrasting with P-core Xeon processors for HPC.

## Relationships

No specific relationship to visible context pages in the current wiki.

## Sources

- [Sierra Forest - Wikipedia](raw/cache/2d8c35938e7c7c6b.md)
