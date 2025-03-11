

# Slot: has_part


_This slot is described in more detail within the class in which it is used._





URI: [dcterms:hasPart](http://purl.org/dc/terms/hasPart)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AnalysedData](AnalysedData.md) | Information that was evaluated within an Analysis |  no  |
| [HardwareTool](HardwareTool.md) | A hardware device with a certain function that was used within a DataCreating... |  no  |
| [NMRSpectrum](NMRSpectrum.md) | A set of chemical shifts obtained via NMR spectroscopy |  no  |
| [Catalogue](Catalogue.md) | See [DCAT-AP specs:Catalogue](https://semiceu |  yes  |
| [ChemicalSample](ChemicalSample.md) |  |  no  |
| [ChemicalReaction](ChemicalReaction.md) | An experimental procedure with the aim of producing a portion of a given comp... |  no  |
| [EvaluatedActivity](EvaluatedActivity.md) | An activity or process that is being evaluated in a DataCreatingActivity |  no  |
| [NMRSpectroscopy](NMRSpectroscopy.md) | Spectroscopy where the energy states of spin-active nuclei placed in a static... |  no  |
| [DataCreatingActivity](DataCreatingActivity.md) | An activity (process) that has the objective to produce information about an ... |  yes  |
| [EvaluatedEntity](EvaluatedEntity.md) | Something (not an activity or process) that is being evaluated in a DataCreat... |  no  |
| [DataAnalysis](DataAnalysis.md) | A DataCreatingActivity that evaluates the data produced by another DataCreati... |  no  |
| [SoftwareTool](SoftwareTool.md) | A software device with a certain function that was used within a DataCreating... |  no  |
| [NMRSpectralAnalysis](NMRSpectralAnalysis.md) | A DataAnalysis which assigns a chemical structure to the peaks of a NMRSpectr... |  no  |
| [ResearchCatalog](ResearchCatalog.md) | A curated collection of metadata about data resources |  no  |
| [Tool](Tool.md) | A entity with a certain function used within a DataCreatingActivity |  yes  |
| [ChemicalSubstance](ChemicalSubstance.md) | A portion of matter of constant composition, composed of molecular entities o... |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterms:hasPart |
| native | nfdi4c:has_part |




## LinkML Source

<details>
```yaml
name: has_part
description: This slot is described in more detail within the class in which it is
  used.
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
rank: 1000
slot_uri: dcterms:hasPart
alias: has_part
domain_of:
- Catalogue
- DataCreatingActivity
- EvaluatedEntity
- EvaluatedActivity
- Tool
range: string

```
</details>