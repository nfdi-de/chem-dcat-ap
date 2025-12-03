# Versioning of the dcat-ap-plus model

The versioning of the dcat-ap-plus model is following the **SchemaVer** scheme proposed in a [snowplow blog post](https://snowplow.io/blog/introducing-schemaver-for-semantic-versioning-of-schemas). The same principles are applied for the [HCA schema versioning](https://github.com/HumanCellAtlas/metadata-schema/blob/master/docs/evolution.md#schema-versioning). SchemaVer is also adapted by [openlineage](https://github.com/OpenLineage/OpenLineage/blob/main/spec/Versioning.md).

**SchemaVer**: Given a version number MODEL.REVISION.ADDITION, increment the

- MODEL when you make a breaking schema change which will prevent interaction with any historical data
- REVISION when you make a schema change which may prevent interaction with some historical data
- ADDITION when you make a schema change that is compatible with all historical data

The versions are tagged in git (for example "v1.2.3").
Based on the tags we also create GitHub releases to provide easy access to all versions and to document the changes between versions.
