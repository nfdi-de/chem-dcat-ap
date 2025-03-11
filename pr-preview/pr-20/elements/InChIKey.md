

# Class: InChIKey



URI: [CHEMINF:000059](http://semanticscience.org/resource/CHEMINF_000059)






```mermaid
 classDiagram
    class InChIKey
    click InChIKey href "../InChIKey"
      QualitativeAttribute <|-- InChIKey
        click QualitativeAttribute href "../QualitativeAttribute"
      
      InChIKey : description
        
      InChIKey : rdf_type
        
          
    
    
    InChIKey --> "0..1 _recommended_" DefinedTerm : rdf_type
    click DefinedTerm href "../DefinedTerm"

        
      InChIKey : title
        
      InChIKey : type
        
          
    
    
    InChIKey --> "0..1" DefinedTerm : type
    click DefinedTerm href "../DefinedTerm"

        
      InChIKey : value
        
      
```





## Inheritance
* [QualitativeAttribute](QualitativeAttribute.md) [ [ClassifierMixin](ClassifierMixin.md)]
    * **InChIKey**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [title](title.md) | 0..1 <br/> [String](String.md) | This slot is described in more detail within the class in which it is used | [QualitativeAttribute](QualitativeAttribute.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | This slot is described in more detail within the class in which it is used | [QualitativeAttribute](QualitativeAttribute.md) |
| [value](value.md) | 1 <br/> [String](String.md) | The slot to provide the literal value of the QualitativeAttribute | [QualitativeAttribute](QualitativeAttribute.md) |
| [type](type.md) | 0..1 <br/> [DefinedTerm](DefinedTerm.md) | This slot is described in more detail within the class in which it is used | [ClassifierMixin](ClassifierMixin.md) |
| [rdf_type](rdf_type.md) | 0..1 _recommended_ <br/> [DefinedTerm](DefinedTerm.md) | The slot to specify the ontology class that is instantiated by an entity | [ClassifierMixin](ClassifierMixin.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ChemicalEntity](ChemicalEntity.md) | [inchikey](inchikey.md) | range | [InChIKey](InChIKey.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | CHEMINF:000059 |
| native | nfdi4c:InChIKey |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: InChIKey
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
is_a: QualitativeAttribute
class_uri: CHEMINF:000059

```
</details>

### Induced

<details>
```yaml
name: InChIKey
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
is_a: QualitativeAttribute
attributes:
  title:
    name: title
    description: This slot is described in more detail within the class in which it
      is used.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:title
    alias: title
    owner: InChIKey
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
    owner: InChIKey
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
    owner: InChIKey
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
    owner: InChIKey
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
    owner: InChIKey
    domain_of:
    - ClassifierMixin
    range: DefinedTerm
    recommended: true
    inlined: true
class_uri: CHEMINF:000059

```
</details>