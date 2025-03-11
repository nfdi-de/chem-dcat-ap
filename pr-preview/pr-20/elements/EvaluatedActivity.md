

# Class: EvaluatedActivity


_An activity or process that is being evaluated in a DataCreatingActivity._





URI: [prov:Activity](http://www.w3.org/ns/prov#Activity)






```mermaid
 classDiagram
    class EvaluatedActivity
    click EvaluatedActivity href "../EvaluatedActivity"
      ClassifierMixin <|-- EvaluatedActivity
        click ClassifierMixin href "../ClassifierMixin"
      Activity <|-- EvaluatedActivity
        click Activity href "../Activity"
      

      EvaluatedActivity <|-- ChemicalReaction
        click ChemicalReaction href "../ChemicalReaction"
      
      
      EvaluatedActivity : description
        
      EvaluatedActivity : has_part
        
      EvaluatedActivity : has_qualitative_attribute
        
          
    
    
    EvaluatedActivity --> "*" QualitativeAttribute : has_qualitative_attribute
    click QualitativeAttribute href "../QualitativeAttribute"

        
      EvaluatedActivity : has_quantitative_attribute
        
          
    
    
    EvaluatedActivity --> "*" QuantitativeAttribute : has_quantitative_attribute
    click QuantitativeAttribute href "../QuantitativeAttribute"

        
      EvaluatedActivity : id
        
      EvaluatedActivity : other_identifier
        
          
    
    
    EvaluatedActivity --> "*" Identifier : other_identifier
    click Identifier href "../Identifier"

        
      EvaluatedActivity : rdf_type
        
          
    
    
    EvaluatedActivity --> "0..1 _recommended_" DefinedTerm : rdf_type
    click DefinedTerm href "../DefinedTerm"

        
      EvaluatedActivity : title
        
      EvaluatedActivity : type
        
          
    
    
    EvaluatedActivity --> "0..1" DefinedTerm : type
    click DefinedTerm href "../DefinedTerm"

        
      
```





## Inheritance
* [Activity](Activity.md)
    * **EvaluatedActivity** [ [ClassifierMixin](ClassifierMixin.md)]
        * [ChemicalReaction](ChemicalReaction.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [title](title.md) | 0..1 <br/> [String](String.md) | This slot is described in more detail within the class in which it is used | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) | This slot is described in more detail within the class in which it is used | direct |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) |  | direct |
| [other_identifier](other_identifier.md) | * <br/> [Identifier](Identifier.md) | A secondary identifier of the EvaluatedActivity | direct |
| [has_qualitative_attribute](has_qualitative_attribute.md) | * <br/> [QualitativeAttribute](QualitativeAttribute.md) | The slot to relate a qualitative attribute to an entity of interest, tool or ... | direct |
| [has_quantitative_attribute](has_quantitative_attribute.md) | * <br/> [QuantitativeAttribute](QuantitativeAttribute.md) | The slot to relate a quantitative  attribute to an entity of interest, tool o... | direct |
| [has_part](has_part.md) | 0..1 <br/> [String](String.md) | This slot is described in more detail within the class in which it is used | direct |
| [type](type.md) | 0..1 <br/> [DefinedTerm](DefinedTerm.md) | This slot is described in more detail within the class in which it is used | [ClassifierMixin](ClassifierMixin.md) |
| [rdf_type](rdf_type.md) | 0..1 _recommended_ <br/> [DefinedTerm](DefinedTerm.md) | The slot to specify the ontology class that is instantiated by an entity | [ClassifierMixin](ClassifierMixin.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [NMRAnalysisDataset](NMRAnalysisDataset.md) | [describes_activity](describes_activity.md) | range | [EvaluatedActivity](EvaluatedActivity.md) |
| [NMRSpectralAnalysis](NMRSpectralAnalysis.md) | [evaluated_activity](evaluated_activity.md) | range | [EvaluatedActivity](EvaluatedActivity.md) |
| [NMRSpectroscopy](NMRSpectroscopy.md) | [evaluated_activity](evaluated_activity.md) | range | [EvaluatedActivity](EvaluatedActivity.md) |
| [ResearchDataset](ResearchDataset.md) | [describes_activity](describes_activity.md) | range | [EvaluatedActivity](EvaluatedActivity.md) |
| [AnalysisDataset](AnalysisDataset.md) | [describes_activity](describes_activity.md) | range | [EvaluatedActivity](EvaluatedActivity.md) |
| [DataCreatingActivity](DataCreatingActivity.md) | [evaluated_activity](evaluated_activity.md) | range | [EvaluatedActivity](EvaluatedActivity.md) |
| [DataAnalysis](DataAnalysis.md) | [evaluated_activity](evaluated_activity.md) | range | [EvaluatedActivity](EvaluatedActivity.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | prov:Activity |
| native | nfdi4c:EvaluatedActivity |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: EvaluatedActivity
description: An activity or process that is being evaluated in a DataCreatingActivity.
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
is_a: Activity
mixins:
- ClassifierMixin
slots:
- title
- description
- id
- other_identifier
- has_qualitative_attribute
- has_quantitative_attribute
- has_part
slot_usage:
  other_identifier:
    name: other_identifier
    description: A secondary identifier of the EvaluatedActivity
    slot_uri: adms:identifier
    range: Identifier
    required: false
    multivalued: true
    inlined_as_list: true
class_uri: prov:Activity

```
</details>

### Induced

<details>
```yaml
name: EvaluatedActivity
description: An activity or process that is being evaluated in a DataCreatingActivity.
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
is_a: Activity
mixins:
- ClassifierMixin
slot_usage:
  other_identifier:
    name: other_identifier
    description: A secondary identifier of the EvaluatedActivity
    slot_uri: adms:identifier
    range: Identifier
    required: false
    multivalued: true
    inlined_as_list: true
attributes:
  title:
    name: title
    description: This slot is described in more detail within the class in which it
      is used.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:title
    alias: title
    owner: EvaluatedActivity
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
    owner: EvaluatedActivity
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
    owner: EvaluatedActivity
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
    description: A secondary identifier of the EvaluatedActivity
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: adms:identifier
    alias: other_identifier
    owner: EvaluatedActivity
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
    owner: EvaluatedActivity
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
    owner: EvaluatedActivity
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
    owner: EvaluatedActivity
    domain_of:
    - Catalogue
    - DataCreatingActivity
    - EvaluatedEntity
    - EvaluatedActivity
    - Tool
    range: string
  type:
    name: type
    description: This slot is described in more detail within the class in which it
      is used.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:type
    alias: type
    owner: EvaluatedActivity
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
    owner: EvaluatedActivity
    domain_of:
    - ClassifierMixin
    range: DefinedTerm
    recommended: true
    inlined: true
class_uri: prov:Activity

```
</details>