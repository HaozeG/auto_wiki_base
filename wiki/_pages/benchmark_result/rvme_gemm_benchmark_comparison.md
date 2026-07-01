---
type: benchmark_result
canonical_name: RVME GEMM benchmark comparison
aliases:
- RVME vs RVV vs Eyeriss vs TPUv1 vs Gemmini
tags:
- risc-v
- benchmark
- gemm
- accelerator-comparison
hardware_targets:
- RVME
- RVV-based vector engine
- Eyeriss
- TPUv1
- Gemmini
- MECLA
- MX
- MACO
workloads:
- Transformer-base (embedding, encoder, decoder, output_layer)
- BERT-base (embedding, encoder, output_layer)
- ResNet-50 (conv1-conv5, im2col-based GEMM)
- MobileNetV2 (depthwise-separable convolution GEMM)
datatypes:
- INT8
- INT32
metrics:
- instruction count reduction
- speedup vs RVV
- peak area efficiency (GOPS/mm^2)
- peak energy efficiency (GOPS/W)
- peak energy-area efficiency (GOPS/W/mm^2)
toolchains:
- extended gem5 simulator
- extended RISC-V GNU toolchain
- SCALE-Sim (used to model competitor accelerators)
evidence_strength: reported
measurement_context:
- RVME and RVV evaluated with extended gem5 simulator, extended RISC-V GNU toolchain,
  matched 256-bit VLEN/RLEN datapath width
- competitor accelerators (Eyeriss, TPUv1, Gemmini) modeled with SCALE-Sim under matched
  DRAM bandwidth assumptions
- RVME synthesized with Synopsys Design Compiler at 28nm; power via Synopsys PrimeTime
  PX + extended McPAT; memory parameters from CACTI
sources:
- raw/sources/RVME_An_Efficient_Matrix_Engine_Design_Based_on_Matrix_Extension_of_RISC-V.pdf
created: 2026-07-01
updated: 2026-07-01
cold_start: true
inbound_links: 1
scorecard:
  novelty_delta: 0.85
  claim_density: 0.9
  self_containedness: 0.85
  bridge_score: 0.6
  hub_potential: 0.55
needs_summary_revision: true
---

# RVME GEMM benchmark comparison

This page reports the benchmark results from the RVME paper (IEEE ICCD 2025) comparing the RVME matrix-engine coprocessor against a RISC-V Vector Extension (RVV)-based vector engine and against six published DNN accelerators (Eyeriss, TPUv1, Gemmini, MECLA, MX, MACO), all measured or modeled under matched or documented configurations rather than vendor marketing claims. Against the RVV baseline (same 256-bit VLEN/RLEN datapath width, RVME using four 8x8 OPAs vs. an 8-lane vector engine consuming the same 16 input elements/cycle), RVME reduces total instruction count by over 21.7x across four representative DNN models (Transformer-base, BERT-base, ResNet-50, MobileNetV2) converted to GEMM via im2col for convolutional layers. Measured end-to-end speedups over RVV range from 7.9x-9.4x for Transformer-base and BERT-base, 8.5x-13.4x for ResNet-50, and up to roughly 6.3x (varying 4.9x-6.3x across depthwise-separable-convolution layers) for MobileNetV2. In area/energy efficiency comparisons using SCALE-Sim-modeled competitor accelerators under matched DRAM bandwidth assumptions across GEMM workloads sized [M,N,K] from 256x256x768 up to 128x2048x512, RVME reaches a peak area efficiency of 586 GOPS/mm^2 and average 527.9 GOPS/mm^2 (over 9.3x higher area efficiency than Eyeriss, 8.8x higher than Gemmini on average, and 17.4x higher than TPUv1 under-utilized on smaller GEMM shapes). RVME's peak energy-area efficiency reaches 1921.4 GOPS/W/mm^2, more than 6x higher than the next-best accelerator in the comparison table.

## Key Claims

- RVME achieves over 21.7x reduction in total instruction count compared to a state-of-the-art RVV-based vector engine, evaluated across Transformer-base, BERT-base, ResNet-50, and MobileNetV2 with matched 256-bit VLEN/RLEN.
- End-to-end speedup over RVV: 7.9x-9.4x (Transformer-base/BERT-base), 8.5x-13.4x (ResNet-50), 4.9x-6.3x (MobileNetV2, varying by depthwise-separable-convolution layer).
- Peak area efficiency of 586 GOPS/mm^2 and average 527.9 GOPS/mm^2 across GEMM workloads sized from 256x256x768 to 128x2048x512, measured against SCALE-Sim models of Eyeriss, TPUv1, Gemmini, and RVME's own RTL-derived numbers.
- RVME shows over 9x higher area efficiency than Eyeriss (attributed to Eyeriss's row-stationary dataflow having poor data reuse on GEMM workloads) and 8.8x higher average area efficiency than Gemmini.
- Table IV cross-accelerator comparison (technology node, frequency, area, peak performance in GOPS, peak area efficiency in GOPS/mm^2, peak energy efficiency in GOPS/W, peak energy-area efficiency in GOPS/W/mm^2): RVME (28nm, 1000MHz, 0.63mm^2, INT8) reports 512 GOPS peak performance, 586(a) GOPS/mm^2 peak area efficiency, 1202.1(a) GOPS/W peak energy efficiency, and 1921.4(a) GOPS/W/mm^2 peak energy-area efficiency, where (a) denotes results obtained from real workloads rather than pure peak-hardware specification; comparators include Eyeriss (65nm, 200MHz, 12.25mm^2, 16b fixed-point, 6.9 GOPS/mm^2), TPUv1 (28nm, 700MHz, 331mm^2, INT8, 245.6 GOPS/mm^2), Gemmini (22nm, 1000MHz, 1.03mm^2, INT8, 497 GOPS/mm^2), MECLA (28nm, 1000MHz, 22.02mm^2, INT8, 636 GOPS/mm^2), MX (12nm, 2500MHz, FP32, 202.4 GOPS/mm^2 at FP16), and MACO (12nm/910MHz 64-core cluster, FP16/32/64, 213.2 GOPS/mm^2 at FP16).
- RVME's peak energy-area efficiency of 1921.4 GOPS/W/mm^2 is reported as more than 6x higher than the next-best accelerator among the compared designs.

## Measurement Context

RVV comparison: RVME and the RVV vector engine baseline are both simulated on an extended gem5 model with an extended RISC-V GNU toolchain, using matched 256-bit VLEN/RLEN so the datapath width is identical (16 input elements/cycle for both). Cross-accelerator comparison: Eyeriss, TPUv1, and Gemmini are modeled with SCALE-Sim under the same DRAM bandwidth setting as RVME, since neither publicly specifies DRAM bandwidth; RVME's own numbers are derived from RTL synthesized with Synopsys Design Compiler at 28nm, with power measured via Synopsys PrimeTime PX and an extended McPAT model, and memory component energy/area parameters from CACTI 6.0.

## Relationships

- [[rvme]]: this benchmark comparison is measured on the RVME hardware design described in that page.

## Sources

- W. Chen, W. Yang, Y. Guo, J. Qiu, R. Wang, J. Jiang, N. Jing, Q. Wang, "RVME: An Efficient Matrix Engine Design Based on Matrix Extension of RISC-V," 2025 IEEE 43rd International Conference on Computer Design (ICCD), pp. 606-609 (Sections IV.A-C, Table III, Table IV, Fig. 6, Fig. 8). raw/sources/RVME_An_Efficient_Matrix_Engine_Design_Based_on_Matrix_Extension_of_RISC-V.pdf.
