---
canonical_name: Maestro
aliases:
- Maestro SoC
subtype: null
tags: []
hardware_targets:
- Maestro
toolchains: []
constraints:
- TSMC 65nm CMOS
- peak power <50mW
- FP16 precision for VTU
- multi-precision 16/32-bit FP for FFT
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
type: hardware_target
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 1
---

# Maestro

Maestro is a RISC-V System-on-Chip (SoC) designed for edge processing in wearable ultrasound devices, fabricated in TSMC 65nm CMOS technology. It features a unified Vector-Tensor Unit (VTU) that supports FP16 operations and a multi-precision 16/32-bit floating-point Fast Fourier Transform (FFT) accelerator. The VTU achieves peak performance of 19.8 GFLOPS and 302 GFLOPS/W at FP16, while the FFT accelerator delivers 3.6 GFLOPS and 60.6 GFLOPS/W at FP16. The SoC targets a power envelope below 50 mW to enable un-tethered operation with small batteries and no active cooling, and is intended for wearable ultrasound applications such as gesture recognition and human-machine interfaces.

## Key Claims

- Maestro achieves a peak VTU performance of 19.8 GFLOPS and 302 GFLOPS/W at FP16.
- The FFT accelerator reaches 3.6 GFLOPS and 60.6 GFLOPS/W at FP16.
- On a wearable ultrasound gesture recognition pipeline, the signal processing part runs at 1.62 GFLOPS with 26.68 GFLOPS/W, and the CNN part at 19.52 GFLOPS with 298.03 GFLOPS/W.
- End-to-end pipeline consumes 12 mW and 2.5 mJ per inference, achieving 5× speedup over a state-of-the-art SoC.
- The SoC is fabricated in cost-effective TSMC 65nm technology.

## Optimization-Relevant Details

- ISA/profile: RISC-V with custom vector-tensor extensions (Vector-Tensor Unit).
- Vector/matrix/accelerator support: VTU for FP16 tensor operations; dedicated FFT accelerator for 16/32-bit floating-point frequency-domain processing.
- Memory/cache/TLB/DMA: Not detailed in available source.
- Compiler/toolchain support: Not specified.

## Relationships

Both Maestro and [[gap9]] are ultra-low-power RISC-V SoCs designed for edge AI processing, but Maestro is specialized for wearable ultrasound workloads with a vector-tensor unit and FFT accelerator, whereas GAP9 is a general-purpose PULP processor targeting a broader range of edge AI and DSP tasks. The Maestro paper reports a 5× speedup over an unnamed state-of-the-art SoC with a similar mission profile; GAP9 is a likely candidate for comparison given its role in the edge AI domain.

## Sources

- https://arxiv.org/html/2503.04581v1
