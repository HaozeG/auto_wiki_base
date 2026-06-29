---
cold_start: false
created: '2025-03-05'
inbound_links: 0
needs_summary_revision: true
scorecard:
  bridge_score: 0.4
  claim_density: 0.6
  hub_potential: 0.7
  novelty_delta: 0.9
  self_containedness: 0.8
sources:
- https://github.com/RALC88/riscv-vectorized-benchmark-suite
tags:
- RISC-V
- benchmark
- vector
- data-parallel
type: entity
updated: '2026-06-28'
---

# RiVEC Benchmark Suite

The RiVEC Benchmark Suite is a collection of data-parallel applications from various domains, designed for benchmarking vector microarchitectures. Originally targeting RISC-V architectures with the V extension, the suite can be ported to other vector or SIMD ISAs through a wrapper library. The suite implements the latest RISC-V vector intrinsics for rvv-1.0 and includes versions for rvv-0.7 and rvv-1.0 with PLCT Lab's LLVM. It has been tested on the Spike RISC-V ISA simulator, QEMU system emulator, and gem5 simulator. The suite provides 12 benchmark applications, including Axpy, Blackscholes, matmul, and others, covering domains such as high-performance computing, financial analysis, and engineering. The benchmark suite is available as open source and is accompanied by a research paper published in ACM Transactions on Architecture and Code Optimization (2020).

## Key Claims

- RiVEC is a collection of 12 data-parallel applications for benchmarking vector microarchitectures.
- It targets RISC-V V extension v1.0 with the master branch, with additional branches for v0.7 and v1.0-PLCTLab.
- It uses a wrapper library to map vector intrinsics to different ISAs.
- It has been successfully tested on Spike, QEMU, and gem5.
- The suite is open source and free of charge, with some applications having their own licensing.
- The accompanying research paper is published in ACM TACO, October 2020.

## Relationships

- [[Sipeed_MAIX_series]] – The Sipeed MAIX series uses a RISC-V core but is not directly related to the benchmark suite; it serves as an example of RISC-V hardware that could potentially be benchmarked with RiVEC.
- Insufficient context for additional cross-links.

## Sources

- [GitHub repository: RALC88/riscv-vectorized-benchmark-suite](https://github.com/RALC88/riscv-vectorized-benchmark-suite)
