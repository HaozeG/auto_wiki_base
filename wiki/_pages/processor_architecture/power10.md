---
canonical_name: Power10
aliases:
- P10
- IBM Power10
subtype: null
hardware_targets:
- Power10
workloads:
- general-purpose computing
- AI inference
datatypes: []
metrics:
- clock speed
- power efficiency
- bandwidth
- latency
toolchains:
- Linux
- PowerVM
constraints:
- Power ISA v.3.1
- 7 nm Samsung
evidence_strength: reported
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.9
  self_containedness: 1.0
  bridge_score: 0.4
  hub_potential: 0.5
sources:
- raw/cache/095f234d853014b9.md
- https://en.m.wikipedia.org/wiki/Power10
source_url: https://en.m.wikipedia.org/wiki/Power10
fetched_at: '2026-07-17T13:06:21.185626+00:00'
type: processor_architecture
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 0
outbound_links:
- target: alphawave_semi_hbm_subsystem
  reason: Power10 supports HBM memory for high-bandwidth workloads, similar to the
    Alphawave Semi HBM Subsystem which provides a JEDEC-compliant HBM interface IP,
    both targeting memory-intensive computing but at different integration levels
    (processor-integrated vs. standalone IP)
- target: meta_vistara_cxl_bridge
  reason: Power10's Open Memory Interface (OMI) enables flexible memory configurations
    using serial memory communications, aligning with the memory flexibility goal
    of Meta's Vistara CXL bridge, though OMI is a processor-side interface and Vistara
    is a separate bridge chip for DDR4 reuse
---

# Power10

Power10 is a superscalar, multi-threading, multi-core microprocessor family based on the open source Power ISA, announced in August 2020 at Hot Chips and available from September 2021. Designed by IBM and manufactured by Samsung using a 7 nm process, the chip features 15 SMT8 cores (with one spare for yield) and up to 30 SMT4 cores in multi-chip configurations, with a die size of 602 mm² and 18 billion transistors. Power10 emphasizes higher performance per watt, improved memory and I/O architectures, and artificial intelligence (AI) workloads, supported by matrix math assist (MMA) engines that deliver a twenty-fold performance increase for AI inference compared to its predecessor POWER9. The processor supports a wide range of memory types including DDR4, DDR5, GDDR, and HBM, and introduces the Open Memory Interface (OMI) and Open Coherent Accelerator Processor Interface (OpenCAPI) for flexible system design.

## Key Claims

- 15 SMT8 cores (one spare for yield), also configurable as 30 SMT4 cores in multi-chip modules.
- Fabricated on Samsung 7 nm process with 18 billion transistors on a 602 mm² die.
- L1 cache: 48 KB instruction + 32 KB data per core; L2 cache: 2 MB per core; L3 cache: 120 MB per chip (128 MB with 16 cores, reduced by 8 MB when one core is disabled).
- Maximum clock frequency: 3.5 GHz to 4 GHz.
- DDR4 memory: up to 16 TiB, 410 GB/s bandwidth, 10 ns latency; GDDR6: up to 800 GB/s.
- 2.6× better performance per watt than POWER9.
- AI inference performance improvement of 20× thanks to four matrix math assist (MMA) engines per core.
- Each core is SMT8 capable, providing 120 logical cores per single-chip module (15 cores × 8 threads) and 240 threads per dual-chip socket.
- Eight crypto accelerators offloading AES and SHA-3.
- Supports OpenCAPI and OMI for flexible memory and I/O architectures.

## Relationships

- [[alphawave_semi_hbm_subsystem]]: Power10 supports HBM memory for high-bandwidth workloads, similar to the Alphawave Semi HBM Subsystem which provides a JEDEC-compliant HBM interface IP, both targeting memory-intensive computing but at different integration levels (processor-integrated vs. standalone IP).
- [[meta_vistara_cxl_bridge]]: Power10's Open Memory Interface (OMI) enables flexible memory configurations using serial memory communications, aligning with the memory flexibility goal of Meta's Vistara CXL bridge, though OMI is a processor-side interface and Vistara is a separate bridge chip for DDR4 reuse.

## Sources

- [Power10 - Wikipedia](raw/cache/095f234d853014b9.md)
