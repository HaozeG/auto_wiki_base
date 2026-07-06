---
canonical_name: SOPHON SG2042
aliases:
- SG2042
- Sophon SG2042
- Sophon SG2042 SoC
- Sophgo SG2042
- V-Seek LLM Inference Benchmark on Sophon SG2042
- V-Seek benchmark
- SG2042 LLM benchmark
- DeepSeek on SG2042
- Sophon SG2042 CPU
- Sophon SG2042 (Pioneer Box)
subtype: null
tags: []
hardware_targets:
- XuanTie C920
- SOPHON SG2042
toolchains: []
constraints:
- 2 GHz
- 64 cores
scorecard:
  novelty_delta: 0.7
  claim_density: 0.4
  self_containedness: 0.6
  bridge_score: 0.5
  hub_potential: 0.3
sources:
- raw/cache/84d6450ea6e13cca.md
- https://milkv.io/docs/pioneer/getting-started/processor
- raw/cache/17712147076f7c6c.md
- https://ar5iv.labs.arxiv.org/html/2309.00381
- raw/cache/5756ea94463b1961.md
- https://arxiv.org/abs/2503.17422
- raw/cache/b8ccce9b3180873d.md
- https://arxiv.org/html/2406.12394v1
- raw/cache/5b1c2c5ef89a99ef.md
- https://arxiv.org/abs/2406.12394
- raw/cache/76977c56a6102e86.md
- https://github.com/sophgo/sophgo-doc/blob/main/SG2042/TRM/source/system.rst
- raw/cache/04daa5f8f10c7be0.md
- https://browser.geekbench.com/v5/cpu/21586331
- raw/cache/f4ce8d173e27b53c.md
- https://www.researchgate.net/publication/381517668_Performance_characterisation_of_the_64-core_SG2042_RISC-V_CPU_for_HPC
source_url: https://milkv.io/docs/pioneer/getting-started/processor
fetched_at: '2026-07-03T14:18:06.914938+00:00'
type: hardware_target
created: '2026-07-03'
updated: '2026-07-06'
cold_start: true
inbound_links: 0
outbound_links:
- target: c908-wino-gemm-optimization
  reason: Shares the XuanTie core architecture lineage with the C908, but the SG2042
    uses the newer C920 core with higher core count (64 vs. 8) and a different microarchitecture;
    both are RISC-V application processors from T-Head's XuanTie family
---

# SOPHON SG2042

The SOPHON SG2042 is the world's first publicly available, mass-produced 64-core RISC-V CPU targeting high-performance workloads. It is also the first commercially available many-core RISC-V CPU with vector processing capabilities, targeting flexible and cost-effective inference and reasoning workloads for large language models. Developed by Sophgo (later Sophon), the chip was released in summer 2023 and operates at a base clock frequency of 2 GHz. It employs the XuanTie C920 core from T-Head (Alibaba), a high-performance out-of-order design. The 64 cores are organized in clusters of four, sharing an L2 cache (the memory subsystem is identified as the primary performance bottleneck). The SG2042 powers the Milk-V Pioneer developer motherboard, which adopts a standard mATX form factor with PC-like interfaces (e.g., PCIe, SATA, USB) for native RISC-V development and desktop use. The Milk-V Pioneer board is equipped with 128GB of DRAM and features a Non-Uniform Memory Access (NUMA) hierarchy. The processor's 64 cores provide strong multi-threaded computing capability, significantly surpassing earlier RISC-V boards in core count and enabling workloads such as server applications, compilation, and parallel scientific computing. Independent benchmarking using the RAJAPerf suite has shown that the SG2042 delivers, per core, between five and ten times the performance compared to the nearest widely available RISC-V hardware, while high-performance x86 CPUs commonly used in supercomputers outperform it by four to eight times for multi-threaded workloads, though some individual kernels run faster on the SG2042. Additional characterization using the NAS Parallel Benchmark (NPB) suite shows that the SG2042 outperforms other RISC-V CPUs by a factor of 2.6 to 16.7 at the single-core level, but its memory bandwidth and latency limit performance on memory-bound algorithms relative to x86-64 and AArch64 CPUs.

## Key Claims

- 64 RISC-V cores operating at 2 GHz base clock.
- Server-grade chip targeting high-performance computing workloads.
- Based on the XuanTie C920 core microarchitecture from T-Head (high-performance out-of-order cores).
- Used in the Milk-V Pioneer developer motherboard (mATX form factor, PC-like interfaces, 128GB DRAM, NUMA memory hierarchy).
- The SG2042 is the first commodity 64-core RISC-V CPU for high-performance workloads.
- The SG2042 is the first commercially available many-core RISC-V CPU with vector processing capabilities.
- Per-core performance is 5–10× that of the nearest widely available RISC-V hardware (RAJAPerf benchmarks).
- Modern x86 HPC CPUs outperform the SG2042 by 4–8× in multi-threaded workloads on average.
- Some individual kernels in the RAJAPerf suite execute faster on the SG2042 than on the x86 CPUs tested.
- Cores are organized in clusters of four, sharing an L2 cache; memory subsystem is the primary performance bottleneck.
- Outperforms other RISC-V CPUs by 2.6–16.7× at single-core level (NPB benchmarks).
- Competes well with x86-64 and AArch64 CPUs on compute-bound workloads but lags on memory-bound workloads.
- The paper is described as the first independent benchmarking study of a high-performance 64-core RISC-V CPU.
- The vector processing units require the Xuantie fork of GCC 10.4 for compiling optimized kernels; the overall inference framework (e.g., llama.cpp) can use GCC 13.2 or Clang 19.
- The platform serves as a testbed for the V-Seek LLM inference optimization framework.

## Optimization-Relevant Details

- **ISA/profile:** RISC-V with vector extensions (RVV 1.0, based on C920 support).
- **Vector/matrix/accelerator support:** RVV 1.0 (VLEN and DLEN not specified in available sources).
- **Memory/cache/TLB/DMA:** 128GB DRAM, NUMA architecture; cores organized in clusters of four sharing an L2 cache (specific cache sizes not published); memory subsystem identified as primary performance bottleneck.
- **Compiler/toolchain support:** Xuantie GCC 10.4 (required for vector kernel compilation), GCC 13.2, Clang 19; NPB benchmarks likely used standard GCC/LLVM with RISC-V backend.
- **Constraints:** 64 cores, XuanTie C920 core microarchitecture.

## Relationships

- [[c908-wino-gemm-optimization]]: Both the SG2042 and the C908 are T-Head XuanTie core products. The SG2042 uses the higher-end C920 core with 64 cores and a different microarchitecture, while the C908 is a more efficiency-focused design (8 cores) with RVV 1.0 and different optimization techniques. They share the XuanTie core family but target different segments (HPC vs. AI acceleration).

## Sources

- https://milkv.io/docs/pioneer/getting-started/processor (Milk-V Pioneer documentation)
- https://ar5iv.labs.arxiv.org/html/2309.00381
- Brown, N., Jamieson, M., Lee, J., & Wang, P. (2023). Is RISC-V ready for HPC prime-time: Evaluating the 64-core Sophon SG2042 RISC-V CPU. arXiv:2309.00381.
- https://arxiv.org/abs/2503.17422
- https://arxiv.org/abs/2406.12394
