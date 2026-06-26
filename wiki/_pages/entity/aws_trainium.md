---
type: entity
tags: [ai-hardware, training, custom-silicon, aws, accelerator]
sources:
  - https://aws.amazon.com/ai/machine-learning/trainium/
  - https://aws.amazon.com/ec2/instance-types/trn2/
  - https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/trainium2.html
  - https://aws.amazon.com/blogs/aws/amazon-ec2-trn2-instances-and-trn2-ultraservers-for-aiml-training-and-inference-is-now-available/
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

# AWS Trainium

AWS Trainium is Amazon Web Services' custom silicon accelerator optimized for large-scale deep learning training, and serves as the training-focused counterpart to AWS Inferentia inference chips. Introduced with Trn1 instances in 2022 and substantially expanded with Trainium2 (Trn2) in 2024, Trainium chips share the NeuronCore architecture and Neuron SDK ecosystem with Inferentia but are sized and interconnected for gradient-heavy distributed training workloads. First-generation Trn1 chips each contain two NeuronCore-v2 engines and interconnect at up to 800 Gbps via second-generation Elastic Fabric Adapter (EFAv2), with Trn1n instances reaching 1600 Gbps for collective communication in large clusters. Trainium2 chips scale to eight NeuronCores each and 96 GiB of HBM per chip at 2.9 TB/s HBM bandwidth, delivering 1.3 petaflops of dense FP8 compute or 5.2 petaflops of sparse FP8 per chip. Chips within a Trn2 instance are connected via NeuronLink in a 2D torus topology at 1 TB/s chip-to-chip bandwidth, enabling tensor and pipeline parallelism across 16 chips without traversing the EFA fabric. The Trn2 UltraServer form factor aggregates 64 Trainium2 chips across four Trn2 instances into a single interconnected unit with 6 TB of total HBM, 185 TB/s of aggregate memory bandwidth, and 12.8 Tbps of EFAv3 for scale-out communication — positioning the UltraServer as a direct competitor to NVIDIA DGX SuperPOD configurations for training very large language models.

## Key Claims

- Each Trainium2 chip contains eight NeuronCores and 96 GiB of HBM with 2.9 TB/s memory bandwidth, delivering 1.3 petaflops of dense FP8 compute and 5.2 petaflops of sparse FP8 compute per chip.
- A single Trn2 instance (16 Trainium2 chips) provides up to 20.8 petaflops of FP8 compute, 1.5 TB of HBM3, and 46 TB/s of aggregate memory bandwidth.
- Trn2 chips interconnect intra-instance via NeuronLink in a 2D torus at 1 TB/s chip-to-chip bandwidth; scale-out uses EFAv3 at 3.2 Tbps per instance.
- The Trn2 UltraServer integrates 64 Trainium2 chips, 512 NeuronCores, 6 TB of HBM, and 185 TB/s of aggregate HBM bandwidth with 12.8 Tbps of EFAv3 networking.
- Trainium2 delivers 4x higher compute speed, 4x more memory bandwidth, and 3x more memory capacity than first-generation Trn1 chips.
- Trn1 instances support up to 16 Trainium chips with up to 800 Gbps EFAv2 (Trn1) or 1600 Gbps EFAv2 (Trn1n) for distributed training collectives.

## Relationships

- [[aws_inferentia]] — Trainium (training) and Inferentia (inference) are paired AWS custom silicon families sharing the NeuronCore microarchitecture, Neuron SDK, and NeuronLink interconnect.
- [[google_tpu]] — Google TPU v4/v5 pods are the primary structural peer: both use proprietary matrix-engine chips arranged in high-bandwidth interconnect topologies for large-scale distributed training.
- [[nvidia_hopper_h100]] — H100 NVLink/NVSwitch clusters are Trainium's primary competitive target for LLM training; Trainium2 UltraServers aim to match H100 DGX configurations at lower cost on AWS.
- [[arm_sme2]] — Graviton-based host CPUs pair with Trainium chips within Trn1/Trn2 instances for data loading, preprocessing, and orchestration tasks outside the NeuronCore compute path.

## Sources

- AWS Trainium product page: https://aws.amazon.com/ai/machine-learning/trainium/
- EC2 Trn2 instance types and specs: https://aws.amazon.com/ec2/instance-types/trn2/
- Trainium2 architecture documentation: https://awsdocs-neuron.readthedocs-hosted.com/en/latest/about-neuron/arch/neuron-hardware/trainium2.html
- Trn2 and UltraServer availability announcement: https://aws.amazon.com/blogs/aws/amazon-ec2-trn2-instances-and-trn2-ultraservers-for-aiml-training-and-inference-is-now-available/
- EC2 Trn1 instance types: https://aws.amazon.com/ec2/instance-types/trn1/
