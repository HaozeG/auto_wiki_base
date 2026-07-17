---
connected_entities:
- nvidia_blackwell_ultra
- nvidia_hopper_architecture
synthesis_status: draft
scorecard:
  bridge_score: 0.5
  contradiction_potential: 1.0
  cross_domain_connection: null
sources:
- raw/cache/70d47a6d919b3e37.md
- https://blog.prompt20.com/posts/nvidia-datacenter-gpus/
source_url: https://blog.prompt20.com/posts/nvidia-datacenter-gpus/
fetched_at: '2026-07-17T11:48:49.233882+00:00'
type: synthesis
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 0
outbound_links:
- target: nvidia_blackwell_ultra
  reason: unlabeled
- target: nvidia_hopper_architecture
  reason: unlabeled
---

# NVIDIA Datacenter GPU Generations

## RAG Summary

The NVIDIA datacenter GPU lineup has evolved from the Hopper architecture (H100, H200) in 2022 to the Blackwell architecture (B100, B200, GB200) in 2024, with the Rubin family announced for 2026-2027. The Hopper architecture, featuring the H100 with 80 GB HBM3 and 3.0 TB/s bandwidth, established the standard for AI training and inference. The H200 doubled inference throughput with 141 GB HBM3e at 4.8 TB/s. The NVIDIA Blackwell architecture, including the B200 with 8 TB/s HBM and FP4 tensor cores, offered up to 5× throughput over Hopper FP8. The GB200 NVL72 extended this to rack-scale with 72 GPUs in a unified NVLink fabric. The Rubin architecture (R100, GR200) promises 2× per-watt improvement over Blackwell. A key design consideration is the arithmetic intensity wall: modern GPUs perform far more flops per second than their memory bandwidth can feed, making workload-to-SKU matching critical. This synthesis connects the NVIDIA Blackwell Ultra GPU page—which details the latest Blackwell variant—and the NVIDIA Hopper Architecture page—which describes the workhorse Hopper generation—by tracing the evolution of HBM capacity, tensor core precision, and interconnects across generations. The comparison informs SKU selection for training versus inference workloads.

---

## Full Synthesis

NVIDIA's datacenter GPU cadence follows a two-year architectural refresh cycle: Ampere (2020), Hopper (2022), Blackwell (2024), and Rubin (2026). Each generation doubles peak compute and increases HBM capacity and bandwidth. Hopper introduced FP8 tensor cores and the Transformer Engine, making it the first architecture designed for transformer models. Blackwell extended this with FP4 precision and the GB200 rack-scale system. The arithmetic intensity wall—the gap between compute throughput and memory bandwidth—drives architectural innovation. Hopper's H100 achieves ~660 flops per byte (FP16), while Blackwell's B200 raises both compute and memory bandwidth, shifting the balance. For inference workloads, which are memory-bound, the H200's increased HBM bandwidth provides 1.6-1.9x decode throughput over the H100. For training, Blackwell's FP4 throughput offers up to 5x over Hopper's FP8. The Rubin architecture is expected to continue this trend with ~2x perf-per-watt over Blackwell.

## Open Questions

- How will the Rubin architecture's performance improvements scale with existing software ecosystems?
- What is the practical impact of FP4 precision on model accuracy across different workloads?
- How does the GB200 NVL72 rack-scale design affect total cost of ownership compared to traditional 8-GPU nodes?

## Connected Pages

- [[nvidia_blackwell_ultra]]
- [[nvidia_hopper_architecture]]

## Sources

- [NVIDIA Datacenter GPUs for AI: The Complete Guide — Prompt20 Blog](raw/cache/70d47a6d919b3e37.md)
