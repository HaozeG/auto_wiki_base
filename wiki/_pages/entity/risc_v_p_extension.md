---
cold_start: true
created: 2026-06-27
inbound_links: 6
needs_summary_revision: true
scorecard:
  bridge_score: null
  claim_density: null
  hub_potential: null
  novelty_delta: null
  self_containedness: null
sources:
- https://github.com/riscv/riscv-p-spec
- https://riscv.org/blog/imperas-updates-free-reference-model-riscvovpsimplus-with-new-risc-v-p-simd-dsp-extension-and-architectural-validation-test-suites/
- https://ieeexplore.ieee.org/document/11129627/
- https://dl.acm.org/doi/full/10.1145/3569939
tags:
- risc-v
- dsp
- packed-simd
- embedded
- tinyml
- isa-extension
type: entity
updated: 2026-06-27
---

# RISC-V P-Extension (Packed SIMD)

The RISC-V P-extension (officially "Packed SIMD/DSP extension") defines instructions that operate on sub-word SIMD data packed within standard XLEN-width integer registers, enabling DSP and lightweight AI operations without adding separate vector registers or co-processor hardware. Unlike the V-extension (RVV), which uses a dedicated scalable vector register file, the P-extension works entirely within the 32-bit or 64-bit general-purpose registers, making it suitable for constrained embedded processors where area and power budgets prohibit a full vector unit. The specification was originally developed by Andes Technology Corporation and contributed to RISC-V International.

## Key Claims

- P-extension instructions pack multiple narrow data elements (Int4, Int8, Int16) into a single XLEN register and operate on them in parallel (e.g., four 8-bit MACs in one 32-bit register for RV32).
- Operates entirely within the existing integer register file (x0–x31), requiring no additional architectural register state — critical for area-minimal embedded implementations.
- The specification is a work-in-progress (not yet ratified as of 2025) in the RISC-V P Extension Task Group; GCC, binutils, and QEMU development implementations exist.
- Andes Technology's AX45MP and N25F/NX25F cores include P-extension support; Andes certified the Imperas RISC-V reference model for P-extension architectural validation testing.
- A P-CORE paper (IEEE Xplore, 2025) demonstrated P-extension hardware exploration for CNN inference, achieving measurable throughput gains over scalar execution on embedded RISC-V without vector hardware.
- TVM auto-tuning for fixed-point precision with the P-extension (ACM TODS, 2023) showed that P-extension SIMD can accelerate tinyML workloads on embedded RISC-V by 2–4× versus scalar baselines when combined with quantization.
- Target markets: audio/speech processing, IoT, tinyML, and edge devices where RVV is too expensive in silicon area and power.

## Relationships

- [[risc_v_vector_extension]]: P-extension is the lightweight embedded counterpart to RVV; targets area-constrained MCUs where RVV's scalable vector register file is prohibitive.
- [[andes_ax45mp_nx27v]]: Andes Technology contributed the P-extension spec; their AX45MP cores include P-extension alongside RVV via the NX27V co-processor.
- [[tvm_riscv_backend]]: TVM supports P-extension intrinsics for quantized model inference on embedded RISC-V targets.

## Sources

- GitHub spec: https://github.com/riscv/riscv-p-spec
- RISC-V blog (Imperas): https://riscv.org/blog/imperas-updates-free-reference-model-riscvovpsimplus-with-new-risc-v-p-simd-dsp-extension-and-architectural-validation-test-suites/
- P-CORE CNN paper: https://ieeexplore.ieee.org/document/11129627/
- TVM P-extension paper: https://dl.acm.org/doi/full/10.1145/3569939
