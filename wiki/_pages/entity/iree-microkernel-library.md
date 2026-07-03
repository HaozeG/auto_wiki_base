---
canonical_name: IREE Microkernel Library
aliases:
- IREE ukernel library
- IREE microkernels
- ukernel
subtype: null
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.7
  self_containedness: 1.0
  bridge_score: 0.5
  hub_potential: 0.6
sources:
- raw/cache/6412b2ea6af4dd07.md
- https://github.com/iree-org/iree/tree/main/runtime/src/iree/builtins/ukernel
source_url: https://github.com/iree-org/iree/tree/main/runtime/src/iree/builtins/ukernel
fetched_at: '2026-07-03T15:27:45.106083+00:00'
type: entity
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 0
outbound_links:
- target: iree-riscv-microkernel-support
  reason: This optimization recipe uses the IREE mmt4d microkernels for RISC-V LLM
    inference, demonstrating one application of the ukernel library on a specific
    hardware target with RVV 1.0 support
---

# IREE Microkernel Library

The IREE Microkernel Library (ukernel library) is a self-contained C library of small, specialized functions that can be used as lowering targets for MLIR arithmetic operations within the IREE compiler framework. Ukernels perform arithmetic and memory access via pointer and stride arguments, but cannot use any library (including the C standard library), allocate memory, interface with the operating system, have side effects beyond writing to destination buffers, maintain state, or be non-reentrant. They are compiled once per target architecture, not per platform, and are typically embedded as LLVM bitcode in the IREE compiler or built as a native library for the VMVX back-end. The library includes operations such as mmt4d (matrix multiply with transpose), pack, unpack, and query tile sizes, and is accompanied by unit tests and microbenchmarks in the tools/ subdirectory.

## Key Claims

- Ukernels can perform arithmetic and memory access but cannot use any library (including the C standard library), allocate memory, interface with the operating system, have side effects beyond writing to destination buffers, maintain state, or be non-reentrant.
- Ukernels are compiled once per target architecture, not per platform.
- Ukernels are typically compiled to LLVM bitcode embedded in the IREE compiler, or built as a native library for the VMVX back-end.
- The ukernel library includes operations for mmt4d, pack, unpack, and query_tile_sizes.
- The tools/ directory contains unit tests and microbenchmarks for ukernel development.
- External ukernel bitcode files can be passed to the IREE compiler.

## Relationships

- [[iree-riscv-microkernel-support]]: This optimization recipe uses the IREE mmt4d microkernels for RISC-V LLM inference, demonstrating one application of the ukernel library on a specific hardware target with RVV 1.0 support.

## Sources

- https://github.com/iree-org/iree/tree/main/runtime/src/iree/builtins/ukernel
