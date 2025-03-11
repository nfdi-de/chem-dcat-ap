

# Class: QualitativeAttribute


_A piece of information that is attributed to an entity of interest, tool or environment._





URI: [prov:Entity](http://www.w3.org/ns/prov#Entity)






```mermaid
 classDiagram
    class QualitativeAttribute
    click QualitativeAttribute href "../QualitativeAttribute"
      ClassifierMixin <|-- QualitativeAttribute
        click ClassifierMixin href "../ClassifierMixin"
      

      QualitativeAttribute <|-- InChIKey
        click InChIKey href "../InChIKey"
      QualitativeAttribute <|-- InChi
        click InChi href "../InChi"
      QualitativeAttribute <|-- IUPACChemicalFormula
        click IUPACChemicalFormula href "../IUPACChemicalFormula"
      QualitativeAttribute <|-- SMILES
        click SMILES href "../SMILES"
      
      
      QualitativeAttribute : description
        
      QualitativeAttribute : rdf_type
        
          
    
    
    QualitativeAttribute --> "0..1 _recommended_" DefinedTerm : rdf_type
    click DefinedTerm href "../DefinedTerm"

        
      QualitativeAttribute : title
        
      QualitativeAttribute : type
        
          
    
    
    QualitativeAttribute --> "0..1" DefinedTerm : type
    click DefinedTerm href "../DefinedTerm"

        
      QualitativeAttribute : value
        
      
```





## Inheritance
* **QualitativeAttribute** [ [ClassifierMixin](ClassifierMixin.md)]
    * [InChIKey](InChIKey.md)
    * [InChi](InChi.md)
    * [IUPACChemicalFormula](IUPACChemicalFormula.md)
    * [SMILES](SMILES.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [title](title.md) | 0..1 <br/> [String](String.md) | This slot is described in more detail within the class in which it is used | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) | This slot is described in more detail within the class in which it is used | direct |
| [value](value.md) | 1 <br/> [String](String.md) | The slot to provide the literal value of the QualitativeAttribute | direct |
| [type](type.md) | 0..1 <br/> [DefinedTerm](DefinedTerm.md) | This slot is described in more detail within the class in which it is used | [ClassifierMixin](ClassifierMixin.md) |
| [rdf_type](rdf_type.md) | 0..1 _recommended_ <br/> [DefinedTerm](DefinedTerm.md) | The slot to specify the ontology class that is instantiated by an entity | [ClassifierMixin](ClassifierMixin.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ChemicalReaction](ChemicalReaction.md) | [has_qualitative_attribute](has_qualitative_attribute.md) | range | [QualitativeAttribute](QualitativeAttribute.md) |
| [ChemicalSubstance](ChemicalSubstance.md) | [has_qualitative_attribute](has_qualitative_attribute.md) | range | [QualitativeAttribute](QualitativeAttribute.md) |
| [ChemicalSample](ChemicalSample.md) | [has_qualitative_attribute](has_qualitative_attribute.md) | range | [QualitativeAttribute](QualitativeAttribute.md) |
| [NMRSpectrum](NMRSpectrum.md) | [has_qualitative_attribute](has_qualitative_attribute.md) | range | [QualitativeAttribute](QualitativeAttribute.md) |
| [EvaluatedEntity](EvaluatedEntity.md) | [has_qualitative_attribute](has_qualitative_attribute.md) | range | [QualitativeAttribute](QualitativeAttribute.md) |
| [AnalysedData](AnalysedData.md) | [has_qualitative_attribute](has_qualitative_attribute.md) | range | [QualitativeAttribute](QualitativeAttribute.md) |
| [EvaluatedActivity](EvaluatedActivity.md) | [has_qualitative_attribute](has_qualitative_attribute.md) | range | [QualitativeAttribute](QualitativeAttribute.md) |
| [Tool](Tool.md) | [has_qualitative_attribute](has_qualitative_attribute.md) | range | [QualitativeAttribute](QualitativeAttribute.md) |
| [HardwareTool](HardwareTool.md) | [has_qualitative_attribute](has_qualitative_attribute.md) | range | [QualitativeAttribute](QualitativeAttribute.md) |
| [SoftwareTool](SoftwareTool.md) | [has_qualitative_attribute](has_qualitative_attribute.md) | range | [QualitativeAttribute](QualitativeAttribute.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | prov:Entity |
| native | nfdi4c:QualitativeAttribute |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: QualitativeAttribute
description: A piece of information that is attributed to an entity of interest, tool
  or environment.
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
    description: The slot to provide the literal value of the QualitativeAttribute.
    required: true
class_uri: prov:Entity

```
</details>

### Induced

<details>
```yaml
name: QualitativeAttribute
description: A piece of information that is attributed to an entity of interest, tool
  or environment.
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
mixins:
- ClassifierMixin
slot_usage:
  value:
    name: value
    description: The slot to provide the literal value of the QualitativeAttribute.
    required: true
attributes:
  title:
    name: title
    description: This slot is described in more detail within the class in which it
      is used.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:title
    alias: title
    owner: QualitativeAttribute
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
    owner: QualitativeAttribute
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
    description: The slot to provide the literal value of the QualitativeAttribute.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: prov:value
    alias: value
    owner: QualitativeAttribute
    domain_of:
    - QualitativeAttribute
    - QuantitativeAttribute
    range: string
    required: true
  type:
    name: type
    description: This slot is described in more detail within the class in which it
      is used.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:type
    alias: type
    owner: QualitativeAttribute
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
    owner: QualitativeAttribute
    domain_of:
    - ClassifierMixin
    range: DefinedTerm
    recommended: true
    inlined: true
class_uri: prov:Entity

```
</details>