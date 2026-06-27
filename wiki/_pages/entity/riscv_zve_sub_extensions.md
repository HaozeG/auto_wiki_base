---
type: entity
tags: []
sources:
  - https://lkml.org/lkml/2024/5/10/8
  - https://patchew.org/linux/20240510-zve-detection-v5-0-0711bdd26c12@sifive.com/20240510-zve-detection-v5-6-0711bdd26c12@sifive.com/
  - http://mirror.iscas.ac.cn/riscv-toolchains/release/riscv/riscv-isa-manual/Release%20riscv-isa-release-7749d5d-2025-05-19/riscv-unprivileged.pdf
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

# RISC-V Zve* Sub-Extensions

The RISC-V Zve* (Vector Extensions for Embedded Processors) family is a set of five standard vector sub-extensions defined in the RISC-V Unprivileged Specification that provide scaled-down vector capabilities for resource-constrained embedded processors, including IoT microcontrollers and edge AI accelerators. The family consists of Zve32x (minimum VLEN 32 bits, integer-only, maximum element width 32 bits), Zve32f (adds single-precision FP), Zve64x (minimum VLEN 64 bits, integer-only, maximum element width 64 bits), Zve64f (adds single-precision FP), and Zve64d (adds double-precision FP). The naming convention encodes the maximum supported element width (32 or 64 bits) and FP capability (X = none, F = single-precision, D = double-precision). All Zve* extensions support the full vector integer instruction set (excluding vmulh variants for 64-bit elements in Zve64*), vector fixed-point arithmetic, single-width and widening integer reductions, vector mask operations, and vector permutation instructions. The dependency chain is hierarchical: Zve32x depends only on Zicsr, Zve32f adds the F extension and Zve32x, Zve64x depends on Zve32x, and so forth — these dependencies were formally codified in Linux kernel device-tree bindings in 2024 to prevent invalid ISA string combinations. The Zve* family is the critical enabler for embedded TinyML inference on low-cost RISC-V MCUs, allowing integer-quantized neural network kernels (INT8, INT16) to exploit vector parallelism without the hardware cost of full RVV (which mandates VLEN ≥ 128 and FP64 support). As of Linux kernel 6.10 (merged May 2024, patches by SiFive's Andy Chiu), all five Zve* sub-extensions are exposed to userspace via the RISC-V hwprobe interface, enabling ML runtimes such as TensorFlow Lite Micro and ONNX Runtime to query available vector capabilities for runtime dispatch of optimized inference kernels.

## Key Claims

- The Zve* family defines five extensions (Zve32x, Zve32f, Zve64x, Zve64f, Zve64d) with minimum VLEN of either 32 or 64 bits, compared to full RVV which mandates VLEN ≥ 128 and FP64 support.
- Zve32x and Zve64x provide integer-only vector operations, directly enabling INT8/INT16 quantized neural network inference on MCU-class RISC-V cores without any floating-point vector hardware.
- Linux kernel 6.10 (May 2024) added Zve* detection via the RISC-V hwprobe interface at bits 37–41 of RISCV_HWPROBE_KEY_IMA_EXT_0, enabling userspace ML runtimes to discover and dispatch to optimized vector kernels.
- The formal dependency chain codified in 2024 device-tree bindings prevents illegal ISA combinations — for example, Zve64f requires both Zve32f and Zve64x, which together require F, Zve32x, and Zicsr.
- All Zve* extensions include the full vector configuration (vsetvli and related), vector load/store, vector integer arithmetic, vector fixed-point, vector mask, and vector permutation instruction subsets — a substantial fraction of the full V extension.
- The Zve* extensions are specifically positioned as the embedded AI inference baseline: Zve32x for INT8-only TinyML, Zve32f for FP32 models on MCU-class devices, and Zve64f for higher-precision embedded workloads.

## Relationships

- [[risc_v_vector_extension]]: The Zve* family is a strict subset of the full V extension, trading vector length and FP precision for reduced hardware area — all Zve* instructions are valid V-extension instructions.
- [[canaan_kendryte_k510_k230]]: The K230 implements full RVV 1.0 (128-bit VLEN) rather than a Zve* profile, but its dual-core architecture (with/without VPU) demonstrates the same design philosophy of scaling vector capabilities to application requirements.
- [[risc_v_p_extension]]: The P-extension (Packed SIMD) targets a similar embedded DSP space as Zve* but uses a SIMD paradigm rather than vector — both address integer signal processing and quantized inference on low-cost cores.

## Sources

- https://lkml.org/lkml/2024/5/10/8
- https://patchew.org/linux/20240510-zve-detection-v5-0-0711bdd26c12@sifive.com/20240510-zve-detection-v5-6-0711bdd26c12@sifive.com/
- http://mirror.iscas.ac.cn/riscv-toolchains/release/riscv/riscv-isa-manual/Release%20riscv-isa-release-7749d5d-2025-05-19/riscv-unprivileged.pdf
