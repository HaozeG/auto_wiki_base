---
canonical_name: AMD GPU Architecture
aliases:
- AMD GPU hardware implementation
- AMD GPU microarchitecture
subtype: null
hardware_targets:
- AMD CDNA
- AMD RDNA
workloads:
- parallel computing
- data-parallel workloads
- GPU compute
datatypes: []
metrics:
- latency
- throughput
- bandwidth
toolchains:
- ROCm
- HIP
constraints: []
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 0.8
  bridge_score: 0.7
  hub_potential: 0.8
sources:
- raw/cache/3335f370ecc08017.md
- https://rocm.docs.amd.com/projects/HIP/en/develop/understand/hardware_implementation.html
source_url: https://rocm.docs.amd.com/projects/HIP/en/develop/understand/hardware_implementation.html
fetched_at: '2026-07-17T10:50:54.716747+00:00'
type: gpu_architecture
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 4
---

# AMD GPU Architecture

The AMD GPU architecture, as supported by the HIP programming model, is a hierarchical parallel computing design that dedicates the majority of die area to arithmetic pipelines to achieve extreme throughput density for data-parallel workloads. Unlike CPUs, GPUs minimize silicon for instruction flow control and caching to maximize the number of arithmetic operations per clock cycle. The architecture is organized into a three-level hierarchy: shader engines (SEs) as top-level units, each containing multiple shader arrays, which in turn group compute units (CUs) — the fundamental execution blocks capable of managing thousands of concurrent threads organized into warps of 32 (RDNA) or 64 (CDNA) threads. The command processor (CP) serves as the primary interface between the CPU and GPU, consisting of the command processor fetcher (CPF) and the command processor packet processor (CPC). Asynchronous compute engines (ACEs) break kernels into workgroups and dispatch them to the workgroup managers (SPI) within each shader engine, which schedule workgroups onto available CUs while tracking resource limits such as warp slots, vector registers, and local data share memory. This design enables latency hiding through massive hardware multithreading and concurrent kernel execution.

## Key Claims

- The command processor (CP) contains two components: CPF (fetches commands from memory) and CPC (decodes and dispatches kernels to ACEs).
- Asynchronous compute engines (ACEs) break kernels into workgroups and distribute them to shader processor input (SPI) blocks; multiple ACEs enable concurrent kernel execution.
- Most GPUs contain two DMA engines for concurrent bidirectional memory transfers over PCIe, but each engine cannot handle multiple copy commands simultaneously.
- The GPU organization is hierarchical: shader engines (SEs) contain shader arrays, which contain compute units (CUs).
- Each shader engine contains a workgroup manager (SPI), scalar L1 data cache (sL1D), and L1 instruction cache (L1I) shared across its compute units.
- The SPI schedules workgroups onto CUs and tracks four critical resources: warp slots, VGPRs, SGPRs, and LDS memory.
- Compute units (CUs) are the fundamental execution units; each CU manages warps of 32 threads (RDNA) or 64 threads (CDNA) and uses massive multithreading to hide memory latency.
- Workgroup-to-CU mapping is non-deterministic and based on available resources; the same kernel launch may have different workgroup distributions.

## Relationships

- The AMD CDNA architecture described in this page contains Matrix Cores ([[amd_matrix_cores]]) as specialized units within compute units for accelerating matrix multiplication workloads, which are programmed via HIP intrinsic functions.

## Sources

- [Hardware implementation — HIP 7.15.0 Documentation](raw/cache/3335f370ecc08017.md)
