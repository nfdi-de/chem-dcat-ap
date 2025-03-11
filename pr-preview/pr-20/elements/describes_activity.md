

# Slot: describes_activity


_A slot to provide the EvaluatedActivity that is described by a Dataset._





URI: [dcterms:relation](http://purl.org/dc/terms/relation)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AnalysisDataset](AnalysisDataset.md) |  |  no  |
| [NMRAnalysisDataset](NMRAnalysisDataset.md) | A dataset that is the result of a NMRSpectralAnalysis of a ChemicalSample |  no  |
| [ResearchDataset](ResearchDataset.md) | A collection of data, published or curated by a single agent, and available f... |  no  |







## Properties

* Range: [EvaluatedActivity](EvaluatedActivity.md)

* Multivalued: True

* Recommended: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterms:relation |
| native | nfdi4c:describes_activity |




## LinkML Source

<details>
```yaml
name: describes_activity
description: A slot to provide the EvaluatedActivity that is described by a Dataset.
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
rank: 1000
slot_uri: dcterms:relation
alias: describes_activity
domain_of:
- ResearchDataset
range: EvaluatedActivity
recommended: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details>