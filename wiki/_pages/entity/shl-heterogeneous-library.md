---
canonical_name: SHL
aliases:
- Structure of Heterogeneous Library
- ShiHulan
- SHL (Structure of Heterogeneous Library)
- T-HEAD SHL
- CSI-NN2 reference implementation
subtype: null
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.6
  self_containedness: 0.8
  bridge_score: 0.7
  hub_potential: 0.5
sources:
- raw/cache/eb1dc4a967c736d9.md
- https://github.com/openvinotoolkit/shl/blob/main/README.md
- raw/cache/170b3421dbbb9c39.md
- https://zhangwm-pt.github.io/shl/md_README.html
- raw/cache/685ba9df7cd4100f.md
- https://github.com/openvinotoolkit/shl
- raw/cache/7f3fb17b96da7520.md
- https://github.com/BHbean/shl
source_url: https://github.com/openvinotoolkit/shl/blob/main/README.md
fetched_at: '2026-07-02T12:16:16.524999+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# SHL

SHL (Structure of Heterogeneous Library, also known as ShiHulan) is a high-performance heterogeneous computing library developed and provided by T-HEAD, the CPU design team at Alibaba Group. It implements the CSI-NN2 neural network library API for XuanTie CPU platforms, offering optimized binary libraries that include both a reference C code implementation and assembly-optimized versions specifically tailored for XuanTie RISC-V processors. The library supports symmetric and asymmetric quantization, operates on 8-bit, 16-bit, and float16 data types, and is compatible with both NCHW and NHWC data layouts. SHL is designed to be used with the HHB deployment tool for automatic API calls, and it provides reference heterogeneous scheduling implementations that span CPU and NPU architectures. The library is primarily intended as a reference implementation for the XuanTie CPU platform, with optimization for specific NPU targets left to the respective platform vendors. SHL is available as a Python package (via `pip install hhb`) or can be built from source using the T-HEAD RISC-V GCC toolchain, as demonstrated in the build example for the XuanTie C906 core.

## Key Claims

- SHL is a high-performance heterogeneous computing library by T-HEAD implementing the CSI-NN2 API for XuanTie CPU platforms.
- Provides both a reference C code implementation and assembly-optimized implementations for XuanTie CPUs.
- Supports symmetric and asymmetric quantization with 8-bit, 16-bit, and float16 data types.
- Compatible with NCHW and NHWC data formats.
- Integrates with the HHB deployment tool for automatic API invocation.
- Includes reference heterogeneous scheduling for CPU and NPU architectures.
- Can be installed via the `hhb` PyPI package or built from source using T-HEAD RISC-V GCC 2.6.
- Includes an example demonstrating mobilenetv1 inference with fused batch normalization on the XuanTie C906 core, generating a float16 model.
- Referenced in MLPerf Tiny v0.7 results under the Alibaba submission.

## Relationships

- [[kendryte-k230-neural-network-benchmarks]]: As a benchmark page for a RISC-V AI SoC, the K230 benchmarks illustrate a competing platform's performance; SHL provides the software stack for XuanTie-based CPUs and can be compared in terms of deployment workflow and supported workloads.
- [[spacemit-x60-processor]]: The SpacemiT X60 is another RISC-V processor with AI acceleration; SHL's optimization techniques for XuanTie may be contrasted with the software ecosystem around the X60, including different AI libraries and compiler support.

Insufficient context for additional cross-links to entity pages; only two entity-like pages are available in the wiki_context that are relevant to RISC-V AI hardware.

## Sources

- [SHL README (GitHub - openvinotoolkit/shl)](https://github.com/openvinotoolkit/shl/blob/main/README.md)
- [SHL official page](https://csi-nn2.opensource.alibaba.com/)
- [HHB deployment tool documentation](https://www.yuque.com/za4k4z/kvkcoh)
- [MLPerf Tiny v0.7 results (Alibaba)](https://github.com/mlcommons/tiny_results_v0.7/tree/main/open/Alibaba)
