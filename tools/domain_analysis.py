"""Generic domain analysis helpers for research discovery and evaluation."""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


STRUCTURED_FIELDS = (
    "hardware_targets",
    "workloads",
    "datatypes",
    "metrics",
    "toolchains",
    "constraints",
    "evidence_strength",
)

OPTIMIZATION_PAGE_TYPES = (
    "hardware_target",
    "workload_kernel",
    "optimization_recipe",
    "benchmark_result",
)

DEFAULT_PAGE_TYPE_TAXONOMY = {
    "entity": {"description": "Specific entity or concept page"},
    "synthesis": {"description": "Cross-page synthesis or comparison"},
    "source_note": {"description": "Source-grounded note used when a source is useful but not yet page-worthy"},
}

THEME_PAGE_TYPE_LIBRARY = {
    "hardware_target": {
        "description": "Hardware or ISA target with memory hierarchy, accelerator, and compiler details",
        "structured_fields": ["hardware_targets", "toolchains", "constraints"],
    },
    "workload_kernel": {
        "description": "Kernel/workload shape, datatype, layout, sparsity, and baseline implementation",
        "structured_fields": ["workloads", "datatypes", "constraints"],
    },
    "optimization_recipe": {
        "description": "Transformation, prerequisites, expected effect, failure modes, and measurements",
        "structured_fields": ["hardware_targets", "workloads", "datatypes", "metrics", "toolchains"],
    },
    "benchmark_result": {
        "description": "Measured or reported result with hardware/software versions and measurement context",
        "structured_fields": ["hardware_targets", "workloads", "datatypes", "metrics", "toolchains", "evidence_strength"],
    },
    "character": {"description": "Person or character with traits, relationships, and arc"},
    "theme": {"description": "Recurring idea, motif, or interpretive thread"},
    "event": {"description": "Plot, historical, or timeline event"},
    "company": {"description": "Organization participating in a market or ecosystem"},
    "product": {"description": "Product, service, or offering with positioning and capabilities"},
    "market": {"description": "Market segment, customer need, or competitive landscape"},
    "concept": {"description": "Research concept, method, or term"},
    "method": {"description": "Procedure, technique, or experimental approach"},
    "paper": {"description": "Scholarly work with claims, method, evidence, and limitations"},
}


def _profile_page_types(*specialized: str) -> dict[str, dict[str, Any]]:
    page_types = dict(DEFAULT_PAGE_TYPE_TAXONOMY)
    for page_type in specialized:
        page_types[page_type] = THEME_PAGE_TYPE_LIBRARY[page_type]
    return page_types


def _theme_matches(theme_l: str, terms: tuple[str, ...]) -> bool:
    """Word-boundary keyword match, not naive substring containment.

    Plain `term in theme_l` false-positives on short acronym keywords: "soc"
    (system-on-chip) matches inside the ordinary English word "social", so a
    theme like "Victorian literature and its social themes" was misclassified
    into the hardware/architecture_first profile via "soc" before the
    correctly-matching "literature" keyword (checked in a later branch) ever
    got a chance — branches return early, first match wins. Caught live via
    Phase 4c's second-theme verification, not by the existing unit tests
    (which happened not to use a term with this collision)."""
    return any(re.search(rf"\b{re.escape(term)}\b", theme_l) for term in terms)


def propose_theme_profiles(theme: str) -> list[dict[str, Any]]:
    """Return deterministic first-run organization profiles for a broad wiki theme."""
    theme_l = theme.lower()
    base = {
        "theme": theme,
        "relationship_rules": [
            "Prefer explicit bidirectional relationships between specialized pages and their related entity/synthesis pages.",
            "Use synthesis pages for cross-page comparisons, contradictions, and landscape-level claims.",
        ],
        "lint_priorities": [
            "self-contained opening paragraphs",
            "grounded sources for major claims",
            "missing cross-references after enough pages accumulate",
        ],
    }

    if _theme_matches(theme_l, ("risc-v", "riscv", "accelerator", "hardware", "ai chip", "soc")):
        return [
            {
                **base,
                "id": "architecture_first",
                "name": "Architecture-first",
                "description": "Organize around ISA features, cores, accelerators, memory systems, and toolchains.",
                "page_types": _profile_page_types("hardware_target", "benchmark_result"),
                "source_preferences": ["official documentation", "ISA specification", "compiler documentation", "paper"],
                "coverage_priorities": ["ISA/profile coverage", "core and accelerator pages", "memory and toolchain support"],
            },
            {
                **base,
                "id": "workflow_first",
                "name": "Workflow-first",
                "description": "Organize around hardware targets, workload kernels, optimization recipes, and benchmark results.",
                "page_types": _profile_page_types(
                    "hardware_target", "workload_kernel", "optimization_recipe", "benchmark_result"
                ),
                "source_preferences": [
                    "official documentation",
                    "benchmark repository",
                    "compiler documentation",
                    "SDK guide",
                    "paper",
                ],
                "coverage_priorities": [
                    "hardware/software/workload coverage",
                    "measurement context for benchmark results",
                    "optimization prerequisites and failure modes",
                ],
                "lint_priorities": base["lint_priorities"] + [
                    "benchmark measurement context",
                    "hardware-target/workload/recipe relationship coverage",
                ],
            },
            {
                **base,
                "id": "ecosystem_first",
                "name": "Ecosystem-first",
                "description": "Organize around vendors, open-source projects, standards, software stacks, and benchmarks.",
                "page_types": _profile_page_types("company", "product", "hardware_target", "benchmark_result"),
                "source_preferences": ["official documentation", "standards documents", "project repository", "benchmark repository"],
                "coverage_priorities": ["vendors and projects", "standards and software stacks", "benchmark families"],
            },
        ]

    if _theme_matches(theme_l, ("book", "novel", "story", "film", "series", "literature")):
        return [
            {
                **base,
                "id": "character_first",
                "name": "Character-first",
                "description": "Organize around characters, relationships, events, and recurring themes.",
                "page_types": _profile_page_types("character", "event", "theme"),
                "source_preferences": ["primary text", "chapter notes", "critical essay"],
                "coverage_priorities": ["character arcs", "relationship changes", "theme evidence"],
            },
            {
                **base,
                "id": "theme_first",
                "name": "Theme-first",
                "description": "Organize around motifs, claims, passages, and supporting events.",
                "page_types": _profile_page_types("theme", "event", "character"),
                "source_preferences": ["primary text", "annotated edition", "critical essay"],
                "coverage_priorities": ["motifs", "contradictory readings", "passage-level evidence"],
            },
        ]

    if _theme_matches(theme_l, ("competitive", "competitor", "market", "company", "product")):
        return [
            {
                **base,
                "id": "market_first",
                "name": "Market-first",
                "description": "Organize around markets, companies, products, and competitive claims.",
                "page_types": _profile_page_types("market", "company", "product"),
                "source_preferences": ["company documentation", "regulatory filing", "pricing page", "market report"],
                "coverage_priorities": ["market segments", "product positioning", "evidence strength"],
            },
            {
                **base,
                "id": "product_first",
                "name": "Product-first",
                "description": "Organize around products, capabilities, vendors, and comparisons.",
                "page_types": _profile_page_types("product", "company", "market"),
                "source_preferences": ["product documentation", "changelog", "customer case study", "market report"],
                "coverage_priorities": ["capability coverage", "version/date tracking", "competitive comparisons"],
            },
        ]

    return [
        {
            **base,
            "id": "concept_first",
            "name": "Concept-first",
            "description": "Organize around concepts, methods, sources, and synthesis pages.",
            "page_types": _profile_page_types("concept", "method", "paper"),
            "source_preferences": ["paper", "official documentation", "technical report", "dataset"],
            "coverage_priorities": ["core concepts", "method comparisons", "source-grounded claims"],
        },
        {
            **base,
            "id": "source_first",
            "name": "Source-first",
            "description": "Organize around source notes first, then promote stable concepts and syntheses.",
            "page_types": _profile_page_types("paper", "concept", "method"),
            "source_preferences": ["primary source", "paper", "official documentation", "dataset"],
            "coverage_priorities": ["source coverage", "claim extraction", "promotion candidates"],
        },
    ]

DEFAULT_REQUIRED_MEASUREMENT_FIELDS = (
    "hardware_targets",
    "workloads",
    "metrics",
    "measurement_context",
)

_VERSION_RE = re.compile(r"\b(?:v?\d+\.\d+(?:\.\d+)?|[A-Z][A-Za-z0-9_-]*\s+\d+(?:\.\d+)*)\b")
# These four regexes and _DEFAULT_METRIC_TERMS are RISC-V/hardware-benchmark
# shaped defaults. For a non-hardware theme (literature, market/competitive)
# they structurally can't match anything, so extract_evidence() would quietly
# return empty evidence every session instead of adapting. A theme profile can
# override any of them via [research_config].extraction_patterns (a dict of
# field_name -> list of regex fragments, or for "metrics", plain words) set at
# theme setup time; extract_evidence() falls back to these when absent, so the
# current RISC-V wiki's behavior is unchanged (its theme_profile doesn't set
# extraction_patterns).
_MEASUREMENT_RE = re.compile(
    r"\b\d+(?:\.\d+)?\s*(?:"
    r"ns|us|ms|s|cycles?|ops/s|op/s|TOPS|TFLOPS|GFLOPS|GOPS|GB/s|MB/s|"
    r"tokens/s|tok/s|queries/s|qps|fps|%|x|W|mW|MHz|GHz"
    r")\b",
    re.IGNORECASE,
)
_TOOLCHAIN_RE = re.compile(
    r"\b(?:LLVM|Clang|GCC|GNU|MLIR|TVM|IREE|OpenCL|CUDA|ROCm|oneDNN|"
    r"ONNX Runtime|XNNPACK|TFLite|PyTorch|TensorFlow|CMake|Bazel)\b",
    re.IGNORECASE,
)
_WORKLOAD_RE = re.compile(
    r"\b(?:GEMM|matmul|convolution|conv2d|attention|softmax|layernorm|"
    r"FFT|stencil|reduction|scan|sort|embedding|quantization|inference|training)\b",
    re.IGNORECASE,
)
_HARDWARE_RE = re.compile(
    r"\b(?:[A-Z][A-Za-z]+[ -]?\d+[A-Za-z0-9-]*|[A-Z]{2,}[A-Za-z0-9_-]*|"
    r"[A-Za-z]+[A-Za-z-]*(?:CPU|GPU|NPU|TPU|DSP|SoC|FPGA|ASIC))\b"
)
_DEFAULT_METRIC_TERMS = (
    "latency", "throughput", "bandwidth", "speedup", "utilization", "power", "energy", "accuracy",
)


def _pattern_from_config(
    patterns: list[str] | str | None, default: re.Pattern[str], flags: int = re.IGNORECASE
) -> re.Pattern[str]:
    """Compile a theme-supplied list of regex fragments into one alternation
    pattern, falling back to `default` when the theme doesn't supply any.

    Accepts a bare string as a single fragment: [theme_profile].extraction_patterns
    is authored by an LLM (profile-architect subagent) or a human editing
    CLAUDE.md's YAML, and a single string where a one-item list was intended is
    an easy, plausible mistake — without this guard, iterating a raw string
    walks it character-by-character, building a garbage regex that fails to
    compile and silently falls back to `default` with only a log warning."""
    if not patterns:
        return default
    if isinstance(patterns, str):
        patterns = [patterns]
    fragments = [str(p).strip() for p in patterns if str(p).strip()]
    if not fragments:
        return default
    try:
        return re.compile(r"\b(?:" + "|".join(fragments) + r")\b", flags)
    except re.error:
        logging.getLogger(__name__).warning(
            "extraction_patterns: invalid regex in theme config, falling back to default"
        )
        return default


@dataclass
class PageRecord:
    path: Path
    frontmatter: dict[str, Any]
    body: str


def listify(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(v).strip() for v in value if str(v).strip()]
    if isinstance(value, (tuple, set)):
        return [str(v).strip() for v in value if str(v).strip()]
    if isinstance(value, str):
        if not value.strip():
            return []
        return [part.strip() for part in re.split(r"[,;]", value) if part.strip()]
    return [str(value).strip()] if str(value).strip() else []


def parse_page(path: Path) -> PageRecord:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return PageRecord(path=path, frontmatter={}, body="")
    if not text.startswith("---"):
        return PageRecord(path=path, frontmatter={}, body=text)
    end = text.find("---", 3)
    if end == -1:
        return PageRecord(path=path, frontmatter={}, body=text)
    try:
        fm = yaml.safe_load(text[3:end].strip()) or {}
    except yaml.YAMLError:
        fm = {}
    return PageRecord(path=path, frontmatter=fm, body=text[end + 3 :].strip())


def iter_page_records(pages_dir: Path) -> list[PageRecord]:
    if not pages_dir.exists():
        return []
    return [parse_page(path) for path in sorted(pages_dir.rglob("*.md"))]


def _coverage_values(records: list[PageRecord], field: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for rec in records:
        for value in listify(rec.frontmatter.get(field)):
            counts[value] = counts.get(value, 0) + 1
    return dict(sorted(counts.items(), key=lambda item: (-item[1], item[0].lower())))


def build_gap_manifest(pages_dir: Path, config: dict | None = None) -> dict[str, Any]:
    """Summarize structured coverage gaps from existing page frontmatter."""
    config = config or {}
    records = iter_page_records(pages_dir)
    taxonomy = config.get("page_type_taxonomy") or DEFAULT_PAGE_TYPE_TAXONOMY
    fields = list(config.get("structured_fields") or STRUCTURED_FIELDS)
    required_measurement_fields = list(
        config.get("required_measurement_fields") or DEFAULT_REQUIRED_MEASUREMENT_FIELDS
    )

    page_type_counts: dict[str, int] = {}
    missing_structured_fields: dict[str, int] = {field: 0 for field in fields}
    for rec in records:
        page_type = str(rec.frontmatter.get("type") or rec.path.parent.name or "unknown")
        page_type_counts[page_type] = page_type_counts.get(page_type, 0) + 1
        for field in fields:
            if not listify(rec.frontmatter.get(field)):
                missing_structured_fields[field] += 1

    coverage = {field: _coverage_values(records, field) for field in fields}
    # coverage_tracked_page_types/coverage_required_fields default to the
    # RISC-V-shaped OPTIMIZATION_PAGE_TYPES constant for backward compatibility,
    # but a theme profile can declare its own subtypes here (e.g. a literature
    # theme's "character"/"event") — otherwise this whole gap-detection block
    # silently no-ops for any theme whose subtypes don't happen to be named
    # hardware_target/workload_kernel/optimization_recipe/benchmark_result.
    tracked_page_types = config.get("coverage_tracked_page_types") or OPTIMIZATION_PAGE_TYPES
    optimization_counts = {
        page_type: page_type_counts.get(page_type, 0)
        for page_type in taxonomy
        if page_type in tracked_page_types
    }
    required_coverage_fields = config.get("coverage_required_fields") or (
        "hardware_targets", "workloads", "metrics", "toolchains"
    )

    gap_types: list[str] = []
    for page_type, count in optimization_counts.items():
        if count == 0:
            gap_types.append(f"missing_page_type:{page_type}")
    if optimization_counts:
        for field in required_coverage_fields:
            if field in coverage and not coverage[field]:
                gap_types.append(f"missing_structured_field:{field}")

    benchmark_missing_required: list[str] = []
    for rec in records:
        if rec.frontmatter.get("type") != "benchmark_result":
            continue
        missing = _missing_measurement_fields(rec.frontmatter, rec.body, required_measurement_fields)
        if missing:
            benchmark_missing_required.append(f"{rec.path.name}: {', '.join(missing)}")

    return {
        "page_count": len(records),
        "page_type_counts": dict(sorted(page_type_counts.items())),
        "optimization_page_type_counts": optimization_counts,
        "structured_field_coverage": coverage,
        "missing_structured_fields": missing_structured_fields,
        "benchmark_results_missing_required_fields": benchmark_missing_required,
        "gap_types": gap_types,
    }


def build_structured_query(candidate: dict, evidence: dict | None = None) -> str:
    evidence = evidence or {}
    parts: list[str] = []
    for key in ("hardware_names", "workload_names", "metrics", "toolchain_names"):
        parts.extend(listify(evidence.get(key)))
    if not parts:
        parts.extend([
            str(candidate.get("title", "")),
            str(candidate.get("snippet", ""))[:160],
        ])
    seen: set[str] = set()
    unique = []
    for part in parts:
        low = part.lower()
        if low and low not in seen:
            unique.append(part)
            seen.add(low)
    return " ".join(unique[:12]).strip()


def extract_evidence(content: str, candidate: dict | None = None, config: dict | None = None) -> dict[str, Any]:
    """Extract lightweight evidence signals from fetched source text.

    config.extraction_patterns (set via the active theme profile) overrides
    the hardware/benchmark-shaped defaults per field; see the module-level
    note above _MEASUREMENT_RE for why this matters for non-hardware themes.
    """
    candidate = candidate or {}
    config = config or {}
    patterns = config.get("extraction_patterns") or {}
    text = f"{candidate.get('title', '')}\n{candidate.get('snippet', '')}\n{content or ''}"

    measurement_re = _pattern_from_config(patterns.get("measurements"), _MEASUREMENT_RE)
    hardware_re = _pattern_from_config(patterns.get("hardware"), _HARDWARE_RE, flags=0)
    workload_re = _pattern_from_config(patterns.get("workloads"), _WORKLOAD_RE)
    toolchain_re = _pattern_from_config(patterns.get("toolchains"), _TOOLCHAIN_RE)
    metric_terms = [str(m).strip() for m in patterns.get("metrics") or _DEFAULT_METRIC_TERMS if str(m).strip()]

    measurements = sorted(set(measurement_re.findall(text)))
    metric_names = []
    for metric in metric_terms:
        if re.search(rf"\b{re.escape(metric)}\b", text, re.IGNORECASE):
            metric_names.append(metric)

    return {
        "candidate_measurements": measurements[:20],
        "metrics": metric_names[:12],
        "hardware_names": sorted(set(hardware_re.findall(text)))[:20],
        "workload_names": sorted({m.group(0) for m in workload_re.finditer(text)})[:20],
        "toolchain_names": sorted({m.group(0) for m in toolchain_re.finditer(text)})[:20],
        "version_strings": sorted(set(_VERSION_RE.findall(text)))[:20],
    }


def _missing_measurement_fields(
    frontmatter: dict[str, Any],
    body: str,
    required_fields: list[str],
) -> list[str]:
    missing = []
    lower_body = body.lower()
    for field in required_fields:
        if listify(frontmatter.get(field)):
            continue
        if field == "measurement_context":
            context_fields = (
                "measurement_context",
                "measurement_method",
                "benchmark_method",
                "software_versions",
                "hardware_versions",
            )
            if any(listify(frontmatter.get(name)) for name in context_fields):
                continue
            if "measurement context" in lower_body or "measurement method" in lower_body:
                continue
        missing.append(field)
    return missing


def validate_benchmark_claim(
    frontmatter: dict[str, Any],
    body: str = "",
    config: dict | None = None,
) -> dict[str, Any]:
    """Validate generic benchmark evidence quality before writing a benchmark_result page."""
    config = config or {}
    required_fields = list(
        config.get("required_measurement_fields") or DEFAULT_REQUIRED_MEASUREMENT_FIELDS
    )
    missing = _missing_measurement_fields(frontmatter, body, required_fields)
    evidence_strength = listify(frontmatter.get("evidence_strength"))
    if not evidence_strength:
        evidence_strength = ["reported"]
    allowed_strengths = {"measured", "reported", "derived", "marketing"}
    invalid_strengths = [s for s in evidence_strength if s not in allowed_strengths]
    return {
        "pass": not missing and not invalid_strengths,
        "missing_fields": missing,
        "evidence_strength": evidence_strength[0],
        "invalid_evidence_strength": invalid_strengths,
    }


def source_grounded_snippets(content: str, page_type: str, limit: int = 5) -> list[str]:
    """Return short snippets with measurements or transformation terms for eval manifests."""
    if page_type not in {"benchmark_result", "optimization_recipe"}:
        return []
    sentences = re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", content or "").strip())
    signals = ("latency", "throughput", "speedup", "bandwidth", "measured", "benchmark", "optimiz")
    snippets = []
    for sentence in sentences:
        lower = sentence.lower()
        if _MEASUREMENT_RE.search(sentence) or any(sig in lower for sig in signals):
            snippets.append(sentence[:320])
        if len(snippets) >= limit:
            break
    return snippets
