# LLM Wiki — Schema and Protocol

You are the maintainer of this wiki. You create pages, update them on ingest, maintain cross-references, and run lint passes. The human sources content, directs exploration, and asks questions. Follow this document precisely.

**The LLM never modifies `raw/`. All writes go to `wiki/` or this file (`CLAUDE.md`).**

---

## System State

```yaml
[system_state]
graph_maturity: true
cold_start_page_count: 58
mean_inbound_links: 3.9655
retrospective_lint_done: true
```

---

## Page Templates

### Entity / Concept Page

Every entity page must use this exact frontmatter structure:

```markdown
---
type: entity
tags: []
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
cold_start: true
inbound_links: 0
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

<Structured list of specific, verifiable claims. Each claim is a complete sentence
that stands alone. Prefer: numbers, ratios, named systems, concrete comparisons.>

## Relationships

<Explicit links to other pages with one-line description of the relationship.>

## Sources

<Inline citations to raw/ files for each major claim.>
```

**Hard rejection criteria — stop and do not write the page if:**
- First paragraph contains a dangling reference pattern (see `[eval_config]` below)
- Page has fewer than 3 independently verifiable claims
- `sources` list is empty (ungrounded page)

---

### Synthesis Page

Every synthesis page must use this exact frontmatter structure:

```markdown
---
type: synthesis
connected_entities: []
synthesis_status: draft
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
or gaps that new sources could fill.>

## Connected Pages

<Links to all entity pages this synthesis draws from.>
```

**Hard rejection criteria — stop and do not write the page if:**
- RAG Summary block is absent
- RAG Summary is below 150 words or exceeds 250 words
- RAG Summary contains any dangling reference pattern
- `connected_entities` list is empty

---

## Ingest Protocol

When asked to ingest a source file, follow these steps in order:

### Step 0 — Source-Level Filter

Read `wiki/index.md`. Estimate how much of the source's content is already covered by existing pages with `cold_start: false`. If >80% is already covered, log a `skipped` entry and stop:

```
## [YYYY-MM-DD] skipped | <source filename>
reason: high redundancy with existing pages (<list page names>)
```

### Step 1 — Classify Source Content

Determine what the source primarily warrants:
- (a) Specific, citable factual claims → prioritize Entity pages
- (b) Cross-domain connections, synthesis, argument → prioritize Synthesis pages
- (c) Both → generate Entity pages first, then one Synthesis page referencing them

### Step 2 — Score Each Planned Page

Apply the cold-start scorecard while `[system_state].graph_maturity = false`:

```yaml
active_dimensions: [novelty_delta, claim_density, self_containedness, temporal_stability]
hard_rejection_threshold: 0.2   # only self_containedness triggers hard rejection
soft_log_threshold: 0.3         # others below this: log but don't reject
```

After graph maturity, use the entity or synthesis scorecard variants (see `[eval_thresholds]`).

### Step 3 — Execute Writes

For each page that passes its scorecard:
1. Create or update the page file in `wiki/_pages/entity/` or `wiki/_pages/synthesis/`
2. Update `inbound_links` count on any page that gains a new reference from this page
3. Update `wiki/index.md` (add row to the correct table, update Concept Index)
4. Run: `python tools/graph_stats.py wiki/_pages/` and update `[system_state].mean_inbound_links`

### Step 4 — Log Entry

Append to `wiki/log.md`:

```
## [YYYY-MM-DD] ingest | <source filename>
pages_created: [list]
pages_updated: [list]
pages_deferred: [list with reason]
cold_start: true
```

### Maturity Transition

After each ingest, if `graph_stats.py` reports `mean_inbound_links > 2.0` and `[system_state].graph_maturity` is still `false`:
1. Set `graph_maturity: true` in `[system_state]`
2. Log:
   ```
   ## [YYYY-MM-DD] transition | cold_start → mature
   pages_at_transition: N
   mean_inbound_links: X.XX
   ```
3. Do NOT immediately run retrospective lint — wait for explicit `lint retrospective` command.

---

## Query Protocol

When asked a question:
1. Use `qmd` to find relevant pages: `qmd search "<query>" --top 10`
2. Read the full text of the returned pages
3. Synthesize an answer with citations to wiki page filenames (not raw source filenames directly)
4. If the answer constitutes a significant synthesis not already captured in a page: create a new Synthesis page, log as `query_synthesis`:

```
## [YYYY-MM-DD] query_synthesis | <synthesis title>
source_query: <question>
pages_created: [list]
```

For regular queries, log:
```
## [YYYY-MM-DD] query | <question truncated to 80 chars>
```

After writing any new synthesis page, run `uv run --no-sync qmd update` (see qmd notes in Constraints).

---

## Lint Protocol

### Routine Lint (`lint routine`)

Check the wiki for:
- Orphan pages (no inbound links after wiki is mature)
- Stale claims (Synthesis pages with `temporal_stability: low` older than 90 days)
- Missing cross-references (entity mentioned in 3+ pages but no dedicated entity page)
- Synthesis pages with empty `open_questions` section
- Pages with `needs_summary_revision: true`
- Contradictions between pages (scan for conflicting claims)

Output a list of action candidates for human review before executing any changes. Append to `wiki/log.md`:

```
## [YYYY-MM-DD] lint | routine
issues_found: N
actions_taken: [list]
deferred_for_human: [list with reason]
```

### Retrospective Lint (`lint retrospective`)

Only runs when `[system_state].graph_maturity = true`. For every page with `cold_start: true`:

1. Run: `python tools/eval_summary.py <page_path> --type <entity|synthesis> --verbose`
2. Compute structural metrics (bridge_score, hub_potential) against current graph
3. Classify result:
   - `CLEARED` → scorecard passes; set `cold_start: false`
   - `RESTRUCTURE` → entity page should split into entity + synthesis; flag for rewrite
   - `MERGE` → content already covered by mature pages; propose merge target
   - `DELETE` → all metrics below threshold; no salvageable content

4. Write `wiki/retrospective_lint_report.md` with this structure:

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

5. **Wait for explicit `lint apply` command** before executing any MERGE or DELETE. After `lint apply`, set `[system_state].retrospective_lint_done: true`.

Append to `wiki/log.md`:
```
## [YYYY-MM-DD] lint | retrospective
issues_found: N
actions_taken: [list]
deferred_for_human: [list with reason]
```

---

## Index Format (`wiki/index.md`)

Update on every ingest. Structure:

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
- **ConceptName**: mentioned in [page_a](entity/page_a.md) — *no dedicated page*
- **ConceptName2**: → [page_c](entity/page_c.md)
```

---

## Evaluation Thresholds

```yaml
[eval_thresholds]
entity_page:
  entity_density_min: 0.15
  measurement_density_min: 0.0
  compression_ratio_max: 0.75

synthesis_rag_summary:
  entity_density_min: 0.10
  compression_ratio_max: 0.80

entity_scorecard:
  weights:
    structural: 0.3
    information: 0.5
    synthesis: 0.2
  hard_rejection_threshold: 0.2
  acceptance_threshold: 0.4

synthesis_scorecard:
  weights:
    structural: 0.4
    information: 0.2
    synthesis: 0.4
  hard_rejection_threshold: 0.2
  acceptance_threshold: 0.4
```

---

## Eval Configuration

```yaml
[eval_config]
dangling_patterns:
  # Chinese
  - "如前所述"
  - "上文提到"
  - "见上节"
  - "前文"
  - "如上"
  - "详见.{0,10}页"
  - "参考.{0,10}章节"
  - "前述"
  # English
  - "as (mentioned|discussed|described) (above|earlier|previously)"
  - "see (above|section|chapter|below)"
  - "the (aforementioned|previous|above)"
  - "this (follows from|builds on|extends)"
  - "as (noted|shown|established) (above|earlier)"
  - "refer to (the previous|section|chapter)"

word_count_bounds:
  entity_first_paragraph:
    min: 80
    max: 300
  synthesis_rag_summary:
    min: 150
    max: 250

spacy_model: en_core_web_sm
```

---

## Research Configuration

```yaml
[research_config]
max_candidates_per_session: 20
max_new_pages_per_session: 10
max_eval_subagent_tokens: 16000
max_discovery_subagent_tokens: 3000
max_retries_on_fetch_failure: 2
discovery_search_queries_limit: 5
keyword_recommendation_limit: 5
max_keyword_recommender_tokens: 16000
keyword_recommender_model: null
recent_audit_sessions_for_discovery: 10
repeat_url_suppression: true
qmd_command: ["uv", "run", "--no-sync", "qmd"]
research_state_dir: "wiki/research_state"
topic_similarity_min_score: 0.80
near_duplicate_score: 0.90
topic_saturation_hit_threshold: 2   # pre-eval skip if qmd returns this many similar pages
title_overlap_threshold: 0.8        # pre-eval skip for hard title duplicates, not broad shared stack/vendor terms
synthesis_gap_min_cluster_size: 3   # log synthesis gap if tag cluster has >= this many entity pages
domain_stopwords: []                # optional domain terms ignored by duplicate/saturation token overlap
preferred_source_types:
  - official documentation
  - paper
  - technical report
  - implementation repository
required_measurement_fields:
  - hardware_targets
  - workloads
  - metrics
  - measurement_context
page_type_taxonomy:
  entity: general concept, project, system, chip, or architecture page
  synthesis: cross-page comparison, contradiction, or landscape page
  source_note: source-grounded note used when a source is useful but not yet page-worthy
```

---

## Constraints and Notes

- **Frontmatter is the source of truth for graph structure.** `inbound_links` in frontmatter is canonical. `graph_stats.py` reads frontmatter, not markdown link syntax.
- **Obsidian compatibility.** Internal links use `[[page_name]]` syntax. No Obsidian-specific syntax in page body.
- **Version control.** Commit after each ingest. Use the log entry title as the commit message.
- **qmd BM25 path.** The research harness uses `uv run --no-sync qmd update` before a session and after each successful page write, then checks candidates with `uv run --no-sync qmd search -c _pages --format json`. Strong duplicate signals may reject a candidate before evaluation; topic saturation is only a merge/update hint. Do not call `qmd query`, `qmd vsearch`, or `qmd embed` in the default harness path; those paths require embeddings/model setup and may trigger large local downloads. Never use `qmd index` — that command does not exist.
- **Patch queue.** `pages_to_update` proposals are written to `wiki/patch_queue.md` for review instead of being appended directly to target pages.
- **Research resume state.** Runtime checkpoints live under `wiki/research_state/` and are intentionally ignored by git. Use `research --resume <session_id>` to continue a stopped session and `research --list-sessions` to inspect available checkpoints.
- **Language handling.** The dangling reference patterns above cover Chinese and English. Extend `[eval_config].dangling_patterns` for other languages.
