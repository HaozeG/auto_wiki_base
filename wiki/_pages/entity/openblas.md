---
canonical_name: OpenBLAS
aliases: []
subtype: null
tags: []
scorecard:
  novelty_delta: 0.6
  claim_density: 0.5
  self_containedness: 0.8
  bridge_score: 0.7
  hub_potential: 0.5
sources:
- raw/cache/7faacd6b50447ac2.md
- https://sourceforge.net/projects/openblas/files/v0.3.28/
source_url: https://sourceforge.net/projects/openblas/files/v0.3.28/
fetched_at: '2026-07-06T02:12:23.471404+00:00'
type: entity
created: '2026-07-06'
updated: '2026-07-06'
cold_start: true
inbound_links: 0
outbound_links:
- target: xuantie-c920v2-hardware-target
  reason: OpenBLAS 0.3.28's DYNAMIC_ARCH support for RVV 1.0 with VLEN 128 and 256
    directly enables optimized BLAS operations on the C920v2 core, which implements
    RVV 1.0 with 128-bit VLEN
- target: sophon-sg2044-hardware-target
  reason: The SG2044's C920v2 cores can leverage OpenBLAS 0.3.28's RISC-V RVV 1.0
    support for accelerated GEMM and other BLAS routines, as the changelog confirms
    addition of DYNAMIC_ARCH for RVV 1.0 targets
- target: vicuna-2-0-hardware-target
  reason: While Vicuna 2.0 is a vector coprocessor targeting embedded systems, OpenBLAS's
    RVV 1.0 support may apply if the host scalar core uses RVV; however, Vicuna 2.0
    implements the Zve32x/Zve32f subset of RVV 1.0, which is compatible with OpenBLAS's
    generic RISC-V RVV 1.0 DYNAMIC_ARCH targets
---

# OpenBLAS

OpenBLAS is an optimized Basic Linear Algebra Subprograms (BLAS) library based on GotoBLAS2. It provides highly tuned implementations of BLAS routines for various processor architectures including x86_64, ARM, ARM64, POWER, RISC-V, and LoongArch. Version 0.3.28, released in August 2024, adds significant improvements for RISC-V: DYNAMIC_ARCH support encompassing GENERIC_RISCV64 and RVV 1.0 targets with vector lengths of 128 and 256, fixes for OpenMP compilation on RISCV64_GENERIC, and a workaround for the ZVL128B kernels mishandling zero Y increment in AXPBY. The library supports multithreading with an optional callback function for external backends like TBB, and includes the CBLAS_GEMM_BATCH extension. Across architectures, version 0.3.28 improves multithreaded GEMM performance, fixes accuracy issues in various kernels, and enhances build system support for cross-compilation and compiler detection.

## Key Claims

- OpenBLAS is an optimized BLAS library based on GotoBLAS2.
- Version 0.3.28 introduced DYNAMIC_ARCH support for RISC-V including GENERIC_RISCV64 and RVV 1.0 targets with vector lengths of 128 and 256.
- Version 0.3.28 improved multithreaded GEMM performance for large non-skinny matrices.
- Version 0.3.28 added an implementation of the CBLAS_GEMM_BATCH extension.
- Version 0.3.28 fixed multiple accuracy and compilation issues across x86_64, ARM, ARM64, POWER, RISC-V, and LoongArch.
- The library supports a callback function (openblas_set_threads_callback_function) for multithreading with external backends like TBB.
- Version 0.3.28 added a fast path for SGEMM/DGEMM 1xN or Mx1 calls on ARM64 and optimized SGEMV/DGEMV kernels for A64FX.
- On POWER10, version 0.3.28 significantly improved SBGEMM performance.

## Relationships

- [[xuantie-c920v2-hardware-target]]: OpenBLAS 0.3.28's DYNAMIC_ARCH support for RVV 1.0 with VLEN 128 and 256 directly enables optimized BLAS operations on the C920v2 core, which implements RVV 1.0 with 128-bit VLEN.
- [[sophon-sg2044-hardware-target]]: The SG2044's C920v2 cores can leverage OpenBLAS 0.3.28's RISC-V RVV 1.0 support for accelerated GEMM and other BLAS routines, as the changelog confirms addition of DYNAMIC_ARCH for RVV 1.0 targets.
- [[vicuna-2-0-hardware-target]]: While Vicuna 2.0 is a vector coprocessor targeting embedded systems, OpenBLAS's RVV 1.0 support may apply if the host scalar core uses RVV; however, Vicuna 2.0 implements the Zve32x/Zve32f subset of RVV 1.0, which is compatible with OpenBLAS's generic RISC-V RVV 1.0 DYNAMIC_ARCH targets.

## Sources

- https://sourceforge.net/projects/openblas/files/v0.3.28/
