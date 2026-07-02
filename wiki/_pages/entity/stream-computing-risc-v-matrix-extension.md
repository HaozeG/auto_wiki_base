---
canonical_name: Stream Computing RISC-V Matrix Extension
aliases:
- RISC-V Matrix Instruction Set
- Stream Computing Matrix Extension
- riscv-matrix-spec
subtype: null
tags: []
scorecard:
  novelty_delta: 0.6
  claim_density: 0.5
  self_containedness: 0.8
  bridge_score: 0.6
  hub_potential: 0.5
sources:
- raw/cache/7d87f6fece87063a.md
- https://riscv.org/blog/2024/11/stream-computing-risc-v-matrix-extension-open-source-project-upgrades-to-version-0-5-supporting-vectormatrix-implementation/
source_url: https://riscv.org/blog/2024/11/stream-computing-risc-v-matrix-extension-open-source-project-upgrades-to-version-0-5-supporting-vectormatrix-implementation/
fetched_at: '2026-07-02T10:13:28.142082+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# Stream Computing RISC-V Matrix Extension

The Stream Computing RISC-V Matrix Extension is an open-source proposal for a matrix instruction set architecture (ISA) extension designed to accelerate artificial intelligence (AI) workloads on RISC-V processors. Initiated in 2021 by Stream Computing, the project addresses instruction fragmentation in the RISC-V AI ecosystem by providing a standardized, scalable domain-specific architecture for matrix operations. Version 0.5, released in November 2024, introduces a tile-based matrix multiplication architecture with both 32-bit and 64-bit instruction encoding options, a parameterized register architecture, and a modular type system to support applications ranging from edge to cloud deployments. The project includes a complete toolchain comprising an LLVM-based compiler, a Spike-based simulator, a GDB debugger, and an open-source core implementation based on the SCOOP (Stream Computing Out-of-Order Processor) platform which integrates RVV 1.0 and matrix support into the Berkeley BOOM core. This makes it the first open-source RISC-V Vector and Matrix project in the industry.

## Key Claims

- Stream Computing released v0.5 of its RISC-V Matrix ISA Specification and supporting toolchains in October 2024, becoming the first company to submit a complete RISC-V matrix instruction set and tools to the global community.
- The instruction set uses a tile-based matrix multiplication architecture with both 32-bit and 64-bit long instruction encoding variants.
- The design features a parameterized register architecture and modular type system to adapt to various application scenarios from edge to cloud.
- Supporting tools include an LLVM-based compiler, a Spike-based simulator, a GDB debugger, and an open-source core implementation.
- The SCOOP platform extends the Berkeley BOOM core with RVV 1.0 and matrix support, claiming to be the first open-source RISC-V Vector and Matrix project.
- The compiler, simulator, and debugger are updated to v0.5; the open-source core is at v0.2.
- The project collaborates with academia: Dr. Tianyu Jia of Peking University adopted SCOOP into a graduate SOC design course in Fall 2024.

## Relationships

- [[cpa-factored-gemmini-systolic-array]]: Both projects target RISC-V matrix/vector acceleration; the Gemmini systolic array is a separate hardware generator while Stream Computing focuses on ISA extension and open-source tooling.
- Insufficient context for additional cross-links; no existing entity pages for Stream Computing, SCOOP, or related matrix extension projects are present in the wiki.

## Sources

- [Stream Computing RISC-V Matrix Extension Open Source Project Upgrades to Version 0.5](https://riscv.org/blog/2024/11/stream-computing-risc-v-matrix-extension-open-source-project-upgrades-to-version-0-5-supporting-vectormatrix-implementation/)
