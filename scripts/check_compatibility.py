#!/usr/bin/env python3
"""check_compatibility.py — Check schema dependency compatibility.

For each deployed version of chem-dcat-ap (excluding dev), fetches the
frozen dcat-ap-plus version from the deployed schema and checks whether
that upstream version is still accessible on GitHub Pages.

Supports both version formats:
  New format: version in prefix value
    dcatapplus: https://.../v0.3.0/
  Old format (legacy): version in import path
    dcatapplus:v0.3.0/schema/

Outputs (all written to --output-dir):
  badge.json          shields.io endpoint badge data
  compatibility.html  standalone HTML compatibility matrix
  compatibility.md    MkDocs-compatible markdown compatibility matrix
  status.env          KEY=VALUE pairs for GitHub Actions $GITHUB_OUTPUT

Exit codes:
  0  all released versions valid
  1  some released versions stale, but latest is valid
  2  latest version is stale (critical)

Usage:
  python3 scripts/check_compatibility.py \\
      --chemdcatap-url https://HendrikBorgelt.github.io/test_chemDCAT_ap_versioning_freeze \\
      --dcatapplus-url https://HendrikBorgelt.github.io/test_dcat_ap_plus_versioning_freeze \\
      --output-dir /tmp/compat_output
"""

import argparse
import json
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


# ---------------------------------------------------------------------------
# HTTP helpers
# ---------------------------------------------------------------------------

def fetch_json(url: str) -> list | dict:
    req = urllib.request.Request(
        url, headers={"User-Agent": "chem-dcat-ap-compat-check/1.0"}
    )
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.load(r)


def fetch_text(url: str) -> str | None:
    try:
        req = urllib.request.Request(
            url, headers={"User-Agent": "chem-dcat-ap-compat-check/1.0"}
        )
        with urllib.request.urlopen(req, timeout=15) as r:
            return r.read().decode("utf-8")
    except Exception:
        return None


def url_accessible(url: str) -> bool:
    """Return True if URL responds with HTTP 2xx (HEAD request)."""
    try:
        req = urllib.request.Request(
            url,
            method="HEAD",
            headers={"User-Agent": "chem-dcat-ap-compat-check/1.0"},
        )
        with urllib.request.urlopen(req, timeout=15) as r:
            return r.status < 300
    except Exception:
        return False


# ---------------------------------------------------------------------------
# Freeze-status lookup
# ---------------------------------------------------------------------------

def fetch_freeze_status(chemdcatap_base: str) -> dict:
    """Fetch freeze-status.json from gh-pages. Returns {} on any error.
    The file records whether post-deploy-validate succeeded for each released
    version. Keys are version strings (e.g. 'v0.3.0').
    """
    try:
        req = urllib.request.Request(
            f"{chemdcatap_base}/freeze-status.json",
            headers={"User-Agent": "chem-dcat-ap-compat-check/1.0"},
        )
        with urllib.request.urlopen(req, timeout=15) as r:
            return json.load(r)
    except Exception:
        return {}


# ---------------------------------------------------------------------------
# Schema parsing
# ---------------------------------------------------------------------------

def extract_dcatapplus_version(schema_text: str) -> str | None:
    """Extract the pinned dcatapplus version from either:
    - New format: dcatapplus: https://.../vX.Y.Z/ (version in prefix value)
    - Old format (legacy): dcatapplus:vX.Y.Z/schema/ (version in import path)
    Returns the version string (e.g. 'v0.3.0') or None if not pinned.
    """
    # New format: version in prefix value
    m = re.search(r'dcatapplus:\s+https?://\S+/(v[\d.]+)/', schema_text)
    if m:
        return m.group(1)
    # Old format (legacy): version in import path
    m = re.search(r'dcatapplus:(v[\d.]+)/schema/', schema_text)
    if m:
        return m.group(1)
    return None


# Keep old name as alias for backwards compatibility with any callers
extract_dcatapplus_token = extract_dcatapplus_version


# ---------------------------------------------------------------------------
# Badge
# ---------------------------------------------------------------------------

def compute_badge(stale_count: int, total: int, latest_stale: bool) -> dict:
    """
    Color scale:
      red         → latest version stale (critical)
      yellow      → ≥50% of released versions stale, latest valid
      yellowgreen → some stale but <50%, latest valid
      brightgreen → all valid
    """
    if latest_stale:
        color, message = "red", "latest stale"
    elif stale_count == 0:
        color, message = "brightgreen", "all valid"
    elif total > 0 and stale_count / total >= 0.5:
        color, message = "yellow", f"{stale_count} versions stale"
    else:
        noun = "version" if stale_count == 1 else "versions"
        color, message = "yellowgreen", f"{stale_count} {noun} stale"
    return {
        "schemaVersion": 1,
        "label": "schema deps",
        "message": message,
        "color": color,
    }


# ---------------------------------------------------------------------------
# HTML matrix
# ---------------------------------------------------------------------------

_STATUS_META = {
    "valid":      ("✅", "#2d8a4e", "Valid"),
    "stale":      ("⚠️",  "#d93f0b", "Stale"),
    "no-schema":  ("❓", "#9a6700", "Schema not accessible"),
    "not-frozen": ("🔄", "#0550ae", "Not frozen"),
}


def build_html(results: list[dict], now: str, chemdcatap_url: str, freeze_status: dict) -> str:
    rows = []

    # Dev row — always first, purely informational
    rows.append(
        "<tr>"
        "<td><code>dev</code></td>"
        "<td><em>latest (floating)</em></td>"
        '<td style="color:#57606a">🔄 Development — floating import, not checked</td>'
        '<td style="color:#57606a">—</td>'
        "</tr>"
    )

    for r in results:
        ver = r["version"]
        ver_label = (
            f"<strong>{ver}</strong>&nbsp;<em>(latest)</em>" if r["is_latest"] else ver
        )
        token = r["token"] or "—"
        token_cell = f"<code>{token}</code>"

        icon, color, text = _STATUS_META.get(r["status"], ("❓", "#9a6700", "Unknown"))

        if r["status"] == "stale":
            detail = f"dcat-ap-plus&nbsp;<code>{token}</code> not found on GitHub Pages"
            status_html = f'<td style="color:{color}">{icon} {text} — {detail}</td>'
        elif r["status"] == "no-schema":
            status_html = (
                f'<td style="color:{color}">{icon} {text} — '
                "could not fetch deployed schema</td>"
            )
        else:
            status_html = f'<td style="color:{color}">{icon} {text}</td>'

        fs = freeze_status.get(ver)
        if fs is None:
            freeze_cell = '<td style="color:#57606a">—</td>'
        elif fs.get("validated"):
            freeze_cell = '<td style="color:#2d8a4e">✅ Validated</td>'
        else:
            freeze_cell = '<td style="color:#d93f0b">❌ Failed</td>'

        rows.append(
            f"<tr><td>{ver_label}</td><td>{token_cell}</td>{status_html}{freeze_cell}</tr>"
        )

    rows_html = "\n      ".join(rows)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>chem-dcat-ap — Schema Compatibility Matrix</title>
  <style>
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
      max-width: 960px; margin: 2rem auto; padding: 0 1.5rem;
      color: #24292f; line-height: 1.5;
    }}
    h1 {{ border-bottom: 1px solid #d0d7de; padding-bottom: .5rem; font-size: 1.5rem; }}
    .meta {{ color: #57606a; font-size: .875rem; margin-bottom: 1.5rem; }}
    .meta a {{ color: #0550ae; }}
    table {{ border-collapse: collapse; width: 100%; font-size: .9rem; }}
    th {{
      background: #f6f8fa; text-align: left;
      padding: .5rem .75rem; border: 1px solid #d0d7de; font-weight: 600;
    }}
    td {{ padding: .5rem .75rem; border: 1px solid #d0d7de; vertical-align: middle; }}
    tr:hover td {{ background: #f6f8fa; }}
    code {{
      background: #f6f8fa; border: 1px solid #d0d7de;
      border-radius: 4px; padding: .1em .35em; font-size: .85em;
    }}
    .legend {{ margin-top: 1.5rem; font-size: .85rem; color: #57606a; }}
  </style>
</head>
<body>
  <h1>chem-dcat-ap — Schema Compatibility Matrix</h1>
  <p class="meta">
    Last checked: <strong>{now}</strong> &nbsp;·&nbsp;
    <a href="{chemdcatap_url}">Documentation site</a> &nbsp;·&nbsp;
    Generated by the <code>check-schema-compatibility</code> workflow
  </p>
  <table>
    <thead>
      <tr>
        <th>chem-dcat-ap version</th>
        <th>dcat-ap-plus dependency</th>
        <th>Status</th>
        <th>Freeze validated</th>
      </tr>
    </thead>
    <tbody>
      {rows_html}
    </tbody>
  </table>
  <p class="legend">
    ✅ Valid — the frozen upstream schema URL responds with HTTP 200<br>
    ⚠️ Stale — the frozen upstream schema URL returns 404 or is unreachable<br>
    ❓ Schema not accessible — the deployed chem-dcat-ap schema could not be fetched<br>
    🔄 Development — not a released version, floating import, not checked<br>
    ✅/❌ Freeze validated — result of the post-deploy-validate job; — means no data yet
  </p>
</body>
</html>
"""


# ---------------------------------------------------------------------------
# Markdown matrix (MkDocs-compatible)
# ---------------------------------------------------------------------------

def build_markdown(results: list[dict], now: str, chemdcatap_url: str, freeze_status: dict) -> str:
    """Generate a MkDocs-compatible markdown file with the compatibility matrix."""
    rows = []

    # Dev row — always first, purely informational
    rows.append("| `dev` | *latest (floating)* | 🔄 Not frozen / Development — floating import, not checked | — |")

    for r in results:
        ver = r["version"]
        ver_label = f"**{ver}** *(latest)*" if r["is_latest"] else ver
        token = r["token"] or "—"
        token_cell = f"`{token}`"

        icon, _, text = _STATUS_META.get(r["status"], ("❓", "#9a6700", "Unknown"))

        if r["status"] == "stale":
            status_cell = f"{icon} Stale — dcat-ap-plus `{token}` not found on GitHub Pages"
        elif r["status"] == "no-schema":
            status_cell = f"{icon} Schema not accessible — could not fetch deployed schema"
        elif r["status"] == "not-frozen":
            status_cell = f"🔄 Not frozen / Development — floating import, not checked"
        else:
            status_cell = f"{icon} {text}"

        fs = freeze_status.get(ver)
        if fs is None:
            freeze_cell = "—"
        elif fs.get("validated"):
            freeze_cell = "✅ Validated"
        else:
            freeze_cell = "❌ Failed"

        rows.append(f"| {ver_label} | {token_cell} | {status_cell} | {freeze_cell} |")

    rows_md = "\n".join(rows)

    return f"""---
title: Schema Compatibility
---

# Schema Compatibility Matrix

Last checked: **{now}** · [Documentation site]({chemdcatap_url}) · Generated by the `check-schema-compatibility` workflow

| chem-dcat-ap version | dcat-ap-plus dependency | Status | Freeze validated |
|---|---|---|---|
{rows_md}

**Legend:**

- ✅ Valid — frozen upstream URL responds HTTP 200
- ⚠️ Stale — frozen upstream URL returns 404 or is unreachable
- ❓ Schema not accessible — deployed chem-dcat-ap schema could not be fetched
- 🔄 Not frozen / Development — floating import, not checked
- ✅/❌ Freeze validated — result of the post-deploy-validate job; — means no data yet
"""


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    p = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument(
        "--chemdcatap-url", required=True,
        help="Base GitHub Pages URL for chem-dcat-ap (no trailing slash)",
    )
    p.add_argument(
        "--dcatapplus-url", required=True,
        help="Base GitHub Pages URL for dcat-ap-plus (no trailing slash)",
    )
    p.add_argument(
        "--output-dir", required=True,
        help="Directory to write badge.json, compatibility.html, compatibility.md, status.env",
    )
    args = p.parse_args()

    chemdcatap_base = args.chemdcatap_url.rstrip("/")
    dcatapplus_base = args.dcatapplus_url.rstrip("/")
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------------------
    # Fetch deployed versions
    # ------------------------------------------------------------------
    print(f"Fetching versions from {chemdcatap_base}/versions.json …")
    try:
        versions_data = fetch_json(f"{chemdcatap_base}/versions.json")
    except Exception as exc:
        print(f"ERROR: could not fetch versions.json: {exc}", file=sys.stderr)
        return 2

    latest_version = next(
        (e["version"] for e in versions_data if "latest" in e.get("aliases", [])),
        None,
    )
    print(f"Latest released version: {latest_version}")

    # ------------------------------------------------------------------
    # Fetch freeze-validation status
    # ------------------------------------------------------------------
    print(f"Fetching freeze-status from {chemdcatap_base}/freeze-status.json …")
    freeze_status = fetch_freeze_status(chemdcatap_base)
    print(f"  Found freeze status for {len(freeze_status)} version(s).")

    # ------------------------------------------------------------------
    # Check each released version (dev excluded)
    # ------------------------------------------------------------------
    results: list[dict] = []

    for entry in versions_data:
        version = entry["version"]
        if version == "dev":
            continue

        is_latest = version == latest_version
        schema_url = f"{chemdcatap_base}/{version}/schema/chem_dcat_ap.yaml"
        print(f"  {version} …", end=" ", flush=True)

        schema_text = fetch_text(schema_url)
        if schema_text is None:
            print("schema not accessible")
            results.append({
                "version": version, "is_latest": is_latest,
                "token": None, "status": "no-schema",
            })
            continue

        token = extract_dcatapplus_version(schema_text)
        if token is None or token == "latest":
            print(f"not frozen (token={token!r})")
            results.append({
                "version": version, "is_latest": is_latest,
                "token": token or "not found", "status": "not-frozen",
            })
            continue

        upstream_url = f"{dcatapplus_base}/{token}/schema/dcat_ap_plus.yaml"
        ok = url_accessible(upstream_url)
        print("✅ valid" if ok else "⚠️  STALE")
        results.append({
            "version": version, "is_latest": is_latest,
            "token": token, "status": "valid" if ok else "stale",
        })

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    stale = [r for r in results if r["status"] in ("stale", "no-schema")]
    total = len(results)
    latest_stale = any(r["is_latest"] and r["status"] != "valid" for r in results)
    stale_count = len(stale)
    print(
        f"\nSummary: {total} released version(s), "
        f"{stale_count} stale, latest_stale={latest_stale}"
    )

    # ------------------------------------------------------------------
    # Write badge.json
    # ------------------------------------------------------------------
    badge = compute_badge(stale_count, total, latest_stale)
    (output_dir / "badge.json").write_text(json.dumps(badge, indent=2) + "\n")
    print(f"Badge: {badge['color']} / {badge['message']!r}")

    # ------------------------------------------------------------------
    # Write compatibility.html and compatibility.md
    # ------------------------------------------------------------------
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    html = build_html(results, now, chemdcatap_base, freeze_status)
    (output_dir / "compatibility.html").write_text(html)
    print(f"Wrote compatibility.html ({len(html):,} bytes)")

    md = build_markdown(results, now, chemdcatap_base, freeze_status)
    (output_dir / "compatibility.md").write_text(md)
    print(f"Wrote compatibility.md ({len(md):,} bytes)")

    # ------------------------------------------------------------------
    # Write status.env (KEY=VALUE for GitHub Actions $GITHUB_OUTPUT)
    # ------------------------------------------------------------------
    status_lines = [
        f"latest_stale={'true' if latest_stale else 'false'}",
        f"stale_count={stale_count}",
        f"total_count={total}",
        f"badge_color={badge['color']}",
        f"badge_message={badge['message']}",
    ]
    (output_dir / "status.env").write_text("\n".join(status_lines) + "\n")

    if latest_stale:
        return 2
    if stale_count > 0:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
