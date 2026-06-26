---
type: entity
tags: [ai-accelerator, systolic-array, google, tpu, trillium, v6e, training, inference]
sources:
  - https://cloud.google.com/blog/products/compute/introducing-trillium-6th-gen-tpus
  - https://docs.cloud.google.com/tpu/docs/v6e
  - https://www.nextplatform.com/2024/06/10/lots-of-questions-on-googles-trillium-tpu-v6-a-few-answers/
  - https://introl.com/blog/google-tpu-architecture-complete-guide-7-generations
  - https://www.spheron.network/blog/google-tpu-trillium-v6-vs-nvidia-b200-llm-inference/
created: 2026-06-26
updated: 2026-06-26
cold_start: true
inbound_links: 0
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# Google Trillium (TPU v6e)

Google Trillium, also designated TPU v6e, is the sixth-generation Tensor Processing Unit chip announced at Google I/O 2024 and made generally available in late 2024. It represents Google's most significant architectural leap between consecutive TPU generations since the v2 transition and is the first generation to double the Matrix Multiply Unit (MXU) size back to 256×256 multiply-accumulate units — the same width as TPU v1's INT8 array — but now operating in bfloat16 with FP32 accumulation. The expanded MXU quadruples the number of multiply-accumulate operations per cycle compared to the 128×128 arrays used in TPU v2 through v5p. Trillium delivers a 4.7× increase in peak compute performance per chip relative to TPU v5e, reaching approximately 918 TFLOPS of BF16 compute per chip. It carries 32 GB of HBM per chip (doubling v5e capacity) and doubles the inter-chip interconnect (ICI) bandwidth to 3,200 Gbps per chip versus v5e. Energy efficiency is more than 67% better than v5e per unit of compute. The chip includes a third-generation SparseCore for accelerating embedding-table lookups common in recommendation models, with variable SIMD width (8 elements for FP32, 16 for bfloat16) and improved memory-access patterns that reduce wasted bandwidth from misaligned reads.

## Key Claims

- Trillium's MXU expanded from 128×128 to 256×256 multiply-accumulate units, quadrupling the MACs per cycle relative to TPU v2–v5p; this is the first return to a 256-wide array since TPU v1's INT8 design.
- Peak BF16 compute performance is approximately 918 TFLOPS per chip — a 4.7× improvement over TPU v5e on a per-chip basis.
- HBM capacity is 32 GB per chip; a four-chip Trillium slice aggregates 128 GB across chips, double the per-chip HBM of v5e.
- ICI bandwidth doubled to 3,200 Gbps per chip compared to v5e, enabling larger batch coordination across chips without communication stalls.
- Trillium is more than 67% more energy-efficient than TPU v5e per unit of BF16 compute, reducing per-TFLOP power cost substantially.
- The third-generation SparseCore introduced variable SIMD width (8 elements for FP32, 16 for bfloat16) and improved memory-access patterns targeting embedding workloads in recommendation systems — a workload class poorly served by dense systolic arrays.
- Trillium was announced at Google I/O 2024 and became the foundational training chip for subsequent Gemini model iterations deployed internally and on Google Cloud.

## Relationships

- [[google_tpu]] — Trillium is the sixth generation of the Google TPU family; it builds on the MXU systolic array design lineage and the ICI interconnect fabric established across v1–v5p.
- [[gemmini]] — Gemmini and TPU/Trillium share systolic array dataflow principles; Trillium's 256×256 MXU is an industry-scale realization of the same matrix-multiply building block Gemmini studies academically.
- [[tenstorrent]] — Tenstorrent and Google Trillium are competing datacenter AI ASICs; Trillium's SparseCore targets recommendation workloads similarly to how Tenstorrent Blackhole targets diverse model types.

## Sources

- Google Cloud Blog, "Introducing Trillium, sixth-generation TPUs." https://cloud.google.com/blog/products/compute/introducing-trillium-6th-gen-tpus — 4.7× performance claim, energy efficiency, ICI doubling, announcement at Google I/O 2024.
- Google Cloud TPU v6e documentation. https://docs.cloud.google.com/tpu/docs/v6e — MXU 256×256 size, 32 GB HBM, 3,200 Gbps ICI, SparseCore SIMD widths.
- Next Platform, "Lots Of Questions On Google's Trillium TPU v6." https://www.nextplatform.com/2024/06/10/lots-of-questions-on-googles-trillium-tpu-v6-a-few-answers/ — architectural context and generational comparison.
- Introl Blog, "Google TPU Architecture: 7 Generations Explained." https://introl.com/blog/google-tpu-architecture-complete-guide-7-generations — cross-generation MXU size comparison and BF16 TFLOPS figures.
