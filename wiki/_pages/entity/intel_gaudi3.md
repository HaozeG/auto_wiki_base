---
type: entity
tags: [intel, ai-accelerator, data-center, hbm2e, habana]
sources:
  - https://cdrdv2-public.intel.com/817486/gaudi-3-ai-accelerator-white-paper.pdf
  - https://wccftech.com/intel-gaudi-3-ai-accelerator-5nm-128-gb-hbm2e-900w-50-percent-faster-nvidia-h100/
  - https://docs.habana.ai/en/latest/Gaudi_Overview/Gaudi_Architecture.html
  - https://cdrdv2-public.intel.com/845118/gaudi-3-ai-accelerator-30-3-30.pdf
  - https://www.tomshardware.com/pc-components/cpus/intel-details-guadi-3-at-vision-2024-new-ai-accelerator-sampling-to-partners-now-volume-production-in-q3
created: 2026-06-26
updated: 2026-06-26
cold_start: false
inbound_links: 0
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# Intel Gaudi 3

Intel Gaudi 3 is the third-generation AI training and inference accelerator from Intel's Habana Labs division, fabricated on a 5nm process node and released in 2024 with volume production beginning Q3 2024. The accelerator targets the data-center AI market as a direct competitor to NVIDIA H100, with Intel claiming 50% higher throughput and 40% better power efficiency than the H100 for generative AI training workloads. The chip integrates 64 fifth-generation Tensor Processing Cores (TPC) and eight Matrix Math Engines (MME), each MME capable of 64,000 parallel operations per cycle, delivering 1,835 TFLOPS of BF16 compute at 600W TDP in the PCIe HL-338 form factor. Memory subsystem comprises 128 GB of HBM2e across eight HBM sites (8-high stacks of 16 Gb dies) at 3.7 TB/s total bandwidth — 33% more memory than Gaudi 2. Networking is built in: 24 on-chip 200 Gbps RDMA-capable Ethernet ports enable scale-out without external NICs, a key differentiator from NVIDIA's reliance on InfiniBand or NVLink. Intel ships Gaudi 3 as an OAM module (HL-325L, up to 900W) and PCIe card (HL-338, up to 600W), and supports it through the open-source Intel Extension for PyTorch (IPEX) and the Optimum-Habana integration for Hugging Face models.

## Key Claims

- Gaudi 3 delivers 1,835 TFLOPS BF16 at 600W (PCIe HL-338 form factor); the OAM module HL-325L supports up to 900W TDP.
- Memory is 128 GB HBM2e at 3.7 TB/s bandwidth, built from 8 HBM sites each with 8-high 16 Gb stacks — 33% more capacity than Gaudi 2's 96 GB.
- 24 integrated 200 Gbps Ethernet RDMA NICs provide 4.8 Tb/s of on-chip scale-out bandwidth without external networking hardware.
- The compute fabric includes 64 fifth-gen TPCs and 8 MMEs; each MME performs 64,000 parallel operations per cycle for matrix math.
- Manufactured on TSMC 5nm; volume production began Q3 2024 with OEM partners including Supermicro, Dell, and HPE.
- Intel positions Gaudi 3 as 50% faster than NVIDIA H100 on generative AI training and 40% more power-efficient, based on LLM benchmarks published in the Gaudi 3 white paper.
- Software stack is open-source: Intel Extension for PyTorch (IPEX) and Optimum-Habana provide model support without proprietary compiler lock-in, unlike CUDA.

## Relationships

- [[nvidia_hopper_h100]] — Primary competitive target; Intel claims 1.5× training throughput and 1.4× power efficiency versus H100 SXM at comparable workloads.
- [[nvidia_blackwell_b200]] — Successor-generation competitor; Gaudi 3 competes at the H100 tier while Blackwell and Vera Rubin represent the next two generations ahead.
- [[hbm_high_bandwidth_memory]] — Uses HBM2e, an older HBM generation versus H100's HBM3 and Blackwell's HBM3e, contributing to lower per-GB bandwidth than competitors.
- [[intel_amx]] — Intel AMX is the matrix extension in Intel Xeon CPUs; Gaudi 3's MME is the equivalent matrix engine for the dedicated AI accelerator product line.

## Sources

- Intel Gaudi 3 AI Accelerator White Paper (official): https://cdrdv2-public.intel.com/817486/gaudi-3-ai-accelerator-white-paper.pdf
- WCCFTech — Gaudi 3 announcement (5nm, 128 GB, 900W, H100 comparison): https://wccftech.com/intel-gaudi-3-ai-accelerator-5nm-128-gb-hbm2e-900w-50-percent-faster-nvidia-h100/
- Habana/Intel official architecture docs: https://docs.habana.ai/en/latest/Gaudi_Overview/Gaudi_Architecture.html
- Intel Gaudi 3 30-3-30 datasheet: https://cdrdv2-public.intel.com/845118/gaudi-3-ai-accelerator-30-3-30.pdf
- Tom's Hardware — Gaudi 3 Vision 2024 detail and sampling timeline: https://www.tomshardware.com/pc-components/cpus/intel-details-guadi-3-at-vision-2024-new-ai-accelerator-sampling-to-partners-now-volume-production-in-q3
