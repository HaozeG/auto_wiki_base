---
canonical_name: XuanTie C906
aliases:
- C906
- T-HEAD XuanTie C906
- Alibaba XuanTie C906
subtype: null
tags: []
hardware_targets:
- XuanTie C906
toolchains:
- CSI-NN2
- HHB
- TVM
constraints:
- RISC-V Vector extension V0.7.1
- 128-bit vector units
- 5-8 stage integer pipeline
- int8, int16, int32, int64, bf16, fp16, fp32, fp64 support
scorecard:
  novelty_delta: 0.8
  claim_density: 0.6
  self_containedness: 0.8
  bridge_score: 0.5
  hub_potential: 0.6
sources:
- raw/cache/43eb1940c8335240.md
- https://riscv.org/blog/xuantie-c906-tops-mlperf-tiny-v0-7-benchmark-mengchang-alibaba-cloud/
source_url: https://riscv.org/blog/xuantie-c906-tops-mlperf-tiny-v0-7-benchmark-mengchang-alibaba-cloud/
fetched_at: '2026-07-02T11:04:05.109814+00:00'
type: hardware_target
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# XuanTie C906

XuanTie C906 is a 64-bit high-energy processor developed by Alibaba Cloud based on the RISC-V instruction set architecture, featuring a five- to eight-stage integer pipeline and 128-bit vector operation units compliant with RISC-V Vector extension V0.7.1. It supports a wide range of data formats including int8, int16, int32, int64, bf16, fp16, fp32, and fp64, and uses fp16 as the default data type for benchmark deployments. The processor is integrated into the Allwinner D1 SoC, which has entered full-scale production and is available on the open market via development boards and AliExpress. Software support includes the open-source CSI-NN2 neural network acceleration library and the HHB deployment toolchain based on Apache TVM, both providing assembly-level optimizations for the RISC-V Vector extension. The XuanTie C906 achieved top marks across all four categories of the MLPerf Tiny v0.7 benchmark: Visual Wake Words (VWW), Image Classification (IC), Keyword Spotting (KWS), and Anomaly Detection (AD).

## Key Claims

- 64-bit RISC-V architecture with 5-8 stage integer pipeline.
- 128-bit vector units based on RISC-V Vector extension V0.7.1.
- Supports int8/int16/int32/int64/bf16/fp16/fp32/fp64; optimal performance with fp16.
- Top marks in all MLPerf Tiny v0.7 categories (VWW, IC, KWS, AD).
- Used in Allwinner D1 SoC, available for purchase on AliExpress.
- Software tools: CSI-NN2 (open source), HHB (TVM-based, open source), Sinian (model compression, 3-8x workload reduction).

## Optimization-Relevant Details

- ISA/profile: RV64GCV (RISC-V Vector extension V0.7.1)
- Vector/matrix/accelerator support: 128-bit vector operation units, multi-channel and mode data prefetching.
- Memory/cache/TLB/DMA: Data access bandwidth optimization; specific cache sizes not disclosed in source.
- Compiler/toolchain support: CSI-NN2 assembly-level optimizations for RVV; HHB based on Apache TVM supporting Caffe, TensorFlow, ONNX, TensorFlow Lite; Sinian for model compression.

## Relationships

- [[kendryte-k230-neural-network-benchmarks]]: Another RISC-V AI benchmark result for comparison of different hardware platforms.
- Insufficient context for additional cross-links; no other XuanTie family pages are present in the current wiki context.

## Sources

- https://riscv.org/blog/xuantie-c906-tops-mlperf-tiny-v0-7-benchmark-mengchang-alibaba-cloud/
