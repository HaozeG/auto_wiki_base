---
cold_start: false
created: 2026-06-27
inbound_links: 0
needs_summary_revision: false
scorecard:
  bridge_score: null
  claim_density: null
  hub_potential: null
  novelty_delta: null
  self_containedness: null
sources:
- https://arxiv.org/abs/2508.13840
- https://arxiv.org/html/2508.13840v1
- https://www.tomshardware.com/news/chinese-company-develops-64-core-riscv-cpu-as-us-sanctions-loom
- http://riscv.epcc.ed.ac.uk/assets/files/hpcasia24/hpc_asia_wang.pdf
tags:
- risc-v
- hpc
- server
- ai-inference
- t-head
- sophgo
type: entity
updated: 2026-06-27
---

# SOPHGO SG2044

The SOPHGO SG2044 is a 64-core RISC-V server-class CPU produced by the Chinese fabless semiconductor company SOPHGO, designed for workstation and HPC workloads and announced for Q1 2024 availability. The SG2044 is the direct successor to the SG2042 — the first widely available RISC-V server chip — and replaces the C920v1 core with the upgraded T-Head XuanTie C920v2, implementing RVV 1.0 (the ratified RISC-V Vector extension) rather than the pre-ratification vector draft used in SG2042. The most consequential architectural change is the memory subsystem: the SG2044 deploys 32 memory controllers and 32 DDR5 channels versus four in the SG2042, delivering more than three times the memory bandwidth at full 64-core utilization. All 64 cores reside within a single NUMA domain, eliminating the NUMA-crossing penalty that affected SG2042 workloads. The chip targets HPC users who need RISC-V for open-ISA research or AI inference workloads such as LLM decoding, and published benchmarks at SC'25 confirm up to 4.91x speedup over SG2042 on memory-latency-bound kernels, substantiating the memory subsystem redesign as the primary performance driver.

## Key Claims

- The SG2044 integrates 64 T-Head XuanTie C920v2 cores at 2.6 GHz (versus 2.0 GHz in SG2042) organized in 16 clusters of four cores, all within a single NUMA domain.
- Memory bandwidth exceeds 300 GB/s via 32 DDR5 memory controllers and 32 channels, more than three times the bandwidth of the SG2042's four-controller design.
- SC'25 benchmark evaluation (arXiv:2508.13840) reports up to 4.91x speedup over SG2042 on 64-core memory-latency-bound (IS) kernels and 2.25x speedup on memory-bandwidth-bound (MG) kernels; single-core gains are modest (1.08x–1.30x).
- The SG2044 implements RVV 1.0 (ratified RISC-V Vector specification), enabling 128-bit vector operations through standard GCC and LLVM toolchain support without vendor patches.
- AI inference capability includes the T-Head Matrix Extension, and the SG2044 has been demonstrated running LLaMA-7B at 40 tokens/second.
- PCIe connectivity is upgraded to Gen 5.0 x80 lanes, doubling per-lane bandwidth versus the SG2042's PCIe Gen 4.0.

## Relationships

- [[sophgo_sg2042]] — The SG2042 is the predecessor 64-core RISC-V server chip; SG2044 replaces C920v1 cores with C920v2 and triples memory bandwidth.
- [[alibaba_xuantie_c910_c920]] — The C920v2 core used in SG2044 is T-Head (Alibaba's chip division) intellectual property, an evolution of the XuanTie C920 family.
- [[risc_v_vector_extension]] — SG2044 is the first SOPHGO server chip to ship with ratified RVV 1.0, enabling mainline toolchain support.
- [[riscv_matrix_extension]] — The T-Head Matrix Extension available in C920v2 provides matrix-multiply acceleration for AI inference workloads.
- [[llm_inference_riscv]] — SG2044 demonstrated LLaMA-7B inference at 40 tokens/second, establishing a concrete LLM inference baseline for RISC-V servers.
- [[firesim_fpga_simulation]] — FireSim and similar research platforms validated SG2042 architecture; SG2044 targets production HPC deployments.

## Sources

- SC'25 paper evaluating SG2044 HPC readiness (arXiv:2508.13840): https://arxiv.org/abs/2508.13840
- Full evaluation paper HTML: https://arxiv.org/html/2508.13840v1
- Tom's Hardware on SG2044 and sanctions context: https://www.tomshardware.com/news/chinese-company-develops-64-core-riscv-cpu-as-us-sanctions-loom
- SOPHGO roadmap presentation at HPC-Asia 2024: http://riscv.epcc.ed.ac.uk/assets/files/hpcasia24/hpc_asia_wang.pdf
