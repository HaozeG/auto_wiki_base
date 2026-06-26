---
type: synthesis
connected_entities: [groq_lpu, sambanova_sn40l, cerebras_wse, tenstorrent_blackhole, aws_inferentia, nvidia_hopper_h100]
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

# Inference Accelerator Startups: Architectural Differentiation Against GPU Dominance

## RAG Summary

Groq, SambaNova, Cerebras, and Tenstorrent each pursue a distinct architectural bet against NVIDIA's general-purpose GPU, collectively revealing that LLM inference performance is bottlenecked by memory bandwidth and scheduling latency rather than raw FLOPS. Groq's Language Processing Unit eliminates off-chip DRAM entirely, storing all model weights in 230 MB of on-chip SRAM accessed at 80 TB/s — roughly 10× higher than H100's 3.35 TB/s HBM3 bandwidth — and relies on a fully static compiler that pre-schedules every clock cycle, enabling Llama 3 8B to exceed 1,300 tokens/second versus roughly 100 tokens/second on H100. Cerebras WSE-3 scales the SRAM principle to wafer dimensions: a single 46,225 mm² die integrates 44 GB of on-chip SRAM at 21 PB/s bandwidth, running Llama 3.1 70B at 2,100 tokens/second per user, more than 21× faster than the Blackwell B200. SambaNova SN40L targets trillion-parameter sparse models through a three-tier memory hierarchy — 520 MB SRAM, 64 GB HBM3 at 2 TB/s, and up to 1.5 TB DDR5 per socket — achieving 3.7× throughput advantage over a DGX H100 on Composition of Experts workloads. Tenstorrent Blackhole takes a programmability-first approach: 120 Tensix cores built on 768 RISC-V processors with an open-source Metalium software stack, targeting edge and cloud deployments at a $1,399 PCIe card price point. AWS Inferentia2, while a hyperscaler internal chip rather than an open-market startup product, validates the cost thesis: Inf2 instances target 70% cost-per-inference reduction versus GPU instances on supported workloads.

---

## Full Synthesis

### The Core Diagnosis: FLOPS Are Not the Bottleneck

The NVIDIA H100 SXM5 delivers 3,026 TFLOPS of dense FP8 compute and 3.35 TB/s of HBM3 memory bandwidth. For LLM inference in the autoregressive decode phase, a transformer layer must load its full weight matrix from memory for each generated token, making the process memory-bandwidth-bound rather than compute-bound. A model with 70 billion parameters at BF16 precision requires ~140 GB of data movement per forward pass; the H100's 3.35 TB/s bandwidth can move this in roughly 42 ms, irrespective of the chip's peak compute headroom. Every startup analyzed here attacks this specific bottleneck through a different structural mechanism.

### Groq: Determinism via SRAM Exclusivity

Groq's GroqChip1 replaces HBM with 230 MB of on-chip SRAM at 80 TB/s — a 23× bandwidth advantage per chip over H100 — and compiles the entire inference graph, including inter-chip communication timing, to a fixed static schedule with no runtime arbitration. This eliminates both the memory-bandwidth bottleneck for model sizes that fit in SRAM and the scheduling jitter that makes GPU latency non-deterministic. The constraint is weight capacity: 230 MB fits a fraction of a large model, requiring multi-chip scale-out via 16 chip-to-chip links per device. The second-generation LPX system raises system-level SRAM bandwidth to 40 PB/s across a rack. The result is measurable: Llama 3 8B exceeds 1,300 tokens/second on GroqCloud, more than 13× faster than H100 equivalents.

### Cerebras: SRAM at Wafer Scale

Cerebras WSE-3 pursues the same SRAM-centric principle but scales it by fabricating on an entire 300 mm wafer: 46,225 mm² integrating 4 trillion transistors, 900,000 cores, and 44 GB of on-chip SRAM at 21 PB/s — approximately 6,000× more bandwidth than the H100. By eliminating die-to-die communication latency, WSE-3 can hold large model layers in SRAM without multi-chip coherency overhead. For models exceeding 44 GB, the MemoryX weight-streaming system loads weights layer by layer from external DRAM servers, hiding off-chip bandwidth behind the wafer's compute depth. In single-user latency benchmarks, CS-3 ran Llama 3.1 70B at 2,100 tokens/second — more than 21× faster than Blackwell B200 — and demonstrated trillion-parameter model training on a single node. The trade-off is system complexity: a single CS-3 system is a purpose-built appliance rather than a commodity card.

### SambaNova: Tiered Memory for Sparse Giants

SambaNova SN40L targets a different problem: trillion-parameter mixture-of-experts (MoE) models where total weight footprint vastly exceeds any practical SRAM budget. The three-tier hierarchy — 520 MB on-chip SRAM for active activations, 64 GB HBM3 at ~2 TB/s for currently-routing expert weights, and up to 1.5 TB DDR5 per socket for cold experts — allows a single 8-RDU SambaRack node to host 150 independent 7B expert models totaling ~1 trillion parameters (Composition of Experts, CoE). Only the routed expert weights migrate from DDR to HBM and then to SRAM during each inference step, making the effective working set bandwidth-friendly. Benchmarks show 3.7× CoE throughput over DGX H100 and 6.6× over DGX A100, plus 15–31× faster model switching — a critical latency metric for multi-tenant serving. Each SN40L socket integrates 102 billion transistors in a dual-die CoWoS package at 640 BF16 TFLOPS. Unlike Groq or Cerebras, the RDU also supports fine-tuning on the same hardware without reconfiguration.

### Tenstorrent: Open-Source Programmability and Cost Disruption

Tenstorrent Blackhole takes a contrasting bet: rather than maximizing bandwidth through exotic memory design, it bets on programmability and accessibility. The Blackhole p150a packs 120 Tensix cores with 768 RISC-V processors, 32 GB GDDR6, and ten 400GbE ports into a $1,399 PCIe card supported by the open-source Metalium software stack. RISC-V cores enable software-defined computation without vendor lock-in, positioning Tenstorrent against both NVIDIA's CUDA ecosystem and Groq/Cerebras's fixed-function inference pipelines. At $1,399, Blackhole targets edge AI deployments and cost-sensitive inference workloads where raw tokens-per-second matters less than total cost of ownership. The open ISA allows custom operator definition and inspection of hardware behavior, which is structurally impossible on Groq's static-compiled TSP or Inferentia's fixed NeuronCore instruction sets.

### AWS Inferentia: Hyperscaler Validation of the Cost Thesis

AWS Inferentia2 does not originate from an AI hardware startup but validates the economic argument underpinning the entire sector. Inf2 instances deliver up to 2.3 petaflops across 12 chips, 384 GB shared HBM, and 9.8 TB/s total bandwidth. Amazon Alexa's deployment on Inf1 achieved 25% lower latency and 30% lower cost versus GPU. The Neuron SDK compiler approach — compiling PyTorch/JAX models to fixed NeuronCore instruction streams — mirrors Groq's compiler-directed philosophy but without the SRAM exclusivity. At 190 TFLOPS FP16 per chip, Inferentia2 is compute-modest compared to H100's 1,513 TFLOPS FP16 dense, but at the per-inference cost level it targets throughput-bound batch workloads where utilization efficiency matters more than peak throughput.

### Convergent Architecture Themes

Four structural patterns cut across all five challengers:

1. **Memory hierarchy redesign over compute scaling:** Every chip described here invests its primary architectural novelty in memory organization (SRAM exclusivity, tiered hierarchy, wafer-scale on-chip) rather than in new compute instruction sets. The H100's 3,026 TFLOPS far exceeds what any of these chips deliver in raw compute, but raw FLOPS are irrelevant in the memory-bound decode phase.

2. **Compiler-directed vs. dynamic scheduling:** Groq and AWS Inferentia use static, ahead-of-time compilation; SambaNova's RDU dataflow and Cerebras's data-triggered 2D mesh represent intermediate positions. Tenstorrent's RISC-V cores support the most dynamic, runtime-flexible scheduling. This spectrum maps onto a latency-determinism vs. programmability trade-off.

3. **Fit-to-scale tension:** The SRAM-only designs (Groq, Cerebras) excel at latency for models that fit on-chip; trillion-parameter models require multi-chip scale-out (Groq) or weight streaming (Cerebras MemoryX). SambaNova's tiered hierarchy is the only design that natively accommodates models far exceeding on-chip SRAM without an external streaming layer.

4. **Open vs. closed software stack:** Tenstorrent Metalium and RISC-V ISA represent the open end; Groq's static compiler and Inferentia's Neuron SDK represent the closed end. This choice determines ecosystem portability for customers but does not directly affect inference speed.

## Open Questions

1. **Single-user latency vs. multi-user throughput:** Groq's 1,300+ tokens/second and Cerebras's 2,100 tokens/second are single-user metrics. Whether these advantages hold at 100+ concurrent users — where batching across users is possible and HBM bandwidth can be amortized — is not established in the available data. GPU efficiency at batch sizes of 32–128 may close the gap significantly.

2. **MoE model trajectory and memory tier value:** If the industry converges on sparse MoE architectures for frontier models (Mixtral, Llama 4 MoE-style), SambaNova's three-tier hierarchy gains structural advantage. If dense models remain dominant or per-expert specialization grows, Groq's SRAM-only model may remain competitive. The architectural bet of each vendor is tightly coupled to which model families become standard.

3. **Cost and yield viability at scale:** Cerebras WSE-3's wafer-scale die is the most structurally differentiated design but also the most expensive to manufacture; defect-tolerant routing across the wafer is required. Groq's multi-chip scale-out with 16 chip-to-chip links adds system-level complexity. Whether either approach can reach cost-per-token parity with commodity GPU clusters at volume remains unverified.

4. **Training co-location:** SambaNova RDU supports inference and fine-tuning on the same hardware; Groq LPU and AWS Inferentia are inference-only. As on-device continuous fine-tuning becomes standard for model personalization, inference-only designs face a structural limitation that may require separate training infrastructure, increasing total deployment cost.

5. **Tenstorrent benchmark gap:** The Blackhole entity page lacks published token/second benchmarks comparable to Groq, Cerebras, or SambaNova. Whether the RISC-V programmability advantage translates to competitive inference throughput on standard LLM workloads — or represents primarily a cost and ecosystem story — cannot be assessed from available data.

## Connected Pages

- [[groq_lpu]]
- [[sambanova_sn40l]]
- [[cerebras_wse]]
- [[tenstorrent_blackhole]]
- [[aws_inferentia]]
- [[nvidia_hopper_h100]]
