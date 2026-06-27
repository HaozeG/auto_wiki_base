---
type: entity
tags: [risc-v, vector-processor, UC-Berkeley, research, accelerator, history]
sources:
  - http://hwacha.org/
  - https://people.eecs.berkeley.edu/~krste/papers/EECS-2015-263.pdf
  - https://people.eecs.berkeley.edu/~krste/papers/eos18-esscirc2014.pdf
  - https://arxiv.org/pdf/1906.00478
created: 2026-06-27
updated: 2026-06-27
cold_start: true
inbound_links: 0
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# Hwacha Vector Accelerator

Hwacha is an explicitly decoupled vector-fetch accelerator developed at UC Berkeley as a research predecessor to the RISC-V Vector (RVV) extension. Designed between approximately 2013 and 2017, Hwacha attaches to the Rocket RISC-V core via the RoCC (Rocket Custom Coprocessor) interface and executes a separate vector instruction stream issued from scalar code, avoiding the single-instruction-stream model of later SIMD designs like ARM NEON or Intel AVX. Architecturally, Hwacha draws inspiration from the Cray-style traditional vector pipelines of the 1970s and 1980s rather than from SIMD extensions; it consists of one or more replicated vector lanes with dedicated Vector Memory Units (VMUs) and Vector Processing Units (VPUs) for floating-point computation. An early ASIC prototype was fabricated in a 45 nm SOI process: a dual-core RISC-V system with Hwacha vector accelerators achieving 16.7 double-precision GFLOPS/W, representing the first silicon demonstration of a RISC-V vector accelerator. Hwacha's explicit decoupling, where the vector fetch engine can issue ahead of the scalar core, differs from the coupled single-instruction-stream model ultimately chosen for RVV 1.0. Lessons from Hwacha about lane scalability, memory access patterns, and mixed-precision support directly informed the RISC-V V extension specification, making Hwacha the primary architectural antecedent to the current RISC-V vector ecosystem including Ara and SiFive X280.

## Key Claims

- Hwacha is an explicitly decoupled vector accelerator attached to RISC-V Rocket via the RoCC interface, developed at UC Berkeley circa 2013–2017.
- A 45 nm SOI ASIC prototype achieved 16.7 double-precision GFLOPS/W, the first silicon RISC-V vector accelerator.
- Hwacha's microarchitecture separates VMU (Vector Memory Unit) and VPU (Vector Processing Unit) pipelines within each lane.
- The explicitly decoupled vector-fetch model differs from the single-instruction-stream approach adopted by RVV 1.0.
- Hwacha directly influenced the RISC-V V extension specification; Ara (ETH Zurich) and later RVV processors are its architectural successors.
- The Hwacha Microarchitecture Manual (version 3.8.1) is a public document describing the full lane and pipeline organization.

## Relationships

- [[ara_vector_processor]]: Ara (ETH Zurich) is the direct open-source successor that implements RVV 1.0 in the tradition Hwacha established.
- [[risc_v_vector_extension]]: RVV 1.0 adopted the single-instruction stream model, departing from Hwacha's explicit decoupling while retaining lane scalability.
- [[gemmini]]: Gemmini uses the same RoCC interface to Rocket as Hwacha, both being Berkeley accelerator research projects.
- [[chipyard_soc_framework]]: Chipyard integrates Rocket+Hwacha configurations as historical reference designs.

## Sources

- http://hwacha.org/ (official Hwacha project page)
- https://people.eecs.berkeley.edu/~krste/papers/EECS-2015-263.pdf (Hwacha Microarchitecture Manual v3.8.1)
- https://people.eecs.berkeley.edu/~krste/papers/eos18-esscirc2014.pdf (45nm ESSCIRC 2014 silicon results, 16.7 DP-GFLOPS/W)
- https://arxiv.org/pdf/1906.00478 (Ara paper references Hwacha as predecessor)
