

# Slot: has_qualitative_attribute


_The slot to relate a qualitative attribute to an entity of interest, tool or environment._





URI: [dcterms:relation](http://purl.org/dc/terms/relation)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [AnalysedData](AnalysedData.md) | Information that was evaluated within an Analysis |  no  |
| [NMRSpectrum](NMRSpectrum.md) | A set of chemical shifts obtained via NMR spectroscopy |  no  |
| [ChemicalSample](ChemicalSample.md) |  |  no  |
| [EvaluatedActivity](EvaluatedActivity.md) | An activity or process that is being evaluated in a DataCreatingActivity |  no  |
| [ChemicalSubstance](ChemicalSubstance.md) | A portion of matter of constant composition, composed of molecular entities o... |  no  |
| [EvaluatedEntity](EvaluatedEntity.md) | Something (not an activity or process) that is being evaluated in a DataCreat... |  no  |
| [Tool](Tool.md) | A entity with a certain function used within a DataCreatingActivity |  no  |
| [SoftwareTool](SoftwareTool.md) | A software device with a certain function that was used within a DataCreating... |  no  |
| [ChemicalReaction](ChemicalReaction.md) | An experimental procedure with the aim of producing a portion of a given comp... |  no  |
| [HardwareTool](HardwareTool.md) | A hardware device with a certain function that was used within a DataCreating... |  no  |







## Properties

* Range: [QualitativeAttribute](QualitativeAttribute.md)

* Multivalued: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterms:relation |
| native | nfdi4c:has_qualitative_attribute |




## LinkML Source

<details>
```yaml
name: has_qualitative_attribute
description: The slot to relate a qualitative attribute to an entity of interest,
  tool or environment.
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
rank: 1000
slot_uri: dcterms:relation
alias: has_qualitative_attribute
domain_of:
- EvaluatedEntity
- EvaluatedActivity
- Tool
range: QualitativeAttribute
multivalued: true
inlined: true
inlined_as_list: true

```
</details>