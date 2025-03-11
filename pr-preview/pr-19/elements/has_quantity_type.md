

# Slot: has_quantity_type


_The type of quality that is quantifiable according to the QUDT ontology._





URI: [qudt:hasQuantityKind](http://qudt.org/schema/qudt/hasQuantityKind)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QuantitativeAttribute](QuantitativeAttribute.md) | A quantifiable piece of information that is attributed to an entity of intere... |  no  |







## Properties

* Range: [DefinedTerm](DefinedTerm.md)

* Required: True





## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | qudt:hasQuantityKind |
| native | nfdi4c:has_quantity_type |




## LinkML Source

<details>
```yaml
name: has_quantity_type
description: The type of quality that is quantifiable according to the QUDT ontology.
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
rank: 1000
slot_uri: qudt:hasQuantityKind
alias: has_quantity_type
owner: QuantitativeAttribute
domain_of:
- QuantitativeAttribute
range: DefinedTerm
bindings:
- range: QUDTQuantityKindEnum
  obligation_level: RECOMMENDED
  binds_value_of: id
  description: Binds the type of a quantifiable attribute to a QUDT Quantity Kind
    instance from the QUDT Quantity Kind vocabulary.
required: true

```
</details>