---
canonical_name: cpufp
aliases:
- cpufp
- CPU Floating Point Benchmark
subtype: null
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.8
  self_containedness: 0.9
  bridge_score: 0.7
  hub_potential: 0.8
sources:
- raw/cache/5b40ed5242b6308a.md
- https://github.com/pigirons/cpufp
source_url: https://github.com/pigirons/cpufp
fetched_at: '2026-07-02T04:41:40.066867+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: false
inbound_links: 1
needs_summary_revision: false
---

# cpufp

cpufp is an open-source benchmarking tool designed to measure the peak floating-point and AI instruction set performance of CPUs. It automatically detects the local SIMD and Domain-Specific Accelerator (DSA) instruction sets at compile time, supporting a wide range of architectures including arm64, e2k, loongarch64, riscv64, and x86-64. The tool provides microarchitectural latency and throughput data for specific instructions on supported platforms, such as the Elbrus e2k combined operation fmul_addd on elbrus-v1 and elbrus-v4. cpufp is developed by Yang Gao (pigirons) and is available under the GNU General Public License v3.0. It is written primarily in assembly and C, and is intended for hardware engineers and performance analysts evaluating CPU capabilities for AI and scientific computing workloads.

## Key Claims

- cpufp benchmarks peak performance of floating-point and AI ISAs across multiple architectures.
- Automatically senses local SIMD/DSA ISAs during compilation.
- Supports x86-64: SSE, SSE2, AVX, FMA, AVX512f, AVX512_VNNI, AVX_VNNI, AVX512_FP16, AVX512_BF16, AVX_VNNI_INT8, AVX_VNNI_INT16, AMX_INT8, AMX_BF16, AMX_FP16.
- Supports arm64: asimd, asimd_hp, asimd_dp, bf16, i8mm.
- Supports riscv64: V (vector) extension 1.0 and SpacemiT-X60 custom ime matrix extension.
- Supports loongarch64: LASX, LSX, and scalar FP.
- Supports e2k (Elbrus): v1–v6 ISAs with combined operation instructions, e.g., fmul_addd with reported latency of 8 cycles and throughput of 0.16 CPI (elbrus-v4) and 0.25 CPI (elbrus-v1).
- Provides build scripts for each target architecture.
- Usage: `./cpufp --thread_pool=[list] --idle_time=sec`, where thread_pool sets CPU affinity and idle_time sets interval between benchmarks.
- Links to benchmark results for many processors (e.g., AMD Ryzen 7 9700X, Intel Xeon Gold 6455B, Apple Silicon M4 Max, Qualcomm Snapdragon X Elite, AWS Graviton 3E).

## Relationships

- cpufp can be used to benchmark the performance of RISC-V platforms such as the [[k230]] which integrates RISC-V C908 cores supporting the Vector Extension 1.0.
- The tool also supports arm64 benchmarking, which covers SoCs like the [[allwinner_v853]] (though that specific SoC uses a 32-bit Cortex-A7, its NPU and RISC-V coprocessor are relevant for AI benchmarking context).
- Insufficient context for additional cross-links.

## Sources

- https://github.com/pigirons/cpufp
