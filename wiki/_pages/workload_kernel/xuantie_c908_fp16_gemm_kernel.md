---
canonical_name: XuanTie C908 FP16 GEMM Outer Product Kernel
aliases:
- C908 GEMM kernel
- VLEN128 fp16 gemm kernel
workloads:
- gemm
datatypes:
- fp16
constraints:
- RVV VLEN128
- XuanTie C908 instruction fusion
hardware_targets:
- XuanTie C908
scorecard:
  novelty_delta: 0.9
  claim_density: 0.85
  self_containedness: 0.9
  bridge_score: 0.3
  hub_potential: 0.8
sources:
- raw/cache/73bedd2221cd9a03.md
- https://riscv.org/blog/xuantie-c908-accelerates-ai-with-software-and-hardware-fusion/
source_url: https://riscv.org/blog/xuantie-c908-accelerates-ai-with-software-and-hardware-fusion/
fetched_at: '2026-07-01T02:54:06.948603+00:00'
type: workload_kernel
created: '2026-07-01'
updated: '2026-07-01'
cold_start: true
inbound_links: 7
needs_summary_revision: false
---

# XuanTie C908 FP16 GEMM Outer Product Kernel

This kernel implements the core GEMM computation used in SHL’s convolution acceleration for the XuanTie C908 processor. For fp16 arithmetic on a VLEN 128 RISC‑V vector unit, the kernel loads weight matrices using vector load (vle) and input activations using scalar floating‑point loads (flh), then performs an outer product accumulation across a 16×12 register block. The arrangement exploits the full vector register count to maximize throughput while manually scheduling instructions to remove read‑after‑write and write‑after‑write data hazards. Instruction fusion technology on XuanTie C908 further pipelines the sequence, reducing instruction overhead. This kernel is the computational heart of both the im2col+GEMM and Winograd convolution paths in SHL, enabling high‑performance CNN inference.

## Key Claims

- FP16 GEMM outer product using 16×12 register tile with vector‑weight and scalar‑input loads.
- Manual instruction scheduling removes data dependencies.
- Leverages XuanTie C908’s instruction fusion for improved throughput.
- Used in conjunction with SHL’s convolution operators for CNN acceleration.

## Kernel Shape

- Operation: GEMM (matrix multiply) via outer product accumulation.
- Shapes: Optimized tile of 16×12; exact input/output dimensions depend on convolution lowering.
- Datatypes: FP16.
- Layout: Weight stored in vector‑wide memory order for vle; input accessed via scalar flh.
- Sparsity: Not utilized.
- Baseline implementation: Naïve inner‑product GEMM or im2col without register blocking.

## Relationships

- Hardware target: [[xuantie_c908]]
- Optimization recipe: [[xuantie_c908_shl_convolution_acceleration]]
- Benchmark result: [[xuantie_c908_ai_inference_performance]]

## Sources

- https://riscv.org/blog/xuantie-c908-accelerates-ai-with-software-and-hardware-fusion/
