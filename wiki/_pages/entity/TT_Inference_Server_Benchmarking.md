---
cold_start: true
created: '2026-07-04'
inbound_links: 1
scorecard:
  bridge_score: 0.7
  claim_density: 0.5
  hub_potential: 0.6
  novelty_delta: 0.7
  self_containedness: 0.8
sources:
- https://github.com/tenstorrent/tt-inference-server/blob/main/benchmarking/README.md
tags:
- Tenstorrent
- LLM
- benchmark
- tt-inference-server
type: entity
updated: '2026-06-29'
---

# TT-Inference-Server Benchmarking

The tt-inference-server benchmarking framework provides a unified toolchain for measuring performance of LLM inference implementations on Tenstorrent hardware, including the Blackhole-based TT-LoudBox (T3K) and Galaxy (32-chip) systems. It supports four benchmarking tools: vLLM (default server-side measurements), GenAI-Perf (NVIDIA Triton SDK tool for cross-vendor comparability), AIPerf (detailed percentile metrics including mean, P50, P95, P99), and GuideLLM (dataset-driven multi-turn and omni-modal workloads). The framework is orchestrated via `run.py` with the `--workflow benchmarks` flag and uses a configuration system (`benchmark_config.py`) that defines `BenchmarkConfig`, `BenchmarkTask`, and `BenchmarkTaskParams` to statically specify Python environments, benchmark parameters, and expected performance targets for each model implementation. Performance targets are theoretical estimates for each model architecture and hardware combination, stored in `model_performance_reference.json`. For example, the Llama-3.3-70B architecture on T3K (TT-LoudBox) has a theoretical time-to-first-token (TTFT) of 38 ms and a throughput of 28 tokens per second at 128 input and 128 output sequence lengths. The framework also supports prefix-caching benchmarks via the `tt-inference-server-v2` submodule.

## Key Claims

- The framework provides four benchmarking tools: vLLM, GenAI-Perf, AIPerf, and GuideLLM, each serving different measurement purposes (baseline, Triton comparability, detailed percentiles, multi-turn/omni-modal).
- Benchmark configuration is statically defined per model implementation using `BenchmarkConfig`, `BenchmarkTask`, and `BenchmarkTaskParams` classes.
- Theoretical performance targets are defined per model architecture and hardware combination, keyed by the first model weight name.
- For Llama-3.3-70B on T3K (TT-LoudBox): theoretical TTFT = 38 ms, throughput = 28 tokens/s at ISL=128, OSL=128.
- For Llama-3.3-70B on Galaxy: theoretical TTFT = 50 ms, throughput = 80 tokens/s at ISL=128, OSL=128.
- Prefix-caching benchmarks are implemented in a separate `tt-inference-server-v2/` submodule.
- The workflow includes CLI parsing, model/device validation, server readiness check, and subprocess execution of benchmark tasks.

## Relationships

- [[Blackhole_Architecture]] – The hardware target (T3K/LoudBox, Galaxy) is built on Blackhole accelerators, and the benchmarks measure performance on this architecture.
- Insufficient context for additional cross-links: the wiki currently lacks entity pages for TT-LoudBox, TT-QuietBox, or the Tenstorrent Galaxy system; only Blackhole Architecture is available.

## Sources

- [tt-inference-server/benchmarking/README.md – GitHub](https://github.com/tenstorrent/tt-inference-server/blob/main/benchmarking/README.md)
