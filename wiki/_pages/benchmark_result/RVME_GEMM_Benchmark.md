---
type: benchmark_result
tags:
  - RISC-V
  - GEMM
  - matrix extension
  - coprocessor
  - benchmark
  - DNN inference
  - area efficiency
sources:
  - raw/sources/RVME_An_Efficient_Matrix_Engine_Design_Based_on_Matrix_Extension_of_RISC-V.pdf
created: 2026-06-29
updated: 2026-06-29
cold_start: false
inbound_links: 0
hardware_targets:
  - RVME (28 nm, 1 GHz, 4×OPA 8×8, RLEN=256-bit)
  - Baseline RVV engine (VLEN=RLEN=256-bit, 8 lanes)
  - Eyeriss (65 nm, 200 MHz)
  - TPUv1 (28 nm, 700 MHz)
  - Gemmini (22 nm, 1 GHz)
workloads:
  - Transformer-base (embedding, encoder, decoder, output_layer)
  - BERT-base (embedding, encoder, output_layer)
  - ResNet-50 (conv1–conv5 via im2col)
  - MobileNetV2 (depthwise-separable convolutions via im2col)
datatypes:
  - INT8 (source), INT32 (accumulation)
metrics:
  - speedup vs RVV
  - instruction count ratio (Matrix/RVV)
  - area efficiency (GOPS/mm²)
  - energy-area efficiency (GOPS/W/mm²)
  - peak performance (GOPS)
toolchains:
  - Extended RISC-V GNU toolchain
  - gem5 full-system simulator (extended with RVME model)
  - Synopsys Design Compiler (28 nm synthesis)
  - McPAT + CACTI (power/area estimation)
  - SCALE-SIM (competitor modeling)
evidence_strength: simulation + RTL synthesis
scorecard:
  novelty_delta: 0.9
  claim_density: 0.95
  self_containedness: 0.9
  bridge_score: 0.8
  hub_potential: 0.75
---

# RVME GEMM Benchmark Results

RVME is a RISC-V Matrix Extension coprocessor (28 nm, 1 GHz) with four 8×8 Outer Product Arrays, benchmarked against a RISC-V RVV-based vector engine and several state-of-the-art DNN accelerators on GEMM workloads derived from Transformer-base, BERT-base, ResNet-50, and MobileNetV2. The evaluation uses a gem5 full-system simulation platform and Synopsys RTL synthesis. All RVV vs RVME comparisons use identical memory configuration (VLEN = RLEN = 256-bit) to isolate ISA and microarchitecture effects.

## Key Claims

- Single `mmacc` instruction performs 64× more MAC operations than a single `vmacc`, yielding a 21.7× reduction in total instruction count across all four DNN models.
- Speedup vs RVV on transformer/attention layers: 7.9×–9.4× for Transformer-base and BERT-base (embedding, encoder, decoder layers).
- Speedup vs RVV on ResNet-50 convolutional layers: 8.5×–13.4× (batch=1, im2col for conv→GEMM).
- Speedup vs RVV on MobileNetV2: 4.9×–6.3× for depthwise-separable layers (small GEMM tiles do not fully utilize OPA and MRF, limiting gains).
- Peak area efficiency: 586 GOPS/mm² (peak), average 527.9 GOPS/mm² across representative workloads (28 nm, 1 GHz, INT8).
- Peak energy-area efficiency: 1921.4 GOPS/W/mm² under real GEMM workloads at 1 GHz, surpassing all compared accelerators by more than 6×.
- RVME vs Eyeriss (65 nm, 200 MHz): 93× higher area efficiency; gap explained by technology scaling (65→28 nm) and Eyeriss's row-stationary dataflow performing poorly on GEMM-shaped workloads.
- RVME vs Gemmini (22 nm, 1 GHz, INT8): 8.8× higher average area efficiency; same technology node; gap attributed to bubble-free OPA execution vs systolic-array pre-load stalls and fixed dataflow in Gemmini.
- RVME vs TPUv1 (28 nm, 700 MHz, INT8, 512 GOPS peak): 17.4× higher average area efficiency; TPUv1 SA cannot always maintain high PE utilization on non-square GEMM tiles.
- Area: 0.63 mm² total (28 nm): matrix cache + L2 = 61.8%, OPAs = 24.4%, MRF = 7%, others = 6.8%.
- Power: 0.377 W average; DRAM = 48.5%, cache = 29.5%, OPAs = 15.8%, MRF = 5.1%.
- Competitor comparison methodology: SCALE-SIM used to model Eyeriss, TPUv1, Gemmini under same DRAM bandwidth as RVME; RVME results from extended gem5 + McPAT/CACTI energy model.

## Relationships

- [[RVME_Matrix_Engine]] — hardware configuration and design details for the benchmarked system.
- [[RISC-V_Matrix_Extension]] — the ISA that RVME implements; benchmark validates the coprocessor model proposed in the RVM spec.
- [[Gemmini_Architecture]] — primary systolic-array comparison target; RVME outperforms by 8.8× in area efficiency at the same node/frequency.
- [[GEMM_with_RISC-V_Vector_Extension]] — the RVV baseline; 21.7× instruction count reduction, 7.9×–13.4× execution speedup.

## Sources

- RVME: An Efficient Matrix Engine Design Based on Matrix Extension of RISC-V (IEEE ICCD 2025, DOI 10.1109/ICCD65941.2025.00092): `raw/sources/RVME_An_Efficient_Matrix_Engine_Design_Based_on_Matrix_Extension_of_RISC-V.pdf`
  - Sec. IV-A: comparison with RVV — speedup (Fig. 6), instruction ratio analysis
  - Sec. IV-B: RTL synthesis area/power breakdown (Fig. 7, Table III)
  - Sec. IV-C: area efficiency comparison vs Eyeriss/TPUv1/Gemmini/MECLA/MX/MACO (Fig. 8, Table IV)
  - Table IV: head-to-head specs for Eyeriss, TPUv1, Gemmini, MECLA, MX, MACO, RVME
