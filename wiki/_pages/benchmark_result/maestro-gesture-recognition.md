---
canonical_name: Maestro gesture recognition benchmark
aliases:
- Maestro ultrasound gesture recognition
- Maestro WUS pipeline
subtype: null
tags: []
hardware_targets:
- Maestro
workloads:
- Ultrasound signal processing
- Convolutional Neural Network (CNN)
datatypes:
- FP16
metrics:
- GFLOPS
- GFLOPS/W
- power (mW)
- energy (mJ)
toolchains: []
hardware_versions:
- Maestro SoC, TSMC 65nm
software_versions: []
measurement_method: Evaluated on a wearable ultrasound channel preprocessing and ML-based
  postprocessing pipeline for gesture recognition.
evidence_strength: measured
scorecard:
  novelty_delta: 0.9
  claim_density: 0.7
  self_containedness: 0.9
  bridge_score: 0.5
  hub_potential: 0.3
sources:
- raw/cache/8bd3e6ec105e032d.md
- https://arxiv.org/html/2503.04581v1
source_url: https://arxiv.org/html/2503.04581v1
fetched_at: '2026-07-03T14:44:02.750808+00:00'
type: benchmark_result
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 0
---

# Maestro gesture recognition benchmark

Maestro was evaluated on a wearable ultrasound (US)-based gesture recognition task, encompassing a signal processing pipeline and a Convolutional Neural Network (CNN). The signal processing portion achieved 1.62 GFLOPS at 26.68 GFLOPS/W, while the CNN workload reached 19.52 GFLOPS at 298.03 GFLOPS/W. The end-to-end pipeline consumed 12 mW with an energy consumption of 2.5 mJ per inference, achieving a 5× speedup over a state-of-the-art SoC with a similar mission profile. This benchmark demonstrates the SoC's ability to handle both frequency-domain signal conditioning and deep learning inference within a strict power envelope below 50 mW, making it suitable for wearable ultrasound edge computing applications.

## Key Claims

- Signal processing (ultrasound preprocessing) achieves 1.62 GFLOPS at 26.68 GFLOPS/W.
- CNN inference achieves 19.52 GFLOPS at 298.03 GFLOPS/W.
- Total pipeline power consumption is 12 mW with 2.5 mJ per inference.
- 5× speedup over a state-of-the-art SoC with similar mission profile.

## Measurement Context

- Hardware version: Maestro SoC fabricated in TSMC 65nm.
- Software/toolchain version: Not specified in available source.
- Workload shape: Ultrasound channel preprocessing (signal conditioning) followed by a CNN for gesture classification; exact model and kernel shapes not provided.
- Metric: GFLOPS, GFLOPS/W, power (mW), energy (mJ).
- Method: Measured on a wearable ultrasound channel preprocessing and ML-based postprocessing pipeline; the paper states the pipeline was evaluated on a US-based gesture recognition task.
- Evidence strength: measured

## Relationships

The benchmark results are specific to [[maestro]], the RISC-V SoC with Vector-Tensor Unit and FFT accelerator. The comparison target for the 5× speedup is not explicitly named but shares a similar mission profile; one possible comparison candidate is [[gap9]], a state-of-the-art ultra-low-power RISC-V SoC for edge AI.

## Sources

- https://arxiv.org/html/2503.04581v1
