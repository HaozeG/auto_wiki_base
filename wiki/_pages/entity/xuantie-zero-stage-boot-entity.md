---
canonical_name: XuanTie Zero Stage Boot
aliases:
- ZSB
- zero_stage_boot
- Xuantie zero stage boot
- zsb
subtype: null
tags:
- XuanTie
- boot firmware
- RISC-V
scorecard:
  novelty_delta: 0.7
  claim_density: 0.6
  self_containedness: 0.9
  bridge_score: 0.6
  hub_potential: 0.4
sources:
- raw/cache/88ba69c5166b3c47.md
- https://github.com/XUANTIE-RV/zero_stage_boot
source_url: https://github.com/XUANTIE-RV/zero_stage_boot
fetched_at: '2026-07-03T15:25:07.818579+00:00'
type: entity
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 0
outbound_links:
- target: xuantie-c906-hardware-target
  reason: zero_stage_boot initializes the custom XuanTie CSRs that the C906 core defines,
    enabling its custom instruction extensions and memory model attributes used during
    Linux boot
- target: gcc-tuning-c908-canmv-k230
  reason: The GCC tuning for C908 assumes that the core's CSRs are correctly initialized
    by boot firmware such as zero_stage_boot; the boot flags in ZSB that enable custom
    extensions are prerequisites for the ISA features the tuning targets
---

# XuanTie Zero Stage Boot

XuanTie Zero Stage Boot (ZSB) is the initial processor initialization firmware for XuanTie RISC-V SoCs, executing before OpenSBI. It is responsible for relocating the Global Offset Table (GOT) and offset variables, initializing Control and Status Registers (CSRs) per CPUID for each hart, and enabling support for heterogeneous multi-core configurations such as combining C908 and C910 cores. The firmware handles ABI variants including 64lp64, 32ilp32, and 64ilp32. ZSB is designed to be compiled with a standard RISC-V GCC toolchain and is distributed as pre-compiled binaries for FPGA bringup. The boot flow follows the sequence: JTAG/gdbinit → zero_stage_boot → OpenSBI → Linux. The repository provides DTS device tree examples for OpenSBI generic firmware with "thead,c900-clint" and "thead,c900-plic" compatible strings, as well as a GDB initialization script for loading the boot stages into memory and setting CPU functional flags. The firmware supports enabling custom T-Head extensions such as RV64XT32, COPINSTEE, and XTINSTEE via boot flags.

## Key Claims

- Zero stage boot is the XuanTie processor init code that runs before OpenSBI.
- SoC vendors must prepare DDR init and CPU reset procedures prior to ZSB.
- All harts enter ZSB together; the first hart relocates GOT and offset variables, while others wait.
- Each hart initializes its CSRs based on its CPUID version, enabling heterogeneous core configurations (e.g., 4×C908 + 2×C910).
- Standard OpenSBI and Linux kernel binaries compiled from open-source repositories are fully compatible with XuanTie processors.
- Pre-compiled ZSB, OpenSBI, and Linux binaries are provided under the Releases tab for FPGA bringup, with version tracking and testing.
- ABI variants supported: 64lp64 (lp64 ABI on 64-bit hardware), 32ilp32 (ilp32 on 32-bit), 64ilp32 (ilp32 on 64-bit).
- DTS examples are provided for OpenSBI generic firmware using "thead,c900-clint" and "thead,c900-plic" compatible strings.
- A GDB initialization script loads binaries into memory, sets boot flags for custom extensions (RV64XT32, COPINSTEE, XTINSTEE), and releases harts from reset.
- The firmware is compiled with a standard RISC-V GCC compiler using `CROSS_COMPILE=riscv64-unknown-linux-gnu- make`.

## Relationships

- [[xuantie-c906-hardware-target]]: zero_stage_boot initializes the custom XuanTie CSRs that the C906 core defines, enabling its custom instruction extensions and memory model attributes used during Linux boot.
- [[gcc-tuning-c908-canmv-k230]]: The GCC tuning for C908 assumes that the core's CSRs are correctly initialized by boot firmware such as zero_stage_boot; the boot flags in ZSB that enable custom extensions are prerequisites for the ISA features the tuning targets.

## Sources

- https://github.com/XUANTIE-RV/zero_stage_boot
