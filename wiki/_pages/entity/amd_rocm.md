---
canonical_name: AMD ROCm
aliases:
- ROCm
- ROCm open software platform
- AMD ROCm LLM Inference Optimization
- AMD ROCm LLM Inference
- ROCm LLM Inference
- Radeon Open Compute
- ROCm software stack
subtype: null
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.2
  self_containedness: 0.7
  bridge_score: 0.6
  hub_potential: 0.3
sources:
- raw/cache/18f0c08b582fb9e3.md
- https://rocm.docs.amd.com/
- raw/cache/a5b087e1be2d14bc.md
- https://wiki.gentoo.org/wiki/ROCm
- raw/cache/8aeaea8865feedd7.md
- https://github.com/MayurVijayPatil/amd-llm-rocm
- raw/cache/ecb24386768e9cbe.md
- https://www.amd.com/en/products/software/rocm.html
source_url: https://rocm.docs.amd.com/
fetched_at: '2026-07-17T09:28:20.706557+00:00'
type: entity
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 0
---

# AMD ROCm

AMD ROCm (Radeon Open Compute) is AMD's open-source GPU computing platform providing an end-to-end ecosystem of compilers, runtimes, and libraries for artificial intelligence, high-performance computing, and domain-specific workloads. It supports Linux and Windows operating systems and is optimized for AMD Instinct, AMD Radeon, and AMD Ryzen AI devices. The platform includes a Core SDK with math libraries, communication primitives, HIP runtime, and profiling and debugging tools. It also offers an AI ecosystem with deep learning frameworks such as PyTorch and JAX and inference engines like vLLM and SGLang. GPU systems and infrastructure documentation covers driver installation, cluster management, GPU partitioning, monitoring, virtualization, cloud deployments, and containers. Additionally, ROCm provides specialized toolkits for data science, finance, life science, LLM extensions, and simulation.

## Key Claims

- ROCm is an open-source GPU computing platform.
- It is cross-platform, supporting Linux and Windows.
- It is optimized for AMD Instinct, AMD Radeon, and AMD Ryzen AI devices.
- The Core SDK includes math libraries, HIP runtime, communication primitives, and debugging tools.
- The AI ecosystem supports PyTorch, JAX, vLLM, and SGLang.
- GPU systems infrastructure documentation covers driver installation, cluster management, GPU partitioning, monitoring, virtualization, cloud deployments, and containers.
- Domain-specific toolkits are available for data science, finance, life science, LLM extensions, and simulation.

## Relationships

- ROCm provides the software runtime and libraries that enable AI and HPC workloads on AMD Instinct accelerators, which are built on the [[amd_cdna]] microarchitecture.

## Sources

- [AMD ROCm — AMD ROCm 7.14.0](raw/cache/18f0c08b582fb9e3.md)
