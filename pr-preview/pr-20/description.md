

# Slot: description


_This slot is described in more detail within the class in which it is used._





URI: [dcterms:description](http://purl.org/dc/terms/description)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CatalogueRecord](CatalogueRecord.md) | See [DCAT-AP specs:CatalogueRecord](https://semiceu |  yes  |
| [AnalysisDataset](AnalysisDataset.md) |  |  no  |
| [Laboratory](Laboratory.md) | A facility that provides controlled conditions in which scientific or technol... |  no  |
| [Catalogue](Catalogue.md) | See [DCAT-AP specs:Catalogue](https://semiceu |  yes  |
| [Distribution](Distribution.md) | See [DCAT-AP specs:Distribution](https://semiceu |  yes  |
| [AnalysedData](AnalysedData.md) | Information that was evaluated within an Analysis |  no  |
| [NMRSpectroscopy](NMRSpectroscopy.md) | Spectroscopy where the energy states of spin-active nuclei placed in a static... |  no  |
| [ResearchDataset](ResearchDataset.md) | A collection of data, published or curated by a single agent, and available f... |  no  |
| [InChIKey](InChIKey.md) |  |  no  |
| [ChemicalSample](ChemicalSample.md) |  |  no  |
| [DataAnalysis](DataAnalysis.md) | A DataCreatingActivity that evaluates the data produced by another DataCreati... |  no  |
| [QualitativeAttribute](QualitativeAttribute.md) | A piece of information that is attributed to an entity of interest, tool or e... |  no  |
| [HardwareTool](HardwareTool.md) | A hardware device with a certain function that was used within a DataCreating... |  no  |
| [EvaluatedEntity](EvaluatedEntity.md) | Something (not an activity or process) that is being evaluated in a DataCreat... |  no  |
| [IUPACChemicalFormula](IUPACChemicalFormula.md) | A systematic name which is formulated according to the rules and recommendati... |  no  |
| [Environment](Environment.md) | The surrounding in which the dataset creating activity took place (e |  no  |
| [SMILES](SMILES.md) | A structure descriptor that denotes a molecular structure as a graph and conf... |  no  |
| [ResearchCatalog](ResearchCatalog.md) | A curated collection of metadata about data resources |  no  |
| [DatasetSeries](DatasetSeries.md) | See [DCAT-AP specs:DatasetSeries](https://semiceu |  yes  |
| [InChi](InChi.md) | A structure descriptor which conforms to the InChI format specification |  no  |
| [EvaluatedActivity](EvaluatedActivity.md) | An activity or process that is being evaluated in a DataCreatingActivity |  no  |
| [SoftwareTool](SoftwareTool.md) | A software device with a certain function that was used within a DataCreating... |  no  |
| [ChemicalSubstance](ChemicalSubstance.md) | A portion of matter of constant composition, composed of molecular entities o... |  no  |
| [Tool](Tool.md) | A entity with a certain function used within a DataCreatingActivity |  no  |
| [Dataset](Dataset.md) | See [DCAT-AP specs:Dataset](https://semiceu |  yes  |
| [NMRSpectralAnalysis](NMRSpectralAnalysis.md) | A DataAnalysis which assigns a chemical structure to the peaks of a NMRSpectr... |  no  |
| [NMRAnalysisDataset](NMRAnalysisDataset.md) | A dataset that is the result of a NMRSpectralAnalysis of a ChemicalSample |  no  |
| [NMRSpectrum](NMRSpectrum.md) | A set of chemical shifts obtained via NMR spectroscopy |  no  |
| [ChemicalReaction](ChemicalReaction.md) | An experimental procedure with the aim of producing a portion of a given comp... |  no  |
| [DataService](DataService.md) | See [DCAT-AP specs:DataService](https://semiceu |  yes  |
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
| self | dcterms:description |
| native | nfdi4c:description |




## LinkML Source

<details>
```yaml
name: description
description: This slot is described in more detail within the class in which it is
  used.
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
rank: 1000
slot_uri: dcterms:description
alias: description
domain_of:
- Catalogue
- CatalogueRecord
- DataService
- Dataset
- DatasetSeries
- Distribution
- DataCreatingActivity
- EvaluatedEntity
- EvaluatedActivity
- Tool
- Environment
- Plan
- QualitativeAttribute
- QuantitativeAttribute
range: string

```
</details>