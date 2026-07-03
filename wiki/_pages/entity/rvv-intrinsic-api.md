---
canonical_name: RISC-V Vector Extension Intrinsic API
aliases:
- RVV Intrinsic API
- rvv-intrinsic-api
- RISC-V Vector Intrinsic API
subtype: null
tags: []
scorecard:
  novelty_delta: 0.8
  claim_density: 0.5
  self_containedness: 0.4
  bridge_score: 0.6
  hub_potential: 0.5
sources:
- raw/cache/d2679c74451e1bcb.md
- https://github.com/LSNUDT/rvv-intrinsic-doc/blob/master/rvv-intrinsic-api.md
source_url: https://github.com/LSNUDT/rvv-intrinsic-doc/blob/master/rvv-intrinsic-api.md
fetched_at: '2026-07-03T13:31:37.551787+00:00'
type: entity
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 0
outbound_links:
- target: c908-wino-gemm-optimization
  reason: The RVV intrinsic API documented here targets the 0.9-draft specification,
    which is the direct predecessor to the RVV 1.0 specification implemented by the
    XuanTie C908 core used in the Winograd and GEMM optimization page. The C908's
    SHL library uses RVV 1.0 intrinsics that evolved from this API
---

# RISC-V Vector Extension Intrinsic API

The RISC-V Vector Extension (RVV) Intrinsic API provides a C programming language interface for the RISC-V Vector extension, enabling developers to write portable vector code using built-in functions that map directly to RVV instructions. This reference manual, hosted on GitHub by LSNUDT, targets the RVV 0.9-draft specification from February 2020 and documents the intrinsic programming model, including naming conventions, function prototypes for configuration-setting operations, vector loads and stores, vector AMO operations, and vector integer arithmetic operations. Known issues covered include the compiler-time knowledge requirement for ELEN, and the handling of XLEN versus SEW mismatches in slide and splat operations. The manual serves as a companion to an external RFC document that defines the detailed naming rules and design philosophy.

## Key Claims

- The API targets RVV 0.9-draft (20200221) and documents the intrinsic programming model.
- ELEN must be known at compile time; widening instructions depend on ELEN and become unsupported when ELEN is too small.
- When XLEN < SEW, scalar values are sign-extended; for unsigned scalars this causes semantics issues in operations like vmv.s.x and vslide1up.
- The API defines configuration-setting functions (vsetvli, vsetvl), vector load/store operations (unit-stride, strided, indexed, fault-only-first, segment), vector AMO operations, reinterpret cast conversions, and URW vector CSR read/write functions.
- Vector AMO operations require SEW ≤ XLEN; otherwise an illegal instruction exception is raised.
- Segment load/store operations (Zvlsseg) and segment AMO operations are only partially documented (marked TODO).

## Relationships

- [[c908-wino-gemm-optimization]]: The RVV intrinsic API documented here targets the 0.9-draft specification, which is the direct predecessor to the RVV 1.0 specification implemented by the XuanTie C908 core used in the Winograd and GEMM optimization page. The C908's SHL library uses RVV 1.0 intrinsics that evolved from this API.

## Sources

- https://github.com/LSNUDT/rvv-intrinsic-doc/blob/master/rvv-intrinsic-api.md
