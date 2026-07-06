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
inbound_links: 5
scorecard:
  novelty_delta: 0.9
  claim_density: 0.9
  self_containedness: 0.9
  bridge_score: 0.5
  hub_potential: 0.3
source_url: https://github.com/qiurui144/local-ai-bench/blob/main/benchmark/llama_baselines/k1-spacemit/2026-04-14T07-24-01/analysis_report.md
fetched_at: '2026-07-03T14:11:33.052230+00:00'
created: '2026-07-03'
updated: '2026-07-06'
---

# SpacemiT K1

The SpacemiT K1 (also referred to as Key Stone K1) is an 8-core RISC-V application processor designed for AI inference at the edge. It integrates SpacemiT's proprietary X60 RISC-V core, which conforms to the RISC-V 64GCVB architecture and the RVA22 standard, and extends the ISA with 16 dedicated AI instructions for matrix multiplication and sliding window operations. The X60 cores also include RVV 1.0 vector extension support (zve64d/f/x) and the proprietary SpacemiT IME (Intelligent Memory Engine). The open instruction set and operator library can execute AI models from classical AlexNet to modern large language models such as Llama-2-7b. The SoC is equipped with 16 GB of LPDDR4X-3200 memory providing approximately 25.6 GB/s of theoretical bandwidth. It runs a Linux 6.6.63 kernel with glibc 2.39 and supports OpenBLAS, GGML (through Ollama 0.6.8), and ONNX Runtime 1.18.0 for AI workloads. The hardware includes a PMU (Performance Monitoring Unit) but it does not expose standard RISC-V hardware events, requiring raw event IDs for access. The K1 implements RISC-V PMP security specifications and ePMP security extensions, and supports secure boot, secure storage, signature verification, and product lifecycle security management. It includes an SDIO3.0 interface for SD cards and hardware video encoding/decoding for 4K resolutions in H.265, H.264, VP9, and VP8 formats. The system is available on the MUSE Pi Pro development board and has been benchmarked for LLM inference, embedding, reranking, ASR, and OCR tasks.

## Key Claims

- 8-core SpacemiT X60 CPU with RVV 1.0, SpacemiT IME, and 16 dedicated AI instructions for matrix multiplication and sliding window.
- X60 core adheres to RISC-V 64GCVB and RVA22.
- LPDDR4X-3200 16 GB memory with 25.6 GB/s theoretical bandwidth.
- Linux 6.6.63 kernel, glibc 2.39.
- Ollama 0.6.8 custom build with GGML RVV and IME support enabled.
- ONNX Runtime 1.18.0.
- PMU available but only supports raw event IDs (non-standard RISC-V events).
- Supports RISC-V PMP and ePMP security extensions, secure boot, secure storage, signature verification, and product lifecycle security management.
- Supports SDIO3.0 SD card interface.
- Hardware video decode/encode for 4K formats: H.265, H.264, VP9, VP8.

## Optimization-Relevant Details

- ISA/profile: RV64GC with RVV 1.0, zve64d, zve64f, zve64x; also conforms to RISC-V 64GCVB and RVA22; proprietary X60 AI extensions (16 dedicated AI instructions for matrix multiplication and sliding window).
- Vector/matrix/accelerator support: RVV 1.0, VLEN=256 bit, SpacemiT IME, plus 16 dedicated AI instructions.
- Memory/cache/TLB/DMA: 16 GB LPDDR4X-3200, unified memory (no dedicated L3 cache).
- Compiler/toolchain support: glibc 2.39, OpenBLAS, GGML, ONNX Runtime.

## Relationships

- The BPI-F3 LLM inference benchmark with RVV-optimized llama.cpp validates the practical performance of the SpacemiT K1 RVV 1.0 extensions on representative LLM workloads (see [[bpi-f3-rvv-llm-benchmark]]).
- No specific relationship to visible context pages. The SpacemiT K1 is a different hardware target than the XuanTie C908, with distinct vector length, toolchain support, and peripheral architecture.

## Sources

- https://github.com/qiurui144/local-ai-bench/blob/main/benchmark/llama_baselines/k1-spacemit/2026-04-14T07-24-01/analysis_report.md
- https://docs.banana-pi.org/en/BPI-F3/SpacemiT_K1
- https://github.com/SpacemiT-OpenSource/docs-chip/blob/main/en/key_stone/k1/k1_docs/k1_ds.md (referenced in search snippets)
