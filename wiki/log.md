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
