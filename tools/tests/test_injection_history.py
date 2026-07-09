import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from injection_history import (  # noqa: E402
    is_overrepresented,
    load_state,
    save_state,
    share,
    tick,
)


def test_missing_file_returns_cold_start():
    counts, total = load_state(Path("/nonexistent/injection_history.json"))
    assert counts == {}
    assert total == 0.0


def test_corrupt_file_returns_cold_start(tmp_path):
    path = tmp_path / "injection_history.json"
    path.write_text("not valid json{{{", encoding="utf-8")
    counts, total = load_state(path)
    assert counts == {}
    assert total == 0.0


def test_single_tick_records_injected_page():
    counts, total = tick({}, 0.0, ["hub"], beta=0.9)
    assert counts["hub"] == 1.0
    assert total == 1.0


def test_tick_decays_existing_counts_before_incrementing():
    counts, total = tick({"hub": 4.0}, 4.0, ["hub"], beta=0.5)
    # existing 4.0 decays to 2.0, then +1 for this tick's injection
    assert counts["hub"] == 3.0
    assert total == 3.0  # 4.0 * 0.5 + 1.0


def test_tick_decays_pages_not_injected_this_round():
    counts, total = tick({"hub": 4.0, "other": 2.0}, 6.0, ["hub"], beta=0.5)
    assert counts["hub"] == 3.0   # 4.0*0.5 + 1.0
    assert counts["other"] == 1.0  # 2.0*0.5, no increment
    assert total == 4.0  # 6.0*0.5 + 1.0


def test_negligible_decayed_entries_pruned():
    counts, _ = tick({"stale": 1e-8}, 0.0, [], beta=0.5)
    assert "stale" not in counts


def test_share_is_zero_with_no_history():
    assert share({}, 0.0, "hub") == 0.0


def test_share_reflects_fraction_of_total_ticks():
    counts = {"hub": 3.0}
    assert abs(share(counts, 10.0, "hub") - 0.3) < 1e-9


def test_share_converges_to_injection_probability_under_stationary_process():
    """A page injected every single tick should converge toward a share of 1.0
    (not decay toward 0) -- the EWMA numerator and denominator must warm up
    together at the same rate."""
    counts: dict[str, float] = {}
    total = 0.0
    for _ in range(200):
        counts, total = tick(counts, total, ["always"], beta=0.9)
    assert share(counts, total, "always") > 0.99


def test_share_reflects_partial_injection_rate():
    """A page injected on half of all ticks should converge to a share near
    0.5, not 1.0 and not 0.0 -- this is the exposure-independent behavior
    that fixes the raw-count approach (an old page injected 5/10 times looks
    the same as a new page injected 5/10 times)."""
    counts: dict[str, float] = {}
    total = 0.0
    for i in range(400):
        stems = ["sometimes"] if i % 2 == 0 else []
        counts, total = tick(counts, total, stems, beta=0.95)
    assert 0.4 < share(counts, total, "sometimes") < 0.6


def test_is_overrepresented_false_for_fresh_page():
    assert not is_overrepresented({}, 0.0, "new-page", page_count=10)


def test_is_overrepresented_true_when_share_exceeds_multiple_of_fair_share():
    # fair share of 10 pages = 0.1; 3x fair share = 0.3
    counts = {"hub": 4.0}
    assert is_overrepresented(counts, total_ticks=10.0, stem="hub", page_count=10, multiplier=3.0)


def test_is_overrepresented_false_when_share_within_fair_multiple():
    counts = {"hub": 2.0}
    assert not is_overrepresented(counts, total_ticks=10.0, stem="hub", page_count=10, multiplier=3.0)


def test_is_overrepresented_exposure_independent_old_vs_new_page():
    """The core fix: an "old" page whose absolute count is large purely
    because it's existed longer must not be flagged over-represented if its
    *rate* of injection matches everyone else's -- only genuine
    disproportion (relative to page_count) should trip the flag."""
    counts: dict[str, float] = {}
    total = 0.0
    # "old" page injected on 1 out of every 10 ticks for 300 ticks (many more
    # exposure opportunities than a "new" page would ever see)
    for i in range(300):
        stems = ["old"] if i % 10 == 0 else []
        counts, total = tick(counts, total, stems, beta=0.95)
    # a "new" page injected at the exact same 1-in-10 rate for only the last 20 ticks
    for i in range(20):
        stems = ["new"] if i % 10 == 0 else []
        counts, total = tick(counts, total, stems, beta=0.95)

    old_share = share(counts, total, "old")
    new_share = share(counts, total, "new")
    assert abs(old_share - new_share) < 0.05  # same rate -> same share, despite unequal exposure
    assert not is_overrepresented(counts, total, "old", page_count=10, multiplier=3.0)


def test_round_trip_save_and_load(tmp_path):
    path = tmp_path / "injection_history.json"
    save_state(path, {"hub": 3.5, "leaf": 0.2}, total_ticks=12.0)

    counts, total = load_state(path)

    assert counts["hub"] == 3.5
    assert counts["leaf"] == 0.2
    assert total == 12.0


def test_save_prunes_negligible_counts(tmp_path):
    path = tmp_path / "injection_history.json"
    save_state(path, {"real": 2.0, "tiny": 1e-9}, total_ticks=5.0)

    counts, _ = load_state(path)
    assert "tiny" not in counts
    assert counts["real"] == 2.0
