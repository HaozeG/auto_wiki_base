---
canonical_name: SpacemiT K1 AI Benchmark Report (2026-04-14)
aliases:
- K1 SpacemiT Benchmark Report v3
- K1 AI Benchmark 2026-04-14
subtype: null
type: benchmark_result
tags: []
sources:
- raw/cache/fb13c2effa6c4276.md
- https://github.com/qiurui144/local-ai-bench/blob/main/benchmark/llama_baselines/k1-spacemit/2026-04-14T07-24-01/analysis_report.md
hardware_targets:
- SpacemiT K1
workloads:
- LLM (Qwen2.5-0.5B, DeepSeek-R1-1.5B)
- Text Embedding (nomic-embed-text, bge-m3)
- Text Rerank (bge-m3)
- ASR (Whisper-tiny, SenseVoice)
- OCR (PP-OCR v3)
datatypes:
- FP32
- INT8 (pending due to ONNX Runtime version)
metrics:
- decode tokens/s
- TTFT (ms)
- prefill tokens/s
- samples/s
- cross-lingual similarity
- NDCG@5
- P@3
- RTF
- image/s
- keyword accuracy
toolchains:
- Ollama 0.6.8
- llama.cpp/GGML
- ONNX Runtime 1.18.0
- OpenBLAS
hardware_versions:
- SpacemiT K1 MUSE Pi Pro
software_versions:
- Linux 6.6.63
- glibc 2.39
- Ollama 0.6.8 (custom+GGML)
- ONNX Runtime 1.18.0
measurement_method: Automated benchmark using local-ai-bench framework with L1-L7
  bottleneck analysis, Roofline model, and thermal throttling test.
evidence_strength: measured
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
cold_start: true
inbound_links: 0
outbound_links:
- target: spacemit-k1
  reason: This benchmark is executed on the SpacemiT K1 hardware target and provides
    the primary measured performance data for that platform
---

# SpacemiT K1 AI Benchmark Report (2026-04-14)

The SpacemiT K1 AI Benchmark Report (version 3, dated 2026-04-14) presents measured performance of the SpacemiT K1 MUSE Pi Pro running a suite of AI workloads including LLM inference (Qwen2.5-0.5B and DeepSeek-R1-1.5B via Ollama with GGML backend), text embedding (nomic-embed-text and bge-m3), reranking (bge-m3), speech recognition (Whisper-tiny and SenseVoice via ONNX Runtime), and OCR (PP-OCR v3 via RapidOCR ONNX). The system ran Linux 6.6.63 with glibc 2.39 and utilized OpenBLAS, GGML with RVV and SpacemiT IME support, and ONNX Runtime 1.18.0. The benchmark data was collected using the local-ai-bench automated testing framework, and the report includes detailed bottleneck analysis, Roofline modeling, and optimization recommendations. Evidence strength is measured, as the results are from a controlled benchmark run.

## Key Claims

- Qwen2.5-0.5B short prompt decode: 10.8 tok/s, TTFT 390 ms.
- DeepSeek-R1-1.5B short prompt decode: 4.1 tok/s, TTFT 602 ms.
- nomic-embed-text throughput: 2.0 samples/s.
- bge-m3 throughput: 0.45 samples/s, cross-lingual similarity 0.752.
- bge-m3 rerank NDCG@5: 0.832, P@3: 1.00.
- Whisper-tiny FP32 ONNX encoder RTF: 0.12-0.57 (real-time for short audio).
- Complete ASR pipeline (Whisper-tiny + Qwen2.5 post-processing) RTF: 0.22 for 10s audio.
- PP-OCR v3 throughput: 0.151 img/s, keyword accuracy 94.2%.
- No thermal throttling detected after 60s continuous load (performance improved slightly due to cache warming).
- DDR bandwidth utilization only 7.5% for LLM decode; real bottleneck is Ollama HTTP overhead and small batch size.

### Optimization Paths (derived from analysis)

| Priority | Measure | Expected Effect | Verification |
|----------|---------|-----------------|--------------|
| P1 | Use Q2_K/Q3_K quantization | Bandwidth utilization 7.5% → 25%, decode ~2x | Pending |
| P1 | Bypass Ollama HTTP bridge, call llama.cpp C API | Eliminate serialization overhead | Pending |
| P2 | Upgrade ONNX Runtime ≥1.19 to enable ConvInteger int8 | ASR inference ~2x | Pending |
| P2 | OCR input downsampling (50% resolution) | Latency -30-50%, accuracy +16% (verified) | Verified |
| P3 | Use raw PMU events to measure real IPC | Better bottleneck identification | Pending |

## Measurement Context

- Hardware version: SpacemiT K1 MUSE Pi Pro
- Software/toolchain version: Linux 6.6.63, glibc 2.39, Ollama 0.6.8 (custom with GGML RVV+IME), ONNX Runtime 1.18.0, OpenBLAS
- Workload shape: LLM short/medium/long prompts (83-1753 tokens), embedding dimension 768/1024, rerank pairs, ASR audio durations 5-15s, OCR on Chinese+English images
- Metric: decode tokens/s, TTFT, prefill tokens/s, samples/s, NDCG@5, P@3, RTF, accuracy
- Method: Automated benchmark using local-ai-bench framework; L1-L7 bottleneck analysis with Roofline model; thermal throttling test (60s load)
- Evidence strength: measured

## Relationships

- [[spacemit-k1]]: This benchmark is executed on the SpacemiT K1 hardware target and provides the primary measured performance data for that platform.

## Sources

- https://github.com/qiurui144/local-ai-bench/blob/main/benchmark/llama_baselines/k1-spacemit/2026-04-14T07-24-01/analysis_report.md
