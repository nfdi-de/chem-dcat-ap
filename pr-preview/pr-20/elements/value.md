

# Slot: value


_A slot to provide the literal value of an attribute._





URI: [prov:value](http://www.w3.org/ns/prov#value)



<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QualitativeAttribute](QualitativeAttribute.md) | A piece of information that is attributed to an entity of interest, tool or e... |  yes  |
| [SMILES](SMILES.md) | A structure descriptor that denotes a molecular structure as a graph and conf... |  no  |
| [IUPACChemicalFormula](IUPACChemicalFormula.md) | A systematic name which is formulated according to the rules and recommendati... |  no  |
| [InChIKey](InChIKey.md) |  |  no  |
| [QuantitativeAttribute](QuantitativeAttribute.md) | A quantifiable piece of information that is attributed to an entity of intere... |  yes  |
| [InChi](InChi.md) | A structure descriptor which conforms to the InChI format specification |  no  |







## Properties

* Range: [String](String.md)





## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | prov:value |
| native | nfdi4c:value |




## LinkML Source

<details>
```yaml
name: value
description: A slot to provide the literal value of an attribute.
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
rank: 1000
slot_uri: prov:value
alias: value
domain_of:
- QualitativeAttribute
- QuantitativeAttribute
range: string

```
</details>