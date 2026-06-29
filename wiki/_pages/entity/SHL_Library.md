---
cold_start: true
created: '2025-01-29'
inbound_links: 0
scorecard:
  bridge_score: 0.7
  claim_density: 0.6
  hub_potential: 0.5
  novelty_delta: 0.7
  self_containedness: 0.9
sources:
- https://zhangwm-pt.github.io/shl/md_README.html
tags:
- SHL
- T-HEAD
- XuanTie
- heterogeneous computing
- CSI-NN2
- neural network library
type: entity
updated: '2026-06-29'
---

# SHL (Structure of Heterogeneous Library)

SHL (Structure of Heterogeneous Library, Chinese name: ShiHulan) is a high-performance heterogeneous computing library developed by T-HEAD that provides optimized binary libraries for XuanTie CPU platforms. The library's interface is based on the CSI-NN2 (T-HEAD neural network library API), offering both reference C code implementations and assembly-optimized routines specifically tuned for XuanTie CPUs. SHL supports symmetric and asymmetric quantization, works with 8-bit, 16-bit, and half-precision (f16) data types, and is compatible with both NCHW and NHWC data formats. It includes reference heterogeneous scheduling implementations and can be automatically invoked via the HHB deployment tool, covering different architectures including CPU and NPU. In principle, SHL provides only the reference implementation for XuanTie CPU platforms, while optimization for each NPU target platform is completed by the vendor of the specific platform.

## Key Claims

- SHL provides a high-level API based on CSI-NN2 for T-HEAD's XuanTie CPU family.
- It includes both reference C implementations and assembly-optimized implementations for XuanTie CPUs.
- Supports symmetric and asymmetric quantization for neural network inference.
- Data type support includes 8-bit, 16-bit, and half-precision (f16).
- Compatible with NCHW and NHWC data formats.
- The HHB tool can automatically call SHL API for model deployment.
- Covers heterogeneous architectures including CPU and NPU.
- Binary libraries and source build instructions are available; examples include running MobileNetV1 on a C906-based development board (e.g., D1).
- BN fusion is expected to be performed prior to using the provided example code.

## Relationships

- [[TVM_CSINN2_Integration_Optimization_Recipe]] – This optimization recipe describes integration of CSI-NN2 (the underlying library used by SHL) with Apache TVM for RISC-V CPUs with vector extensions, targeting the same XuanTie C906 hardware.
- Insufficient context for additional cross-links to entity pages; only one suitable related page is available in the current wiki context.

## Sources

- [SHL README on GitHub Pages](https://zhangwm-pt.github.io/shl/md_README.html)

