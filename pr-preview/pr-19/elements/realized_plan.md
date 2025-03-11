

# Slot: realized_plan


_The slot to specify the Method (aka Procedure) that was realized by a DataCreatingActivity._





URI: [prov:used](http://www.w3.org/ns/prov#used)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NMRSpectralAnalysis](NMRSpectralAnalysis.md) | A DataAnalysis which assigns a chemical structure to the peaks of a NMRSpectr... |  no  |
| [DataCreatingActivity](DataCreatingActivity.md) | An activity (process) that has the objective to produce information about an ... |  no  |
| [DataAnalysis](DataAnalysis.md) | A DataCreatingActivity that evaluates the data produced by another DataCreati... |  no  |
| [NMRSpectroscopy](NMRSpectroscopy.md) | Spectroscopy where the energy states of spin-active nuclei placed in a static... |  no  |







## Properties

* Range: [Plan](Plan.md)

* Recommended: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | prov:used |
| native | nfdi4c:realized_plan |




## LinkML Source

<details>
```yaml
name: realized_plan
description: The slot to specify the Method (aka Procedure) that was realized by a
  DataCreatingActivity.
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
rank: 1000
slot_uri: prov:used
alias: realized_plan
domain_of:
- DataCreatingActivity
range: Plan
recommended: true

```
</details>