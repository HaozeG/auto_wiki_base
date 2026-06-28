# Auto Wiki Base

Auto Wiki Base is a markdown knowledge-base template for maintaining a curated wiki with an LLM agent. Raw sources stay immutable, the wiki pages are generated and maintained, and lightweight Python tools validate pages, compute graph health, and run an optional autonomous research loop.

The repository starts with an empty wiki baseline. The first step for a new wiki is to choose a broad theme and write a theme profile into `CLAUDE.md`; that profile tells the agent what page families, relationships, source preferences, coverage priorities, and lint priorities fit this wiki.

## Repository Layout

- `raw/` - source material. Treat these files as immutable inputs.
- `wiki/_pages/entity/` - entity pages for systems, chips, projects, papers, and other concrete objects.
- `wiki/_pages/synthesis/` - synthesis pages that connect multiple entities.
- `wiki/index.md` - human and agent-facing catalog of wiki pages.
- `wiki/log.md` - chronological append-only activity log.
- `wiki/audit/` - ignored runtime audit logs for research sessions.
- `wiki/research_state/` - ignored resumable research checkpoints.
- `CLAUDE.md` - operating schema and configuration for LLM agents.
- `tools/` - validation, graph, qmd, and research harness code.
- `subagent_env_setup.sh` - ignored local environment setup script for subagent API credentials.

## Requirements

- Python `>=3.10`
- `uv`
- qmd CLI installed separately for wiki search:

```bash
npm install -g @tobilu/qmd
```

Install Python dependencies with:

```bash
uv sync
```

If you do not want to sync/install dependencies during a command, most project commands are written as:

```bash
uv run --no-sync <command>
```

## First-Time QMD Setup

The research harness expects a qmd collection named `_pages` and uses BM25 search only.

```bash
qmd collection add wiki/_pages --name _pages
uv run --no-sync qmd update
uv run --no-sync qmd search "example topic" -c _pages -n 5 --format json
```

Do not use `qmd query`, `qmd vsearch`, or `qmd embed` for the default harness path. Those require embedding/model setup and may trigger large local downloads.

## Start A Fresh Wiki

Use this sequence when starting from the empty baseline on `main`.

1. Choose a broad theme.
2. Ask the agent to propose organization options for that theme.
3. Pick one option and persist it to `CLAUDE.md`.
4. Add source files to `raw/` or run the autonomous research loop.
5. Review generated wiki pages, patch-queue entries, index changes, and log entries.
6. Run tests/validation and commit durable artifacts.

For example, list organization options:

```bash
uv run --no-sync python tools/orchestrator.py setup theme "RISC-V AI accelerator"
```

This prints 2-4 choices such as architecture-first, workflow-first, or ecosystem-first when the theme is hardware-oriented. Other themes produce different structures, such as character/theme/event options for a book or company/product/market options for competitive analysis.

Persist the selected option:

```bash
uv run --no-sync python tools/orchestrator.py setup theme "RISC-V AI accelerator" --choice workflow_first
```

The command writes a `[theme_profile]` block into `CLAUDE.md`. The base harness remains domain-agnostic; specialized page types such as `hardware_target`, `optimization_recipe`, or `benchmark_result` appear only when the selected theme profile enables them.

Useful prompt for an agent-driven setup:

```text
We are starting a fresh Auto Wiki. Use tools/orchestrator.py setup theme "<theme>" to list organization options, explain the tradeoffs, ask me which option to choose, then persist the selected theme profile to CLAUDE.md.
```

After setup, update qmd:

```bash
uv run --no-sync qmd update
```

## Local Subagent Environment

For research runs that call the evaluation subagent, source the local environment script:

```bash
source ./subagent_env_setup.sh
```

The orchestrator reads standard Anthropic-compatible environment variables such as `ANTHROPIC_API_KEY`, `ANTHROPIC_BASE_URL`, `ANTHROPIC_DEFAULT_HAIKU_MODEL`, and `CLAUDE_CODE_SUBAGENT_MODEL`.

## Human Wiki Workflow

Use an LLM coding agent with this repository open. The normal workflow is:

1. Confirm `CLAUDE.md` has the intended `[theme_profile]`.
2. Add or identify a source in `raw/`.
3. Ask the agent to ingest it into the wiki according to the selected theme profile.
4. Review changed pages in `wiki/_pages/` and any proposed updates in `wiki/patch_queue.md`.
5. Run validation and graph checks.
6. Update qmd search after accepted writes.
7. Commit the source, wiki changes, index, log, and schema/config updates.

For reading and browsing, open `wiki/` in Obsidian or any markdown editor. Internal links use `[[page_name]]` syntax.

Useful prompt for source ingest:

```text
Ingest raw/sources/<file> into the wiki. Follow CLAUDE.md, use the active theme profile, keep raw/ immutable, write only orchestrator-approved pages/patch-queue entries, update wiki/index.md and wiki/log.md, run validation, and summarize what changed.
```

## Query The Wiki

For quick local search:

```bash
uv run --no-sync qmd search "example topic" -c _pages -n 10 --format json
```

Then open the returned markdown files under `wiki/_pages/`.

For agent-assisted questions, ask the LLM to search qmd first, read the full relevant pages, and answer with citations to wiki page filenames.

## Validate A Page

Run the three-layer page validation pipeline:

```bash
uv run python tools/eval_summary.py wiki/_pages/entity/example_entity.md --type entity --verbose
uv run python tools/eval_summary.py wiki/_pages/synthesis/example_synthesis.md --type synthesis --verbose
```

Exit code `0` means approved. Exit code `1` means the page failed a hard validation gate.

## Check Graph Health

Compute graph statistics from page frontmatter:

```bash
uv run python tools/graph_stats.py wiki/_pages
```

Useful variants:

```bash
uv run python tools/graph_stats.py wiki/_pages --verbose
uv run python tools/graph_stats.py wiki/_pages --median
uv run python tools/graph_stats.py wiki/_pages --exclude-hubs 20
```

If the output says the graph is mature, update `[system_state].graph_maturity` and related stats in `CLAUDE.md`.

## Run The Autonomous Research Loop

The research loop discovers URLs, gates near-duplicates with qmd BM25 search, fetches candidate content, calls an evaluation subagent, validates drafts, writes approved pages immediately, and checkpoints progress. It reads the active `[theme_profile]` from `CLAUDE.md` and passes that profile into discovery/evaluation manifests.

Start a small run:

```bash
source ./subagent_env_setup.sh

uv run python tools/orchestrator.py research \
  --query "example research topic" \
  --max-candidates 2 \
  --max-new-pages 1 \
  --depth shallow
```

Full interface:

```bash
uv run python tools/orchestrator.py research \
  --query "<query>" \
  --max-candidates 10 \
  --max-new-pages 5 \
  --depth shallow
```

Use `--depth deep` for broader search, longer content windows, and supplemental snippets:

```bash
uv run python tools/orchestrator.py research \
  --query "<query>" \
  --max-candidates 10 \
  --max-new-pages 5 \
  --depth deep
```

List resumable sessions:

```bash
uv run python tools/orchestrator.py research --list-sessions
```

Resume a session:

```bash
uv run python tools/orchestrator.py research --resume <session_id>
```

Inspect a checkpoint:

```bash
jq '.candidates[] | {url: .candidate.url, state, skip_reason, qmd_matches, written_files}' \
  wiki/research_state/session_<session_id>.json
```

Research session states include `discovered`, `skipped_similarity`, `fetch_failed`, `evaluating`, `eval_rejected`, `pipeline_rejected`, `approved`, and `written`.

If qmd update/search fails, the loop stops as `blocked_qmd` before eval API calls.

Useful prompt for agent-driven research:

```text
Run a small autonomous research session for "<topic>" using the active theme profile. Keep the run bounded, inspect audit/session output, verify generated pages, and tell me whether coverage gaps remain before we commit.
```

## Run Tests

```bash
uv run --no-sync pytest -q
```

The tests mock qmd and API-sensitive paths, so they do not require a live qmd index or API key.

## Configuration

The main configuration lives in YAML blocks inside `CLAUDE.md`:

- `[system_state]` - current wiki maturity and graph state.
- `[theme_profile]` - selected first-run organization profile, including theme-derived page families, source preferences, coverage priorities, and lint priorities.
- `[eval_thresholds]` - page validation thresholds.
- `[research_config]` - research loop limits, qmd command, state directory, and duplicate-gate thresholds.

Important research defaults:

```yaml
qmd_command: ["uv", "run", "--no-sync", "qmd"]
research_state_dir: "wiki/research_state"
topic_similarity_min_score: 0.80
near_duplicate_score: 0.90
topic_saturation_hit_threshold: 2
title_overlap_threshold: 0.8
```

First-run setup is theme-adaptive; see [Start A Fresh Wiki](#start-a-fresh-wiki). If `[theme_profile]` is absent, the harness falls back to generic page types: `entity`, `synthesis`, and `source_note`.

## Git Hygiene

Ignored runtime/local files include:

- `wiki/audit/`
- `wiki/research_state/`
- `subagent_env_setup.sh`
- `.venv/`
- `.pytest_cache/`
- Python cache files

Before committing, inspect changes:

```bash
git status --short
git diff
```

Commit durable knowledge artifacts: raw sources, wiki pages, `wiki/index.md`, `wiki/log.md`, tool changes, tests, and docs. Do not commit runtime audit/checkpoint files or local credential scripts.
