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
source_url: https://milkv.io/docs/pioneer/getting-started/processor
fetched_at: '2026-07-03T14:18:06.914938+00:00'
type: hardware_target
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 0
outbound_links:
- target: c908-wino-gemm-optimization
  reason: Shares the XuanTie core architecture lineage with the C908, but the SG2042
    uses the newer C920 core with higher core count (64 vs. 8) and a different microarchitecture;
    both are RISC-V application processors from T-Head's XuanTie family
---

# SOPHON SG2042

The SOPHON SG2042 is a 64-core server-grade RISC-V processor designed for high-performance computing, operating at a base clock frequency of 2 GHz. It employs the XuanTie C920 core from T-Head (Alibaba), making it one of the highest-core-count RISC-V server chips available. The SG2042 is the processor powering the Milk-V Pioneer developer motherboard, which adopts a standard mATX form factor with PC-like interfaces (e.g., PCIe, SATA, USB) for native RISC-V development and desktop use. The processor's 64 cores provide strong multi-threaded computing capability, significantly surpassing earlier RISC-V boards in core count and enabling workloads such as server applications, compilation, and parallel scientific computing.

## Key Claims

- 64 RISC-V cores operating at 2 GHz base clock.
- Server-grade chip targeting high-performance computing workloads.
- Based on the XuanTie C920 core microarchitecture from T-Head.
- Used in the Milk-V Pioneer developer motherboard (mATX form factor, PC-like interfaces).
- Provides stronger multi-threaded capability compared to previous RISC-V boards.

## Optimization-Relevant Details

- ISA/profile: RISC-V (presumably RV64GC with vector extensions based on C920 support).
- Vector/matrix/accelerator support: Not specified; XuanTie C920 typically includes RVV 1.0.
- Memory/cache/TLB/DMA: Not specified in available sources.
- Compiler/toolchain support: Not specified; expected support from GCC/LLVM for RISC-V.

## Relationships

- [[c908-wino-gemm-optimization]]: Shares the XuanTie core architecture lineage with the C908, but the SG2042 uses the newer C920 core with higher core count (64 vs. 8) and a different microarchitecture; both are RISC-V application processors from T-Head's XuanTie family.

## Sources

- https://milkv.io/docs/pioneer/getting-started/processor (Milk-V Pioneer documentation)
