

# Class: Environment


_The surrounding in which the dataset creating activity took place (e.g. a lab)._





URI: [prov:Entity](http://www.w3.org/ns/prov#Entity)






```mermaid
 classDiagram
    class Environment
    click Environment href "../Environment"
      ClassifierMixin <|-- Environment
        click ClassifierMixin href "../ClassifierMixin"
      

      Environment <|-- Laboratory
        click Laboratory href "../Laboratory"
      
      
      Environment : description
        
      Environment : other_identifier
        
          
    
    
    Environment --> "*" Identifier : other_identifier
    click Identifier href "../Identifier"

        
      Environment : rdf_type
        
          
    
    
    Environment --> "0..1 _recommended_" DefinedTerm : rdf_type
    click DefinedTerm href "../DefinedTerm"

        
      Environment : title
        
      Environment : type
        
          
    
    
    Environment --> "0..1" DefinedTerm : type
    click DefinedTerm href "../DefinedTerm"

        
      
```





## Inheritance
* **Environment** [ [ClassifierMixin](ClassifierMixin.md)]
    * [Laboratory](Laboratory.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [title](title.md) | 0..1 <br/> [String](String.md) | This slot is described in more detail within the class in which it is used | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) | This slot is described in more detail within the class in which it is used | direct |
| [other_identifier](other_identifier.md) | * <br/> [Identifier](Identifier.md) | A secondary identifier of the Environment | direct |
| [type](type.md) | 0..1 <br/> [DefinedTerm](DefinedTerm.md) | This slot is described in more detail within the class in which it is used | [ClassifierMixin](ClassifierMixin.md) |
| [rdf_type](rdf_type.md) | 0..1 _recommended_ <br/> [DefinedTerm](DefinedTerm.md) | The slot to specify the ontology class that is instantiated by an entity | [ClassifierMixin](ClassifierMixin.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [NMRSpectralAnalysis](NMRSpectralAnalysis.md) | [occurred_in](occurred_in.md) | range | [Environment](Environment.md) |
| [NMRSpectroscopy](NMRSpectroscopy.md) | [occurred_in](occurred_in.md) | range | [Environment](Environment.md) |
| [DataCreatingActivity](DataCreatingActivity.md) | [occurred_in](occurred_in.md) | range | [Environment](Environment.md) |
| [DataAnalysis](DataAnalysis.md) | [occurred_in](occurred_in.md) | range | [Environment](Environment.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | prov:Entity |
| native | nfdi4c:Environment |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Environment
description: The surrounding in which the dataset creating activity took place (e.g.
  a lab).
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
mixins:
- ClassifierMixin
slots:
- title
- description
- other_identifier
slot_usage:
  other_identifier:
    name: other_identifier
    description: A secondary identifier of the Environment
    slot_uri: adms:identifier
    range: Identifier
    required: false
    multivalued: true
    inlined_as_list: true
class_uri: prov:Entity

```
</details>

### Induced

<details>
```yaml
name: Environment
description: The surrounding in which the dataset creating activity took place (e.g.
  a lab).
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
mixins:
- ClassifierMixin
slot_usage:
  other_identifier:
    name: other_identifier
    description: A secondary identifier of the Environment
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
    owner: Environment
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
    owner: Environment
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
  other_identifier:
    name: other_identifier
    description: A secondary identifier of the Environment
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: adms:identifier
    alias: other_identifier
    owner: Environment
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
  type:
    name: type
    description: This slot is described in more detail within the class in which it
      is used.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:type
    alias: type
    owner: Environment
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
    owner: Environment
    domain_of:
    - ClassifierMixin
    range: DefinedTerm
    recommended: true
    inlined: true
class_uri: prov:Entity

```
</details>