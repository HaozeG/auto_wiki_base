---
canonical_name: Whisper
aliases:
- tenstorrent/whisper
- Whisper ISS
- SweRV-ISS (derived)
subtype: null
tags:
- RISC-V
- instruction set simulator
- ISS
- Tenstorrent
scorecard:
  novelty_delta: 0.9
  claim_density: 0.7
  self_containedness: 0.9
  bridge_score: 0.3
  hub_potential: 0.3
sources:
- raw/cache/91e2f9c71426e086.md
- https://github.com/tenstorrent/whisper
source_url: https://github.com/tenstorrent/whisper
fetched_at: '2026-07-03T17:16:25.201385+00:00'
type: entity
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 0
outbound_links:
- target: sophon-sg2044-hardware-target
  reason: Whisper can simulate the RISC-V ISA targeting the SG2044's XuanTie C920v2
    cores, enabling pre-silicon software development for that platform
- target: xuantie-c906-hardware-target
  reason: Both the XuanTie C906 and Whisper are RISC-V tools; Whisper simulates the
    RISC-V ISA that the C906 implements, allowing testing of C906-targeted code without
    hardware
- target: spacemit-x60-hardware-target
  reason: Whisper can simulate RISC-V code for the SpacemiT X60 core, supporting software
    development and testing for the K1 SoC platform
---

# Whisper

Whisper is a RISC-V instruction set simulator (ISS) developed by Tenstorrent for verifying RISC-V micro-controllers, initially designed for the SweRV collection of micro-controllers. It allows users to execute RISC-V code without physical hardware, offering an interactive mode for single-stepping through instructions and inspecting or modifying RISC-V registers and system memory. Whisper can also operate in lock-step with a Verilog simulator, serving as a golden model to verify implementations instruction-by-instruction during test program execution. The simulator requires a Linux host with the RISC-V toolchain, g++ 11 or higher, and Boost 1.75 or later. It supports multiple compilation options including soft-float support, PCI library, trace reader, sparse memory model, fast sloppy mode, LZ4 compression, and a remote frame buffer for graphical output. Whisper is configured via command-line options and can be used with gdb for debugging. It includes features for memory consistency checks, code coverage, and has Python bindings for scripting. The simulator runs standalone programs compiled to RISC-V binaries and handles program termination through a tohost mechanism. Whisper supports various RISC-V extensions and can be used with the RISCOF framework for running riscv-arch-test compliance suite.

## Key Claims

- Whisper is a RISC-V ISS initially developed for SweRV micro-controllers.
- It supports interactive single-stepping and register/memory inspection.
- It can run in lock-step with a Verilog simulator as a golden model for instruction-by-instruction verification.
- It requires g++ 11 or higher and Boost 1.75 or later.
- Compilation options include SOFT_FLOAT, PCI, TRACE_READER, MEM_CALLBACKS, FAST_SLOPPY, LZ4_COMPRESS, and REMOTE_FRAME_BUFFER.
- It uses a tohost mechanism for program termination.
- It includes memory consistency checks, code coverage support, and Python bindings.
- It can be integrated with gdb for debugging.
- It supports execution of RISC-V arch-test via RISCOF.

## Relationships

- [[sophon-sg2044-hardware-target]]: Whisper can simulate the RISC-V ISA targeting the SG2044's XuanTie C920v2 cores, enabling pre-silicon software development for that platform.
- [[xuantie-c906-hardware-target]]: Both the XuanTie C906 and Whisper are RISC-V tools; Whisper simulates the RISC-V ISA that the C906 implements, allowing testing of C906-targeted code without hardware.
- [[spacemit-x60-hardware-target]]: Whisper can simulate RISC-V code for the SpacemiT X60 core, supporting software development and testing for the K1 SoC platform.

## Sources

- https://github.com/tenstorrent/whisper
