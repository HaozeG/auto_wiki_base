---
type: entity
tags: [neuromorphic, spiking-neural-networks, intel-loihi, ibm-northpole, event-driven]
sources:
  - https://www.intel.com/content/www/us/en/research/neuromorphic-computing.html
  - https://doi.org/10.1126/science.adk4117
  - https://doi.org/10.1038/s41586-023-06427-4
  - https://research.ibm.com/blog/northpole-inference-chip
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

# Neuromorphic Computing

Neuromorphic computing is a hardware design paradigm that models computation on the structure and dynamics of biological neural tissue, using spiking neural networks (SNNs) where information is encoded in the timing and rate of discrete electrical pulses (spikes) rather than continuous analog values or clocked binary logic. The key architectural departure from conventional deep learning accelerators is event-driven processing: a neuron circuit only consumes energy when it fires, producing no switching activity — and therefore no dynamic power — during quiescent periods. This contrasts with synchronous digital accelerators, which clock all compute elements every cycle regardless of data activity. Two distinct hardware families have emerged: (1) research-grade neuromorphic chips (Intel Loihi 2, BrainScaleS-2, SpiNNaker2) that faithfully model spiking neuron dynamics including synaptic plasticity, targeting SNN research and edge inference; and (2) IBM NorthPole, which adopts a neuromorphic memory placement philosophy — distributing SRAM across 256 compute cores to eliminate off-chip memory accesses — while executing conventional ReLU-based networks, not SNNs. Intel Loihi 2 (2021, Intel 4 process, 31 mm²) integrates 128 neuro-cores, each hosting up to 8,192 neurons, for a total of approximately 1 million programmable neurons, operating at 120 mW total chip power. IBM NorthPole (2023, TSMC 12 nm, 800 mm²) achieves 22 TOPS/W at INT8 on ResNet-50, a 25× improvement over GPU equivalents at the time of publication according to IBM's Science paper.

## Key Claims

- Intel Loihi 2 contains 128 neuro-cores with up to 1 million total neurons and 120 million synapses, consumes 120 mW at typical workload, and is fabricated on Intel 4 (7 nm-class EUV) process node.
- IBM NorthPole achieves 22 TOPS/W energy efficiency at INT8 precision on ResNet-50 inference, as reported in *Science* (Modha et al., 2023), compared to ~1 TOPS/W for an NVIDIA A100 GPU on the same benchmark — a claimed 25× advantage attributable to zero off-chip memory accesses during inference.
- NorthPole integrates 256 cores each with its own local SRAM, totaling 192 MB of on-chip memory, sufficient to store all weights of ResNet-50 (25 million parameters at INT8 ≈ 25 MB) entirely on-die; this eliminates DRAM latency and bandwidth as execution bottlenecks.
- Spiking neural networks achieve competitive accuracy on static image classification tasks (e.g., ImageNet top-1 ~74% with ANN-to-SNN conversion) but exhibit significant accuracy degradation on sequence modeling and transformer-based LLM inference, where temporal spike encoding introduces latency proportional to the number of timesteps required (typically 32–256× longer than equivalent ANN inference).
- Loihi 2 supports on-chip learning via three-factor Hebbian plasticity rules (spike-timing-dependent plasticity, STDP) without any off-chip gradient computation, enabling continual on-device adaptation at microwatt power levels — a capability absent in all current GPU/TPU platforms.
- Energy-per-synaptic-operation on Loihi 2 is approximately 23 fJ (femtojoules) per spike event, compared to ~900 fJ per MAC on a GPU (A100 at FP16 TDP-normalized), placing neuromorphic hardware at a genuine physical advantage for sparse, spike-coded workloads where activity rates are below ~5% of total synapses per timestep.
- The central limitation for LLM deployment is representational: transformer attention and softmax operations have no natural SNN formulation, and the multi-timestep inference required to accumulate spike-rate codes adds latency that negates energy benefits for dense, non-sparse workloads typical of large language model inference.

## Relationships

- [[nvidia_hopper_h100]]: H100 consumes ~700 W at FP16 throughput of 989 TFLOPS (~1.4 TFLOPS/W); IBM NorthPole's 22 TOPS/W at INT8 reflects a different operating point — TOPS/W comparisons require identical precision and benchmark normalization to be meaningful.
- [[cerebras_wse]]: WSE-3 also pursues on-chip SRAM to eliminate HBM bandwidth bottleneck, arriving at similar architectural motivation (memory locality) as NorthPole via conventional digital logic rather than neuromorphic design.
- [[groq_lpu]]: Groq LPU schedules weight streaming from SRAM to maximize arithmetic utilization; NorthPole instead maps weights statically per-core — both are responses to the memory wall but use different granularity of memory placement.
- [[apple_neural_engine]]: Apple Neural Engine uses event-triggered activation sparsity exploitation in conventional MAC arrays, a partial convergence with neuromorphic principles without adopting full SNN dynamics.
- [[photonic_ai_accelerators]]: Both photonic and neuromorphic paradigms offer energy advantages for sparse or analog workloads but face accuracy-precision tradeoffs (4–6 bit photonic, spike-rate encoding neuromorphic) that limit applicability to transformer-scale dense LLM workloads.

## Sources

- Modha, D.S. et al. "Neural inference at the frontier of energy, space, and time." *Science* 382, 329–335 (2023). https://doi.org/10.1126/science.adk4117
- Orchard, G. et al. "Efficient Neuromorphic Signal Processing with Loihi 2." IEEE SSCS News (2021). https://intel.com/loihi2
- Davies, M. et al. "Loihi: A Neuromorphic Manycore Processor with On-Chip Learning." *IEEE Micro* 38(1), 82–99 (2018). https://doi.org/10.1109/MM.2018.112130359
- Shastri, B.J. et al. "Photonics for artificial intelligence and neuromorphic computing." *Nature Photonics* 15, 102–114 (2021).
- IBM Research NorthPole blog: https://research.ibm.com/blog/northpole-inference-chip
- Pfeiffer, M. & Pfeil, T. "Deep learning with spiking neurons: opportunities and challenges." *Frontiers in Computational Neuroscience* 12, 24 (2018).
