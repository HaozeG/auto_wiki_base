---
canonical_name: HIP/C++ Kernel Programming for AMD CDNA3/CDNA4
aliases:
- HIP C++ kernel programming
- CDNA3 HIP programming
- CDNA4 HIP programming
- GEAK HIP overview
- AMD HIP kernel programming
- HIP for Instinct
subtype: null
tags:
- CDNA3
- CDNA4
- HIP
- ROCm
- kernel programming
scorecard:
  novelty_delta: 0.8
  claim_density: 0.9
  self_containedness: 1.0
  bridge_score: 0.8
  hub_potential: 0.5
sources:
- raw/cache/3338e9312ea01c1e.md
- https://github.com/AMD-AGI/GEAK/blob/main/perf_knowledge/languages/hip_cpp/overview.md
source_url: https://github.com/AMD-AGI/GEAK/blob/main/perf_knowledge/languages/hip_cpp/overview.md
fetched_at: '2026-07-17T10:52:53.235486+00:00'
type: entity
created: '2026-07-17'
updated: '2026-07-17'
cold_start: true
inbound_links: 0
outbound_links:
- target: amd_gpu_architecture
  reason: This page provides the detailed hardware organization (command processor,
    ACEs, SEs, CUs, wavefront sizes) that HIP/C++ programs directly target. The HIP
    kernel programming model leverages the hierarchical parallel design and wave64
    execution model described in the AMD GPU Architecture page, and the hardware constants
    (CU count, LDS size, VGPR budgets) from this programming guide supplement that
    architectural overview
- target: amd_matrix_cores
  reason: HIP/C++ is the primary programming interface for the Matrix Core MFMA instructions
    within CDNA architectures. The language provides built-in intrinsics for controlling
    data layout, accumulator register selection, and matrix operation precision, enabling
    users to optimize GEMM kernels beyond what higher-level libraries offer
---

# HIP/C++ Kernel Programming for AMD CDNA3/CDNA4

HIP/C++ kernel programming is the lowest-level portable authoring interface for AMD CDNA3 and CDNA4 GPU architectures, providing full control over local data share (LDS), registers, wave and cross-lane operations, MFMA matrix-core intrinsics, and instruction scheduling via the hipcc/amdclang++ compiler toolchain. The CDNA wavefront model uses 64 lanes per wave (not 32 as in CUDA), requiring thread-block sizes that are multiples of 64. On MI300X (CDNA3), each compute unit has 64 KB of LDS with 32 banks of 4 bytes delivering 128 bytes per clock, 512 VGPRs per SIMD lane-slot, and approximately 102 usable SGPRs per wave. CDNA4 (MI350X) increases LDS to 160 KB per CU with 256 bytes per clock bandwidth and introduces OCP FP8 and MXFP block-scaled matrix multiply-accumulate instructions while removing TF32 support. HIP/C++ is used when higher-level abstractions like Triton or Composable Kernel cannot express a required fusion, or to generate and inspect exact AMDGCN instruction streams.

## Key Claims

- The AMD CDNA programming model uses a wavefront size of 64 lanes (`warpSize == 64`), requiring thread-block dimensions to be multiples of 64 (e.g., 64, 128, 256).
- LDS capacity per compute unit is 64 KB on CDNA3 (MI300X) and 160 KB on CDNA4 (MI350X).
- MI300X (gfx942) contains 304 Compute Units across 8 XCDs (38 CUs per XCD), with 4 SIMDs per CU.
- VGPR resources are 512 registers per SIMD lane-slot with a granularity of 16; SGPRs are approximately 102 usable per wave; AGPRs (MFMA accumulator registers) share the VGPR budget on CDNA3.
- HIP provides built-in intrinsics for explicit LDS layout and padding, direct-to-LDS async copy (`global_load_lds`), hand-built instruction scheduling via `sched_group_barrier`, and 64-bit wave masks—capabilities not available in higher-level frameworks.
- Toolchain flags: `--offload-arch=gfx942/gfx950` targets specific CDNA3/4 architectures; `-munsafe-fp-atomics` enables hardware FP32 atomics for reductions; `-Rpass-analysis=kernel-resource-usage` prints VGPR/SGPR/LDS usage per kernel.
- The `__launch_bounds__(maxTPB, minWavesPerEU)` attribute caps register usage: `minWavesPerEU=2` forces VGPR ≤ 256; `=4` forces VGPR ≤ 128. Excessively aggressive bounds cause scratch spills to HBM, degrading performance 3–5×.
- CDNA4 removes the TF32 datatype and adds OCP FP8 (E4M3FN, E5M2) and MXFP block-scaled formats for matrix multiplication.
- The HIP programming model includes a command processor with CPF/CPC, asynchronous compute engines (ACEs) that dispatch kernels to workgroup managers (SPI), and a hierarchical organization of shader engines, shader arrays, and compute units.
- Grid dimensions should be ≥ 1024 workgroups to keep all 304 CUs occupied across 8 XCDs.

## Relationships

- [[amd_gpu_architecture]]: This page provides the detailed hardware organization (command processor, ACEs, SEs, CUs, wavefront sizes) that HIP/C++ programs directly target. The HIP kernel programming model leverages the hierarchical parallel design and wave64 execution model described in the AMD GPU Architecture page, and the hardware constants (CU count, LDS size, VGPR budgets) from this programming guide supplement that architectural overview.
- [[amd_matrix_cores]]: HIP/C++ is the primary programming interface for the Matrix Core MFMA instructions within CDNA architectures. The language provides built-in intrinsics for controlling data layout, accumulator register selection, and matrix operation precision, enabling users to optimize GEMM kernels beyond what higher-level libraries offer.

## Sources

- [GEAK/perf_knowledge/languages/hip_cpp/overview.md at main ...](raw/cache/3338e9312ea01c1e.md)
