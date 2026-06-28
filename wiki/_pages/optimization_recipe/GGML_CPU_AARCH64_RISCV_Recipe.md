---
cold_start: true
constraints:
- RISC-V with vector extensions (v)
- 64-core CPU
- 125GB RAM
- GGML_CPU_AARCH64=ON required
- no GPU
created: '2025-11-10'
datatypes:
- FP16 (base)
- quantized Q4_0
evidence_strength: reported
hardware_targets:
- MilkV Pioneer
inbound_links: 0
metrics: []
scorecard:
  bridge_score: 0.8
  claim_density: 0.7
  hub_potential: 0.7
  novelty_delta: 0.8
  self_containedness: 0.9
sources:
- https://bruno.verachten.fr/2025/11/10/running-a-70b-llm-on-pure-risc-v-the-milkv-pioneer-deployment-journey/
tags:
- llama.cpp
- GGML
- RISC-V
- MilkV Pioneer
- LLM inference
- build
toolchains:
- GCC 13.2.1
- CMake
- llama.cpp
type: optimization_recipe
updated: '2026-06-28'
workloads:
- LLM inference (70B parameter models)
---

# GGML_CPU_AARCH64 RISC-V Recipe for llama.cpp

This recipe describes the build and configuration steps to deploy llama.cpp on a RISC-V workstation (specifically the MilkV Pioneer) to run large language models such as a 70B parameter model. The key enabling factor is setting GGML_CPU_AARCH64=ON during CMake configuration, which allows llama.cpp to use ARM-optimized code paths that map to RISC-V vector extensions. The recipe assumes a system with the rv64imafdcv ISA (including vector extension), 64 cores, at least 125GB of RAM, and Fedora Linux. Prerequisites include GCC 13.2.1 (or compatible), CMake, git, and ccache. Expected effect: a fully functional llama.cpp build that can load quantized 70B models (e.g., Q4_0) using CPU-only inference. Major claims are grounded in a successful deployment reported in a community blog; quantitative performance measurements were not collected. Failure modes include attempting this on RISC-V hardware without vector extensions, which would result in 5-10x slower inference, or using a compiler version incompatible with CMake.

## Key Claims

- Setting GGML_CPU_AARCH64=ON enables llama.cpp to use ARM-optimized SIMD code paths on RISC-V due to architectural similarities between RVV and ARM NEON.
- Standard CMake build (cmake -B build, cmake --build build) works without patches on RISC-V with vector extensions.
- The build successfully produces llama-cli, llama-server, llama-bench, and other executables.
- A 70B parameter model quantized to Q4_0 (~40GB) can be loaded into the 125GB RAM without disk swapping.
- Vector extensions are critical; systems without v extension will see 5-10x slower performance.

## Transformation

- Prerequisites: RISC-V system with rv64imafdcv (vector extension), 64 cores, ≥125GB RAM, Fedora Linux, GCC 13.2.1, CMake, git, ccache.
- Steps:
  1. Clone llama.cpp repository: `git clone https://github.com/ggerganov/llama.cpp.git`
  2. Configure with CMake: `cmake -B build -DGGML_CPU_AARCH64=ON -DGGML_ACCELERATE=ON`
  3. Build using all cores: `cmake --build build --config Release -j 64`
  4. Verify build: `./build/bin/llama-cli --version`
  5. Load and run a quantized model (e.g., a 70B Q4_0 GGUF file) using llama-cli or llama-server.
- Expected effect: Successful build and deployment of llama.cpp for CPU-only LLM inference on RISC-V. The model runs, but performance is not benchmarked in the source.
- Failure modes: Running on RISC-V without vector extensions (v) will lead to very poor performance. Using an incompatible compiler or missing dependencies may cause build failures. Memory insufficient for model load will cause swapping or out-of-memory errors.
- Measurements: Build success was reported; performance estimates of 1-5 tokens/sec are theoretical extrapolations. No measured benchmark data was collected. Evidence strength is classified as reported.

## Relationships

- [[MilkV_Pioneer]] – The specific hardware target used for this deployment.
- [[RVV_Autovectorization_Optimization_Insights]] – Optimization insights for RVV, relevant to improving vector utilization in llama.cpp on RISC-V.

## Sources

- [Bruno Verachten, "Running a 70B LLM on Pure RISC-V: The MilkV Pioneer Deployment Journey"](https://bruno.verachten.fr/2025/11/10/running-a-70b-llm-on-pure-risc-v-the-milkv-pioneer-deployment-journey/)

