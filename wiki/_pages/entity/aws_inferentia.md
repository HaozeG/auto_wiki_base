---
type: entity
tags: [ai-hardware, inference, custom-silicon, aws, accelerator]
sources:
  - https://aws.amazon.com/ai/machine-learning/inferentia/
  - https://aws.amazon.com/ec2/instance-types/inf2/
  - https://awsdocs-neuron.readthedocs-hosted.com/en/latest/general/arch/neuron-hardware/inferentia2.html
  - https://aws.amazon.com/blogs/machine-learning/aws-inferentia2-builds-on-aws-inferentia1-by-delivering-4x-higher-throughput-and-10x-lower-latency/
created: 2026-06-26
updated: 2026-06-26
cold_start: true
inbound_links: 0
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# AWS Inferentia

AWS Inferentia is Amazon Web Services' custom silicon accelerator designed specifically for deep learning inference workloads. First introduced in 2019 (Inferentia/Inf1) and substantially revised in 2023 (Inferentia2/Inf2), Inferentia chips power EC2 Inf1 and Inf2 instance families and serve as the inference-side complement to AWS Trainium training chips. The first-generation chip houses four NeuronCores, each built around a high-performance systolic array matrix-multiply engine paired with a large on-chip scratchpad cache that minimizes external memory access. Inferentia2 advances the design to two NeuronCore-v2 engines per chip, each containing four dedicated sub-engines — Tensor (matrix operations), Vector (batch normalization, pooling), Scalar (element-wise ops such as ReLU), and GP-SIMD (general-purpose SIMD) — enabling heterogeneous computation within a single autonomous core. Memory capacity expands to 32 GB HBM per chip on Inferentia2, four times larger than first-generation, with an aggregate bandwidth of 9.8 TB/s across a full Inf2 instance. The Neuron SDK (compiler, runtime, profiler) targets PyTorch and JAX, compiling models to NeuronCore instruction streams without requiring manual kernel authoring. The chips interconnect within an instance via NeuronLink, a proprietary high-speed fabric, enabling tensor-parallel inference across multiple chips. Inferentia's design philosophy prioritizes low-latency, high-throughput fixed-function inference over the general-purpose programmability of GPUs, accepting narrower operator coverage in exchange for superior cost-per-inference on supported model families.

## Key Claims

- Each AWS Inferentia2 chip delivers up to 190 TFLOPS of FP16 performance and supports FP32, TF32, BF16, FP16, UINT8, and configurable FP8 (cFP8) data types.
- Inf2 instances are powered by up to 12 Inferentia2 chips connected via NeuronLink, providing up to 2.3 petaflops of compute, 384 GB of shared HBM, and 9.8 TB/s of total memory bandwidth.
- Inferentia2 achieves 4x higher throughput and 10x lower latency compared to first-generation Inferentia1 chips on equivalent workloads.
- First-generation Inf1 instances deliver up to 2.3x higher throughput and up to 70% lower cost-per-inference compared to comparable GPU instances for supported models.
- Amazon Alexa migrated its text-to-speech workloads to Inf1 instances, achieving 25% lower end-to-end latency and 30% lower cost versus GPU-based deployment.
- Each NeuronCore-v2 is an autonomous heterogeneous compute unit with dedicated Tensor, Vector, Scalar, and GP-SIMD engines, where the first-generation NeuronCore used a single systolic array design.

## Relationships

- [[aws_trainium]] — Inferentia (inference) and Trainium (training) are paired AWS custom silicon families sharing the NeuronCore architecture and Neuron SDK toolchain.
- [[google_tpu]] — Google's TPU is a structural peer: both are inference/training ASICs built around systolic array matrix engines, deployed as managed cloud services rather than sold as discrete accelerators.
- [[nvidia_hopper_h100]] — H100 GPUs are the primary competitive alternative for inference; Inferentia2 targets 70%+ cost reduction versus GPU instances for throughput-bound workloads.
- [[arm_sme2]] — Graviton-based host CPUs (ARM architecture) pair with Inferentia chips in Inf1/Inf2 instances for pre/post-processing; Inferentia offloads the matrix-heavy inference kernel.

## Sources

- AWS Inferentia product page: https://aws.amazon.com/ai/machine-learning/inferentia/
- EC2 Inf2 instance types: https://aws.amazon.com/ec2/instance-types/inf2/
- Inferentia2 architecture documentation: https://awsdocs-neuron.readthedocs-hosted.com/en/latest/general/arch/neuron-hardware/inferentia2.html
- Inferentia2 vs Inferentia1 blog post: https://aws.amazon.com/blogs/machine-learning/aws-inferentia2-builds-on-aws-inferentia1-by-delivering-4x-higher-throughput-and-10x-lower-latency/
- Alexa Inf1 deployment: https://aws.amazon.com/blogs/aws/majority-of-alexa-now-running-on-faster-more-cost-effective-amazon-ec2-inf1-instances/
