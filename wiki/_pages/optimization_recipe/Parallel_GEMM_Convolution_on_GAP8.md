---
cold_start: false
constraints:
- scratchpad memory hierarchy requiring explicit DMA transfers
- 1+8 core heterogeneous architecture
- limited memory capacity for edge devices
created: '2024-02-19'
datatypes:
- INT8
evidence_strength: reported
hardware_targets:
- GAP8 (PULP platform)
inbound_links: 12
metrics:
- latency
- throughput
- bandwidth
- power
- energy
needs_summary_revision: true
scorecard:
  bridge_score: 0.8
  claim_density: 0.7
  hub_potential: 0.6
  novelty_delta: 0.9
  self_containedness: 0.8
sources:
- https://link.springer.com/article/10.1007/s11227-024-05927-y
tags:
- RISC-V
- GAP8
- convolution
- GEMM
- IM2COL
- IM2ROW
- ultra-low power
- edge AI
- parallel computing
toolchains: []
type: optimization_recipe
updated: '2026-06-28'
workloads:
- Convolution (im2col/im2row)
- GEMM
---

# Parallel GEMM-Based Convolution on GAP8

This optimization recipe transforms the convolution operator into a general matrix-matrix multiplication (GEMM) using the im2col (or im2row) lowering approach, adapted for the GAP8 parallel ultra-low power platform (PULP). The GAP8 features a fabric controller (FC) and eight compute cores with scratchpad memory and DMA support. The transformation applies tiling and loop parallelism to the GEMM kernel, using 8-bit integer (INT8) arithmetic and the dot product instruction available on the platform. Data movements are carefully orchestrated via DMA transfers across the four-level memory hierarchy. The paper reports that this approach achieves reasonable performance on the GAP8, though specific numerical results are not available in the extracted resource content. The expected effect is an efficient convolution implementation for deep neural network inference on edge IoT devices.

## Key Claims

- Convolution is lowered to GEMM via im2col or im2row transforms, enabling reuse of optimized matrix multiplication kernels.
- Implementation uses INT8 arithmetic to exploit the GAP8's dot product support.
- Parallelization distributes work across all eight compute cores; the fabric controller manages DMA transfers.
- Tiling and loop parallelism are adapted from cache-aware GEMM to the scratchpad-based memory hierarchy.
- The approach is experimentally evaluated; results are reported in the original paper but not extracted here.

## Transformation

- Prerequisites: GAP8 platform (fabric controller + 8 compute cores), INT8 dot product support, DMA capability, and a compiler supporting the RISC-V target.
- Steps:
  1. Lower the convolution operator to GEMM via im2col or im2row data layout transformation.
  2. Implement a blocked GEMM algorithm with tiling parameters tuned for the GAP8 scratchpad sizes.
  3. Use the fabric controller to coordinate data movement (packing/unpacking buffers) via DMA.
  4. Execute the GEMM micro-kernel on the eight compute cores in parallel, performing INT8 dot products.
  5. Apply loop parallelism and reduce memory bandwidth contention through careful scheduling.
- Expected effect: Efficient convolution inference for deep learning on edge devices, with performance limited by memory bandwidth and scratchpad capacity. The paper demonstrates that adapting cache-based GEMM techniques to a scratchpad architecture yields reasonable performance.
- Failure modes: Not explicitly discussed; likely include DMA transfer overhead, limited scratchpad size causing additional data movement, and synchronization costs between cores.
- Measurements: The paper states a complete experimental evaluation was performed comparing im2col and im2row variants, but specific numerical results (latency, throughput, power) are not present in the extracted content. Evidence strength is classified as reported based on the paper's claims.

## Relationships

- [[GAP8_PULP_Processor]] – The hardware target for which this optimization is designed.
- [[GEMM_with_RISC-V_Vector_Extension]] – A contrasting GEMM implementation using standard RISC-V vector extensions, highlighting the differences between vector and scratchpad approaches.

## Sources

- [Parallel GEMM-based convolution for deep learning on multicore RISC-V processors – Springer](https://link.springer.com/article/10.1007/s11227-024-05927-y)

