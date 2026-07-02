---
canonical_name: Vortex
aliases:
- Vortex GPGPU
- OpenCL Compatible RISC-V GPGPU
subtype: null
tags: []
scorecard:
  novelty_delta: 0.8
  claim_density: 0.3
  self_containedness: 0.9
  bridge_score: 0.2
  hub_potential: 0.4
sources:
- raw/cache/d9bf7c1ca9900d3a.md
- https://www.luffca.com/ja/2023/03/riscv-gpgpu-vortex-part2/
source_url: https://www.luffca.com/ja/2023/03/riscv-gpgpu-vortex-part2/
fetched_at: '2026-07-02T11:19:33.877937+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# Vortex

Vortex is a RISC-V-based General-Purpose Graphics Processing Unit (GPGPU) that provides OpenCL compatibility through a SIMT (Single Instruction, Multiple Thread) architecture. Its instruction set architecture extends the RV32IMF base with custom instructions to support parallel execution of OpenCL programs. The Intrinsic Library, implemented within the Vortex runtime, enables programmers to utilize these custom instructions through standard OpenCL programming models without requiring modifications to the underlying Clang/LLVM compiler toolchain. This architecture targets efficient execution of general-purpose compute workloads, such as matrix multiplication (GEMM), leveraging the RISC-V Vector Extension.

## Key Claims

- Vortex is a RISC-V-based GPGPU that supports OpenCL.
- It implements a SIMT architecture.
- Its ISA extends RISC-V RV32IMF with custom instructions for GPU operations.
- An Intrinsic Library in the Vortex runtime allows using these custom instructions through standard OpenCL programming models without modifying the Clang/LLVM toolchain.
- Vortex targets general-purpose compute workloads, including matrix multiplication (GEMM), leveraging the RISC-V Vector Extension.

## Relationships

- [[llvm-riscv-fptrunc-narrowing-optimization]]: As a LLVM-related optimization recipe for RISC-V platforms, this could improve code generation efficiency for workloads running on the Vortex GPGPU.
- Insufficient context for additional cross-links; no other entity pages are available in the wiki context.

## Sources

- [Luffca blog: Vortex: OpenCL Compatible RISC-V Based GPGPU (Part 2)](https://www.luffca.com/ja/2023/03/riscv-gpgpu-vortex-part2/)
- arXiv paper: [Vortex: OpenCL Compatible RISC-V GPGPU (2002.12151)](https://arxiv.org/abs/2002.12151)
