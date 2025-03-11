

# Slot: conforms_to


_This slot is described in more detail within the class in which it is used._





URI: [dcterms:conformsTo](http://purl.org/dc/terms/conformsTo)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dataset](Dataset.md) | See [DCAT-AP specs:Dataset](https://semiceu |  yes  |
| [ResearchDataset](ResearchDataset.md) | A collection of data, published or curated by a single agent, and available f... |  no  |
| [AnalysisDataset](AnalysisDataset.md) |  |  no  |
| [DataService](DataService.md) | See [DCAT-AP specs:DataService](https://semiceu |  yes  |
| [NMRAnalysisDataset](NMRAnalysisDataset.md) | A dataset that is the result of a NMRSpectralAnalysis of a ChemicalSample |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterms:conformsTo |
| native | nfdi4c:conforms_to |




## LinkML Source

<details>
```yaml
name: conforms_to
description: This slot is described in more detail within the class in which it is
  used.
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
rank: 1000
slot_uri: dcterms:conformsTo
alias: conforms_to
domain_of:
- DataService
- Dataset
range: string

```
</details>