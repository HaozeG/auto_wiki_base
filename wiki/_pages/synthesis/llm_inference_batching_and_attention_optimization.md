---
cold_start: false
connected_entities: []
created: '2026-07-04'
inbound_links: 0
scorecard:
  bridge_score: 0.6
  contradiction_potential: 0.1
  cross_domain_connection: null
sources:
- https://insujang.github.io/2024-01-07/llm-inference-continuous-batching-and-pagedattention/
synthesis_status: draft
tags:
- llm
- inference
- batching
- attention
- vllm
- orca
type: synthesis
updated: '2026-07-04'
---

# LLM Inference Batching and Attention Optimization

## RAG Summary

The optimization of large language model (LLM) inference has become critical as models grow in size and deployment scales. Two key techniques address throughput and memory inefficiencies: continuous batching (iteration-level scheduling) and PagedAttention. Continuous batching, introduced in the Orca system (OSDI '22), overcomes the limitations of static batching by allowing new sequences to be added to a running batch at each decoding iteration, rather than waiting for the entire batch to complete. This significantly improves GPU utilization and throughput, especially under varying request lengths and arrival patterns. PagedAttention, introduced in the vLLM system, solves the memory fragmentation problem in the key-value (KV) cache used during autoregressive decoding. Traditional systems pre-allocate contiguous memory blocks for each request's KV cache, leading to internal and external fragmentation. PagedAttention manages the KV cache in fixed-size pages (blocks), analogous to virtual memory in operating systems, allowing non-contiguous memory storage and copy-on-write sharing across requests. This reduces memory waste by up to 80% and enables larger batch sizes and higher throughput. Together, these techniques form the backbone of modern high-performance LLM serving systems, enabling efficient handling of large-scale inference workloads.

---

## Full Synthesis

### Continuous Batching (Iteration-Level Scheduling)

Before the introduction of continuous batching, LLM serving systems used static batching: a batch of requests is formed and processed together through all decoding steps until every sequence in the batch reaches its end-of-sequence token. This approach suffers from low GPU utilization because requests have different lengths; shorter sequences finish early, leaving the GPU idle within the batch slot. Orca (OSDI '22) proposed continuous batching, also called iteration-level scheduling. The key idea is that at every decoding iteration, the scheduler can add new sequences to the batch and remove finished sequences. This keeps the GPU fully occupied and improves throughput by up to 2–3× compared to static batching. The technique also enables higher latency fairness and support for varying priorities.

### PagedAttention

The attention mechanism in transformer decoders requires storing key and value tensors (KV cache) for every prior token in the sequence. The KV cache size grows linearly with sequence length, and for long generations it dominates GPU memory. Conventional implementations pre-allocate a contiguous memory buffer for each request's KV cache. This leads to internal fragmentation (over-provisioning for maximum sequence length) and external fragmentation (inability to pack requests efficiently). PagedAttention, introduced in the vLLM system, treats the KV cache as a set of fixed-size blocks (pages) that can be stored non-contiguously in GPU memory. Each block stores the keys and values of a fixed number of tokens. The attention computation is then performed by fetching the required blocks via a mapping table, similar to virtual memory page tables. This eliminates wasted memory from pre-allocation and allows sharing of blocks across requests that share prefixes (e.g., system prompts). The result is up to 80% reduction in KV cache memory usage, enabling 2–4× higher throughput in practice.

### Combined Impact

Continuous batching and PagedAttention are orthogonal and complementary. Continuous batching increases the number of requests that can be processed concurrently by optimizing scheduling, while PagedAttention reduces the memory footprint per request, allowing larger effective batch sizes. Their combination has become the standard design for high-throughput LLM inference engines (e.g., vLLM, TensorRT-LLM, OpenPPL). Empirically, systems incorporating both techniques achieve 2–8× throughput improvements over naive implementations, with minimal degradation in latency.

## Open Questions

- How do these techniques scale to extremely long contexts (e.g., 128K+ tokens) where the KV cache dominates even with paging?
- Can PagedAttention be combined with sparse attention patterns to further reduce memory and compute?
- What are the optimal page sizes for different hardware architectures (NVIDIA vs. AMD vs. custom accelerators)?
- How do these techniques interact with speculative decoding or other advanced generation strategies?

## Connected Pages

No existing wiki pages currently cover LLM inference optimization topics. This page serves as a foundational entry point for future pages on Orca, vLLM, KV cache management, and related systems.
