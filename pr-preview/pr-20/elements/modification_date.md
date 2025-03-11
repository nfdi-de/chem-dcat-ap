

# Slot: modification_date


_This slot is described in more detail within the class in which it is used._





URI: [dcterms:modified](http://purl.org/dc/terms/modified)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Catalogue](Catalogue.md) | See [DCAT-AP specs:Catalogue](https://semiceu |  yes  |
| [AnalysisDataset](AnalysisDataset.md) |  |  no  |
| [NMRAnalysisDataset](NMRAnalysisDataset.md) | A dataset that is the result of a NMRSpectralAnalysis of a ChemicalSample |  no  |
| [DatasetSeries](DatasetSeries.md) | See [DCAT-AP specs:DatasetSeries](https://semiceu |  yes  |
| [Distribution](Distribution.md) | See [DCAT-AP specs:Distribution](https://semiceu |  yes  |
| [ResearchDataset](ResearchDataset.md) | A collection of data, published or curated by a single agent, and available f... |  no  |
| [Dataset](Dataset.md) | See [DCAT-AP specs:Dataset](https://semiceu |  yes  |
| [ResearchCatalog](ResearchCatalog.md) | A curated collection of metadata about data resources |  no  |
| [CatalogueRecord](CatalogueRecord.md) | See [DCAT-AP specs:CatalogueRecord](https://semiceu |  yes  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterms:modified |
| native | nfdi4c:modification_date |




## LinkML Source

<details>
```yaml
name: modification_date
description: This slot is described in more detail within the class in which it is
  used.
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
rank: 1000
slot_uri: dcterms:modified
alias: modification_date
domain_of:
- Catalogue
- CatalogueRecord
- Dataset
- DatasetSeries
- Distribution
range: string

```
</details>