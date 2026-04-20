#!/usr/bin/env python3
"""Decide whether a newly pushed tag should replace the 'latest' mike alias.

Compares the new version against the version currently carrying the 'latest'
alias in this repo's mike versions.json.  Outputs exactly one line:

    true   — new_version >= current_latest  (promote 'latest')
    false  — new_version < current_latest   (keep existing 'latest')

This prevents a maintenance release on an older major branch (e.g. v1.10.4)
from overwriting the 'latest' alias when a newer major (e.g. v2.0.1) is
already live.

On any error (network failure, unparseable version, etc.) the script defaults
to "true" so a release is never silently skipped.

Usage:
    uv run python scripts/should_update_latest.py \\
        --new-version v0.2.0 \\
        --versions-url https://HendrikBorgelt.github.io/test_chemDCAT_ap_versioning_freeze/versions.json

Exit codes
----------
0  Always (the answer is encoded in stdout).
"""

import argparse
import json
import sys
import urllib.request

from packaging.version import InvalidVersion, Version


# ---------------------------------------------------------------------------
# Core helper
# ---------------------------------------------------------------------------

def should_update(new_version_str: str, versions_url: str) -> bool:
    """Return True if new_version_str should become the new 'latest'."""
    try:
        with urllib.request.urlopen(versions_url, timeout=15) as resp:
            versions = json.load(resp)
    except Exception as exc:
        print(
            f"WARNING: Could not fetch {versions_url} ({exc}). "
            "Defaulting to update latest.",
            file=sys.stderr,
        )
        return True

    current_latest_str = next(
        (e["version"] for e in versions if "latest" in e.get("aliases", [])),
        None,
    )

    if current_latest_str is None:
        # No 'latest' alias exists yet — always promote
        return True

    try:
        new_v = Version(new_version_str.lstrip("v"))
        cur_v = Version(current_latest_str.lstrip("v"))
    except InvalidVersion as exc:
        print(
            f"WARNING: Could not parse version for comparison ({exc}). "
            "Defaulting to update latest.",
            file=sys.stderr,
        )
        return True

    return new_v >= cur_v


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument(
        "--new-version",
        required=True,
        help="The version tag just pushed, e.g. 'v0.2.0'.",
    )
    p.add_argument(
        "--versions-url",
        required=True,
        help="URL to *this* repo's mike versions.json.",
    )
    return p


def main() -> int:
    args = build_parser().parse_args()
    result = should_update(args.new_version, args.versions_url)
    print("true" if result else "false")
    return 0


if __name__ == "__main__":
    sys.exit(main())
