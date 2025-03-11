

# Slot: occurred_in


_The slot to specify the Method (aka Procedure) that was used in the DataCreatingActivity._





URI: [BFO:0000066](http://purl.obolibrary.org/obo/BFO_0000066)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [NMRSpectroscopy](NMRSpectroscopy.md) | Spectroscopy where the energy states of spin-active nuclei placed in a static... |  no  |
| [DataCreatingActivity](DataCreatingActivity.md) | An activity (process) that has the objective to produce information about an ... |  no  |
| [DataAnalysis](DataAnalysis.md) | A DataCreatingActivity that evaluates the data produced by another DataCreati... |  no  |
| [NMRSpectralAnalysis](NMRSpectralAnalysis.md) | A DataAnalysis which assigns a chemical structure to the peaks of a NMRSpectr... |  no  |







## Properties

* Range: [Environment](Environment.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | BFO:0000066 |
| native | nfdi4c:occurred_in |




## LinkML Source

<details>
```yaml
name: occurred_in
description: The slot to specify the Method (aka Procedure) that was used in the DataCreatingActivity.
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
rank: 1000
slot_uri: BFO:0000066
alias: occurred_in
domain_of:
- DataCreatingActivity
range: Environment

```
</details>