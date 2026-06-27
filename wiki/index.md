# Wiki Index

Last updated: 2026-06-27 | Pages: 19 | Sources: 36

## Entity Pages

| Page | Summary | Tags | Sources | Inbound |
|------|---------|------|---------|---------|
| [risc_v_vector_extension](entity/risc_v_vector_extension.md) | Standardized SIMD-style ISA extension enabling variable-width vector computation across RISC-V implementations | risc-v, hardware, AI-acceleration, vector-processing, ISA | 4 | 6 |
| [alibaba_xuantie_c950](entity/alibaba_xuantie_c950.md) | First RISC-V CPU architected for native LLM inference; 5nm, 3.2 GHz, 70+ SPECint2006, 8 TOPS/TPE | risc-v, AI-acceleration, processor, LLM-inference, alibaba | 4 | 2 |
| [alibaba_xuantie_c910_c920](entity/alibaba_xuantie_c910_c920.md) | Open-sourced out-of-order RISC-V cores adopting RVV 0.7.1 (C910) and RVV 1.0 (C920); predecessors to C950 | risc-v, processor, alibaba, out-of-order, open-source | 2 | 2 |
| [esperanto_et_soc1](entity/esperanto_et_soc1.md) | 1,092-core RISC-V AI inference chip on 7nm; 835.6 TOPS INT8 per 6-chip card at ~120W | risc-v, AI-accelerator, many-core, inference, hardware | 3 | 2 |
| [tenstorrent_tt_ascalon](entity/tenstorrent_tt_ascalon.md) | RVA23-compliant 8-wide OoO RISC-V CPU IP achieving 22+ SPECint2006/GHz on Samsung SF4X | risc-v, processor, AI-acceleration, out-of-order, server | 3 | 2 |
| [sifive_intelligence_x280](entity/sifive_intelligence_x280.md) | 512-bit VLEN in-order RISC-V core with VCIX custom extension interface; 12× inference speedup over base RISC-V | risc-v, processor, vector-processing, AI-acceleration, embedded | 3 | 2 |
| [ventana_veyron_v2](entity/ventana_veyron_v2.md) | 192-core, 4nm, 3.6 GHz RVA23-compliant server CPU with UCIe chiplet interface for AI accelerator attachment | risc-v, server, data-center, AI-acceleration, chiplet | 3 | 2 |
| [tvm_riscv_backend](entity/tvm_riscv_backend.md) | Apache TVM compiler backend for RISC-V RVV achieving 46% latency reduction vs GCC and 35% vs LLVM | compiler, optimization, risc-v, TVM, ML-frameworks, quantization | 4 | 4 |
| [gemmini](entity/gemmini.md) | Open-source parameterizable systolic array generator for DNN inference, attached to RISC-V via RoCC; 106.1 GOPS/W on Beagle SoC | risc-v, accelerator, systolic-array, open-source, uc-berkeley | 3 | 0 |
| [ara_vector_processor](entity/ara_vector_processor.md) | ETH Zurich open-source RVV 1.0 lane-scalable vector processor; 2–64 lanes, 41 DP-GFLOPS/W in 22 nm FD-SOI | risc-v, vector-processor, open-source, eth-zurich, rvv | 4 | 0 |
| [xiangshan_riscv](entity/xiangshan_riscv.md) | ICT-CAS open-source OoO RISC-V; 16.5 SPEC CPU2006 pts/GHz, Cortex-A76 class, Chisel/Mulan PSL | risc-v, open-source, high-performance, out-of-order, china | 4 | 0 |
| [boom_riscv](entity/boom_riscv.md) | UC Berkeley open-source OoO RISC-V (SonicBOOM); 6.2 CoreMarks/MHz, Chisel, Gemmini host CPU | risc-v, open-source, out-of-order, uc-berkeley, research | 4 | 0 |
| [andes_ax45mp_nx27v](entity/andes_ax45mp_nx27v.md) | Andes 64-bit superscalar AX45MP + NX27V RVV 1.0 VPU; BF16/Int4, AndesAIRE SDK, QiLai SoC | risc-v, commercial-ip, dsp, vector, ai-edge, andes-technology | 3 | 0 |
| [mlir_riscv_backend](entity/mlir_riscv_backend.md) | MLIR/LLVM lowering pipeline for RVV: Linalg → vector dialect → RVV intrinsics → machine code | mlir, risc-v, compiler, rvv, llvm, software-stack | 4 | 0 |
| [iree_riscv](entity/iree_riscv.md) | Google IREE ML compiler runtime on RISC-V; added RV64 microkernels in 2025 for GenAI workloads | risc-v, mlir, compiler-runtime, google, ml-deployment | 4 | 0 |
| [risc_v_p_extension](entity/risc_v_p_extension.md) | RISC-V packed SIMD/DSP extension for embedded MCUs; operates in integer registers, targets IoT/tinyML | risc-v, dsp, packed-simd, embedded, tinyml | 4 | 0 |
| [nuclei_ux900_n900](entity/nuclei_ux900_n900.md) | Nuclei 32/64-bit RISC-V cores with RVV VLEN 128–512; ~1B cumulative shipments, ASIL-D certified | risc-v, commercial-ip, china, embedded, aiot, nuclei | 4 | 0 |

## Synthesis Pages

| Page | Connected Entities | Status | Inbound |
|------|--------------------|--------|---------|
| [riscv_open_ai_acceleration](synthesis/riscv_open_ai_acceleration.md) | risc_v_vector_extension, alibaba_xuantie_c950, alibaba_xuantie_c910_c920, esperanto_et_soc1, tenstorrent_tt_ascalon, sifive_intelligence_x280, ventana_veyron_v2, tvm_riscv_backend | draft | 0 |
| [riscv_open_source_ai_stack](synthesis/riscv_open_source_ai_stack.md) | gemmini, ara_vector_processor, mlir_riscv_backend, iree_riscv, tvm_riscv_backend, risc_v_vector_extension, risc_v_p_extension, boom_riscv, andes_ax45mp_nx27v, xiangshan_riscv | draft | 0 |

## Concept Index

- **RVV (RISC-V Vector Extension)**: → [risc_v_vector_extension](entity/risc_v_vector_extension.md)
- **RVA23 Profile**: → [risc_v_vector_extension](entity/risc_v_vector_extension.md) — *mandatory RVV; also see [[ventana_veyron_v2]], [[tenstorrent_tt_ascalon]], [[alibaba_xuantie_c950]]*
- **XuanTie C950**: → [alibaba_xuantie_c950](entity/alibaba_xuantie_c950.md)
- **XuanTie C910 / C920**: → [alibaba_xuantie_c910_c920](entity/alibaba_xuantie_c910_c920.md)
- **Attached Matrix Extension (AME)**: → [alibaba_xuantie_c950](entity/alibaba_xuantie_c950.md)
- **Tensor Processing Engine (TPE)**: → [alibaba_xuantie_c950](entity/alibaba_xuantie_c950.md)
- **ET-SoC-1**: → [esperanto_et_soc1](entity/esperanto_et_soc1.md)
- **ET-Minion / ET-Maxion**: → [esperanto_et_soc1](entity/esperanto_et_soc1.md)
- **TT-Ascalon / Ascalon-X**: → [tenstorrent_tt_ascalon](entity/tenstorrent_tt_ascalon.md)
- **Babylon (Tenstorrent)**: mentioned in [tenstorrent_tt_ascalon](entity/tenstorrent_tt_ascalon.md) — *no dedicated page*
- **SiFive Intelligence X280**: → [sifive_intelligence_x280](entity/sifive_intelligence_x280.md)
- **VCIX (Vector Coprocessor Interface Extension)**: → [sifive_intelligence_x280](entity/sifive_intelligence_x280.md)
- **Ventana Veyron V2**: → [ventana_veyron_v2](entity/ventana_veyron_v2.md)
- **UCIe chiplet interface**: → [ventana_veyron_v2](entity/ventana_veyron_v2.md)
- **Apache TVM**: → [tvm_riscv_backend](entity/tvm_riscv_backend.md)
- **TVM MetaSchedule**: → [tvm_riscv_backend](entity/tvm_riscv_backend.md)
- **IREE (ML runtime)**: → [iree_riscv](entity/iree_riscv.md)
- **muRISCV-NN**: mentioned in [tvm_riscv_backend](entity/tvm_riscv_backend.md) — *no dedicated page*
- **SPEED processor**: mentioned in [risc_v_vector_extension](entity/risc_v_vector_extension.md) — *no dedicated page*
- **Gemmini**: → [gemmini](entity/gemmini.md)
- **RoCC (Rocket Chip Co-processor interface)**: → [gemmini](entity/gemmini.md)
- **Ara / Ara2 / AraXL**: → [ara_vector_processor](entity/ara_vector_processor.md)
- **XiangShan (香山) / Yanqihu / Nanhu / Kunminghu**: → [xiangshan_riscv](entity/xiangshan_riscv.md)
- **BOOM / SonicBOOM**: → [boom_riscv](entity/boom_riscv.md)
- **Andes AX45MP / NX27V / AndesAIRE**: → [andes_ax45mp_nx27v](entity/andes_ax45mp_nx27v.md)
- **MLIR vector dialect / RVV dialect**: → [mlir_riscv_backend](entity/mlir_riscv_backend.md)
- **RISC-V P-extension (packed SIMD)**: → [risc_v_p_extension](entity/risc_v_p_extension.md)
- **Nuclei UX900 / N900 / QiLai**: → [nuclei_ux900_n900](entity/nuclei_ux900_n900.md)
- **linalg.mmt4d**: → [iree_riscv](entity/iree_riscv.md)
- **FireSim**: mentioned in [boom_riscv](entity/boom_riscv.md) — *no dedicated page*
