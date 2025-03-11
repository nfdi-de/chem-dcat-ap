

# Slot: unit



URI: [qudt:unit](http://qudt.org/schema/qudt/unit)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QuantitativeAttribute](QuantitativeAttribute.md) | A quantifiable piece of information that is attributed to an entity of intere... |  no  |







## Properties

* Range: [DefinedTerm](DefinedTerm.md)

* Recommended: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | qudt:unit |
| native | nfdi4c:unit |




## LinkML Source

<details>
```yaml
name: unit
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
rank: 1000
slot_uri: qudt:unit
alias: unit
owner: QuantitativeAttribute
domain_of:
- QuantitativeAttribute
range: DefinedTerm
bindings:
- range: QUDTUnitEnum
  obligation_level: RECOMMENDED
  binds_value_of: id
  description: Restricts the allowable defined terms to the QUDT Unit vocabulary.
recommended: true

```
</details>