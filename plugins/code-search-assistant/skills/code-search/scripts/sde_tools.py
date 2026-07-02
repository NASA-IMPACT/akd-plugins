"""Local tools for the Code Search Agent skill: `sde_search_tool` and `repository_search_tool`.

The agent's two primary discovery tools, shipped as a self-contained, **stdlib-only** script so
the plugin works in Claude Code with no MCP wiring and no packages to install (`python3` only).
Ported from the project's authoritative pydantic-ai `sde_tools.py`. The changes: `httpx` ->
`urllib.request` (stdlib), an added CLI entrypoint for Bash invocation, a display-title helper
(`_title_for`), graceful JSON error handling on runtime failures, and a `note` flagging
unauthenticated GitHub rate limits. Behavior is preserved: the SDE endpoint,
`search_type="hybrid"`, **`min_score=0.0`** (deliberate — weak queries otherwise return nothing),
`repository_search`'s `document_type=["Software and Tools"]` scope, GitHub REST enrichment
(`GITHUB_ACCESS_TOKEN` if set), and the reliability score
(Age*0.20 + Activity*0.25 + Stars*0.25 + Forks*0.15 + History*0.15).

Two surfaces from one file:
  * AKD Labs / pydantic-ai: the top-level `sde_search_tool` / `repository_search_tool` functions
    auto-register as tools (underscore-prefixed helpers are ignored).
  * Claude Code plugin: the skill runs the CLI with Bash, e.g.
      python3 "${CLAUDE_SKILL_DIR}/scripts/sde_tools.py" repository-search --query "adaptive mesh refinement hydrodynamics" --max-results 10
      python3 "${CLAUDE_SKILL_DIR}/scripts/sde_tools.py" sde-search --query "aerosol optical depth retrieval" --limit 10 --doc-type "Software and Tools"
    Runtime failures (SDE/GitHub errors, timeouts, non-200) are caught and returned as JSON on
    stdout — {"error": "...", "total_count": 0, "results": []} — instead of a traceback. (Argument
    errors from argparse still exit non-zero with usage on stderr, as usual.)

The other tools named in the prompt (code_signals, ascl, ads, ads_links_resolver) are MCP-backed
and are NOT included in this script build — see SKILL.md / the plugin README for status.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import urllib.parse
import urllib.request
from datetime import datetime, timezone

SDE_URL = "https://dyejsbdumgpqz.cloudfront.net/api/search"


def _post_json(url: str, payload: dict, timeout: float = 30.0) -> dict:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json", "Accept": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _to_aware(s):
    """Parse an ISO-8601 timestamp to a timezone-aware datetime (UTC), or None if unparseable.

    GitHub always returns `...Z`; this defensively coerces a naive datetime to UTC so a later
    `now - dt` subtraction can't raise TypeError (which would otherwise blank an entire search).
    """
    try:
        dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
    except (ValueError, AttributeError):
        return None
    return dt.replace(tzinfo=timezone.utc) if dt.tzinfo is None else dt


# github.com top-level paths that are site features, not user/org accounts (GitHub reserves
# these names, so a real repo owner can never collide with one).
_GH_RESERVED_OWNERS = frozenset({
    "orgs", "topics", "sponsors", "features", "marketplace", "apps", "collections",
    "about", "pricing", "settings", "notifications", "explore", "search", "login",
    "join", "new", "issues", "pulls", "users",
})


def _gh_owner_repo(url: str):
    """Return ("owner", "repo") for a github.com **repository** URL, else None.

    Uses a real host check (urlparse().hostname == github.com) — `.hostname` normalizes case
    and strips any port / userinfo, unlike a raw `.netloc` compare or a `"github.com" in url`
    substring test (the latter false-matches docs.github.com, github.community, and paths like
    `.../github.com-mirror/...`). Reserved site paths (e.g. /orgs/x, /topics/y) are not repos.
    """
    try:
        p = urllib.parse.urlparse((url or "").strip())
    except Exception:
        return None
    if (p.hostname or "").lower() not in ("github.com", "www.github.com"):
        return None
    parts = [seg for seg in p.path.split("/") if seg]
    if len(parts) < 2:
        return None  # bare host, or /owner with no repo — nothing to enrich
    owner, repo = parts[0], parts[1]
    if owner.lower() in _GH_RESERVED_OWNERS:
        return None  # a github.com site feature (org/topic/sponsor page), not owner/repo
    if repo.endswith(".git"):
        repo = repo[:-4]
    return owner, repo


def _title_for(url: str, doc: dict):
    """Display title: "owner/repo" for GitHub repo URLs; the SDE title for project-site / other URLs.

    For a GitHub repo, "owner/repo" is stable even for deep/query/branch URLs (where the URL
    tail would be a filename or "tree"). For non-GitHub hosts the tail is often "site" /
    "index.html" / a version string, which makes a poor title — so use the SDE `title` there
    (the skill deliberately includes project-website hosts, not just Git repos).
    """
    owner_repo = _gh_owner_repo(url)
    if owner_repo:
        return "/".join(owner_repo)
    # Non-GitHub: prefer the SDE title, but collapse noisy whitespace first and fall back to the
    # URL tail if the title is missing or all-whitespace (which would otherwise collapse to "").
    raw = doc.get("title")
    collapsed = " ".join(raw.split()) if isinstance(raw, str) else None
    tail = (url or "").rstrip("/").split("/")[-1]
    return collapsed or tail or None


def _sde_search_impl(query: str, limit: int = 10, doc_type: str | None = "Software and Tools") -> dict:
    """Search NASA's Science Discovery Engine (SDE) using the unified /api/search endpoint.

    The Science Discovery Engine (SDE) is NASA's centralized search platform that indexes
    scientific data, publications, and resources from multiple NASA data sources including
    CMR (Earth observation), PDS (planetary science), SPASE (heliophysics), GCN (astronomy),
    code repositories, and documentation. This tool uses the /api/search endpoint which
    provides cross-source vector, keyword and hybrid (vector + keyword) semantic search,
    returning unified results across all indexed NASA content.

    Args:
        query: Natural language search query (e.g., "Mars rover spectroscopy data").
        limit: Maximum number of results to return (1-100, default 10).
        doc_type: Optional filter by document type — Data, Documentation, Software and Tools,
            Images, Missions and Instruments. Pass None for no filter.

    Returns documents with: title, url, content (description/snippet), score (relevance),
    division (NASA SMD division), doc_type, and source (sde-cmr, sde-pds4, sde-web, sde-code, ...).
    """
    payload = {
        "page": 1,
        "pageSize": limit,
        "search_term": query,
        "search_type": "hybrid",
        "min_score": 0.0,
    }
    if doc_type:
        payload["filters"] = {"document_type": [doc_type]}

    data = _post_json(SDE_URL, payload, timeout=30.0)

    results = []
    for doc in data.get("documents", []):
        content = (
            doc.get("full_text")
            or doc.get("data_product_desc")
            or doc.get("description")
            or ""
        )
        results.append(
            {
                "title": doc.get("title"),
                "url": doc.get("url"),
                "content": content[:1500],
                "score": doc.get("_score"),
                "division": doc.get("division"),
                "doc_type": doc.get("document_type"),
                "source": doc.get("api_source"),
            }
        )

    return {"total_count": data.get("total_count"), "results": results}


def _repository_search_impl(query: str, max_results: int = 10) -> dict:
    """Search for relevant code and implementations within specialized science repositories.

    This tool performs a targeted search across curated scientific codebases to find
    relevant GitHub repositories with README. It enriches the search results with
    GitHub metadata such as stars, forks, and development activity, which are then
    used to compute a reliability score for each item.

    The reliability score (0-100) is a weighted average of repository maturity, activity, and community trust.

    The formula: Score = (Age * 0.20) + (Activity * 0.25) + (Stars * 0.25) + (Forks * 0.15) + (History * 0.15)

    How components are calculated:
      - Age (20%): Higher for older repos; reaches 100% after 4 years.
      - Activity (25%): Starts at 100% and drops to 0% if the repo hasn't been updated in a year.
      - Stars (25%): Logarithmic scale where ~1,000 stars = 100%.
      - Forks (15%): Logarithmic scale where ~500 forks = 100%.
      - History (15%): Based on the span between the first commit and now; reaches 100% after 4 years.

    Args:
        query: Natural language or keyword search for scientific code / repositories.
        max_results: Maximum number of repositories to return (default 10).
    """
    GH_TOKEN = os.getenv("GITHUB_ACCESS_TOKEN")

    # 1) Search SDE, scoped to code repositories
    payload = {
        "page": 1,
        "pageSize": max_results,
        "search_term": query,
        "search_type": "hybrid",
        "min_score": 0.0,
        "filters": {"document_type": ["Software and Tools"]},
    }
    documents = _post_json(SDE_URL, payload, timeout=30.0).get("documents", [])[:max_results]

    # 2) GitHub metadata (one REST call per repo)
    def github_metadata(url: str) -> dict:
        meta = {
            "stars": 0,
            "forks": 0,
            "watchers": 0,
            "open_issues": 0,
            "created_at": "",
            "last_updated": "",
            "first_commit_date": None,
        }

        owner_repo = _gh_owner_repo(url)
        if not owner_repo:
            return meta
        owner, repo = owner_repo

        headers = {"Accept": "application/vnd.github+json", "User-Agent": "code-search-assistant"}
        if GH_TOKEN:
            headers["Authorization"] = f"Bearer {GH_TOKEN}"

        try:
            req = urllib.request.Request(
                f"https://api.github.com/repos/{owner}/{repo}", headers=headers, method="GET"
            )
            with urllib.request.urlopen(req, timeout=15.0) as r:
                if r.status == 200:
                    g = json.loads(r.read().decode("utf-8"))
                    meta.update(
                        stars=g.get("stargazers_count", 0),
                        forks=g.get("forks_count", 0),
                        watchers=g.get("subscribers_count", 0),
                        open_issues=g.get("open_issues_count", 0),
                        created_at=g.get("created_at") or "",
                        last_updated=g.get("pushed_at") or "",
                    )
        except Exception:
            # Best-effort: rate limits (403), 404s, network errors leave the zeroed default,
            # which yields reliability_score=None (see the note in the returned dict).
            pass

        return meta

    # 3) Reliability score — ported verbatim from akd-ext calculate_reliability_score
    def reliability_score(m: dict):
        if not m or not m.get("created_at"):
            return None

        now = datetime.now(timezone.utc)

        created = _to_aware(m["created_at"])
        if created is None:
            return None  # unparseable created_at -> "not scored" (null), not a real 0.0 score

        score_age = min((now - created).total_seconds() / (24 * 3600) / 1460 * 100, 100) * 0.20

        score_activity = 0.0
        upd = _to_aware(m["last_updated"]) if m.get("last_updated") else None
        if upd is not None:
            d = (now - upd).total_seconds() / (24 * 3600)
            score_activity = max(0, min(100 - (d / 365 * 100), 100)) * 0.25

        score_stars = (
            min(math.log10(m["stars"] + 1) / 3 * 100, 100) * 0.25
            if m.get("stars", 0) > 0
            else 0.0
        )
        score_forks = (
            min(math.log10(m["forks"] + 1) / 2.7 * 100, 100) * 0.15
            if m.get("forks", 0) > 0
            else 0.0
        )

        # NOTE: first_commit_date is never populated by the GitHub /repos response above, so
        # `start` stays == `created` and the History component computes the same value as Age
        # (both are days-since-creation / 1460). Net effect: ~35% of the score is one signal
        # counted twice. Kept faithful to the canonical akd-ext formula; documented here rather
        # than changed. Wiring a true first-commit lookup would need an extra GitHub /commits call.
        start = created
        if m.get("first_commit_date"):
            fc = _to_aware(m["first_commit_date"])
            if fc is not None:
                start = fc

        score_history = min((now - start).total_seconds() / (24 * 3600) / 1460 * 100, 100) * 0.15
        return round(score_age + score_activity + score_stars + score_forks + score_history, 2)

    results = []
    for doc in documents:
        url = doc.get("url") or ""
        meta = github_metadata(url) if _gh_owner_repo(url) else {}
        results.append(
            {
                "title": _title_for(url, doc),
                "url": url,
                "content": (doc.get("full_text") or doc.get("description") or "")[:1500],
                "score": doc.get("_score"),
                "reliability_score": reliability_score(meta) if meta else None,
                "repository_metadata": meta,
            }
        )

    out = {"total_count": len(results), "results": results}
    # Only warn about the rate limit when it can actually bite: at least one GitHub repo result
    # AND no token. (Non-GitHub results also get a null reliability_score, but that has nothing
    # to do with the token, so the note would be misleading there.)
    if not GH_TOKEN and any(_gh_owner_repo(r["url"]) for r in results):
        out["note"] = (
            "GITHUB_ACCESS_TOKEN not set: GitHub enrichment is unauthenticated (60 requests/hour), "
            "so reliability_score may be null for some repos once the limit is hit. A null "
            "reliability_score means 'not scored' (non-GitHub URL, missing metadata, or a "
            "rate-limited/failed lookup) — it never means 'unreliable'."
        )
    return out


# Tool entrypoints
#
# Runtime convention: each top-level function becomes a tool; names starting with an
# underscore are ignored. These wrappers preserve the tool names referenced in agents.md.

def sde_search_tool(query: str, limit: int = 10, doc_type: str | None = "Software and Tools") -> dict:
    return _sde_search_impl(query=query, limit=limit, doc_type=doc_type)


def repository_search_tool(query: str, max_results: int = 10) -> dict:
    return _repository_search_impl(query=query, max_results=max_results)


def _main() -> None:
    parser = argparse.ArgumentParser(description="Code Search Agent local tools (SDE-backed).")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_repo = sub.add_parser("repository-search", help="Curated scientific code repos + reliability score.")
    p_repo.add_argument("--query", required=True)
    p_repo.add_argument("--max-results", type=int, default=10)

    p_sde = sub.add_parser("sde-search", help="NASA Science Discovery Engine unified search.")
    p_sde.add_argument("--query", required=True)
    p_sde.add_argument("--limit", type=int, default=10)
    p_sde.add_argument("--doc-type", default="Software and Tools",
                       help='Document type filter, or "none" for no filter.')

    args = parser.parse_args()
    try:
        if args.cmd == "repository-search":
            out = repository_search_tool(args.query, args.max_results)
        else:
            doc_type = None if str(args.doc_type).lower() in ("", "none", "null") else args.doc_type
            out = sde_search_tool(args.query, args.limit, doc_type)
    except Exception as e:
        # Degrade gracefully: always emit JSON on stdout so the skill can parse it, even on
        # SDE/GitHub downtime, timeouts, or non-200 responses (instead of a Python traceback).
        out = {"error": f"{type(e).__name__}: {e}", "total_count": 0, "results": []}
    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    _main()
