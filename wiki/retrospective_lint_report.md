# Retrospective Lint Report — 2026-07-09

Scope: all 13 pages with `cold_start: true` (the full graph — this is the first
retrospective pass since `graph_maturity` flipped true this session).

Methodology: `tools/eval_summary.py --verbose` per page (Layer 1 structural,
Layer 2 density/compression, Layer 3 qmd BM25 self-retrieval/saturation) plus
`tools/graph_topology.py wiki/_pages/ --verbose` for real degree/betweenness
centrality, compared against each page's subjective `bridge_score`/`hub_potential`.
Graph median betweenness centrality is 0.0 (7 of 13 pages have zero betweenness),
so "elevated" below means clearing both a fixed floor (~0.25, roughly half the
graph's max of 0.53) and the zero median by a wide margin — not just "nonzero".

**Infra fix applied during this pass**: `tools/eval_summary.py` Layer 3
self-retrieval had two real bugs, found and fixed while running this lint
(not content-quality issues — every page's `needs_summary_revision` flag was
being computed wrong):
1. `slug = path.stem` kept hyphens, but qmd result filenames were normalized
   to underscores before comparison, so `slug in top_k` could never match for
   any multi-word filename (11 of 13 pages here). Fixed by normalizing the
   slug the same way before comparison.
2. qmd's BM25 backend (SQLite FTS5) treats `()"*^` as query-syntax operators;
   a title like "Single-Core Matmul (TT-Metalium)" silently returned zero
   results because of the parens, unrelated to actual retrievability. Fixed
   by stripping those characters from the query text before calling `qmd
   search` (display title is untouched).

Also ran `uv run --no-sync qmd update` before this pass (previously stale —
it still listed `tenstorrent_blackhole_architecture`, a duplicate merged and
deleted earlier this session, as a live competitor).

After both fixes, all 13 pages pass Layer 3 self-retrieval cleanly; the
Merge Candidates saturation numbers below are now reliable.

## Cleared (11 pages)

All passed Layer 1 (structural) and Layer 2 (entity_density/measurement_density/
compression_ratio) with no hard violations. `cold_start` set to `false`.

- `entity/blackhole-quietbox.md`
- `entity/tensix-core.md`
- `entity/tenstorrent.md`
- `entity/tenstorrent-memory-model.md`
- `entity/tt-forge.md`
- `entity/tt-forge-onnx.md`
- `entity/tt-metalium.md`
- `entity/wormhole.md`
- `optimization_recipe/tt-xla-performance-optimization-techniques.md`
- `synthesis/wormhole-vs-blackhole-architecture.md`
- `workload_kernel/single-core-matmul-tt-metalium.md`

## Restructure Candidates

Dual-signal bar (per CLAUDE.md's RESTRUCTURE rule): subjective `bridge_score`
high (≥0.7) **and** real betweenness centrality elevated (≥0.25, well above
the graph's zero median). Both pages left `cold_start: true` pending human
decision — not flipped to `false` since a restructure changes their content.

- `entity/blackhole.md`: bridge_score=0.70, betweenness=0.5303 (highest in
  graph, degree=0.4167). This page now carries the shared Tensix-tile
  architecture detail (NoC routing, MOP expander, ISA specifics) merged in
  from three separate source collisions this session, plus product-line
  claims (P100A/P150A/P150B pricing, Galaxy rack). It is the graph's
  structural hub — 9 inbound links, connects the chip-architecture cluster
  (wormhole, tensix-core) to the product cluster (tt-quietbox-2,
  blackhole-quietbox, tt-metalium, tt-forge).
  - Proposed synthesis title: "Blackhole Chip Architecture vs. Product Lineup"
    — split the deep ISA/NoC/toolchain architecture content into its own
    entity page (or fold into `tensix-core.md`, which already covers the
    compute-tile internals) and leave `blackhole.md` as the product/variant
    page (P100A/P150A/P150B/Galaxy pricing and positioning).
- `entity/tt-quietbox-2.md`: bridge_score=0.70, betweenness=0.3030
  (degree=0.3333). Bridges the hardware cluster (blackhole) to the software
  cluster (tt-metalium, tt-forge) and to its sibling product
  (blackhole-quietbox).
  - Proposed synthesis title: "Tenstorrent Workstation Lineup: QuietBox vs.
    QuietBox 2" — a comparison synthesis connecting `tt-quietbox-2.md` and
    `blackhole-quietbox.md` (specs, price, generation) would let both pages
    stay focused as entity pages rather than growing further via ad hoc
    merges.

## Merge Candidates

None. MERGE requires content already covered by a page with `cold_start: false`
— every page in the wiki is still cold_start as of this pass, so there is no
established page for any content to be redundant against yet. Most pages clear
the configured `topic_saturation_hit_threshold` (2) with 2-4 same-cluster
competitors each (`tt-forge`↔`tt-forge-onnx`, `tt-quietbox-2`↔`blackhole-quietbox`,
`tensix-core`↔{blackhole,wormhole,tt-metalium,single-core-matmul}, etc.) but in
each case the pages cover distinct scope (sub-project vs. parent compiler stack;
two hardware generations with different specs; a shared architectural component
vs. the products/SDK built on it) — this is expected topical clustering in a
young, tightly-themed 13-page wiki, not duplication. Re-evaluate once more
pages exist outside this cluster.

## Delete Candidates

None. Every page passed Layer 1/2 with strong entity_density and
compression_ratio; none show near-zero novelty or unsalvageable content.

## Deferred for Human Decision

- `entity/blackhole-quietbox.md` vs `entity/tt-quietbox-2.md`: both describe
  a liquid-cooled 4-chip Blackhole workstation, but with materially different
  specs (EPYC Siena 8124P / 512 GB DDR5 / $11,999 / Nov 2025 review vs. Ryzen
  7 9700X / 256 GB DDR5 / $9,999 / March 2026 launch). Treated this session as
  two distinct generations (`blackhole-quietbox` = QuietBox 1,
  `tt-quietbox-2` = QuietBox 2) and cross-linked as a predecessor/successor
  pair rather than merged — but the only evidence for "two generations" is
  the spec delta across two secondary-source articles, not an explicit
  Tenstorrent statement that QuietBox 1 exists as a named product distinct
  from QuietBox 2. Please confirm this reading is correct; if QuietBox 1
  turns out to be a misreported/pre-release configuration of the same QB2
  hardware, these two pages should be merged instead.

## Applied (lint apply, 2026-07-09)

Both RESTRUCTURE candidates executed:

- `entity/blackhole.md`: the shared Tensix-tile architecture detail (MOP
  expander, Wait Gate, 19-bit Matrix Unit, 32-lane SFPU, 16-bank L1 SRAM)
  moved into `entity/tensix-core.md`, which already covered the compute-tile
  internals. `blackhole.md`'s Architecture section now points to
  `[[tensix-core]]` and keeps only chip/board-specific facts (grid dimensions,
  P100A harvesting, host PCIe routing, die-level SiFive X280 cores). Both
  pages re-evaluated through `eval_summary.py` (Layer 1/2 pass) after the
  edit. `cold_start` set to `false`.
- `entity/tt-quietbox-2.md`: created
  `synthesis/quietbox-vs-quietbox-2-workstation-lineup.md` comparing it
  against `blackhole-quietbox.md` (spec table, generational-cost-down
  reading, and the deferred identity question carried into its Open
  Questions section rather than silently resolved). Evaluated through
  `eval_summary.py --type synthesis` (Layer 1/2 pass). `cold_start` set to
  `false` on `tt-quietbox-2.md`; the new synthesis page starts `cold_start:
  true` per the page-creation default.

The deferred QuietBox-generation question above is **not** resolved by this
pass — it is carried forward as an Open Question on the new synthesis page,
since no new primary-source evidence was found to settle it either way.
Graph re-checked after all edits: 14 pages, `orphan_fraction: 0.0`,
`median_inbound_links: 1.5`. `[system_state].retrospective_lint_done: true`.
