---
canonical_name: AMD Matrix Cores
aliases:
- MFMA
- AMD CDNA Matrix Cores
- AMD Matrix Core
subtype: null
hardware_targets:
- AMD Instinct MI325X (CDNA3)
- AMD Instinct MI355X (CDNA4)
workloads:
- matrix multiplication (MFMA)
- AI/ML inference
- HPC linear algebra
datatypes:
- FP16
- BF16
- FP8
- FP6
- FP4
- FP32
metrics:
- TFLOPS
- speedup vs FP32
- throughput
toolchains:
- ROCm
- HIP
constraints:
- exponent bias
- data layout requirements
- special value encodings (NaN, Infinity)
evidence_strength: reported
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.9
  self_containedness: 0.6
  bridge_score: 0.5
  hub_potential: 0.3
sources:
- raw/cache/4ee94c993b5c3f39.md
- https://rocm.blogs.amd.com/software-tools-optimization/matrix-cores-cdna/README.html
source_url: https://rocm.blogs.amd.com/software-tools-optimization/matrix-cores-cdna/README.html
fetched_at: '2026-07-17T10:19:54.049853+00:00'
type: ai_accelerator_architecture
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 5
---

# AMD Matrix Cores

AMD Matrix Cores are dedicated hardware units within the AMD CDNA architecture that accelerate fused-multiply-add (MFMA) operations for matrix multiplication, a critical workload in AI and HPC applications. They are specialized for mixed-precision computation, using low-precision input datatypes such as FP16, FP8, FP6, and FP4 while maintaining full-precision output in FP32 to preserve accuracy. On the AMD Instinct MI325X (CDNA3), FP16 Matrix Cores deliver up to 1307.4 TFLOPS (~8x over FP32), and FP8 reaches 2614.9 TFLOPS (~16x over FP32). The CDNA4 architecture, featured in the MI355X, doubles FP16 and FP8 throughput and introduces FP6 and FP4 types, achieving up to 10 PFLOPS (32x–64x over FP32). This page describes the programming model, supported datatypes, and performance characteristics of Matrix Cores on CDNA3 and CDNA4.

## Key Claims

- On AMD Instinct MI325X (CDNA3): FP16 Matrix Core performance 1307.4 TFLOPS (~8× FP32); FP8 2614.9 TFLOPS (~16× FP32); FP64 163.4 TFLOPS (1×).
- On AMD Instinct MI355X (CDNA4): FP16/FP8 throughput is 2× higher than CDNA3; FP6 reaches ~10 PFLOPS (~32× FP32); FP4 reaches ~10 PFLOPS (~64× FP32).
- Supported low-precision types: FP16 (E5M10), BF16 (E8M7), FP8 (E4M3FN, E4M3FNUZ, E5M2, E5M2FNUZ), FP6 (E2M3, E3M2), FP4 (E2M1), plus E8M0 for exponent-only scaling.
- Matrix Cores are programmed via HIP intrinsic functions within the ROCm software stack.
- Each low-precision type defines specific exponent bias, range, and special value encodings (e.g., E4M3FN supports ±NaN but no infinities; E4M3FNUZ uses unsigned zero and single NaN).
- CDNA4 introduces matrix multiplication instructions with exponent block scaling, enabling efficient use of FP6 and FP4.

## Relationships

- The AMD Matrix Core is the matrix-multiply-accumulate (MFMA) hardware unit within the [[amd_cdna]] microarchitecture family. This page details the CDNA3 and CDNA4 implementations, building directly on the architectural foundations described in the CDNA page.

## Sources

- [Matrix Core Programming on AMD CDNA™3 and CDNA™4 ...](raw/cache/4ee94c993b5c3f39.md)
