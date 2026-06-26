---
type: entity
tags: [tinyml, mcu, inference, edge-ai, quantization, benchmark]
sources:
  - https://arxiv.org/abs/2106.07597
  - https://github.com/mlcommons/tiny
  - https://mlcommons.org/benchmarks/inference-tiny/
  - https://arxiv.org/pdf/2505.15622
  - https://arxiv.org/pdf/2303.13569
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

# TinyML and MCU Inference

TinyML refers to the deployment of machine learning inference on microcontroller-class hardware — processors with tens to hundreds of kilobytes of SRAM, typically running at tens to hundreds of MHz, at active power budgets of 1 mW or below. This constraint class sits one to three orders of magnitude below mobile-tier inference (which operates on dedicated NPUs with tens of TOPS and gigabytes of DRAM) and requires fundamentally different model design, quantization, and memory management strategies. The dominant workloads for MCU inference are keyword spotting (KWS), anomaly detection on sensor streams, visual wake words (distinguishing whether a person is present in a low-resolution image), and simple image classification. These tasks are chosen because they are latency-tolerant enough for sub-second inference on modest hardware while being useful for always-on IoT applications such as industrial motor monitoring, wildlife acoustic sensors, and voice-activated consumer devices. INT8 quantization is effectively mandatory: 32-bit floating point operations exceed both the compute and memory capacity of typical MCUs, whereas INT8 reduces model weight storage by 4× and is natively supported by Arm Cortex-M SIMD instructions and dedicated microNPU IP such as the Arm Ethos-U55. Energy efficiency — measured in microjoules per inference — is often the primary engineering constraint rather than raw latency, because MCU-based sensor nodes frequently operate on coin cells or energy harvesting.

## Key Claims

- **MLPerf Tiny benchmark scope**: MLPerf Tiny, defined by MLCommons in collaboration with EEMBC, standardizes four tasks — keyword spotting, visual wake words, image classification, and anomaly detection — and measures accuracy, latency, and energy (in µJ per inference) under a target of less than 1 mW active power, establishing the first systematic comparison across MCU-class AI systems.
- **Energy measurements**: A Syntiant NDP120 submitted to MLPerf Tiny completed keyword spotting inference in approximately 4.3 ms while consuming only 35 µJ per inference at 30 MHz operation, illustrating that specialized always-on inference microcontrollers can achieve two to three orders of magnitude lower energy than general-purpose Cortex-M4/M7 solutions running the same model.
- **CMSIS-NN acceleration**: The Arm CMSIS-NN library provides INT8 kernel implementations for Cortex-M targets; it delivers approximately 3.2× inference speedup over naive C on Cortex-M7 and 2.4× on Cortex-M4, translating to roughly 5× combined speed and energy improvement versus unoptimized baselines.
- **Hardware constraints**: The Arduino Nano 33 BLE Sense — one of the most widely used TinyML development boards — is built on the Nordic nRF52840 SoC with a Cortex-M4F at 64 MHz, 256 KB SRAM, and 1 MB flash; it has been used for keyword spotting, gesture recognition, and anomaly detection on washing machines with reported accuracy near 90%.
- **Quantization impact**: Post-training INT8 quantization reduces model file size by approximately 75% relative to FP32 while maintaining 95%+ task accuracy for typical KWS and image classification models, according to TensorFlow Lite's quantization toolkit documentation; this reduction is necessary to fit models into the 256–512 KB flash budgets common on STM32 and nRF52 class MCUs.
- **STM32 industrial benchmarking**: An STMicroelectronics NUCLEO-U385RG-Q board submitted to MLPerf Tiny achieved over 48 keyword spotting inferences per second while drawing 245 mW, demonstrating that commodity STM32 MCUs with ST's X-CUBE-AI toolkit can meet practical latency targets without custom silicon.

## Relationships

- [[arm_ethos_npu]] — The Arm Ethos-U55 and U65 microNPUs are purpose-built silicon IP for MCU SoCs to accelerate the same TinyML workloads (KWS, anomaly detection) that CMSIS-NN handles in pure software; Ethos-U55 provides up to 480× ML performance uplift relative to a software-only Cortex-M baseline.
- [[fpga_riscv_isa_extension_nn_inference]] — FPGA-based and RISC-V ISA extension approaches offer an alternative hardware substrate for TinyML, enabling custom dataflows not possible with fixed-function microNPU IP; both approaches target the same sub-1-mW inference regime.
- [[int8_fp8_quantization_llm_inference]] — INT8 quantization is the enabling technology for MCU inference; the same post-training quantization and quantization-aware training techniques developed for server-side LLM compression are applied at extreme scale-down to fit models into hundreds of kilobytes.
- [[qualcomm_ai_engine]] — Qualcomm's AI Engine targets the mobile tier (multiple TOPS, LPDDR bandwidth), one to two orders of magnitude above the MCU tier; understanding the full edge AI stack requires spanning both segments.
- [[apple_neural_engine]] — Apple ANE operates in the multi-TOPS mobile regime; it does not target the sub-1-mW MCU class, but the software stack concepts (quantization, operator fusion) originate from the same TinyML research lineage.

## Sources

- MLPerf Tiny Benchmark paper (arXiv 2106.07597): https://arxiv.org/abs/2106.07597
- MLCommons Tiny GitHub repository: https://github.com/mlcommons/tiny
- MLCommons Tiny benchmark results page: https://mlcommons.org/benchmarks/inference-tiny/
- "Benchmarking Energy and Latency in TinyML" (arXiv 2505.15622): https://arxiv.org/pdf/2505.15622
- "TinyML: Tools, Applications, Challenges" survey (arXiv 2303.13569): https://arxiv.org/pdf/2303.13569
- STMicroelectronics MLPerf Tiny submission blog: https://community.st.com/t5/developer-news/latest-mlperf-tiny-benchmark-results-your-stm32-is-ai-ready/ba-p/842111
- Arduino Nano 33 BLE Sense anomaly detection: https://zbotic.in/arduino-nano-33-ble-sense-machine-learning-on-a-tiny-board/
