"""
Cross-session context-injection history: per-event EWMA share, not a
wall-clock or page-count decay.

context_selector.py's per-session injection_cap (see its docstring) stops a
hub page from dominating *within* one session, but the counter it works from
resets to empty on every new `orchestrator.py research` invocation. Found
live running 10 short back-to-back sessions on one theme: two pages (the
first vector-processor entities created) organically became hubs, and
because each session re-starts injection_counts at {}, the per-session cap
never engages across sessions.

Two design mistakes to avoid, in order:

1. Decaying by wall-clock time couples the estimator to *operator cadence*,
   not to the process being measured (how often a page is actually being
   injected). Ten sessions run back-to-back in an hour barely decay; the same
   ten sessions spread across ten days decay a lot -- same injection
   behavior, wildly different penalty. Decaying by wiki page count has the
   same defect from the other direction: sessions that inject context but
   write zero new pages (a third of a real run, in practice) apply no decay
   at all while still injecting repeatedly. Both couple the clock to a
   quantity the injection process doesn't control.

   The fix: decay per *event* -- one tick per candidate-evaluation, the same
   unit the injection decisions themselves happen in. This is a standard
   EWMA (exponentially-weighted moving average): every tick, every page's
   running count is multiplied by `beta`, and the page(s) actually injected
   this tick get +1. A page's "effective sample size" is ~1/(1-beta) ticks.

2. A raw decaying count is still confounded by *exposure*: a page injected
   since the wiki's first session has had far more opportunities to
   accumulate ticks than one created yesterday, so a fixed cap unfairly
   favors old pages regardless of whether they're still the best match. The
   fix is to track a page's *share* of total injection events, not its raw
   count: alongside each page's decayed count, track a single decayed
   `total_ticks` (one tick per candidate evaluated, incremented whether or
   not it selected this particular page). share(page) = count(page) /
   total_ticks is a weighted average of "was this page injected on tick i"
   over the same decayed window for every page -- exposure-independent by
   construction, because numerator and denominator warm up together from
   the same tick 0 (no separate bias-correction term needed, unlike the
   textbook 1/(1-beta^t)-normalized EWMA-of-a-mean, precisely because the
   denominator here is an explicit running sum rather than an assumed
   steady-state constant).

A page is flagged over-represented when its share exceeds a multiple of its
"fair share" (1 / current page count) -- e.g. 3x fair share, matching the
old flat injection_cap=3's rough magnitude but now normalized rather than
absolute. This deliberately does not try to suppress a page's real,
warranted centrality (some hub formation is correct -- see Barabasi-Albert
preferential attachment): only a page repeatedly and disproportionately
over-injected relative to how many pages exist gets deprioritized, and even
then only as a soft reorder (see context_selector.py), never excluded.
"""

from __future__ import annotations

import json
from pathlib import Path

DEFAULT_BETA = 0.9  # effective window ~= 1/(1-beta) = 10 candidate-evaluation ticks
DEFAULT_FAIR_SHARE_MULTIPLIER = 3.0
_NEGLIGIBLE = 1e-6


def load_state(path: Path) -> tuple[dict[str, float], float]:
    """Return (counts, total_ticks) from persisted history. Missing or
    corrupt state is treated as a cold start ({}, 0.0) rather than raising --
    this is a soft anti-inflation signal, not something that should ever
    block a session from running."""
    if not path.exists():
        return {}, 0.0
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}, 0.0
    if not isinstance(raw, dict):
        return {}, 0.0
    total_ticks = raw.get("total_ticks")
    total_ticks = float(total_ticks) if isinstance(total_ticks, (int, float)) else 0.0
    counts_raw = raw.get("counts")
    counts = {
        stem: float(v) for stem, v in counts_raw.items()
        if isinstance(counts_raw, dict) and isinstance(v, (int, float)) and float(v) > _NEGLIGIBLE
    } if isinstance(counts_raw, dict) else {}
    return counts, total_ticks


def save_state(path: Path, counts: dict[str, float], total_ticks: float) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "total_ticks": round(total_ticks, 6),
        "counts": {
            stem: round(count, 6) for stem, count in counts.items() if count > _NEGLIGIBLE
        },
    }
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def tick(
    counts: dict[str, float], total_ticks: float, injected_stems: list[str],
    beta: float = DEFAULT_BETA,
) -> tuple[dict[str, float], float]:
    """Advance one candidate-evaluation tick: decay every existing page's
    count by `beta`, then add 1 to each page in `injected_stems` (the pages
    actually shown as context this tick), and add 1 to total_ticks
    regardless of which pages were injected. Pure function -- does not
    touch disk."""
    decayed = {stem: count * beta for stem, count in counts.items() if count * beta > _NEGLIGIBLE}
    for stem in injected_stems:
        decayed[stem] = decayed.get(stem, 0.0) + 1.0
    return decayed, total_ticks * beta + 1.0


def share(counts: dict[str, float], total_ticks: float, stem: str) -> float:
    """This page's share of decayed total injection-consideration ticks."""
    if total_ticks <= 0:
        return 0.0
    return counts.get(stem, 0.0) / total_ticks


def is_overrepresented(
    counts: dict[str, float], total_ticks: float, stem: str, page_count: int,
    multiplier: float = DEFAULT_FAIR_SHARE_MULTIPLIER,
) -> bool:
    """True when this page's decayed share of injection events exceeds
    `multiplier` times its fair share (1 / page_count) of all pages. A brand
    new page or one with no recorded history never trips this (share 0)."""
    if page_count <= 0:
        return False
    fair_share = 1.0 / page_count
    return share(counts, total_ticks, stem) > multiplier * fair_share
