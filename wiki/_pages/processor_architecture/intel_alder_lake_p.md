---
canonical_name: Intel Alder Lake P
aliases:
- 12th Gen Intel Core mobile processors for IoT
- Alder Lake-P
subtype: null
hardware_targets:
- Alder Lake P processor
workloads:
- AI inference
- GPU image classification inference
- 3D graphics
- multithreaded computing
- single-threaded computing
datatypes: []
metrics:
- single-thread performance (1.07x vs 11th Gen)
- multithread performance (1.29x)
- 3D graphics performance (2.47x)
- GPU image classification inference performance (2.77x)
- power (15W-45W base power)
- cores (up to 14)
- threads (up to 20)
- GPU execution units (up to 96)
- memory bandwidth (DDR5 4800, LPDDR5-5200)
toolchains:
- Intel Deep Learning Boost (Intel DL Boost)
- Intel Distribution of OpenVINO toolkit
constraints:
- BGA package
- IoT applications
- Thunderbolt 4/USB4
- PCIe Gen4
evidence_strength: reported
scorecard:
  novelty_delta: 0.9
  claim_density: 0.7
  self_containedness: 0.9
  bridge_score: 0.2
  hub_potential: 0.2
sources:
- raw/cache/37e72486a1647d3d.md
- https://www.intel.com/content/www/us/en/products/platforms/details/alder-lake-p.html
source_url: https://www.intel.com/content/www/us/en/products/platforms/details/alder-lake-p.html
fetched_at: '2026-07-17T12:55:19.528788+00:00'
type: processor_architecture
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 0
---

# Intel Alder Lake P

Intel Alder Lake P is a 12th Gen Intel Core mobile processor family designed for IoT applications, released as part of the Alder Lake microarchitecture. It is Intel's first Core processor line to feature a performance hybrid architecture combining Performance-cores (P-cores) and Efficient-cores (E-cores), managed by Intel Thread Director for optimized workload scheduling. The platform integrates up to 14 cores and 20 threads in IoT SKUs, with a processor base power range of 15W to 45W, targeting small form-factor embedded and edge computing devices. Graphics are handled by up to 96 execution units based on the Intel Iris Xe Graphics architecture, supporting up to four concurrent 4K60 HDR displays or a single 8K display. AI acceleration is provided via Intel Deep Learning Boost (VNNI instructions on the CPU) and the Intel Distribution of OpenVINO toolkit, enabling up to 2.77x faster GPU image classification inference compared to the 11th Gen. Memory support includes DDR5-4800 and LPDDR5-5200, with multiple PCIe Gen4 lanes and Thunderbolt 4/USB4 for high-bandwidth connectivity.

## Key Claims

- Alder Lake P is the first Intel Core processor family to feature a performance hybrid architecture with P-cores and E-cores.
- Intel Thread Director optimizes embedded workloads by dynamically assigning tasks to the appropriate core type.
- Up to 14 cores and 20 threads in IoT SKUs.
- Processor base power ranges from 15W to 45W.
- Up to 96 GPU execution units based on Intel Iris Xe Graphics architecture.
- Up to 2.47x faster 3D graphics performance vs. 11th Gen Intel Core processors.
- Up to 2.77x faster GPU image classification inference performance vs. 11th Gen.
- Up to 1.07x single-thread and 1.29x multithread performance gains vs. 11th Gen.
- Supports DDR5-4800 and LPDDR5-5200 memory.
- Supports PCIe Gen4 and Thunderbolt 4/USB4 for connectivity.
- AI acceleration via Intel DL Boost (VNNI) and OpenVINO toolkit.
- Up to four concurrent 4K60 HDR displays or one 8K display.

## Relationships

No specific relationship to visible context pages in the current wiki.

## Sources

- [Alder Lake P: Overview and Technical Documentation - Intel](raw/cache/37e72486a1647d3d.md)
