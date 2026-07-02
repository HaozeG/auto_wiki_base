---
canonical_name: Kendryte K210
aliases:
- K210
- Kendryte K210 SoC
- Kendryte K210 processor
subtype: null
tags:
- RISC-V
- AI accelerator
- SoC
- Kendryte
scorecard:
  novelty_delta: 0.7
  claim_density: 0.6
  self_containedness: 0.9
  bridge_score: 0.4
  hub_potential: 0.3
sources:
- raw/cache/13888bfdb880d78c.md
- https://www.hackster.io/news/you-ll-want-to-fetch-this-ai-powered-robot-dog-101c0e2fce26
source_url: https://www.hackster.io/news/you-ll-want-to-fetch-this-ai-powered-robot-dog-101c0e2fce26
fetched_at: '2026-07-02T07:09:30.274513+00:00'
type: entity
created: '2026-07-02'
updated: '2026-07-02'
cold_start: false
inbound_links: 1
needs_summary_revision: false
---

# Kendryte K210

The Kendryte K210 is a RISC-V-based system-on-chip (SoC) developed by Canaan Inc., designed for AIoT applications. It features a dual-core 64-bit RISC-V processor running at 400 MHz, with hardware acceleration for AI tasks enabling up to a trillion operations per second (1 TOPS). The K210 was succeeded by the Kendryte K510, a tri-core RISC-V SoC with a higher clock speed (approximately 800 MHz), up to three trillion operations per second, 1.5 MB of SRAM, and an integrated video processing unit. The K210 gained popularity in edge AI platforms such as the XGO-Mini robotic dog from Luwu Intelligence Technology, where it handles face detection, image recognition, object tracking, and voice recognition.

## Key Claims

- Dual-core 64-bit RISC-V processor operating at 400 MHz.
- Hardware AI acceleration achieving up to 1 trillion operations per second (1 TOPS).
- Powers the XGO-Mini robot dog, supporting face detection, image recognition, object tracking, voice recognition, human posture recognition, dynamic gestures, and traffic sign recognition.
- Successor K510 offers tri-core RISC-V architecture, up to 3 TOPS, 1.5 MB SRAM, and a video processing unit.

## Relationships

- [[k230]]: The K230 is Canaan's next-generation SoC that succeeded the K210/K510 family, integrating dual XuanTie C908 cores and a dedicated KPU.
- [[xuantie_c908]]: A RISC-V processor core from T-Head Semiconductor that powers the K230; the K210 and K510 use different, earlier-generation Canaan core designs but share the same target edge AI application space.
- [[kendryte_k510]]: the direct successor SoC, doubling clock speed and tripling NPU throughput over the K210.

## Sources

- https://www.hackster.io/news/you-ll-want-to-fetch-this-ai-powered-robot-dog-101c0e2fce26
