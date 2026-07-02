---
canonical_name: YOLO26 to RKNN Export
aliases:
- YOLO26 RKNN export
- YOLO26 RKNN conversion
- Ultralytics YOLO26 RKNN
subtype: null
tags: []
hardware_targets:
- Rockchip RK3588
- Rockchip RK3566
- Rockchip RK3576
- Rockchip RK3568
- Rockchip RK3562
- Rockchip RK2118
- Rockchip RV1126B
- Rockchip RV1103
- Rockchip RV1106
- Rockchip RV1103B
- Rockchip RV1106B
workloads:
- YOLO26 object detection
datatypes:
- FP16
- INT8
metrics:
- inference latency (ms/im)
- model size (MB)
- mAP50-95(B)
toolchains:
- Ultralytics YOLO (Python)
- rknn-toolkit2
constraints:
- Export host must be x86 Linux (ARM64 not supported for export)
- Model input size defaults to 640 (configurable)
- No separate FP32 export mode; default is FP16 for FP16-capable targets
- INT8 quantization requires calibration data (e.g., COCO8 dataset)
- Detection models only; other tasks not yet supported
evidence_strength: reported
scorecard:
  novelty_delta: 0.9
  claim_density: 0.9
  self_containedness: 0.9
  bridge_score: 0.8
  hub_potential: 0.7
sources:
- raw/cache/4b7115f77243bab6.md
- https://docs.ultralytics.com/integrations/rockchip-rknn
source_url: https://docs.ultralytics.com/integrations/rockchip-rknn
fetched_at: '2026-07-02T07:18:28.238392+00:00'
type: optimization_recipe
created: '2026-07-02'
updated: '2026-07-02'
cold_start: false
inbound_links: 1
needs_summary_revision: false
---

# YOLO26 to RKNN Export

The YOLO26 to RKNN export optimization transforms a standard Ultralytics YOLO26 PyTorch model into the Rockchip Neural Network (RKNN) format, enabling deployment on Rockchip NPU-equipped devices such as the RK3588 and RK3566. The prerequisite for this transformation is an x86 Linux machine with the Ultralytics YOLO Python package installed. The export process consists of loading a YOLO26 model (e.g., yolo26n.pt) and calling model.export(format="rknn", name="<target>", quantize=<precision>). The expected effect is optimized inference performance on Rockchip NPUs, with reduced latency and power consumption compared to CPU inference. Failure modes include runtime version mismatches between the RKNN toolkit and the device's librknnrt.so, which can be resolved by replacing the library file. Measurements of the resulting model size, mAP, and inference time are documented in the corresponding benchmark results.

## Key Claims

- Export is performed on x86 Linux; inference runs on ARM64 Rockchip devices.
- Supported quantization modes: FP16 (default for FP16-capable targets) and INT8 (specified via quantize=8).
- INT8 quantization requires a calibration data YAML file (default is selected automatically if omitted).
- The export supports detection models only at the time of writing; other task types are planned.
- After export, the model can be loaded and run with YOLO("<exported_folder>") directly on the Rockchip device.

## Transformation

- **Prerequisites:** x86 Linux machine; ultralytics package installed; Rockchip device with flashed OS (e.g., Radxa Rock 5B or Zero 3W).
- **Steps:**
  1. Load YOLO26 model: `model = YOLO("yolo26n.pt")`
  2. Export to RKNN: `model.export(format="rknn", name="rk3588", quantize=16)` (FP16) or `model.export(format="rknn", name="rk3588", quantize=8, data="coco8.yaml")` (INT8)
  3. Transfer exported folder to Rockchip device.
  4. Run inference: `model = YOLO("./yolo26n_rknn_model"); results = model("image.jpg")`
- **Expected effect:** optimized NPU inference with low latency and power efficiency.
- **Failure modes:** RKNN runtime version mismatch (fix by replacing /usr/lib/librknnrt.so); export fails on ARM64 host; unsupported model task (detection only).
- **Measurements:** Benchmark results for Radxa Rock 5B (RK3588) are available on the [[yolo26_rknn_rockchip_rk3588_benchmark]] page.

## Relationships

- The target hardware [[rockchip_rk3588]] provides the NPU that benefits from this optimization.
- Benchmark results for this recipe are documented in [[yolo26_rknn_rockchip_rk3588_benchmark]].
- Comparable NPU export workflows exist for [[k230]] (via KPU) and [[allwinner_v853]] (via its NPU toolchain).

## Sources

- https://docs.ultralytics.com/integrations/rockchip-rknn
