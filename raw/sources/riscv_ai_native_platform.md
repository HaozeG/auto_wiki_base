# Source: RISC-V AI-Native Platform (riscv.org/blog/risc-v-ai-native)
Fetched: 2026-06-26

## Market Metrics
- Global AI processor market: $261.4bn (2025), projected $385.4bn by 2030 at 8.1% CAGR
- Hardware revenue proportion: ~70% of total AI market
- NVIDIA RISC-V deployment (2024): Over 1 billion cores shipped
- Codasip: 2+ billion RISC-V cores shipped

## Core AI Architectural Features
- Scalable vector processing with flexible vector lengths
- Mixed-precision data handling
- 128-bit RISC-V Vector extensions (leveraged by llama.cpp)
- Modular ISA enabling domain-specific customization
- RVA23 profile ratified late 2024; hardware deployments expected 2026

## Matrix Extensions Under Development
- Integrated Matrix Extension (IME)
- Matrix-in-Vector Extension (VME)
- Attached Matrix Extension (AME)
- All focus on high-efficiency matrix operations for transformers and deep learning

## AI Workload Targets
- Neural Processing Units (NPUs) for inference acceleration
- Tensor acceleration engines for matrix multiplications
- Compute-in-Memory (CiM) architectures
- Transformer workloads (GenAI, LLMs, multimodal models)

## Key Vendors
- Andes Technology: DSP, vector, extensibility features
- Codasip: 2+ billion cores shipped
- Semidynamics: Tensor Unit for streaming/sparse operations
- SiFive: edge to enterprise-grade systems
- Tenstorrent: chiplet architectures, 2nm collaboration with LSTC
- Ventana: Veyron family, OCE chiplet standards
- SpacemiT: Muse Book K1 chip, upcoming 64-core VitalStone V100
- XuanTie/Alibaba: C930 server processor
- VRULL: software stack R&D, matrix extensions

## Software Ecosystem
- Red Hat Enterprise Linux 10: developer preview on SiFive HiFive Premier P550
- Canonical Ubuntu 25.10/26.04: targeting RVA23 profile
- NVIDIA announced CUDA port for RVA23
- PyTorch upstream support in development
- llama.cpp fully leverages 128-bit Vector extensions

## Design Philosophy
- Zero-day bring-up: Linux kernel, compilers, and runtime libraries support new AI features immediately upon silicon delivery
- Evidence-driven specification: rigorous quantitative/qualitative justification required for each instruction
- $5 Raspberry Pi Pico 2 entry-level access; DeepComputing RISC-V mainboard for Framework Laptop 13
