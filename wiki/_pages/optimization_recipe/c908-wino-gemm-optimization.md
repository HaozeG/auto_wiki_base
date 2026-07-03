---
canonical_name: null
aliases: null
subtype: null
tags: []
hardware_targets:
- XuanTie C908
workloads:
- Convolution (CNN)
- GEMM
datatypes:
- FP16
- INT8
metrics:
- computational efficiency
- instruction throughput
toolchains:
- SHL
constraints:
- VLEN 128
- register blocking 16x12
- instruction fusion
evidence_strength: reported
scorecard:
  novelty_delta: 1.0
  claim_density: 0.9
  self_containedness: 0.8
  bridge_score: 0.6
  hub_potential: 0.3
sources:
- raw/cache/73bedd2221cd9a03.md
- https://riscv.org/blog/xuantie-c908-accelerates-ai-with-software-and-hardware-fusion/
source_url: https://riscv.org/blog/xuantie-c908-accelerates-ai-with-software-and-hardware-fusion/
fetched_at: '2026-07-03T13:28:59.802023+00:00'
type: optimization_recipe
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 8
outbound_links:
- target: shl
  reason: SHL is the library implementing these optimization techniques for the XuanTie
    C908
---

# C908 Winograd and GEMM Optimization in SHL

The Structure of Heterogeneous Library (SHL) implements optimized convolution algorithms for the XuanTie C908 processor, including the im2col + GEMM approach and the Winograd algorithm. The primary optimization technique involves a carefully tuned GEMM kernel that uses vector loads for weight data and scalar loads for input data, with a 16x12 register blocking scheme to maximize computational efficiency via outer product matrix multiplication. Manual instruction scheduling removes read-after-write and write-after-write data dependencies, and instruction fusion technology is applied to further optimize the instruction flow. This recipe is reported by T-Head in a 2022 blog post and has not been independently verified.

## Key Claims

- SHL supports im2col + GEMM and Winograd for convolution acceleration on XuanTie C908.
- The GEMM kernel uses vector load (vle) for weights and scalar load (flh) for inputs.
- A 16x12 register block design improves computational efficiency via outer product matrix operations.
- Manual removal of data dependencies (RAW, WAW) optimizes instruction flow.
- Advanced instruction fusion technology is incorporated to fully optimize performance.
- The optimized operators list includes conv2d, depthwiseconv2d, maxpool2d, avgpool2d, global_maxpool2d, global_avgpool2d, fullyconnected, relu, relu6, leaky_relu, prelu, sigmoid, softmax, concat, pad, elementwise_add, elementwise_mul, sum.

## Transformation

- Prerequisites: XuanTie C908 processor with RVV 1.0 support; SHL library; understanding of convolution algorithm (im2col or Winograd).
- Steps: (1) Input padding, (2) Input transformation, (3) Input reordering, (4) Batch GEMM operations, (5) Output transformation, (6) Output cropping (for Winograd). For GEMM: use vector load for weights, scalar load for inputs; apply 16x12 register blocking; remove RAW/WAW dependencies; apply instruction fusion.
- Expected effect: Improved convolution inference performance, up to 3.75-4.57x overall vs C906.
- Failure modes: Not specified; may require exact register arrangement and instruction scheduling to avoid pipeline stalls.
- Measurements: Not provided as isolated measurements; overall system benchmarks available on the benchmark result page.

## Relationships

- [[shl]]: SHL is the library implementing these optimization techniques for the XuanTie C908.

## Sources

- https://riscv.org/blog/xuantie-c908-accelerates-ai-with-software-and-hardware-fusion/
