---
canonical_name: PULP-NN
aliases:
- PULP_NN
- pulp-nn
- PULP-NN library
subtype: null
tags:
- RISC-V
- quantized neural network
- low-power
- parallel computing
hardware_targets:
- PULP Cluster
workloads:
- quantized neural network inference
- convolution
- matrix multiplication
datatypes:
- int8
- mixed-precision
metrics:
- throughput
- energy efficiency
toolchains:
- GCC (RISC-V toolchain)
- pulp-sdk
constraints:
- Xpulp ISA extension
- RISC-V Vector extension (RVV)
- HWC data layout
- CHW data layout
- im2col conversion
evidence_strength: reported
scorecard:
  novelty_delta: 0.8
  claim_density: 0.5
  self_containedness: 0.7
  bridge_score: 0.7
  hub_potential: 0.4
sources:
- raw/cache/b23970a7f296e294.md
- https://github.com/pulp-platform/pulp-nn
source_url: https://github.com/pulp-platform/pulp-nn
fetched_at: '2026-07-02T10:49:32.706001+00:00'
type: optimization_recipe
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 1
---

# PULP-NN: Accelerating Quantized Neural Networks on Parallel Ultra-Low-Power RISC-V Clusters

PULP-NN is a multicore computing library for quantized neural network (QNN) inference on Parallel-Ultra-Low-Power (PULP) clusters of RISC-V processors. The library adopts the Height-Width-Channel (HWC) data layout for activations and weights, decomposes convolution into an im2col step followed by matrix multiplication (MatMul), and exploits the Xpulp ISA extension along with cluster-level parallelism to achieve high throughput and energy efficiency. The 4x2 sized MatMul kernel, which processes two output activations across four channels in parallel, was identified as the optimal structure for data reuse at the register file level. Depthwise convolution uses a CHW layout for inputs and HWC for outputs to maintain efficiency. PULP-NM also includes mixed-precision kernels for sub-byte quantization. The library is evaluated in two research papers and is open-source on GitHub.

## Key Claims

- HWC data layout enables regular memory access patterns for MatMul, avoiding performance degradation from irregular access.
- Decomposing convolution into im2col + MatMul enables efficient execution on microcontroller-class devices.
- The 4x2 MatMul kernel maximizes data reuse at the register file level and delivers the best throughput.
- Depthwise convolution leverages CHW input layout to minimize channel-wise computation overhead, with HWC output to feed subsequent layers.
- The library exploits the SIMD sum-of-dot-products instructions available in the Xpulp ISA extension.
- PULP-NN achieves high energy efficiency (reported in referenced papers) on PULP-based devices.

## Transformation

- Prerequisites: A PULP cluster with RISC-V cores supporting the Xpulp ISA extension (including SIMD dot-product instructions). The cluster must have a shared memory, multiple cores for parallelism, and a software development environment (pulp-sdk, GCC toolchain). The baseline inference approach would be a naive per-layer implementation without these optimizations.
- Steps: (1) Store activations and weights in HWC layout in contiguous memory, grouping channels first then spatial dimensions. (2) For standard and pointwise convolutions, perform im2col to flatten the 3D input feature map into a 1D vector per filter window. (3) Execute matrix multiplication using the 4x2 MatMul kernel, which multiplies two rows of activations by columns of weights to produce two output channels per loop iteration. (4) For depthwise convolution, use CHW layout for inputs and weights, then apply an im2col step on the spatial dimensions, followed by channel-wise MatMul, and store results in HWC layout. (5) Utilize the SIMD dot-product ISA instructions (e.g., p.dsp) within the MatMul kernel to compute multiple parallel dot products per cycle.
- Expected effect: Significant performance improvement (speedup) and energy efficiency gain over baseline implementations, as quantified in the papers (Garofalo et al. 2020, Bruschi et al. 2020). The 4x2 MatMul design specifically maximizes register reuse and minimizes memory traffic.
- Failure modes: The MatMul kernel can blow up memory if memory access patterns are irregular. The HWC layout regularizes accesses to avoid this. Mixed-precision kernels are still in progress for full application testing.
- Measurements: Reported throughput and energy efficiency improvements across various convnet layers; precise numbers are provided in the academic publications. Evidence strength: reported.

## Relationships

- [[earth-shifting-based-vector-memory-access]]: Both PULP-NN and EARTH target performance optimization for data movement on RISC-V architectures, with PULP-NN focusing on NN inference data layouts and EARTH on vector memory access hardware.
- [[cpa-factored-gemmini-systolic-array]]: Both are optimization recipes for accelerating machine learning workloads on RISC-V platforms; PULP-NN addresses software-level kernel optimization while CPA-factored Gemmini targets hardware systolic array efficiency.

## Sources

- [pulp-platform/pulp-nn GitHub Repository](https://github.com/pulp-platform/pulp-nn)
- Garofalo, A., Rusci, M., Conti, F., Rossi, D., & Benini, L. (2020). PULP-NN: accelerating quantized neural networks on parallel ultra-low-power RISC-V processors. *Phil. Trans. R. Soc. A*, 378, 20190155. [arXiv:1908.11263](https://arxiv.org/abs/1908.11263)
- Bruschi, N., Garofalo, A., Conti, F., Tagliavini, G., & Rossi, D. (2020). Enabling Mixed-Precision Quantized Neural Networks in Extreme-Edge Devices. *Proceedings of the 17th ACM International Conference on Computing Frontiers*, pp. 217–220. [arXiv:2007.07759](https://arxiv.org/abs/2007.07759)
