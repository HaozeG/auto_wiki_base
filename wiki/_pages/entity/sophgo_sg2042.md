---
cold_start: true
created: 2026-06-27
inbound_links: 1
needs_summary_revision: true
scorecard:
  bridge_score: null
  claim_density: null
  hub_potential: null
  novelty_delta: null
  self_containedness: null
sources:
- https://en.sophgo.com/product/introduce/sg2042.html
- https://arxiv.org/abs/2406.12394
- https://milkv.io/docs/pioneer/getting-started/processor
- https://semiengineering.com/supercomputing-sg2042-64-core-risc-v-cpu-versus-existing-risc-v-hw-and-high-performance-x86-cpus/
tags:
- risc-v
- server
- HPC
- SoC
- sophgo
- many-core
type: entity
updated: 2026-06-27
---

# Sophgo SG2042

Sophgo SG2042 is the first mass-produced, commodity-available, high-core-count RISC-V server CPU, integrating 64 XuanTie C920 cores on a single die manufactured at TSMC 6nm. Released in mid-2023, the SG2042 targets HPC and AI inference workloads and powers the Milk-V Pioneer desktop workstation, making it the primary vehicle for RISC-V server software ecosystem development. Each C920 core runs at 2 GHz, implements RV64GCV with RVV v0.7.1 at 128-bit vector width, and shares a 64 MB system-level L3 cache. The chip integrates four DDR4-3200 memory controllers and a PCIe Gen4 x32 interface, enabling direct GPU/accelerator attachment for heterogeneous AI workloads.

## Key Claims

- 64 XuanTie C920 RISC-V cores at 2 GHz with 64 MB shared L3 cache on a single SG2042 die.
- Four DDR4-3200 memory channels provide peak bandwidth of approximately 102 GB/s.
- PCIe Gen4 x32 interface allows GPU or accelerator attachment; the Milk-V Pioneer board supports up to 128 GB DDR4 RAM.
- Independent benchmarks show SG2042 delivers between 2.6× and 16.7× single-core performance uplift over all other tested RISC-V platforms.
- Memory subsystem is the primary bottleneck: memory-bandwidth-sensitive workloads (NAS Integer Sort, Multi-Grid) suffer significantly compared to compute-bound kernels on x86-64 or AArch64 peers.
- LLM inference benchmarks show ~4.32 tokens/s for Llama-3 8B using llama.cpp with RVV optimization on the full 64-core system.
- SG2042 is the chip inside the Milk-V Pioneer, the first workstation-class RISC-V system sold commercially.

## Relationships

- [[milkv_pioneer_duo]]: SG2042 is the processor powering the Milk-V Pioneer workstation board.
- [[alibaba_xuantie_c910_c920]]: C920 cores are the building blocks of SG2042; SG2042 instantiates 64 of them.
- [[llm_inference_riscv]]: SG2042 is the primary hardware platform for RISC-V LLM inference benchmarks.
- [[risc_v_vector_extension]]: C920 implements RVV v0.7.1 at 128-bit VLEN, enabling vectorized AI kernels.

## Sources

- https://en.sophgo.com/product/introduce/sg2042.html
- https://arxiv.org/abs/2406.12394
- https://milkv.io/docs/pioneer/getting-started/processor
- https://semiengineering.com/supercomputing-sg2042-64-core-risc-v-cpu-versus-existing-risc-v-hw-and-high-performance-x86-cpus/
