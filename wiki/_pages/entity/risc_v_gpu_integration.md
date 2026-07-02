---
canonical_name: RISC-V and GPU Integration
aliases:
- RISC-V GPU integration
- RISC-V+GPU SoC design
- SpacemiT K3
subtype: null
tags:
- RISC-V
- GPU
- SoC
scorecard:
  novelty_delta: 0.8
  claim_density: 0.5
  self_containedness: 0.9
  bridge_score: 0.7
  hub_potential: 0.6
sources:
- raw/cache/b5fdb989562650ec.md
- https://www.indexbox.io/blog/risc-v-and-gpu-integration-the-new-frontier-in-high-performance-soc-design/
source_url: https://www.indexbox.io/blog/risc-v-and-gpu-integration-the-new-frontier-in-high-performance-soc-design/
fetched_at: '2026-07-02T04:39:04.856754+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# RISC-V and GPU Integration

RISC-V and GPU integration represents an emerging trend in high-performance SoC design, where RISC-V CPU IP is combined with GPU capabilities to target applications such as AI PCs, robotics, and intelligent edge devices. The open and extensible nature of the RISC-V ISA allows for custom SIMT extensions and GPGPU implementations, such as the open-source Ventus GPGPU, which leverages the RISC-V Vector Extension (RVV) to accelerate parallel workloads. This integration is exemplified by processors like SpacemiT's K3, which combine RISC-V CPU cores with GPU compute to create single-chip solutions that can address both general-purpose and graphics-intensive workloads. The approach is seen as a path towards more flexible and competitive platforms that can challenge traditional CPU+GPU architectures dominated by x86 and ARM.

## Key Claims

- RISC-V and GPU integration is positioned as a new frontier in high-performance SoC design, driving ecosystem maturity and system-level innovation.
- SpacemiT's K3 processor exemplifies this integration, targeting AI PCs, robotics, and intelligent edge devices.
- Ventus is an open-source GPGPU implementation built upon the RISC-V architecture with vector extension (RVV), introducing customized instructions and a comprehensive software toolchain.
- Tenstorrent's RISC-V CPU is designed for orchestration, I/O, and latency-sensitive tasks rather than raw compute, offering a different role in heterogeneous computing.
- Andes Technology and Imagination Technologies demonstrated a RISC-V + GPU graphics card using the Imagination BXT-32-1024 GPU, delivering 48 Gpixels/sec fill rate.

## Relationships

- [[xuantie_c908]]: A RISC-V AIoT processor with vector extension, representing the CPU side of RISC-V accelerated computing.
- [[llvm_riscv_target]]: The LLVM compiler backend for RISC-V, which supports GPU-related extensions and code generation for RISC-V hardware.
- [[mlir_xdsl_rvv_gemm_codegen_recipe]]: An optimization recipe for RISC-V vector code generation, relevant to GPGPU workloads on RVV.

## Sources

- https://www.indexbox.io/blog/risc-v-and-gpu-integration-the-new-frontier-in-high-performance-soc-design/
