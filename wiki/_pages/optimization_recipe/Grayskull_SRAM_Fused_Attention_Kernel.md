---
cold_start: false
constraints:
- SRAM-only execution
- Fused kernel combining matmul, scaling, and Softmax
- Quadratic time and memory complexity in sequence length
created: '2025-04-09'
datatypes:
- Bfloat16
evidence_strength: reported
hardware_targets:
- Tenstorrent Grayskull e150
inbound_links: 1
metrics:
- speedup
needs_summary_revision: false
scorecard:
  bridge_score: 0.6
  claim_density: 0.9
  hub_potential: 0.5
  novelty_delta: 0.9
  self_containedness: 0.8
sources:
- https://arxiv.org/abs/2407.13885
tags:
- Tenstorrent
- Grayskull
- attention
- Softmax
- SRAM
- fusion
toolchains:
- TT-Metalium
- TT-Buda
type: optimization_recipe
updated: '2026-06-29'
workloads:
- Self-attention (Softmax)
- Matrix multiplication (QK^T)
---

# Grayskull SRAM Fused Attention Kernel

The Grayskull SRAM Fused Attention Kernel is an optimization recipe that implements the self-attention mechanism of Transformers entirely within the SRAM of the Tenstorrent Grayskull e150 accelerator. By combining matrix multiplication (QK^T), attention score scaling, and Softmax into a single fused kernel, the recipe eliminates the overhead of dispatching multiple kernels and moving intermediate results between DRAM and SRAM. The prerequisite hardware is the Tenstorrent Grayskull e150 with its 120 MB distributed SRAM. The implementation uses TT-Metalium or TT-Buda for kernel programming. The expected effect is a significant speedup over CPU-based implementations: the dedicated Softmax kernel achieves up to a 10× speedup, and the fused kernel performs approximately 1.8× faster than the dedicated Softmax kernel alone. The recipe maintains quadratic time and memory complexity with sequence length, but within the SRAM budget the kernel avoids DRAM accesses for the attention computation. No failure modes are discussed in the source. Measurements are reported from the paper.

## Key Claims

- The fused kernel that combines matrix multiplication, scaling, and Softmax in SRAM on the Grayskull e150 achieves an approximately 1.8× speedup over a dedicated Softmax kernel implemented in SRAM.
- The dedicated Softmax kernel achieves up to a 10× speedup compared to a CPU baseline implementation.
- Both kernels operate entirely within the Grayskull's SRAM, avoiding DRAM traffic for the attention-weight computation.

## Transformation

- Prerequisites: Tenstorrent Grayskull e150 hardware; TT-Buda or TT-Metalium software stack; workload in Bfloat16 tile format (32×32 tiles).
- Steps:
  1. Partition the attention computation across Tensix cores using the dataflow architecture.
  2. Load queries and keys from DRAM into per-core SRAM buffers.
  3. Execute matrix multiplication (QK^T) on the compute engine's FPU in Bfloat16.
  4. Scale the attention scores by 1/sqrt(d_k) using the vector engine (SFPU).
  5. Apply Softmax using the dedicated or fused kernel, with tiling if necessary to fit within SRAM.
  6. In the fused variant, perform steps 3–5 without intermediate DRAM writes, keeping all data in SRAM.
- Expected effect: Up to 10× speedup over CPU for Softmax, and additional 1.8× improvement from fusion.
- Failure modes: Not discussed in the source. Possible issues include SRAM capacity overflow for long sequences, NoC congestion for large-scale parallelization, and precision loss due to Bfloat16 formatting.
- Measurements: Reported in the paper (arXiv:2407.13885). Specific testbed and CPU baseline not detailed beyond "CPU implementation serving as a baseline."

## Relationships

- [[Tenstorrent_Grayskull_e150]] – The hardware target required for this optimization.
- [[Gemmini_Architecture]] – A contrasting DNN accelerator architecture (systolic array) vs. the dataflow grid approach of Grayskull.

## Sources

- arXiv:2407.13885 – Attention in SRAM on Tenstorrent Grayskull
