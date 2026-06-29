---
cold_start: true
created: '2026-12-07'
datatypes: []
evidence_strength: reported
hardware_targets:
- Tenstorrent Grayskull e75
- Tenstorrent Grayskull e150
- Tenstorrent Wormhole n150
- Tenstorrent Wormhole n300 (single-chip)
- Tenstorrent Wormhole n300 (dual-chip)
- TT-LoudBox/TT-QuietBox (4 MMIO chip)
- TT-LoudBox/TT-QuietBox (8 chip)
hardware_versions:
- Grayskull e75
- Grayskull e150
- Wormhole n150
- Wormhole n300 (single-chip)
- Wormhole n300 (dual-chip)
- TT-LoudBox/TT-QuietBox (4 MMIO chip)
- TT-LoudBox/TT-QuietBox (8 chip)
inbound_links: 0
measurement_method: End-to-end host-measured performance using benchmark.py, measuring
  time from first input pushed to last output received, post-compile.
metrics:
- sen/s (sentences per second)
- tok/s (tokens per second)
- s/img (seconds per image)
- img/s (images per second)
scorecard:
  bridge_score: 0.8
  claim_density: 0.9
  hub_potential: 0.8
  novelty_delta: 0.9
  self_containedness: 0.9
software_versions:
- TT-Buda (archived)
sources:
- https://github.com/tenstorrent/tt-buda-benchmarks/blob/main/README.md
tags:
- Tenstorrent
- BUDA
- AI
- benchmark
toolchains:
- TT-Buda
type: benchmark_result
updated: '2026-06-29'
workloads:
- BERT-Large
- T5-Large
- FLAN-T5-Large
- Whisper-Small
- Falcon-7B
- Stable Diffusion v1-4
- ResNet50
- VoVNet-V2
- MobileNetV1
- MobileNetV2
- MobileNetV3
- HRNet-V2
- ViT-Base
- DeiT-Base
- YOLOv5-Small
- OpenPose-2D
- U-Net
- Inception-v4
---

# TT-BUDA Benchmark Results

TT-BUDA Benchmarks is a performance measurement repository for AI model inference on Tenstorrent hardware using the TT-BUDA software stack. The benchmark table presents throughput and latency numbers for 18 popular AI models, including BERT-Large, T5-Large, ResNet50, and Stable Diffusion v1-4, across seven Tenstorrent hardware configurations: Grayskull e75, Grayskull e150, Wormhole n150, Wormhole n300 (single-chip and dual-chip), TT-LoudBox/TT-QuietBox (4 MMIO chip and 8 chip). Measurements were obtained using the benchmark.py script, which records end-to-end host time from first input submission to last output reception, post-compilation. The repository is now archived as the BUDA project has been completed; Tenstorrent's current SDK is TT-Metalium.

## Key Claims

- BERT-Large on Grayskull e75: 81 sen/s (batch 64, sequence length 384).
- BERT-Large on Wormhole n150: 118 sen/s (batch 64, sequence length 384).
- ResNet50 on Grayskull e150: 1410 img/s (batch 256, input 3x224x224).
- ResNet50 on Wormhole n150: 2891 img/s (batch 256, input 3x224x224).
- ResNet50 on TT-LoudBox/TT-QuietBox (8 chip): 4711 img/s (batch 256, input 3x224x224).
- Falcon-7B on Wormhole n150: 76 tok/s (batch 32, sequence length 128).
- Stable Diffusion v1-4 on Wormhole n150: 50 s/img (batch 1, 512x512).
- MobileNetV2 on TT-LoudBox/TT-QuietBox (8 chip): 6800 img/s (batch 256, input 3x224x224).

Full performance table:

| Model | Input Size | Batch | Grayskull e75 | Grayskull e150 | Wormhole n150 | Wormhole n300 (single-chip) | Wormhole n300 (dual-chip) | TT-LoudBox/TT-QuietBox (4 MMIO chip) | TT-LoudBox/TT-QuietBox (8 chip) |
|-------|------------|-------|---------------|----------------|---------------|-----------------------------|---------------------------|--------------------------------------|--------------------------------| 
| BERT-Large (sen/s) | 384 | 64 | 81 | 99 | 118 | 103 | x | x | x |
| T5-Large (tok/s) | 64 | 1 | 25 | 30 | 75 | 68 | x | x | x |
| FLAN-T5-Large (tok/s) | 64 | 1 | 9 | 25 | 71 | 52 | x | x | x |
| Whisper-Small (tok/s) | 30s | 1 | 3.4 | 3.7 | 16 | 10 | x | x | x |
| Falcon-7B (tok/s) | 128 | 32 | x | x | 76 | 77 | x | x | x |
| Stable Diffusion v1-4 (s/img) | 512x512 | 1 | x | x | 50 | 50 | x | x | x |
| ResNet50 (img/s) | 3x224x224 | 256 | 1106 | 1410 | 2891 | 1060 | 2000 | 3315 | 4711 |
| VoVNet-V2 (img/s) | 3x224x224 | 128 | 518 | 819 | 1603 | 1197 | 1931 | 2860 | 3294 |
| MobileNetV1 (img/s) | 3x224x224 | 128 | 2468 | 2924 | 3102 | 2338 | 2978 | 4334 | 4347 |
| MobileNetV2 (img/s) | 3x224x224 | 256 | 1141 | 1491 | 2721 | 2439 | 4332 | 4579 | 6800 |
| MobileNetV3 (img/s) | 3x224x224 | 64 | 1192 | 1741 | 1981 | 1670 | 2017 | 2695 | 1688 |
| HRNet-V2 (img/s) | 3x224x224 | 128 | 197 | 233 | 324 | 257 | 269 | 845 | 262 |
| ViT-Base (img/s) | 3x224x224 | 64 | 301 | 363 | 540 | 447 | 546 | 970 | 1311 |
| DeiT-Base (img/s) | 3x224x224 | 64 | 301 | 363 | 539 | 446 | 545 | 973 | 1317 |
| YOLOv5-Small (img/s) | 3x320x320 | 128 | 290 | 232 | 1190 | 1090 | 1435 | x | x |
| OpenPose-2D (img/s) | 3x224x224 | 64 | 828 | 1098 | 1252 | 1204 | 1805 | 1542 | 1438 |
| U-Net (img/s) | 3x256x256 | 48 | 222 | 268 | 490 | 344 | 547 | 455 | x |
| Inception-v4 (img/s) | 3x224x224 | 128 | 371 | 458 | 1061 | 1116 | 1810 | 2795 | 3162 |

## Measurement Context

- Hardware version: Grayskull e75, Grayskull e150, Wormhole n150, Wormhole n300 (single-chip and dual-chip), TT-LoudBox/TT-QuietBox (4 MMIO chip and 8 chip).
- Software/toolchain version: TT-Buda (archived); the benchmark repository is no longer maintained.
- Workload shape: As specified per model (input sizes and batch sizes listed in the table).
- Metric: Throughput in sentences/second (BERT-Large), tokens/second (T5-Large, FLAN-T5-Large, Whisper-Small, Falcon-7B), seconds/image (Stable Diffusion), or images/second (all others).
- Method: End-to-end host-time measurement using the benchmark.py script. The script accepts a model name and optional configuration, runs post-compile, and measures the wall-clock time from the first input submission to the last output reception.
- Evidence strength: reported (data extracted from the archived repository README; original measurements were likely performed by the Tenstorrent team).

## Relationships

- [[Tenstorrent_Grayskull_e150]] – Hardware target showing performance for a mid-range Grayskull card.
- [[Tenstorrent_Wormhole_n300]] – Hardware target covering single and dual-chip configurations.
- (Insufficient context for additional cross-links)

## Sources

- [tt-buda-benchmarks README.md at main](https://github.com/tenstorrent/tt-buda-benchmarks/blob/main/README.md)
