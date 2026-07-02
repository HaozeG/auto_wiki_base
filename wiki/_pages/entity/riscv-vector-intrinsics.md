---
canonical_name: RISC-V Vector Intrinsics
aliases:
- GCC RISC-V Vector Intrinsics
- RVV Intrinsics
- riscv_vector.h
- RISC-V Vector C Intrinsics
- RISC-V V extension intrinsics
- RVV C intrinsics
subtype: null
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.7
  self_containedness: 0.9
  bridge_score: 0.6
  hub_potential: 0.7
sources:
- raw/cache/1832799e1fb9c123.md
- https://gcc.gnu.org/onlinedocs/gcc-13.1.0/gcc/RISC-V-Vector-Intrinsics.html
- raw/cache/c6fd44b003a42be6.md
- https://github.com/riscv-non-isa/riscv-rvv-intrinsic-doc/blob/main/doc/rvv-intrinsic-spec.adoc
- raw/cache/1854701592a00b21.md
- https://runebook.dev/en/docs/gcc/risc_002dv-vector-intrinsics
source_url: https://gcc.gnu.org/onlinedocs/gcc-13.1.0/gcc/RISC-V-Vector-Intrinsics.html
fetched_at: '2026-07-02T09:52:54.906605+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# RISC-V Vector Intrinsics

RISC-V Vector Intrinsics are a set of functions and macros that allow developers to write C/C++ code that directly uses the RISC-V Vector Extension (RVV) instructions. GCC, the GNU Compiler Collection, supports these intrinsics as specified in version 0.11 of the RISC-V vector intrinsic specification, available from the riscv-non-isa repository. The intrinsics are declared in the include file `riscv_vector.h`, and the availability of specific intrinsic variants depends on the required architecture specified via the `-march` compiler option. The implementation has been integrated into the risc-gnu-toolchain and has been verified using internal test suites and projects. In addition to GCC, the LLVM toolchain also supports RVV intrinsics. This GCC documentation covers RISC-V vector intrinsics as part of the built-in functions specific to RISC-V target machines, and includes versions such as GCC 14.

## Key Claims

- GCC supports vector intrinsics per version 0.11 of the RISC-V vector intrinsic specification.
- All intrinsic functions are declared in the header file `riscv_vector.h`.
- The intrinsics enable C/C++ code to directly use RISC-V Vector Extension instructions.
- Availability of intrinsic variants depends on the required architecture specified via `-march`.
- RVV intrinsics have been integrated into the risc-gnu-toolchain.
- The implementation is verified using internal test suites and projects.

## Relationships

- [[gemmini]]: Gemmini is a RISC-V-based systolic array generator that may utilize RISC-V vector intrinsics for host-accelerator communication.
- [[sifive-intelligence-x160-gen-2]]: A hardware target that implements RVV1.0 and thus can make use of the RISC-V vector intrinsics for vector operations.
- Insufficient context for additional cross-links; only one entity page (gemmini) is available in the current wiki.

## Sources

- [GCC RISC-V Vector Intrinsics documentation](https://gcc.gnu.org/onlinedocs/gcc-13.1.0/gcc/RISC-V-Vector-Intrinsics.html)
- [RISC-V vector intrinsic specification v0.11](https://github.com/riscv-non-isa/rvv-intrinsic-doc/tree/v0.11.x)
- [A Friendly Guide to RISC-V Vector Intrinsics in GCC](https://www.w3cubdocs.com) (W3cubDocs)
