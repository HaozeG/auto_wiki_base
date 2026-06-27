---
type: entity
tags: [risc-v, ISA, vector, embedded, microcontroller, tinyML, Zve]
sources:
  - https://riscv.github.io/riscv-isa-manual/snapshot/spec/
  - https://fprox.substack.com/p/taxonomy-of-risc-v-vector-extensions
  - https://llvm.org/docs/RISCVUsage.html
  - https://github.com/riscvarchive/riscv-v-spec/commit/808a6f83b72d92757ef4c93fcdf076ed99bbecae
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

# RISC-V Zve* Embedded Vector Sub-Extensions

The RISC-V Zve* sub-extensions are a family of embedded vector profiles derived from the full RISC-V Vector (RVV 1.0) specification, designed for microcontroller and resource-constrained processors where implementing the complete V extension would be impractical. They were ratified as part of the RVV 1.0 standard (November 2021) and share the same variable-length vector register model (VLEN/ELEN abstraction) as the full V extension but relax certain requirements. Five sub-extensions exist: Zve32x and Zve32f restrict the maximum element width (ELEN) to 32 bits — eliminating 64-bit element operations entirely — while Zve64x, Zve64f, and Zve64d allow 64-bit element widths. The "x" suffix indicates no vector floating-point unit; "f" adds 32-bit (single-precision) FP; "d" (Zve64d only) adds 64-bit (double-precision) FP. Zve64d differs from the full V extension by not mandating vmulh* (widening integer multiply-high) and vsmul* (saturating multiply) instructions, keeping die area lower. LLVM and GCC both expose these sub-extensions via -march= flags (e.g., rv32gcv_zve32x), and Linux hwprobe can query them at runtime. Zve extensions are important for TinyML and IoT workloads because they enable efficient SIMD without committing to full 64-bit vector hardware.

## Key Claims

- Five Zve sub-extensions: Zve32x, Zve32f, Zve64x, Zve64f, Zve64d — all ratified in RVV 1.0 (November 2021).
- Zve32x / Zve32f: ELEN capped at 32 bits; 64-bit element operations (EEW=64) are illegal.
- "x" suffix = no vector FPU; "f" suffix = single-precision FP; "d" suffix = double-precision FP.
- Zve64d omits vmulh* and vsmul* instructions vs. full V extension, reducing implementation cost.
- All Zve extensions share the same VLEN-agnostic programming model as full RVV 1.0.
- LLVM and GCC support Zve sub-extensions via -march= flags; Linux hwprobe exposes them at runtime.

## Relationships

- [[risc_v_vector_extension]]: Zve* are embedded subsets of full RVV 1.0; full V implies all Zve sub-extensions.
- [[risc_v_p_extension]]: P-extension (packed SIMD) targets fixed-width MCUs while Zve* targets scalable-vector MCUs.
- [[nuclei_ux900_n900]]: Nuclei's embedded RISC-V cores support Zve sub-extensions for constrained AI inference.
- [[canaan_kendryte_k230]]: K230's secondary CPU0 core uses base scalar ISA while CPU1 uses full RVV 1.0.

## Sources

- https://riscv.github.io/riscv-isa-manual/snapshot/spec/
- https://fprox.substack.com/p/taxonomy-of-risc-v-vector-extensions
- https://llvm.org/docs/RISCVUsage.html
