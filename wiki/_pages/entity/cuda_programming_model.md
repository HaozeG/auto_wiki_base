---
type: entity
tags: [gpu, cuda, nvidia, parallel-programming, memory-hierarchy]
sources:
  - "NVIDIA CUDA C++ Programming Guide (v12.x). https://docs.nvidia.com/cuda/cuda-c-programming-guide/"
  - "NVIDIA H100 Tensor Core GPU Architecture Whitepaper (2022)."
  - "Choquette, J. et al. (2021). NVIDIA A100 Tensor Core GPU: Performance and Innovation. IEEE Micro."
created: 2026-06-26
updated: 2026-06-26
cold_start: false
inbound_links: 0
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# CUDA Programming Model

CUDA (Compute Unified Device Architecture) is NVIDIA's parallel programming platform, first released in 2007, that exposes GPU hardware through a hierarchical thread-block-grid abstraction. A CUDA kernel launches a **grid** of **thread blocks**, where each thread block contains up to 1024 threads that share a fast on-chip **shared memory** (SRAM) and can synchronize via barriers. Threads within a block are scheduled in groups of 32 called **warps**; all 32 threads in a warp execute the same instruction simultaneously (SIMT execution), so divergent branches cause serialization. Thread blocks are assigned to **Streaming Multiprocessors (SMs)** — the fundamental compute units of the GPU. The H100 SXM5 GPU contains 132 SMs, each with 256 KB of configurable L1/shared memory (up to 228 KB usable as shared memory per SM). Global memory corresponds to the GPU's HBM (High Bandwidth Memory), which on H100 SXM5 provides 3.35 TB/s bandwidth but incurs hundreds of nanoseconds of latency per access. Shared memory latency is approximately 20–30 cycles (~5 ns). Correct use of the CUDA memory hierarchy — minimizing global memory traffic by staging data in shared memory — is the central discipline of GPU kernel optimization and directly maps to improving a kernel's arithmetic intensity as defined by the Roofline model.

## Key Claims

- The H100 SXM5 GPU has 132 Streaming Multiprocessors (SMs); each SM contains 4 warp schedulers and can concurrently execute up to 64 warps (2048 threads per SM), yielding a maximum of 132 × 2048 = 270,336 concurrent threads.
- Each SM on H100 has 256 KB of combined L1 data cache and shared memory, configurable so that up to 228 KB is usable as programmer-managed shared memory (SMEM), compared to 164 KB on A100.
- A warp consists of exactly 32 threads; all 32 execute in lockstep. Branch divergence within a warp causes the two paths to serialize, halving throughput in the worst case of a 50/50 branch.
- **Memory coalescing**: when all 32 threads in a warp access consecutive 4-byte addresses, the hardware merges them into a single 128-byte global memory transaction; uncoalesced access can increase effective memory traffic by up to 32×.
- **Occupancy** is the ratio of active warps per SM to the maximum (64 on H100); low occupancy due to large register use or large shared memory allocation reduces the GPU's ability to hide memory latency through warp switching.
- The WMMA (Warp Matrix Multiply Accumulate) API and its successor `mma.sync` PTX instructions expose H100 Tensor Cores, which perform 16×8×16 FP16 matrix multiply-accumulate operations in a single warp instruction, delivering up to 989 TFLOP/s peak FP16 throughput.
- **CUDA Streams** enable overlapping of data transfer (H2D/D2H via NVLink or PCIe) with kernel execution; H100's third-generation NVLink provides 900 GB/s bidirectional bandwidth between GPUs in an NVL8 configuration, making stream overlap essential for multi-GPU pipelines.

## Relationships

- [[nvidia_hopper_h100]] — H100 is the current flagship CUDA device; its SM count (132), shared memory per SM (228 KB usable), and Tensor Core throughput (989 TFLOP/s FP16) are the concrete parameters referenced in CUDA occupancy and performance analysis.
- [[roofline_model_arithmetic_intensity]] — The CUDA memory hierarchy (shared memory vs. global/HBM) is the mechanism through which programmers improve arithmetic intensity; tiling algorithms stage data in shared memory to reduce HBM traffic, shifting kernels toward the compute roof.
- [[openai_triton]] — Triton compiles Python-level tile programs to PTX, auto-managing shared memory allocation, warp tiling, and memory coalescing that must be hand-coded in CUDA; Triton's abstractions map directly to CUDA SM resources.
- [[flash_attention]] — FlashAttention's core implementation relies on CUDA shared memory tiling of Q, K, V matrices per SM to avoid round-trips to HBM, achieving IO-awareness through explicit CUDA memory hierarchy management.
- [[hbm_high_bandwidth_memory]] — HBM is the physical implementation of CUDA global memory; its bandwidth (3.35 TB/s on H100) sets the memory roof and motivates shared memory reuse in high-performance kernels.

## Sources

- NVIDIA CUDA C++ Programming Guide (v12.x). https://docs.nvidia.com/cuda/cuda-c-programming-guide/
- NVIDIA H100 Tensor Core GPU Architecture Whitepaper (2022). https://resources.nvidia.com/en-us-tensor-core
- Choquette, J. et al. (2021). "NVIDIA A100 Tensor Core GPU: Performance and Innovation." *IEEE Micro*, 41(2), 29–35.
- CUDA Best Practices Guide — Occupancy. https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/index.html#occupancy
