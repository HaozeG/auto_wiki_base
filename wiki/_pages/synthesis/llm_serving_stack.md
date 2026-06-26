---
type: synthesis
connected_entities: [kv_cache_llm_inference, flash_attention, mixture_of_experts_moe_llm, int8_fp8_quantization_llm_inference, groq_lpu, sambanova_sn40l, nvidia_hopper_h100, transformer_architecture]
synthesis_status: draft
created: 2026-06-26
updated: 2026-06-26
cold_start: false
inbound_links: 0
scorecard:
  bridge_score: ~
  contradiction_potential: ~
  cross_domain_connection: ~
---

# The LLM Serving Stack: From Tokens to Hardware Utilization

## RAG Summary

High-throughput LLM serving requires co-optimizing across five interdependent layers — model architecture (MoE, GQA), numerical formats (FP8/INT8), memory management (KV cache paging, prefix caching), scheduling (continuous batching, speculative decoding), and hardware selection (memory-bandwidth vs. compute-bound) — and the efficiency gains from each layer multiply rather than add. The transformer architecture's autoregressive decode phase is memory-bandwidth-bound, not compute-bound: on the NVIDIA H100 SXM5 with 3.35 TB/s HBM3e bandwidth, arithmetic intensity during decode sits below 10 FLOP/byte against a hardware ridge point of roughly 140 FLOP/byte. Techniques that address this bottleneck compound: Grouped Query Attention (GQA) cuts KV cache size 8× in LLaMA-2 70B; FP8 quantization halves memory bandwidth per weight byte while doubling Tensor Core throughput on H100 (3,958 vs. 1,979 TFLOPS); PagedAttention eliminates up to 55% of fragmentation waste; and continuous batching raises GPU utilization from 30–40% to 70–90%. MoE architectures like Mixtral 8×7B (46.7B total, 12.9B active parameters) further reduce per-token compute while introducing expert-parallelism communication overhead. Hardware diversity reflects these trade-offs: the Groq LPU removes the HBM bottleneck entirely with 230 MB on-chip SRAM at 80 TB/s, achieving 1,300+ tokens/second on Llama 3 8B; the SambaNova SN40L adds DDR5 as a third memory tier to host trillion-parameter MoE models that no GPU cluster can fit in HBM alone.

---

## Full Synthesis

### The Serving Stack as a Layered Optimization Problem

LLM serving is not a single optimization target but a stack of interacting constraints. The transformer architecture defines the computational structure: O(n²) attention during prefill, O(n) per-step cost during decode (with KV caching), and two-thirds of parameters in feed-forward layers. Each of these phases has a different bottleneck: prefill is compute-bound (large matrix multiplications over the full prompt), while decode is memory-bandwidth-bound (loading all model weights and KV cache state from HBM for each new token). The serving system must manage both modes simultaneously for a diverse population of concurrent requests.

The five optimization layers are:

**Layer 1 — Model Architecture.** The transformer's attention sublayer generates KV cache that scales as 2 × n_layers × seq_len × n_kv_heads × head_dim × bytes_per_element. LLaMA-2 70B's adoption of GQA (8 KV heads instead of 64) cuts this by 8× to approximately 0.32 MB per token per sequence. MoE architectures (Mixtral 8×7B, DeepSeek-V2) trade dense compute for sparse activation: Mixtral activates ~12.9 billion of 46.7 billion parameters per token, achieving LLaMA-2 70B quality at roughly 2× the throughput. However, MoE does not reduce attention KV cache — the attention layers remain dense — and introduces all-to-all expert routing communication that can consume 30–40% of step time at scale.

**Layer 2 — Numerical Formats.** INT8 and FP8 quantization addresses memory-bandwidth pressure from both model weights and KV cache. NVIDIA H100 FP8 Tensor Cores deliver 3,958 TFLOPS, exactly 2× the FP16 rate, while FP8 also halves the bytes transferred from HBM per weight element. SmoothQuant enables accurate INT8 weight-and-activation quantization for GPT-3-scale models with less than 1% accuracy loss. AWQ achieves INT4 compression of LLaMA-2 70B (140 GB → 35 GB) with a 2.36-point WikiText-2 perplexity gap — a 4× footprint reduction for roughly 7% quality degradation. KV cache quantization to INT8 or FP8 further halves the cache memory footprint, with KVQuant demonstrating under 1% quality degradation at INT4.

**Layer 3 — Memory Management.** Even with GQA and quantization, KV cache fragmentation and reservation waste are severe at scale. A batch of 512 sequences at 4096 tokens in FP16 with LLaMA-2 70B's GQA-8 requires roughly 164 GB of KV cache, near the limit of two H100 GPUs. PagedAttention (vLLM, SOSP 2023) partitions KV cache into fixed OS-page-style blocks, reducing fragmentation and enabling copy-on-write for parallel sampling, recovering up to 55% of previously wasted capacity. Prefix caching (also implemented in vLLM) allows KV cache computed for shared prompt prefixes to be reused across requests — a significant gain for chatbot applications with system prompts shared across millions of queries.

**Layer 4 — Scheduling.** Static batching allocates a GPU for the maximum possible sequence length of each request, leaving compute idle during shorter requests. Continuous batching (Orca, OSDI 2022) replaces batch boundaries with per-iteration scheduling: as soon as a sequence slot frees up, a new request is inserted. This raises GPU utilization from roughly 30–40% to 70–90% in throughput benchmarks. Speculative decoding — generating candidate tokens with a small draft model and verifying with the large model — trades extra compute for lower latency at low batch sizes.

**Layer 5 — Hardware Selection.** The choice of hardware fundamentally determines which bottlenecks are tractable. The H100's 3.35 TB/s HBM3e and 900 GB/s NVLink position it as the reference platform for large-batch training-grade throughput. The Groq LPU eliminates the HBM bottleneck structurally: with 230 MB on-chip SRAM at 80 TB/s internal bandwidth, KV cache is held on-chip and each token generation is deterministic, delivering over 1,300 tokens/second on Llama 3 8B — more than 13× a comparable H100 deployment at low batch size. The SambaNova SN40L targets the opposite corner of the design space: by adding a DDR5 tier (1.5 TB per socket), it can host trillion-parameter MoE models with CoE (Composition of Experts), achieving 3.7× throughput over DGX H100 for that specific workload.

### Multiplicative Compounding of Efficiency Gains

The gains from each layer compound multiplicatively rather than additively when co-optimized:

- GQA-8 (8× KV reduction) × FP8 quantization (2× memory per element) = 16× reduction in KV cache bandwidth demand, without any change to attention compute quality.
- Continuous batching (2–3× utilization improvement) × PagedAttention (reduces waste by ~55%) × FP8 weights (2× weight-load throughput) can yield 4–6× end-to-end throughput over a naive FP16 static-batching baseline, with KV cache as the binding constraint relaxed at each step.
- FlashAttention-3 on H100 reaches 740–760 TFLOPS (75% of theoretical peak) by combining IO-aware tiling with asynchronous execution; when combined with FP8 attention computation, this collapses prefill bottlenecks that would otherwise saturate compute before memory.

### Hardware Diversity as a Reflection of Stack-Layer Trade-offs

The current market diversity in LLM inference hardware is not redundancy — it reflects genuinely different points in the serving-stack trade-off space:

| Hardware | Memory Bandwidth | Weight Capacity | Latency Model | Primary Target |
|---|---|---|---|---|
| H100 SXM5 | 3.35 TB/s HBM3e | 80 GB per chip | Throughput-optimized | Large batch, training-class |
| Groq LPU | 80 TB/s SRAM | 230 MB per chip | Deterministic, latency-optimized | Low-batch, latency-critical |
| SambaNova SN40L | SRAM + 2 TB/s HBM3 + 200+ GB/s DDR5 | ~1.5 TB per socket | Capacity-optimized | Trillion-param MoE, enterprise |

The H100 must rely on software techniques (FlashAttention, vLLM, quantization) to compensate for HBM's architectural gap with on-chip SRAM bandwidth. The Groq LPU avoids the software complexity but requires models to fit in 230 MB; scaling to 70B models requires multi-chip systems. The SN40L's DDR5 tier accepts latency penalties on cold-weight access but achieves weight capacities unreachable by GPU clusters of similar rack footprint.

### Tensions and Unresolved Interactions

MoE architectures expose a tension with all-SRAM hardware: the Groq LPU's deterministic scheduling requires full weight residency, but MoE models' sparse activation means most weights sit idle at any step. SambaNova's DDR-backed CoE is more natural for MoE workloads. Meanwhile, speculative decoding assumes a draft model that runs faster than the target model, which is structurally simple on GPUs (draft = small dense model) but complex on Groq (requires separate compiled programs with deterministic timing).

Quantization interacts differently with attention and feed-forward layers. Weight-only quantization (GPTQ, AWQ) targets feed-forward parameters, which are static; KV cache quantization targets dynamic, per-request data. Combining both requires separate calibration paths and error accounting — the techniques are complementary but not trivially composable.

## Open Questions

- **MoE + speculative decoding compatibility:** Speculative decoding with a MoE target model is underexplored. The sparse expert activation pattern means draft tokens must pass through different subsets of experts than verification tokens, creating load-balancing mismatches. No production system had resolved this cleanly as of mid-2026.
- **Bandwidth wall at context length scaling:** As context lengths push toward 1M tokens (enabled by RoPE generalization and ring-attention techniques), the KV cache for a single long-context request can exceed entire GPU memory even with GQA and FP8. Whether software-only techniques (prefix caching, partial offload) can close the gap, or whether fundamentally different architectures (state-space models, linear attention) are required, remains open.
- **Cross-layer co-design:** All five optimization layers are currently tuned largely independently by different teams (model researchers for architecture, systems researchers for scheduling, hardware engineers for quantization support). There is no established framework for joint optimization — e.g., co-designing GQA group count with PagedAttention block size with FP8 KV cache granularity. Optimal joint configurations are almost certainly different from the union of separately optimal choices.
- **Groq LPU scaling for MoE:** Groq's deterministic architecture requires all weights to be resident at compile time, which conflicts with MoE's value proposition (sparse activation over large weight sets). Whether Groq can adapt its static-scheduling model to support dynamic expert selection without sacrificing determinism is not publicly resolved.

## Connected Pages

- [[transformer_architecture]] — baseline computational structure whose O(n²) attention and feed-forward parameter dominance define the serving problem
- [[kv_cache_llm_inference]] — memory structure whose bandwidth and capacity dominate decode-phase throughput; GQA and PagedAttention are the primary mitigations
- [[flash_attention]] — IO-aware attention kernel that eliminates O(n²) HBM materialization during prefill; FlashAttention-3 reaches 75% of H100 theoretical peak
- [[mixture_of_experts_moe_llm]] — architecture that reduces active compute per token but introduces expert routing communication and preserves dense KV cache pressure
- [[int8_fp8_quantization_llm_inference]] — numerical format reduction that halves per-element bandwidth demand and doubles Tensor Core throughput on H100
- [[nvidia_hopper_h100]] — dominant training and serving platform; FP8 Tensor Cores, 3.35 TB/s HBM3e, and 900 GB/s NVLink define the reference hardware envelope
- [[groq_lpu]] — SRAM-only architecture that eliminates HBM bandwidth as a bottleneck; 80 TB/s internal bandwidth enables deterministic sub-millisecond latency
- [[sambanova_sn40l]] — three-tier memory hierarchy (SRAM + HBM + DDR5) targeting trillion-parameter MoE capacity that GPU clusters cannot host in HBM
