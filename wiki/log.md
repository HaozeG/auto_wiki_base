# Wiki Log

## [2026-06-26] research | ARM SVE2 SME AI ISA extensions
pages_created: [arm_sve2, arm_sme, arm_sme2, arm_vs_riscv_matrix_isa]
pages_updated: []
cold_start: true



## [2026-06-26] research | RISC-V AI accelerator
session_id: 5b20fd13
candidates_evaluated: 4
pages_written: 0
pipeline_rejection_rate: 0%
audit_file: /home/gaohaoze/personal/full_stack/auto_wiki_base/wiki/audit/research_5b20fd13_2026-06-26.json

## [2026-06-26] ingest | riscv_ai_native_platform.md
pages_created: [risc_v_vector_extension, rva23_profile]
pages_updated: []
pages_deferred: []
cold_start: true

## [2026-06-26] ingest | fpga_riscv_isa_extensions_nn.md + arrow_riscv_vector_ml_inference.md
pages_created: [fpga_riscv_isa_extension_nn_inference]
pages_updated: []
pages_deferred: []
cold_start: true

## [2026-06-26] ingest | tenstorrent_blackhole_riscv.md
pages_created: [tenstorrent_blackhole]
pages_updated: []
pages_deferred: []
cold_start: true

## [2026-06-26] ingest | sifive_intelligence_x280_2ndgen.md
pages_created: [sifive_intelligence_x280]
pages_updated: []
pages_deferred: []
cold_start: true

## [2026-06-26] query_synthesis | RISC-V AI Accelerator Landscape: Architectural Strategies and Ecosystem Convergence
source_query: exploration loop — theme: RISC-V ai accelerator
pages_created: [riscv_ai_accelerator_landscape]

## [2026-06-26] transition | cold_start → mature
pages_at_transition: 6
mean_inbound_links: 3.00

## [2026-06-26] research | RISC-V AI accelerator Gemmini systolic array
session_id: 53abb802
candidates_evaluated: 3
pages_written: 0
pipeline_rejection_rate: 33%
audit_file: /home/gaohaoze/personal/full_stack/auto_wiki_base/wiki/audit/research_53abb802_2026-06-26.json

## [2026-06-26] research | RISC-V AI accelerator Gemmini systolic array
session_id: bb14cfe8
candidates_evaluated: 3
pages_written: 0
pipeline_rejection_rate: 0%
audit_file: /home/gaohaoze/personal/full_stack/auto_wiki_base/wiki/audit/research_bb14cfe8_2026-06-26.json

## [2026-06-26] research | RISC-V AI accelerator Gemmini systolic array
session_id: c4f62b5a
candidates_evaluated: 3
pages_written: 1
pipeline_rejection_rate: 0%
audit_file: /home/gaohaoze/personal/full_stack/auto_wiki_base/wiki/audit/research_c4f62b5a_2026-06-26.json

## [2026-06-26] research | RISC-V AI accelerator Tensix Gemmini matrix extensions archi
session_id: aec1498d
candidates_evaluated: 12
pages_written: 5
pipeline_rejection_rate: 8%
audit_file: /home/gaohaoze/personal/full_stack/auto_wiki_base/wiki/audit/research_aec1498d_2026-06-26.json

## [2026-06-26] research | RISC-V AI accelerator Tensix Gemmini matrix extensions
session_id: aec1498d
candidates_evaluated: 12
pages_written: 5
pipeline_rejection_rate: 8%
new_pages: [gemmini, intel_itanium, tenstorrent, tenstorrent_automotive_ai_accelerator, tenstorrent_blackhole (updated)]
audit_file: wiki/audit/research_aec1498d_2026-06-26.json

## [2026-06-26] lint | retrospective
issues_found: 8
actions_taken:
  - fixed malformed frontmatter delimiters on 5 entity pages (extra dashes → standard ---)
  - set cold_start: false on 9 cleared pages (all except intel_itanium)
deferred_for_human:
  - intel_itanium.md: RESTRUCTURE candidate — synthetic content typed as entity; awaiting lint apply
  - 5 orphan pages (inbound_links: 0): gemmini, intel_itanium, tenstorrent, tenstorrent_automotive_ai_accelerator, riscv_ai_accelerator_landscape — cross-link additions needed
  - 5 pages with null scorecards — spaCy en_core_web_sm not installed; Layer 2 eval skipped
  - graph_stats/frontmatter inbound_links discrepancy flagged in report

## [2026-06-26] lint | apply
actions_taken:
  - restructured intel_itanium.md: trimmed to factual entity stub; moved synthetic "modern parallels" content to new synthesis page
  - created synthesis/epic_vliw_ai_accelerator_legacy.md: EPIC/VLIW Principles in Modern AI Accelerators
  - added [[tenstorrent]] to tenstorrent_blackhole.md and tenstorrent_automotive_ai_accelerator.md (orphan fix)
  - updated tenstorrent.md inbound_links: 0 → 2
  - added [[gemmini]] to riscv_ai_accelerator_landscape.md connected_entities and Connected Pages
  - updated gemmini.md inbound_links: 0 → 1
  - set cold_start: false on intel_itanium.md
  - updated wiki/index.md: new synthesis page, corrected inbound counts
  - set retrospective_lint_done: true in CLAUDE.md
pages_created: [synthesis/epic_vliw_ai_accelerator_legacy]
pages_restructured: [entity/intel_itanium]

## [2026-06-26] research | Tensix architecture Metalium RISC-V matrix extensions IME VM
session_id: d31ae6bf
candidates_evaluated: 12
pages_written: 5
pipeline_rejection_rate: 0%
audit_file: /home/gaohaoze/personal/full_stack/auto_wiki_base/wiki/audit/research_d31ae6bf_2026-06-26.json

## [2026-06-26] research | Metalium tt-metal Tenstorrent software stack RISC-V AI progr
session_id: ece444a8
candidates_evaluated: 12
pages_written: 3
pipeline_rejection_rate: 0%
audit_file: /home/gaohaoze/personal/full_stack/auto_wiki_base/wiki/audit/research_ece444a8_2026-06-26.json

## [2026-06-26] research | ARM SVE2 SME AI ISA extensions
pages_created: [entity/arm_sve2, entity/arm_sme, entity/arm_sme2, synthesis/arm_vs_riscv_matrix_isa]
pages_updated: [wiki/index.md]

## [2026-06-26] research | Intel AMX AVX-512 VNNI Google TPU Apple AMX Neural Engine
pages_created: [entity/intel_amx, entity/intel_avx512_vnni, entity/google_tpu, entity/google_trillium_tpu_v6e, entity/apple_amx, entity/apple_neural_engine]
pages_updated: [wiki/index.md]

## [2026-06-26] research | NVIDIA Tensor Cores H100 Qualcomm Hexagon AI Engine taxonomy
pages_created: [entity/nvidia_tensor_cores, entity/nvidia_hopper_h100, entity/qualcomm_hexagon_dsp, entity/qualcomm_ai_engine, synthesis/ai_accelerator_design_taxonomy]
pages_updated: [wiki/index.md]

## [2026-06-26] research | AMD CDNA MI300X AWS Inferentia Trainium Microsoft Maia Cobalt
pages_created: [entity/amd_cdna_architecture, entity/amd_mi300x, entity/aws_inferentia, entity/aws_trainium, entity/microsoft_azure_maia_100, entity/microsoft_cobalt_100]
pages_updated: [wiki/index.md]

## [2026-06-26] research | Cerebras WSE Groq LPU SambaNova RDU hyperscaler synthesis
pages_created: [entity/cerebras_wse, entity/groq_lpu, entity/sambanova_sn40l, synthesis/hyperscaler_custom_silicon]
pages_updated: [wiki/index.md]

## [2026-06-26] research | Graphcore IPU Etched Sohu HBM NVLink CXL inference synthesis
pages_created: [entity/graphcore_ipu, entity/etched_sohu, entity/hbm_high_bandwidth_memory, entity/nvlink_nvswitch, entity/cxl_compute_express_link, synthesis/inference_accelerator_startups]
pages_updated: [wiki/index.md]

## [2026-06-26] research | Blackwell B200 quantization sparsity chiplets TSMC N3/N2
pages_created: [entity/nvidia_blackwell_b200, entity/int8_fp8_quantization_llm_inference, entity/nvidia_2_4_structured_sparsity, entity/chiplet_architecture_advanced_packaging, entity/tsmc_n3_n2_process_node]
pages_updated: [wiki/index.md]

## [2026-06-26] research | Transformer FlashAttention MoE KV-cache sw-hw co-design synthesis
pages_created: [entity/transformer_architecture, entity/flash_attention, entity/mixture_of_experts_moe_llm, entity/kv_cache_llm_inference, synthesis/software_hardware_codesign_ai]
pages_updated: [wiki/index.md]

## [2026-06-26] research | Speculative decoding model parallelism Triton MLIR TensorRT LLM serving
pages_created: [entity/speculative_decoding_llm_inference, entity/model_parallelism_llm_training_inference, entity/openai_triton, entity/mlir_llvm_ai, entity/onnx_tensorrt, synthesis/llm_serving_stack]
pages_updated: [wiki/index.md]

## [2026-06-26] research | Roofline CUDA photonic neuromorphic datacenter power TCO
pages_created: [entity/roofline_model_arithmetic_intensity, entity/cuda_programming_model, entity/photonic_ai_accelerators, entity/neuromorphic_computing, entity/ai_datacenter_power_and_cooling, entity/ai_hardware_tco]
pages_updated: [wiki/index.md]

## [2026-06-26] research | Vera Rubin MI400 Gaudi3 Ethos TinyML export controls future synthesis
pages_created: [entity/nvidia_vera_rubin, entity/amd_instinct_mi400, entity/intel_gaudi3, entity/arm_ethos_npu, entity/tinyml_mcu_inference, entity/ai_chip_export_controls, synthesis/future_ai_hardware_trajectories]
pages_updated: [wiki/index.md]

## [2026-06-27] lint | retrospective
issues_found: 1
actions_taken: [fixed dangling_ref in intel_amx.md; set cold_start: false on 77 pages]
deferred_for_human: []

## [2026-06-26] research | JAX XLA compiler framework Google AI training TPU JIT compil
session_id: abae4d96
candidates_evaluated: 0
pages_written: 0
pipeline_rejection_rate: 0%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_abae4d96_2026-06-26.json

## [2026-06-26] research | JAX XLA compiler framework Google AI training TPU JIT compil
session_id: 9944cab6
candidates_evaluated: 12
pages_written: 2
pipeline_rejection_rate: 0%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_9944cab6_2026-06-26.json

## [2026-06-26] research | vLLM PagedAttention LLM inference serving SGLang TGI continu
session_id: 8b7bf5de
candidates_evaluated: 12
pages_written: 5
pipeline_rejection_rate: 17%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_8b7bf5de_2026-06-26.json

## [2026-06-26] research | InfiniBand RoCE RDMA AI cluster networking 400G 800G etherne
session_id: 815a25fe
candidates_evaluated: 10
pages_written: 2
pipeline_rejection_rate: 0%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_815a25fe_2026-06-26.json

## [2026-06-26] research | Mamba SSM state space model linear attention RWKV RetNet alt
session_id: 4725ff04
candidates_evaluated: 12
pages_written: 2
pipeline_rejection_rate: 0%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_4725ff04_2026-06-26.json

## [2026-06-26] research | Samsung SK Hynix HBM3E HBM4 DRAM memory bandwidth AI trainin
session_id: 1f981612
candidates_evaluated: 11
pages_written: 4
pipeline_rejection_rate: 0%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_1f981612_2026-06-26.json

## [2026-06-26] research | Intel Ponte Vecchio Falcon Shores GPU architecture Xe HPC
session_id: 1e62638b
candidates_evaluated: 9
pages_written: 4
pipeline_rejection_rate: 0%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_1e62638b_2026-06-26.json

## [2026-06-27] research | AI training data pipeline preprocessing tokenization web cra
session_id: 4ef3792b
candidates_evaluated: 12
pages_written: 5
pipeline_rejection_rate: 0%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_4ef3792b_2026-06-26.json

## [2026-06-27] research | RLHF RLAIF DPO PPO reward model alignment fine-tuning LLM sa
session_id: f2a98ec7
candidates_evaluated: 12
pages_written: 5
pipeline_rejection_rate: 0%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_f2a98ec7_2026-06-27.json

## [2026-06-27] research | LoRA QLoRA parameter efficient fine-tuning PEFT adapter LLM 
session_id: 0e3449fe
candidates_evaluated: 11
pages_written: 2
pipeline_rejection_rate: 0%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_0e3449fe_2026-06-27.json

## [2026-06-27] lint | retrospective
issues_found: 1
actions_taken: [fixed dangling_ref in intel_amx.md (second instance); set cold_start: false on 30 pages; backfilled scorecard scores on 13 pages from audit raw_response; normalized scorecard fields on 10 entity pages (removed extra gap_fill_score/contradiction_potential/weighted_total)]
deferred_for_human: []

## [2026-06-27] lint | routine
issues_found: 3
actions_taken: []
deferred_for_human: [79 entity pages with inbound_links=0 in frontmatter — note: graph_stats.py wikilink-scan shows all 107 pages have inbound wikilinks; frontmatter counter is underreported due to cumulative ingest ordering (pages written before their referrers); | riscv_ai_ecosystem: referenced by 8 entity pages, no dedicated wiki page — root-level risc_v_ai_ecosystem.md confirmed as theme file (empty, intentional); synthesis page or entity page creation deferred to human; | 12 synthesis pages with inbound_links=0 — expected for synthesis pages (they are retrieval targets not link targets); no action needed]

## [2026-06-27] research | Alibaba T-Head Xuantie C910 C920 RISC-V AI SoC TH1520
session_id: fb042b87
candidates_evaluated: 12
pages_written: 3
pipeline_rejection_rate: 0%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_fb042b87_2026-06-27.json

## [2026-06-27] research | SOPHGO SG2042 64-core RISC-V server chip Milk-V Pioneer SG23
session_id: ee728e2f
candidates_evaluated: 11
pages_written: 4
pipeline_rejection_rate: 0%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_ee728e2f_2026-06-27.json

## [2026-06-27] research | OpenXiangShan high-performance RISC-V CPU open-source China
session_id: d4483dbd
candidates_evaluated: 10
pages_written: 2
pipeline_rejection_rate: 0%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_d4483dbd_2026-06-27.json

## [2026-06-27] research | Esperanto ET-SoC-1 RISC-V 1092 minion cores ML inference ASI
session_id: 6977021d
candidates_evaluated: 10
pages_written: 1
pipeline_rejection_rate: 0%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_6977021d_2026-06-27.json

## [2026-06-27] research | Ventana Veyron V1 V2 server RISC-V datacenter CMC interconne
session_id: eae8140a
candidates_evaluated: 10
pages_written: 3
pipeline_rejection_rate: 0%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_eae8140a_2026-06-27.json

## [2026-06-27] research | NVIDIA Falcon RISC-V microcontroller GPU security PMU GSP
session_id: 7b7cb596
candidates_evaluated: 10
pages_written: 1
pipeline_rejection_rate: 0%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_7b7cb596_2026-06-27.json

## [2026-06-27] research | TVM Apache RISC-V RVV vectorization edge deployment BYOC
session_id: 954844ca
candidates_evaluated: 10
pages_written: 2
pipeline_rejection_rate: 0%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_954844ca_2026-06-27.json

## [2026-06-27] research | LLVM RISC-V backend RVV auto-vectorization codegen compiler
session_id: 86a982f2
candidates_evaluated: 10
pages_written: 2
pipeline_rejection_rate: 10%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_86a982f2_2026-06-27.json

## [2026-06-27] research | China RISC-V AI sovereign chip strategy export controls SOPH
session_id: e5573066
candidates_evaluated: 9
pages_written: 3
pipeline_rejection_rate: 0%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_e5573066_2026-06-27.json

## [2026-06-27] research | SpacemiT K1 8-core RVV RISC-V SoC NPU BananaPi F3
session_id: 91d32686
candidates_evaluated: 8
pages_written: 1
pipeline_rejection_rate: 12%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_91d32686_2026-06-27.json

## [2026-06-27] research | RISC-V open-source silicon sovereign AI chip strategy Wester
session_id: 12aa5970
candidates_evaluated: 8
pages_written: 3
pipeline_rejection_rate: 0%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_12aa5970_2026-06-27.json

## [2026-06-27] ingest | RISC-V AI multi-cluster research (8 sessions)
pages_created: [xuantie_c930, alibaba_th1520_soc, alibaba_xuantie_c950, milkv_pioneer, sophgo_sg2380, risc_v_summit_europe_2025, xiangshan_riscv_processor, et_soc_1, ventana_veyron_v1, ventana_veyron_v2, veylon_risc_v_core, risc_v_vector_extension_tvm_optimization, tvm_hybrid_op_riscv_p_extension, lowrisc_riscv_llvm, risc_v_architecture, alibaba_xuantie_c950, spacemit_k1_archlinux, risc_v_2026_disruption, risc_v, FSP_SEC2_FALCON_Relationship (synthesis), china_risc_v_ecosystem_strategy (synthesis)]
pages_updated: [ai_chip_export_controls]
pages_deferred: [andes_technology_nx27v (timeout), western_digital_swerv (timeout), zephyr_rtos_riscv_ml (not attempted), iree_riscv (not attempted)]
cold_start: false
notes: 4 duplicate pages removed (milk-v-pioneer.md, milk_v_pioneer.md, alibaba_th1520_risc_v_soc.md, riscv_vector_extension.md); index cleaned of stale/duplicate rows; 8 orchestrator sessions across China RISC-V AI, Milk-V/SOPHGO, OpenXiangShan, Esperanto/Ventana, NVIDIA Falcon RISC-V, TVM/LLVM toolchain clusters

## [2026-06-27] research | Zephyr RTOS RISC-V TFLite Micro embedded ML real-time infere
session_id: cf732447
candidates_evaluated: 8
pages_written: 1
pipeline_rejection_rate: 0%
audit_file: /mnt/d/OneDrive - ETH Zurich/ETHz/code/auto_wiki_base/wiki/audit/research_cf732447_2026-06-27.json

## [2026-06-27] ingest | RISC-V AI edge research round
pages_created: [andes_andescore_nx27v, western_digital_swerv_core, marvell_octeon_10_dpu, iree_mlir_compiler, zephyr_rtos_tflite_micro, spacemit_k1_soc, riscv_p_extension_dsp, riscv_zvfh_extension, lowrisc_opentitan, starfive_visionfive2_jh7110, riscv_ai_edge_mcu_to_soc (synthesis), open_source_riscv_ai_silicon (synthesis)]
pages_updated: []
pages_deferred: []
cold_start: false
notes: All 10 orchestrators timed out (exit 143); Zephyr orchestrator created microchip_edge_ai_platform.md as tangential page; all 10 entity pages and 2 synthesis pages written manually from provided key facts; mean_inbound_links=0.5929 (140 pages total)
