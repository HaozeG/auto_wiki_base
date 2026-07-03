import sys
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).parent.parent))

from qmd_runner import QmdRunner


def _run_result(returncode=0, stdout="", stderr=""):
    from unittest.mock import MagicMock
    m = MagicMock()
    m.returncode = returncode
    m.stdout = stdout
    m.stderr = stderr
    return m


def test_update_repoints_collection_when_it_points_elsewhere(tmp_path):
    """Regression: qmd collections are a single global, name-keyed registry,
    not scoped per cwd/worktree. Without re-pointing, `qmd update` silently
    re-indexes whatever directory "_pages" was last registered to — found
    live: after running research in one git worktree, "_pages" still pointed
    at a different worktree's wiki/_pages, so duplicate/saturation checks
    were comparing new candidates against the wrong branch's content."""
    runner = QmdRunner(cwd=tmp_path)
    expected_path = str((tmp_path / "wiki" / "_pages").resolve())
    calls = []

    def fake_run(cmd, **kwargs):
        calls.append(cmd)
        if cmd[-2:] == ["collection", "show"] or (len(cmd) >= 3 and cmd[-3] == "collection" and cmd[-2] == "show"):
            return _run_result(0, stdout="Collection: _pages\n  Path:     /some/other/worktree/wiki/_pages\n")
        return _run_result(0)

    with patch("subprocess.run", side_effect=fake_run):
        ok, err = runner.update()

    assert ok is True
    remove_calls = [c for c in calls if "remove" in c]
    add_calls = [c for c in calls if "add" in c]
    assert remove_calls, "expected the stale collection to be removed"
    assert add_calls, "expected a fresh collection pointed at this project's wiki/_pages"
    assert expected_path in add_calls[0]


def test_update_does_not_repoint_when_collection_already_correct(tmp_path):
    runner = QmdRunner(cwd=tmp_path)
    expected_path = str((tmp_path / "wiki" / "_pages").resolve())
    calls = []

    def fake_run(cmd, **kwargs):
        calls.append(cmd)
        if len(cmd) >= 2 and cmd[-1] == "_pages" and "show" in cmd:
            return _run_result(0, stdout=f"Collection: _pages\n  Path:     {expected_path}\n")
        return _run_result(0)

    with patch("subprocess.run", side_effect=fake_run):
        ok, err = runner.update()

    assert ok is True
    assert not any("remove" in c for c in calls)
    assert not any("add" in c for c in calls)


def test_update_creates_collection_when_none_registered_yet(tmp_path):
    runner = QmdRunner(cwd=tmp_path)
    calls = []

    def fake_run(cmd, **kwargs):
        calls.append(cmd)
        if "show" in cmd:
            return _run_result(1, stderr="collection not found")
        return _run_result(0)

    with patch("subprocess.run", side_effect=fake_run):
        ok, err = runner.update()

    assert ok is True
    assert not any("remove" in c for c in calls)
    assert any("add" in c for c in calls)
