

# Slot: evaluated_entity


_The slot to specify the entity of interest that was evaluated._





URI: [prov:used](http://www.w3.org/ns/prov#used)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NMRSpectroscopy](NMRSpectroscopy.md) | Spectroscopy where the energy states of spin-active nuclei placed in a static... |  yes  |
| [DataCreatingActivity](DataCreatingActivity.md) | An activity (process) that has the objective to produce information about an ... |  no  |
| [DataAnalysis](DataAnalysis.md) | A DataCreatingActivity that evaluates the data produced by another DataCreati... |  yes  |
| [NMRSpectralAnalysis](NMRSpectralAnalysis.md) | A DataAnalysis which assigns a chemical structure to the peaks of a NMRSpectr... |  yes  |







## Properties

* Range: [EvaluatedEntity](EvaluatedEntity.md)

* Multivalued: True

* Recommended: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | prov:used |
| native | nfdi4c:evaluated_entity |




## LinkML Source

<details>
```yaml
name: evaluated_entity
description: The slot to specify the entity of interest that was evaluated.
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
rank: 1000
slot_uri: prov:used
alias: evaluated_entity
domain_of:
- DataCreatingActivity
range: EvaluatedEntity
recommended: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details>