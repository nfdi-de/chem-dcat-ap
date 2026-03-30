# Versioning Freeze — Implementation Guide for chem-dcat-ap

This folder contains **drop-in artefacts** for implementing the versioning freeze
pipeline in the real [chem-dcat-ap](https://github.com/nfdi-de/chem-dcat-ap)
repository. Everything here is production-ready (using `w3id.org/nfdi-de/…` URLs)
and was developed and validated in the test repos
[test_dcat_ap_plus_versioning_freeze](https://github.com/HendrikBorgelt/test_dcat_ap_plus_versioning_freeze) and
[test_chemDCAT_ap_versioning_freeze](https://github.com/HendrikBorgelt/test_chemDCAT_ap_versioning_freeze).

**No changes are needed in dcat-ap-plus.** The pipeline is entirely self-contained
within chem-dcat-ap.

---

## The problem being solved

`chem_dcat_ap.yaml`, `chemical_reaction_ap.yaml`, and `material_entities_ap.yaml`
all import dcat-ap-plus via:

```yaml
imports:
  - dcatapplus:latest/schema/dcat_ap_plus
```

`latest` is a **live alias** that mike updates on every dcat-ap-plus release.
This means every previously deployed version of chem-dcat-ap silently switches
to the new dcat-ap-plus the moment it is released — retroactively breaking any
version that was not compatible with the new dcat-ap-plus.

Two fixes work together:

1. **Release-time freeze** — at tag push time, the CI pins the import to the
   specific dcat-ap-plus version that `latest` resolves to at that moment.
   Only the deployed GitHub Pages snapshot carries the pinned import; source
   files are never modified.

2. **Daily upstream check** — a scheduled workflow polls dcat-ap-plus GitHub
   Pages once a day, detects any new release, and automatically opens a
   compatibility freeze PR so maintainers can verify the new version before
   it affects any chem-dcat-ap release.

---

## Folder structure

```
for_direct_implementation_at_chemdcat_ap/
  README.md                            ← This file
  workflows/
    deploy-docs.yaml                   ← Drop-in for .github/workflows/deploy-docs.yaml
    handle-upstream-release.yaml       ← New workflow (add to .github/workflows/)
  scripts/
    freeze_imports.py                  ← Add to scripts/ in chem-dcat-ap
    should_update_latest.py            ← Add to scripts/ in chem-dcat-ap
```

---

## Implementation steps

### 1. Add the scripts

Create a `scripts/` directory in the root of chem-dcat-ap (if it does not exist)
and copy both Python files from `scripts/` here into it.

### 2. Enable Actions to create pull requests (one-time)

In the repository go to **Settings → Actions → General → Workflow permissions**
and tick **"Allow GitHub Actions to create and approve pull requests"**.

Without this, the `handle-upstream-release` workflow will fail when it tries
to open the freeze PR.

### 3. Replace / add the workflows

- Replace `.github/workflows/deploy-docs.yaml` with `workflows/deploy-docs.yaml`
  from this folder.
- Copy `workflows/handle-upstream-release.yaml` into `.github/workflows/`
  (this is a new file — it does not replace anything).

> **Note on action versions:** The production workflow uses stable floating
> tags (`actions/checkout@v4`, `astral-sh/setup-uv@v5`, etc.). Update these
> to whatever your project currently uses if needed.

### 4. Verify locally (optional but recommended)

Run the freeze script in dry-run style to confirm it resolves the alias
correctly — then discard the change:

```bash
# Check which version 'latest' currently resolves to
uv run python scripts/freeze_imports.py \
    --schema-dir src/chem_dcat_ap/schema \
    --prefix dcatapplus \
    --from-alias latest \
    --versions-url https://nfdi-de.github.io/dcat-ap-plus/versions.json

# Revert — the CI never commits this change, but locally you need to undo it
git checkout src/chem_dcat_ap/schema/
```

### 5. Release as usual

The release workflow is **unchanged** — just push a version tag:

```bash
git tag v1.2.0
git push origin v1.2.0
```

The CI will automatically freeze the import and handle the `latest` alias.

---

## How the pipeline works end to end

```
Every day at 08:00 UTC
        │
        ▼
chem-dcat-ap handle-upstream-release.yaml
  • Fetch versions.json from nfdi-de.github.io/dcat-ap-plus
  • Detect current dcatapplus token in source schemas
  • Skip guard A: already up to date? → stop
  • Skip guard B: freeze PR already open? → stop
  • Create branch  freeze/dcatapplus-v1.2.0
  • Commit: dcatapplus:<old>/ → dcatapplus:v1.2.0/
  • Open PR with CI checklist
  • Post notice on every open PR
        │
        ▼
Maintainer reviews freeze PR
  • CI green → merge; main now deterministically targets v1.2.0
  • CI red   → breaking change in v1.2.0; fix schema before merging
        │
        ▼
chem-dcat-ap release: git tag v2.0.0 && git push
        │
        ▼
deploy-docs.yaml (release path)
  • freeze_imports.py: source already has dcatapplus:v1.2.0/ → no-op
  • just gen-doc  →  mike deploy v2.0.0
  • deployed schema at /v2.0.0/schema/ has frozen import
```

The `handle-upstream-release` workflow can also be triggered manually at any
time via **Actions → Handle upstream dcat-ap-plus release → Run workflow** —
useful for an immediate check or to backfill after a missed schedule run.

---

## Design decisions FAQ

### Does the schema `id:` need to be versioned?

**No.** The `id:` field is the stable namespace for concepts defined in the
schema (e.g. `chemdcatap:SubstanceSample`). Versioning it would change the
URI for every concept on every release, breaking RDF compatibility. The
GitHub Pages path already provides versioning context — the deployed file at
`/v1.2.0/schema/chem_dcat_ap.yaml` *is* the versioned artefact. Consumers
who need version-pinned imports reference that path directly.

### Do tests need versioning?

**No.** Tests run against the current branch's schema. On the `main` branch
they always use `dcatapplus:latest/`, which is correct for development. At
release time the freeze runs *before* `just gen-doc`, so any schema-level
validation performed during doc generation also exercises the frozen import.

If you want to additionally run `just test` against the frozen schema in CI
(recommended for critical releases), add a `just test` step *after* the
freeze step in `deploy-docs.yaml`.

### Does test data need versioning?

**No.** Test data files (`tests/data/valid/*.yaml`) live on the branch and
are implicitly versioned by git. When a breaking schema change is introduced,
the test data is updated in the same PR. On a maintenance branch (see below)
the test data reflects that version's schema.

### How do I work on v1.10.4 while v2.0.1 is already live?

Use a **maintenance branch**:

```bash
# Create a v1.x maintenance branch from the last v1 tag
git checkout -b v1.x v1.10.3
```

On the `v1.x` branch, **commit the frozen import** to git (unlike the
`main`-branch approach where only CI freezes it). This ensures that
`just test` works correctly locally and in CI for v1.x:

```bash
# On the v1.x branch, run the freeze and commit the result
uv run python scripts/freeze_imports.py \
    --schema-dir src/chem_dcat_ap/schema \
    --prefix dcatapplus \
    --from-alias latest \
    --versions-url https://nfdi-de.github.io/dcat-ap-plus/versions.json

git add src/chem_dcat_ap/schema/
git commit -m "chore: freeze dcatapplus import to <version> for v1.x maintenance"
```

Now apply your fix, then release:

```bash
git tag v1.10.4
git push origin v1.x v1.10.4
```

The `should_update_latest.py` script will detect that v1.10.4 < v2.0.1 and
**will not overwrite the `latest` alias**. The docs at `/v1.10.4/` will be
deployed cleanly alongside `/v2.0.1/` and `/latest/`.

---

## Summary table

| Concern | Approach |
|---|---|
| Import freeze scope | `src/chem_dcat_ap/schema/*.yaml` only |
| Release-time freeze | CI working copy only — never committed to `main` |
| Upstream change detection | Daily poll of dcat-ap-plus `versions.json` — no secrets, no changes to dcat-ap-plus |
| Duplicate PR guard | Checks for existing `freeze/dcatapplus-<version>` branch before acting |
| Schema `id:` | Unchanged — unversioned stable namespace |
| `latest` alias promotion | Semver-gated via `should_update_latest.py` |
| Test data | Branch-versioned via git, no explicit versioning needed |
| Maintenance releases | `v1.x` branch + committed frozen import |

---

## Optional tools: compatibility badge and matrix

These tools surface the health of all deployed versions to **maintainers**
(via a GitHub Issue) and **downstream users** (via a badge in the README and
a compatibility matrix page).

### Folder structure additions

```
for_direct_implementation_at_chemdcat_ap/
  workflows/
    check-schema-compatibility.yaml   ← New workflow (add to .github/workflows/)
  scripts/
    check_compatibility.py            ← New script (add to scripts/)
```

### What the workflow does

Runs every **Monday at 06:00 UTC** (plus `workflow_dispatch` for manual runs):

1. Checks every deployed version's frozen `dcatapplus:vX.Y.Z/` import against
   dcat-ap-plus GitHub Pages (HTTP HEAD request — no auth needed).
2. Generates `badge.json` and `compatibility.html` and pushes them to the
   **gh-pages root** as stable, version-independent URLs:
   - `https://nfdi-de.github.io/chem-dcat-ap/badge.json`
   - `https://nfdi-de.github.io/chem-dcat-ap/compatibility.html`
3. **Issue on breakage** — if `latest` has newly become stale, opens a
   `schema-dep-stale` issue to notify maintainers. The label is created
   automatically if it does not exist.
4. **Auto-closes** the issue once `latest` is valid again.

`dev` is excluded from all checks and counts — it has a floating import by design.

### Badge color scale

| Badge | Condition |
|---|---|
| 🟢 `all valid` | Every released version's upstream resolves |
| 🟡🟢 `N version(s) stale` | Some older versions stale, `latest` valid, < 50% total |
| 🟡 `N versions stale` | ≥ 50% of released versions stale, `latest` valid |
| 🔴 `latest stale` | The `latest`-aliased version has a broken import |

### Implementation steps

#### 1. Copy the files

- `scripts/check_compatibility.py` → `scripts/check_compatibility.py`
- `workflows/check-schema-compatibility.yaml` → `.github/workflows/check-schema-compatibility.yaml`

#### 2. Add the badge to the README

```markdown
[![schema deps](https://img.shields.io/endpoint?url=https://nfdi-de.github.io/chem-dcat-ap/badge.json&style=flat-square)](https://nfdi-de.github.io/chem-dcat-ap/compatibility.html)
```

#### 3. Run once manually to initialise

After merging, trigger the workflow manually via
**Actions → Check schema compatibility → Run workflow**
to generate the initial `badge.json` and `compatibility.html` before the
first scheduled run.

> The `schema-dep-stale` label and the gh-pages files are all created
> automatically on the first run — no manual setup beyond copying the files.
