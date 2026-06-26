# Source: FPGA-Accelerated RISC-V ISA Extensions for Neural Network Inference (arxiv 2511.06955)
Fetched: 2026-06-26

## System Architecture
- Custom RISC-V RV32I core, 5-stage pipeline, deployed on Xilinx PYNQ-Z2 (Zynq-7020)
- Four ISA extensions: FPGA.VCONV (vectorized convolution), FPGA.GEMM (matrix multiplication), FPGA.RELU (activation), FPGA.CUSTOM (extensible)
- Timing closure at 50 MHz; +12.793 ns worst negative slack

## Hardware Resource Utilization
- Base core: 0.43% LUTs, 0.24% flip-flops, 11.4% BRAM
- Accelerator overlay: 9.6% LUTs, 8.2% FFs, 40.7% BRAMs, 43.6% DSPs when active
- Total power: 2.00–2.14 W during operation
- Memory: 64 KB BRAM, AXI4-Lite 32-bit control (1 MB/s), AXI4 data 850 MB/s, DDR3 1.8 GB/s

## Performance Results
- MobileNet V2: 1.81× speedup (491.65 ms → 272.33 ms)
- ResNet-18: 1.76× speedup (921.30 ms → 523.23 ms)
- EfficientNet Lite: 2.49× speedup (430.39 ms → 172.52 ms)
- YOLO Tiny: 2.51× speedup (798.58 ms → 317.64 ms)
- Average: 2.14× speedup across benchmarks

## Individual Extension Performance
- FPGA.VCONV: 7.20× speedup, 60–75% time savings per inference
- FPGA.GEMM: 4.20× speedup, 10–20% time savings
- FPGA.RELU: 3.00× speedup, 5–10% time savings
- FPGA.CUSTOM: 5.80× speedup, 5–15% time savings

## Quantization
- 16-bit fixed-point arithmetic (Q8.8/Q12.4 format)
- ≤0.1% accuracy degradation vs FP32 across all tested models

## Energy Efficiency
- Average 49.1% energy reduction versus ARM Cortex-A9 baseline
- Battery life: 10,000 mAh extends from 12.3 hours to 24.2 hours (96% improvement)

## Performance Gap Analysis
- Theoretical max speedup (Amdahl's Law): 3.39×; actual 2.14× = 63% of theoretical
- DMA overhead: 15%; memory bandwidth limitations: 12%; unaccelerated operations: 10%

## Comparison with Alternatives
| Platform | Power (W) | Latency (ms) | Cost ($) |
|----------|-----------|--------------|----------|
| This work (PYNQ-Z2) | 2.14 | 321 | 129 |
| Google Edge TPU | 2.0 | 185 | 60 |
| Jetson Nano | 10 | 95 | 100 |
| Intel NCS2 | 2.5 | 240 | 70 |

## Target Applications
- Low-frame-rate scenarios tolerating 300–500 ms latency
- Industrial inspection, agricultural sensing, warehouse robotics, remote monitoring

## Limitations
- Single-threaded execution only
- 50 MHz conservative clock (timing margin permits 100+ MHz)
- Feedforward CNNs only (no LSTM/attention)
- Manual per-layer optimization required
