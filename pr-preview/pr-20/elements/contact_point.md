

# Slot: contact_point


_This slot is described in more detail within the class in which it is used._





URI: [dcat:contactPoint](http://www.w3.org/ns/dcat#contactPoint)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AnalysisDataset](AnalysisDataset.md) |  |  no  |
| [NMRAnalysisDataset](NMRAnalysisDataset.md) | A dataset that is the result of a NMRSpectralAnalysis of a ChemicalSample |  no  |
| [DatasetSeries](DatasetSeries.md) | See [DCAT-AP specs:DatasetSeries](https://semiceu |  yes  |
| [ResearchDataset](ResearchDataset.md) | A collection of data, published or curated by a single agent, and available f... |  no  |
| [Dataset](Dataset.md) | See [DCAT-AP specs:Dataset](https://semiceu |  yes  |
| [DataService](DataService.md) | See [DCAT-AP specs:DataService](https://semiceu |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:contactPoint |
| native | nfdi4c:contact_point |




## LinkML Source

<details>
```yaml
name: contact_point
description: This slot is described in more detail within the class in which it is
  used.
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
rank: 1000
slot_uri: dcat:contactPoint
alias: contact_point
domain_of:
- DataService
- Dataset
- DatasetSeries
range: string

```
</details>