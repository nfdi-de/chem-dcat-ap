

# Slot: geographical_coverage


_This slot is described in more detail within the class in which it is used._





URI: [dcterms:spatial](http://purl.org/dc/terms/spatial)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Catalogue](Catalogue.md) | See [DCAT-AP specs:Catalogue](https://semiceu |  yes  |
| [Dataset](Dataset.md) | See [DCAT-AP specs:Dataset](https://semiceu |  yes  |
| [ResearchCatalog](ResearchCatalog.md) | A curated collection of metadata about data resources |  no  |
| [NMRAnalysisDataset](NMRAnalysisDataset.md) | A dataset that is the result of a NMRSpectralAnalysis of a ChemicalSample |  no  |
| [AnalysisDataset](AnalysisDataset.md) |  |  no  |
| [ResearchDataset](ResearchDataset.md) | A collection of data, published or curated by a single agent, and available f... |  no  |
| [DatasetSeries](DatasetSeries.md) | See [DCAT-AP specs:DatasetSeries](https://semiceu |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterms:spatial |
| native | nfdi4c:geographical_coverage |




## LinkML Source

<details>
```yaml
name: geographical_coverage
description: This slot is described in more detail within the class in which it is
  used.
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
rank: 1000
slot_uri: dcterms:spatial
alias: geographical_coverage
domain_of:
- Catalogue
- Dataset
- DatasetSeries
range: string

```
</details>