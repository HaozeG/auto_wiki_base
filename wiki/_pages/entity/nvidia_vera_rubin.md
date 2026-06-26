---
type: entity
tags: [nvidia, gpu, ai-accelerator, data-center, hbm4, nvlink]
sources:
  - https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/
  - https://videocardz.com/newz/nvidia-vera-rubin-nvl72-detailed-72-gpus-36-cpus-260-tb-s-scale-up-bandwidth
  - https://slyd.com/hardware/nvidia-rubin
  - https://www.thundercompute.com/blog/nvidia-rubin-architecture
  - https://www.storagereview.com/news/nvidia-launches-vera-rubin-architecture-at-ces-2026-the-vr-nvl72-rack
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

# NVIDIA Vera Rubin (R100)

NVIDIA Vera Rubin is the successor GPU architecture to Blackwell, comprising the R100 GPU die and Vera CPU, announced at GTC 2025 and launched into full production in June 2026. The R100 GPU features 336 billion transistors, 288 GB of HBM4 memory with 22 TB/s bandwidth, and delivers 50 petaFLOPS of FP4 inference compute — approximately 2.5–5× the FP4 throughput of the B200 Blackwell GPU. The platform is named after astronomer Vera Rubin and dark-matter physicist Vera Cooper Rubin, following NVIDIA's tradition of naming architectures after scientists. The Vera Rubin platform replaces the Grace Blackwell (GB) pairing: the new Vera CPU features 88 custom Olympus cores implementing the Armv9.2 ISA with spatial multithreading (176 threads total), architecturally distinct from the licensed Arm Neoverse cores used in the prior Grace CPU. The NVLink 6 interconnect delivers 3.6 TB/s of scale-up bandwidth per GPU, doubling NVLink 5's 1.8 TB/s on Blackwell. The flagship rack-scale system, the VR NVL72, integrates 72 R100 GPUs and 36 Vera CPUs, with 260 TB/s total scale-up bandwidth via NVLink 6 switching, paired with ConnectX-9 SuperNICs and BlueField-4 DPUs for scale-out.

## Key Claims

- The R100 GPU delivers 50 PFLOPS FP4 inference and 35 PFLOPS FP4 training, compared to approximately 10–20 PFLOPS FP4 on Blackwell B200.
- HBM4 memory capacity is 288 GB per R100 GPU at 22 TB/s bandwidth, up from 192 GB HBM3e at 8 TB/s on the B200 — a 2.75× bandwidth increase.
- NVLink 6 provides 3.6 TB/s of inter-GPU bandwidth per GPU, exactly double NVLink 5's 1.8 TB/s; NVLink-C2C CPU-GPU coherent link delivers 1.8 TB/s.
- The R100 die contains 336 billion transistors, compared to approximately 208 billion for the Blackwell B200 GPU die.
- The Vera CPU packs 88 custom Olympus Armv9.2 cores with spatial multithreading into a single package, replacing the 144-core Grace Neoverse V2 CPU.
- The VR NVL72 rack integrates 72 R100 GPUs and 36 Vera CPUs, achieving 260 TB/s scale-up bandwidth across the rack via NVLink 6 switches.
- Full production began June 2026 with partner availability in H2 2026; GB300 (Blackwell Ultra) with 288 GB HBM3e serves as the bridge product at 15 PFLOPS FP4.

## Relationships

- [[nvidia_blackwell_b200]] — Vera Rubin is the direct successor; R100 replaces B200 with 2.75× HBM bandwidth and 2.5–5× FP4 throughput.
- [[nvidia_hopper_h100]] — Two generations prior; Vera Rubin continues the annual cadence H100→B200→R100.
- [[hbm_high_bandwidth_memory]] — R100 adopts HBM4 (first-generation), enabling 22 TB/s bandwidth versus HBM3e's 8 TB/s.
- [[nvlink_nvswitch]] — NVLink 6 at 3.6 TB/s per GPU is the defining scale-up interconnect of the Vera Rubin platform.
- [[nvidia_tensor_cores]] — Rubin introduces the next-generation Tensor Core supporting FP4 and FP6 in addition to FP8/BF16/FP16.

## Sources

- NVIDIA Technical Blog — Vera Rubin platform overview (six-chip design, NVL72 specs): https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/
- VideoCardz — VR NVL72 specs (72 GPUs, 36 CPUs, 260 TB/s): https://videocardz.com/newz/nvidia-vera-rubin-nvl72-detailed-72-gpus-36-cpus-260-tb-s-scale-up-bandwidth
- Slyd GPU database — R100 specs (288 GB HBM4, 50 PFLOPS FP4): https://slyd.com/hardware/nvidia-rubin
- StorageReview — CES 2026 launch coverage: https://www.storagereview.com/news/nvidia-launches-vera-rubin-architecture-at-ces-2026-the-vr-nvl72-rack
- Thunder Compute — Rubin architecture deep-dive: https://www.thundercompute.com/blog/nvidia-rubin-architecture
