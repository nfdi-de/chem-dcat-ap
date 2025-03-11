

# Slot: id



URI: [dcterms:identifier](http://purl.org/dc/terms/identifier)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ChemicalSubstance](ChemicalSubstance.md) | A portion of matter of constant composition, composed of molecular entities o... |  no  |
| [AnalysedData](AnalysedData.md) | Information that was evaluated within an Analysis |  no  |
| [NMRSpectrum](NMRSpectrum.md) | A set of chemical shifts obtained via NMR spectroscopy |  no  |
| [ChemicalSample](ChemicalSample.md) |  |  no  |
| [ChemicalReaction](ChemicalReaction.md) | An experimental procedure with the aim of producing a portion of a given comp... |  no  |
| [EvaluatedActivity](EvaluatedActivity.md) | An activity or process that is being evaluated in a DataCreatingActivity |  no  |
| [EvaluatedEntity](EvaluatedEntity.md) | Something (not an activity or process) that is being evaluated in a DataCreat... |  no  |
| [ResearchCatalog](ResearchCatalog.md) | A curated collection of metadata about data resources |  no  |
| [NMRAnalysisDataset](NMRAnalysisDataset.md) | A dataset that is the result of a NMRSpectralAnalysis of a ChemicalSample |  no  |
| [AnalysisDataset](AnalysisDataset.md) |  |  no  |
| [ResearchDataset](ResearchDataset.md) | A collection of data, published or curated by a single agent, and available f... |  no  |
| [DefinedTerm](DefinedTerm.md) | A word, name, acronym, phrase that is defined in a controlled vocabulary (CV)... |  no  |







## Properties

* Range: [Uriorcurie](Uriorcurie.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterms:identifier |
| native | nfdi4c:id |




## LinkML Source

<details>
```yaml
name: id
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
rank: 1000
slot_uri: dcterms:identifier
identifier: true
alias: id
domain_of:
- DefinedTerm
- ResearchDataset
- ResearchCatalog
- EvaluatedEntity
- EvaluatedActivity
range: uriorcurie
required: true

```
</details>