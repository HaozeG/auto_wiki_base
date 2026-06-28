---
cold_start: true
created: '2026-05-10'
inbound_links: 0
needs_summary_revision: true
scorecard:
  bridge_score: 0.7
  claim_density: 0.6
  hub_potential: 0.7
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://link.springer.com/chapter/10.1007/978-981-92-0378-9_24
tags:
- RISC-V
- LLM
- benchmark
- RVV
- inference
type: entity
updated: '2026-06-28'
---

# RVLLM-Bench

RVLLM-Bench is a comprehensive benchmark suite designed to evaluate the effectiveness and cross-platform portability of the RISC-V Vector (RVV) extension for large language model (LLM) inference. Proposed in a 2026 conference paper presented at DASFAA, the benchmark incorporates both the pre-filling (prompt processing) and decoding (token generation) phases across different workload patterns on typical RISC-V platforms. It uses two C/C++ inference engines, llama.cpp and fastllm, and supports multiple model scales to provide a reproducible baseline for RVV-based acceleration. The suite covers a range of configurations to measure throughput and energy consumption, addressing the lack of extensive benchmarks for RVV-based LLM inference. The source code and data are publicly available on GitHub, enabling community reuse and extension.

## Key Claims

- RVLLM-Bench evaluates both the pre-filling and decoding phases of LLM inference using the RISC-V Vector extension.
- The suite employs two C/C++ engines: llama.cpp and fastllm, providing cross-platform portability.
- It supports multiple model scales and workload patterns.
- Benchmark results demonstrate significant performance gains from RVV in both phases under various configurations.
- The suite provides a comprehensive and reproducible baseline for RVV-based acceleration of LLM inference.
- Code and data are publicly available at https://github.com/JocelynPanPan/rvllm-bench.

## Relationships

- [[Sipeed_MAIX_series]] – Both are RISC-V-based platforms targeting AI workloads, though Sipeed focuses on edge AI with the K210 processor while RVLLM-Bench targets general LLM inference acceleration via RVV.
- (Insufficient context for additional cross-links to other entity pages; only one entity page was available in the wiki context.)

## Sources

- [RVLLM-Bench: A Comprehensive Benchmark for Large Language Model Inference with RISC-V Vector Extension – Springer Link](https://link.springer.com/chapter/10.1007/978-981-92-0378-9_24)
