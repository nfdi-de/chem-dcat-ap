

# Slot: composed_of


_The slot to provide the chemical entities of which the chemical substance is composed of._





URI: [nfdi4c:composed_of](https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap/composed_of)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ChemicalSubstance](ChemicalSubstance.md) | A portion of matter of constant composition, composed of molecular entities o... |  no  |
| [ChemicalSample](ChemicalSample.md) |  |  no  |







## Properties

* Range: [ChemicalEntity](ChemicalEntity.md)

* Multivalued: True

* Recommended: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | nfdi4c:composed_of |
| native | nfdi4c:composed_of |
| exact | BFO:0000051 |




## LinkML Source

<details>
```yaml
name: composed_of
description: The slot to provide the chemical entities of which the chemical substance
  is composed of.
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
exact_mappings:
- BFO:0000051
rank: 1000
alias: composed_of
owner: ChemicalSubstance
domain_of:
- ChemicalSubstance
range: ChemicalEntity
recommended: true
multivalued: true
inlined: true
inlined_as_list: true

```
</details>