---
canonical_name: TT-XLA Performance Optimization Techniques
aliases:
- TT-XLA optimization guide
- Forge performance optimization
subtype: null
hardware_targets:
- Tenstorrent AI accelerator (single-chip)
workloads:
- generic PyTorch model
datatypes:
- bfloat16
- bfloat8_b
metrics:
- throughput
- latency
- compilation time
- runtime performance
toolchains:
- TT-XLA
- Forge compiler
- PyTorch
- TT-MLIR
constraints:
- single-chip Tenstorrent hardware
- PyTorch model
evidence_strength: reported
tags: []
scorecard:
  novelty_delta: 0.8
  claim_density: 0.9
  self_containedness: 1.0
  bridge_score: 0.5
  hub_potential: 0.6
sources:
- raw/cache/84d5d8713b70ee41.md
- https://docs.tenstorrent.com/tt-xla/performance.html
source_url: https://docs.tenstorrent.com/tt-xla/performance.html
fetched_at: '2026-07-09T11:09:38.829308+00:00'
type: optimization_recipe
created: '2026-07-09'
updated: '2026-07-09'
cold_start: true
inbound_links: 3
---

# TT-XLA Performance Optimization Techniques

This guide presents a collection of optimization techniques for PyTorch models compiled with the TT-XLA frontend of the Forge compiler, targeting single-chip Tenstorrent hardware. The transformations include adjusting compiler optimization levels (0, 1, 2), performing device warmup iterations, using lower-precision data formats (bfloat16 and bfloat8_b) along with per-tensor weight dtype overrides for manual mixed precision, enabling runtime trace to reduce host-device communication overhead, and tuning batch size. Prerequisites include a PyTorch model, a Tenstorrent single-chip system, and the TT-XLA toolchain. Expected effects are faster computation, reduced memory usage, and improved overall throughput. No systematic measurements are provided; the claims are based on documented best practices. Failure modes include accuracy loss when using reduced precision and out-of-memory (OOM) errors with large batch sizes.

## Key Claims

- Optimization level 0 disables all MLIR optimizer passes and places all tensors in DRAM, providing fastest compilation but slowest runtime performance.
- Optimization level 1 enables basic optimizations including constant evaluation of Conv2D weights and fusion patterns, offering a good balance between compilation speed and runtime performance.
- Optimization level 2 enables advanced optimizations that maximize placement of tensors in SRAM instead of DRAM, achieving the best runtime performance at the cost of slower compilation.
- Device warmup of at least 3 dummy iterations eliminates first-run overhead from model compilation, kernel compilation, weight transfer, and caching.
- Using bfloat16 for model weights and inputs reduces memory usage by 50% compared to fp32 and provides faster computation with minimal accuracy loss for most workloads.
- Enabling bfloat8_b (bfp_bf8) weight conversion casts matmul weights to block float 8-bit format, further speeding computation and reducing memory, though accuracy loss may occur for some workloads.
- Per-tensor weight dtype overrides allow manual mixed precision: sensitive layers can remain at higher precision (e.g., bf16) while others use lower formats (bfp_bf8 or bfp_bf4), applied via the `apply_weight_dtype_overrides()` function.
- Runtime trace, enabled by setting `TT_RUNTIME_TRACE_REGION_SIZE` (recommended 10 MB) and enabling `"enable_trace": "true"`, records and replays command sequences to reduce host-device communication overhead.
- Batch size tuning should start with values like 1, 2, 4, 8, 16, 32; throughput is measured for each, and the optimal batch size occurs when throughput plateaus, starts decreasing, or memory is exhausted.

## Transformation

### 1. Optimization Levels
- Prerequisites: TT-XLA environment.
- Steps: Set `torch_xla.set_custom_compile_options({"optimization_level": level})` with level 0, 1, or 2.
- Expected effect: Level 2 yields best runtime performance; level 0 fastest compile.
- Failure modes: None specified.
- Measurements: Compilation time and runtime performance tradeoff.

### 2. Device Warmup
- Prerequisites: Model and input ready.
- Steps: Run at least 3 dummy inference iterations under `torch.no_grad()`.
- Expected effect: Eliminates one-time overhead of compilation, weight transfer, caching, and trace capture.
- Failure modes: None.

### 3. Data Formats
- Prerequisites: Model in torch.bfloat16 for bfloat16 usage; model in bfloat16 with experimental_weight_dtype="bfp_bf8" for bfloat8_b.
- Steps: Convert model with `model.to(torch.bfloat16)` for bfloat16; add compile option for bfloat8_b; optionally use `apply_weight_dtype_overrides()` for per-tensor overrides.
- Expected effect: Faster computation and reduced memory usage; minimal accuracy loss for most workloads with bfloat16; possible accuracy loss with bfloat8_b.
- Failure modes: Accuracy degradation in sensitive layers; not all layer types (e.g., convolution) support lower dtypes through the compiler.

### 4. Runtime Trace
- Prerequisites: Set environment variable `TT_RUNTIME_TRACE_REGION_SIZE` before importing torch_xla (recommended 10 MB).
- Steps: Enable trace in compile options with `"enable_trace": "true"`.
- Expected effect: Reduced host-device communication overhead by recording and replaying command sequences as a single command.
- Failure modes: Trace-related errors if region size is too small; increase size if errors occur.

### 5. Batch Size Tuning
- Prerequisites: Model, input, device.
- Steps: Try batch sizes 1, 2, 4, 8, 16, 32; measure throughput for each.
- Expected effect: Larger batches typically increase throughput but also per-sample latency; smaller batches may utilize SRAM more effectively and yield higher throughput in some cases.
- Failure modes: Out-of-memory (OOM) at large batch sizes.

## Relationships

- [[blackhole]] is a Tenstorrent single-chip AI accelerator; the optimization techniques in this guide apply directly to Blackhole as a target hardware, and users should follow these practices to improve performance on that chip.

## Sources

- https://docs.tenstorrent.com/tt-xla/performance.html
