---
canonical_name: riscv-vector-tests
aliases:
- chipsalliance/riscv-vector-tests
- RISC-V Vector Tests Generator
- RVV unit test generator
subtype: null
tags:
- RISC-V
- RVV
- testing
- test generation
scorecard:
  novelty_delta: 0.8
  claim_density: 0.5
  self_containedness: 0.9
  bridge_score: 0.5
  hub_potential: 0.3
sources:
- raw/cache/fff2a4a89fcbb7b1.md
- https://github.com/chipsalliance/riscv-vector-tests
source_url: https://github.com/chipsalliance/riscv-vector-tests
fetched_at: '2026-07-02T04:22:39.560873+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# riscv-vector-tests

The RISC-V Vector Tests Generator (riscv-vector-tests) is a tool developed under the Chips Alliance that automatically generates unit tests for the RISC-V Vector Extension (RVV). It uses the Spike simulator as a golden reference by adding a custom special instruction to automatically produce reference results for each test, allowing almost automatic test generation across all RVV instructions. The tool supports both user-mode and machine-mode binaries, integrates TestFloat3 for floating-point testing, and is configurable via a simple config file per instruction. It covers SEW from e8 to e64, LMUL from mf8 to m8, and VLEN from 64 to 65536, and supports RV32 and RV64 as well as several sub-extensions including Zvfh, Zvbb, Zvbc, Zvkg, Zvkned, Zvknha, Zvksed, Zvksh, Zvfbfmin, and Zvfbfwma. While it generates per-instruction tests in a uniform fashion, it has known limitations such as lack of support for tail/mask agnostic modes, fault-only-first testing, vstart testing, and register group overlap testing. The project is distributed under the Apache License Version 2.0.

## Key Claims

- Provides a simple and easy-to-use test generation framework similar to riscv-tests.
- Self-verifying tests (reference results generated automatically by Spike), making it co-simulator friendly.
- Generates both user-mode and machine-mode binaries.
- Supports a wide range of vector configurations: SEW e8–e64, LMUL mf8–m8, VLEN 64–65536.
- Integrates TestFloat3 for robust floating-point verification.
- Supports RV32 and RV64 base ISA widths.
- Supports sub-extensions: Zvfh, Zvbb, Zvbc, Zvkg, Zvkned, Zvknha, Zvksed, Zvksh, Zvfbfmin, Zvfbfwma.
- Configurable options are available via `make help`.
- Limitations include no coverage statistics, lack of tail/mask agnostic testing, fault-only-first, vstart, and register overlap tests.

## Relationships

- The tool can generate tests for hardware targets implementing RVV, such as [[xuantie_c908]] and [[k230]].
- The testing approach relies on the Spike simulator, a RISC-V ISC simulator widely used in the ecosystem.
- The generated tests are relevant to any optimization or kernel development for RVV, including the [[xuantie_c908_fp16_gemm_kernel]].

## Sources

- https://github.com/chipsalliance/riscv-vector-tests
