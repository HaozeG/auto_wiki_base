---
canonical_name: SiFive Performance P570 Gen3
aliases:
- P570 Gen3
- SiFive P570
- Performance P570 Gen3
- P570 Gen 3
- SiFive Performance P570 Gen 3
subtype: null
tags:
- SiFive
- RISC-V
- RVA23
- out-of-order
hardware_targets:
- SiFive Performance P570 Gen3
toolchains:
- GCC
- LLVM
- RISC-V GNU toolchain
- Android
- Ubuntu
- Red Hat Enterprise Linux
constraints:
- RVA23 profile mandatory extensions
- RISC-V Vector Extension 1.0 (RVV)
- 128-bit VLEN vector pipeline
- 3-wide 13-stage out-of-order superscalar
- multicore coherence up to 16 cores (4x 4-core clusters)
- advanced interrupt architecture (AIA)
- WorldGuard security
- IOMMU
scorecard:
  novelty_delta: 0.9
  claim_density: 0.85
  self_containedness: 0.9
  bridge_score: 0.7
  hub_potential: 0.75
sources:
- raw/cache/be2d792fec6c9de9.md
- https://www.cnx-software.com/2026/05/12/sifive-performance-p570-gen3-rva23-compliant-risc-v-core-consumer-aiot-applications/
source_url: https://www.cnx-software.com/2026/05/12/sifive-performance-p570-gen3-rva23-compliant-risc-v-core-consumer-aiot-applications/
fetched_at: '2026-07-02T04:40:01.003634+00:00'
type: hardware_target
created: '2026-07-02'
updated: '2026-07-02'
cold_start: false
inbound_links: 10
needs_summary_revision: false
outbound_links:
- target: llvm_vcix_scheduling_model
  reason: the LLVM scheduling model mechanism for SiFive Vector Coprocessor Interface
    (VCIX) instructions, applicable to this core's SiFive 7-family scheduling
- target: compiler_benchmark_bananapi_f3_gcc15_clang21
  reason: a GCC-vs-Clang RVV 1.0 autovectorization comparison on a different (in-order)
    core, offering a contrasting compiler-quality data point to this out-of-order
    design
---

# SiFive Performance P570 Gen3

The SiFive Performance P570 Gen3 is a 64-bit out-of-order RISC-V processor core released in May 2026 by SiFive. It is compliant with the RVA23 ISA profile, which ensures compatibility with modern operating systems including Ubuntu 26.04 LTS and Red Hat Enterprise Linux. The core is built on a third-generation microarchitecture that features a 3-wide, 13-stage fully out-of-order superscalar pipeline with a single 128-bit vector pipeline supporting dot product extensions. Designed for edge AI, high-end consumer devices, and commercial IoT applications, the P570 Gen3 can be integrated into a complete system-on-chip with up to 16 cores organized in four 4-core clusters. SiFive also provides companion system IP including a RISC-V standard advanced interrupt architecture (AIA), WorldGuard security, and a second-generation IOMMU. The P570 Gen3 delivers significant performance improvements over its predecessors: twice the performance per GHz of the P550 in Geekbench 6, 21x higher performance for AI object-detection workloads, and 30% higher overall performance than the P470 Gen2. Power efficiency is also improved, with 13% and 5% lower dynamic power (mW/GHz) relative to the P550 and P470 respectively, and 51% and 5% lower leakage power. The core supports a broad software ecosystem including Android, Ubuntu, Red Hat, and a full-featured OP-TEE implementation being upstreamed by RISCstar in collaboration with SiFive and the RISC-V Software Ecosystem (RISE) project.

## Key Claims

- RVA23 profile compliance enabling support for Ubuntu 26.04 LTS and Red Hat Enterprise Linux.
- Additional extensions for security and performance: Smepmp, Zvkng, Zvksg, Zicfilp, Zicfiss, Zfbfmin, Zvfbfmin, Zvfbfwma, and Zvdot4a8i.
- Third-generation out-of-order microarchitecture with 3-wide, 13-stage pipeline.
- Single 128-bit vector pipeline with dot product extensions for AI workloads.
- Multicore scalability up to 16 cores in a core complex (4x 4-core clusters).
- 2x performance per GHz vs P550 in Geekbench 6; 21x for AI object detection; 30% vs P470 Gen2.
- SpecInt 2006/2017 performance: 7–13% improvement over P550, same as P470.
- Dynamic power reduction of 13% (vs P550) and 5% (vs P470); leakage reduction of 51% (vs P550) and 5% (vs P470).
- Software ecosystem support: Android, Canonical Ubuntu, Red Hat, OP-TEE via RISCstar/RISE.

## Optimization-Relevant Details

- ISA/profile: RVA23 compliant, RV64 with mandatory RVA23 extensions.
- Vector/matrix/accelerator support: 128-bit VLEN vector pipeline, dot product extensions (Zvdot4a8i, etc.).
- Memory/cache/TLB/DMA: Not disclosed in the source; SoC-level IOMMU provided.
- Compiler/toolchain support: GCC and LLVM (via RISC-V target), Android, Ubuntu, Red Hat. OP-TEE for trusted execution.

## Relationships

- The P570 Gen3 is built on the same lineage as the earlier [[llvm_riscv_target]]-supported cores and benefits from the LLVM RISC-V target for code generation.
- Comparable to [[xuantie_c908]] as a contemporary RISC-V core targeting AIoT workloads, though the P570 is a higher-performance out-of-order design while the C908 is an in-order core with configurable vector length.
- Expected to serve as a hardware target for optimization recipes such as [[mlir_xdsl_rvv_gemm_codegen_recipe]] when targeting the RISC-V vector unit.
- The P570's predecessor, the P550, and its mid-range sibling, the P470, are referenced in performance comparisons but do not yet have dedicated wiki pages.
- [[llvm_vcix_scheduling_model]]: the LLVM scheduling model mechanism for SiFive Vector Coprocessor Interface (VCIX) instructions, applicable to this core's SiFive 7-family scheduling.
- [[compiler_benchmark_bananapi_f3_gcc15_clang21]]: a GCC-vs-Clang RVV 1.0 autovectorization comparison on a different (in-order) core, offering a contrasting compiler-quality data point to this out-of-order design.

## Sources

- https://www.cnx-software.com/2026/05/12/sifive-performance-p570-gen3-rva23-compliant-risc-v-core-consumer-aiot-applications/
- SiFive press release (Business Wire) referenced in the article.
