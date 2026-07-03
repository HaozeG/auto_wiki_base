---
canonical_name: Systolic Tensor Units
aliases:
- STU
- systolic array unit
- tensor systolic array
subtype: null
tags:
- systolic array
- tensor unit
- TPU
- accelerator
scorecard:
  novelty_delta: 0.6
  claim_density: 0.3
  self_containedness: 0.4
  bridge_score: 0.2
  hub_potential: 0.5
sources:
- raw/cache/c6cd3341b0edc494.md
- https://www.emergentmind.com/topics/systolic-tensor-units
source_url: https://www.emergentmind.com/topics/systolic-tensor-units
fetched_at: '2026-07-02T05:48:46.491932+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: false
inbound_links: 1
needs_summary_revision: false
outbound_links:
- target: gemmini
  reason: An open-source framework for generating systolic array-based DNN accelerators,
    closely related to the systolic tensor unit concept
- target: xuantie_c908_fp16_gemm_kernel
  reason: A GEMM micro-kernel that can be mapped to systolic array hardware, demonstrating
    the connection between systolic tensor units and optimized matrix multiplication
    kernels
---

# Systolic Tensor Units

Systolic tensor units are 2D tiled arrays of processing elements optimized for high-throughput matrix and tensor operations, supporting both dense and sparse computations. These units are used in hardware accelerators such as Google's Tensor Processing Unit (TPU), which employs a systolic array to accelerate matrix multiplication using a dataflow operation. Each processing element (PE) in the array performs multiply-and-accumulate (MAC) operations. The TPU v4, announced in May 2021, achieved over 2x performance improvement over TPU v3 chips through enhancements in the systolic array and associated data movement. The architecture relies on tensor DMA engines to decode and execute DMA instructions, offloading work from the main TensorCore to dedicated hardware for efficient memory access.

## Key Claims

- Systolic tensor units are 2D tiled arrays of processing elements designed for high-throughput matrix and tensor operations with support for both dense and sparse computations.
- Google TPU v4 demonstrated a performance improvement of more than 2x over TPU v3 chips, as stated by CEO Sundar Pichai at Google I/O 2021.
- Each PE in a systolic array is responsible for multiply-and-accumulate (MAC) operations, and the array uses dataflow operation to accelerate matrix computation.
- Tensor DMA engines decode and execute DMA instructions to offload work from the main TensorCore.

## Relationships

- [[gemmini]]: An open-source framework for generating systolic array-based DNN accelerators, closely related to the systolic tensor unit concept.
- [[xuantie_c908_fp16_gemm_kernel]]: A GEMM micro-kernel that can be mapped to systolic array hardware, demonstrating the connection between systolic tensor units and optimized matrix multiplication kernels.

## Sources

- https://www.emergentmind.com/topics/systolic-tensor-units
