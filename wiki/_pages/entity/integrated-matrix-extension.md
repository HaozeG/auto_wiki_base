---
canonical_name: Integrated Matrix Extension
aliases:
- IME
- RISC-V IME Extension
- SpacemiT RISC-V IME
- RISCV IME
- Intelligent Matrix Engine
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
- raw/cache/f08fc9741536d1a3.md
- https://deepwiki.com/spacemit-com/riscv-ime-extension-spec
source_url: https://riscv.atlassian.net/wiki/spaces/IMEX/pages/598867969/IME+Ratification+Plan
fetched_at: '2026-07-03T13:49:52.970234+00:00'
type: entity
created: '2026-07-03'
updated: '2026-07-06'
cold_start: true
inbound_links: 0
---

# Integrated Matrix Extension

The Integrated Matrix Extension (IME) is a proposed RISC-V ISA extension designed for high-performance matrix operations targeting both traditional HPC (scientific and technical computing) and modern AI/ML workloads including Large Language Models and convolution. IME introduces no new architected state for matrix data; all matrix operands are stored in the existing RISC-V V vector registers, with only modest additions to control registers. The extension defines 32-bit instructions for matrix-level arithmetic and logic operations such as matrix multiplication with accumulation, as well as vector-matrix operations like outer product accumulation. Supporting instructions for packing and unpacking sub-matrices between memory and vector registers are also planned. IME supports a range of data types: IEEE FP64, FP32, bfloat16, INT8, and FP8. The extension supports vector lengths (VLEN) from 128 bits to 4096 bits, providing compatibility across a wide range of implementations while maintaining almost binary compatibility. The IME extension aims to deliver more than a tenfold performance improvement for AI matrix multiplication and convolution workloads at a very small hardware cost. Performance is inherently limited by processor load bandwidth and the amount of matrix state in vector registers. The IME Task Group, under the Unprivileged Committee, is developing this specification with input from the Vector SIG and AI/ML SIG. A detailed specification authored by SpacemiT (referring to the extension as the Intelligent Matrix Engine) is available on GitHub, written in AsciiDoctor following standard RISC-V documentation conventions, and organized for easy building and contribution.

## Key Claims

- IME targets both HPC and AI/ML applications, including Large Language Models and convolution.
- Matrix data is stored in existing V vector registers; no new architected state for matrix data.
- IME includes instructions for matrix multiplication, outer product, and supporting packing/unpacking operations.
- Supported data types: IEEE fp64, fp32, bfloat16, int8, fp8.
- All IME instructions are encoded as 32-bit.
- Supports VLEN from 128 bits to 4096 bits for broad implementation compatibility.
- Almost binary compatibility across different VLEN configurations.
- Can achieve >10x performance improvement for AI matrix multiplication and convolution workloads.
- Performance is inherently limited by processor load bandwidth and the amount of matrix state in vector registers.
- The IME Task Group operates under the Unprivileged Committee with input from Vector SIG and AI/ML SIG.
- The specification is open-source on GitHub (authored by SpacemiT) and written in AsciiDoctor.

## Relationships

No specific relationship to visible context pages.

## Sources

- https://riscv.atlassian.net/wiki/spaces/IMEX/pages/598867969/IME+Ratification+Plan
- https://github.com/spacemit-com/riscv-ime-extension-spec
- https://deepwiki.com/spacemit-com/riscv-ime-extension-spec
