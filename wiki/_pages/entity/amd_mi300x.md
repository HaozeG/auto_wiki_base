---
type: entity
tags: [ai-accelerator, gpu, hpc, amd, cdna]
sources:
  - https://www.amd.com/en/products/accelerators/instinct/mi300/mi300x.html
  - https://www.anandtech.com/show/21116/amd-instinct-mi300x-review
  - https://arxiv.org/abs/2312.06839
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

# AMD Instinct MI300X

The AMD Instinct MI300X is a data-center GPU accelerator released in late 2023, designed primarily for large-scale AI inference and training workloads. It is the first GPU from any vendor to integrate 192 GB of HBM3 memory on a single package, delivering 5.3 TB/s of aggregate memory bandwidth. The MI300X is built on a 3D chiplet architecture that stacks four GPU compute dies (XCDs, each containing CDNA3 Matrix Cores) alongside four I/O dies and twelve HBM3 stacks, all connected through AMD's Infinity Fabric interconnect. The chip is manufactured on TSMC's 5 nm node for compute dies and 6 nm for I/O dies. Its primary competitive target is the NVIDIA H100 SXM5, and its main advantage is a memory capacity approximately 2.4× larger (192 GB vs 80 GB), which allows full deployment of large language models such as LLaMA-70B and GPT-3 175B on a single device without model parallelism across cards. Peak compute throughput reaches 1307.4 TFLOPS at FP16 and 2614.9 TOPS at INT8, making the MI300X one of the highest-throughput AI accelerators commercially available at its launch.

## Key Claims

- The MI300X integrates 192 GB of HBM3 memory across 12 stacks, with a total memory bandwidth of 5.3 TB/s — approximately 1.35× the bandwidth of the H100 SXM5 (3.35 TB/s) and 2.4× the memory capacity (80 GB).
- Peak FP16 throughput is 1307.4 TFLOPS using the CDNA3 Matrix Core MFMA (Matrix Fused Multiply-Accumulate) instructions, compared to approximately 989 TFLOPS (without sparsity) on the H100 SXM5.
- The package contains 8 chiplets in a 3D stack: 4 XCDs (compute GPU dies) and 4 I/O dies, with XCDs manufactured on TSMC 5 nm and I/O dies on TSMC 6 nm, totaling approximately 153 billion transistors across all dies.
- Each XCD contains 40 Compute Units (CUs), giving the full chip 304 active CUs; each CU contains 4 MFMA units capable of executing matrix operations natively in FP64, FP32, FP16, BF16, and INT8 precisions.
- The MI300X is connected to the host CPU through PCIe 5.0 (x16) or, in the OAM form factor, through the Infinity Fabric at up to 896 GB/s bidirectional bandwidth when used in 8-GPU configurations with AMD EPYC CPUs in the MI300A APU variant.
- AMD ROCm 6.0 provides software-stack support including HIP (an equivalent to CUDA), hipBLAS, MIOpen (equivalent to cuDNN), and RCCL (equivalent to NCCL), enabling porting of PyTorch and JAX workloads without CUDA rewriting.
- In MLPerf Inference v3.1 benchmarks (2023), MI300X systems achieved competitive throughput to H100 systems on the Llama 2 70B text generation task, with a higher advantage on batch sizes constrained by memory capacity.

## Relationships

- [[nvidia_hopper_h100]]: Direct competitive comparison target; MI300X has 2.4× more memory but similar or slightly higher raw compute at FP16; H100 retains advantages in NVLink bandwidth at scale.
- [[nvidia_tensor_cores]]: AMD MFMA (Matrix Fused Multiply-Accumulate) instructions in CDNA3 are the functional equivalent of NVIDIA Tensor Cores; both implement outer-product matrix accumulation in hardware.
- [[amd_cdna_architecture]]: MI300X implements the CDNA3 generation of AMD's Compute DNA GPU architecture, which introduced the XCD chiplet design and expanded the MFMA instruction set.
- [[google_tpu]]: Google TPU v4/Trillium are comparable HPC AI accelerators in the same deployment tier; unlike MI300X they use systolic arrays rather than GPU-style SIMD with matrix extensions.
- [[intel_amx]]: Intel AMX is a competing x86 ISA matrix extension for CPUs rather than discrete accelerators; MI300A (the APU sibling) combines CDNA3 GPU cores with EPYC CPU cores in the same package.

## Sources

- AMD Instinct MI300X product page: https://www.amd.com/en/products/accelerators/instinct/mi300/mi300x.html
- AMD CDNA3 white paper (2023): https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/white-papers/amd-cdna-3-white-paper.pdf
- AnandTech MI300X deep dive review (2023): https://www.anandtech.com/show/21116/amd-instinct-mi300x-review
- MLPerf Inference v3.1 results (2023): https://mlcommons.org/benchmarks/inference-datacenter/
- AMD ROCm 6.0 documentation: https://rocm.docs.amd.com/
