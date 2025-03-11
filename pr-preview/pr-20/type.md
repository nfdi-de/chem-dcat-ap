

# Slot: type


_This slot is described in more detail within the class in which it is used._





URI: [dcterms:type](http://purl.org/dc/terms/type)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AnalysisDataset](AnalysisDataset.md) |  |  no  |
| [Laboratory](Laboratory.md) | A facility that provides controlled conditions in which scientific or technol... |  no  |
| [AnalysedData](AnalysedData.md) | Information that was evaluated within an Analysis |  no  |
| [NMRSpectroscopy](NMRSpectroscopy.md) | Spectroscopy where the energy states of spin-active nuclei placed in a static... |  no  |
| [ResearchDataset](ResearchDataset.md) | A collection of data, published or curated by a single agent, and available f... |  no  |
| [InChIKey](InChIKey.md) |  |  no  |
| [ChemicalSample](ChemicalSample.md) |  |  no  |
| [DataAnalysis](DataAnalysis.md) | A DataCreatingActivity that evaluates the data produced by another DataCreati... |  no  |
| [QualitativeAttribute](QualitativeAttribute.md) | A piece of information that is attributed to an entity of interest, tool or e... |  no  |
| [HardwareTool](HardwareTool.md) | A hardware device with a certain function that was used within a DataCreating... |  no  |
| [LicenseDocument](LicenseDocument.md) | See [DCAT-AP specs:LicenseDocument](https://semiceu |  yes  |
| [EvaluatedEntity](EvaluatedEntity.md) | Something (not an activity or process) that is being evaluated in a DataCreat... |  no  |
| [IUPACChemicalFormula](IUPACChemicalFormula.md) | A systematic name which is formulated according to the rules and recommendati... |  no  |
| [SMILES](SMILES.md) | A structure descriptor that denotes a molecular structure as a graph and conf... |  no  |
| [Environment](Environment.md) | The surrounding in which the dataset creating activity took place (e |  no  |
| [InChi](InChi.md) | A structure descriptor which conforms to the InChI format specification |  no  |
| [EvaluatedActivity](EvaluatedActivity.md) | An activity or process that is being evaluated in a DataCreatingActivity |  no  |
| [SoftwareTool](SoftwareTool.md) | A software device with a certain function that was used within a DataCreating... |  no  |
| [Agent](Agent.md) | See [DCAT-AP specs:Agent](https://semiceu |  yes  |
| [ChemicalSubstance](ChemicalSubstance.md) | A portion of matter of constant composition, composed of molecular entities o... |  no  |
| [Tool](Tool.md) | A entity with a certain function used within a DataCreatingActivity |  no  |
| [Dataset](Dataset.md) | See [DCAT-AP specs:Dataset](https://semiceu |  yes  |
| [NMRSpectralAnalysis](NMRSpectralAnalysis.md) | A DataAnalysis which assigns a chemical structure to the peaks of a NMRSpectr... |  no  |
| [NMRAnalysisDataset](NMRAnalysisDataset.md) | A dataset that is the result of a NMRSpectralAnalysis of a ChemicalSample |  no  |
| [NMRSpectrum](NMRSpectrum.md) | A set of chemical shifts obtained via NMR spectroscopy |  no  |
| [ClassifierMixin](ClassifierMixin.md) | A mixin with which an entity of this schema can be classified via an addition... |  yes  |
| [ChemicalReaction](ChemicalReaction.md) | An experimental procedure with the aim of producing a portion of a given comp... |  no  |
| [QuantitativeAttribute](QuantitativeAttribute.md) | A quantifiable piece of information that is attributed to an entity of intere... |  no  |
| [DataCreatingActivity](DataCreatingActivity.md) | An activity (process) that has the objective to produce information about an ... |  no  |
| [Plan](Plan.md) | A piece of information that specifies: a) how an activity has to be carried o... |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterms:type |
| native | nfdi4c:type |




## LinkML Source

<details>
```yaml
name: type
description: This slot is described in more detail within the class in which it is
  used.
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
rank: 1000
slot_uri: dcterms:type
alias: type
domain_of:
- Agent
- Dataset
- LicenseDocument
- ClassifierMixin
range: string

```
</details>