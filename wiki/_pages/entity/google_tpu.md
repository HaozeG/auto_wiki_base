---
type: entity
tags: [ai-accelerator, systolic-array, google, tpu, inference, training, datacenter]
sources:
  - https://arxiv.org/pdf/1704.04760
  - https://dl.acm.org/doi/10.1145/3079856.3080246
  - https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm
  - https://docs.cloud.google.com/tpu/docs/v5p
  - https://docs.cloud.google.com/tpu/docs/v4
  - https://cloud.google.com/blog/products/ai-machine-learning/introducing-cloud-tpu-v5p-and-ai-hypercomputer
  - https://cloud.google.com/blog/products/ai-machine-learning/bfloat16-the-secret-to-high-performance-on-cloud-tpus
  - https://introl.com/blog/google-tpu-architecture-complete-guide-7-generations
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

# Google TPU (Tensor Processing Unit)

The Google Tensor Processing Unit (TPU) is a family of domain-specific ASICs designed by Google to accelerate neural network workloads inside Google's datacenters. First deployed in 2015 and publicly disclosed in a 2017 ISCA paper ("In-Datacenter Performance Analysis of a Tensor Processing Unit"), the TPU line spans at least six publicly documented generations (v1 through v6e/Trillium) and forms the compute backbone for Google's AI products and cloud offerings. TPU v1 was designed exclusively for inference and used a 256×256 systolic array of 8-bit multiply-accumulate units delivering 92 TOPS peak, while consuming roughly 40 W and fitting within the power envelope of an existing datacenter server slot. Beginning with TPU v2 (2017), the architecture shifted to support training by adopting bfloat16 (BF16) floating-point — a 16-bit format with the same 8-bit exponent as FP32 but only 7 mantissa bits, invented by Google Brain specifically for this transition. From v2 onward, each generation couples a Matrix Multiply Unit (MXU) built as a 128×128 systolic array (later 256×256 in v6e) with High Bandwidth Memory (HBM), a dedicated inter-chip interconnect (ICI), and a 3D torus network topology for large-scale pod deployments. The overarching design philosophy diverges from GPU architectures by optimizing for deterministic latency, high utilization on dense matrix operations, and tight coupling of compute and on-chip memory bandwidth rather than general-purpose programmability.

## Key Claims

- TPU v1 (2015/2017) achieved 15–30× higher performance and 30–80× higher performance-per-watt than contemporary Haswell CPUs and Nvidia K80 GPUs on production inference workloads, as reported in the 2017 ISCA paper.
- TPU v1 contained a 256×256 systolic array of 8-bit multiply-accumulate units (65,536 MACs) yielding 92 TOPS peak; it operated exclusively on inference and could not train models.
- Bfloat16 (BF16) was invented by Google Brain for TPU v2 training: it retains FP32's 8-bit exponent for wide dynamic range while truncating the mantissa to 7 bits, halving memory use versus FP32. TPU v2 delivered approximately 45 TFLOPS BF16 per chip (180 TFLOPS for a 4-chip v2 platform).
- TPU v3 doubled the systolic arrays to two 128×128 MXUs per core, reaching approximately 420 TFLOPS BF16 — a 2.3× improvement over v2.
- TPU v4 introduced a 3D torus ICI topology with each chip connected to six neighbors; a full v4 Pod comprises 4,096 chips with reconfigurable high-speed links.
- TPU v5p (2023) packs 95 GB HBM2e per chip with 2,765 GB/s memory bandwidth, uses ICI at 4,800 Gbps/chip in a 3D torus pod of 8,960 chips, and delivers more than 2× the FLOPS and 3× the HBM capacity of v4; it trains large LLMs approximately 2.8× faster than v4.
- The MXU architecture from v2 through v5p used 128×128 multiply-accumulate arrays; multiplications accept BF16 inputs while all accumulations are performed in FP32, preventing accumulation error growth.
- The 3D torus topology reduces worst-case inter-chip hop count from approximately 2√N (2D torus) to 3∛N: for a 4,096-chip pod this drops maximum hops from ~128 to ~48, substantially reducing all-reduce latency.
- TPU v1's deterministic execution model (no speculative execution, no caches, no branch predictors on the matrix path) was designed to satisfy 99th-percentile response-time requirements for production inference services, where GPU-style average-throughput optimizations degrade tail latency.

## Relationships

- [[gemmini]] — Gemmini is an open-source academic systolic array accelerator that shares the same fundamental systolic dataflow principles pioneered by TPU v1; both use weight-stationary or output-stationary systolic arrays for matrix multiply.
- [[tenstorrent]] — Tenstorrent Tensix cores are a commercial alternative to TPUs for AI acceleration; both compete in the datacenter AI ASIC space but differ in architecture (Tensix uses multi-core RISC-V tiles vs. TPU's monolithic MXU).
- [[tensix_architecture]] — The Tensix systolic-array-based design can be contrasted with TPU's MXU in terms of programmability trade-offs.
- [[arm_sme]] — ARM Scalable Matrix Extension provides matrix-acceleration ISA extensions for CPUs; TPU MXU achieves higher throughput by dedicating the entire chip die to matrix multiply rather than extending a general-purpose ISA.
- [[risc_v_matrix_extensions]] — RISC-V matrix extensions (IME/VME/AME) aim to bring TPU-like matrix acceleration to RISC-V CPUs as ISA extensions rather than discrete ASICs.

## Sources

- Jouppi et al., "In-Datacenter Performance Analysis of a Tensor Processing Unit," ISCA 2017. https://arxiv.org/pdf/1704.04760 — primary source for v1 design goals, 92 TOPS figure, 15–30× GPU comparison, deterministic latency rationale.
- Google Cloud TPU system architecture documentation. https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm — MXU sizing (128×128 for v2-v5p, 256×256 for v6e+), BF16/FP32 accumulation behavior.
- Google Cloud TPU v5p documentation. https://docs.cloud.google.com/tpu/docs/v5p — 95 GB HBM2e, 2,765 GB/s bandwidth, 4,800 Gbps/chip ICI, 8,960-chip pod, 2.8× v4 training speed.
- Google Cloud TPU v4 documentation. https://docs.cloud.google.com/tpu/docs/v4 — 4,096-chip pod, six ICI links per chip, 3D torus topology.
- Google Cloud Blog, "BFloat16: The secret to high performance on Cloud TPUs." https://cloud.google.com/blog/products/ai-machine-learning/bfloat16-the-secret-to-high-performance-on-cloud-tpus — BF16 invention by Google Brain, exponent/mantissa tradeoff.
- Introl Blog, "Google TPU Architecture: 7 Generations Explained." https://introl.com/blog/google-tpu-architecture-complete-guide-7-generations — cross-generation performance figures.
