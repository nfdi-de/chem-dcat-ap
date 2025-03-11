

# Slot: evaluated_activity


_The slot to specify the activity of interest that was evaluated._





URI: [prov:wasInformedBy](http://www.w3.org/ns/prov#wasInformedBy)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NMRSpectralAnalysis](NMRSpectralAnalysis.md) | A DataAnalysis which assigns a chemical structure to the peaks of a NMRSpectr... |  no  |
| [DataCreatingActivity](DataCreatingActivity.md) | An activity (process) that has the objective to produce information about an ... |  no  |
| [DataAnalysis](DataAnalysis.md) | A DataCreatingActivity that evaluates the data produced by another DataCreati... |  no  |
| [NMRSpectroscopy](NMRSpectroscopy.md) | Spectroscopy where the energy states of spin-active nuclei placed in a static... |  no  |







## Properties

* Range: [EvaluatedActivity](EvaluatedActivity.md)

* Multivalued: True

* Recommended: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | prov:wasInformedBy |
| native | nfdi4c:evaluated_activity |




## LinkML Source

<details>
```yaml
name: evaluated_activity
description: The slot to specify the activity of interest that was evaluated.
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
rank: 1000
slot_uri: prov:wasInformedBy
alias: evaluated_activity
domain_of:
- DataCreatingActivity
range: EvaluatedActivity
recommended: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details>