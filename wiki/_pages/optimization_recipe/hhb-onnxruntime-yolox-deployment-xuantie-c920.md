---
canonical_name: HHB-onnxruntime YOLOX Deployment on Xuantie C920
aliases:
- YOLOX on LPi4A
- TH1520 YOLOX tutorial
- HHB-onnxruntime YOLOX inference
subtype: null
tags: []
hardware_targets:
- Xuantie C920
workloads:
- YOLOX (object detection)
datatypes: []
metrics: []
toolchains:
- HHB-onnxruntime
- SHL
constraints:
- RISC-V vector extension support on C920
- LPi4A board with TH1520 SoC
- Python 3.11 environment
evidence_strength: reported
scorecard:
  novelty_delta: 0.4
  claim_density: 0.4
  self_containedness: 0.7
  bridge_score: 0.6
  hub_potential: 0.3
sources:
- raw/cache/0fb64a0873f0fa31.md
- https://riscv.org/blog/yolox-for-object-detection/
source_url: https://riscv.org/blog/yolox-for-object-detection/
fetched_at: '2026-07-03T16:32:49.291504+00:00'
type: optimization_recipe
created: '2026-07-03'
updated: '2026-07-03'
cold_start: true
inbound_links: 0
---

# HHB-onnxruntime YOLOX Deployment on Xuantie C920

This optimization recipe describes how to deploy a YOLOX object detection model on a RISC-V development board equipped with a Xuantie C920 CPU, using HHB-onnxruntime—a customized ONNX Runtime backend that leverages the SHL library for RISC-V vector extension instructions. The recipe targets the LicheePi Module 4A (LPi4A) board with a TH1520 SoC. It covers environment setup, model acquisition, source code modification, dependency installation, and execution. No quantitative performance measurements are provided in the source; the optimization claim is that HHB-onnxruntime enables vectorized execution on C920, improving performance over a generic ONNX Runtime. The recipe is self-contained on RISC-V hardware and does not require an x86 host.

## Key Claims

- HHB-onnxruntime supports vector instructions on the Xuantie C920 CPU to optimize execution performance (source: GitHub release description and tutorial).
- SHL (CSI-NN2) provides optimized code for RISC-V vector extension instructions on C920, used as the backend for HHB-onnxruntime.
- The deployment workflow runs entirely on RISC-V development boards without x86 hosts.
- The YOLOX demo can be executed by modifying a single file to set the Python path and using precompiled wheels for RISC-V Python packages.

## Transformation

- Prerequisites:
  - LPi4A development board with TH1520 SoC (Xuantie C920 CPU)
  - Internet connection
  - Python 3.11 installed (default on LPi4A system image)
  - Root access
- Steps:
  1. Update apt sources and install base tools: `apt update && apt install wget git vim python3-pip python3.11-venv`
  2. Install the SHL library: download `c920.tar.gz` from the T-Head CSI-NN2 release, extract, and copy `lib/*` to `/usr/lib/riscv64-linux-gnu/`.
  3. Create and activate a Python virtual environment: `python3 -m venv ort && source /root/ort/bin/activate`
  4. Clone the YOLOX repository and download the `yolox_s.onnx` model.
  5. Modify `demo/ONNXRuntime/onnx_inference.py` to insert `sys.path.insert(0, "../../")` so the YOLOX package is discoverable.
  6. Install precompiled Python packages for RISC-V from `prebuilt_whl` repository (numpy, opencv, Pillow, torch, etc.) using `pip install` for each `.whl`.
  7. Install HHB-onnxruntime wheel: `pip install onnxruntime-1.14.1-cp311-cp311-linux_riscv64.whl`
  8. Execute the demo: `python3 onnx_inference.py -m yolox_s.onnx -i ../../assets/dog.jpg -o outdir -s 0.7 --input_shape 640,640`
- Expected effect: YOLOX inference runs on RISC-V with vectorized computation via HHB-onnxruntime and SHL, potentially higher performance than generic ONNX Runtime on the same hardware (no specific speedup reported).
- Failure modes:
  - Missing or incompatible Python packages: must use precompiled RISC-V wheels (source provides links for Python 3.11).
  - Incorrect library path for SHL: ensure `/usr/lib/riscv64-linux-gnu/` contains the shared objects.
  - Outdated apt packages may cause dependency version conflicts.
- Measurements: None provided in source.

## Relationships

No specific relationship to visible context pages. The recipe links Xuantie C920, SHL, HHB-onnxruntime, and YOLOX, but none of these concepts currently have dedicated pages in the visible wiki context.

## Sources

- https://riscv.org/blog/yolox-for-object-detection/
