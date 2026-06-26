# Wiki Index

Last updated: 2026-06-26 | Pages: 16 | Sources: 9

## Entity Pages

| Page | Summary | Tags | Sources | Inbound |
|------|---------|------|---------|---------|
| [tt_metal.md](entity/tt_metal.md) | TT-Metal | tenstorrent, ai-hardware, software-stack, tt-nn, tt-metalium | 1 | 0 |
| [tensix_architecture.md](entity/tensix_architecture.md) | Tensix Architecture | tensix, tenstorrent, matrix-multiplication, architecture | 1 | 0 |
| [tenstorrent_ai_accelerators.md](entity/tenstorrent_ai_accelerators.md) | Tenstorrent AI Accelerators | risc-v, ai-accelerator, open-source, tensix, tenstorrent | 5 | 0 |
| [tensix_architecture.md](entity/tensix_architecture.md) | Tensix Architecture | tensix, tenstorrent, risc-v, ai-acceleration, tensegrity-robotics, hardware-co-design | 2 | 0 |
| [risc_v_vme.md](entity/risc_v_vme.md) | RISC-V Vector Matrix Extension (VME) | risc-v, matrix-extension, specification | 1 | 0 |
| [riscv_matrix_extensions_proposal.md](entity/riscv_matrix_extensions_proposal.md) | RISC-V Matrix Extensions Proposal | risc-v, matrix-extension, isa, proposal | 3 | 0 |
| [riscv_matrix_extensions.md](entity/riscv_matrix_extensions.md) | RISC-V Matrix Extensions (IME, VME, AME) | risc-v, isa-extension, matrix, ai-acceleration | 1 | 0 |
| [risc_v_matrix_extensions.md](entity/risc_v_matrix_extensions.md) | RISC-V Matrix Extensions | risc-v, matrix-extension, isa-extension | 1 | 0 |
| [risc_v_vector_extension.md](entity/risc_v_vector_extension.md) | Scalable SIMD ISA extension for RISC-V enabling AI/ML vector compute | risc-v, isa, vector-processing, ai-acceleration | 4 | 7 |
| [tenstorrent_blackhole.md](entity/tenstorrent_blackhole.md) | 120 Tensix-core RISC-V AI accelerator with 768 RISC-V cores, 32 GB GDDR6, $1,399 | ai-accelerator, risc-v, tensix, open-source-hardware | 1 | 3 |
| [sifive_intelligence_x280.md](entity/sifive_intelligence_x280.md) | Licensable 512-bit RISC-V vector processor IP for AI/ML SoC integration | risc-v, ai-accelerator, sifive, vector-processor, ip-core | 2 | 5 |
| [rva23_profile.md](entity/rva23_profile.md) | RISC-V profile mandating RVV 1.0; convergence point for NVIDIA, Canonical, Red Hat | risc-v, isa-profile, standardization, ai-acceleration | 2 | 3 |
| [fpga_riscv_isa_extension_nn_inference.md](entity/fpga_riscv_isa_extension_nn_inference.md) | FPGA-hosted RISC-V custom ISA extensions for edge neural network inference | risc-v, fpga, isa-extension, neural-network, edge-inference | 2 | 7 |
| [gemmini.md](entity/gemmini.md) | Open-source RISC-V RoCC systolic array DNN accelerator generator (Berkeley) | risc-v, gemmini, systolic-array, rocc, deep-learning, accelerator | 2 | 0 |
| [intel_itanium.md](entity/intel_itanium.md) | VLIW/EPIC architecture (2001–2021): predication, speculative loads, register rotation | itanium, epic, vliw, architecture | 1 | 1 |
| [tenstorrent.md](entity/tenstorrent.md) | Tenstorrent company: Tensix+RISC-V AI chips, Jim Keller, Qualcomm acquisition talks | risc-v, ai-chip, tenstorrent, qualcomm, acquisition | 1 | 2 |
| [tenstorrent_automotive_ai_accelerator.md](entity/tenstorrent_automotive_ai_accelerator.md) | Tenstorrent automotive-grade RISC-V AI accelerator chiplet (Eagle-N) | risc-v, automotive, ai-accelerator, chiplet, tenstorrent, tensix | 1 | 1 |

## Synthesis Pages

| Page | Connected Entities | Status | Inbound |
|------|--------------------|--------|---------|
| [riscv_ai_accelerator_landscape.md](synthesis/riscv_ai_accelerator_landscape.md) | risc_v_vector_extension, tenstorrent_blackhole, sifive_intelligence_x280, rva23_profile, fpga_riscv_isa_extension_nn_inference, gemmini | draft | 0 |
| [epic_vliw_ai_accelerator_legacy.md](synthesis/epic_vliw_ai_accelerator_legacy.md) | intel_itanium, risc_v_vector_extension | active | 1 |

## Concept Index

- **RVV (RISC-V Vector Extension)**: → [risc_v_vector_extension](entity/risc_v_vector_extension.md)
- **RVA23 Profile**: → [rva23_profile](entity/rva23_profile.md)
- **SiFive Intelligence X280**: → [sifive_intelligence_x280](entity/sifive_intelligence_x280.md)
- **Tenstorrent Blackhole**: → [tenstorrent_blackhole](entity/tenstorrent_blackhole.md)
- **Tenstorrent (company)**: → [tenstorrent](entity/tenstorrent.md)
- **Gemmini**: → [gemmini](entity/gemmini.md)
- **Intel Itanium / VLIW-EPIC**: → [intel_itanium](entity/intel_itanium.md)
- **Tenstorrent Automotive AI Accelerator**: → [tenstorrent_automotive_ai_accelerator](entity/tenstorrent_automotive_ai_accelerator.md)
- **FPGA RISC-V ISA Extension**: → [fpga_riscv_isa_extension_nn_inference](entity/fpga_riscv_isa_extension_nn_inference.md)
- **Tensix Architecture**: mentioned in [tenstorrent_blackhole](entity/tenstorrent_blackhole.md), [tenstorrent](entity/tenstorrent.md), [riscv_ai_accelerator_landscape](synthesis/riscv_ai_accelerator_landscape.md) — *no dedicated page*
- **Metalium Software Stack**: mentioned in [tenstorrent_blackhole](entity/tenstorrent_blackhole.md) — *no dedicated page*
- **RISC-V Matrix Extensions (IME, VME, AME)**: mentioned in [risc_v_vector_extension](entity/risc_v_vector_extension.md), [rva23_profile](entity/rva23_profile.md), [riscv_ai_accelerator_landscape](synthesis/riscv_ai_accelerator_landscape.md) — *no dedicated page*
- **VCIX (Vector Coprocessor Interface Extension)**: mentioned in [sifive_intelligence_x280](entity/sifive_intelligence_x280.md) — *no dedicated page*
- **EPIC/VLIW AI Legacy**: → [epic_vliw_ai_accelerator_legacy](synthesis/epic_vliw_ai_accelerator_legacy.md)
- **Google TPU**: mentioned in [intel_itanium](entity/intel_itanium.md), [epic_vliw_ai_accelerator_legacy](synthesis/epic_vliw_ai_accelerator_legacy.md) — *no dedicated page*
- **Qualcomm**: mentioned in [tenstorrent](entity/tenstorrent.md) — *no dedicated page*
- **Arrow Accelerator**: mentioned in [fpga_riscv_isa_extension_nn_inference](entity/fpga_riscv_isa_extension_nn_inference.md) — *no dedicated page*
