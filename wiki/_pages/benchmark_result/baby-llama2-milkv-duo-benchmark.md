---
canonical_name: Baby LLama2 Benchmark on Milk-V Duo
aliases:
- rvspoc-s2311-llama2
- Baby LLama2 Milk-V Duo 24 tok/s
- Baby LLama2 Optimization for Milk-V Duo
- Baby LLama2 optimization C906
subtype: null
tags: []
hardware_targets:
- Milk-V Duo
- XuanTie C906
workloads:
- Baby LLama2 (story generation)
datatypes:
- int8
metrics:
- tokens/s
toolchains:
- Xuantie-900-gcc-linux-5.10.4-musl32
- Xuantie-900-llvm-linux-5.10.4-glibc
hardware_versions:
- T-Head C906 1GHz with RVV0.7, 64MB SDRAM
software_versions:
- official Milk-V Duo system image (55MB memory)
measurement_method: 'Story generation speed measured on official Milk-V Duo system
  with 55MB memory configuration using optimized binary.

  '
evidence_strength: measured
scorecard:
  novelty_delta: 0.9
  claim_density: 0.7
  self_containedness: 0.8
  bridge_score: 0.3
  hub_potential: 0.2
sources:
- raw/cache/256636dc54c122ce.md
- https://github.com/chamchamgo/rvspoc-s2311-llama2
source_url: https://github.com/chamchamgo/rvspoc-s2311-llama2
fetched_at: '2026-07-03T14:49:40.043210+00:00'
type: benchmark_result
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 2
---

# Baby LLama2 Benchmark on Milk-V Duo

Baby LLama2 is an open-source LLM inference engine implemented in fewer than 1000 lines of C code. This benchmark measures the story generation speed achieved after optimizing Baby LLama2 for the Milk-V Duo board, a RISC-V platform built around the T-Head C906 core clocked at 1GHz with the RVV 0.7 vector extension and 64MB SDRAM. The optimization employed int8 quantization, partial on-fly dequantization, RVV intrinsic for matrix multiplication, fast exponential approximation, and OpenMP auto-vectorization. On the official Milk-V Duo system with 55MB memory configuration, the optimized binary achieved a story generation speed of 24 tokens/s. The binary was compiled using the Xuantie-900-gcc-linux-5.10.4-musl32 V2.8.1 toolchain as the default, although the Xuantie-900-llvm-linux-5.10.4-glibc V1.0.0-beta could also be used. This result was reported as the outcome of the first RVSPOC (RISC-V Software Porting and Optimization Competition) held in 2023.

## Key Claims

- Story generation speed of 24 tokens/s on Milk-V Duo board with T-Head C906 core at 1GHz, RVV 0.7, 64MB SDRAM, and 55MB memory configuration.
- Optimization includes int8 quantization, partial on-fly dequantization, RVV intrinsics for matmul, fast exponential approximation, and OpenMP auto-vectorization.
- The official Milk-V Duo GCC toolchain V2.6.1 cannot compile the RVV intrinsic code; the required toolchain is Xuantie-900-gcc-linux-5.10.4-musl32 V2.8.1.
- GCC-compiled binary is approximately 10% slower than Clang-compiled binary but smaller.

## Measurement Context

- Hardware version: Milk-V Duo board with T-Head C906 1GHz, RVV0.7, 64MB SDRAM
- Software/toolchain version: official Milk-V Duo system image (55MB memory), Xuantie-900-gcc-linux-5.10.4-musl32 V2.8.1 (default) or Xuantie-900-llvm-linux-5.10.4-glibc V1.0.0-beta
- Workload shape: Baby LLama2 story generation (LLM inference, int8 quantized model)
- Metric: tokens per second (tokens/s)
- Method: Story generation speed measured on official Milk-V Duo system with 55MB memory configuration using optimized binary. No further run count or warm-up details provided.
- Evidence strength: measured

## Relationships

No specific relationship to visible context pages in this wiki. This benchmark targets the Milk-V Duo board with the XuanTie C906 core (RVV 0.7), which is not yet represented in existing pages for SpacemiT X60 (RVV 1.0) or C908 GCC tuning (scalar core without vector extension).

## Sources

- https://github.com/chamchamgo/rvspoc-s2311-llama2
