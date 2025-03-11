

# Slot: was_generated_by


_This slot is described in more detail within the class in which it is used._





URI: [prov:wasGeneratedBy](http://www.w3.org/ns/prov#wasGeneratedBy)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NMRSpectrum](NMRSpectrum.md) | A set of chemical shifts obtained via NMR spectroscopy |  yes  |
| [NMRAnalysisDataset](NMRAnalysisDataset.md) | A dataset that is the result of a NMRSpectralAnalysis of a ChemicalSample |  yes  |
| [AnalysisDataset](AnalysisDataset.md) |  |  yes  |
| [ResearchDataset](ResearchDataset.md) | A collection of data, published or curated by a single agent, and available f... |  yes  |
| [ChemicalSample](ChemicalSample.md) |  |  no  |
| [Dataset](Dataset.md) | See [DCAT-AP specs:Dataset](https://semiceu |  yes  |
| [EvaluatedEntity](EvaluatedEntity.md) | Something (not an activity or process) that is being evaluated in a DataCreat... |  yes  |
| [AnalysedData](AnalysedData.md) | Information that was evaluated within an Analysis |  yes  |
| [ChemicalSubstance](ChemicalSubstance.md) | A portion of matter of constant composition, composed of molecular entities o... |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | prov:wasGeneratedBy |
| native | nfdi4c:was_generated_by |




## LinkML Source

<details>
```yaml
name: was_generated_by
description: This slot is described in more detail within the class in which it is
  used.
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
rank: 1000
slot_uri: prov:wasGeneratedBy
alias: was_generated_by
domain_of:
- Dataset
- EvaluatedEntity
range: string

```
</details>