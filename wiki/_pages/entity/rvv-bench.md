---
cold_start: false
created: '2025-10-27'
inbound_links: 1
scorecard:
  bridge_score: 0.5
  claim_density: 0.3
  hub_potential: 0.3
  novelty_delta: 0.8
  self_containedness: 0.9
sources:
- https://github.com/camel-cdr/rvv-bench
tags:
- RISC-V
- RVV
- benchmark
- open-source
- vector
type: entity
updated: '2026-06-29'
---

# rvv-bench

rvv-bench is an open-source collection of RISC-V Vector (RVV) benchmarks hosted on GitHub, maintained by camel-cdr, intended to help developers write portable and performant RVV code. The repository includes multiple benchmark implementations of common algorithms, such as those found in the ./bench/ directory, and a separate tool for measuring the cycle count of individual RVV instructions by unrolling and looping over instructions repeatedly. Configuration files (config.h) allow users to tailor benchmarks to specific processors, adjusting parameters like memory scaling (MAX_MEM) and feature flags (e.g., HAS_E64). The suite is designed for easy execution via the bench-all.sh script, and results can be contributed to a companion aggregation repository. The project is licensed under the MIT license.

## Key Claims

- A collection of RISC-V Vector (RVV) benchmarks to assist developers in writing portably performant RVV code.
- Includes a cycle count measurement utility for RVV instructions that reports latency and throughput via unrolled loops.
- Offers easy setup and execution through the `./bench-all.sh` script.
- Benchmark parameters can be adjusted via configuration files to match the target processor.
- Results can be published to a community-driven results repository for cross-platform comparison.

## Relationships

- [[Chiplet_RISC_V_AI_SoC_Benchmark_Results]] – Example benchmark result page that may benefit from the rvv-bench testing framework.
- [[Tenstorrent_Grayskull_MatMul_Efficiency]] – Another benchmark result page demonstrating performance measurement similar to what rvv-bench enables.
- Note: There are currently no directly related entity pages in the wiki; links to existing benchmark result pages are provided for context.

## Sources

- [GitHub - camel-cdr/rvv-bench](https://github.com/camel-cdr/rvv-bench)

