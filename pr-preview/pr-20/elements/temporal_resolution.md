

# Slot: temporal_resolution


_This slot is described in more detail within the class in which it is used._





URI: [dcat:temporalResolution](http://www.w3.org/ns/dcat#temporalResolution)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AnalysisDataset](AnalysisDataset.md) |  |  no  |
| [NMRAnalysisDataset](NMRAnalysisDataset.md) | A dataset that is the result of a NMRSpectralAnalysis of a ChemicalSample |  no  |
| [Distribution](Distribution.md) | See [DCAT-AP specs:Distribution](https://semiceu |  yes  |
| [ResearchDataset](ResearchDataset.md) | A collection of data, published or curated by a single agent, and available f... |  no  |
| [Dataset](Dataset.md) | See [DCAT-AP specs:Dataset](https://semiceu |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:temporalResolution |
| native | nfdi4c:temporal_resolution |




## LinkML Source

<details>
```yaml
name: temporal_resolution
description: This slot is described in more detail within the class in which it is
  used.
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
rank: 1000
slot_uri: dcat:temporalResolution
alias: temporal_resolution
domain_of:
- Dataset
- Distribution
range: string

```
</details>