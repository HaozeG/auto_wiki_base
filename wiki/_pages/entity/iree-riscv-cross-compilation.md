---
canonical_name: IREE
aliases:
- IREE RISC-V cross-compilation
- IREE (RISC-V)
subtype: null
tags: []
scorecard:
  novelty_delta: 0.5
  claim_density: 0.4
  self_containedness: 0.7
  bridge_score: 0.3
  hub_potential: 0.3
sources:
- raw/cache/9bb37ab9e9974aa7.md
- https://github.com/iree-org/iree/blob/main/docs/website/docs/building-from-source/riscv.md
source_url: https://github.com/iree-org/iree/blob/main/docs/website/docs/building-from-source/riscv.md
fetched_at: '2026-07-06T02:47:12.772057+00:00'
type: entity
created: '2026-07-06'
updated: '2026-07-06'
cold_start: true
inbound_links: 0
outbound_links:
- target: xuantie-c920v2-hardware-target
  reason: The IREE LLVM-CPU backend flags for RVV 1.0 match the vector extension implemented
    by the XuanTie C920V2 core, allowing IREE to generate vectorized code for that
    hardware target
---

# IREE

IREE (Intermediate Representation Execution Environment) is an MLIR-based compiler and runtime for deploying deep learning models on diverse hardware. This document describes the cross-compilation workflow for running IREE bytecode modules on RISC-V 64-bit Linux systems. The workflow involves building the IREE compiler on a host platform (e.g., Linux) and the IREE runtime for the target RISC-V architecture, then executing compiled modules using a RISC-V enabled QEMU emulator or natively on RISC-V hardware. The instructions cover toolchain prerequisites including LLVM/Clang and QEMU, CMake configuration for both host and target, and optional RISC-V Vector Extension (RVV) 1.0 support for SIMD acceleration. The vector extension configuration uses the LLVM-CPU backend with specific target-cpu-features flags for +v and +zvl512b.

## Key Claims

- IREE supports RISC-V cross-compilation via a host-to-target build process using a RISC-V LLVM/Clang toolchain and a RISC-V-enabled QEMU emulator.
- The prebuilt toolchain is available via the `riscv_bootstrap.sh` script, with default install path `~/riscv/toolchain/clang/linux/RISCV`.
- For RISC-V Vector Extension (RVV) 1.0 support, the LLVM-CPU backend must be configured with `--iree-hal-local-target-device-backends=llvm-cpu`, `--iree-llvmcpu-target-triple=riscv64`, `--iree-llvmcpu-target-abi=lp64d`, `--iree-llvmcpu-target-cpu-features="+m,+a,+f,+d,+zvl512b,+v"`, and `--riscv-v-fixed-length-vector-lmul-max=8`.
- Execution on QEMU requires `-cpu rv64,Zve64d=true,vlen=512,elen=64,vext_spec=v1.0` and the sysroot from the toolchain.

## Relationships

- [[xuantie-c920v2-hardware-target]]: The IREE LLVM-CPU backend flags for RVV 1.0 match the vector extension implemented by the XuanTie C920V2 core, allowing IREE to generate vectorized code for that hardware target.

## Sources

- https://github.com/iree-org/iree/blob/main/docs/website/docs/building-from-source/riscv.md
