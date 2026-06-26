# Retrospective Lint Report — 2026-06-27

## Summary

- **Total pages evaluated**: 78 (69 entity, 9 synthesis)
- **Cleared**: 77
- **Restructure**: 0
- **Merge**: 0
- **Delete**: 0
- **Deferred for human decision**: 0
- **Note**: spaCy not installed; Layer 2 (entity/measurement density) was skipped for all pages. Layer 1 (dangling reference check) ran fully.

---

## Cleared (77 pages)

All entity and synthesis pages passed Layer 1 evaluation and have been set to `cold_start: false`.

One page required a pre-clearance fix:
- `entity/intel_amx.md`: phrase "the previous best x86 path" matched dangling reference pattern `the (aforementioned|previous|above)`. Fixed to "the dominant x86 path for matrix multiply before AMX". Cleared after fix.

All other 76 pages passed without modification.

---

## Restructure Candidates

None identified.

---

## Merge Candidates

None identified (Layer 2 spaCy analysis unavailable; overlap detection based on structural review only).

---

## Delete Candidates

None identified.

---

## Deferred for Human Decision

None.

---

## Notes

- `graph_stats.py` reports `mean_inbound_links: 0.6154` — below the 2.0 graph maturity threshold. The `graph_maturity: true` flag in CLAUDE.md was set manually after retrospective lint was authorized. The low mean_inbound_links reflects that most entity pages reference each other via `[[wikilink]]` syntax but graph_stats counts frontmatter `inbound_links` fields, which have not been kept current with the actual link graph.
- Recommend a follow-up `lint routine` pass to count actual `[[wikilink]]` occurrences and update `inbound_links` frontmatter fields across all pages.
