---
canonical_name: Integrated Matrix Extension
aliases:
- IME
subtype: null
tags: []
scorecard:
  novelty_delta: 0.7
  claim_density: 0.5
  self_containedness: 0.9
  bridge_score: 0.3
  hub_potential: 0.2
sources:
- raw/cache/5ac8eb56f1f5ccd7.md
- https://riscv.atlassian.net/wiki/spaces/IMEX/pages/598867969/IME+Ratification+Plan
source_url: https://riscv.atlassian.net/wiki/spaces/IMEX/pages/598867969/IME+Ratification+Plan
fetched_at: '2026-07-03T13:49:52.970234+00:00'
type: entity
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 0
---

# Integrated Matrix Extension

The Integrated Matrix Extension (IME) is a proposed RISC-V ISA extension designed for high-performance matrix operations targeting both traditional HPC (scientific and technical computing) and modern AI/ML workloads including Large Language Models. IME introduces no new architected state for matrix data; all matrix operands are stored in the existing RISC-V V vector registers, with only modest additions to control registers. The extension defines 32-bit instructions for matrix-level arithmetic and logic operations such as matrix multiplication with accumulation, as well as vector-matrix operations like outer product accumulation. Supporting instructions for packing and unpacking sub-matrices between memory and vector registers are also planned. IME supports a range of data types: IEEE FP64, FP32, bfloat16, INT8, and FP8. The extension's performance ceiling is determined by processor load bandwidth and the amount of matrix state held in vector registers. The IME Task Group, under the Unprivileged Committee, is developing this specification with input from the Vector SIG and AI/ML SIG.

## Key Claims

- IME targets both HPC and AI/ML applications, including Large Language Models.
- Matrix data is stored in existing V vector registers; no new architected state for matrix data.
- IME includes instructions for matrix multiplication, outer product, and supporting packing/unpacking operations.
- Supported data types: IEEE fp64, fp32, bfloat16, int8, fp8.
- All IME instructions are encoded as 32-bit.
- Performance is inherently limited by processor load bandwidth and the amount of matrix state in vector registers.
- Goal: achieve significant speedup over the V extension at similar cost.
- The IME Task Group operates under the Unprivileged Committee with input from Vector SIG and AI/ML SIG.

## Relationships

No specific relationship to visible context pages.

## Sources

- https://riscv.atlassian.net/wiki/spaces/IMEX/pages/598867969/IME+Ratification+Plan
