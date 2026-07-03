import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from relationship_links import extract_outbound_links


def test_extracts_target_and_reason_from_relationships_section():
    body = (
        "# Some Page\n\n"
        "First paragraph.\n\n"
        "## Relationships\n\n"
        "- [[gemmini]]: shares the same systolic-array accelerator design.\n"
        "- [[k230]]: alternative edge AI target.\n\n"
        "## Sources\n\n"
        "cite here\n"
    )
    links = extract_outbound_links(body)
    assert links == [
        {"target": "gemmini", "reason": "shares the same systolic-array accelerator design"},
        {"target": "k230", "reason": "alternative edge AI target"},
    ]


def test_extracts_from_connected_pages_section_for_synthesis():
    body = (
        "## RAG Summary\n\nSummary text.\n\n"
        "## Full Synthesis\n\nNarrative mentioning [[unrelated-mention]] inline.\n\n"
        "## Open Questions\n\n- one\n\n"
        "## Connected Pages\n\n"
        "- [[xuantie-c950]]\n"
        "- [[k230]]\n"
    )
    links = extract_outbound_links(body)
    assert links == [
        {"target": "xuantie-c950", "reason": "unlabeled"},
        {"target": "k230", "reason": "unlabeled"},
    ]


def test_inline_mentions_outside_relationships_section_are_not_edges():
    body = (
        "# Page\n\nMentions [[other-page]] inline but has no Relationships section.\n"
    )
    assert extract_outbound_links(body) == []


def test_no_relationships_section_returns_empty():
    assert extract_outbound_links("# Page\n\nJust prose.\n") == []


def test_duplicate_targets_deduplicated_keeping_first():
    body = (
        "## Relationships\n\n"
        "- [[gemmini]]: first reason.\n"
        "- [[gemmini]]: second reason should be dropped.\n"
    )
    links = extract_outbound_links(body)
    assert links == [{"target": "gemmini", "reason": "first reason"}]


def test_stops_at_next_heading():
    body = (
        "## Relationships\n\n"
        "- [[gemmini]]: real edge.\n\n"
        "## Sources\n\n"
        "- [[not-a-relationship]]: this is under a different section.\n"
    )
    links = extract_outbound_links(body)
    assert links == [{"target": "gemmini", "reason": "real edge"}]


def test_extracts_with_hyphen_and_dash_separators():
    """Regression: found live via a real replication run that the subagent
    does not consistently use a colon separator — CLAUDE.md's page template
    only specifies "a one-line description," not punctuation. Every
    Relationships bullet actually written in that run used a plain hyphen,
    en-dash, or em-dash instead of a colon, e.g.
    "- [[k230]] – The K230 integrates two XuanTie C908 cores...". The
    colon-only regex silently matched zero of them, leaving outbound_links
    empty on every page in the run."""
    body = (
        "## Relationships\n\n"
        "- [[xuantie_c908]] – The K230 integrates two XuanTie C908 cores; provides core details.\n"
        "- [[allwinner_d1]] - The Allwinner D1 integrates the XuanTie C906 core.\n"
        "- [[visionfive2]] — A different RISC-V core family used in other SBCs.\n"
    )
    links = extract_outbound_links(body)
    assert links == [
        {"target": "xuantie_c908", "reason": "The K230 integrates two XuanTie C908 cores; provides core details"},
        {"target": "allwinner_d1", "reason": "The Allwinner D1 integrates the XuanTie C906 core"},
        {"target": "visionfive2", "reason": "A different RISC-V core family used in other SBCs"},
    ]
