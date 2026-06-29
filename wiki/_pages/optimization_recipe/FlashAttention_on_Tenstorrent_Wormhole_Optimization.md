---
cold_start: true
constraints:
- Wormhole architecture
- 120 MB L1 memory (on-chip SRAM)
- 288 GB/s DRAM bandwidth
- up to 160W power (n150 system)
- 8x10 grid of Tensix cores with 1.5 MB L1 per core
created: '2025-04-14'
datatypes: []
evidence_strength: reported
hardware_targets:
- Tenstorrent Wormhole n150
inbound_links: 1
metrics:
- speedup
scorecard:
  bridge_score: 0.7
  claim_density: 0.8
  hub_potential: 0.6
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- https://github.com/tenstorrent/tt-metal/blob/main/tech_reports/FlashAttention/FlashAttention.md
tags:
- FlashAttention
- Tenstorrent
- Wormhole
- TT-Metal
- attention
- transformer
toolchains:
- TT-Metalium
type: optimization_recipe
updated: '2026-06-29'
workloads:
- Scaled Dot-Product Attention (SDPA)
---

# FlashAttention on Tenstorrent Wormhole Optimization

This optimization applies the FlashAttention-2 algorithm—parallelizing the Q dimension across multiple Tensix processors and computing online softmax on chunks of K and V—along with kernel-level optimizations from FlashAttention-3, including pipelined data movement and asynchronous execution on Tenstorrent’s Wormhole accelerator through the TT-Metal software stack. The implementation uses Wormhole’s tile-based compute engines and exploits the 120 MB of on-chip SRAM (L1 memory) distributed across a 8x10 grid of Tensix cores, each with 1.5 MB of L1. By fusing the attention computation and overlapping data movement, the recipe avoids round-trips to GDDR6 DRAM (288 GB/s bandwidth) and achieves a reported 20x speedup over baseline sharded scaled dot-product attention on the same Wormhole n150 system. The technique also includes causality-aware parallelization specific to Tensix core scheduling. Failure modes are not explicitly documented but may arise from insufficient L1 space for very long sequences or inefficient batch sizes, though the implementation is used in production for LLMs such as Llama3-70B and Mixtral-8x7B.

## Key Claims

- The FlashAttention implementation on Wormhole achieves a **20x speedup** over the baseline sharded attention implementation on the same hardware.
- The algorithm is derived from FlashAttention-2 (Q parallelization, online softmax) and incorporates optimizations from FlashAttention-3 (asynchronous data movement and compute pipelining).
- Causality-aware load scheduling is adapted to the grid of Tensix cores, allowing efficient handling of causal attention masks.
- Data movement between Tensix cores and DRAM is minimized by using L1 sharding and asynchronous execution, reducing global memory bandwidth load.
- The implementation is open-source, available in the tt-metal repository, and used in production for LLMs including Llama3-70B and Mixtral-8x7B.

## Transformation

- **Prerequisites:** Access to Tenstorrent Wormhole n150 hardware (or similar Wormhole system), the TT-Metal software stack (TT-Metalium), and familiarity with the FlashAttention algorithm.
- **Steps:**
  1. Parallelize the Q matrix across multiple Tensix cores, distributing rows of Q across the grid.
  2. For each core, process chunks of K and V sequentially to compute partial attention scores with online softmax, avoiding materialization of the full attention matrix.
  3. Apply causality-aware scheduling: only process KV chunks that lie within the causal mask, reducing computation for autoregressive decoding.
  4. Overlap data movement (NoC transfers of KV chunks from DRAM or other cores) with computation on the tile-based math engines using the asynchronous RISC-V cores available in each Tensix.
  5. Exploit tile-level matrix operations (32x32 tiles) for efficient matmul, scaling, and softmax.
- **Expected effect:** Significantly reduced global memory reads/writes and fused attention computation, enabling fast inference and training for long sequences. The 20x speedup is measured against a baseline that already uses L1 sharding but without the FlashAttention tiled approach.
- **Failure modes:** Not documented in the source. Potential issues include L1 overflow when sequence lengths exceed available SRAM capacity, overhead from causality scheduling for non-causal attention, and synchronization costs across many cores for very small batch sizes.
- **Measurements:** The source claims a 20x speedup on the Wormhole n150 system for scaled dot-product attention. No breakdown by sequence length or batch size is provided. The evidence strength is classified as *reported* because the measurement context (workload shape, specific attention variant, batch size) is not detailed in the technical report.

## Relationships

- [[Tenstorrent_Wormhole_n150]] – Hardware target for which this optimization is designed.
- Insufficient context for additional cross-links; no existing entity pages for attention algorithms or Tenstorrent software are present in the current wiki.

## Sources

- [tt-metal/tech_reports/FlashAttention/FlashAttention.md at main (GitHub)](https://github.com/tenstorrent/tt-metal/blob/main/tech_reports/FlashAttention/FlashAttention.md)
