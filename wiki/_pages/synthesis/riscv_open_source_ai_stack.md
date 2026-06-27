---
type: synthesis
connected_entities: [gemmini, ara_vector_processor, mlir_riscv_backend, iree_riscv, tvm_riscv_backend, risc_v_vector_extension, risc_v_p_extension, boom_riscv, andes_ax45mp_nx27v, xiangshan_riscv]
synthesis_status: draft
created: 2026-06-27
updated: 2026-06-27
cold_start: true
inbound_links: 0
sources:
  - entity/gemmini.md
  - entity/ara_vector_processor.md
  - entity/mlir_riscv_backend.md
  - entity/iree_riscv.md
  - entity/tvm_riscv_backend.md
scorecard:
  bridge_score: ~
  contradiction_potential: ~
  cross_domain_connection: ~
---

# Open-Source RISC-V AI Stack: from ISA to Runtime

## RAG Summary
<!-- 150-250 words, self-contained, no dangling refs, names ≥2 entities explicitly, first sentence = core synthetic claim -->

A complete open-source RISC-V AI software and hardware stack now exists spanning ISA extensions, custom accelerators, and ML compiler runtimes — a level of vertical integration previously available only in proprietary systems. At the ISA level, the ratified RVV 1.0 vector extension provides the programmable compute substrate; Ara2 (ETH Zurich) and Andes NX27V are the leading open-source and commercial silicon implementations, respectively. Gemmini (UC Berkeley) extends the stack with a fixed-function systolic array that attaches to a host RISC-V core (such as BOOM or XiangShan) via the RoCC co-processor interface, enabling energy-efficient matrix multiplication at 106.1 GOPS/W in 22 nm silicon. On the software side, IREE and TVM form competing but complementary ML compiler stacks: IREE uses MLIR's progressive lowering through Linalg → vector dialect → RVV intrinsics, while TVM uses its own tensor expression language and auto-tuning infrastructure. Both as of 2025 lack optimized RISC-V microkernels compared to their ARM or x86 equivalents, a gap being actively closed by community contributions. A key architectural tension exists: the RISC-V P-extension targets area-minimal embedded cores (IoT, tinyML) without a vector register file, while RVV targets higher-throughput application processors. Bridging both with a single ML compiler toolchain remains an open challenge, as P-extension intrinsics and RVV intrinsics require separate code generation paths in TVM and IREE.

---

## Full Synthesis

The open-source RISC-V AI stack can be organized into four layers: (1) ISA extensions, (2) custom accelerators, (3) processor cores, and (4) ML compiler runtimes. Unlike proprietary AI stacks (e.g., NVIDIA CUDA + cuDNN, Apple AMX + CoreML), each layer of the RISC-V stack is independently open-sourced and composable.

### Layer 1: ISA Extensions

The foundational compute abstraction is the RISC-V Vector Extension (RVV 1.0, ratified 2021). RVV uses a variable-length vector model — hardware reports VLEN at runtime, and software scales to it — which distinguishes it from fixed-width SIMD like x86 AVX-512 or ARM NEON. The RISC-V P-extension (packed SIMD, under ratification) targets a different point in the design space: embedded cores that cannot afford the area of a full vector register file but need SIMD throughput for audio, tinyML, and DSP.

### Layer 2: Custom Accelerators

Two major open-source hardware accelerators populate this layer. **Gemmini** (UC Berkeley) is a parameterizable systolic array generator that attaches to any RISC-V core via RoCC, exposing custom instructions (`matmul.preload`, `mvin`, `mvout`) to software. It demonstrated 106.1 GOPS/W on the Beagle SoC in 2021. **Ara2** (ETH Zurich) is a 2–16 lane in-order RVV 1.0 vector processor that functions as a co-processor alongside scalar cores like CVA6, achieving 37.8 DP-GFLOPS/W at 4 lanes in 22 nm FD-SOI.

### Layer 3: Processor Cores

BOOM (UC Berkeley) and XiangShan (ICT-CAS) represent the two leading open-source out-of-order RISC-V cores. BOOM (SonicBOOM, 6.2 CoreMarks/MHz) prioritizes parameterizable research flexibility and integrates with Gemmini. XiangShan Nanhu achieves 16.5 SPEC CPU2006 points/GHz and adds experimental matrix extensions for LLM inference. Commercial cores from Andes (AX45MP + NX27V) and Nuclei (UX900/N900) bridge open-source architecture to production deployment with certified safety profiles (ASIL-D) and proprietary AI data types (BF16, Int4).

### Layer 4: ML Compiler Runtimes

IREE (Google, now open-source) and TVM are the primary compiler stacks. IREE lowers through MLIR Linalg → linalg.mmt4d → RVV microkernels; as of 2024 these microkernels were missing for RISC-V, causing poor GenAI performance. The 2025 paper arXiv:2508.14899 added them. TVM auto-tunes across RISC-V RVV targets and additionally supports the P-extension for embedded quantized inference. MLIR itself provides the shared middle-end used by IREE, with an RVV dialect mapping vector operations to scalable vector types in LLVM IR.

### Tension: Fragmentation Across ISA Points

The P-extension and RVV serve different segments but require separate compiler code generation paths. ML frameworks must choose: deploy once to RVV-capable Linux cores (AX45MP + NX27V, UX900, XiangShan), or separately to P-extension-only MCU cores. No unified abstraction layer currently bridges both in TVM or IREE.

## Open Questions

- Will the RISC-V matrix extension (proposed Zmatmul / AME) unify the systolic/vector distinction, or produce a third incompatible code generation path?
- Can IREE or TVM microkernels for RISC-V reach ARM NEON performance parity on identical operations?
- Will XiangShan Kunminghu integrate Ara-style vector lanes natively, blending the core and accelerator layers?
- How will the P-extension ratification timeline affect TVM's embedded RISC-V deployment story vs. RVV-based alternatives?

## Connected Pages

- [[risc_v_vector_extension]]
- [[risc_v_p_extension]]
- [[gemmini]]
- [[ara_vector_processor]]
- [[boom_riscv]]
- [[xiangshan_riscv]]
- [[tvm_riscv_backend]]
- [[mlir_riscv_backend]]
- [[iree_riscv]]
- [[andes_ax45mp_nx27v]]
- [[nuclei_ux900_n900]]
