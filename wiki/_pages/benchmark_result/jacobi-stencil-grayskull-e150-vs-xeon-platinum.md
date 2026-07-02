---
canonical_name: Jacobi Stencil on Tenstorrent Grayskull e150 vs Xeon Platinum
aliases:
- Grayskull e150 Jacobi stencil benchmark
- Brown-Barton Grayskull stencil benchmark
subtype: null
tags: []
hardware_targets:
- Tenstorrent Grayskull e150
workloads:
- Jacobi iterative method (stencil)
datatypes:
- BF16
- FP32
metrics:
- performance
- energy efficiency
toolchains: []
hardware_versions:
- Tenstorrent Grayskull e150 (no specific version)
software_versions: []
measurement_method: Comparison of execution time and energy between Grayskull e150
  and Xeon Platinum CPU; scaling test with 4 e150 cards.
evidence_strength: reported
scorecard:
  novelty_delta: 0.9
  claim_density: 0.6
  self_containedness: 0.7
  bridge_score: 0.5
  hub_potential: 0.6
sources:
- raw/cache/52612464b0ae26b5.md
- https://www.research.ed.ac.uk/en/publications/accelerating-stencils-on-the-tenstorrent-grayskull-risc-v-acceler
source_url: https://www.research.ed.ac.uk/en/publications/accelerating-stencils-on-the-tenstorrent-grayskull-risc-v-acceler
fetched_at: '2026-07-02T10:05:55.497315+00:00'
type: benchmark_result
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# Jacobi Stencil on Tenstorrent Grayskull e150 vs Xeon Platinum

The Jacobi iterative method stencil benchmark on the Tenstorrent Grayskull e150 accelerator, conducted by Brown and Barton (2024) and presented at the International Workshop on RISC-V for HPC (RISCV-HPC) at SC24, compares the performance and energy efficiency of the RISC-V accelerator against a Xeon Platinum CPU. The benchmark uses the Jacobi iterative method as a vehicle for stencil computations and evaluates both a single e150 card and a cluster of four e150 cards. The measurement context includes a qualitative performance comparison (similar performance at BF16 vs FP32) and energy efficiency (approximately five times less energy per card). The results demonstrate that the Grayskull e150 achieves comparable computational throughput to a high-end x86 CPU while consuming significantly less energy, and that the accelerator scales nearly linearly across four cards.

## Key Claims

- Single Grayskull e150 provides performance similar to a Xeon Platinum CPU when executing the Jacobi iterative method (BF16 vs FP32).
- Single e150 uses approximately five times less energy than the Xeon Platinum CPU.
- Four e150 cards achieve approximately four times the performance of a single Xeon Platinum CPU while maintaining the five times energy savings.

## Measurement Context

- Hardware version: Tenstorrent Grayskull e150 (PCIe accelerator), Xeon Platinum CPU.
- Software/toolchain version: Not specified in the source.
- Workload shape: Jacobi iterative method (stencil computation).
- Metric: Performance (throughput/comparative), energy efficiency (relative).
- Method: Comparison of execution time and energy between Grayskull e150 and Xeon Platinum; scaling test with 4 e150 cards. Results are reported qualitatively as "similar performance" and quantitative multiples for energy.
- Evidence strength: reported (accepted workshop paper).

## Relationships

- [[tenstorrent-grayskull-e150]]: The hardware target on which this benchmark is conducted.
- [[gemmini]]: Both this benchmark and Gemmini represent RISC-V-based accelerator evaluation; Gemmini provides a generator approach while Grayskull offers a fixed architecture.
- [[nncase]]: nncase compiles neural network models for RISC-V AI accelerators; similar benchmarking methodologies may apply.

## Sources

- [Accelerating stencils on the Tenstorrent Grayskull RISC-V accelerator (arXiv)](https://arxiv.org/pdf/2409.18835)
