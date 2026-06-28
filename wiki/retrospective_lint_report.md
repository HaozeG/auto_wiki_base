# Retrospective Lint Report — 2026-06-28

85 cold-start pages evaluated via `eval_summary.py` (three-layer pipeline).
7 pages had malformed frontmatter closing delimiters (`---…` instead of `---`) — fixed before eval.

---

## Cleared (36 pages)

All layers passed; no saturation warning. Setting `cold_start: false`.

- `benchmark_result/greenwaves_gap9_mobilenet_v1_benchmark.md`
- `benchmark_result/tinyissimoyolo_object_detection_on_gap9_smart_glasses.md`
- `benchmark_result/tt_loudbox_quietbox_performance.md`
- `entity/SimpleEdgeAiSoC.md`
- `entity/akeana_riscv_cores.md`
- `entity/andes_nx27v_sifive_p870_comparison.md`
- `entity/boom_riscv.md`
- `entity/bouffalo_lab_bl808_bl616.md`
- `entity/building_gap8_applications.md`
- `entity/esperanto_et_soc1.md`
- `entity/gapuino_gap8.md`
- `entity/hailo_model_zoo.md`
- `entity/hwacha_vector_accelerator.md`
- `entity/microchip_polarfire_soc.md`
- `entity/nvidia_riscv_falcon_gsp.md`
- `entity/openhw_cva6.md`
- `entity/openxiangshan_difftest_nemu.md`
- `entity/pybuda.md`
- `entity/revyos.md`
- `entity/risc_v_profiles_rva.md`
- `entity/riscv_automotive_asil.md`
- `entity/riscv_dsc_tinyml_accelerator.md`
- `entity/riscv_sparse_computation.md`
- `entity/shakti_processor.md`
- `entity/sifive_hifive_boards.md`
- `entity/sifive_p870_x390.md`
- `entity/sophgo_sg2044.md`
- `entity/spacemit_k1_soc.md`
- `entity/spacemit_k3.md`
- `entity/tenstorrent_tt_metal.md`
- `entity/wd_swerv_cores.md`
- `entity/xiangshan_riscv.md`
- `entity/ztachip.md`
- `synthesis/riscv_edge_ai_llm_inference.md`
- `synthesis/riscv_open_source_ai_stack.md`
- `synthesis/riscv_vs_arm_edge_ai.md`

---

## Restructure Candidates

### `synthesis/riscv_standardization_software_ecosystem.md`
- **Eval result:** Layer 1 FAIL — `EMPTY_SOURCES: frontmatter 'sources' list is empty or missing`
- **Issue:** Synthesis template does not define a `sources` field, but eval enforces it for all page types. Content is substantive (strong RAG summary, 11 connected entities), yet date-stamped claims (GCC 14 April 2024, RVA23 October 2024, etc.) are uncited in frontmatter.
- **Proposed action:** Add `sources` list to frontmatter citing primary references used in the RAG summary. Do NOT delete — content passes all other checks.

---

## Merge Candidates

Awaiting `lint apply` before executing. Two confirmed duplicate clusters; one deferred.

### Cluster A — TT-Metalium duplicates → merge into `entity/tenstorrent_tt_metalium.md`
- `entity/tt_metalium.md` (inbound=0): First paragraph identical in scope; added as standalone slug without recognising existing page.
- `entity/tt_metalium_framework.md` (inbound=0): Same subject, different slug. Intro: "TT-Metalium is a low-level C++ programming framework…" — verbatim scope overlap with tenstorrent_tt_metalium.
- **Proposed action:** Cherry-pick any unique claims into `tenstorrent_tt_metalium.md`, then delete both. No inbound links to retarget.

### Cluster B — SiFive X390 duplicate → merge into `entity/sifive_p870_x390.md`
- `entity/sifive_intelligence_x390.md` (inbound=0, saturation 80%): Covers X390 alone. `sifive_p870_x390.md` already covers "SiFive Performance P870 / Intelligence X390" as a combined page and passes eval unsaturated.
- **Proposed action:** Merge any unique X390-specific claims into `sifive_p870_x390.md`, delete `sifive_intelligence_x390.md`.

### Cluster C — GreenWaves combined overview (deferred for human)
- `entity/greenwaves_gap8_gap9.md` (saturation 80%, vs greenwaves_gap9, greenwaves_gap9_hardware, greenwaves_autotiler, riscv_vs_arm_edge_ai): Combined GAP8/GAP9 overview that partially duplicates the individual `greenwaves_gap8.md` and `greenwaves_gap9.md` pages.
- **Cannot auto-resolve:** Page may serve as a useful comparison entry point. Human should decide: keep as comparison, merge into gap8/gap9, or restructure as a synthesis page.

---

## Deferred for Human Decision — saturation only

45 pages pass all eval layers but trigger the Layer 3 saturation warning (≥2 BM25 competitors in top-5). In a focused single-domain wiki, topic density naturally produces high BM25 similarity across related-but-distinct entity pages. Saturation alone does not warrant merge or delete. Presented for awareness; no action proposed at `lint apply`.

| Page | Saturation | Competitor sample |
|------|-----------|-------------------|
| `entity/alibaba_xuantie_c910_c920.md` | 80% | alibaba_xuantie_c950, thead_th1520 |
| `entity/alibaba_xuantie_c950.md` | 80% | alibaba_xuantie_c910_c920, tvm_riscv_backend |
| `entity/allwinner_d1.md` | 67% | riscv_vs_arm_edge_ai, bouffalo_lab_bl808_bl616 |
| `entity/andes_ax45mp_nx27v.md` | 80% | andes_nx27v_sifive_p870_comparison, sifive_p870_x390 |
| `entity/ara_vector_processor.md` | 80% | hwacha_vector_accelerator, chipyard_soc_framework |
| `entity/beaglev_ahead.md` | 67% | thead_th1520, allwinner_d1 |
| `entity/canaan_kendryte_k510_k230.md` | 80% | riscv_edge_ai_llm_inference, milkv_pioneer_duo |
| `entity/chips_alliance_governance.md` | 75% | wd_swerv_cores, akeana_riscv_cores |
| `entity/chipyard_soc_framework.md` | 80% | firesim_fpga_simulation, rocket_chip_generator |
| `entity/firesim_fpga_simulation.md` | 67% | chipyard_soc_framework, sifive_hifive_boards |
| `entity/gemmini.md` | 80% | rocket_chip_generator, chipyard_soc_framework |
| `entity/gnu_toolchain_riscv_vector.md` | 67% | riscv_llvm_backend |
| `entity/greenwaves_autotiler.md` | 80% | building_gap8_applications, greenwaves_gap8 |
| `entity/greenwaves_gap8.md` | 80% | greenwaves_gap8_gap9, gapuino_gap8 |
| `entity/greenwaves_gap8_gap9.md` | 80% | greenwaves_gap9_hardware, greenwaves_gap9 |
| `entity/greenwaves_gap9.md` | 80% | greenwaves_gap9_mobilenet_v1_benchmark, greenwaves_gap9_hardware |
| `entity/hailo_8l.md` | 75% | hailo_model_zoo, starfive_jh7110_visionfive2 |
| `entity/iree_riscv.md` | 80% | onnx_runtime_riscv, riscv_open_source_ai_stack |
| `entity/llm_inference_riscv.md` | 80% | riscv_edge_ai_llm_inference, sifive_intelligence_x390 |
| `entity/milkv_pioneer_duo.md` | 75% | sophgo_sg2042, llm_inference_riscv |
| `entity/mlir_riscv_backend.md` | 80% | iree_riscv, riscv_llvm_backend |
| `entity/muriscv_nn.md` | 80% | riscv_edge_ai_llm_inference, tinyml_riscv |
| `entity/nuclei_ux900_n900.md` | 67% | riscv_automotive_asil |
| `entity/onnx_runtime_riscv.md` | 80% | pybuda, sifive_intelligence_x390 |
| `entity/pulp_platform.md` | 80% | riscv_sparse_computation, gapuino_gap8 |
| `entity/qualcomm_riscv_ai.md` | 67% | nvidia_riscv_falcon_gsp, riscv_automotive_asil |
| `entity/risc_v_p_extension.md` | 80% | andes_ax45mp_nx27v, tinyml_riscv |
| `entity/risc_v_vector_extension.md` | 80% | riscv_matrix_extension, riscv_open_source_ai_stack |
| `entity/riscv_llvm_backend.md` | 80% | mlir_riscv_backend, riscv_vs_arm_edge_ai |
| `entity/riscv_matrix_extension.md` | 80% | riscv_sparse_computation, risc_v_vector_extension |
| `entity/riscv_zve_sub_extensions.md` | 80% | tinyml_riscv, muriscv_nn |
| `entity/rocket_chip_generator.md` | 80% | chipyard_soc_framework, gemmini |
| `entity/sifive_intelligence_x280.md` | 80% | sifive_p870_x390, sifive_intelligence_x390 |
| `entity/sophgo_sg2042.md` | 80% | sophgo_sg2044, milkv_pioneer_duo |
| `entity/starfive_jh7110_visionfive2.md` | 75% | canaan_kendryte_k510_k230, beaglev_ahead |
| `entity/tenstorrent.md` | 80% | tenstorrent_tt_ascalon, tenstorrent_tt_metalium |
| `entity/tenstorrent_tensix_architecture.md` | 80% | tenstorrent_tt_metalium, tt_metalium_framework |
| `entity/tenstorrent_tt_ascalon.md` | 80% | riscv_open_ai_acceleration, qualcomm_riscv_ai |
| `entity/tenstorrent_tt_metalium.md` | 80% | tt_metalium_framework, tt_metalium |
| `entity/thead_th1520.md` | 75% | beaglev_ahead, allwinner_d1 |
| `entity/tinyml_riscv.md` | 80% | muriscv_nn, pulp_platform |
| `entity/tt_metalium_framework.md` | 75% | tenstorrent_tt_metalium, tenstorrent |
| `entity/tvm_riscv_backend.md` | 80% | gnu_toolchain_riscv_vector, sifive_intelligence_x390 |
| `entity/ventana_veyron_v2.md` | 80% | qualcomm_riscv_ai, risc_v_vector_extension |
| `hardware_target/greenwaves_gap9_hardware.md` | 80% | greenwaves_gap9, greenwaves_gap8_gap9 |
| `synthesis/riscv_open_ai_acceleration.md` | 80% | tenstorrent, ztachip (expected for synthesis) |

---

## Summary

| Classification | Count |
|---------------|-------|
| CLEARED (cold_start → false) | 36 |
| Restructure — needs sources | 1 |
| Merge — confirmed duplicates (Clusters A + B) | 3 pages |
| Merge — deferred for human (Cluster C) | 1 page |
| Deferred — saturation only, no action proposed | 45 |
| **Total evaluated** | **85** |

Next step: run `lint apply` to execute Cluster A and Cluster B merges and fix the restructure candidate.
