# LLM Wiki — System Design Document

> **For Claude Code**: This document is the authoritative specification for implementing the LLM Wiki system. Implement in the order given in §10. Do not deviate from the schema conventions in §4 — they are load-bearing for the evaluation pipeline.

---

## 1. System Overview

LLM Wiki is a dual-purpose knowledge base system:

- **Human layer**: A browsable, interlinked Obsidian-compatible markdown wiki
- **RAG backend**: A structured source for LLM agent retrieval with self-contained, high-density chunks

The LLM owns the wiki entirely — it creates pages, updates them on ingest, maintains cross-references, and runs lint passes. The human sources, directs, and asks questions. The schema file (`CLAUDE.md`) governs the LLM's behavior as a disciplined wiki maintainer.

**Key design constraint**: the system must be domain-agnostic. No domain-specific configuration at startup. All structure emerges from the data.

---

## 2. Architecture

Three layers, strict separation:

```
raw/          ← Immutable source documents (human-curated, LLM reads only)
wiki/         ← LLM-generated markdown pages (LLM writes, human reads)
CLAUDE.md     ← Schema: page conventions, ingest protocol, scorecard weights
```

Supporting files inside `wiki/`:

```
wiki/
  index.md          ← Content catalog (LLM updates on every ingest)
  log.md            ← Append-only chronological record
  _pages/           ← All wiki pages live here
    entity/         ← Entity/Concept pages
    synthesis/      ← Synthesis pages
```

---

## 3. Directory Structure

```
project-root/
├── CLAUDE.md               ← Schema file (this document's §4 defines its content)
├── raw/                    ← Source documents (never modified by LLM)
│   ├── sources/            ← Articles, papers, notes
│   └── assets/             ← Images, attachments
├── wiki/
│   ├── index.md
│   ├── log.md
│   └── _pages/
│       ├── entity/
│       └── synthesis/
└── tools/                  ← Evaluation scripts (§7)
    ├── eval_summary.py
    ├── graph_stats.py
    └── lint.py
```

---

## 4. Schema File (`CLAUDE.md`)

`CLAUDE.md` is the configuration that governs LLM behavior. It must be present in project root. **Claude Code must generate this file** as part of initialization.

### 4.1 Page Types

The system has exactly two page types. Every wiki page must declare its type in frontmatter.

#### Entity / Concept Page

Purpose: serve RAG direct retrieval. Must be independently meaningful without any other page.

```markdown
---
type: entity
tags: []
sources: []        # list of raw/ filenames that contributed to this page
created: YYYY-MM-DD
updated: YYYY-MM-DD
cold_start: true   # set to false after retrospective lint clears it
inbound_links: 0   # updated by LLM on each ingest pass
scorecard:
  novelty_delta: ~
  claim_density: ~
  self_containedness: ~
  bridge_score: ~
  hub_potential: ~
---

# <Entity Name>

<First paragraph: self-contained definition. Must not reference any other page for meaning.
Must not use: "as mentioned", "see above", "building on", "as established".
Must include: what it is, why it matters, any key numerical parameters if applicable.>

## Key Claims

<Structured list of specific, verifiable claims. Each claim should be a complete sentence
that stands alone. Prefer: numbers, ratios, named systems, concrete comparisons.>

## Relationships

<Explicit links to other pages with one-line description of the relationship.>

## Sources

<Inline citations to raw/ files for each major claim.>
```

**Rejection criteria for Entity pages** (hard stops):
- First paragraph contains a dangling reference pattern (see §7.1)
- Page contains fewer than 3 independently verifiable claims
- No `sources` entry (ungrounded page)

#### Synthesis Page

Purpose: serve human understanding and cross-domain connection. Allows narrative flow.

```markdown
---
type: synthesis
connected_entities: []   # list of entity page filenames this synthesizes
synthesis_status: draft  # draft | active | superseded
created: YYYY-MM-DD
updated: YYYY-MM-DD
cold_start: true
inbound_links: 0
scorecard:
  bridge_score: ~
  contradiction_potential: ~
  cross_domain_connection: ~
---

# <Synthesis Title>

## RAG Summary
<!-- THIS BLOCK IS SPECIAL: 150-250 words, self-contained, written last.
     It is the only block RAG agents retrieve from synthesis pages.
     Requirements:
     - No dangling references of any kind
     - Must name at least 2 connected entities explicitly
     - Must state the core synthetic claim in the first sentence
     - Must mention any active contradictions with existing pages -->

<RAG summary content here>

---

## Full Synthesis

<Narrative content. Cross-references, reasoning chains, contradictions.
Allowed to reference other pages. Should end with an "Open Questions" section.>

## Open Questions

<Explicit list of unresolved issues, contradictions with other pages,
or gaps that new sources could fill. This is input for lint pass.>

## Connected Pages

<Links to all entity pages this synthesis draws from.>
```

**Rejection criteria for Synthesis pages** (hard stops):
- RAG Summary block is absent
- RAG Summary exceeds 250 words or is below 150 words
- RAG Summary contains any dangling reference pattern
- `connected_entities` list is empty (a synthesis over nothing is a duplicate entity page)

### 4.2 Ingest Protocol

On receiving a new source, the LLM follows these steps in order:

**Step 0 — Source-level filter (reads only `index.md`)**

Estimate novelty by scanning the source for entities and concepts, then checking against `index.md` entries. If >80% of the source's content appears already covered by existing pages with `cold_start: false`, log as `skipped` and stop.

```
## [YYYY-MM-DD] skipped | <source filename>
reason: high redundancy with existing pages (<list page names>)
```

**Step 1 — Classify source content**

Determine which type of pages the source primarily warrants:
- (a) Specific, citable factual claims → prioritize Entity pages
- (b) Cross-domain connections, synthesis, argument → prioritize Synthesis pages  
- (c) Both → generate Entity pages first, then one Synthesis page referencing them

**Step 2 — Score each planned page** (see §5 for scorecard)

Apply the appropriate scorecard variant (§5.3) to each planned page before writing.

**Step 3 — Execute writes**

For each page that passes its scorecard threshold:
- Create new page OR update existing page
- Update `inbound_links` count on any page that gains a new reference
- Update `index.md` with new/modified entries
- Append to `log.md`

**Step 4 — Log entry**

```
## [YYYY-MM-DD] ingest | <source filename>
pages_created: [list]
pages_updated: [list]
pages_deferred: [list with reason]
cold_start: true/false
```

### 4.3 Query Protocol

On receiving a query:
1. Read `index.md` to identify candidate pages
2. Read full text of relevant pages
3. Synthesize answer with citations to wiki pages (not raw sources directly)
4. If the answer constitutes a significant synthesis not already captured: create a new Synthesis page and log as `query_synthesis`

### 4.4 Lint Protocol (see §8 for full spec)

```
## [YYYY-MM-DD] lint | <type: routine | retrospective>
issues_found: N
actions_taken: [list]
deferred_for_human: [list with reason]
```

---

## 5. Scorecard Design

### 5.1 Dimensions

#### Structural Value

| Metric | Description | Measurement |
|---|---|---|
| `bridge_score` | Number of distinct page clusters the content connects | Count clusters of linked pages the content spans; 0 = leaf node |
| `hub_potential` | How many existing pages reference concepts this page could anchor | Count `index.md` entries that mention this concept without a dedicated page |
| `retrieval_path_coverage` | Does this page create a shortcut between two previously distant clusters? | Binary: yes/no, determined by checking if content spans pages with no direct link |
| `index_coherence` | Can an agent correctly predict this page's content from its title + summary? | Heuristic: title must contain primary entity name; summary must not introduce new entities not in title |

#### Information Value

| Metric | Description | Measurement |
|---|---|---|
| `novelty_delta` | Fraction of claims not already present in wiki | Estimated by LLM comparison against relevant existing pages |
| `claim_density` | Named entities + measurements per 100 words | Computed by `tools/eval_summary.py` |
| `self_containedness` | No dangling references; all entities defined within the page | Computed by `tools/eval_summary.py` |
| `specificity` | Ratio of concrete values (numbers, named systems, dates) to generic statements | Proxy: measurement density via regex |
| `temporal_stability` | Does content describe current state (unstable) or established facts (stable)? | Low stability → flag for review cadence in frontmatter |

#### Synthesis Value

| Metric | Description | Measurement |
|---|---|---|
| `gap_fill_score` | How many existing pages reference this concept without a dedicated page | Same as `hub_potential` but from demand side |
| `contradiction_potential` | Does content challenge existing claims? | LLM check against existing pages |
| `cross_domain_connection` | Number of distinct topic clusters connected | Same as `bridge_score` but weighted by cluster distance |

### 5.2 Scoring Scale

All metrics: 0.0 – 1.0 float. LLM assigns based on heuristics above. Automated tools (§7) provide objective floor checks that override LLM estimates on `self_containedness` and `claim_density`.

### 5.3 Scorecard Variants

**Cold Start Scorecard** (active while `graph_maturity = false`, see §6):

```yaml
active_dimensions: [novelty_delta, claim_density, self_containedness, temporal_stability]
hard_rejection_threshold: 0.2   # only self_containedness triggers hard rejection
soft_log_threshold: 0.3         # others below this: log but don't reject
```

**Entity Page Scorecard** (active after graph maturity):

```yaml
weights:
  structural: 0.3
  information: 0.5
  synthesis: 0.2
hard_rejection_threshold: 0.2   # any single dimension
acceptance_threshold: 0.4       # weighted average
```

**Synthesis Page Scorecard** (active after graph maturity):

```yaml
weights:
  structural: 0.4
  information: 0.2
  synthesis: 0.4
hard_rejection_threshold: 0.2   # any single dimension
acceptance_threshold: 0.4       # weighted average
additional_hard_requirements:
  - RAG Summary block present and within word bounds
  - connected_entities >= 2
```

---

## 6. Cold Start Protocol

### 6.1 Rationale

Structural metrics (bridge score, hub potential, retrieval path coverage) require an existing graph to be meaningful. During initial wiki population, these metrics would systematically undervalue all content since no clusters exist yet. The system handles this by deferring structural evaluation to a retrospective lint pass triggered by graph maturity.

### 6.2 State Tracking

`CLAUDE.md` maintains a `[system_state]` section updated by the LLM:

```yaml
[system_state]
graph_maturity: false         # flips to true when trigger condition met
cold_start_page_count: 0      # increments on each cold_start page created
mean_inbound_links: 0.0       # recomputed by tools/graph_stats.py on each ingest
retrospective_lint_done: false
```

### 6.3 Maturity Trigger

After each ingest, run:

```bash
python tools/graph_stats.py wiki/_pages/
```

When `mean_inbound_links > 2.0`:
1. Set `graph_maturity: true` in `[system_state]`
2. Log the transition:
   ```
   ## [YYYY-MM-DD] transition | cold_start → mature
   pages_at_transition: N
   mean_inbound_links: X.XX
   ```
3. **Do not immediately run retrospective lint** — log the pending status and wait for explicit `lint retrospective` command

### 6.4 Cold Start Page Behavior

All pages created before maturity carry `cold_start: true` in frontmatter. They participate in normal wiki operations (queries, updates, inbound link counts). They are re-evaluated during retrospective lint.

---

## 7. Evaluation Pipeline

Three-layer pipeline. Each layer is a gate — only pass to the next layer if the current layer passes.

### 7.1 Layer 1: Rule-Based Structural Check (deterministic, <5ms)

Implemented in `tools/eval_summary.py`.

**Dangling reference patterns** (any match = hard fail on self_containedness):

```python
DANGLING_PATTERNS = [
    # Chinese
    r"如前所述", r"上文提到", r"见上节", r"前文", r"如上",
    r"详见.{0,10}页", r"参考.{0,10}章节", r"前述",
    # English  
    r"as (mentioned|discussed|described) (above|earlier|previously)",
    r"see (above|section|chapter|below)",
    r"the (aforementioned|previous|above)",
    r"this (follows from|builds on|extends)",
    r"as (noted|shown|established) (above|earlier)",
    r"refer to (the previous|section|chapter)",
]
```

**Word count checks**:
- Entity page first paragraph: 80–300 words
- Synthesis RAG Summary block: 150–250 words (hard bounds)

**Output**: `{"pass": bool, "violations": [list of matched patterns]}`

### 7.2 Layer 2: Density Metrics (deterministic given fixed spaCy model, ~50ms)

Implemented in `tools/eval_summary.py`. Requires: `pip install spacy && python -m spacy download en_core_web_sm` (or `zh_core_web_sm` for Chinese).

```python
def entity_density(text: str) -> float:
    """Named entities per 100 tokens. Target: > 0.15 for entity pages."""
    doc = nlp(text)
    return (len(doc.ents) / max(len(doc), 1)) * 100

def measurement_density(text: str) -> float:
    """Numeric measurements per 100 words. Target: > 0.05 for technical pages."""
    pattern = r'\d+\.?\d*\s*(ms|GB|TB|TFLOPS|%|ns|MHz|GHz|dB|K|M|B|ops|cycles|tokens)'
    matches = re.findall(pattern, text, re.IGNORECASE)
    words = len(text.split())
    return (len(matches) / max(words, 1)) * 100

def compression_ratio(text: str) -> float:
    """Lower = less redundant. Hard floor: > 0.6 suggests padding."""
    encoded = text.encode('utf-8')
    return len(gzip.compress(encoded)) / len(encoded)
```

**Thresholds** (adjust per domain in `CLAUDE.md`):

```yaml
[eval_thresholds]
entity_page:
  entity_density_min: 0.15
  measurement_density_min: 0.0   # 0 for non-technical domains
  compression_ratio_max: 0.75    # above this = likely padding

synthesis_rag_summary:
  entity_density_min: 0.10
  compression_ratio_max: 0.80
```

**Output**: `{"entity_density": float, "measurement_density": float, "compression_ratio": float, "pass": bool}`

### 7.3 Layer 3: Semantic Coverage (semi-deterministic, ~200ms)

Only triggered when Layer 2 passes but entity_density or compression_ratio is borderline (within 20% of threshold). Implemented in `tools/eval_summary.py`.

Requires: `pip install sentence-transformers`

```python
from sentence_transformers import SentenceTransformer
import numpy as np

MODEL = SentenceTransformer('all-MiniLM-L6-v2')  # pin version for reproducibility

def semantic_coverage(summary: str, full_page: str, threshold: float = 0.65) -> dict:
    """
    For Synthesis pages: checks RAG Summary covers the full page's key claims.
    For Entity pages: checks first paragraph covers the page's scope.
    Returns fraction of full_page sentences with a matching summary sentence.
    """
    full_sentences = [s.strip() for s in re.split(r'[.!?]', full_page) if len(s.strip()) > 20]
    if not full_sentences:
        return {"coverage": 1.0, "pass": True}
    
    summary_emb = MODEL.encode(summary)
    sentence_embs = MODEL.encode(full_sentences)
    
    sims = np.dot(sentence_embs, summary_emb) / (
        np.linalg.norm(sentence_embs, axis=1) * np.linalg.norm(summary_emb) + 1e-8
    )
    coverage = float(np.mean(sims > threshold))
    return {"coverage": coverage, "pass": coverage > 0.5}
```

**If Layer 3 fails**: flag the page with `needs_summary_revision: true` in frontmatter. Do not reject — log for next lint pass. LLM rewrites the RAG Summary block on next lint.

### 7.4 Pipeline Entry Point

```bash
python tools/eval_summary.py <page_path> [--type entity|synthesis] [--verbose]
```

Returns exit code 0 (pass) or 1 (fail with reasons).

---

## 8. Lint Pass Specification

Two types of lint pass:

### 8.1 Routine Lint

Run periodically or on request. Checks:

- Orphan pages (no inbound links after wiki is mature)
- Stale claims (Synthesis pages with `temporal_stability: low` older than 90 days)
- Missing cross-references (entity mentioned in 3+ pages but no dedicated entity page)
- Synthesis pages with empty `open_questions` section
- Pages with `needs_summary_revision: true`
- Contradictions between pages (LLM scan)

Output: append to `log.md`, then list action candidates for human review before executing.

### 8.2 Retrospective Lint (one-time, post-maturity)

Triggered by: `lint retrospective` command after `graph_maturity: true`.

For every page with `cold_start: true`:

1. Run full three-layer evaluation pipeline
2. Compute structural metrics against current graph
3. Classify result:

```
CLEARED     → scorecard passes; set cold_start: false
RESTRUCTURE → entity page should split into entity + synthesis; flag for rewrite
MERGE       → content already covered by mature pages; propose merge target
DELETE      → all metrics below threshold; no salvageable content
```

4. Write candidate report to `wiki/retrospective_lint_report.md`:

```markdown
# Retrospective Lint Report — YYYY-MM-DD

## Cleared (N pages)
...

## Restructure Candidates
- `entity/page_A.md`: bridge_score=0.7, recommend splitting off synthesis layer
  - Proposed synthesis title: ...

## Merge Candidates  
- `entity/page_B.md`: 85% content overlap with `entity/page_C.md`
  - Proposed action: merge into page_C, redirect inbound links

## Delete Candidates
- `entity/page_D.md`: novelty_delta=0.05, self_containedness=FAIL, no unique claims
  - Inbound links: 0

## Deferred for Human Decision
- `synthesis/page_E.md`: contradicts `entity/page_F.md` on claim X — cannot auto-resolve
```

5. **Wait for human confirmation** before executing any MERGE or DELETE actions.
6. After confirmation: execute, update `[system_state].retrospective_lint_done: true`, log completion.

---

## 9. Index and Log Formats

### 9.1 `index.md`

Updated by LLM on every ingest. Structure:

```markdown
# Wiki Index

Last updated: YYYY-MM-DD | Pages: N | Sources: M

## Entity Pages

| Page | Summary | Tags | Sources | Inbound |
|------|---------|------|---------|---------|
| [page_name](entity/page_name.md) | One-line summary | tag1, tag2 | 3 | 5 |

## Synthesis Pages

| Page | Connected Entities | Status | Inbound |
|------|--------------------|--------|---------|
| [synth_name](synthesis/synth_name.md) | entity_a, entity_b | active | 2 |

## Concept Index

Flat list of all concepts mentioned across pages (with or without dedicated pages):
- **ConceptName**: mentioned in [page_a](entity/page_a.md), [page_b](synthesis/page_b.md) — *no dedicated page*
- **ConceptName2**: → [page_c](entity/page_c.md)
```

### 9.2 `log.md`

Append-only. Each entry starts with a parseable prefix:

```
## [YYYY-MM-DD] <type> | <title>
```

Where `<type>` ∈ `{ingest, query, query_synthesis, lint, lint_retrospective, transition, skipped}`.

Parseable with:
```bash
grep "^## \[" wiki/log.md | tail -10
grep "^## \[.*\] ingest" wiki/log.md | wc -l
```

---

## 10. Implementation Roadmap

Implement in this order. Each phase is independently testable.

### Phase 1: Scaffolding

- [ ] Create directory structure (`raw/`, `wiki/`, `wiki/_pages/entity/`, `wiki/_pages/synthesis/`, `tools/`)
- [ ] Generate `CLAUDE.md` with all sections from §4 pre-filled
- [ ] Create empty `wiki/index.md` and `wiki/log.md` with correct headers
- [ ] Initialize `[system_state]` in `CLAUDE.md` with all fields set to initial values

### Phase 2: Evaluation Tools

- [ ] Implement `tools/eval_summary.py` with all three layers (§7)
  - Layer 1 (regex): no dependencies
  - Layer 2 (density): spaCy dependency
  - Layer 3 (semantic): sentence-transformers dependency, optional
- [ ] Implement `tools/graph_stats.py`
  - Parse all frontmatter `inbound_links` values from `wiki/_pages/**/*.md`
  - Compute and print `mean_inbound_links`
  - Exit with message if below/above maturity threshold
- [ ] Add CLI entry points with `--help` and `--verbose` flags
- [ ] Write unit tests for Layer 1 (deterministic, easy to test)

### Phase 3: Ingest Workflow

- [ ] Implement ingest command: reads source file, runs §4.2 protocol
- [ ] Source-level filter (index.md scan)
- [ ] Page classification (entity vs synthesis vs both)
- [ ] Per-page scorecard application using cold start vs mature variant
- [ ] Page write with correct frontmatter template
- [ ] `index.md` update routine
- [ ] `log.md` append routine
- [ ] `graph_stats.py` called after each ingest; maturity check + state update

### Phase 4: Lint

- [ ] Implement routine lint (`lint routine` command, §8.1)
- [ ] Implement retrospective lint (`lint retrospective` command, §8.2)
  - Generates report only; does not execute changes without confirmation
  - Confirmation mechanism: human edits report to mark approved actions, then runs `lint apply`

### Phase 5: Query

- [ ] Implement query command: reads index, retrieves pages, synthesizes answer
- [ ] Implement `query_synthesis` flow: optionally saves answer as Synthesis page

### Phase 6: Auto Research Harness

- [ ] Implement `tools/orchestrator.py` (§12.3)
- [ ] Implement subagent system prompts as static strings in `tools/subagent_prompts.py` (§12.4)
- [ ] Implement context injection logic in `tools/context_selector.py` (§12.7)
- [ ] Implement output validation in `tools/validate_output.py` (§12.5)
- [ ] Implement audit logging in `tools/audit.py` (§12.9)
- [ ] Implement quota manager in `tools/quota.py` (§12.8)
- [ ] Wire all components: `research` CLI command triggers full harness loop

---

## 11. Notes and Constraints

**The LLM never modifies `raw/`.** All writes are to `wiki/` or `CLAUDE.md`.

**Frontmatter is the source of truth for graph structure.** `inbound_links` in frontmatter is the canonical count. `graph_stats.py` reads frontmatter, not markdown link syntax, to avoid parsing edge cases.

**Thresholds in §7.4 are starting points, not fixed values.** After the first retrospective lint, the human should review whether the thresholds correctly separated useful from low-value cold_start pages, and adjust `[eval_thresholds]` in `CLAUDE.md` accordingly.

**Language handling**: the dangling reference patterns in §7.1 cover Chinese and English. If the wiki is used in another language, extend the pattern list in `CLAUDE.md`'s `[eval_config]` section — `eval_summary.py` reads this list at runtime.

**Obsidian compatibility**: all pages use standard markdown. Frontmatter is YAML. Internal links use `[[page_name]]` syntax which is valid for both Obsidian graph view and standard markdown renderers. Do not use Obsidian-specific syntax in page body.

**Version control**: the entire project root is a git repo. Commit after each ingest. Log entries map 1:1 to commits (use log entry title as commit message).

---

## 12. Auto Research Harness

The auto research harness enables autonomous resource discovery and evaluation. An **orchestrator** (stateful, long-running) controls a loop that spawns short-lived **subagents** (stateless, fresh context per invocation) to discover and evaluate candidate resources. The orchestrator owns all wiki writes; subagents only return structured JSON.

> **For Claude Code**: §12 is a strict implementation spec. Do not deviate from the subagent type definitions, I/O schemas, or the write isolation rule. Every deviation is a correctness bug, not a style choice.

### 12.1 Core Principles

**Write isolation**: subagents never write to disk. They return content. The orchestrator validates and writes. This is non-negotiable — it is what allows the deterministic evaluation pipeline (§7) to act as a gate between LLM output and wiki state.

**Context isolation**: each subagent invocation is a fresh API call with no shared conversation history. The orchestrator reconstructs the necessary context from disk before each call. A subagent must not assume it knows anything about previous invocations.

**Minimal context injection**: the orchestrator selects only the wiki pages relevant to the current candidate resource. It never dumps the full wiki into a subagent context. This keeps token costs bounded and prevents cross-contamination between unrelated topics.

**Structured I/O at all boundaries**: the only information that crosses the orchestrator/subagent boundary is JSON. System prompts define the output schema. The orchestrator validates every response against the schema before acting on it. Natural language in subagent output outside the JSON envelope is ignored.

**Audit trail**: every subagent invocation is logged with its full input manifest and raw output before any validation or action. This is the primary debugging surface.

---

### 12.2 System Topology

```
Human
  │ research query + scope
  ▼
Orchestrator (tools/orchestrator.py)
  │
  ├─── Discovery Subagent (one invocation)
  │       input:  DiscoveryManifest
  │       output: CandidateList JSON
  │       tools:  web_search only
  │
  ├─── [dedup + fetch loop, per candidate]
  │
  ├─── Evaluation Subagent (one invocation per candidate)
  │       input:  EvalManifest
  │       output: EvalResult JSON (scorecard + page drafts)
  │       tools:  none
  │
  ├─── Deterministic pipeline (tools/eval_summary.py)
  │       validates each draft from EvalResult
  │
  └─── Wiki write (only if pipeline passes)
          normal ingest protocol (§4.2 Step 3–4)
```

**No other topology is permitted.** In particular:
- Discovery Subagent must not call the Evaluation Subagent
- Evaluation Subagent must not perform web search
- No subagent spawns another subagent
- The orchestrator is the only process that reads from or writes to `wiki/`

---

### 12.3 Orchestrator Loop (`tools/orchestrator.py`)

```python
def run_research_session(query: str, scope: ResearchScope) -> SessionSummary:
    """
    Full research session. Single entry point for the harness.
    ResearchScope contains: max_candidates, max_new_pages, depth (shallow|deep)
    """
    session_id = generate_session_id()
    audit_log = AuditLog(session_id)

    # Step 1: Discovery
    discovery_manifest = build_discovery_manifest(query, scope)
    audit_log.record_invocation("discovery", discovery_manifest)
    
    raw_response = call_subagent(
        subagent_type="discovery",
        manifest=discovery_manifest
    )
    audit_log.record_response("discovery", raw_response)
    
    candidate_list = validate_and_parse(raw_response, schema=CandidateListSchema)
    if candidate_list is None:
        return SessionSummary(status="discovery_failed", session_id=session_id)

    # Step 2: Dedup against processed sources
    candidates = dedup_candidates(candidate_list, processed_log="wiki/log.md")
    candidates = candidates[:scope.max_candidates]  # quota hard cap

    # Step 3: Evaluate each candidate
    approved_pages = []
    for candidate in candidates:
        if quota_exceeded(approved_pages, scope):
            break

        content = fetch_resource(candidate.url)
        if content is None:
            audit_log.record_skip(candidate, reason="fetch_failed")
            continue

        # Context injection: select relevant wiki pages
        injected_pages = select_context_pages(content, max_tokens=4000)

        eval_manifest = build_eval_manifest(
            candidate=candidate,
            content=content,
            wiki_pages=injected_pages,
            cold_start=(not wiki_is_mature())
        )
        audit_log.record_invocation("evaluation", eval_manifest)

        raw_eval = call_subagent(
            subagent_type="evaluation",
            manifest=eval_manifest
        )
        audit_log.record_response("evaluation", raw_eval)

        eval_result = validate_and_parse(raw_eval, schema=EvalResultSchema)
        if eval_result is None:
            audit_log.record_skip(candidate, reason="malformed_eval_output")
            continue

        if eval_result.decision == "reject":
            audit_log.record_skip(candidate, reason=eval_result.rejection_reason)
            continue

        # Step 4: Deterministic pipeline gate
        for draft in eval_result.page_drafts:
            pipeline_result = run_eval_pipeline(draft)
            if pipeline_result.passes:
                approved_pages.append((draft, candidate))
            else:
                audit_log.record_pipeline_rejection(draft, pipeline_result)

    # Step 5: Write approved pages via normal ingest protocol
    for draft, candidate in approved_pages:
        write_page(draft)                          # creates/updates file
        update_inbound_links(draft)                # updates referenced pages
        update_index(draft)                        # updates index.md

    # Step 6: Post-session bookkeeping
    run_graph_stats()                              # check maturity transition
    append_session_log(session_id, approved_pages, audit_log)
    
    return SessionSummary(
        session_id=session_id,
        candidates_found=len(candidate_list),
        candidates_evaluated=len(candidates),
        pages_written=len(approved_pages),
        audit_log_path=audit_log.path
    )
```

**`call_subagent` implementation note**: this function makes a single Anthropic API call with the appropriate system prompt and the manifest JSON as user message content. It does not maintain conversation history. It must set a hard `max_tokens` limit (see §12.8). The raw response string is stored in the audit log before any parsing.

---

### 12.4 Subagent Types and System Prompts

System prompts are defined as static string constants in `tools/subagent_prompts.py`. They must not be generated dynamically. If you need to vary behavior, create a new subagent type — do not template-interpolate into system prompts.

#### Discovery Subagent

**Purpose**: given a research query, find URLs of candidate resources worth evaluating.

**Tools**: `web_search` only. No file access, no wiki access.

**System prompt** (`DISCOVERY_SYSTEM_PROMPT`):

```
You are a research discovery agent. Your only job is to find URLs of resources
relevant to the given research query.

You will receive a JSON object (DiscoveryManifest). You must respond with ONLY
a JSON object matching CandidateList schema. No other text before or after the JSON.

Constraints:
- Do not evaluate or summarize the resources you find
- Do not access the wiki or any local files
- Do not generate URLs from memory; only return URLs confirmed by web_search results
- Prefer primary sources (papers, official docs, authoritative blogs) over aggregators
- Already-processed URLs are listed in the manifest; exclude them from output

Output schema (respond with ONLY this JSON, nothing else):
{
  "candidates": [
    {
      "url": "string",
      "title": "string",
      "relevance_rationale": "string (max 50 words)",
      "estimated_type": "entity | synthesis | unknown"
    }
  ],
  "search_queries_used": ["string"]
}
```

#### Evaluation Subagent

**Purpose**: evaluate a single candidate resource against the current wiki state and, if approved, produce page drafts.

**Tools**: none. The subagent operates only on what is provided in the input manifest.

**System prompt** (`EVALUATION_SYSTEM_PROMPT`):

```
You are a wiki evaluation and drafting agent. You evaluate a single candidate
resource and, if it passes the scorecard, draft the wiki pages it should produce.

You will receive a JSON object (EvalManifest). You must respond with ONLY
a JSON object matching EvalResult schema. No other text before or after the JSON.

Constraints:
- Do not perform web searches or access external URLs
- Do not reference information not present in the manifest
- Evaluate only the resource content provided; do not reason from memory about the topic
- Page drafts must follow the exact templates in the manifest (entity or synthesis)
- Self-containedness rule: drafted pages must not contain dangling references.
  Forbidden phrases include (but are not limited to): "as mentioned", "see above",
  "as established", "building on the previous", "refer to section"
- If you decide to reject, set decision="reject" and explain in rejection_reason;
  do not produce page_drafts
- RAG Summary blocks in synthesis drafts must be 150-250 words, self-contained,
  and state the core synthetic claim in the first sentence

Scorecard dimensions to assess (0.0-1.0 each):
  novelty_delta, claim_density, self_containedness, bridge_score,
  hub_potential, gap_fill_score, contradiction_potential

Output schema (respond with ONLY this JSON, nothing else):
{
  "decision": "approve | reject",
  "rejection_reason": "string | null",
  "scorecard": {
    "novelty_delta": float,
    "claim_density": float,
    "self_containedness": float,
    "bridge_score": float,
    "hub_potential": float,
    "gap_fill_score": float,
    "contradiction_potential": float,
    "weighted_total": float
  },
  "page_drafts": [
    {
      "page_type": "entity | synthesis",
      "filename": "string (no path, no extension)",
      "frontmatter": { ... },
      "content": "string (full markdown body)"
    }
  ],
  "pages_to_update": [
    {
      "filename": "string",
      "section": "string",
      "update_description": "string (orchestrator will apply update)"
    }
  ],
  "contradictions_found": [
    {
      "existing_page": "string",
      "conflicting_claim": "string",
      "new_evidence": "string"
    }
  ]
}
```

**Note on `pages_to_update`**: the Evaluation Subagent identifies what existing pages should be updated but does not produce the update content. The orchestrator applies updates using a separate targeted call or defers to the next lint pass. This prevents the subagent from needing to read arbitrary existing page content beyond what was injected.

---

### 12.5 Input Manifest Schemas

All manifests are JSON objects passed as the user message content to the subagent API call.

#### DiscoveryManifest

```json
{
  "query": "string",
  "scope": {
    "max_candidates": "int",
    "depth": "shallow | deep"
  },
  "already_processed_urls": ["string"],
  "wiki_topic_summary": "string (≤200 words, from index.md header)",
  "existing_concept_gaps": ["string"]
}
```

`wiki_topic_summary` is a brief description of the wiki's current focus, extracted from `index.md`. It guides the discovery subagent toward relevant resources without exposing full page content. `existing_concept_gaps` is the list of concepts appearing in the Concept Index without dedicated pages — this directs discovery toward gap-filling sources.

#### EvalManifest

```json
{
  "candidate": {
    "url": "string",
    "title": "string"
  },
  "resource_content": "string (full text, max ~6000 words)",
  "wiki_context": {
    "relevant_pages": [
      {
        "filename": "string",
        "type": "entity | synthesis",
        "content": "string (full page content)"
      }
    ],
    "concept_gaps": ["string"],
    "graph_maturity": "bool"
  },
  "scorecard_config": {
    "variant": "cold_start | entity | synthesis",
    "weights": { ... },
    "acceptance_threshold": "float",
    "hard_rejection_threshold": "float"
  },
  "page_templates": {
    "entity": "string (full entity page template from §4.1)",
    "synthesis": "string (full synthesis page template from §4.1)"
  }
}
```

The `page_templates` field embeds the exact page templates from §4.1 verbatim. This ensures the subagent always has the current template even if the schema evolves.

---

### 12.6 Output Validation (`tools/validate_output.py`)

The orchestrator validates every subagent response before acting on it. Validation has two stages:

**Stage 1: Schema validation** (always runs)

```python
def validate_and_parse(raw_response: str, schema: type) -> dict | None:
    """
    Extracts JSON from raw_response, validates against schema.
    Returns parsed dict on success, None on any failure.
    Never raises — caller always handles None.
    """
    try:
        # Strip any accidental preamble (subagent violated the "only JSON" rule)
        json_str = extract_json_block(raw_response)
        data = json.loads(json_str)
        validate_schema(data, schema)
        return data
    except Exception as e:
        log_validation_failure(raw_response, e)
        return None
```

`extract_json_block` looks for the outermost `{...}` in the response. If none found or if parsing fails, returns None. **Do not retry automatically** on schema failure — log and skip. Retrying malformed LLM output in a tight loop wastes quota.

**Stage 2: Deterministic pipeline** (runs only on approved EvalResult page drafts)

Each draft in `eval_result.page_drafts` is written to a temp file, then:

```python
result = subprocess.run(
    ["python", "tools/eval_summary.py", temp_path, "--type", draft["page_type"]],
    capture_output=True
)
if result.returncode != 0:
    # pipeline rejection — log and skip this draft
    # do not re-run the evaluation subagent
```

The pipeline is the final gate. Its result overrides the subagent's own `scorecard.self_containedness` assessment. If the pipeline rejects a draft that the subagent approved, the draft is dropped (not retried). This enforces that the deterministic layer cannot be bypassed by LLM judgment.

---

### 12.7 Context Injection Protocol (`tools/context_selector.py`)

The orchestrator selects which wiki pages to inject into the EvalManifest. Selection must be bounded to stay within the subagent's effective context window.

**Token budget**: 4000 tokens for `wiki_context.relevant_pages` total. This leaves sufficient room for the resource content and the output schema.

**Selection algorithm**:

```python
def select_context_pages(resource_content: str, max_tokens: int = 4000) -> list[dict]:
    """
    1. Extract candidate entities from resource_content using NLP (spaCy NER)
    2. Score each wiki page by overlap with candidate entities
    3. Rank pages by score, then by inbound_links (hub pages first)
    4. Greedily include pages until token budget is reached
    5. Always include index.md summary regardless of score
    """
    entities = extract_entities(resource_content)
    
    all_pages = list_all_pages("wiki/_pages/")
    scored = []
    for page in all_pages:
        frontmatter, body = parse_page(page)
        overlap = entity_overlap(entities, frontmatter.get("tags", []) + [page.stem])
        scored.append((overlap, frontmatter.get("inbound_links", 0), page, body))
    
    scored.sort(key=lambda x: (x[0], x[1]), reverse=True)
    
    selected = []
    token_count = 0
    for overlap, inbound, page, body in scored:
        if overlap == 0:
            break  # no entity overlap at all — stop
        page_tokens = estimate_tokens(body)
        if token_count + page_tokens > max_tokens:
            continue  # skip this page, try smaller ones
        selected.append({"filename": page.name, "type": ..., "content": body})
        token_count += page_tokens
    
    return selected
```

**Critical**: if no pages score above zero entity overlap, inject zero pages. The subagent must handle an empty `relevant_pages` list (this is normal during cold start).

---

### 12.8 Quota and Rate Limiting (`tools/quota.py`)

Quotas are configured per research session in `CLAUDE.md`:

```yaml
[research_config]
max_candidates_per_session: 20
max_new_pages_per_session: 10
max_eval_subagent_tokens: 2000      # max_tokens for evaluation subagent API call
max_discovery_subagent_tokens: 1000 # max_tokens for discovery subagent API call
max_retries_on_fetch_failure: 2
discovery_search_queries_limit: 5   # passed to discovery subagent
```

**Hard caps that are not configurable**:
- Max subagent API calls per session: 50 (discovery + evaluations combined)
- Max tokens per subagent output: 3000 (enforced via API `max_tokens` parameter)
- Min time between API calls: 1 second (rate limit buffer)

The orchestrator checks quota at the start of each loop iteration. If any cap is reached, it finalizes the current session and writes a partial session log — it does not error out.

---

### 12.9 Failure Handling

The orchestrator must not crash on individual subagent failures. Every failure path logs and continues.

| Failure | Action |
|---|---|
| Schema validation fails | Log to audit, skip candidate, continue loop |
| Fetch resource fails (network) | Retry up to `max_retries_on_fetch_failure`, then skip |
| Subagent returns `decision: reject` | Log rejection reason, skip candidate |
| Deterministic pipeline rejects draft | Log pipeline output, drop draft, continue (do not re-run evaluation subagent) |
| `pages_to_update` conflicts with pipeline output | Defer all updates to next lint pass, log conflict |
| Quota exceeded | Finalize session immediately, log remaining unprocessed candidates |
| API call fails (network/auth) | Log error, abort session, write partial log |

**No automatic retry on subagent output failures.** If the subagent produced malformed JSON or a draft that fails the pipeline, re-running the same subagent on the same input is unlikely to improve the result and wastes quota. Skip and continue.

---

### 12.10 Audit Log (`tools/audit.py`)

Every research session generates a structured audit file at:

```
wiki/audit/research_<session_id>_<YYYY-MM-DD>.json
```

Schema:

```json
{
  "session_id": "string",
  "timestamp": "ISO-8601",
  "query": "string",
  "scope": { ... },
  "invocations": [
    {
      "subagent_type": "discovery | evaluation",
      "timestamp": "ISO-8601",
      "input_manifest": { ... },
      "raw_response": "string",
      "schema_valid": true,
      "pipeline_results": [
        {
          "filename": "string",
          "layer1_pass": true,
          "layer2_pass": true,
          "layer3_triggered": false,
          "final_decision": "approved | rejected",
          "rejection_detail": "string | null"
        }
      ],
      "pages_written": ["string"],
      "skipped_reason": "string | null"
    }
  ],
  "session_summary": {
    "candidates_found": 0,
    "candidates_evaluated": 0,
    "pages_written": 0,
    "pages_rejected_by_subagent": 0,
    "pages_rejected_by_pipeline": 0,
    "schema_validation_failures": 0
  }
}
```

The `raw_response` field stores the literal string returned by the API before any parsing. This is essential for debugging — if the subagent violated the "only JSON" rule, the preamble is visible here.

Audit files are never deleted by the system. They are not committed to git by default (add `wiki/audit/` to `.gitignore`) but should be retained locally.

**Log entry in `wiki/log.md`** (appended after each session):

```
## [YYYY-MM-DD] research | <query (truncated to 60 chars)>
session_id: <id>
candidates_evaluated: N
pages_written: M
pipeline_rejection_rate: X%
audit_file: wiki/audit/research_<id>_<date>.json
```

---

### 12.11 Directory Additions for Harness

```
tools/
  orchestrator.py       ← Main harness entry point (§12.3)
  subagent_prompts.py   ← Static system prompt constants (§12.4)
  context_selector.py   ← Wiki page selection for injection (§12.7)
  validate_output.py    ← Schema + pipeline validation (§12.6)
  quota.py              ← Session quota tracking (§12.8)
  audit.py              ← Audit log writer (§12.10)

wiki/
  audit/                ← Session audit files (gitignored)
```

CLI entry point:

```bash
python tools/orchestrator.py research \
  --query "transformer attention mechanisms" \
  --max-candidates 10 \
  --max-new-pages 5 \
  --depth shallow
```