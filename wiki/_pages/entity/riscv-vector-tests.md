---
canonical_name: riscv-vector-tests
aliases:
- RISC-V Vector Tests Generator
- RVV unit tests generator
- chipsalliance/riscv-vector-tests
subtype: null
tags:
- RVV
- testing
- verification
- Spike
- RISC-V
scorecard:
  novelty_delta: 0.8
  claim_density: 0.6
  self_containedness: 0.9
  bridge_score: 0.5
  hub_potential: 0.2
sources:
- raw/cache/fff2a4a89fcbb7b1.md
- https://github.com/chipsalliance/riscv-vector-tests
source_url: https://github.com/chipsalliance/riscv-vector-tests
fetched_at: '2026-07-02T11:17:38.203892+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 2
---

# riscv-vector-tests

riscv-vector-tests is an open-source unit test generator for the RISC-V Vector Extension (RVV) hosted by the Chips Alliance. It automatically generates per-instruction tests for all supported RVV instructions by using a custom-modified Spike simulator as a golden reference model: the simulator is instrumented with a special instruction that computes the expected result for any RVV instruction, allowing the generator to create self-verifying test binaries without manual golden reference writing. The generator supports RV32 and RV64 base ISAs, element widths from e8 to e64, vector length multipliers from mf8 to m8, and vector lengths from 64 to 65536. It also covers a range of ratified and draft sub-extensions including Zvfh, Zvbb, Zvbc, Zvkg, Zvkned, Zvknha, Zvksed, Zvksh, Zvfbfmin, and Zvfbfwma. The tool integrates TestFloat3 for floating-point verification and produces both user-mode and machine-mode binaries. Key limitations include the lack of tail and mask agnostic testing, fault-only-first coverage, vstart variation, and register group overlap tests; no coverage statistics or guarantees are provided.

## Key Claims

- Generates per-instruction unit tests for the RISC-V Vector Extension (RVV) using a modified Spike simulator as a golden reference.
- Supports RV32 and RV64, SEW from e8 to e64, LMUL from mf8 to m8, and VLEN from 64 to 65536.
- Covers sub-extensions: Zvfh, Zvbb, Zvbc, Zvkg, Zvkned, Zvknha, Zvksed, Zvksh, Zvfbfmin, Zvfbfwma.
- Integrates TestFloat3 for floating-point verification.
- Produces both user-mode and machine-mode binaries; supports co-simulation via a single stage-1 generator.
- Limitations: no tail/mask agnostic testing, no fault-only-first, no vstart testing, no register group overlap testing.
- Requires riscv64-unknown-elf-gcc with RVV 1.0 support, Spike simulator, Go 1.19+, and optionally riscv-pk.
- Licensed under Apache License Version 2.0.

## Relationships

- [[rvv-bench]]: related via shared rvv.

- [[opencv-hal-riscv-rvv]]: related via shared riscv, rvv.

- [[llvm-riscv-fptrunc-narrowing-optimization]]: As an optimization recipe that targets RISC-V hardware, this LLVM transformation may be tested or validated using the test suites produced by riscv-vector-tests on relevant platforms.
- [[spacemit-x60-processor]]: The SpacemiT X60 is a RISC-V processor that supports the RVA22 profile and AI acceleration; riscv-vector-tests could be used to verify RVV correctness on such hardware targets.
- Insufficient context for additional cross-links to entity pages; only two pages are available in the wiki context.

## Sources

- [GitHub repository: chipsalliance/riscv-vector-tests](https://github.com/chipsalliance/riscv-vector-tests)
