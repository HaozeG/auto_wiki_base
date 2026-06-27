# Wiki Index

Last updated: 2026-06-27 | Pages: 28 | Sources: 63

## Entity Pages

| Page | Summary | Tags | Sources | Inbound |
|------|---------|------|---------|---------|
| [risc_v_vector_extension](entity/risc_v_vector_extension.md) | Standardized SIMD-style ISA extension enabling variable-width vector computation across RISC-V implementations | risc-v, hardware, AI-acceleration, vector-processing, ISA | 4 | 13 |
| [alibaba_xuantie_c950](entity/alibaba_xuantie_c950.md) | First RISC-V CPU architected for native LLM inference; 5nm, 3.2 GHz, 70+ SPECint2006, 8 TOPS/TPE | risc-v, AI-acceleration, processor, LLM-inference, alibaba | 4 | 2 |
| [alibaba_xuantie_c910_c920](entity/alibaba_xuantie_c910_c920.md) | Open-sourced out-of-order RISC-V cores adopting RVV 0.7.1 (C910) and RVV 1.0 (C920); predecessors to C950 | risc-v, processor, alibaba, out-of-order, open-source | 2 | 4 |
| [esperanto_et_soc1](entity/esperanto_et_soc1.md) | 1,092-core RISC-V AI inference chip on 7nm; 835.6 TOPS INT8 per 6-chip card at ~120W | risc-v, AI-accelerator, many-core, inference, hardware | 3 | 2 |
| [tenstorrent_tt_ascalon](entity/tenstorrent_tt_ascalon.md) | RVA23-compliant 8-wide OoO RISC-V CPU IP achieving 22+ SPECint2006/GHz on Samsung SF4X | risc-v, processor, AI-acceleration, out-of-order, server | 3 | 5 |
| [sifive_intelligence_x280](entity/sifive_intelligence_x280.md) | 512-bit VLEN in-order RISC-V core with VCIX custom extension interface; 12× inference speedup over base RISC-V | risc-v, processor, vector-processing, AI-acceleration, embedded | 3 | 5 |
| [ventana_veyron_v2](entity/ventana_veyron_v2.md) | 192-core, 4nm, 3.6 GHz RVA23-compliant server CPU with UCIe chiplet interface for AI accelerator attachment | risc-v, server, data-center, AI-acceleration, chiplet | 3 | 3 |
| [tvm_riscv_backend](entity/tvm_riscv_backend.md) | Apache TVM compiler backend for RISC-V RVV achieving 46% latency reduction vs GCC and 35% vs LLVM | compiler, optimization, risc-v, TVM, ML-frameworks, quantization | 4 | 4 |
| [gemmini](entity/gemmini.md) | Open-source parameterizable systolic array generator for DNN inference, attached to RISC-V via RoCC; 106.1 GOPS/W on Beagle SoC | risc-v, accelerator, systolic-array, open-source, uc-berkeley | 3 | 1 |
| [ara_vector_processor](entity/ara_vector_processor.md) | ETH Zurich open-source RVV 1.0 lane-scalable vector processor; 2–64 lanes, 41 DP-GFLOPS/W in 22 nm FD-SOI | risc-v, vector-processor, open-source, eth-zurich, rvv | 4 | 1 |
| [xiangshan_riscv](entity/xiangshan_riscv.md) | ICT-CAS open-source OoO RISC-V; 16.5 SPEC CPU2006 pts/GHz, Cortex-A76 class, Chisel/Mulan PSL | risc-v, open-source, high-performance, out-of-order, china | 4 | 2 |
| [boom_riscv](entity/boom_riscv.md) | UC Berkeley open-source OoO RISC-V (SonicBOOM); 6.2 CoreMarks/MHz, Chisel, Gemmini host CPU | risc-v, open-source, out-of-order, uc-berkeley, research | 4 | 1 |
| [andes_ax45mp_nx27v](entity/andes_ax45mp_nx27v.md) | Andes 64-bit superscalar AX45MP + NX27V RVV 1.0 VPU; BF16/Int4, AndesAIRE SDK, QiLai SoC | risc-v, commercial-ip, dsp, vector, ai-edge, andes-technology | 3 | 1 |
| [mlir_riscv_backend](entity/mlir_riscv_backend.md) | MLIR/LLVM lowering pipeline for RVV: Linalg → vector dialect → RVV intrinsics → machine code | mlir, risc-v, compiler, rvv, llvm, software-stack | 4 | 0 |
| [iree_riscv](entity/iree_riscv.md) | Google IREE ML compiler runtime on RISC-V; added RV64 microkernels in 2025 for GenAI workloads | risc-v, mlir, compiler-runtime, google, ml-deployment | 4 | 0 |
| [risc_v_p_extension](entity/risc_v_p_extension.md) | RISC-V packed SIMD/DSP extension for embedded MCUs; operates in integer registers, targets IoT/tinyML | risc-v, dsp, packed-simd, embedded, tinyml | 4 | 1 |
| [nuclei_ux900_n900](entity/nuclei_ux900_n900.md) | Nuclei 32/64-bit RISC-V cores with RVV VLEN 128–512; ~1B cumulative shipments, ASIL-D certified | risc-v, commercial-ip, china, embedded, aiot, nuclei | 4 | 0 |
| [riscv_matrix_extension](entity/riscv_matrix_extension.md) | In-development Attached Matrix Extension (AME) TG; standalone or RVV-coupled, datatypes FP64/INT8/FP8, 4–7× speedup MME precursor | risc-v, matrix-extension, AI-acceleration, ISA, AME | 3 | 2 |
| [andes_nx27v_sifive_p870_comparison](entity/andes_nx27v_sifive_p870_comparison.md) | NX27V (RVV 512-bit in-order VPU) vs P870 (6-wide OoO RVA23 CPU + X390 NPU) — two divergent RISC-V AI design philosophies | risc-v, comparison, vector-processor, npu, AI-acceleration | 3 | 0 |
| [qualcomm_riscv_ai](entity/qualcomm_riscv_ai.md) | Qualcomm shipped ~650M RISC-V MCUs in Snapdragon; acquired Ventana (Veyron V2); Snapdragon Wear RISC-V SoC due 2025 | risc-v, qualcomm, edge-ai, wearable, datacenter | 3 | 0 |
| [starfive_jh7110_visionfive2](entity/starfive_jh7110_visionfive2.md) | Quad-core U74 RISC-V SBC with on-die NVDLA + NNE; VisionFive 2 AI Kit with Hailo-8L delivers 13 TOPS | risc-v, sbc, edge-ai, nvdla, hailo | 3 | 1 |
| [canaan_kendryte_k510_k230](entity/canaan_kendryte_k510_k230.md) | First commercial RISC-V AI chip family; K230: dual XuanTie C908, RVV 1.0, 6 TOPS KPU, TSMC 12nm, ~2W | risc-v, ai-soc, edge-vision, kpu, canaan | 3 | 2 |
| [riscv_zve_sub_extensions](entity/riscv_zve_sub_extensions.md) | Zve32x/32f/64x/64f/64d embedded vector sub-extensions for MCU-class TinyML inference; hwprobe in Linux 6.10 | risc-v, embedded, tinyml, vector, ISA | 3 | 2 |
| [openhw_cva6](entity/openhw_cva6.md) | Open-source 6-stage in-order RV64 Linux-capable core; CV-X-IF accelerator interface; Solderpad license; TRL-5; 1.7 GHz 22nm | risc-v, open-source, processor, application-class, OpenHW | 4 | 2 |
| [pulp_platform](entity/pulp_platform.md) | ETH Zurich + Bologna parallel ULP RISC-V platform; 50+ chips, Darkside 835 GOPS/W, Occamy 432-core 6.1 TFLOPS | risc-v, ultra-low-power, open-source, eth-zurich, tinyml | 3 | 2 |
| [chips_alliance_governance](entity/chips_alliance_governance.md) | Linux Foundation-hosted open HW consortium; Verilator, SweRV, AIB chiplet std; three-tier RISC-V governance model | risc-v, governance, open-source, eda, chiplets | 3 | 0 |

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
- **XuanTie C908**: mentioned in [canaan_kendryte_k510_k230](entity/canaan_kendryte_k510_k230.md) — *no dedicated page*
- **Attached Matrix Extension (AME)**: → [riscv_matrix_extension](entity/riscv_matrix_extension.md)
- **Tensor Processing Engine (TPE)**: → [alibaba_xuantie_c950](entity/alibaba_xuantie_c950.md)
- **ET-SoC-1**: → [esperanto_et_soc1](entity/esperanto_et_soc1.md)
- **ET-Minion / ET-Maxion**: → [esperanto_et_soc1](entity/esperanto_et_soc1.md)
- **TT-Ascalon / Ascalon-X**: → [tenstorrent_tt_ascalon](entity/tenstorrent_tt_ascalon.md)
- **Babylon (Tenstorrent)**: mentioned in [tenstorrent_tt_ascalon](entity/tenstorrent_tt_ascalon.md) — *no dedicated page*
- **SiFive Intelligence X280**: → [sifive_intelligence_x280](entity/sifive_intelligence_x280.md)
- **SiFive Intelligence X390 NPU**: mentioned in [andes_nx27v_sifive_p870_comparison](entity/andes_nx27v_sifive_p870_comparison.md) — *no dedicated page*
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
- **CV-X-IF (Coprocessor Extension Interface)**: → [openhw_cva6](entity/openhw_cva6.md)
- **Ara / Ara2 / AraXL**: → [ara_vector_processor](entity/ara_vector_processor.md)
- **XiangShan (香山) / Yanqihu / Nanhu / Kunminghu**: → [xiangshan_riscv](entity/xiangshan_riscv.md)
- **BOOM / SonicBOOM**: → [boom_riscv](entity/boom_riscv.md)
- **Andes AX45MP / NX27V / AndesAIRE**: → [andes_ax45mp_nx27v](entity/andes_ax45mp_nx27v.md)
- **MLIR vector dialect / RVV dialect**: → [mlir_riscv_backend](entity/mlir_riscv_backend.md)
- **RISC-V P-extension (packed SIMD)**: → [risc_v_p_extension](entity/risc_v_p_extension.md)
- **Nuclei UX900 / N900 / QiLai**: → [nuclei_ux900_n900](entity/nuclei_ux900_n900.md)
- **linalg.mmt4d**: → [iree_riscv](entity/iree_riscv.md)
- **FireSim**: mentioned in [boom_riscv](entity/boom_riscv.md) — *no dedicated page*
- **Zve* sub-extensions**: → [riscv_zve_sub_extensions](entity/riscv_zve_sub_extensions.md)
- **StarFive JH7110 / VisionFive 2**: → [starfive_jh7110_visionfive2](entity/starfive_jh7110_visionfive2.md)
- **NVDLA (NVIDIA Deep Learning Accelerator)**: → [starfive_jh7110_visionfive2](entity/starfive_jh7110_visionfive2.md)
- **Hailo-8L**: mentioned in [starfive_jh7110_visionfive2](entity/starfive_jh7110_visionfive2.md) — *no dedicated page*
- **Canaan Kendryte K230 / K510 / K210**: → [canaan_kendryte_k510_k230](entity/canaan_kendryte_k510_k230.md)
- **KPU (Knowledge Process Unit)**: → [canaan_kendryte_k510_k230](entity/canaan_kendryte_k510_k230.md)
- **Qualcomm Snapdragon RISC-V**: → [qualcomm_riscv_ai](entity/qualcomm_riscv_ai.md)
- **Snapdragon Wear RISC-V**: → [qualcomm_riscv_ai](entity/qualcomm_riscv_ai.md)
- **Chips Alliance**: → [chips_alliance_governance](entity/chips_alliance_governance.md)
- **AIB (Advanced Interface Bus)**: → [chips_alliance_governance](entity/chips_alliance_governance.md)
- **Verilator**: mentioned in [chips_alliance_governance](entity/chips_alliance_governance.md) — *no dedicated page*
- **PULP Platform**: → [pulp_platform](entity/pulp_platform.md)
- **Darkside processor**: mentioned in [pulp_platform](entity/pulp_platform.md) — *no dedicated page*
- **Occamy chiplet**: mentioned in [pulp_platform](entity/pulp_platform.md) — *no dedicated page*
- **xPULP ISA extensions**: mentioned in [pulp_platform](entity/pulp_platform.md) — *no dedicated page*
- **Greenwaves GAP8/GAP9**: mentioned in [pulp_platform](entity/pulp_platform.md) — *no dedicated page*
- **OpenHW Group**: → [openhw_cva6](entity/openhw_cva6.md)
- **Eclipse Foundation**: mentioned in [chips_alliance_governance](entity/chips_alliance_governance.md) — *no dedicated page*
