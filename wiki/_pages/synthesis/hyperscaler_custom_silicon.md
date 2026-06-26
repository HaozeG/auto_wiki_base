---
type: synthesis
connected_entities: [google_tpu, google_trillium_tpu_v6e, aws_inferentia, aws_trainium, microsoft_azure_maia_100, microsoft_cobalt_100, apple_neural_engine]
synthesis_status: draft
created: 2026-06-26
updated: 2026-06-26
cold_start: true
inbound_links: 0
scorecard:
  bridge_score: ~
  contradiction_potential: ~
  cross_domain_connection: ~
---

# Hyperscaler Custom Silicon: Why Google, AWS, Microsoft, and Apple Build Their Own AI Chips

## RAG Summary

All four major hyperscalers — Google, AWS, Microsoft, and Apple — have independently converged on custom AI silicon for the same root reason: merchant GPUs cannot be optimized for each company's specific workload shapes, cost structures, and memory bandwidth requirements. Yet they have taken divergent architectural paths that reveal different make-vs-buy thresholds. Google's TPU lineage (now on sixth-generation Trillium at 918 TFLOPS BF16 per chip) reflects the longest vertical integration program, beginning with TPU v1 in 2015 and driving bfloat16 adoption industry-wide. AWS splits the problem across two chip families — Inferentia2 for inference (190 TFLOPS FP16, targeting 70% cost reduction versus GPU instances) and Trainium2 for training (1.3 PFLOPS dense FP8, 96 GiB HBM per chip) — sharing the NeuronCore microarchitecture and Neuron SDK across both. Microsoft Azure Maia 100 takes the largest monolithic die approach at 820 mm² on TSMC N5 with a custom vector ISA, paired with the Cobalt 100 Arm CPU as the host processor. Apple Neural Engine is the sole edge-device entrant, embedded in every A-series and M-series SoC since 2017, delivering 38 TOPS at roughly 3.8 TOPS/W on M4 — prioritizing energy efficiency and tight OS integration over raw datacenter throughput. The divergence in scope, programmability, and deployment context across these four programs constitutes the central tension in the custom silicon landscape.

---

## Full Synthesis

### The Common Forcing Function

The primary driver for all four programs is economic: GPUs are priced and architectured for the broad market, carrying features (general shader programmability, peer-to-peer NVLink protocols, graphics fixed-function units) that hyperscalers do not need, while lacking optimizations that hyperscalers do — such as deterministic tail latency (Google's explicit requirement for v1), tight integration with proprietary network fabrics, or power envelopes tuned to specific rack densities.

Google articulated this earliest. The 2017 ISCA paper for TPU v1 reported 15–30× higher performance and 30–80× higher performance-per-watt versus Haswell CPUs and Nvidia K80 GPUs on production inference workloads. TPU v1 achieved this by stripping the chip to a 256×256 systolic array of INT8 MACs — 65,536 multiply-accumulate operations per cycle — with no caches, no branch predictors, and no speculative execution on the matrix path, explicitly to satisfy 99th-percentile latency requirements that GPU average-throughput optimizations would violate.

AWS reached the same conclusion for a different reason: as the dominant cloud provider, it runs both training and inference at volumes where even modest per-operation cost reductions compound to hundreds of millions of dollars annually. The Alexa text-to-speech migration to Inf1 instances demonstrated a 25% reduction in end-to-end latency and 30% lower cost versus GPU deployment — figures that justify the NeuronCore development program even without any training silicon in the picture.

Microsoft's Maia 100 reflects a later entry with a more aggressive die-size bet: 105 billion transistors on 820 mm² at TSMC N5, the largest reticle-limited monolithic die at that process node, with 64 GB HBM2E at 1.8 TB/s. The primary motivation was cost reduction for GPT-3.5-Turbo-class inference across Azure OpenAI Service and Copilot — workloads where Microsoft can predict request distributions and optimize a fixed ISA accordingly. The custom Sidekick liquid-cooling rack is a downstream consequence: Maia 100's 500 W production TDP (700 W ceiling) required mechanical co-design with the rack because no standard existed.

### Architectural Divergence

Despite the shared forcing function, the four programs reveal structurally different bets:

**Google: Vertical integration across the full stack.** Trillium (TPU v6e) delivers 918 TFLOPS BF16 per chip, 32 GB HBM, and 3,200 Gbps ICI bandwidth, with 67% better energy efficiency than v5e. The 3D torus pod topology (up to 8,960 chips in v5p configurations) makes Google's interconnect investment as large as its compute investment. Google also invented bfloat16 as a TPU training requirement; the format's subsequent adoption across the industry (NVIDIA, Intel, Arm) means Google's internal chip decision shaped the global AI compute toolchain.

**AWS: Split specialization with a shared software layer.** The Inferentia/Trainium split is a deliberate bet that inference and training have irreconcilable silicon trade-offs. Trainium2's 96 GiB HBM per chip and 2D torus NeuronLink at 1 TB/s chip-to-chip bandwidth optimize for gradient communication in distributed training. Inferentia2's four-engine NeuronCore-v2 (Tensor, Vector, Scalar, GP-SIMD) optimizes for heterogeneous operator coverage in low-latency inference. The Neuron SDK bridges both, but the hardware is not shared. The Trn2 UltraServer — 64 Trainium2 chips, 6 TB of HBM, 185 TB/s aggregate memory bandwidth — is AWS's competitive answer to NVIDIA DGX SuperPOD for LLM training at scale.

**Microsoft: Co-design at the system level.** Maia 100 is unusual in that its design forced infrastructure changes upstream (custom racks, Sidekick cooling) and downstream (Cobalt 100 as host CPU). This system-level co-design is most explicit in the Cobalt/Maia pairing: Cobalt 100's 128 Arm Neoverse N2 cores and 12-channel DDR5 are sized specifically to feed Maia 100's memory hierarchy without becoming the bottleneck. This mirrors Google's Titanium offload approach but is architecturally more tightly coupled.

**Apple: Edge-first, closed ecosystem.** The ANE's design point is fundamentally different from the other three. At 38 TOPS on M4 (approximately 19 TFLOPS FP16), it is orders of magnitude below datacenter silicon in absolute throughput, but it operates at roughly 3.8 TOPS/Watt — competitive with datacenter chips on efficiency per watt. The ANE is not programmable via a public ISA; all workloads reach it through Core ML, which compiles to an internal MIL representation. The Orion reverse-engineering project (arXiv 2603.06728) demonstrated direct ANE programming for LLM training and inference on M4, suggesting that the closed ecosystem is a product decision rather than a hardware constraint.

### The Make-vs-Buy Threshold

The clearest signal about each company's make-vs-buy threshold comes from what they chose *not* to build. Google has never publicly pursued a custom CPU for TPU host processing. AWS builds training and inference silicon but continues to sell GPU instances as the primary compute platform for customers who are not AWS workloads. Microsoft built Cobalt 100 only after Maia 100 validated that system-level co-design would pay off. Apple builds ANE and AMX but has never attempted a discrete datacenter accelerator.

The threshold appears to be: custom silicon is justified when (a) workload volume is large enough to amortize NRE costs, (b) the workload shape is predictable enough to allow architectural specialization, and (c) the software stack required to program the chip can be built or adapted from existing compiler infrastructure. Apple meets all three for on-device inference. Google meets all three for its own AI products and cloud offerings. AWS meets all three for the subset of customer workloads that match Neuron-supported model architectures. Microsoft meets them for the specific transformer inference workloads running at scale on Azure.

## Open Questions

1. **Programmability ceiling**: Maia 100's custom vector ISA enables compute density but raises questions about operator coverage — what fraction of modern transformer variants (mixture-of-experts routing, speculative decoding, RoPE attention) are expressible in BF16/INT8 ISA without software workarounds? No public benchmarks from Microsoft compare Maia 100 to H100 on tasks beyond GPT-3.5-Turbo.

2. **Training vs. inference silicon split**: AWS's two-family strategy (Trainium + Inferentia) assumes the training/inference boundary remains stable. If inference-time compute (chain-of-thought, multi-step reasoning with verifiers) grows to consume as much compute as training, the architectural assumptions baked into Inferentia2's heterogeneous NeuronCore-v2 may need to be revisited. Google's TPU handles both training and inference on the same chip family, which may prove more flexible.

3. **Apple's datacenter trajectory**: Apple Silicon M-series chips now appear in Mac Studio and Mac Pro configurations used for on-premises LLM inference. The ANE's 38 TOPS is below datacenter accelerators, but the unified memory architecture (up to 192 GB in M3 Ultra) and ~3.8 TOPS/Watt efficiency ratio could make Apple Silicon competitive for specific low-batch inference workloads. Whether Apple will extend this into server-form-factor products targeting enterprise inference is unresolved.

4. **Interconnect as first-class differentiator**: Google's 3D torus ICI and AWS's NeuronLink/EFAv3 both indicate that chip-to-chip and pod-scale interconnect is now as architecturally important as per-chip compute. Maia 100's interconnect specification is not publicly disclosed at the same level of detail. Whether Microsoft has equivalent all-reduce bandwidth for multi-chip inference is unclear from available sources.

## Connected Pages

- [[google_tpu]]
- [[google_trillium_tpu_v6e]]
- [[aws_inferentia]]
- [[aws_trainium]]
- [[microsoft_azure_maia_100]]
- [[microsoft_cobalt_100]]
- [[apple_neural_engine]]
