---
cold_start: true
created: '2026-12-03'
inbound_links: 0
scorecard:
  bridge_score: '~'
  claim_density: '~'
  contradiction_potential: '~'
  gap_fill_score: '~'
  hub_potential: '~'
  novelty_delta: '~'
  self_containedness: '~'
sources:
- the-architecture-that-was-right-about-everything.md
tags:
- itanium
- epic
- vliw
- architecture
- ai-accelerators
- nvidia
- tpu
type: entity
updated: '2026-12-03'
---

# Intel Itanium

Intel Itanium is a 64-bit VLIW (Very Long Instruction Word) architecture based on EPIC (Explicitly Parallel Instruction Computing) principles, first released in 2001. It aimed to extract instruction-level parallelism entirely in hardware through compiler orchestration, relying on features such as wide instruction bundles, predicated execution (removing branches), speculative loads (to hide memory latency), register rotation (for software pipelining), and a large register file of 128 integer and 128 floating-point registers. Despite its innovative design, Itanium failed commercially due to poor compiler maturity, high power consumption, backward-compatibility issues with x86, and market dominance of x86 and RISC architectures. Production was discontinued by 2020. However, the article "The Architecture That Was Right About Everything" argues that Itanium's core ideas have been rediscovered and adapted in modern AI accelerator architectures, including NVIDIA's CUDA cores (which use predication, wide warps, and large register files), Google's Tensor Processing Unit (TPU) (which employs VLIW-style instruction bundles and systolic arrays), and emerging RISC-V extensions (such as the V vector extension and matrix extensions like IME/VME/AME). This retrospective positions Itanium not as a failure of ideas but as a case of premature optimization for a workload that did not yet exist.

## Key Claims

- Itanium used EPIC features: predicated execution, speculative loads, register rotation, and wide instruction bundles of three instructions each.
- Compiler inability to exploit EPIC parallelism was the primary cause of performance shortfall versus hand-scheduled VLIW or dynamically scheduled superscalar processors.
- Itanium's register rotation mechanism for software pipelining is conceptually similar to NVIDIA GPU's warp scheduling and register file banking.
- Predicated execution, which eliminates branch mispredictions, is now used extensively in NVIDIA GPUs to handle diverging warps.
- Large register files (128 each) anticipated the need for keeping many threads in flight, a key technique in modern GPUs.
- Google's TPU uses a VLIW-like control paradigm and systolic array execution, echoing Itanium's bundle-based parallelism.
- RISC-V's vector extension (RVV) and matrix extensions are exploring similar terrain of wide, compiler-managed parallelism.
- The article claims Itanium was "right about everything" because its architectural choices align with the demands of modern AI workloads (parallel, data-intensive, branch-predictable).

## Relationships

- [[risc_v_vector_extension]]: Itanium's register rotation and wide instructions are conceptual precursors to RISC-V's vector length agnostic design.
- [[fpga_riscv_isa_extension_nn_inference]]: FPGA prototypes of RISC-V AI extensions share the VLIW/EPIC goal of exposing parallelism to the compiler, though implemented on a different substrate.
- [[nvidia_cuda_architecture]]: NVIDIA GPUs incorporate predication, large register files, and wide warps, which are descendants of EPIC ideas.
- [[google_tpu]]: TPU's VLIW-style instruction scheduling and systolic array processing reflect the bundle-based parallel execution philosophy of Itanium.

## Sources

- the-architecture-that-was-right-about-everything.md: Main source for all claims about Itanium's features, failure, and modern parallels.

