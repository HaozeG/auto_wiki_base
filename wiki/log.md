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

## [2026-06-27] lint | routine
issues_found: 6
actions_taken:
  - reconciled inbound_links frontmatter from actual [[wikilink]] graph (46 pages updated)
  - mean_inbound_links corrected from 0.90 to 3.97 — graph now MATURE
  - updated CLAUDE.md system_state: graph_maturity=true, mean_inbound_links=3.9655
deferred_for_human:
  - MERGE candidate: gnu_toolchain_riscv_vector ↔ riscv_llvm_backend (6 shared tags; both cover GCC+LLVM RVV support)
  - MERGE candidate: chipyard_soc_framework ↔ rocket_chip_generator (4 shared tags; Rocket is subcomponent of Chipyard)
  - MERGE candidate: tinyml_riscv ↔ muriscv_nn (3 shared tags; muriscv_nn is the dominant RISC-V TinyML library)
  - MERGE candidate: llm_inference_riscv ↔ onnx_runtime_riscv (3 shared tags; partial topic overlap)
  - ORPHAN review: 8 pages with inbound_links=0 — andes_nx27v_sifive_p870_comparison, microchip_polarfire_soc, nvidia_riscv_falcon_gsp, rocket_chip_generator, shakti_processor, sifive_hifive_boards, sifive_p870_x390, wd_swerv_cores
  - needs_summary_revision=true on 25 pages (Layer 3 coverage 0.20 across board; caused by qmd returning similar pages for every RISC-V query — topic saturation)

## [2026-06-27] transition | cold_start → mature
pages_at_transition: 58
mean_inbound_links: 3.97

## [2026-06-27] research | RISC-V AI accelerator software stack
session_id: b2d85c85
candidates_evaluated: 2
pages_written: 1
pipeline_rejection_rate: 0%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_b2d85c85_2026-06-27.json

## [2026-06-27] research | RISC-V AI accelerator kernel optimization
session_id: 45e63013
candidates_evaluated: 2
pages_written: 1
pipeline_rejection_rate: 0%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_45e63013_2026-06-27.json

## [2026-06-27] research | RISC-V AI accelerator optimization software deploy
session_id: 9d098879
candidates_evaluated: 8
pages_written: 2
pipeline_rejection_rate: 38%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_9d098879_2026-06-27.json

## [2026-06-28] research | RISC-V AI accelerator optimization software deploy
session_id: 13ed63de
candidates_evaluated: 9
pages_written: 1
pipeline_rejection_rate: 11%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_13ed63de_2026-06-28.json

## [2026-06-28] research | Tenstorrent optimization software nn
session_id: 7c38510c
candidates_evaluated: 7
pages_written: 3
pipeline_rejection_rate: 43%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_7c38510c_2026-06-28.json

## [2026-06-28] research | Tenstorrent optimization software nn
session_id: d9f8f654
candidates_evaluated: 3
pages_written: 3
pipeline_rejection_rate: 0%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_d9f8f654_2026-06-28.json

## [2026-06-28] research | Tenstorrent optimization kernel
session_id: 9bc681d5
candidates_evaluated: 8
pages_written: 4
pipeline_rejection_rate: 12%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_9bc681d5_2026-06-28.json

## [2026-06-28] research | RISC-V optimization kernel
session_id: 4a90b4dc
candidates_evaluated: 3
pages_written: 3
pipeline_rejection_rate: 0%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_4a90b4dc_2026-06-28.json

## [2026-06-28] research | RISC-V optimization kernel
session_id: 8d43da0f
candidates_evaluated: 9
pages_written: 6
pipeline_rejection_rate: 22%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_8d43da0f_2026-06-28.json

## [2026-06-28] lint | retrospective
issues_found: 50
actions_taken:
  - fixed 7 pages with malformed frontmatter closing delimiters (--- + extra dashes)
  - set cold_start: false on 36 CLEARED pages
deferred_for_human:
  - RESTRUCTURE: synthesis/riscv_standardization_software_ecosystem.md — EMPTY_SOURCES Layer 1 fail; needs sources list added to frontmatter
  - MERGE Cluster A (confirmed): tt_metalium.md + tt_metalium_framework.md → tenstorrent_tt_metalium.md (awaiting lint apply)
  - MERGE Cluster B (confirmed): sifive_intelligence_x390.md → sifive_p870_x390.md (awaiting lint apply)
  - MERGE Cluster C (human decision): greenwaves_gap8_gap9.md — combined overview, may overlap with gap8/gap9 pages
  - SATURATION-ONLY: 45 pages flagged by Layer 3 BM25 saturation; no action proposed (expected in focused domain wiki)
report: wiki/retrospective_lint_report.md
