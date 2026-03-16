#!/usr/bin/env python3
"""Freeze LinkML schema import aliases to a specific resolved version.

At release time the CI calls this script to replace every occurrence of
``{prefix}:{alias}/`` (e.g. ``dcatapplus:latest/``) in the schema YAML
files with the concrete version that the alias currently points to
(e.g. ``dcatapplus:v0.2.0/``).

The modification is made to the *working copy only* — it is **not**
committed back to git. This keeps the source files permanently set to
``latest`` for development convenience while ensuring every released
snapshot on GitHub Pages carries a frozen, reproducible import.

Usage (auto-resolve the alias via mike versions.json):
    uv run python scripts/freeze_imports.py \\
        --schema-dir src/chem_dcat_ap/schema \\
        --prefix dcatapplus \\
        --from-alias latest \\
        --versions-url https://HendrikBorgelt.github.io/test_dcat_ap_plus_versioning_freeze/versions.json

Usage (explicit version):
    uv run python scripts/freeze_imports.py \\
        --schema-dir src/chem_dcat_ap/schema \\
        --prefix dcatapplus \\
        --from-alias latest \\
        --to-version v0.2.0

Exit codes
----------
0  Success. The resolved/used version is printed as ``FROZEN_VERSION=<v>``
   on the last line of stdout so shell callers can capture it easily.
1  Error — details on stderr.
"""

import argparse
import json
import sys
import urllib.request
from pathlib import Path


# ---------------------------------------------------------------------------
# Core helpers
# ---------------------------------------------------------------------------

def resolve_alias(versions_url: str, alias: str) -> str:
    """Return the version string that currently carries *alias* in mike's versions.json."""
    try:
        with urllib.request.urlopen(versions_url, timeout=15) as resp:
            versions = json.load(resp)
    except Exception as exc:
        raise RuntimeError(f"Could not fetch {versions_url}: {exc}") from exc

    for entry in versions:
        if alias in entry.get("aliases", []):
            return entry["version"]

    available = [e.get("version") for e in versions]
    raise ValueError(
        f"Alias '{alias}' not found in {versions_url}. "
        f"Available versions: {available}"
    )


def freeze_in_dir(
    schema_dir: Path, prefix: str, from_alias: str, to_version: str
) -> list:
    """Replace ``prefix:from_alias/`` with ``prefix:to_version/`` in all YAML files.

    Returns the list of file names that were actually changed.
    """
    old_token = f"{prefix}:{from_alias}/"
    new_token = f"{prefix}:{to_version}/"
    changed = []
    for yaml_file in sorted(schema_dir.glob("*.yaml")):
        text = yaml_file.read_text(encoding="utf-8")
        if old_token in text:
            yaml_file.write_text(text.replace(old_token, new_token), encoding="utf-8")
            changed.append(yaml_file.name)
    return changed


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument(
        "--schema-dir",
        required=True,
        help="Directory containing the schema YAML files to update.",
    )
    p.add_argument(
        "--prefix",
        required=True,
        help="The LinkML prefix whose alias should be frozen, e.g. 'dcatapplus'.",
    )
    p.add_argument(
        "--from-alias",
        default="latest",
        help="The alias token to replace in import paths (default: 'latest').",
    )
    p.add_argument(
        "--to-version",
        default=None,
        help=(
            "Explicit version to freeze to (e.g. 'v0.2.0'). "
            "Mutually exclusive with --versions-url. "
            "If both are given, --to-version takes precedence."
        ),
    )
    p.add_argument(
        "--versions-url",
        default=None,
        help=(
            "URL to the mike versions.json of the upstream schema repo "
            "(used to auto-resolve the alias when --to-version is not given)."
        ),
    )
    return p


def main() -> int:
    args = build_parser().parse_args()

    schema_dir = Path(args.schema_dir)
    if not schema_dir.is_dir():
        print(f"ERROR: not a directory: {schema_dir}", file=sys.stderr)
        return 1

    # Resolve target version
    if args.to_version:
        version = args.to_version
    elif args.versions_url:
        print(f"Resolving alias '{args.from_alias}' from: {args.versions_url}")
        try:
            version = resolve_alias(args.versions_url, args.from_alias)
        except Exception as exc:
            print(f"ERROR: {exc}", file=sys.stderr)
            return 1
        print(f"  -> resolved to: {version}")
    else:
        print(
            "ERROR: provide either --to-version or --versions-url.",
            file=sys.stderr,
        )
        return 1

    changed = freeze_in_dir(schema_dir, args.prefix, args.from_alias, version)

    if changed:
        old_token = f"{args.prefix}:{args.from_alias}/"
        new_token = f"{args.prefix}:{version}/"
        print(f"Froze '{old_token}' -> '{new_token}'")
        print(f"Modified files: {', '.join(changed)}")
    else:
        old_token = f"{args.prefix}:{args.from_alias}/"
        print(f"Nothing to freeze: '{old_token}' not found in {schema_dir}")

    # Emit version in a machine-parseable form for shell callers
    print(f"FROZEN_VERSION={version}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
