---
cold_start: false
created: '2025-10-13'
inbound_links: 0
needs_summary_revision: false
scorecard:
  bridge_score: 0.5
  claim_density: 0.8
  hub_potential: 0.6
  novelty_delta: 0.9
  self_containedness: 0.9
sources:
- README.md
- .github/workflows/CI.yml
- tools/build/make-example
- tools/build/build
- tools/build/make
- examples/ai/classification/Makefile
tags:
- gap8
- risc-v
- build-system
- toolchain
- docker
- ai-deck
- bitcraze
- greenwaves
type: entity
updated: '2026-06-28'
---

# Building GAP8 Applications

The GAP8 Application Build System is the toolchain and infrastructure used to compile, link, and produce deployable firmware images for the GAP8 processor within the Bitcraze AI-Deck ecosystem. Housed in the `bitcraze/aideck-gap8-examples` repository, this build system relies on Docker containers to provide a reproducible environment containing the `gap_sdk` version 4.22.0, the GCC RISC-V toolchain, and the PMSIS framework. The build process is orchestrated through shell scripts such as `make-example` and `build`, which configure the environment, resolve dependencies, and invoke Makefiles that define memory budgets, compiler flags, and autotiler settings. The system supports both a base Docker image and an extended image with autotiler for neural network kernel generation from TensorFlow Lite models, with DORY available as an alternative when the autotiler website is unreachable.

## Key Claims

- The build environment uses two Docker images: `bitcraze/aideck` (includes `gap_sdk` 4.22.0+, GCC RISC-V toolchain, PMSIS framework) and `bitcraze/aideck-with-autotiler` (adds autotiler for neural network kernel generation from TensorFlow Lite models).
- The `make-example` script configures the JTAG cable setting `GAPY_OPENOCD_CABLE` and installs Python dependency numpy 1.22.3 before invoking make.
- Makefiles define memory budgets: `MODEL_L1_MEMORY` (cluster L1, e.g., 60000 - stack_size), `MODEL_L2_MEMORY` (shared L2, e.g., 270000), `MODEL_L3_MEMORY` (external memory, e.g., 8000000), as well as frequencies `FREQ_FC` (fabric controller, 200 MHz) and `FREQ_CL` (cluster, 170 MHz).
- Compiler flags include `-g` for debug symbols and `-Os` for size optimization.
- DORY is documented as an alternative deployment method when the GreenWaves Technologies autotiler website is unavailable.
- The autotiler populates the `MODEL_GEN_C` variable with generated kernel implementations.

## Relationships

- [[risc_v_vector_extension]] — The GAP8 processor implements custom vector/SIMD extensions that complement the RVV ecosystem; this build system compiles code targeting those extensions.
- [[tvm_riscv_backend]] — Apache TVM can compile neural network models for RISC-V targets; the GAP8 build system integrates autotiler to generate optimized kernels from TensorFlow Lite models, a workflow parallel to TVM's RISC-V compilation pipeline.
- [[gemmini]] — While Gemmini is a systolic array accelerator for RISC-V, the GAP8 build system demonstrates an alternative edge-AI deployment approach using a full SDK toolchain.

## Sources

- README.md of bitcraze/aideck-gap8-examples (lines 1-8)
- .github/workflows/CI.yml (lines 28-37)
- tools/build/make-example (lines 1-15)
- tools/build/build (lines 1-6)
- tools/build/make (lines 1-8)
- examples/ai/classification/Makefile (lines 10-62)
