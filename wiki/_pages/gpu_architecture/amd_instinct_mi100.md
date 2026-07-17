---
canonical_name: AMD Instinct MI100
aliases:
- MI100
- AMD MI100
- Instinct MI100
subtype: null
hardware_targets:
- AMD CDNA
- AMD Instinct MI100
workloads:
- HPC
- AI training
- AI inference
- scientific computing
datatypes:
- FP64
- FP32
- FP16
- bFloat16
- Int8
- Int4
metrics:
- TFLOPS
- memory bandwidth
- compute units
- clock speed
toolchains:
- ROCm
- HIP
- PyTorch
- TensorFlow
constraints:
- Infinity Fabric links
- PCIe Gen 4.0
- HBM2 memory capacity
- peer-to-peer bandwidth
tags: []
sources:
- raw/cache/1929ad5e1a13e287.md
- https://www.amd.com/en/newsroom/press-releases/2020-11-16-amd-announces-world-s-fastest-hpc-accelerator-for-.html
- raw/cache/f7472333b4a951ee.md
- https://www.tweaktown.com/news/76275/amd-instinct-mi100-announced-fastest-hpc-gpu-in-the-world/index.html
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 0
scorecard:
  novelty_delta: 0.9
  claim_density: 0.9
  self_containedness: 0.9
  bridge_score: 0.6
  hub_potential: 0.3
source_url: https://www.amd.com/en/newsroom/press-releases/2020-11-16-amd-announces-world-s-fastest-hpc-accelerator-for-.html
fetched_at: '2026-07-17T11:04:16.425143+00:00'
type: gpu_architecture
---

# AMD Instinct MI100

The AMD Instinct MI100 is a high-performance computing (HPC) graphics processing unit (GPU) accelerator announced by AMD on November 16, 2020. Built on the new AMD CDNA architecture, it was positioned as the world's fastest HPC GPU at launch, being the first x86 server GPU to exceed 10 teraflops of double-precision (FP64) performance. The MI100 offers up to 11.5 TFLOPS peak FP64, 23.1 TFLOPS peak FP32, and 46.1 TFLOPS peak FP32 Matrix performance for AI and machine learning workloads. It features 32 GB of HBM2 ECC memory with 1.23 TB/s bandwidth, supported by second-generation AMD Infinity Fabric technology providing up to 340 GB/s of aggregate peer-to-peer I/O bandwidth per card via three Infinity Fabric links. The accelerator includes new AMD Matrix Core technology for mixed-precision matrix operations, delivering a nearly 7x boost in FP16 peak floating-point performance compared to prior-generation AMD accelerators. The MI100 is supported by the ROCm 4.0 open software platform, which includes compilers, programming APIs, and libraries optimized for exascale computing, with unified support for OpenMP 5.0 and HIP, and optimizations for PyTorch and TensorFlow frameworks. Systems featuring the MI100 are expected from OEM partners including Dell, Gigabyte, HPE, and Supermicro by end of 2020.

## Key Claims

- Delivers industry-leading 11.5 TFLOPS peak FP64 performance and 23.1 TFLOPS peak FP32 performance for HPC workloads.
- Achieves up to 46.1 TFLOPS peak FP32 Matrix performance for AI and machine learning workloads.
- Provides a nearly 7x boost in FP16 theoretical peak floating point performance for AI training compared to AMD's prior generation accelerators.
- Features 32 GB of HBM2 ECC memory at 1.2 GHz, delivering 1.23 TB/s memory bandwidth.
- Supports peer-to-peer I/O bandwidth of up to 340 GB/s per card via three AMD Infinity Fabric links, enabling up to two fully-connected quad GPU hives with 552 GB/s P2P I/O.
- Includes PCIe Gen 4.0 support providing up to 64 GB/s peak theoretical transport data bandwidth from CPU to GPU.
- Introduces AMD Matrix Core technology supporting FP32, FP16, bFloat16, Int8, and Int4 matrix operations.
- Supported by ROCm 4.0 open source platform with compiler upgrades for OpenMP 5.0 and HIP, and performance optimizations for PyTorch and TensorFlow.

## Relationships

- The AMD Instinct MI100 is a specific product implementation based on the [[amd_gpu_architecture]]'s AMD CDNA architecture. It shares the hierarchical compute unit organization, shader engine design, and the ROCm software stack described in that page.
- The MI100 incorporates [[amd_matrix_cores]] for accelerating mixed-precision matrix operations. The Matrix Cores in the MI100 support FP32, FP16, bFloat16, Int8, and Int4 data types, providing up to 46.1 TFLOPS peak FP32 Matrix performance, which is a concrete instantiation of the Matrix Core design.

## Sources

- [AMD Announces World’s Fastest HPC Accelerator for Scientific...](raw/cache/1929ad5e1a13e287.md)
