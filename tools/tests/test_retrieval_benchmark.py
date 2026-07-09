import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from qmd_runner import QmdMatch, QmdSearchResult  # noqa: E402
from retrieval_benchmark import run_benchmark  # noqa: E402


class _FakeQmdRunner:
    """Returns a fixed ranked result list per query, keyed by query text, so
    tests don't need a live qmd install or an on-disk _pages collection."""

    def __init__(self, results_by_query: dict[str, list[QmdMatch]]):
        self._results = results_by_query

    def search(self, query_text, top=5, collection="_pages"):
        matches = self._results.get(query_text, [])
        return QmdSearchResult(ok=True, matches=matches[:top])


def _match(rank, file):
    return QmdMatch(rank=rank, file=file, score=0.5)


def test_top1_hit_scores_full_marks():
    runner = _FakeQmdRunner({
        "q1": [_match(1, "entity/sifive-intelligence-x280.md"), _match(2, "entity/ara2.md")],
    })
    queries = [{"query": "q1", "expected": ["sifive-intelligence-x280"]}]

    stats = run_benchmark(queries, top=5, qmd_runner=runner)

    assert stats["top1_accuracy"] == 1.0
    assert stats["recall_at_5"] == 1.0
    assert stats["mrr"] == 1.0


def test_hit_below_top1_counts_toward_recall_not_top1_accuracy():
    runner = _FakeQmdRunner({
        "q1": [_match(1, "entity/ara2.md"), _match(2, "entity/sifive-intelligence-x280.md")],
    })
    queries = [{"query": "q1", "expected": ["sifive-intelligence-x280"]}]

    stats = run_benchmark(queries, top=5, qmd_runner=runner)

    assert stats["top1_accuracy"] == 0.0
    assert stats["recall_at_5"] == 1.0
    assert stats["mrr"] == 0.5


def test_complete_miss_scores_zero():
    runner = _FakeQmdRunner({
        "q1": [_match(1, "entity/ara2.md")],
    })
    queries = [{"query": "q1", "expected": ["sifive-intelligence-x280"]}]

    stats = run_benchmark(queries, top=5, qmd_runner=runner)

    assert stats["top1_accuracy"] == 0.0
    assert stats["recall_at_5"] == 0.0
    assert stats["mrr"] == 0.0


def test_hyphen_underscore_stem_mismatch_still_counts_as_hit():
    """qmd kebab-cases filenames internally while disk uses snake_case (see
    context_selector._resolve_qmd_path) -- the benchmark must not treat that
    naming difference as a retrieval miss."""
    runner = _FakeQmdRunner({
        "q1": [_match(1, "qmd://_pages/entity/sifive-intelligence-x280.md")],
    })
    queries = [{"query": "q1", "expected": ["sifive_intelligence_x280"]}]

    stats = run_benchmark(queries, top=5, qmd_runner=runner)

    assert stats["top1_accuracy"] == 1.0


def test_aggregate_metrics_average_across_multiple_queries():
    runner = _FakeQmdRunner({
        "hit": [_match(1, "entity/a.md")],
        "miss": [_match(1, "entity/b.md")],
    })
    queries = [
        {"query": "hit", "expected": ["a"]},
        {"query": "miss", "expected": ["a"]},
    ]

    stats = run_benchmark(queries, top=5, qmd_runner=runner)

    assert stats["query_count"] == 2
    assert stats["top1_accuracy"] == 0.5
    assert stats["mrr"] == 0.5


def test_qmd_failure_recorded_without_crashing():
    class _FailingRunner:
        def search(self, query_text, top=5, collection="_pages"):
            return QmdSearchResult(ok=False, matches=[], error="qmd unavailable")

    queries = [{"query": "q1", "expected": ["a"]}]
    stats = run_benchmark(queries, top=5, qmd_runner=_FailingRunner())

    assert stats["failed_queries"] == ["q1"]
    assert stats["top1_accuracy"] == 0.0
