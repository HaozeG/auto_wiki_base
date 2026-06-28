---
cold_start: true
constraints:
- 50 MHz
- rvv0.7
- 256 double-precision elements per instruction
- 8 elements per cycle
created: '2025-03-04'
hardware_targets:
- fpga-sdv cluster
inbound_links: 6
scorecard:
  bridge_score: 0.8
  claim_density: 0.8
  hub_potential: 0.7
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://arxiv.org/html/2501.06175v1
tags:
- RISC-V
- vector
- FPGA
- BSC
toolchains:
- Clang (BSC modified)
type: hardware_target
updated: '2026-06-28'
---------------

# fpga-sdv RISC-V Vector Cluster

The fpga-sdv cluster is an FPGA-based development system that implements a RISC-V scalar core tightly coupled with a vector processing unit. The vector unit supports up to 256 double-precision elements per instruction and can process up to 8 elements per cycle. The ISA extensions available include rv64gcv with the vector extension at revision rvv0.7. The core operates at a frequency of 50 MHz and runs a standard Ubuntu 22.04 Linux image. The system is designed for performance evaluation and includes a custom hardware tracer embedded within the FPGA that can spy on selected signals at each clock cycle for detailed analysis.

## Key Claims

- Supports ISA extensions rv64gcv with rvv0.7 vector extension.
- Vector unit can hold up to 256 double-precision elements per instruction.
- Throughput of 8 double-precision elements per cycle.
- Core frequency: 50 MHz.
- Runs Ubuntu 22.04 Linux.
- Includes a custom hardware tracer for cycle-accurate performance measurement.

## Optimization-Relevant Details

- ISA/profile: rv64gcv with rvv0.7
- Vector/matrix/accelerator support: Vector unit up to 256 double-precision elements
- Memory/cache/TLB/DMA: Not specified in source
- Compiler/toolchain support: Clang-based compiler from BSC, auto-vectorization support, compiler intrinsics for manual vectorization

## Relationships

- [[GEMM_with_RISC-V_Vector_Extension]] – Both are RISC-V vector platforms for GEMM workloads.
- [[Batched_DGEMM_for_Long_Vector_Architectures]] – This hardware target was used to evaluate the batched DGEMM optimization.

## Sources

- [arXiv paper: Batched DGEMMs for scientific codes running on long vector architectures](https://arxiv.org/html/2501.06175v1)
