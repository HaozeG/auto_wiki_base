---
canonical_name: LLVM RISC-V FPTrunc Narrowing Optimization
aliases:
- FPTrunc narrowing fix
- getMinimumFPType range analysis
- RISC-V fdiv regression fix
subtype: null
tags: []
hardware_targets:
- SiFive P550
workloads: []
datatypes:
- float32
- float64
metrics:
- latency
toolchains:
- LLVM
- GCC
constraints: []
evidence_strength: measured
scorecard:
  novelty_delta: 0.9
  claim_density: 0.7
  self_containedness: 0.9
  bridge_score: 0.5
  hub_potential: 0.2
sources:
- raw/cache/e8cf3d77b95c3ea9.md
- https://blog.kaving.me/blog/tracking-down-a-25-regression-on-llvm-risc-v/
source_url: https://blog.kaving.me/blog/tracking-down-a-25-regression-on-llvm-risc-v/
fetched_at: '2026-07-02T10:23:29.659765+00:00'
type: optimization_recipe
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# LLVM RISC-V FPTrunc Narrowing Optimization

The LLVM RISC-V FPTrunc narrowing optimization is a compiler transformation that uses range analysis in the `getMinimumFPType` function to recognize that a chain `fptrunc(uitofp x double) to float` can be reduced to `uitofp x to float`, thereby avoiding a costly double-precision floating-point division on RISC-V targets. The optimization restores a narrowing pass that was inadvertently broken by a prior LLVM commit which folded `fpext(sitofp x to float) to double` into a direct `uitofp x to double` cast. On the SiFive P550 CPU, this replacement replaces a 33-cycle `fdiv.d` instruction with a 19-cycle `fdiv.s` instruction, eliminating a ~24% performance regression observed in LLVM compared to GCC on a RISC-V benchmark from Igalia's performance comparison site. The fix was authored by Kavin Gnanapandithan and committed in April 2026.

## Key Claims

- A recent LLVM commit that improved `isKnownExactCastIntToFP` caused a ~24% performance regression on RISC-V targets (SiFive P550) by breaking a downstream narrowing optimization in `visitFPTrunc`.
- The regression was identified by comparing LLVM and GCC assembly and confirmed via `llvm-mca` analysis and prior build comparisons.
- The fix extends `getMinimumFPType` with range analysis to reduce `fptrunc(uitofp x double) to float` to `uitofp x to float`.
- The fix restores the narrowing optimization, replacing `fdiv.d` (33 cycle latency) with `fdiv.s` (19 cycle latency) on the SiFive P550.
- The expected effect is a ~24% performance improvement on the affected benchmark, closing the gap to GCC.

## Transformation

- **Prerequisites**: LLVM source tree with the regression-inducing commit (improves `isKnownExactCastIntToFP`). The commit that broke the narrowing is from early April 2026. Target CPU: SiFive P550 or other RISC-V cores where `fdiv.d` has significantly higher latency than `fdiv.s`.
- **Steps**: Modify `getMinimumFPType` in the LLVM target-independent code to incorporate range analysis logic that detects when a `uitofp` conversion to `double` followed by `fptrunc` to `float` can be performed entirely in single precision. The patch extends the existing logic to handle the specific pattern `fptrunc(uitofp x double) to float`.
- **Expected effect**: On the affected benchmark, the double-precision division in the hot loop is replaced by a single-precision division, reducing latency per division from 33 to 19 cycles on SiFive P550, yielding approximately 24% overall benchmark improvement. Other workloads with similar patterns may also benefit.
- **Failure modes**: No failure modes documented; the optimization is expected to be safe because it only applies when range analysis can prove the conversion does not lose precision. Overly aggressive range analysis could theoretically produce incorrect results, but the patch is reported as correct.
- **Measurements**: On SiFive P550, `fdiv.d` latency: 33 cycles, `fdiv.s` latency: 19 cycles. The regression was measured at ~24% by comparing LLVM builds before and after the regression commit using the Igalia benchmark (specific benchmark name not disclosed in the blog). Evidence strength: measured (via `llvm-mca` and real-world cycle comparison).

## Relationships

- [[gemmini]]: As a RISC-V AI accelerator, Gemmini may leverage similar floating-point divisions in its compute kernels; this optimization recipe could be relevant for improving LLVM code generation for Gemmini workloads.
- [[nncase]]: As a compiler stack for RISC-V AI accelerators, nncase could incorporate LLVM optimizations, including this FPTrunc narrowing, to improve inference performance on RISC-V hardware.
- Insufficient context for additional cross-links to entity pages; only two entity pages are available in the wiki.

## Sources

- [Tracking down a 25% Regression on LLVM RISC-V – KG's Blog](https://blog.kaving.me/blog/tracking-down-a-25-regression-on-llvm-risc-v/)
