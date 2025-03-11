

# Slot: theme


_This slot is described in more detail within the class in which it is used._





URI: [dcat:theme](http://www.w3.org/ns/dcat#theme)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ResearchDataset](ResearchDataset.md) | A collection of data, published or curated by a single agent, and available f... |  no  |
| [Dataset](Dataset.md) | See [DCAT-AP specs:Dataset](https://semiceu |  yes  |
| [NMRAnalysisDataset](NMRAnalysisDataset.md) | A dataset that is the result of a NMRSpectralAnalysis of a ChemicalSample |  no  |
| [AnalysisDataset](AnalysisDataset.md) |  |  no  |
| [DataService](DataService.md) | See [DCAT-AP specs:DataService](https://semiceu |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:theme |
| native | nfdi4c:theme |




## LinkML Source

<details>
```yaml
name: theme
description: This slot is described in more detail within the class in which it is
  used.
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
rank: 1000
slot_uri: dcat:theme
alias: theme
domain_of:
- DataService
- Dataset
range: string

```
</details>