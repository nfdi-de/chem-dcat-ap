

# Class: QuantitativeAttribute


_A quantifiable piece of information that is attributed to an entity of interest, tool or environment._





URI: [qudt:Quantity](http://qudt.org/schema/qudt/Quantity)






```mermaid
 classDiagram
    class QuantitativeAttribute
    click QuantitativeAttribute href "../QuantitativeAttribute"
      ClassifierMixin <|-- QuantitativeAttribute
        click ClassifierMixin href "../ClassifierMixin"
      
      QuantitativeAttribute : description
        
      QuantitativeAttribute : has_quantity_type
        
          
    
    
    QuantitativeAttribute --> "1" DefinedTerm : has_quantity_type
    click DefinedTerm href "../DefinedTerm"

        
      QuantitativeAttribute : rdf_type
        
          
    
    
    QuantitativeAttribute --> "0..1 _recommended_" DefinedTerm : rdf_type
    click DefinedTerm href "../DefinedTerm"

        
      QuantitativeAttribute : title
        
      QuantitativeAttribute : type
        
          
    
    
    QuantitativeAttribute --> "0..1" DefinedTerm : type
    click DefinedTerm href "../DefinedTerm"

        
      QuantitativeAttribute : unit
        
          
    
    
    QuantitativeAttribute --> "0..1 _recommended_" DefinedTerm : unit
    click DefinedTerm href "../DefinedTerm"

        
      QuantitativeAttribute : value
        
      
```





## Inheritance
* **QuantitativeAttribute** [ [ClassifierMixin](ClassifierMixin.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [title](title.md) | 0..1 <br/> [String](String.md) | This slot is described in more detail within the class in which it is used | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) | This slot is described in more detail within the class in which it is used | direct |
| [value](value.md) | 1 <br/> [Float](Float.md) | The slot to provide the literal value of the QuantitativeAttribute | direct |
| [has_quantity_type](has_quantity_type.md) | 1 <br/> [DefinedTerm](DefinedTerm.md) | The type of quality that is quantifiable according to the QUDT ontology | direct |
| [unit](unit.md) | 0..1 _recommended_ <br/> [DefinedTerm](DefinedTerm.md) |  | direct |
| [type](type.md) | 0..1 <br/> [DefinedTerm](DefinedTerm.md) | This slot is described in more detail within the class in which it is used | [ClassifierMixin](ClassifierMixin.md) |
| [rdf_type](rdf_type.md) | 0..1 _recommended_ <br/> [DefinedTerm](DefinedTerm.md) | The slot to specify the ontology class that is instantiated by an entity | [ClassifierMixin](ClassifierMixin.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ChemicalReaction](ChemicalReaction.md) | [has_quantitative_attribute](has_quantitative_attribute.md) | range | [QuantitativeAttribute](QuantitativeAttribute.md) |
| [ChemicalSubstance](ChemicalSubstance.md) | [has_quantitative_attribute](has_quantitative_attribute.md) | range | [QuantitativeAttribute](QuantitativeAttribute.md) |
| [ChemicalSample](ChemicalSample.md) | [has_quantitative_attribute](has_quantitative_attribute.md) | range | [QuantitativeAttribute](QuantitativeAttribute.md) |
| [NMRSpectrum](NMRSpectrum.md) | [has_quantitative_attribute](has_quantitative_attribute.md) | range | [QuantitativeAttribute](QuantitativeAttribute.md) |
| [EvaluatedEntity](EvaluatedEntity.md) | [has_quantitative_attribute](has_quantitative_attribute.md) | range | [QuantitativeAttribute](QuantitativeAttribute.md) |
| [AnalysedData](AnalysedData.md) | [has_quantitative_attribute](has_quantitative_attribute.md) | range | [QuantitativeAttribute](QuantitativeAttribute.md) |
| [EvaluatedActivity](EvaluatedActivity.md) | [has_quantitative_attribute](has_quantitative_attribute.md) | range | [QuantitativeAttribute](QuantitativeAttribute.md) |
| [Tool](Tool.md) | [has_quantitative_attribute](has_quantitative_attribute.md) | range | [QuantitativeAttribute](QuantitativeAttribute.md) |
| [HardwareTool](HardwareTool.md) | [has_quantitative_attribute](has_quantitative_attribute.md) | range | [QuantitativeAttribute](QuantitativeAttribute.md) |
| [SoftwareTool](SoftwareTool.md) | [has_quantitative_attribute](has_quantitative_attribute.md) | range | [QuantitativeAttribute](QuantitativeAttribute.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | qudt:Quantity |
| native | nfdi4c:QuantitativeAttribute |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: QuantitativeAttribute
description: A quantifiable piece of information that is attributed to an entity of
  interest, tool or environment.
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
mixins:
- ClassifierMixin
slots:
- title
- description
- value
slot_usage:
  value:
    name: value
    description: The slot to provide the literal value of the QuantitativeAttribute.
    range: float
    required: true
attributes:
  has_quantity_type:
    name: has_quantity_type
    description: The type of quality that is quantifiable according to the QUDT ontology.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4nfdi_ap/
    rank: 1000
    slot_uri: qudt:hasQuantityKind
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
  unit:
    name: unit
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4nfdi_ap/
    rank: 1000
    slot_uri: qudt:unit
    domain_of:
    - QuantitativeAttribute
    range: DefinedTerm
    bindings:
    - range: QUDTUnitEnum
      obligation_level: RECOMMENDED
      binds_value_of: id
      description: Restricts the allowable defined terms to the QUDT Unit vocabulary.
    recommended: true
class_uri: qudt:Quantity

```
</details>

### Induced

<details>
```yaml
name: QuantitativeAttribute
description: A quantifiable piece of information that is attributed to an entity of
  interest, tool or environment.
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
mixins:
- ClassifierMixin
slot_usage:
  value:
    name: value
    description: The slot to provide the literal value of the QuantitativeAttribute.
    range: float
    required: true
attributes:
  has_quantity_type:
    name: has_quantity_type
    description: The type of quality that is quantifiable according to the QUDT ontology.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4nfdi_ap/
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
  unit:
    name: unit
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4nfdi_ap/
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
  title:
    name: title
    description: This slot is described in more detail within the class in which it
      is used.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:title
    alias: title
    owner: QuantitativeAttribute
    domain_of:
    - Catalogue
    - CatalogueRecord
    - ConceptScheme
    - DataService
    - Dataset
    - DatasetSeries
    - Distribution
    - DefinedTerm
    - DataCreatingActivity
    - EvaluatedEntity
    - EvaluatedActivity
    - Tool
    - Environment
    - Plan
    - QualitativeAttribute
    - QuantitativeAttribute
    range: string
  description:
    name: description
    description: This slot is described in more detail within the class in which it
      is used.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:description
    alias: description
    owner: QuantitativeAttribute
    domain_of:
    - Catalogue
    - CatalogueRecord
    - DataService
    - Dataset
    - DatasetSeries
    - Distribution
    - DataCreatingActivity
    - EvaluatedEntity
    - EvaluatedActivity
    - Tool
    - Environment
    - Plan
    - QualitativeAttribute
    - QuantitativeAttribute
    range: string
  value:
    name: value
    description: The slot to provide the literal value of the QuantitativeAttribute.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: prov:value
    alias: value
    owner: QuantitativeAttribute
    domain_of:
    - QualitativeAttribute
    - QuantitativeAttribute
    range: float
    required: true
  type:
    name: type
    description: This slot is described in more detail within the class in which it
      is used.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:type
    alias: type
    owner: QuantitativeAttribute
    domain_of:
    - Agent
    - Dataset
    - LicenseDocument
    - ClassifierMixin
    range: DefinedTerm
    inlined: true
  rdf_type:
    name: rdf_type
    description: The slot to specify the ontology class that is instantiated by an
      entity.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: rdf:type
    alias: rdf_type
    owner: QuantitativeAttribute
    domain_of:
    - ClassifierMixin
    range: DefinedTerm
    recommended: true
    inlined: true
class_uri: qudt:Quantity

```
</details>