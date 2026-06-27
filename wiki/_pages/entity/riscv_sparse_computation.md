---
cold_start: true
created: 2026-06-27
inbound_links: 1
scorecard:
  bridge_score: null
  claim_density: null
  hub_potential: null
  novelty_delta: null
  self_containedness: null
sources:
- https://arxiv.org/html/2501.10189v1
- https://arxiv.org/pdf/2501.10189
- https://codasip.com/2024/03/20/a-custom-risc-v-vector-instruction/
- https://riscv.org/job/rv-sparse-open-source-risc-v-vector-accelerated-sparse-linear-algebra-library-risc-v-mentorship/
tags:
- risc-v
- sparsity
- RVV
- neural-networks
- optimization
- research
type: entity
updated: 2026-06-27
---

# Sparse Computation on RISC-V

Sparse computation on RISC-V refers to the use of the RISC-V Vector (RVV) extension's mask register mechanism and custom ISA extensions to accelerate sparse neural network inference, particularly for pruned convolutional and transformer models where a large fraction of weights are zero or near-zero. RVV's per-element mask register (v0) allows conditional execution of vector operations, which maps naturally onto unstructured sparsity: inactive (pruned) elements can be skipped by setting mask bits. For structured sparsity — where weights are pruned in fixed patterns (e.g., 2:4 sparsity where 2 of every 4 weights are zero) — research from 2025 (arXiv 2501.10189) demonstrates that structured-sparse matrix multiplication on RVV vector processors can be accelerated by 25–33% compared to optimized dense vectorized kernels using only existing RVV instructions, and that a minimal custom RISC-V instruction leveraging a mask register to decompress pruned weight matrices directly into register file positions enables further gains. Codasip published a related custom instruction proposal in March 2024, adding a structured-sparsity decompression instruction to the RVV instruction set extension point. The rv-sparse project, a RISC-V International mentorship initiative, aims to deliver an open-source RVV-accelerated sparse linear algebra library supporting CSR and CSC sparse storage formats with vectorized traversal on any RVV-capable RISC-V processor.

## Key Claims

- RVV mask registers (v0) enable per-element conditional execution, providing a natural hardware mechanism for unstructured sparse inference.
- Structured-sparse matrix multiplication on RVV processors is 25–33% faster than dense vectorized kernels with only existing RVV instructions (arXiv 2501.10189, 2025).
- A minimal custom RISC-V instruction for sparse weight decompression into register file positions further improves structured-sparse throughput.
- Codasip (March 2024) proposed a custom structured-sparsity decompression instruction as an extension to the RVV instruction set.
- The rv-sparse RISC-V mentorship project targets an open-source library with CSR/CSC format support and RVV-vectorized sparse traversal.
- PULP-NN (for PULP Platform) achieves up to 15.5 MACs/cycle on INT8 with sub-byte (4-bit, 2-bit, 1-bit) quantized sparse compute on RISC-V.

## Relationships

- [[risc_v_vector_extension]]: RVV mask registers are the ISA primitive enabling conditional sparse vector operations.
- [[muriscv_nn]]: muRISCV-NN targets dense quantized RISC-V inference; sparse extensions would complement its kernel library.
- [[pulp_platform]]: PULP-NN demonstrates sub-byte sparse inference on PULP RISC-V MCU clusters with 15.5 MACs/cycle INT8.
- [[riscv_matrix_extension]]: The RISC-V matrix extension (AME) is expected to incorporate sparsity support alongside dense matrix operations.

## Sources

- https://arxiv.org/html/2501.10189v1 (structured-sparse MatMul on RVV, 25–33% speedup)
- https://arxiv.org/pdf/2501.10189 (full paper PDF)
- https://codasip.com/2024/03/20/a-custom-risc-v-vector-instruction/ (custom RISC-V structured-sparsity instruction proposal)
- https://riscv.org/job/rv-sparse-open-source-risc-v-vector-accelerated-sparse-linear-algebra-library-risc-v-mentorship/ (rv-sparse mentorship project)
