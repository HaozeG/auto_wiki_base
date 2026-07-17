---
canonical_name: AMD Instinct MI300 Series
aliases:
- MI300
- MI300A
- MI300X
- Instinct MI300
- AMD Instinct MI300X
- AMD MI300X
- AMD Instinct MI300X Accelerator
- AMD Instinct MI300
- AMD MI300
- AMD Instinct MI300 series
subtype: null
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.9
  self_containedness: 0.8
  bridge_score: 0.5
  hub_potential: 0.4
sources:
- raw/cache/8099b1af2a641a0e.md
- https://rocm.docs.amd.com/en/latest/conceptual/gpu-arch/mi300.html
- raw/cache/1ec3cc01f6df4500.md
- https://www.amd.com/en/products/accelerators/instinct/mi300/mi300x.html
- raw/cache/c88d1a5781afbd79.md
- https://wccftech.com/amd-unveils-instinct-mi300-apus-mi300a-mi300x-flavors-cdna-3-gpu-up-to-24-zen-4-cores-192-gb-hbm3-153-billion-transistors/
source_url: https://rocm.docs.amd.com/en/latest/conceptual/gpu-arch/mi300.html
fetched_at: '2026-07-17T09:44:48.838472+00:00'
type: entity
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 0
---

# AMD Instinct MI300 Series

The AMD Instinct MI300 Series is a family of GPU accelerators designed by AMD, based on the CDNA 3 architecture, targeted at high-performance computing (HPC), artificial intelligence (AI), and machine learning (ML) workloads. It introduces the Accelerator Complex Die (XCD), a smaller building block containing 40 compute units (CUs)—38 active and 2 disabled for yield management—with a shared 4 MB L2 cache that coalesces all memory traffic for the die. The series integrates up to 8 vertically stacked XCDs, 8 stacks of High-Bandwidth Memory 3 (HBM3) with a theoretical aggregated peak memory bandwidth of 5.3 TB/s, and 4 I/O dies connected via AMD Infinity Fabric technology. Two variants exist: the MI300X, an accelerator with 8 XCDs providing up to 304 CUs, and the MI300A, an APU combining 6 XCDs with 3 CPU chiplet dies (CCDs). At the node level, up to 8 MI300X OAM modules can be fully interconnected via seven high-bandwidth, low-latency Infinity Fabric links per GPU, forming a scalable GPU cluster with optional PCIe Gen 5 host attachment.

## Key Claims

- The MI300 Series is based on the AMD CDNA 3 architecture designed for leadership performance in HPC, AI, and ML workloads, running on systems from individual servers to exascale supercomputers.
- The XCD contains 40 CUs (38 active) and a 4 MB L2 cache, with less than half the CUs of the MI200 series compute die but using advanced packaging to include 6 or 8 XCDs per package.
- CDNA 3 Matrix Cores triple FP16 and BF16 throughput, achieve a 6.8× performance gain for INT8, and a 16× gain for FP8 compared to FP32, and a 4× gain for TF32 compared to FP32, all relative to the MI250X GPUs.
- Peak theoretical performance for the MI300X OAM is 163.4 TFLOPS for Matrix FP64, 81.7 TFLOPS for Vector FP64, 653.7 TFLOPS for Vector TF32, 1307.4 TFLOPS for Matrix FP16/BF16, and 2614.9 TFLOPS for Matrix FP8/INT8.
- The theoretical aggregated peak memory bandwidth of the GPU is 5.3 TB per second using HBM3.
- The MI300X OAM attaches to the host system via PCIe Gen 5 x16 links, and GPUs are fully interconnected via seven high-bandwidth, low-latency AMD Infinity Fabric links forming a 8-GPU system.

## Relationships

- The MI300 Series is the first product implementation of [[amd_cdna]] generation 3 (CDNA 3), inheriting the compute-unit design and matrix core improvements while introducing the XCD chiplet packaging and the APU variant (MI300A) that integrates CPU chiplets via Infinity Fabric.

## Sources

- [AMD Instinct™ MI300 Series microarchitecture](raw/cache/8099b1af2a641a0e.md)
