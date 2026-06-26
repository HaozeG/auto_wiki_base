---
type: entity
tags: [gpu-architecture, ai-accelerator, amd, isa, matrix-extension]
sources:
  - https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/white-papers/amd-cdna-3-white-paper.pdf
  - https://gpuopen.com/learn/amd-lab-notes/amd-lab-notes-matrix-cores-readme/
  - https://www.amd.com/en/technologies/cdna
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

# AMD CDNA Architecture

AMD CDNA (Compute DNA) is a family of GPU microarchitectures from AMD designed exclusively for high-performance computing and AI workloads, distinct from the RDNA line used in consumer graphics cards. CDNA was introduced in 2020 with the Instinct MI100 accelerator and has progressed through three generations: CDNA1 (MI100, 2020), CDNA2 (MI200 series including MI250X, 2021), and CDNA3 (MI300 series including MI300X, 2023). The defining feature of CDNA is the Matrix Fused Multiply-Accumulate (MFMA) instruction set extension to AMD's GCN/CDNA instruction set architecture, which enables hardware-accelerated matrix operations directly within each Compute Unit (CU). Each generation has roughly doubled matrix throughput per chip while expanding supported numeric formats. CDNA3 introduced a chiplet-based 3D-stacked package design (using what AMD calls XCDs, Accelerated Compute Dies) and extended MFMA support to include FP8 formats critical for large language model training. The architecture is supported by the ROCm open-source software stack, which provides a CUDA-like programming environment through the HIP language and associated math libraries.

## Key Claims

- CDNA1 (MI100, 2020) introduced the first-generation MFMA instructions on AMD hardware, delivering 184.6 TFLOPS FP16 peak on a 7 nm TSMC process with 32 GB HBM2 at 1.2 TB/s bandwidth.
- CDNA2 (MI250X, 2021) doubled matrix compute to 383 TFLOPS FP16 and expanded memory to 128 GB HBM2e at 3.2 TB/s across two GPU dies connected by Infinity Fabric, establishing the multi-die GPU model AMD carried forward.
- CDNA3 (MI300X, 2023) added FP8 (E4M3 and E5M2) and BF16 MFMA variants, reaching 1307 TFLOPS FP16 and 2614 TOPS INT8 on 192 GB HBM3 at 5.3 TB/s, representing approximately 3.4× the FP16 throughput of CDNA2 in a single package.
- MFMA instructions operate on matrix tiles: CDNA3 supports D = A × B + C for tile sizes up to 32×32 in FP16/BF16, 16×16 in FP64, and 32×32 in FP8, with the accumulator (D, C) held in VGPR (vector general-purpose registers) across the wavefront.
- AMD Infinity Fabric links between chiplets in the MI300X operate at up to 896 GB/s aggregate bidirectional bandwidth across the four XCDs within the package, enabling cache-coherent NUMA access to all 192 GB of HBM3 from any CU.
- ROCm (Radeon Open Compute), now at version 6.x, provides HIP (Heterogeneous-computing Interface for Portability), MIOpen (DNN library), hipBLAS, RCCL (collective communications), and direct integration with PyTorch and JAX through backends that translate CUDA idioms at compile time.
- The CDNA3 XCD chiplet contains 40 Compute Units; each CU contains 4 SIMD32 units and 4 MFMA units, where the MFMA unit is a dedicated systolic-style matrix accelerator separate from the SIMD floating-point pipeline.

## Relationships

- [[amd_mi300x]]: The MI300X is the flagship CDNA3 product; it packages four XCD chiplets and twelve HBM3 stacks in a single OAM module.
- [[nvidia_tensor_cores]]: NVIDIA Tensor Cores serve the same functional role as AMD MFMA units — dedicated hardware matrix accumulators within each streaming multiprocessor / compute unit; both support FP16, BF16, TF32, FP8 in recent generations.
- [[nvidia_hopper_h100]]: H100 is the primary competitive accelerator built on Hopper architecture; CDNA3/MI300X targets the same HPC/AI data-center segment.
- [[intel_amx]]: Intel AMX is a CPU-side ISA matrix extension (tiles in AMX vs MFMA in CDNA); the MI300A APU combines CDNA3 GPU dies with AMD EPYC CPU dies in a heterogeneous package, paralleling the CPU+accelerator integration model.
- [[google_tpu]]: Google TPU uses a dedicated systolic array ASIC design rather than a programmable GPU with matrix ISA extensions; both compete for the same LLM training/inference infrastructure market.
- [[arm_sme]]: ARM SME (Scalable Matrix Extension) is an ISA-level matrix extension analogous to MFMA but for ARM application processors; CDNA targets discrete accelerator deployment while SME targets edge and mobile.

## Sources

- AMD CDNA3 white paper (2023): https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/white-papers/amd-cdna-3-white-paper.pdf
- AMD Lab Notes — Matrix Cores: https://gpuopen.com/learn/amd-lab-notes/amd-lab-notes-matrix-cores-readme/
- AMD CDNA technology overview: https://www.amd.com/en/technologies/cdna
- AMD Instinct MI100 product brief (2020): https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/product-briefs/amd-instinct-mi100-product-brief.pdf
- Hot Chips 34 — AMD CDNA2 Architecture (2022): https://hotchips.org/hc34/
