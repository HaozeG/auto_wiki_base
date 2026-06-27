# Wiki Log

## [2026-06-27] ingest | web research — RISC-V AI batch 5: hardware/SoCs, compilers, power, automotive
pages_created:
  - entity/sophgo_sg2042.md
  - entity/allwinner_d1.md
  - entity/bouffalo_lab_bl808_bl616.md
  - entity/nvidia_riscv_falcon_gsp.md
  - entity/rocket_chip_generator.md
  - entity/greenwaves_gap8_gap9.md
  - entity/tinyml_riscv.md
  - entity/riscv_automotive_asil.md
  - entity/riscv_llvm_backend.md
  - synthesis/riscv_vs_arm_edge_ai.md
pages_updated: []
pages_deferred:
  - ICG GX8010: insufficient verifiable public claims found
  - OpenCL on RISC-V (POCL): insufficient verifiable benchmark data
  - Halide on RISC-V: insufficient verifiable deployment data
  - JAX on RISC-V: insufficient verifiable implementation data
cold_start: true

## [2026-06-27] ingest | web research — RISC-V AI accelerator and optimizations
pages_created:
  - entity/risc_v_vector_extension.md
  - entity/alibaba_xuantie_c950.md
  - entity/alibaba_xuantie_c910_c920.md
  - entity/esperanto_et_soc1.md
  - entity/tenstorrent_tt_ascalon.md
  - entity/sifive_intelligence_x280.md
  - entity/ventana_veyron_v2.md
  - entity/tvm_riscv_backend.md
  - synthesis/riscv_open_ai_acceleration.md
pages_updated: []
pages_deferred: []
cold_start: true

## [2026-06-27] ingest | web research — RISC-V AI loop batch 2
pages_created:
  - entity/gemmini.md
  - entity/ara_vector_processor.md
  - entity/xiangshan_riscv.md
  - entity/boom_riscv.md
  - entity/andes_ax45mp_nx27v.md
  - entity/mlir_riscv_backend.md
  - entity/iree_riscv.md
  - entity/risc_v_p_extension.md
  - entity/nuclei_ux900_n900.md
  - synthesis/riscv_open_source_ai_stack.md
pages_updated:
  - entity/risc_v_vector_extension.md (inbound_links: 0 → 6)
  - entity/tvm_riscv_backend.md (inbound_links: 0 → 4)
  - entity/alibaba_xuantie_c910_c920.md (inbound_links: 0 → 2)
pages_deferred:
  - RISC-V Matrix Extension (Zmatmul/CMX/AME): insufficient verifiable published specs; proposal still in draft TG stage
  - Qualcomm RISC-V AI cores: no verifiable public specs for Cloud AI 100 RISC-V claims
  - ONNX Runtime RISC-V: thin verifiable claims, no distinct page warranted vs iree/tvm coverage
  - GNU/LLVM auto-vectorization RVV: covered within mlir_riscv_backend.md
  - Near-memory computing RISC-V PIM: insufficient verifiable RISC-V-specific claims
cold_start: true

## [2026-06-27] ingest | web research — RISC-V AI batch 3: Matrix Extension, edge AI SoCs, open-source hardware
pages_created:
  - entity/riscv_matrix_extension.md
  - entity/andes_nx27v_sifive_p870_comparison.md
  - entity/qualcomm_riscv_ai.md
  - entity/starfive_jh7110_visionfive2.md
  - entity/canaan_kendryte_k510_k230.md
  - entity/riscv_zve_sub_extensions.md
  - entity/openhw_cva6.md
  - entity/pulp_platform.md
  - entity/chips_alliance_governance.md
pages_updated:
  - entity/risc_v_vector_extension.md (inbound_links: 6 → 13)
  - entity/xiangshan_riscv.md (inbound_links: 0 → 2)
  - entity/alibaba_xuantie_c910_c920.md (inbound_links: 2 → 4)
  - entity/tenstorrent_tt_ascalon.md (inbound_links: 2 → 5)
  - entity/andes_ax45mp_nx27v.md (inbound_links: 0 → 1)
  - entity/sifive_intelligence_x280.md (inbound_links: 2 → 5)
  - entity/ventana_veyron_v2.md (inbound_links: 2 → 3)
  - entity/risc_v_p_extension.md (inbound_links: 0 → 1)
  - entity/gemmini.md (inbound_links: 0 → 1)
  - entity/boom_riscv.md (inbound_links: 0 → 1)
  - entity/ara_vector_processor.md (inbound_links: 0 → 1)
pages_deferred: []
cold_start: true

## [2026-06-27] lint | retrospective
issues_found: 14
actions_taken:
  - fixed eval_summary.py _set_frontmatter_flag bug (------ → --- delimiter corruption)
  - fixed 11 entity pages with corrupted ------ frontmatter closers
  - expanded first paragraph of 5 entity pages to meet 80-word minimum
  - added sources frontmatter to 2 synthesis pages
deferred_for_human:
  - needs_summary_revision flag on multiple pages (non-blocking, Layer 3 coverage low at cold_start)

## [2026-06-27] ingest | web research — RISC-V AI batch 3 (8 new entity pages)
pages_created:
  - entity/shakti_processor
  - entity/gnu_toolchain_riscv_vector
  - entity/onnx_runtime_riscv
  - entity/muriscv_nn
  - entity/risc_v_profiles_rva
  - entity/sifive_p870_x390
  - entity/openxiangshan_difftest_nemu
  - entity/canaan_kendryte_k230
pages_updated: []
pages_deferred:
  - entity/pulp_platform_gap8_gap9: near-duplicate of existing pulp_platform (different GAP8/GAP9 focus; not added to index)
  - entity/risc_v_zve_embedded_vector: near-duplicate of riscv_zve_sub_extensions; not added to index
  - entity/risc_v_matrix_extension: near-duplicate of riscv_matrix_extension; not added to index
  - entity/chips_alliance: near-duplicate of chips_alliance_governance; not added to index
  - entity/starfive_jh7110: near-duplicate of starfive_jh7110_visionfive2; not added to index
cold_start: true

## [2026-06-27] ingest | synthesis — RISC-V ISA Standardization and Software Stack Convergence
pages_created: [synthesis/riscv_standardization_software_ecosystem]
pages_updated: []
pages_deferred: []
cold_start: true

## [2026-06-27] ingest | web research — WD SweRV Cores
pages_created: [wd_swerv_cores]
pages_updated: []
pages_deferred: []
cold_start: true

## [2026-06-27] ingest | web research — T-Head TH1520 SoC
pages_created: [thead_th1520]
pages_updated: []
pages_deferred: []
cold_start: true

## [2026-06-27] ingest | web research — Microchip PolarFire SoC
pages_created: [microchip_polarfire_soc]
pages_updated: []
pages_deferred: []
cold_start: true

## [2026-06-27] ingest | web research — Milk-V Pioneer and Duo
pages_created: [milkv_pioneer_duo]
pages_updated: []
pages_deferred: []
cold_start: true

## [2026-06-27] ingest | web research — SiFive HiFive Boards
pages_created: [sifive_hifive_boards]
pages_updated: []
pages_deferred: []
cold_start: true

## [2026-06-27] ingest | web research — BeagleV-Ahead
pages_created: [beaglev_ahead]
pages_updated: []
pages_deferred: []
cold_start: true

## [2026-06-27] ingest | web research — LLM Inference on RISC-V
pages_created: [llm_inference_riscv]
pages_updated: []
pages_deferred: []
cold_start: true

## [2026-06-27] ingest | web research — Hwacha Vector Accelerator
pages_created: [hwacha_vector_accelerator]
pages_updated: []
pages_deferred: []
cold_start: true

## [2026-06-27] ingest | web research — Chipyard SoC Framework
pages_created: [chipyard_soc_framework]
pages_updated: []
pages_deferred: []
cold_start: true

## [2026-06-27] ingest | web research — FireSim FPGA Simulation
pages_created: [firesim_fpga_simulation]
pages_updated: []
pages_deferred: []
cold_start: true

## [2026-06-27] ingest | web research — Sparse Computation on RISC-V
pages_created: [riscv_sparse_computation]
pages_updated: []
pages_deferred: []
cold_start: true

## [2026-06-27] ingest | web research — RISC-V Edge AI to LLM Inference (synthesis)
pages_created: [synthesis/riscv_edge_ai_llm_inference]
pages_updated: []
pages_deferred: []
cold_start: true
