---
cold_start: true
constraints:
- Tensix architecture
- on-chip SRAM
- NoC multicast
created: '2026-06-03'
datatypes: []
evidence_strength: reported
hardware_targets:
- Tenstorrent Wormhole n300
inbound_links: 1
metrics:
- latency reduction
- Pearson Correlation Coefficient
scorecard:
  bridge_score: 0.85
  claim_density: 0.85
  hub_potential: 0.75
  novelty_delta: 0.85
  self_containedness: 0.8
sources:
- https://arxiv.org/abs/2606.09879
tags:
- LLM inference
- operator fusion
- Tensix
- Tenstorrent
- Wormhole
- TT-Metalium
toolchains:
- TT-Metalium
type: optimization_recipe
updated: '2026-06-29'
workloads:
- LLM inference (Qwen2.5-0.5B, Qwen3-0.6B, Qwen3-4B)
---

# Operator Fusion for LLM Inference on the Tensix Architecture

This optimization recipe describes a dataflow- and memory-hierarchy-aware operator fusion strategy for decoder-only Transformer inference on Tenstorrent's Tensix architecture, as proposed by Wu et al. (2026). The strategy fuses RMSNorm with matrix multiplication in self-attention (QKV projection) and in the FFN (first matmul), enabling back-to-back execution of memory-bound and compute-bound operators in on-chip SRAM to reduce DRAM reads/writes of intermediate results. To support multi-core parallelism, a NoC-based row/column multicast mechanism distributes inputs and weights across the core mesh, alleviating DRAM bandwidth contention. Experiments on the Wormhole platform with Qwen2.5-0.5B, Qwen3-0.6B, and Qwen3-4B show up to 37.44% latency reduction for attention and 15.89% for MLP, with up to 7.91% reduction per decoder layer, while PCC remains above 98.75%. The recipe is validated on the Wormhole N300 accelerator.

## Key Claims

- RMSNorm is fused with QKV projection matmuls in self-attention and with the first FFN matmul, executed back-to-back in on-chip SRAM to avoid DRAM writebacks and subsequent reads.
- A NoC-based row/column multicast mechanism distributes inputs and weights across the core mesh, with row/column master nodes alleviating DRAM bandwidth contention.
- Latency reduction up to 37.44% for attention and 15.89% for MLP on Wormhole platform across Qwen models.
- Per-decoder-layer latency reduction up to 7.91%.
- Numerical consistency verified with Pearson Correlation Coefficient above 98.75%.

## Transformation

- Prerequisites: Tenstorrent Tensix architecture (e.g., Wormhole n300), TT-Metalium software stack, and decoder-only Transformer models (e.g., Qwen2.5-0.5B, Qwen3-0.6B, Qwen3-4B).
- Steps:
  1. Identify memory-bound operators (RMSNorm) and compute-bound operators (MatMul) in self-attention and FFN blocks.
  2. Fuse RMSNorm with the following MatMul: in self-attention, fuse RMSNorm with QKV projection; in the second residual block, fuse RMSNorm with the first FFN MatMul.
  3. Execute fused operations back-to-back in on-chip SRAM to keep intermediate results local.
  4. For multi-core parallelism, employ a NoC multicast mechanism: designate row/column master nodes to distribute inputs and weights across the core mesh.
  5. Run the fused kernel on the Tensix cores using the TT-Metalium runtime.
- Expected effect: Reduced DRAM access of intermediate results, lower scheduling overhead, and improved data locality, leading to latency reduction up to 37.44% for attention and 15.89% for MLP, with up to 7.91% reduction per decoder layer, while maintaining numerical consistency (PCC > 98.75%).
- Failure modes: Not explicitly discussed; potential issues include increased register pressure from fusion, limited SRAM capacity constraining fused kernel size, and synchronization overhead in multi-core multicast.
- Measurements: Experiments on Tenstorrent Wormhole N300 with Qwen2.5-0.5B, Qwen3-0.6B, and Qwen3-4B. Reported metrics: latency reduction (percentage) and PCC. Evidence strength: reported (from paper).

## Relationships

- [[Tenstorrent_Wormhole_n300]] – Hardware target used in experiments.
- [[TT_Metalium]] – Software stack used to implement the fused kernels.
- [[Parallel_GEMM_Convolution_on_GAP8]] – Another optimization recipe for a different architecture illustrating similar operator fusion principles.

## Sources

- [Operator Fusion for LLM Inference on the Tensix Architecture – arXiv:2606.09879](https://arxiv.org/abs/2606.09879)
