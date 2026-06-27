---
type: entity
tags:
  - risc-v
  - sifive
  - application-processor
  - automotive
  - hpc
  - chips
sources:
  - https://www.sifive.com/cores/performance-p870
  - https://sifive.cdn.prismic.io/sifive/P870-D_Product_Brief.pdf
created: 2026-06-27
updated: 2026-06-27
cold_start: false
inbound_links: 0
scorecard:
  novelty_delta: 0.78
  claim_density: 0.75
  self_containedness: 0.85
  bridge_score: 0.60
  hub_potential: 0.55
---

# SiFive Performance P870

The SiFive Performance P870 is SiFive's highest-performance application-class RISC-V CPU IP core, announced in 2023 and targeting automotive ADAS, HPC offload, and AI inference applications requiring RISC-V ISA compliance at ARM Cortex-X class performance. The P870 implements the RV64 ISA with a wide out-of-order superscalar pipeline (reported 13-stage, 8-wide issue) and supports the full RVA23 profile extension set including vector (RVV 1.0), hypervisor, and Svpbmt. SiFive positions the P870-D (dual-cluster variant) for deployment in 1,000-core AI arrays by stacking clusters in a scalable fabric: a single P870-D die contains two P870 clusters plus coherent memory fabric, and multiple P870-D dies can be tiled to construct NUMA manycore accelerators. The core targets 3.1 GHz at TSMC N3 (3 nm), achieving an estimated 13+ SPECint2017 score per core, placing it above ARM Cortex-X4 on integer workloads. For AI inference, the P870's 4-wide SIMD/vector unit running RVV 1.0 delivers approximately 32 GFLOPS per core at 3 GHz (FP32) or 128 GOPS (INT8 with RISC-V matrix extensions), enabling large-scale RISC-V-native AI inference without proprietary accelerator ISAs.

## Key Claims

- SiFive P870 is reported to achieve a SPEC CPU2017 integer score above 13 per core at 3.1 GHz in TSMC N3, competitive with ARM Cortex-X4 and making it the highest-performing open RISC-V CPU IP announced as of 2024.
- The P870-D package integrates two P870 clusters with a cache-coherent NoC, enabling symmetric multi-processing and NUMA configurations without external glue logic.
- SiFive's customer collateral describes 1,000-core array configurations using tiled P870-D dies for AI inference workloads, targeting data-center-class throughput with RISC-V instruction compatibility.
- P870 implements RVV 1.0 with 512-bit SIMD width, delivering 16 FP32 operations per cycle per core for matrix and convolution kernels used in transformer inference.
- The core supports the RISC-V hypervisor extension (H), enabling virtualized deployment in automotive safety partitions (ASIL-B and ASIL-D with lockstep optional variant P870-S).
- SiFive targets the P870 at automotive OEMs seeking RISC-V alternatives to ARM Cortex-A78AE for ADAS SoC designs, citing ISA longevity and open-standard governance.
- A safety-enhanced P870-S (lockstep) variant adds split-lock execution, hardware error detection, and ASIL-D compliance for functional safety use cases.

## Relationships

- [[sifive_intelligence_x280]] — The SiFive X280 is an earlier SiFive HPC-class core with 512-bit RVV; P870 succeeds it with higher IPC and N3 targeting.
- [[rva23_profile]] — P870 implements the RVA23 mandatory extension set, making it one of the first commercial RISC-V cores to fully conform to the profile.
- [[risc_v_vector_extension]] — P870's 512-bit RVV 1.0 implementation is central to its AI inference performance case.
- [[risc_v_international_foundation]] — SiFive is a founding member of RISC-V International and contributed to the RVA23 profile definition process.

## Sources

- SiFive P870 product page: https://www.sifive.com/cores/performance-p870
- SiFive P870-D Product Brief (2023)
- SiFive press release on 1000-core AI arrays (Hot Chips 2023 presentation)
- RISC-V International RVA23 profile specification
