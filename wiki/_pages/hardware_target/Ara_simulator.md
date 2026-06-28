---
cold_start: true
constraints:
- Simulated hardware
- Long VLEN (default 4096-bit)
- Variable lane configuration
created: '2025-03-04'
hardware_targets:
- Ara
- RISC-V Vector Extension v1.0
inbound_links: 1
scorecard:
  bridge_score: 0.7
  claim_density: 0.8
  hub_potential: 0.5
  novelty_delta: 0.9
  self_containedness: 1.0
sources:
- https://www.luffca.com/2023/02/gemm-riscv-vector-part1/
tags:
- RISC-V
- vector
- simulator
- PULP
toolchains:
- Verilator (simulation)
type: hardware_target
updated: '2026-06-28'
---

# Ara Simulator

Ara is an open-source implementation of the RISC-V Vector Extension (RVV) developed by the PULP (Parallel Ultra Low Power) project. It supports RVV v1.0 and is characterized by a long vector length (VLEN) defaulting to 4096 bits, even in a 256-bit configuration using four 64-bit Vector Units. Each vector register can hold 64 double-precision floating-point elements, allowing up to 2048 elements across 32 registers. Ara is designed for performance evaluation and benchmarking via RTL simulation, and it includes a baseline double-precision matrix multiplication kernel (`fmatmul`) in its repository. The simulator is typically used with a Verilator-based flow.

## Key Claims

- Ara implements the RISC-V Vector Extension version 1.0.
- Default VLEN is 4096 bits; a 256-bit configuration uses four 64-bit Vector Units.
- Each vector register can handle 64 double-precision floating-point elements.
- The baseline `fmatmul` kernel does not support arbitrary matrix sizes.
- Ara's Vector Unit includes FMA (Fused Multiply-Add).

## Optimization-Relevant Details

- ISA/profile: RISC-V Vector Extension v1.0
- Vector/matrix/accelerator support: Vector registers only, no matrix accelerator
- Memory/cache/TLB/DMA: Not specified in the source
- Compiler/toolchain support: Simulation with Verilator; the blog uses Ara's RTL simulator

## Relationships

- [[Sipeed_MAIX_series]] – Both are RISC-V related platforms, though Ara is a simulator and Maix is a hardware board.
- (Insufficient context for additional cross-links)

## Sources

- [GEMM based on the RISC-V Vector Extension (Part 1) - Luffca](https://www.luffca.com/2023/02/gemm-riscv-vector-part1/)

