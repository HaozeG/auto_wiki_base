---
type: entity
tags: []
sources:
  - https://github.com/riscv-admin/attached-matrix-extension/blob/main/charter.adoc
  - https://riscv.org/blog/enhancing-the-future-of-ai-ml-with-attached-matrix-extension/
  - https://lists.riscv.org/g/tech-attached-matrix-extension/topic/meeting_minutes_attached/105135992
created: 2026-06-27
updated: 2026-06-27
cold_start: true
inbound_links: 2
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# RISC-V Matrix Extension Proposals

The RISC-V Attached Matrix Extension (AME) is an in-development ISA extension standardized by a RISC-V International Task Group to accelerate matrix-multiply operations for AI/ML and HPC workloads. Unlike the existing RISC-V Vector Extension (RVV) which processes one-dimensional vectors, AME introduces explicit architectural state in the form of matrix tile registers and defines instructions for matrix-matrix, vector-matrix, and scalar-matrix arithmetic, convolution, reduction, and sparse-matrix operations. The TG was chartered with the requirement that AME must be implementable either standalone (without RVV) or as a coupled accelerator alongside RVV, and explicitly supports both tightly coupled (1:1) and shared (M:N) hart-to-matrix-unit configurations. Target datatypes span HPC (FP64, FP32) and AI/ML (INT8, FP4, FP6, FP8, FP16, BF16) with widened accumulators. As of early 2025, the specification is in active development with industry contributions from Alibaba/T-Head (whose XuanTie C907 already implements a precursor Matrix Multiply Extension achieving 4–7× speedup over vector-only execution), SiFive, UC Berkeley, and VRULL. The AME is distinct from the conceptually separate Integrated Matrix Extension (IME) approach, which would add matrix operations directly to the RVV register file without new architectural state.

## Key Claims

- The AME Task Group charter requires that the extension be implementable without the RISC-V Vector Extension, making it viable for cost-sensitive embedded AI accelerators that omit full RVV hardware.
- Alibaba/T-Head's XuanTie C907 processor implements a precursor Matrix Multiply Extension (MME) achieving 4–7× speedup over vector-only execution on matrix-heavy AI kernels.
- AME supports data types spanning FP64, FP32, BF16, FP16, FP8, FP6, FP4, and INT8, with separate single-width and widened accumulator provisions for HPC and AI/ML respectively.
- The SiFive AME proposal (February 2025) defines an RVV-coupled design where matrix tiles are loaded from vector registers, while UC Berkeley's Xbme proposal (September 2024) advocates a lightweight outer-product approach with minimal new state.
- The RISC-V RVA23 profile, ratified October 2024, mandates the Vector Extension 1.0 and Vector Crypto but does not yet include any matrix extension — AME ratification is targeted for a future profile.
- AME will require Linux kernel support for context switching of matrix register state, analogous to how RVV vector registers are saved and restored on context switch, plus SAIL formal model and ACT compatibility tests.

## Relationships

- [[risc_v_vector_extension]]: AME can operate either as a coupled accelerator using RVV registers for data movement or as a fully standalone extension independent of RVV — both modes are charter requirements.
- [[xiangshan_riscv]]: The Xiangshan high-performance RISC-V core series represents a potential future integration target for ratified AME in Chinese domestic server-class processors.
- [[alibaba_xuantie_c910_c920]]: Alibaba/T-Head's C907 processor implements a precursor MME, and the XuanTie line provides real-world feedback on matrix extension design tradeoffs.
- [[tenstorrent_tt_ascalon]]: Tenstorrent's AI accelerators use RISC-V cores alongside custom matrix engines; a ratified AME would provide a standard ISA alternative to proprietary matrix interfaces.

## Sources

- https://github.com/riscv-admin/attached-matrix-extension/blob/main/charter.adoc
- https://riscv.org/blog/enhancing-the-future-of-ai-ml-with-attached-matrix-extension/
- https://lists.riscv.org/g/tech-attached-matrix-extension/topic/meeting_minutes_attached/105135992
