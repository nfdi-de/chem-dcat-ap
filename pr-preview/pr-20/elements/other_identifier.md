

# Slot: other_identifier


_This slot is described in more detail within the class in which it is used._





URI: [adms:identifier](http://www.w3.org/ns/adms#identifier)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EvaluatedEntity](EvaluatedEntity.md) | Something (not an activity or process) that is being evaluated in a DataCreat... |  yes  |
| [DataAnalysis](DataAnalysis.md) | A DataCreatingActivity that evaluates the data produced by another DataCreati... |  no  |
| [HardwareTool](HardwareTool.md) | A hardware device with a certain function that was used within a DataCreating... |  no  |
| [DataCreatingActivity](DataCreatingActivity.md) | An activity (process) that has the objective to produce information about an ... |  yes  |
| [NMRSpectralAnalysis](NMRSpectralAnalysis.md) | A DataAnalysis which assigns a chemical structure to the peaks of a NMRSpectr... |  no  |
| [AnalysisDataset](AnalysisDataset.md) |  |  no  |
| [AnalysedData](AnalysedData.md) | Information that was evaluated within an Analysis |  no  |
| [Tool](Tool.md) | A entity with a certain function used within a DataCreatingActivity |  yes  |
| [Laboratory](Laboratory.md) | A facility that provides controlled conditions in which scientific or technol... |  no  |
| [ChemicalSample](ChemicalSample.md) |  |  no  |
| [Dataset](Dataset.md) | See [DCAT-AP specs:Dataset](https://semiceu |  yes  |
| [ChemicalReaction](ChemicalReaction.md) | An experimental procedure with the aim of producing a portion of a given comp... |  no  |
| [NMRSpectroscopy](NMRSpectroscopy.md) | Spectroscopy where the energy states of spin-active nuclei placed in a static... |  no  |
| [NMRSpectrum](NMRSpectrum.md) | A set of chemical shifts obtained via NMR spectroscopy |  no  |
| [ChemicalSubstance](ChemicalSubstance.md) | A portion of matter of constant composition, composed of molecular entities o... |  no  |
| [EvaluatedActivity](EvaluatedActivity.md) | An activity or process that is being evaluated in a DataCreatingActivity |  yes  |
| [Environment](Environment.md) | The surrounding in which the dataset creating activity took place (e |  yes  |
| [SoftwareTool](SoftwareTool.md) | A software device with a certain function that was used within a DataCreating... |  no  |
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
| self | adms:identifier |
| native | nfdi4c:other_identifier |




## LinkML Source

<details>
```yaml
name: other_identifier
description: This slot is described in more detail within the class in which it is
  used.
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
rank: 1000
slot_uri: adms:identifier
alias: other_identifier
domain_of:
- Dataset
- DataCreatingActivity
- EvaluatedEntity
- EvaluatedActivity
- Tool
- Environment
range: string

```
</details>