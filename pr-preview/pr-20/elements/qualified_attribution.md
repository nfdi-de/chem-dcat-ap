

# Slot: qualified_attribution


_This slot is described in more detail within the class in which it is used._





URI: [prov:qualifiedAttribution](http://www.w3.org/ns/prov#qualifiedAttribution)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dataset](Dataset.md) | See [DCAT-AP specs:Dataset](https://semiceu |  yes  |
| [AnalysisDataset](AnalysisDataset.md) |  |  no  |
| [NMRAnalysisDataset](NMRAnalysisDataset.md) | A dataset that is the result of a NMRSpectralAnalysis of a ChemicalSample |  no  |
| [ResearchDataset](ResearchDataset.md) | A collection of data, published or curated by a single agent, and available f... |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | prov:qualifiedAttribution |
| native | nfdi4c:qualified_attribution |




## LinkML Source

<details>
```yaml
name: qualified_attribution
description: This slot is described in more detail within the class in which it is
  used.
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
rank: 1000
slot_uri: prov:qualifiedAttribution
alias: qualified_attribution
domain_of:
- Dataset
range: string

```
</details>