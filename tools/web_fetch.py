"""HTTP content retrieval for the research harness.

Replaces a bare urlopen-with-flat-retry loop with three things a live
30-page test run showed were missing (see wiki/log.md 2026-07-08 batches):

1. Retry classification. A permanent client error (404/403/410) was being
   retried exactly like a transient network blip, wasting 2 extra attempts
   and backoff sleep per dead/blocked URL for no chance of success. 429 is
   retried with backoff honoring Retry-After instead of the same flat delay.
2. A per-host circuit breaker. Several sessions saw one host (e.g. a vendor
   blog) reset the connection for every single URL on that domain. Without
   a breaker, every later candidate pointing at that host pays the full
   retry+backoff cost again for a domain already known to be unreachable
   this session.
3. A Wayback Machine fallback tier for the generic fetch path, richer than
   falling straight to a thin DDG snippet when a source is blocked or gone.
"""

from __future__ import annotations

import ipaddress
import json
import logging
import random
import re
import socket
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass

logger = logging.getLogger(__name__)

# Egress hygiene: the discovery loop follows URLs surfaced by web search
# results, which are untrusted input. Two failure modes found by inspecting
# claude-obsidian's equivalent hardening (this project had neither check):
# 1. SSRF — a malicious/compromised search result pointing at a private,
#    loopback, or link-local address (e.g. cloud metadata endpoints) with no
#    scheme/host validation before the request is made.
# 2. Injection via fetched content flowing into wiki drafts — a page body
#    containing literal `[[...]]` creates unintended wikilinks, and a line
#    that is exactly `---`/`...` can splice a second YAML document if the
#    excerpt is ever embedded verbatim near frontmatter.
_ALLOWED_SCHEMES = {"http", "https"}
_MAX_CONTENT_BYTES = 200_000


def _is_private_or_local_host(host: str) -> bool:
    if not host:
        return True
    if host == "localhost" or host.endswith(".localhost"):
        return True
    try:
        addr = ipaddress.ip_address(host)
    except ValueError:
        try:
            infos = socket.getaddrinfo(host, None)
        except socket.gaierror:
            return False  # can't resolve; let the request itself fail naturally
        return any(
            ipaddress.ip_address(info[4][0]).is_private
            or ipaddress.ip_address(info[4][0]).is_loopback
            or ipaddress.ip_address(info[4][0]).is_link_local
            for info in infos
        )
    return addr.is_private or addr.is_loopback or addr.is_link_local


def is_safe_url(url: str) -> bool:
    """Reject non-http(s) schemes and requests targeting loopback, private,
    or link-local addresses (SSRF guard) before any request is made."""
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme not in _ALLOWED_SCHEMES:
        return False
    host = (parsed.hostname or "").lower()
    return not _is_private_or_local_host(host)


_WIKILINK_OPEN_RE = re.compile(r"\[\[")
_WIKILINK_CLOSE_RE = re.compile(r"\]\]")
_FRONTMATTER_DELIM_RE = re.compile(r"^(-{3,}|\.{3,})\s*$", re.MULTILINE)


def sanitize_fetched_content(content: str, max_bytes: int = _MAX_CONTENT_BYTES) -> str:
    """Neutralize fetched-content injection risk before it flows into wiki
    drafts: escape `[[`/`]]` (wikilink injection), escape bare `---`/`...`
    lines (YAML frontmatter-splice injection), and cap size."""
    text = _WIKILINK_OPEN_RE.sub(r"\\[\\[", content)
    text = _WIKILINK_CLOSE_RE.sub(r"\\]\\]", text)
    text = _FRONTMATTER_DELIM_RE.sub(
        lambda m: "".join("\\" + c for c in m.group(1)), text
    )
    encoded = text.encode("utf-8")
    if len(encoded) > max_bytes:
        text = encoded[:max_bytes].decode("utf-8", errors="ignore")
    return text

_BROWSER_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

# Client errors where retrying the identical request cannot succeed.
_PERMANENT_STATUS = {400, 401, 403, 404, 405, 410, 451}
# Server-side/rate-limit statuses worth a bounded retry with backoff.
_RETRYABLE_STATUS = {429, 500, 502, 503, 504}
_MAX_RETRY_AFTER_SECONDS = 30


def _status_label(code: int) -> str:
    if code == 403:
        return "forbidden"
    if code == 404:
        return "not_found"
    if code == 429:
        return "rate_limited"
    if code in _RETRYABLE_STATUS:
        return "server_error"
    return "forbidden" if code in _PERMANENT_STATUS else "network_error"


@dataclass
class FetchResult:
    content: str | None
    status: str  # ok | not_found | forbidden | rate_limited | server_error | network_error | circuit_open
    final_url: str
    attempts: int
    error: str | None = None

    @property
    def ok(self) -> bool:
        return self.content is not None


class DomainCircuitBreaker:
    """Tracks consecutive connectivity-class failures per host for one
    session/process. Only network_error/server_error/rate_limited count --
    forbidden/not_found are per-URL content outcomes, not evidence the whole
    host is unreachable, so they don't trip the breaker."""

    def __init__(self, threshold: int = 3):
        self.threshold = threshold
        self._fail_counts: dict[str, int] = {}
        self._tripped: set[str] = set()

    def is_tripped(self, host: str) -> bool:
        return host in self._tripped

    def record_failure(self, host: str) -> None:
        count = self._fail_counts.get(host, 0) + 1
        self._fail_counts[host] = count
        if count >= self.threshold:
            self._tripped.add(host)

    def record_success(self, host: str) -> None:
        self._fail_counts.pop(host, None)
        self._tripped.discard(host)


def _backoff_seconds(attempt: int) -> float:
    return min(2 ** attempt, 16) + random.uniform(0, 0.5)


def _host_of(url: str) -> str:
    return urllib.parse.urlparse(url).netloc.lower()


def fetch_url(url: str, retries: int = 2, timeout: int = 15,
               breaker: DomainCircuitBreaker | None = None) -> FetchResult:
    """Fetch a URL with retry classification and an optional per-host
    circuit breaker. Never raises; failures come back as a FetchResult.

    Rejects non-http(s) schemes and loopback/private/link-local hosts before
    making any request (SSRF guard — see module docstring)."""
    if not is_safe_url(url):
        return FetchResult(None, "forbidden", url, 0,
                            error=f"blocked unsafe URL scheme/host: {url}")

    host = _host_of(url)
    if breaker is not None and breaker.is_tripped(host):
        return FetchResult(None, "circuit_open", url, 0,
                            error=f"circuit open for {host} after repeated failures this session")

    attempts = 0
    for attempt in range(retries + 1):
        attempts += 1
        try:
            req = urllib.request.Request(url, headers=_BROWSER_HEADERS)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                raw = resp.read()
                if breaker is not None:
                    breaker.record_success(host)
                try:
                    content = raw.decode("utf-8")
                except UnicodeDecodeError:
                    content = raw.decode("latin-1", errors="replace")
                content = sanitize_fetched_content(content)
                return FetchResult(content, "ok", resp.geturl() or url, attempts)
        except urllib.error.HTTPError as e:
            status = _status_label(e.code)
            logger.warning("fetch_url: attempt %d failed for %s — HTTP %d (%s)",
                            attempts, url, e.code, status)
            if e.code in _PERMANENT_STATUS:
                # Retrying an identical request against a permanent client
                # error cannot succeed -- fail fast instead of burning the
                # rest of the retry budget and backoff sleep on it.
                return FetchResult(None, status, url, attempts, error=str(e))
            if e.code not in _RETRYABLE_STATUS:
                return FetchResult(None, "network_error", url, attempts, error=str(e))
            if breaker is not None:
                breaker.record_failure(host)
            if attempt < retries:
                if e.code == 429:
                    retry_after = e.headers.get("Retry-After") if e.headers else None
                    delay = _MAX_RETRY_AFTER_SECONDS
                    if retry_after and retry_after.isdigit():
                        delay = min(int(retry_after), _MAX_RETRY_AFTER_SECONDS)
                    time.sleep(delay)
                else:
                    time.sleep(_backoff_seconds(attempt))
                continue
            return FetchResult(None, status, url, attempts, error=str(e))
        except Exception as e:  # noqa: BLE001 — network/timeout/connection errors
            logger.warning("fetch_url: attempt %d failed for %s — %s", attempts, url, e)
            if breaker is not None:
                breaker.record_failure(host)
            if attempt < retries:
                time.sleep(_backoff_seconds(attempt))
                continue
            return FetchResult(None, "network_error", url, attempts, error=str(e))
    return FetchResult(None, "network_error", url, attempts, error="exhausted retries")


def fetch_wayback_snapshot(url: str, timeout: int = 15) -> str | None:
    """Best-effort fallback for a URL that's currently blocked or gone:
    check the Wayback Machine's availability API and fetch the closest
    archived snapshot. Returns None on any failure (including "no snapshot
    exists"), never raises."""
    api_url = "https://archive.org/wayback/available?url=" + urllib.parse.quote(url, safe="")
    try:
        req = urllib.request.Request(api_url, headers=_BROWSER_HEADERS)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except Exception as e:  # noqa: BLE001
        logger.warning("fetch_wayback_snapshot: availability check failed for %s — %s", url, e)
        return None

    snapshot = (data.get("archived_snapshots") or {}).get("closest")
    if not snapshot or not snapshot.get("available") or not snapshot.get("url"):
        return None

    snapshot_url = snapshot["url"].replace("http://web.archive.org", "https://web.archive.org", 1)
    result = fetch_url(snapshot_url, retries=1, timeout=timeout)
    if not result.ok:
        logger.warning("fetch_wayback_snapshot: snapshot fetch failed for %s — %s", url, result.error)
        return None
    logger.info("fetch_wayback_snapshot: recovered %s via archived snapshot %s", url, snapshot_url)
    return result.content
