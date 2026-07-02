---
canonical_name: Whisper
aliases:
- Tenstorrent Whisper
- SweRV-ISS
subtype: null
tags: []
scorecard:
  novelty_delta: 0.9
  claim_density: 0.6
  self_containedness: 0.8
  bridge_score: 0.7
  hub_potential: 0.4
sources:
- raw/cache/91e2f9c71426e086.md
- https://github.com/tenstorrent/whisper
source_url: https://github.com/tenstorrent/whisper
fetched_at: '2026-07-02T13:05:40.667971+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# Whisper

Whisper is a RISC-V instruction set simulator (ISS) developed by Tenstorrent, originally created for the verification of the Swerv collection of micro-controllers. It enables users to run RISC-V binary code without physical RISC-V hardware, providing an interactive mode for single-stepping and inspecting or modifying registers and simulated system memory. Whisper can also operate in lock step with a Verilog simulator, serving as a golden model to check an implementation after each instruction of a test program. The simulator supports a variety of RISC-V extensions and configurations, and is released under the Apache-2.0 license. It requires a Linux host with the RISC-V toolchain, g++ 11 or higher, and Boost 1.75 or higher. Additional optional features include LZ4 compression support, a VNC-based graphical frame buffer, and code coverage analysis.

## Key Claims

- Whisper is a RISC-V ISS used for verification of SWERV microcontrollers, developed by Tenstorrent.
- It supports both interactive and lock-step modes for debugging and golden-model comparison with Verilog simulation.
- It can execute RISC-V binaries compiled with standard toolchains such as riscv64-unknown-elf-gcc, and handles both RV32 and RV64 targets.
- The simulator provides memory consistency checks, code coverage analysis, and optional graphical output via frame buffer.
- Build prerequisites include g++ 11 or higher, Boost 1.75 or higher, and optionally liblz4-dev and libvncserver-dev.
- Whisper supports a broad range of RISC-V extensions (detailed in the Supported Extensions list in the repository).
- It is open-source under the Apache-2.0 license and hosted on GitHub at tenstorrent/whisper.

## Relationships

- [[spacemit-x60-processor]]: As a RISC-V processor target, the SpacemiT X60 can be simulated and debugged using Whisper during hardware verification and software development.
- [[vectrans]]: Vectorization optimization frameworks such as VecTrans can be tested and validated on simulated RISC-V environments provided by Whisper, enabling compiler research without physical hardware.
- Insufficient context for additional cross-links to entity pages.

## Sources

- [GitHub - tenstorrent/whisper](https://github.com/tenstorrent/whisper)
