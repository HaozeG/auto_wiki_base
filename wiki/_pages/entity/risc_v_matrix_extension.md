---
type: entity
tags: [risc-v, ISA, matrix, AI-acceleration, standardization, HPC, RVA23]
sources:
  - https://riscv.org/blog/stream-computing-risc-v-matrix-extension-open-source-project-upgrades-to-version-0-5-supporting-vectormatrix-implementation/
  - https://www.hpcwire.com/off-the-wire/risc-v-announces-ratification-of-the-rva23-profile-standard/
  - https://www.jonpeddie.com/news/whats-on-tap-from-risc-v-in-2025/
  - https://www.electronicdesign.com/technologies/embedded/digital-ics/processors/article/55283485/risc-v-international-more-about-the-risc-v-rva23-profile
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

# RISC-V Matrix Extension Standardization

The RISC-V matrix extension is an in-progress ISA standardization effort aimed at providing native instruction-set support for matrix multiply-accumulate (MATMUL) and tensor operations — the dominant compute kernel in modern AI/ML workloads. Unlike vector (RVV 1.0, ratified 2021) and packed-SIMD (P-extension) extensions already in the RISC-V ecosystem, a standardized matrix extension remains under active development as of mid-2026. The RVA23 Profile, ratified by RISC-V International in October 2024, mandates RVV 1.0 and several other extensions but does not yet include a ratified matrix extension — instead the profile documentation flags matrix as a key area for future standardization. The most concrete open implementation is from Stream Computing: their RISC-V Matrix ISA Specification reached v0.5 in August 2024, with LLVM-based compiler toolchain, Spike-based simulator, GDB debugger, and an open-source SCOOP platform core all supporting the spec by October 2024. The spec defines a Vector+Matrix combined implementation model. Independent of Stream Computing, academic proposals include Quadrilatero (a programmable matrix coprocessor for low-power edge) and DARE (an irregularity-tolerant matrix processing unit). RISC-V International has a dedicated matrix extension Task Group and AI/ML SIG driving standardization, with hardware products based on ratified matrix instructions expected after RVA23+.

## Key Claims

- RVA23 Profile ratified October 2024 mandates RVV 1.0 but does NOT include a ratified matrix extension.
- Stream Computing's RISC-V Matrix ISA Specification v0.5 completed August 2024; toolchain (LLVM, Spike, GDB) ready by October 2024.
- Stream Computing spec supports Vector+Matrix combined implementation on a single SCOOP-derived open-source core.
- RISC-V International's AI/ML SIG and a Matrix Extension Task Group are driving the standardization process.
- Academic proposals include Quadrilatero (edge matrix coprocessor) and DARE (irregularity-tolerant matrix unit).
- Products based on a ratified RISC-V matrix extension expected in the 2026+ timeframe.

## Relationships

- [[risc_v_vector_extension]]: Matrix extension builds on RVV 1.0 as the foundation; RVA23 mandates RVV while matrix remains pending.
- [[alibaba_xuantie_c950]]: C950's AME (Attached Matrix Extension) is a proprietary matrix accelerator predating ISA standardization.
- [[tvm_riscv_backend]]: TVM will need updated lowering passes once a standard matrix extension is ratified.
- [[mlir_riscv_backend]]: MLIR's RISC-V backend lowering pipeline will require new dialect ops for matrix instructions.

## Sources

- https://riscv.org/blog/stream-computing-risc-v-matrix-extension-open-source-project-upgrades-to-version-0-5-supporting-vectormatrix-implementation/
- https://www.hpcwire.com/off-the-wire/risc-v-announces-ratification-of-the-rva23-profile-standard/
- https://www.jonpeddie.com/news/whats-on-tap-from-risc-v-in-2025/
- https://www.electronicdesign.com/technologies/embedded/digital-ics/processors/article/55283485/risc-v-international-more-about-the-risc-v-rva23-profile
