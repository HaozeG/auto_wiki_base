# Wiki Log

## [2026-06-29] lint | retrospective
issues_found: 0
actions_taken: [cold_start: false set on 54 pages, needs_summary_revision cleared]
deferred_for_human: []

## [2026-06-29] lint | apply
actions_taken:
  - DELETED entity/Qwen3.6.md (off-theme, 0 inbound)
  - DELETED entity/Qwen2.5-Coder-1.5B-Instruct-GGUF.md (off-theme, 0 inbound)
  - DELETED entity/Gemmini.md (merged into hardware_target/Gemmini_Architecture.md)
  - DELETED hardware_target/RVME_Model.md (merged into hardware_target/RVME_Matrix_Engine.md)
pages_after: 136
mean_inbound_links: 2.302

## [2026-06-29] lint | routine
issues_found: 6 categories
actions_taken: [none — output for human review]
deferred_for_human:
  - 61 orphan pages
  - 2 off-theme pages (Qwen3.6, Qwen2.5-Coder-1.5B-Instruct-GGUF)
  - 2 duplicate entity pages (entity/Gemmini.md vs hardware_target/Gemmini_Architecture.md + Gemmini_systolic_array_GEMM_accelerator.md)
  - 2 duplicate RVME hardware_target pages (RVME_Matrix_Engine.md vs RVME_Model.md)
  - 80 pages flagged needs_summary_revision: true (Layer 3 BM25 saturation false-positives)
  - 5 synthesis pages with inbound_links: 0

## [2026-06-29] query_synthesis | RISC-V ISA Extensions for AI Acceleration
source_query: synthesis gap — 18 RISC-V-tagged entity pages without synthesis coverage
pages_created: [synthesis/RISC-V_ISA_Extensions_for_AI.md]

## [2026-06-29] query_synthesis | MLIR for RISC-V AI Compilation
source_query: synthesis gap — 4 MLIR-tagged entity pages without synthesis coverage
pages_created: [synthesis/MLIR_for_RISC-V_AI_Compilation.md]

## [2026-06-29] query_synthesis | Tenstorrent RISC-V AI Ecosystem
source_query: synthesis gap — 6 Tenstorrent-tagged entity pages without synthesis coverage
pages_created: [synthesis/Tenstorrent_RISC-V_AI_Ecosystem.md]

## [2026-06-29] ingest | RVME_An_Efficient_Matrix_Engine_Design_Based_on_Matrix_Extension_of_RISC-V.pdf
pages_created: [hardware_target/RVME_Matrix_Engine.md, benchmark_result/RVME_GEMM_Benchmark.md]
pages_updated: []
pages_deferred: []
cold_start: true
inbound_link_updates: [RISC-V_Matrix_Extension.md +2, Gemmini_Architecture.md +2]

## [2026-06-29] ingest | riscv_matrix_extension_proposal.pdf
pages_created: [entity/RISC-V_Matrix_Extension.md]
pages_updated: []
pages_deferred: []
cold_start: true
inbound_link_updates: [RISC-V_Vector_Extension.md +1, GEMM_with_RISC-V_Vector_Extension.md +1]

## [2026-06-28] setup | theme — RISC-V AI Accelerator
branch: test/riscv-ai-accelerator-2026-06-28
organization: workflow_first
page_types: hardware_target, workload_kernel, optimization_recipe, benchmark_result, entity, synthesis, source_note
source_preferences: official documentation, benchmark repository, compiler documentation, SDK guide, paper
coverage_priorities: hardware/software/workload coverage, measurement context for benchmark results, optimization prerequisites and failure modes


## [2026-06-28] research | RISC-V AI accelerator inference performance benchmark
session_id: 221b2517
candidates_evaluated: 4
pages_written: 5
pipeline_rejection_rate: 0%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_221b2517_2026-06-28.json
theme_profile: RISC-V ai accelerator | workflow_first
coverage_gaps:
  - missing_page_type:hardware_target
  - missing_page_type:workload_kernel
  - missing_page_type:optimization_recipe
  - missing_page_type:benchmark_result
  - missing_structured_field:hardware_targets
  - missing_structured_field:workloads
  - missing_structured_field:metrics
  - missing_structured_field:toolchains

## [2026-06-28] research | RISC-V vector extension SIMD ML kernel inference optimizatio
session_id: 2dabb075
candidates_evaluated: 3
pages_written: 5
pipeline_rejection_rate: 33%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_2dabb075_2026-06-28.json
theme_profile: RISC-V ai accelerator | workflow_first
coverage_gaps:
  - missing_page_type:workload_kernel
  - missing_page_type:optimization_recipe
  - missing_page_type:benchmark_result
  - missing_structured_field:workloads
  - missing_structured_field:metrics
  - missing_structured_field:toolchains

## [2026-06-28] research | RISC-V NPU SoC edge AI inference throughput benchmark
session_id: 5f5d3c17
candidates_evaluated: 9
pages_written: 2
pipeline_rejection_rate: 22%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_5f5d3c17_2026-06-28.json
theme_profile: RISC-V ai accelerator | workflow_first
coverage_gaps:
  - missing_page_type:benchmark_result

## [2026-06-28] research | RISC-V AI inference compiler LLVM TVM IREE ONNX Runtime tool
session_id: 16583ce9
candidates_evaluated: 7
pages_written: 5
pipeline_rejection_rate: 14%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_16583ce9_2026-06-28.json
theme_profile: RISC-V ai accelerator | workflow_first
coverage_gaps:
  - missing_page_type:benchmark_result

## [2026-06-28] research | RISC-V transformer attention inference LLM quantization acce
session_id: 13ec62bc
candidates_evaluated: 7
pages_written: 5
pipeline_rejection_rate: 0%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_13ec62bc_2026-06-28.json
theme_profile: RISC-V ai accelerator | workflow_first

## [2026-06-28] research | SpacemiT T-Head SiFive RISC-V AI SoC inference performance 2
session_id: aa54b157
candidates_evaluated: 10
pages_written: 5
pipeline_rejection_rate: 10%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_aa54b157_2026-06-28.json
theme_profile: RISC-V ai accelerator | workflow_first

## [2026-06-28] research | RISC-V INT8 INT4 quantization neural network inference effic
session_id: c0e668a4
candidates_evaluated: 8
pages_written: 5
pipeline_rejection_rate: 38%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_c0e668a4_2026-06-28.json
theme_profile: RISC-V ai accelerator | workflow_first

## [2026-06-28] research | Gemmini NVDLA open source RISC-V AI accelerator chipyard tap
session_id: 830581bb
candidates_evaluated: 4
pages_written: 3
pipeline_rejection_rate: 0%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_830581bb_2026-06-28.json
theme_profile: RISC-V ai accelerator | workflow_first

## [2026-06-28] research | SpacemiT K1 BananaPi F3 Milk-V Jupiter RISC-V AI inference b
session_id: 5c6e9b0b
candidates_evaluated: 10
pages_written: 1
pipeline_rejection_rate: 10%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_5c6e9b0b_2026-06-28.json
theme_profile: RISC-V ai accelerator | workflow_first

## [2026-06-28] research | RISC-V AI accelerator landscape survey comparison 2024 2025 
session_id: 33d5703c
candidates_evaluated: 10
pages_written: 2
pipeline_rejection_rate: 20%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_33d5703c_2026-06-28.json
theme_profile: RISC-V ai accelerator | workflow_first

## [2026-06-28] research | IREE TVM LLVM MLIR RISC-V machine learning compiler backend 
session_id: 260c01bf
candidates_evaluated: 5
pages_written: 5
pipeline_rejection_rate: 0%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_260c01bf_2026-06-28.json
theme_profile: RISC-V ai accelerator | workflow_first

## [2026-06-28] research | RVV RISC-V vector llama.cpp GEMM matmul benchmark performanc
session_id: ad3d3223
candidates_evaluated: 10
pages_written: 1
pipeline_rejection_rate: 0%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_ad3d3223_2026-06-28.json
theme_profile: RISC-V ai accelerator | workflow_first

## [2026-06-28] research | T-Head XuanTie C908 C910 SiFive X390 P870 RISC-V processor p
session_id: 391b554a
candidates_evaluated: 10
pages_written: 4
pipeline_rejection_rate: 10%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_391b554a_2026-06-28.json
theme_profile: RISC-V ai accelerator | workflow_first

## [2026-06-28] research | Kendryte K210 K510 KPU MLPerf Tiny TinyML RISC-V edge AI ben
session_id: 43dcd93e
candidates_evaluated: 9
pages_written: 4
pipeline_rejection_rate: 22%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_43dcd93e_2026-06-28.json
theme_profile: RISC-V ai accelerator | workflow_first

## [2026-06-28] research | RISC-V AI machine learning accelerator survey review paper a
session_id: 591cbaa5
candidates_evaluated: 4
pages_written: 6
pipeline_rejection_rate: 25%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_591cbaa5_2026-06-28.json
theme_profile: RISC-V ai accelerator | workflow_first

## [2026-06-28] research | RISC-V open source Gemmini accelerator TVM IREE deployment K
session_id: 5eda0bb6
candidates_evaluated: 7
pages_written: 4
pipeline_rejection_rate: 43%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_5eda0bb6_2026-06-28.json
theme_profile: RISC-V ai accelerator | workflow_first

## [2026-06-28] research | XuanTie C906 C908 C910 RISC-V vector GEMM matrix multiplicat
session_id: ff45f3be
candidates_evaluated: 3
pages_written: 2
pipeline_rejection_rate: 0%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_ff45f3be_2026-06-28.json
theme_profile: RISC-V ai accelerator | workflow_first

## [2026-06-28] research | RISC-V RVV 1.0 vector extension performance multiple SoC pla
session_id: 012c54da
candidates_evaluated: 6
pages_written: 4
pipeline_rejection_rate: 0%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_012c54da_2026-06-28.json
theme_profile: RISC-V ai accelerator | workflow_first

## [2026-06-28] research | RISC-V NCNN MNN neural network inference framework optimizat
session_id: d796d2ac
candidates_evaluated: 12
pages_written: 6
pipeline_rejection_rate: 0%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_d796d2ac_2026-06-28.json
theme_profile: RISC-V ai accelerator | workflow_first

## [2026-06-28] research | deploy TVM IREE ONNX Runtime NCNN Kendryte K210 K230 LicheeP
session_id: e3536ed7
candidates_evaluated: 12
pages_written: 5
pipeline_rejection_rate: 8%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_e3536ed7_2026-06-28.json
theme_profile: RISC-V ai accelerator | workflow_first

## [2026-06-28] research | llama.cpp RISC-V RVV benchmark comparison Milk-V Pioneer Lic
session_id: 7609d80e
candidates_evaluated: 6
pages_written: 6
pipeline_rejection_rate: 17%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_7609d80e_2026-06-28.json
theme_profile: RISC-V ai accelerator | workflow_first

## [2026-06-28] research | MobileNet ResNet YOLO workload kernel RISC-V inference bench
session_id: 454306a6
candidates_evaluated: 9
pages_written: 6
pipeline_rejection_rate: 0%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_454306a6_2026-06-28.json
theme_profile: RISC-V ai accelerator | workflow_first

## [2026-06-28] research | RISC-V AI inference benchmark comparison survey 2024 XuanTie
session_id: 41c1b0d5
candidates_evaluated: 9
pages_written: 2
pipeline_rejection_rate: 0%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_41c1b0d5_2026-06-28.json
theme_profile: RISC-V ai accelerator | workflow_first

## [2026-06-28] research | RISC-V vector RVV convolution depthwise separable CNN worklo
session_id: 2dcbe256
candidates_evaluated: 9
pages_written: 4
pipeline_rejection_rate: 0%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_2dcbe256_2026-06-28.json
theme_profile: RISC-V ai accelerator | workflow_first

## [2026-06-29] ingest | synthesis | RISC-V ML Inference Toolchain Landscape
pages_created: [synthesis/RISC-V_ML_Inference_Toolchain_Landscape.md]
pages_updated: []
pages_deferred: []
cold_start: true
connected_entities: [IREE, ncnn, onnxruntime-riscv, ONNX_Runtime_Build_for_Inferencing, llama-cpp-mini, tvmonriscv, GEMM_with_RISC-V_Vector_Extension, QiMeng_TensorOp, XuanTie_GNU_Toolchain, Seal5]
inbound_links_updated: 10 pages

## [2026-06-29] ingest | synthesis | RISC-V AI Hardware Target Taxonomy
pages_created: [synthesis/RISC-V_AI_Hardware_Target_Taxonomy.md]
pages_updated: []
pages_deferred: []
cold_start: true
connected_entities: [XuanTie_C908, XuanTie_C910, SpacemiT_KeyStone_K1, MilkV_Pioneer, SiFive_Intelligence_X390, GAP8_PULP_Processor, Kendryte_K210, Gemmini_Architecture, Sipeed_LicheePi_4A, Kendryte_K230_SoC, SiFive_Performance_P870, Ara_simulator]
inbound_links_updated: 12 pages

## [2026-06-29] transition | cold_start → mature
pages_at_transition: 91
mean_inbound_links: 2.033

## [2026-06-29] lint | retrospective
issues_found: 23
actions_taken: [ran eval_summary.py on all 91 cold_start pages (all exit 0), set cold_start: false on 76 CLEARED pages, wrote wiki/retrospective_lint_report.md]
deferred_for_human: [7 merge clusters (15 pages), 1 restructure candidate (Chiplet_RISC_V_AI_SoC_Architecture), 2 synthesis orphans needing inbound links, systemic needs_summary_revision flag to bulk-clear]

## [2026-06-29] lint | apply
actions_taken:
  - Merged MLPerf Tiny cluster (3 → 1): MLPerf_Tiny_Benchmark.md absorbs v1.1 data and GitHub source; deleted MLPerf_Tiny.md and MLPerf_Tiny_v1.1.md
  - Merged Kendryte K230 cluster (3 → 1): Kendryte_K230_SoC.md absorbs SDK/board details; deleted entity/Kendryte_K230.md and hardware_target/Kendryte_K230.md
  - Merged Gemmini entity (1 → 0): entity/Gemmini.md absorbed into Gemmini_systolic_array_GEMM_accelerator.md (UCB context, Chisel, FireSim, tutorials); deleted entity/Gemmini.md
  - Merged XuanTie C910 duplicate: T-HEAD_XuanTie_C910.md absorbed into XuanTie_C910.md (XIE/XMAE, Coremark, DMIPS, JTAG, power discrepancy note); deleted T-HEAD_XuanTie_C910.md
  - Merged XuanTie C908 entity: entity/XuanTie_C908.md absorbed into hardware_target/XuanTie_C908.md (AIoT context, BF16, Linux 5.19 merge, Alibaba); deleted entity/XuanTie_C908.md
  - Merged FPGA ISA Extensions Recipe (3 → 1): absorbed into FPGA_Accelerated_RISC-V_CNN_ISA_Extensions_Recipe.md (INT8 accuracy failure mode, new relationships); deleted FPGA_Accelerated_RISC_V_ISA_Extensions_Optimization_Recipe.md and FPGA_RISC-V_ISA_Extensions_Optimization_Recipe.md
  - Merged FPGA ISA Extensions Benchmark (2 → 1): absorbed into FPGA_RISC-V_ISA_Extensions_Benchmark_Results.md; deleted FPGA_Accelerated_RISC_V_ISA_Extensions_Benchmark_Results.md
  - Restructured Chiplet_RISC_V_AI_SoC_Architecture.md (bridge_score=0.8): created synthesis/Chiplet_RISC_V_AI_Landscape.md comparing chiplet vs monolithic vs tightly-coupled RISC-V AI approaches
  - Updated inbound_links on 12 affected pages
  - Set retrospective_lint_done: true in CLAUDE.md
  - mean_inbound_links updated to 2.232 (82 pages)
pages_deleted: [entity/MLPerf_Tiny.md, entity/MLPerf_Tiny_v1.1.md, entity/Kendryte_K230.md, hardware_target/Kendryte_K230.md, entity/Gemmini.md, hardware_target/T-HEAD_XuanTie_C910.md, entity/XuanTie_C908.md, optimization_recipe/FPGA_Accelerated_RISC_V_ISA_Extensions_Optimization_Recipe.md, optimization_recipe/FPGA_RISC-V_ISA_Extensions_Optimization_Recipe.md, benchmark_result/FPGA_Accelerated_RISC_V_ISA_Extensions_Benchmark_Results.md]
pages_created: [synthesis/Chiplet_RISC_V_AI_Landscape.md]

## [2026-06-29] research | Tenstorrent RISC-V AI accelerator hardware software
session_id: 5d4b487e
candidates_evaluated: 0
pages_written: 0
pipeline_rejection_rate: 0%
audit_file: /home/gaohaoze/personal/full_stack/auto_wiki_base/wiki/audit/research_5d4b487e_2026-06-29.json
theme_profile: RISC-V ai accelerator | workflow_first

## [2026-06-29] research | Tenstorrent RISC-V AI accelerator hardware software
session_id: 473e371a
candidates_evaluated: 18
pages_written: 7
pipeline_rejection_rate: 17%
audit_file: /home/gaohaoze/personal/full_stack/auto_wiki_base/wiki/audit/research_473e371a_2026-06-29.json
theme_profile: RISC-V ai accelerator | workflow_first

## [2026-06-29] research | Tenstorrent TT-Metal TT-NN tt-buda Tensix core RISC-V kernel
session_id: 7a0d191c
candidates_evaluated: 17
pages_written: 11
pipeline_rejection_rate: 6%
audit_file: /home/gaohaoze/personal/full_stack/auto_wiki_base/wiki/audit/research_7a0d191c_2026-06-29.json
theme_profile: RISC-V ai accelerator | workflow_first

## [2026-06-29] research | Tenstorrent TT-NN PyBuda tt-buda model inference benchmark p
session_id: dc2ac266
candidates_evaluated: 18
pages_written: 2
pipeline_rejection_rate: 17%
audit_file: /home/gaohaoze/personal/full_stack/auto_wiki_base/wiki/audit/research_dc2ac266_2026-06-29.json
theme_profile: RISC-V ai accelerator | workflow_first

## [2026-06-29] research | Tenstorrent Tensix NoC mesh interconnect tt-forge tt-nn ops 
session_id: e217a61b
candidates_evaluated: 16
pages_written: 7
pipeline_rejection_rate: 25%
audit_file: /home/gaohaoze/personal/full_stack/auto_wiki_base/wiki/audit/research_e217a61b_2026-06-29.json
theme_profile: RISC-V ai accelerator | workflow_first

## [2026-06-29] research | Tenstorrent Galaxy multi-chip Ascalon RISC-V CPU IP LLM infe
session_id: e2416a7d
candidates_evaluated: 19
pages_written: 2
pipeline_rejection_rate: 21%
audit_file: /home/gaohaoze/personal/full_stack/auto_wiki_base/wiki/audit/research_e2416a7d_2026-06-29.json
theme_profile: RISC-V ai accelerator | workflow_first

## [2026-06-29] research | RISC-V AI accelerator MLIR compiler backend TVM IREE Gemmini
session_id: 89f5cc6f
candidates_evaluated: 19
pages_written: 8
pipeline_rejection_rate: 26%
audit_file: /home/gaohaoze/personal/full_stack/auto_wiki_base/wiki/audit/research_89f5cc6f_2026-06-29.json
theme_profile: RISC-V ai accelerator | workflow_first

## [2026-06-29] research | RISC-V MLIR dialect compiler optimization pass AI hardware b
session_id: 659eeab3
candidates_evaluated: 17
pages_written: 6
pipeline_rejection_rate: 24%
audit_file: /home/gaohaoze/personal/full_stack/auto_wiki_base/wiki/audit/research_659eeab3_2026-06-29.json
theme_profile: RISC-V ai accelerator | workflow_first

## [2026-06-29] research | RISC-V RVV Zve matrix extension P-extension custom ISA SIMD 
session_id: 4e65adaa
candidates_evaluated: 16
pages_written: 11
pipeline_rejection_rate: 6%
audit_file: /home/gaohaoze/personal/full_stack/auto_wiki_base/wiki/audit/research_4e65adaa_2026-06-29.json
theme_profile: RISC-V ai accelerator | workflow_first

## [2026-06-29] research | SiFive Intelligence X390 P870 XuanTie C910 RVV inference edg
session_id: 09cb5503
candidates_evaluated: 18
pages_written: 7
pipeline_rejection_rate: 50%
audit_file: /home/gaohaoze/personal/full_stack/auto_wiki_base/wiki/audit/research_09cb5503_2026-06-29.json
theme_profile: RISC-V ai accelerator | workflow_first

## [2026-06-29] research | T-Head AME xtheadmatmul matrix engine ISA register tile SHL 
session_id: c60775a1
candidates_evaluated: 20
pages_written: 5
pipeline_rejection_rate: 15%
audit_file: /home/gaohaoze/personal/full_stack/auto_wiki_base/wiki/audit/research_c60775a1_2026-06-29.json
theme_profile: RISC-V ai accelerator | workflow_first

## [2026-06-29] research | RVV GEMV decode LLM INT4 INT8 dequantize vector load KV cach
session_id: 23539621
candidates_evaluated: 19
pages_written: 8
pipeline_rejection_rate: 16%
audit_file: /home/gaohaoze/personal/full_stack/auto_wiki_base/wiki/audit/research_23539621_2026-06-29.json
theme_profile: RISC-V ai accelerator | workflow_first

## [2026-06-29] research | RISC-V multi-core vector barrier DMA double buffer scratchpa
session_id: 648eb276
candidates_evaluated: 14
pages_written: 10
pipeline_rejection_rate: 14%
audit_file: /home/gaohaoze/personal/full_stack/auto_wiki_base/wiki/audit/research_648eb276_2026-06-29.json
theme_profile: RISC-V ai accelerator | workflow_first

## [2026-06-29] ingest | sessions 10-12 — XuanTie hardware, T-SAR/I-LLM, multi-PE roofline
pages_created: [XuanTie_C908 (entity+hw), XuanTie_C930 (entity+hw), XuanTie_C910_ICE_SoC, Xuantie_C920_C907_R910, TVM_CSINN2_Integration_Optimization_Recipe, T-SAR_In_Place_SIMD_ALU_Reorganization, T-SAR_Benchmark_Results, I-LLM_Integer_Only_LLM_Optimization, RISC-V_Vector_Tests_Generator, SpacemiT_Key_Stone_K1, SpacemiT_KeyStone_K1, SpacemiT_K1, Milk-V_Jupiter2, PMU_Roofline_Analysis_RISCV, Ara_Vector_Processor, Ara_Microarchitectural_Co_Optimization, Ara_Microarchitectural_Co_Optimization_Benchmark_Results, FeNN_DMA_RISC_V_SoC, RVV-Lite, TeraPool_1024_Core_Cluster, TeraPool_Barrier_Synchronization_Benchmark_Results, BitNet_RISCV_Multicore]
pages_updated: []
pages_deferred: []
cold_start: false

## [2026-06-29] query_synthesis | Kernel Dispatch Decision Tree for RVV+AME
source_query: agentic kernel optimization — when to use AME vs RVV vs scalar on RISC-V multi-PE chip
pages_created: [synthesis/Kernel_Dispatch_Decision_Tree_RVV_AME.md]

## [2026-06-29] research | arxiv T-Head XuanTie AME matrix engine xtheadmatmul GEMM acc
session_id: 9896a8ab
candidates_evaluated: 8
pages_written: 3
pipeline_rejection_rate: 50%
audit_file: /home/gaohaoze/personal/full_stack/auto_wiki_base/wiki/audit/research_9896a8ab_2026-06-29.json
theme_profile: RISC-V ai accelerator | workflow_first

## [2026-06-29] research | github SHL CSINN2 AME kernel xtheadmatmul T-Head matrix inst
session_id: 98f43cf1
candidates_evaluated: 6
pages_written: 2
pipeline_rejection_rate: 17%
audit_file: /home/gaohaoze/personal/full_stack/auto_wiki_base/wiki/audit/research_98f43cf1_2026-06-29.json
theme_profile: RISC-V ai accelerator | workflow_first

## [2026-06-29] research | XuanTie C930 server chip AME matrix engine INT8 throughput A
session_id: e36ec430
candidates_evaluated: 6
pages_written: 2
pipeline_rejection_rate: 0%
audit_file: /home/gaohaoze/personal/full_stack/auto_wiki_base/wiki/audit/research_e36ec430_2026-06-29.json
theme_profile: RISC-V ai accelerator | workflow_first

## [2026-06-29] research | arxiv.org RISC-V matrix extension benchmark performance eval
session_id: e551970d
candidates_evaluated: 0
pages_written: 0
pipeline_rejection_rate: 0%
audit_file: /home/gaohaoze/personal/full_stack/auto_wiki_base/wiki/audit/research_e551970d_2026-06-29.json
theme_profile: RISC-V ai accelerator | workflow_first

## [2026-06-29] research | arxiv Quadrilatero RISC-V matrix coprocessor edge 2504.07565
session_id: cb22d7ee
candidates_evaluated: 0
pages_written: 0
pipeline_rejection_rate: 0%
audit_file: /home/gaohaoze/personal/full_stack/auto_wiki_base/wiki/audit/research_cb22d7ee_2026-06-29.json
theme_profile: RISC-V ai accelerator | workflow_first

## [2026-06-29] ingest | XuanTie AME primary source — sessions 13-15 + manual
pages_created: [RISC-V_Matrix_Extension_Specification, SHL_Library, XuanTie, XuanTie_AME_ISA, SHL_AME_GEMM_Optimization_Recipe, XuanTie_C950, Tenstorrent_Wormhole, Tenstorrent_Blackhole, Quadrilatero_RISC-V_Matrix_Coprocessor, Zero_Stall_MatMul_RISC-V_Cluster, RVV_Portable_Performance_GCC15_LLVM21]
pages_updated: [Kernel_Dispatch_Decision_Tree_RVV_AME (open questions updated with confirmed AME ISA)]
cold_start: false
