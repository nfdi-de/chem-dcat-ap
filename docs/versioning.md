# Versioning of ChemDCAT-AP

## Versioning scheme: SchemaVer

ChemDCAT-AP follows the **SchemaVer** scheme ([introduced by Snowplow](https://snowplow.io/blog/introducing-schemaver-for-semantic-versioning-of-schemas), also used by [Human Cell Atlas](https://github.com/HumanCellAtlas/metadata-schema/blob/master/docs/evolution.md#schema-versioning) and [OpenLineage](https://github.com/OpenLineage/OpenLineage/blob/main/spec/Versioning.md)). SchemaVer is designed for data schemas, where the critical question is *"will existing data still validate?"*, unlike SemVer, which is designed for code APIs.

Given a version number **MODEL.REVISION.ADDITION**:

| Increment | When | Effect on existing data |
|---|---|---|
| **MODEL** | A breaking schema change that prevents interaction with *any* historical data (e.g. removing a mandatory slot, changing a `class_uri`) | All existing data must be migrated |
| **REVISION** | A schema change that may prevent interaction with *some* historical data (e.g. making an optional slot mandatory, narrowing a range) | Some existing data may need updates |
| **ADDITION** | A schema change compatible with *all* historical data (e.g. adding a new optional slot, adding a new class) | No data migration needed |

### Examples of each level

- **ADDITION** (0.1.0 → 0.1.1): Adding an optional `comment` slot to `DataGeneratingActivity`
- **REVISION** (0.1.x → 0.2.0): Making `rdf_type` on `DataGeneratingActivity` mandatory (previously recommended)
- **MODEL** (0.x.y → 1.0.0): Restructuring the `QuantitativeAttribute` to use a different ontology alignment

Versions are tagged in git (e.g. `v1.2.3`) and published as [GitHub releases](https://github.com/nfdi-de/chem-dcat-ap/releases) with changelogs.

## Relationship to DCAT-AP+ versions

ChemDCAT-AP imports DCAT-AP+, which in turn tracks [DCAT-AP](https://github.com/SEMICeu/DCAT-AP/releases). Changes in either upstream schema propagate to ChemDCAT-AP, but not automatically.

ChemDCAT-AP will soon **pin its import to a specific DCAT-AP+ version** rather than always importing the latest release (see [this PR](https://github.com/nfdi-de/chem-dcat-ap/pull/123)). This ensures that a tested, production-stable combination of schemas is used. The pinned version is visible in the `imports` section of `chem_dcat_ap.yaml`. When a new DCAT-AP+ release is available, the ChemDCAT-AP maintainers evaluate its impact, update the pinned version, and run the full test suite before merging.

The version impact on ChemDCAT-AP depends on the nature of the change, whether upstream or internal:
 
| Change | Version impact |
|---|---|
| DCAT-AP+ adds new optional slots or classes | ADDITION (new capabilities available, no breaking changes) |
| DCAT-AP+ changes cardinality, ranges, or `slot_uri` values | REVISION or MODEL, depending on whether ChemDCAT-AP's own classes or slots are affected |
| Major DCAT-AP+ version change | Likely MODEL bump |
| ChemDCAT-AP adds new classes, slots, or mixins | ADDITION |
| ChemDCAT-AP narrows a range, adds a required constraint, or changes a `class_uri`/`slot_uri` | REVISION (if backward-compatible) or MODEL (if breaking) |
| ChemDCAT-AP removes or renames a class or slot | MODEL |

## Dynamic versioning in development

During development, the version string in the schema YAML header is managed by [`setuptools-scm` / `hatch-vcs`](https://github.com/pypa/hatch-vcs) via a dynamic versioning plugin. This is why the schema header shows a version like:

```yaml
version: "0.1.0rc3.post21.dev0+913fb36"
```

This string is **auto-generated from git tags**. Hence, it should not be edited manually. The components mean:

| Part | Meaning |
|---|---|
| `0.1.0rc3` | The last git tag (release candidate 3 of version 0.1.0) |
| `.post21` | 21 commits since that tag |
| `.dev0` | Development build |
| `+913fb36` | The git commit hash |

On tagged releases, the version simplifies to the clean SchemaVer string (e.g. `0.1.0`).
