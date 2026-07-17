---
canonical_name: AMDGPU Kernel Optimization Guide
aliases:
- AMDGPU kernel optimization guide
- amdgpu_kernel_optimization_guide
- AMDGPU Optimization Guide
subtype: null
scorecard:
  novelty_delta: 0.7
  claim_density: 0.8
  self_containedness: 0.9
  bridge_score: 0.6
  hub_potential: 0.5
sources:
- raw/cache/158e699791e4f788.md
- https://github.com/nod-ai/amd-shark-ai/blob/main/docs/amdgpu_kernel_optimization_guide.md
source_url: https://github.com/nod-ai/amd-shark-ai/blob/main/docs/amdgpu_kernel_optimization_guide.md
fetched_at: '2026-07-17T10:51:37.829488+00:00'
type: entity
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 0
---

# AMDGPU Kernel Optimization Guide

The AMDGPU Kernel Optimization Guide is a technical document authored by Jakub Kuderski as part of the nod-ai/amd-shark-ai project, summarizing the AMDGPU microarchitecture and interleaving actionable optimization tips for kernel code generation in IREE and Turbine Kernels. It covers the GFX9 line including MI300X (CDNA3) and MI355X (CDNA4) architectures, detailing compute topology, memory bandwidth, cache hierarchy, and programming practices to achieve near-peak performance. The guide references official AMD CDNA3 and CDNA4 whitepapers and is updated as of August 2025. It also provides a glossary mapping Vulkan, CUDA, and AMDGPU terminology for clarity.

## Key Claims

- The MI300X GPU consists of 8 XCD chiplets, each with 4 Shader Engines containing 38 Compute Units (CUs), for a total of 304 CUs.
- Each CU contains 4 16-lane-wide SIMDs.
- MI300X features 8 stacks of HBM3 memory with a 8192-bit interface, achieving a theoretical peak bandwidth of 5.2 TB/s.
- MI300X cache hierarchy: L1D 32 kB (write-through), L1I 64 kB, L2 4 MB (writeback/allocate, coherent within XCD), LLC 256 MB (MALL, non-coherent).
- L2 cache is flushed between kernel launches; memory accesses missing L2 are coalesced and go to the data fabric.
- MI355X (CDNA4) has 8 XCDs, 256 active CUs, 8 stacks of HBM3E memory with theoretical peak bandwidth of 8 TB/s.
- MI355X cache hierarchy keeps L1 and MALL mostly unchanged from CDNA3, with coherency optimizations to L2.
- Optimization tip: launch workgroups in multiples of the number of CUs to fully utilize the GPU.
- Optimization tip: to achieve near-peak memory bandwidth, kernel code must engage all 4 IODs.

## Relationships

- Provides detailed compute topology and memory hierarchy specifics for the [[amd_gpu_architecture]] GFX9 family, offering kernel-level optimization recommendations based on that architecture.
- References the Matrix Core capability of [[amd_matrix_cores]] in CDNA3 and CDNA4, and discusses workgroup sizing and memory bandwidth considerations that affect matrix multiplication kernel performance.

## Sources

- [amd-shark-ai/docs/amdgpu_kernel_optimization_guide ... - GitHub](raw/cache/158e699791e4f788.md)
