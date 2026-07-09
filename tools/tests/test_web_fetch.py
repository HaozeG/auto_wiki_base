import io
import sys
import urllib.error
from pathlib import Path
from unittest.mock import MagicMock, patch

sys.path.insert(0, str(Path(__file__).parent.parent))

import web_fetch  # noqa: E402
from web_fetch import (  # noqa: E402
    DomainCircuitBreaker,
    fetch_url,
    fetch_wayback_snapshot,
    is_safe_url,
    sanitize_fetched_content,
)


def _http_error(code, headers=None):
    return urllib.error.HTTPError(
        url="https://example.com/x", code=code, msg="err",
        hdrs=headers or {}, fp=io.BytesIO(b""),
    )


def test_success_returns_ok_and_records_breaker_success():
    breaker = DomainCircuitBreaker()
    breaker.record_failure("example.com")

    resp = MagicMock()
    resp.read.return_value = b"hello world"
    resp.geturl.return_value = "https://example.com/x"
    resp.__enter__.return_value = resp
    resp.__exit__.return_value = False

    with patch.object(web_fetch.urllib.request, "urlopen", return_value=resp):
        result = fetch_url("https://example.com/x", breaker=breaker)

    assert result.ok
    assert result.status == "ok"
    assert result.content == "hello world"
    assert result.attempts == 1
    assert not breaker.is_tripped("example.com")


def test_404_fails_fast_without_retry():
    calls = []

    def fake_urlopen(req, timeout=15):
        calls.append(req)
        raise _http_error(404)

    with patch.object(web_fetch.urllib.request, "urlopen", side_effect=fake_urlopen), \
         patch.object(web_fetch.time, "sleep") as sleep_mock:
        result = fetch_url("https://example.com/dead", retries=2)

    assert result.status == "not_found"
    assert result.content is None
    assert len(calls) == 1  # no retry on a permanent client error
    sleep_mock.assert_not_called()


def test_403_fails_fast_without_retry():
    with patch.object(web_fetch.urllib.request, "urlopen", side_effect=lambda req, timeout=15: (_ for _ in ()).throw(_http_error(403))):
        result = fetch_url("https://example.com/blocked", retries=2)

    assert result.status == "forbidden"
    assert result.content is None


def test_429_retries_honoring_retry_after_then_gives_up():
    calls = []

    def fake_urlopen(req, timeout=15):
        calls.append(req)
        raise _http_error(429, headers={"Retry-After": "5"})

    with patch.object(web_fetch.urllib.request, "urlopen", side_effect=fake_urlopen), \
         patch.object(web_fetch.time, "sleep") as sleep_mock:
        result = fetch_url("https://example.com/limited", retries=2)

    assert result.status == "rate_limited"
    assert len(calls) == 3  # retries=2 -> 3 attempts total
    # Retry-After honored (capped), not the generic exponential backoff.
    assert all(call.args[0] == 5 for call in sleep_mock.call_args_list)


def test_network_error_retries_with_backoff_then_trips_breaker():
    breaker = DomainCircuitBreaker(threshold=2)
    calls = []

    def fake_urlopen(req, timeout=15):
        calls.append(req)
        raise ConnectionResetError("connection reset by peer")

    with patch.object(web_fetch.urllib.request, "urlopen", side_effect=fake_urlopen), \
         patch.object(web_fetch.time, "sleep"):
        result = fetch_url("https://flaky.example.com/a", retries=1, breaker=breaker)

    assert result.status == "network_error"
    assert len(calls) == 2  # retries=1 -> 2 attempts
    # Two failed attempts against the same host both count toward the
    # breaker (threshold=2), so it should now be tripped.
    assert breaker.is_tripped("flaky.example.com")


def test_circuit_breaker_short_circuits_without_network_call():
    breaker = DomainCircuitBreaker(threshold=1)
    breaker.record_failure("flaky.example.com")
    assert breaker.is_tripped("flaky.example.com")

    with patch.object(web_fetch.urllib.request, "urlopen") as urlopen_mock:
        result = fetch_url("https://flaky.example.com/b", breaker=breaker)

    assert result.status == "circuit_open"
    urlopen_mock.assert_not_called()


def test_forbidden_and_not_found_do_not_trip_breaker():
    """A 403/404 is a per-URL content outcome, not evidence the whole host
    is down -- it must not count toward the connectivity circuit breaker."""
    breaker = DomainCircuitBreaker(threshold=1)

    with patch.object(web_fetch.urllib.request, "urlopen", side_effect=lambda req, timeout=15: (_ for _ in ()).throw(_http_error(404))):
        fetch_url("https://example.com/a", breaker=breaker)
    with patch.object(web_fetch.urllib.request, "urlopen", side_effect=lambda req, timeout=15: (_ for _ in ()).throw(_http_error(403))):
        fetch_url("https://example.com/b", breaker=breaker)

    assert not breaker.is_tripped("example.com")


def test_fetch_wayback_snapshot_recovers_archived_content():
    availability_resp = MagicMock()
    availability_resp.read.return_value = (
        b'{"archived_snapshots": {"closest": '
        b'{"available": true, "url": "http://web.archive.org/web/20240101000000/https://example.com/gone"}}}'
    )
    availability_resp.__enter__.return_value = availability_resp
    availability_resp.__exit__.return_value = False

    snapshot_resp = MagicMock()
    snapshot_resp.read.return_value = b"archived page content"
    snapshot_resp.geturl.return_value = "https://web.archive.org/web/20240101000000/https://example.com/gone"
    snapshot_resp.__enter__.return_value = snapshot_resp
    snapshot_resp.__exit__.return_value = False

    with patch.object(web_fetch.urllib.request, "urlopen", side_effect=[availability_resp, snapshot_resp]):
        content = fetch_wayback_snapshot("https://example.com/gone")

    assert content == "archived page content"


def test_fetch_wayback_snapshot_returns_none_when_no_snapshot_exists():
    availability_resp = MagicMock()
    availability_resp.read.return_value = b'{"archived_snapshots": {}}'
    availability_resp.__enter__.return_value = availability_resp
    availability_resp.__exit__.return_value = False

    with patch.object(web_fetch.urllib.request, "urlopen", return_value=availability_resp):
        content = fetch_wayback_snapshot("https://example.com/never-archived")

    assert content is None


# --- Egress hygiene: SSRF guard + fetched-content sanitization ---


def test_is_safe_url_accepts_ordinary_http_https():
    assert is_safe_url("https://example.com/page")
    assert is_safe_url("http://example.com/page")


def test_is_safe_url_rejects_non_http_schemes():
    assert not is_safe_url("file:///etc/passwd")
    assert not is_safe_url("javascript:alert(1)")
    assert not is_safe_url("data:text/html;base64,AAAA")
    assert not is_safe_url("ftp://example.com/x")


def test_is_safe_url_rejects_loopback_and_private_literal_hosts():
    assert not is_safe_url("http://127.0.0.1/admin")
    assert not is_safe_url("http://localhost/admin")
    assert not is_safe_url("http://169.254.169.254/latest/meta-data")  # cloud metadata
    assert not is_safe_url("http://10.0.0.5/internal")
    assert not is_safe_url("http://192.168.1.1/router")
    assert not is_safe_url("http://[::1]/admin")


def test_fetch_url_blocks_unsafe_url_before_any_request():
    with patch.object(web_fetch.urllib.request, "urlopen") as urlopen_mock:
        result = fetch_url("http://127.0.0.1/secret")

    assert result.status == "forbidden"
    assert result.content is None
    urlopen_mock.assert_not_called()


def test_fetch_url_sanitizes_returned_content():
    resp = MagicMock()
    resp.read.return_value = b"See [[Existing Page]] for details.\n---\nmore text"
    resp.geturl.return_value = "https://example.com/x"
    resp.__enter__.return_value = resp
    resp.__exit__.return_value = False

    with patch.object(web_fetch.urllib.request, "urlopen", return_value=resp):
        result = fetch_url("https://example.com/x")

    assert "[[Existing Page]]" not in result.content
    assert "\\[\\[Existing Page\\]\\]" in result.content
    assert "\n---\n" not in result.content


def test_sanitize_fetched_content_escapes_wikilinks_and_frontmatter_delimiters():
    text = "before\n[[Injected Link]]\n---\nafter\n...\n"
    sanitized = sanitize_fetched_content(text)

    assert "[[" not in sanitized
    assert "]]" not in sanitized
    assert "\\[\\[Injected Link\\]\\]" in sanitized
    # bare frontmatter delimiters must no longer stand alone on their own line
    assert not any(line.strip() in ("---", "...") for line in sanitized.splitlines())


def test_sanitize_fetched_content_truncates_to_max_bytes():
    text = "a" * 1000
    sanitized = sanitize_fetched_content(text, max_bytes=100)
    assert len(sanitized.encode("utf-8")) <= 100
