

# Slot: describes_entity


_A slot to provide the EvaluatedEntity that is described by a Dataset._





URI: [dcterms:relation](http://purl.org/dc/terms/relation)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AnalysisDataset](AnalysisDataset.md) |  |  no  |
| [NMRAnalysisDataset](NMRAnalysisDataset.md) | A dataset that is the result of a NMRSpectralAnalysis of a ChemicalSample |  yes  |
| [ResearchDataset](ResearchDataset.md) | A collection of data, published or curated by a single agent, and available f... |  no  |







## Properties

* Range: [EvaluatedEntity](EvaluatedEntity.md)

* Multivalued: True

* Recommended: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterms:relation |
| native | nfdi4c:describes_entity |




## LinkML Source

<details>
```yaml
name: describes_entity
description: A slot to provide the EvaluatedEntity that is described by a Dataset.
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
rank: 1000
slot_uri: dcterms:relation
alias: describes_entity
domain_of:
- ResearchDataset
range: EvaluatedEntity
recommended: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details>