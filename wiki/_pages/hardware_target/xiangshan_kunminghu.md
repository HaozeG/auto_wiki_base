---
canonical_name: XiangShan Kunminghu
aliases:
- Kunminghu
- BOSC Xiangshan Kunminghu
- xiangshan-kunminghu
- XiangShan third generation
- OpenXiangShan Kunminghu
subtype: null
tags:
- RISC-V
- XiangShan
- Kunminghu
- FPGA
- QEMU
hardware_targets:
- XiangShan Kunminghu
toolchains:
- QEMU
- OpenSBI
constraints:
- RV64GCBSUHV
- FPGA prototype platform supports up to 16 cores
- Core Local Interruptor (CLINT)
- Incoming MSI Controller (IMSIC)
- Advanced Platform-Level Interrupt Controller (APLIC)
- UART
- Boot via -bios combined binary
scorecard:
  novelty_delta: 0.9
  claim_density: 0.6
  self_containedness: 0.9
  bridge_score: 0.5
  hub_potential: 0.5
sources:
- raw/cache/14a47e22f1a4efba.md
- https://www.qemu.org/docs/master/system/riscv/xiangshan-kunminghu.html
source_url: https://www.qemu.org/docs/master/system/riscv/xiangshan-kunminghu.html
fetched_at: '2026-07-02T06:52:19.673915+00:00'
type: hardware_target
created: '2026-07-02'
updated: '2026-07-02'
cold_start: true
inbound_links: 0
---

# XiangShan Kunminghu

The XiangShan Kunminghu is the third-generation processor core from the open-source high-performance RISC-V processor project known as XiangShan, developed by the Beijing Open Source Chip (BOSC) community. The Kunminghu core implements the RV64GCBSUHV instruction set architecture, incorporating hypervisor (H) and vector (V) extensions. The QEMU system emulator provides a machine model, xiangshan-kunminghu, that emulates an FPGA prototype platform supporting up to 16 Kunminghu cores, along with devices such as a Core Local Interruptor (CLINT), Incoming MSI Controller (IMSIC), Advanced Platform-Level Interrupt Controller (APLIC), and a UART. The platform boots via a combined firmware, kernel, and device tree blob loaded through QEMU's -bios option, with OpenSBI as the typical supervisor binary interface. This emulation enables software development and testing for the XiangShan Kunminghu processor without requiring physical FPGA hardware.

## Key Claims

- XiangShan is an open-source high-performance RISC-V processor project.
- The third generation processor core is called Kunminghu, a 64-bit RV64GCBSUHV core.
- The QEMU xiangshan-kunminghu machine supports up to 16 Kunminghu cores.
- Supported devices include CLINT, IMSIC, APLIC, and a UART.
- The platform boots using QEMU's -bios functionality with a combined binary containing firmware, kernel, and FDT.
- Example usage: qemu-system-riscv64 -machine xiangshan-kunminghu -smp 16 -m 16G -bios path/to/fw_payload.bin -nographic.

## Optimization-Relevant Details

- ISA/profile: RV64GCBSUHV (base 64-bit with compression, bit manipulation, supervisor, hypervisor, vector extensions).
- Vector/matrix/accelerator support: Vector extension (V) is part of the ISA; no dedicated matrix accelerator mentioned in this source.
- Memory/cache/TLB/DMA: Not specified in the source; the emulated platform uses generic QEMU memory model.
- Compiler/toolchain support: QEMU system emulator, OpenSBI for boot firmware. The broader XiangShan project provides documentation and toolchain guidance at docs.xiangshan.cc.

## Relationships

- [[xuantie_c908]]: Another open-source RISC-V processor core with a different design philosophy and target market, also supported by QEMU and serving as a comparable RISC-V hardware target for AI acceleration workloads.
- [[k230]]: A system-on-chip integrating a different RISC-V core (XuanTie C908) with dedicated AI accelerators; contrasts with the XiangShan Kunminghu's approach of a general-purpose high-performance core with FPGA prototyping.
- [[mlir_xdsl_rvv_gemm_codegen_recipe]]: An optimization recipe for generating RISC-V Vector code, potentially applicable to the Kunminghu's vector extension for GEMM optimization.

## Sources

- https://www.qemu.org/docs/master/system/riscv/xiangshan-kunminghu.html
