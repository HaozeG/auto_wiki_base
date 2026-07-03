---
canonical_name: SpacemiT K1
aliases:
- Spacemit K1
- SpacemiT K1 MUSE Pi Pro
- K1
- Key Stone K1
- SpacemiT Key Stone K1
subtype: null
type: hardware_target
tags: []
sources:
- raw/cache/fb13c2effa6c4276.md
- https://github.com/qiurui144/local-ai-bench/blob/main/benchmark/llama_baselines/k1-spacemit/2026-04-14T07-24-01/analysis_report.md
- raw/cache/5eb1c79e0b60165a.md
- https://docs.banana-pi.org/en/BPI-F3/SpacemiT_K1
hardware_targets:
- SpacemiT K1
toolchains:
- Ollama
- GGML
- ONNX Runtime
- OpenBLAS
constraints:
- RVV 1.0 with zve64d/f/x
- SpacemiT IME
- VLEN=256 bit
- LPDDR4X-3200 16 GB
- Linux 6.6.63
cold_start: true
inbound_links: 4
scorecard:
  novelty_delta: 0.9
  claim_density: 0.9
  self_containedness: 0.9
  bridge_score: 0.5
  hub_potential: 0.3
source_url: https://github.com/qiurui144/local-ai-bench/blob/main/benchmark/llama_baselines/k1-spacemit/2026-04-14T07-24-01/analysis_report.md
fetched_at: '2026-07-03T14:11:33.052230+00:00'
created: '2026-07-03'
updated: '2026-07-03'
---

# SpacemiT K1

The SpacemiT K1 is an 8-core RISC-V application processor designed for AI inference at the edge, built around the SpacemiT X60 CPU cores with RVV 1.0 vector extension support including zve64d/f/x and the proprietary SpacemiT IME (Intelligent Memory Engine). The SoC is equipped with 16 GB of LPDDR4X-3200 memory providing approximately 25.6 GB/s of theoretical bandwidth. It runs a Linux 6.6.63 kernel with glibc 2.39 and supports OpenBLAS, GGML (through Ollama 0.6.8), and ONNX Runtime 1.18.0 for AI workloads. The hardware includes a PMU (Performance Monitoring Unit) but it does not expose standard RISC-V hardware events, requiring raw event IDs for access. The system is available on the MUSE Pi Pro development board and has been benchmarked for LLM inference, embedding, reranking, ASR, and OCR tasks.

## Key Claims

- 8-core SpacemiT X60 CPU with RVV 1.0 and SpacemiT IME.
- LPDDR4X-3200 16 GB memory with 25.6 GB/s theoretical bandwidth.
- Linux 6.6.63 kernel, glibc 2.39.
- Ollama 0.6.8 custom build with GGML RVV and IME support enabled.
- ONNX Runtime 1.18.0.
- PMU available but only supports raw event IDs (non-standard RISC-V events).

## Optimization-Relevant Details

- ISA/profile: RV64GC with RVV 1.0, zve64d, zve64f, zve64x
- Vector/matrix/accelerator support: RVV 1.0, VLEN=256 bit, SpacemiT IME
- Memory/cache/TLB/DMA: 16 GB LPDDR4X-3200, unified memory (no dedicated L3 cache)
- Compiler/toolchain support: glibc 2.39, OpenBLAS, GGML, ONNX Runtime

## Relationships

No specific relationship to visible context pages. The SpacemiT K1 is a different hardware target than the XuanTie C908, with distinct vector length, toolchain support, and peripheral architecture.

## Sources

- https://github.com/qiurui144/local-ai-bench/blob/main/benchmark/llama_baselines/k1-spacemit/2026-04-14T07-24-01/analysis_report.md
