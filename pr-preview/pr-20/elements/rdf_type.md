

# Slot: rdf_type


_The slot to specify the ontology class that is instantiated by an entity._





URI: [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QualitativeAttribute](QualitativeAttribute.md) | A piece of information that is attributed to an entity of interest, tool or e... |  no  |
| [ChemicalSample](ChemicalSample.md) |  |  no  |
| [EvaluatedEntity](EvaluatedEntity.md) | Something (not an activity or process) that is being evaluated in a DataCreat... |  no  |
| [SoftwareTool](SoftwareTool.md) | A software device with a certain function that was used within a DataCreating... |  no  |
| [DataAnalysis](DataAnalysis.md) | A DataCreatingActivity that evaluates the data produced by another DataCreati... |  no  |
| [EvaluatedActivity](EvaluatedActivity.md) | An activity or process that is being evaluated in a DataCreatingActivity |  no  |
| [NMRSpectralAnalysis](NMRSpectralAnalysis.md) | A DataAnalysis which assigns a chemical structure to the peaks of a NMRSpectr... |  no  |
| [Environment](Environment.md) | The surrounding in which the dataset creating activity took place (e |  no  |
| [InChIKey](InChIKey.md) |  |  no  |
| [NMRSpectrum](NMRSpectrum.md) | A set of chemical shifts obtained via NMR spectroscopy |  no  |
| [HardwareTool](HardwareTool.md) | A hardware device with a certain function that was used within a DataCreating... |  no  |
| [NMRSpectroscopy](NMRSpectroscopy.md) | Spectroscopy where the energy states of spin-active nuclei placed in a static... |  yes  |
| [DataCreatingActivity](DataCreatingActivity.md) | An activity (process) that has the objective to produce information about an ... |  no  |
| [Plan](Plan.md) | A piece of information that specifies: a) how an activity has to be carried o... |  no  |
| [ClassifierMixin](ClassifierMixin.md) | A mixin with which an entity of this schema can be classified via an addition... |  no  |
| [IUPACChemicalFormula](IUPACChemicalFormula.md) | A systematic name which is formulated according to the rules and recommendati... |  no  |
| [InChi](InChi.md) | A structure descriptor which conforms to the InChI format specification |  no  |
| [Laboratory](Laboratory.md) | A facility that provides controlled conditions in which scientific or technol... |  no  |
| [SMILES](SMILES.md) | A structure descriptor that denotes a molecular structure as a graph and conf... |  no  |
| [AnalysedData](AnalysedData.md) | Information that was evaluated within an Analysis |  no  |
| [Tool](Tool.md) | A entity with a certain function used within a DataCreatingActivity |  no  |
| [ChemicalSubstance](ChemicalSubstance.md) | A portion of matter of constant composition, composed of molecular entities o... |  no  |
| [QuantitativeAttribute](QuantitativeAttribute.md) | A quantifiable piece of information that is attributed to an entity of intere... |  no  |
| [ChemicalReaction](ChemicalReaction.md) | An experimental procedure with the aim of producing a portion of a given comp... |  no  |







## Properties

* Range: [DefinedTerm](DefinedTerm.md)

* Recommended: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rdf:type |
| native | nfdi4c:rdf_type |




## LinkML Source

<details>
```yaml
name: rdf_type
description: The slot to specify the ontology class that is instantiated by an entity.
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
rank: 1000
slot_uri: rdf:type
alias: rdf_type
domain_of:
- ClassifierMixin
range: DefinedTerm
recommended: true
inlined: true

```
</details>