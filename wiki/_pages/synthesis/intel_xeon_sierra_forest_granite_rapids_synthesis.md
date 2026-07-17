---
canonical_name: null
aliases: []
subtype: null
connected_entities:
- Intel Xeon Granite Rapids
- Intel Xeon Sierra Forest
synthesis_status: draft
scorecard:
  bridge_score: 0.7
  contradiction_potential: 0.0
  cross_domain_connection: null
sources:
- raw/cache/ab5e96c5f731fb9c.md
- https://umatechnology.org/hot-chips-2023-intel-granite-rapids-and-sierra-forest-xeons/
source_url: https://umatechnology.org/hot-chips-2023-intel-granite-rapids-and-sierra-forest-xeons/
fetched_at: '2026-07-17T12:24:19.260832+00:00'
type: synthesis
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 0
outbound_links:
- target: intel_xeon_granite_rapids
  reason: unlabeled
- target: intel_xeon_sierra_forest
  reason: unlabeled
---

# Intel Xeon Split: Granite Rapids and Sierra Forest

## RAG Summary

Intel's Hot Chips 2023 disclosures marked a fundamental shift in the Xeon Scalable processor roadmap: the company is splitting its next-generation data center strategy into two distinct processor lines—Granite Rapids and Sierra Forest—each optimized for different workload domains. Granite Rapids is built with high-performance P-cores and targets demanding enterprise, HPC, AI, database, and scale-up workloads. Sierra Forest, Intel's first E-core Xeon Scalable chip, is built on the Intel 3 process node with EUV lithography and targets high-density, scale-out workloads. This architectural divergence represents a departure from Intel's previous one-size-fits-all Xeon approach. Sierra Forest is the lead vehicle for Intel's EUV-based Intel 3 process, while Granite Rapids leverages a P-core design expected to deliver significant single-threaded performance. Together, Granite Rapids and Sierra Forest cover the full spectrum of server workloads from compute-intensive to throughput-optimized, giving Intel a competitive response to AMD's chiplet-based EPYC processors and Ampere's E-core designs. The two chips share a common platform, enabling system vendors to offer both in compatible socket designs.

---

## Full Synthesis

The introduction of two distinct Xeon families at Hot Chips 2023 represents Intel's recognition that modern data center workloads are diverging too far to be served by a single microarchitecture. Granite Rapids with P-cores targets traditional compute-intensive and latency-sensitive workloads such as enterprise databases, HPC simulations, and AI inference. Sierra Forest with E-cores focuses on throughput-optimized, scale-out workloads like cloud-native microservices, web serving, and content delivery. The use of Intel 3 process with EUV for Sierra Forest marks the first deployment of this advanced node in a Xeon product. Both processors are expected to ship in 2024, with Sierra Forest arriving earlier as the first E-core Xeon. The platform compatibility between the two lines reduces engineering costs for server vendors and allows customers to match processor type to workload within the same infrastructure.

## Open Questions

- What are the exact core counts and frequencies for Granite Rapids and Sierra Forest?
- How does the performance of Sierra Forest's E-cores compare to prior Xeon efficiency cores?
- What memory and I/O configurations are supported (e.g., DDR5, PCIe Gen5, CXL)?
- Are there any shared cache hierarchies or mesh topology details?

## Connected Pages

- [[intel_xeon_granite_rapids]]
- [[intel_xeon_sierra_forest]]

## Sources

- [Hot Chips 2023: Intel Granite Rapids and Sierra Forest Xeons](raw/cache/ab5e96c5f731fb9c.md)
