#!/usr/bin/env python3
"""Freeze LinkML schema imports and identifiers to specific resolved versions.

This script is called at two points in the release pipeline:

PHASE 2  (post-deploy-validate job, after gh-pages deploy)
---------------------------------------------------------------------------
Full freeze — applies ALL transformations at once to the working copy:

  1. Pin the ``dcatapplus`` prefix value:
       dcatapplus: {base}/          ->  dcatapplus: {base}/{version}/
       (also handles re-freeze: dcatapplus: {base}/vOLD/ -> {base}/vNEW/)

  2. Strip any version/alias token from ``dcatapplus:`` import paths:
       dcatapplus:latest/schema/X   ->  dcatapplus:schema/X

  3. Pin the ``chemdcatap`` prefix value:
       chemdcatap: {base}/          ->  chemdcatap: {base}/{version}/

  4. Convert bare local sub-module imports to ``chemdcatap:schema/`` form:
       - chemical_entities_ap       ->  - chemdcatap:schema/chemical_entities_ap
     (enabled via --convert-bare-imports; only safe after Phase 1 deploy
      because the versioned CURIE URLs must already exist on gh-pages)

  5. Remap and version all ``id:`` fields:
       id: {old_id_base}/path/      ->  id: {new_id_base}/path/{version}/

  6. Remap and version own-namespace prefix declarations:
       my_ns: {old_id_base}/path/   ->  my_ns: {new_id_base}/path/{version}/

The modifications are made to the *working copy only* -- they are NOT
committed back to git. Source files stay in their development form on main
(bare imports, unversioned prefixes). Released GitHub Pages snapshots carry
fully versioned, reproducible imports.

HANDLE-UPSTREAM-RELEASE workflow
---------------------------------------------------------------------------
Only steps 1-2 are invoked (with --dcatapplus-base + --dcatapplus-version,
no --convert-bare-imports, no --schema-id-*) to pin dcatapplus on main.

Usage examples
--------------
Full post-deploy freeze (Phase 2) — production:

    uv run python scripts/freeze_imports.py \\
        --schema-dir src/chem_dcat_ap/schema \\
        --dcatapplus-base https://w3id.org/nfdi-de/dcat-ap-plus \\
        --versions-url https://nfdi-de.github.io/dcat-ap-plus/versions.json \\
        --chemdcatap-base https://nfdi-de.github.io/chem-dcat-ap/chemistry \\
        --chemdcatap-version v0.5.0 \\
        --convert-bare-imports \\
        --schema-id-old-base https://w3id.org/nfdi-de/dcat-ap-plus \\
        --schema-id-new-base https://w3id.org/nfdi-de/dcat-ap-plus

Upstream-release pin only (handle-upstream-release workflow):

    uv run python scripts/freeze_imports.py \\
        --schema-dir src/chem_dcat_ap/schema \\
        --dcatapplus-base https://w3id.org/nfdi-de/dcat-ap-plus \\
        --dcatapplus-version v0.5.0

Exit codes
----------
0  Success.
1  Error -- details on stderr.
"""

import argparse
import json
import re
import sys
import urllib.request
from pathlib import Path


# ---------------------------------------------------------------------------
# Core helpers
# ---------------------------------------------------------------------------

def resolve_alias(versions_url: str, alias: str = "latest") -> str:
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


def freeze_dcatapplus_prefix(text: str, base: str, version: str) -> str:
    """Pin the dcatapplus prefix value: base/ -> base/version/

    Replaces lines like:
      dcatapplus: https://w3id.org/nfdi-de/dcat-ap-plus/
    with:
      dcatapplus: https://w3id.org/nfdi-de/dcat-ap-plus/v0.3.0/

    Also handles re-freeze when the prefix is already pinned to a previous
    version, e.g.:
      dcatapplus: https://w3id.org/nfdi-de/dcat-ap-plus/v0.3.0/
    ->
      dcatapplus: https://w3id.org/nfdi-de/dcat-ap-plus/v0.4.0/
    """
    new = f"dcatapplus: {base}/{version}/\n"
    # First try exact match on the base form (most common during first freeze)
    old_base = f"dcatapplus: {base}/\n"
    if old_base in text:
        return text.replace(old_base, new)
    # Fall back: replace any already-versioned form  dcatapplus: {base}/{token}/
    return re.sub(
        r"dcatapplus: " + re.escape(base) + r"/[^/\s]+/\n",
        new,
        text,
    )


def strip_dcatapplus_import_path_token(text: str) -> str:
    """Remove any version/alias token from dcatapplus import paths.

    Handles patterns like:
      - dcatapplus:latest/schema/foo   -> dcatapplus:schema/foo
      - dcatapplus:v0.3.0/schema/foo  -> dcatapplus:schema/foo

    Only matches when there is a token (non-colon, non-slash chars) between
    'dcatapplus:' and '/schema/' -- does not touch lines already in the
    'dcatapplus:schema/' form.
    """
    return re.sub(r"dcatapplus:[^:/\s]+/schema/", "dcatapplus:schema/", text)


def freeze_chemdcatap_prefix(text: str, base: str, version: str) -> str:
    """Pin the chemdcatap prefix value: base/ -> base/version/

    Replaces lines like:
      chemdcatap: https://nfdi-de.github.io/chem-dcat-ap/chemistry/
    with:
      chemdcatap: https://nfdi-de.github.io/chem-dcat-ap/chemistry/v0.2.0/

    Also handles re-freeze from a previously versioned value.
    """
    new = f"chemdcatap: {base}/{version}/\n"
    old_base = f"chemdcatap: {base}/\n"
    if old_base in text:
        return text.replace(old_base, new)
    # Fallback: replace already-versioned form
    return re.sub(
        r"chemdcatap: " + re.escape(base) + r"/[^/\s]+/\n",
        new,
        text,
    )


def convert_bare_imports(text: str) -> str:
    """Convert bare local sub-module imports to prefixed CURIE form.

    For each bare import name, checks whether a matching named prefix is
    declared in the schema. If so, uses that prefix as the CURIE namespace:
      - chemical_entities_ap  ->  - chemical_entities_ap:schema/chemical_entities_ap

    If no matching prefix is declared, falls back to the chemdcatap: prefix:
      - chemical_entities_ap  ->  - chemdcatap:schema/chemical_entities_ap

    This handles two deployment scenarios:

    - Production (w3id.org): each sub-schema has its own prefix pointing to
      a distinct w3id path (chemistry/entity/, chemistry/reaction/, etc.).
      Using that prefix ensures the CURIE resolves to the correct w3id URL.
      The sub-module prefix declarations must exist in the source schema:
        chemical_entities_ap: https://w3id.org/nfdi-de/dcat-ap-plus/chemistry/entity/

    - Test repo: all sub-schemas are deployed under a single chemdcatap: path,
      so no individual prefix is declared and the chemdcatap: fallback is used.

    Only items inside the top-level ``imports:`` block are converted.
    Class-level slot lists, mixin lists, etc. are left untouched.
    Already-prefixed imports (containing ':') are never touched.

    NOTE: only safe to run AFTER the schemas have been deployed to gh-pages,
    because the resolved CURIE URLs must already exist at the versioned path.
    Enable via --convert-bare-imports.
    """
    # Collect all declared prefix names so we can pick the right CURIE namespace
    # for each bare import (two-space-indented prefix declarations).
    declared_prefixes = set(re.findall(r'^  ([A-Za-z][A-Za-z0-9_-]*):', text, re.MULTILINE))

    lines = text.splitlines(keepends=True)
    result = []
    in_imports_block = False
    for line in lines:
        stripped = line.rstrip()

        # Detect the start of the top-level imports: block.
        if re.match(r'^imports:\s*$', stripped):
            in_imports_block = True
            result.append(line)
            continue

        # Any new top-level key (no leading whitespace, not a comment, not a
        # bare list item) signals the end of the imports block.
        if stripped and stripped[0] not in (' ', '\t', '#') and not stripped.startswith('-'):
            in_imports_block = False

        if in_imports_block:
            m = re.match(r'^(\s+- )([A-Za-z][A-Za-z0-9_-]+)\s*$', line)
            if m and ':' not in m.group(2) and '/' not in m.group(2):
                name = m.group(2)
                prefix = name if name in declared_prefixes else "chemdcatap"
                result.append(f"{m.group(1)}{prefix}:schema/{name}\n")
                continue

        result.append(line)
    return "".join(result)


def freeze_schema_id(text: str, old_base: str, new_base: str, version: str) -> str:
    """Remap and version the ``id:`` field of a schema.

    Replaces any line of the form:
      id: {old_base}{suffix}/

    with:
      id: {new_base}{suffix}/{version}/

    For example, with old_base=new_base=https://w3id.org/nfdi-de/dcat-ap-plus,
    version=v0.5.0:

      id: https://w3id.org/nfdi-de/dcat-ap-plus/chemistry/
      -> id: https://w3id.org/nfdi-de/dcat-ap-plus/chemistry/v0.5.0/

      id: https://w3id.org/nfdi-de/dcat-ap-plus/chemistry/entity/
      -> id: https://w3id.org/nfdi-de/dcat-ap-plus/chemistry/entity/v0.5.0/

    When old_base == new_base (standard production case) the function simply
    inserts the version token without changing the base URL.
    """
    def _replace(m: re.Match) -> str:
        suffix = m.group(1).rstrip("/")   # e.g. "/chemistry" or "/chemistry/entity"
        return f"id: {new_base}{suffix}/{version}/"

    return re.sub(
        r"^id: " + re.escape(old_base) + r"(/[^\n]*/)$",
        _replace,
        text,
        flags=re.MULTILINE,
    )


def freeze_own_namespace_prefixes(
    text: str, old_base: str, new_base: str, version: str
) -> str:
    """Remap and version sub-schema own-namespace prefix declarations.

    Matches any indented prefix line (two leading spaces) whose value
    starts with ``old_base`` and ends with ``/``, EXCEPT the reserved
    names ``chemdcatap`` and ``dcatapplus`` (handled separately).

    For example (production, old_base == new_base == w3id.org base):
      chemical_entities_ap: https://w3id.org/nfdi-de/dcat-ap-plus/chemistry/entity/
      -> chemical_entities_ap: https://w3id.org/nfdi-de/dcat-ap-plus/chemistry/entity/v0.5.0/

      material_entities_ap: https://w3id.org/nfdi-de/dcat-ap-plus/materials/
      -> material_entities_ap: https://w3id.org/nfdi-de/dcat-ap-plus/materials/v0.5.0/
    """
    def _replace(m: re.Match) -> str:
        prefix_name = m.group(1)
        suffix = m.group(2).rstrip("/")   # e.g. "/chemistry/entity"
        return f"  {prefix_name}: {new_base}{suffix}/{version}/"

    # Exclude chemdcatap and dcatapplus — they are frozen by their own functions
    return re.sub(
        r"^  (?!chemdcatap|dcatapplus)([A-Za-z][A-Za-z0-9_-]*): "
        + re.escape(old_base)
        + r"(/[^\n]*/)$",
        _replace,
        text,
        flags=re.MULTILINE,
    )


def process_file(
    yaml_file: Path,
    dcatapplus_base: str | None,
    dcatapplus_version: str | None,
    chemdcatap_base: str | None,
    chemdcatap_version: str | None,
    convert_bare: bool,
    schema_id_old_base: str | None,
    schema_id_new_base: str | None,
    sub_module_base: str | None = None,
) -> bool:
    """Apply all requested freezes to one file. Returns True if the file changed."""
    text = yaml_file.read_text(encoding="utf-8")
    original = text

    # 1. Pin dcatapplus prefix + strip import path token
    if dcatapplus_base and dcatapplus_version:
        text = freeze_dcatapplus_prefix(text, dcatapplus_base, dcatapplus_version)
        text = strip_dcatapplus_import_path_token(text)

    # 2. Pin chemdcatap prefix
    if chemdcatap_base and chemdcatap_version:
        text = freeze_chemdcatap_prefix(text, chemdcatap_base, chemdcatap_version)

    # 3. Convert bare local imports to prefixed CURIE form.
    #    Uses each module's own declared prefix when available; falls back to
    #    chemdcatap: for modules without an individual prefix declaration.
    #    Only safe after Phase 1 deploy (versioned URLs must already exist).
    if convert_bare and chemdcatap_base and chemdcatap_version:
        text = convert_bare_imports(text)

    # 4. Remap + version id: field
    if schema_id_old_base and schema_id_new_base and chemdcatap_version:
        text = freeze_schema_id(
            text, schema_id_old_base, schema_id_new_base, chemdcatap_version
        )

    # 5. Version own-namespace prefix declarations.
    #    Two independent code paths:
    #    a) --sub-module-base: versions prefixes matching the given base WITHOUT
    #       touching id: fields. Use in production where sub-schemas have distinct
    #       w3id paths (chemistry/entity/, chemistry/reaction/, materials/, etc.).
    #    b) --schema-id-*: also remaps the base URL in id: fields. Use in the test
    #       repo where id: fields must be redirected to the test GitHub Pages URL.
    if sub_module_base and chemdcatap_version:
        text = freeze_own_namespace_prefixes(
            text, sub_module_base, sub_module_base, chemdcatap_version
        )
    elif schema_id_old_base and schema_id_new_base and chemdcatap_version:
        text = freeze_own_namespace_prefixes(
            text, schema_id_old_base, schema_id_new_base, chemdcatap_version
        )

    if text != original:
        yaml_file.write_text(text, encoding="utf-8")
        return True
    return False


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
    # --- dcatapplus ---
    p.add_argument(
        "--dcatapplus-base",
        default=None,
        help=(
            "Base URL for the dcatapplus prefix, no trailing slash. "
            "e.g. https://w3id.org/nfdi-de/dcat-ap-plus"
        ),
    )
    p.add_argument(
        "--dcatapplus-version",
        default=None,
        help=(
            "Explicit version to pin dcatapplus to (e.g. 'v0.3.0'). "
            "If omitted and --versions-url is given, the 'latest' alias is resolved."
        ),
    )
    p.add_argument(
        "--versions-url",
        default=None,
        help=(
            "URL to the mike versions.json of the upstream dcat-ap-plus repo. "
            "Used to auto-resolve the 'latest' alias when --dcatapplus-version "
            "is not given."
        ),
    )
    # --- chemdcatap ---
    p.add_argument(
        "--chemdcatap-base",
        default=None,
        help=(
            "Base URL for the chemdcatap prefix, no trailing slash. "
            "e.g. https://nfdi-de.github.io/chem-dcat-ap/chemistry"
        ),
    )
    p.add_argument(
        "--chemdcatap-version",
        default=None,
        help="Version to pin chemdcatap to (e.g. the current release tag 'v0.2.0').",
    )
    # --- bare import conversion ---
    p.add_argument(
        "--convert-bare-imports",
        action="store_true",
        default=False,
        help=(
            "Convert bare local sub-module imports to chemdcatap:schema/ CURIE form. "
            "Only safe to run AFTER the schemas have been deployed to gh-pages "
            "(Phase 2 / post-deploy-validate job), because the CURIE URLs must "
            "already exist at the versioned path."
        ),
    )
    # --- sub-module prefix versioning ---
    p.add_argument(
        "--sub-module-base",
        default=None,
        help=(
            "Base URL for versioning sub-module prefix declarations, no trailing slash. "
            "e.g. https://w3id.org/nfdi-de/dcat-ap-plus  "
            "Versions any indented prefix whose value starts with this base: "
            "  name: {base}/path/  ->  name: {base}/path/{version}/  "
            "using --chemdcatap-version as the version token. "
            "Use in production repos where sub-schemas have individual w3id paths "
            "(chemistry/entity/, chemistry/reaction/, materials/, etc.). "
            "Requires --chemdcatap-version. Does NOT affect id: fields "
            "(contrast with --schema-id-old-base which also remaps id: fields)."
        ),
    )
    # --- id: and own-namespace remapping ---
    p.add_argument(
        "--schema-id-old-base",
        default=None,
        help=(
            "Base URL currently used in schema id: fields and own-namespace prefixes. "
            "e.g. https://w3id.org/nfdi-de/dcat-ap-plus  "
            "Will be replaced with --schema-id-new-base and the version injected."
        ),
    )
    p.add_argument(
        "--schema-id-new-base",
        default=None,
        help=(
            "Replacement base URL for schema id: fields and own-namespace prefixes. "
            "For production use, set this to the same value as --schema-id-old-base "
            "(w3id.org) so only the version is injected without changing the base URL."
        ),
    )
    return p


def main() -> int:
    args = build_parser().parse_args()

    schema_dir = Path(args.schema_dir)
    if not schema_dir.is_dir():
        print(f"ERROR: not a directory: {schema_dir}", file=sys.stderr)
        return 1

    # ------------------------------------------------------------------
    # Validate argument combinations
    # ------------------------------------------------------------------
    if args.schema_id_old_base and not args.schema_id_new_base:
        print(
            "ERROR: --schema-id-old-base requires --schema-id-new-base.",
            file=sys.stderr,
        )
        return 1
    if args.schema_id_new_base and not args.schema_id_old_base:
        print(
            "ERROR: --schema-id-new-base requires --schema-id-old-base.",
            file=sys.stderr,
        )
        return 1
    if args.schema_id_old_base and not args.chemdcatap_version:
        print(
            "ERROR: --schema-id-old-base requires --chemdcatap-version "
            "(used as the version token for id: and namespace prefix freeze).",
            file=sys.stderr,
        )
        return 1
    if args.convert_bare_imports and not (args.chemdcatap_base and args.chemdcatap_version):
        print(
            "ERROR: --convert-bare-imports requires --chemdcatap-base and "
            "--chemdcatap-version (needed to version the chemdcatap: fallback prefix).",
            file=sys.stderr,
        )
        return 1
    if args.sub_module_base and not args.chemdcatap_version:
        print(
            "ERROR: --sub-module-base requires --chemdcatap-version "
            "(used as the version token for sub-module prefix versioning).",
            file=sys.stderr,
        )
        return 1

    # ------------------------------------------------------------------
    # Resolve dcatapplus version
    # ------------------------------------------------------------------
    dcatapplus_version: str | None = None
    if args.dcatapplus_base:
        if args.dcatapplus_version:
            dcatapplus_version = args.dcatapplus_version
        elif args.versions_url:
            print(f"Resolving 'latest' alias from: {args.versions_url}")
            try:
                dcatapplus_version = resolve_alias(args.versions_url, "latest")
            except Exception as exc:
                print(f"ERROR: {exc}", file=sys.stderr)
                return 1
            print(f"  -> resolved to: {dcatapplus_version}")
        else:
            print(
                "ERROR: --dcatapplus-base given but neither --dcatapplus-version "
                "nor --versions-url was provided.",
                file=sys.stderr,
            )
            return 1

    chemdcatap_version: str | None = args.chemdcatap_version

    # Require at least one operation
    has_work = (
        bool(dcatapplus_version)
        or bool(chemdcatap_version)
        or args.convert_bare_imports
        or bool(args.schema_id_old_base)
        or bool(args.sub_module_base)
    )
    if not has_work:
        print(
            "ERROR: nothing to do -- provide at least one of: "
            "--dcatapplus-version (or --versions-url), --chemdcatap-version, "
            "--convert-bare-imports, --schema-id-old-base.",
            file=sys.stderr,
        )
        return 1

    # ------------------------------------------------------------------
    # Process all YAML files in schema_dir
    # ------------------------------------------------------------------
    changed_files: list[str] = []
    for yaml_file in sorted(schema_dir.glob("*.yaml")):
        if process_file(
            yaml_file,
            dcatapplus_base=args.dcatapplus_base,
            dcatapplus_version=dcatapplus_version,
            chemdcatap_base=args.chemdcatap_base,
            chemdcatap_version=chemdcatap_version,
            convert_bare=args.convert_bare_imports,
            schema_id_old_base=args.schema_id_old_base,
            schema_id_new_base=args.schema_id_new_base,
            sub_module_base=args.sub_module_base,
        ):
            changed_files.append(yaml_file.name)

    if changed_files:
        print(f"Modified files: {', '.join(changed_files)}")
    else:
        print(f"No files changed in {schema_dir}")

    # ------------------------------------------------------------------
    # Emit machine-parseable KEY=VALUE lines for shell callers
    # ------------------------------------------------------------------
    if dcatapplus_version:
        print(f"FROZEN_VERSION={dcatapplus_version}")
    if chemdcatap_version:
        print(f"FROZEN_CHEMDCATAP_VERSION={chemdcatap_version}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
