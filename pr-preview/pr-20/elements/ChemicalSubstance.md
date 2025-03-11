

# Class: ChemicalSubstance


_A portion of matter of constant composition, composed of molecular entities of the same type or of different types that is being evaluated in a scientific process._





URI: [prov:Entity](http://www.w3.org/ns/prov#Entity)






```mermaid
 classDiagram
    class ChemicalSubstance
    click ChemicalSubstance href "../ChemicalSubstance"
      EvaluatedEntity <|-- ChemicalSubstance
        click EvaluatedEntity href "../EvaluatedEntity"
      

      ChemicalSubstance <|-- ChemicalSample
        click ChemicalSample href "../ChemicalSample"
      
      
      ChemicalSubstance : composed_of
        
          
    
    
    ChemicalSubstance --> "* _recommended_" ChemicalEntity : composed_of
    click ChemicalEntity href "../ChemicalEntity"

        
      ChemicalSubstance : description
        
      ChemicalSubstance : has_part
        
      ChemicalSubstance : has_qualitative_attribute
        
          
    
    
    ChemicalSubstance --> "*" QualitativeAttribute : has_qualitative_attribute
    click QualitativeAttribute href "../QualitativeAttribute"

        
      ChemicalSubstance : has_quantitative_attribute
        
          
    
    
    ChemicalSubstance --> "*" QuantitativeAttribute : has_quantitative_attribute
    click QuantitativeAttribute href "../QuantitativeAttribute"

        
      ChemicalSubstance : has_role
        
      ChemicalSubstance : id
        
      ChemicalSubstance : other_identifier
        
          
    
    
    ChemicalSubstance --> "*" Identifier : other_identifier
    click Identifier href "../Identifier"

        
      ChemicalSubstance : rdf_type
        
          
    
    
    ChemicalSubstance --> "0..1 _recommended_" DefinedTerm : rdf_type
    click DefinedTerm href "../DefinedTerm"

        
      ChemicalSubstance : title
        
      ChemicalSubstance : type
        
          
    
    
    ChemicalSubstance --> "0..1" DefinedTerm : type
    click DefinedTerm href "../DefinedTerm"

        
      ChemicalSubstance : was_generated_by
        
          
    
    
    ChemicalSubstance --> "*" Activity : was_generated_by
    click Activity href "../Activity"

        
      
```





## Inheritance
* [EvaluatedEntity](EvaluatedEntity.md) [ [ClassifierMixin](ClassifierMixin.md)]
    * **ChemicalSubstance**
        * [ChemicalSample](ChemicalSample.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [has_role](has_role.md) | 0..1 <br/> [String](String.md) |  | direct |
| [composed_of](composed_of.md) | * _recommended_ <br/> [ChemicalEntity](ChemicalEntity.md) | The slot to provide the chemical entities of which the chemical substance is ... | direct |
| [title](title.md) | 0..1 <br/> [String](String.md) | This slot is described in more detail within the class in which it is used | [EvaluatedEntity](EvaluatedEntity.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | This slot is described in more detail within the class in which it is used | [EvaluatedEntity](EvaluatedEntity.md) |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) |  | [EvaluatedEntity](EvaluatedEntity.md) |
| [other_identifier](other_identifier.md) | * <br/> [Identifier](Identifier.md) | A secondary identifier of the EvaluatedEntity | [EvaluatedEntity](EvaluatedEntity.md) |
| [has_qualitative_attribute](has_qualitative_attribute.md) | * <br/> [QualitativeAttribute](QualitativeAttribute.md) | The slot to relate a qualitative attribute to an entity of interest, tool or ... | [EvaluatedEntity](EvaluatedEntity.md) |
| [has_quantitative_attribute](has_quantitative_attribute.md) | * <br/> [QuantitativeAttribute](QuantitativeAttribute.md) | The slot to relate a quantitative  attribute to an entity of interest, tool o... | [EvaluatedEntity](EvaluatedEntity.md) |
| [has_part](has_part.md) | 0..1 <br/> [String](String.md) | This slot is described in more detail within the class in which it is used | [EvaluatedEntity](EvaluatedEntity.md) |
| [was_generated_by](was_generated_by.md) | * <br/> [Activity](Activity.md) | A slot to provide the Activity which created the EvaluatedEntity | [EvaluatedEntity](EvaluatedEntity.md) |
| [type](type.md) | 0..1 <br/> [DefinedTerm](DefinedTerm.md) | This slot is described in more detail within the class in which it is used | [ClassifierMixin](ClassifierMixin.md) |
| [rdf_type](rdf_type.md) | 0..1 _recommended_ <br/> [DefinedTerm](DefinedTerm.md) | The slot to specify the ontology class that is instantiated by an entity | [ClassifierMixin](ClassifierMixin.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | prov:Entity |
| native | nfdi4c:ChemicalSubstance |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ChemicalSubstance
description: A portion of matter of constant composition, composed of molecular entities
  of the same type or of different types that is being evaluated in a scientific process.
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
is_a: EvaluatedEntity
slots:
- has_role
attributes:
  composed_of:
    name: composed_of
    description: The slot to provide the chemical entities of which the chemical substance
      is composed of.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    exact_mappings:
    - BFO:0000051
    rank: 1000
    domain_of:
    - ChemicalSubstance
    range: ChemicalEntity
    recommended: true
    multivalued: true
    inlined: true
    inlined_as_list: true
class_uri: prov:Entity

```
</details>

### Induced

<details>
```yaml
name: ChemicalSubstance
description: A portion of matter of constant composition, composed of molecular entities
  of the same type or of different types that is being evaluated in a scientific process.
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
is_a: EvaluatedEntity
attributes:
  composed_of:
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
  has_role:
    name: has_role
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    alias: has_role
    owner: ChemicalSubstance
    domain_of:
    - ChemicalSubstance
    range: string
  title:
    name: title
    description: This slot is described in more detail within the class in which it
      is used.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:title
    alias: title
    owner: ChemicalSubstance
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
    owner: ChemicalSubstance
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
  id:
    name: id
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:identifier
    identifier: true
    alias: id
    owner: ChemicalSubstance
    domain_of:
    - DefinedTerm
    - ResearchDataset
    - ResearchCatalog
    - EvaluatedEntity
    - EvaluatedActivity
    range: uriorcurie
    required: true
  other_identifier:
    name: other_identifier
    description: A secondary identifier of the EvaluatedEntity
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: adms:identifier
    alias: other_identifier
    owner: ChemicalSubstance
    domain_of:
    - Dataset
    - DataCreatingActivity
    - EvaluatedEntity
    - EvaluatedActivity
    - Tool
    - Environment
    range: Identifier
    required: false
    multivalued: true
    inlined_as_list: true
  has_qualitative_attribute:
    name: has_qualitative_attribute
    description: The slot to relate a qualitative attribute to an entity of interest,
      tool or environment.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:relation
    alias: has_qualitative_attribute
    owner: ChemicalSubstance
    domain_of:
    - EvaluatedEntity
    - EvaluatedActivity
    - Tool
    range: QualitativeAttribute
    multivalued: true
    inlined: true
    inlined_as_list: true
  has_quantitative_attribute:
    name: has_quantitative_attribute
    description: The slot to relate a quantitative  attribute to an entity of interest,
      tool or environment.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:relation
    alias: has_quantitative_attribute
    owner: ChemicalSubstance
    domain_of:
    - EvaluatedEntity
    - EvaluatedActivity
    - Tool
    range: QuantitativeAttribute
    multivalued: true
    inlined: true
    inlined_as_list: true
  has_part:
    name: has_part
    description: This slot is described in more detail within the class in which it
      is used.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:hasPart
    alias: has_part
    owner: ChemicalSubstance
    domain_of:
    - Catalogue
    - DataCreatingActivity
    - EvaluatedEntity
    - EvaluatedActivity
    - Tool
    range: string
  was_generated_by:
    name: was_generated_by
    description: A slot to provide the Activity which created the EvaluatedEntity.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: prov:wasGeneratedBy
    alias: was_generated_by
    owner: ChemicalSubstance
    domain_of:
    - Dataset
    - EvaluatedEntity
    range: Activity
    multivalued: true
    inlined_as_list: true
  type:
    name: type
    description: This slot is described in more detail within the class in which it
      is used.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:type
    alias: type
    owner: ChemicalSubstance
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
    owner: ChemicalSubstance
    domain_of:
    - ClassifierMixin
    range: DefinedTerm
    recommended: true
    inlined: true
class_uri: prov:Entity

```
</details>