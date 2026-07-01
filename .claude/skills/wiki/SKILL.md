---
name: wiki
description: Operate the LLM Wiki harness. Use when users ask to set up a theme, run research, apply patches, ingest a source, query the wiki, or run lint. Covers both the automated CLI path and the manual LLM protocol path.
allowed-tools: Bash, Read, Edit, Write
---

# LLM Wiki — Operation Skill

The wiki has two operation paths:

- **CLI (automated)** — `uv run --no-sync python tools/orchestrator.py <subcommand>` runs the full subagent harness: LLM discovery, evaluation, identity resolution, write gate, and patch queue. Use this for autonomous research sessions.
- **Manual (LLM protocol)** — for ingest, query, and lint, follow the step-by-step protocol in `CLAUDE.md`. The LLM reads sources, writes pages, and maintains the graph directly.

---

## Setup

Propose organization profiles for a theme (lists options, writes nothing):

```bash
uv run --no-sync python tools/orchestrator.py setup theme "<your theme>"
```

Select and write a profile:

```bash
uv run --no-sync python tools/orchestrator.py setup theme "<your theme>" --choice <id>
```

After setup, the chosen profile is written into `CLAUDE.md` as `[theme_profile]`. Run setup once per wiki. `--dry-run` shows the profile without writing.

---

## Research

Run an autonomous research session (DDG discovery → evaluation → write gate):

```bash
uv run --no-sync python tools/orchestrator.py research --query "<topic>" --max-candidates 10 --max-new-pages 5
```

Options:
- `--depth shallow|deep` — escalates discovery breadth when early candidates all fail evaluation
- `--resume <session_id>` — resume a stopped session (checkpoints in `wiki/research_state/`)
- `--list-sessions` — list resumable sessions

Pages written to `wiki/_pages/`; update proposals queued to `wiki/patch_queue.md`.

---

## Patch Apply

Apply human-approved merge patches from `wiki/patch_queue.md`. Mark entries `status: approved` in the queue file first, then run:

```bash
uv run --no-sync python tools/orchestrator.py patch apply
```

The harness invokes a content-merge subagent, runs the result through the eval pipeline, and rewrites the target page atomically. The queue entry is marked `applied`. Only `status: approved` entries are processed; all others are left untouched.

---

## Ingest (manual protocol)

Follow the **Ingest Protocol** in `CLAUDE.md` (Steps 0–4). In brief:

1. **Step 0** — identity resolution: check `wiki/index.md`, route existing concepts to upsert
2. **Step 1** — classify: entity pages first, then one synthesis page if warranted
3. **Step 2** — cold-start scorecard: reject pages below threshold before writing
4. **Step 3** — write pages to `wiki/_pages/entity/` or `wiki/_pages/synthesis/`, update `inbound_links`, update `wiki/index.md`, run `python tools/graph_stats.py wiki/_pages/`
5. **Step 4** — append log entry to `wiki/log.md`

Commit after each ingest. Use the log entry title as the commit message.

---

## Query (manual protocol)

Follow the **Query Protocol** in `CLAUDE.md`. In brief:

1. `uv run --no-sync qmd search "<query>" -n 10` to find relevant pages
2. Read the full page content of top hits
3. Synthesize an answer with citations to wiki page filenames
4. If the answer is a significant synthesis not already in the wiki, create a Synthesis page and log as `query_synthesis`

---

## Lint (manual protocol)

Follow the **Lint Protocol** in `CLAUDE.md`.

**Routine lint** — health check (any time):

Check for: orphan pages, stale synthesis claims, missing entity pages for frequently-mentioned concepts, empty `open_questions` sections, `needs_summary_revision: true` flags, contradictions. Output candidates for human review; do not execute changes without review. Log to `wiki/log.md`.

**Retrospective lint** — only when `[system_state].graph_maturity = true`:

```bash
python tools/eval_summary.py wiki/_pages/<page>.md --type entity|synthesis --verbose
```

Run on every page with `cold_start: true`. Classify as `CLEARED / RESTRUCTURE / MERGE / DELETE`. Write `wiki/retrospective_lint_report.md`. Wait for `lint apply` before executing any MERGE or DELETE.

---

## Key invariants

- `raw/` is immutable — the LLM never writes to it
- Frontmatter is the source of truth for graph structure (`inbound_links`)
- Duplicate creation is hard-blocked: a `canonical_name` collision forces `upsert`, never a second page
- `wiki/research_state/` is gitignored; `raw/cache/` content-addressed snapshots are gitignored by default
- All frontmatter writes must be atomic YAML round-trips — never string-splice `---` delimiters
