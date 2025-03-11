

# Class: NMRSpectrum


_A set of chemical shifts obtained via NMR spectroscopy._





URI: [NMR:1002007](http://nmrML.org/nmrCV#NMR:1002007)






```mermaid
 classDiagram
    class NMRSpectrum
    click NMRSpectrum href "../NMRSpectrum"
      AnalysedData <|-- NMRSpectrum
        click AnalysedData href "../AnalysedData"
      
      NMRSpectrum : description
        
      NMRSpectrum : has_part
        
      NMRSpectrum : has_qualitative_attribute
        
          
    
    
    NMRSpectrum --> "*" QualitativeAttribute : has_qualitative_attribute
    click QualitativeAttribute href "../QualitativeAttribute"

        
      NMRSpectrum : has_quantitative_attribute
        
          
    
    
    NMRSpectrum --> "*" QuantitativeAttribute : has_quantitative_attribute
    click QuantitativeAttribute href "../QuantitativeAttribute"

        
      NMRSpectrum : id
        
      NMRSpectrum : other_identifier
        
          
    
    
    NMRSpectrum --> "*" Identifier : other_identifier
    click Identifier href "../Identifier"

        
      NMRSpectrum : rdf_type
        
          
    
    
    NMRSpectrum --> "0..1 _recommended_" DefinedTerm : rdf_type
    click DefinedTerm href "../DefinedTerm"

        
      NMRSpectrum : title
        
      NMRSpectrum : type
        
          
    
    
    NMRSpectrum --> "0..1" DefinedTerm : type
    click DefinedTerm href "../DefinedTerm"

        
      NMRSpectrum : was_generated_by
        
          
    
    
    NMRSpectrum --> "*" NMRSpectroscopy : was_generated_by
    click NMRSpectroscopy href "../NMRSpectroscopy"

        
      
```





## Inheritance
* [EvaluatedEntity](EvaluatedEntity.md) [ [ClassifierMixin](ClassifierMixin.md)]
    * [AnalysedData](AnalysedData.md)
        * **NMRSpectrum**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [title](title.md) | 0..1 <br/> [String](String.md) | This slot is described in more detail within the class in which it is used | [EvaluatedEntity](EvaluatedEntity.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | This slot is described in more detail within the class in which it is used | [EvaluatedEntity](EvaluatedEntity.md) |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) |  | [EvaluatedEntity](EvaluatedEntity.md) |
| [other_identifier](other_identifier.md) | * <br/> [Identifier](Identifier.md) | A secondary identifier of the EvaluatedEntity | [EvaluatedEntity](EvaluatedEntity.md) |
| [has_qualitative_attribute](has_qualitative_attribute.md) | * <br/> [QualitativeAttribute](QualitativeAttribute.md) | The slot to relate a qualitative attribute to an entity of interest, tool or ... | [EvaluatedEntity](EvaluatedEntity.md) |
| [has_quantitative_attribute](has_quantitative_attribute.md) | * <br/> [QuantitativeAttribute](QuantitativeAttribute.md) | The slot to relate a quantitative  attribute to an entity of interest, tool o... | [EvaluatedEntity](EvaluatedEntity.md) |
| [has_part](has_part.md) | 0..1 <br/> [String](String.md) | This slot is described in more detail within the class in which it is used | [EvaluatedEntity](EvaluatedEntity.md) |
| [was_generated_by](was_generated_by.md) | * <br/> [NMRSpectroscopy](NMRSpectroscopy.md) | A slot to provide the Activity which created the EvaluatedEntity | [EvaluatedEntity](EvaluatedEntity.md) |
| [type](type.md) | 0..1 <br/> [DefinedTerm](DefinedTerm.md) | This slot is described in more detail within the class in which it is used | [ClassifierMixin](ClassifierMixin.md) |
| [rdf_type](rdf_type.md) | 0..1 _recommended_ <br/> [DefinedTerm](DefinedTerm.md) | The slot to specify the ontology class that is instantiated by an entity | [ClassifierMixin](ClassifierMixin.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [NMRSpectralAnalysis](NMRSpectralAnalysis.md) | [evaluated_entity](evaluated_entity.md) | range | [NMRSpectrum](NMRSpectrum.md) |






## Comments

* This class serves as an example for the way in which we want to build domain specific schema profiles. It will be outsourced to a more appropriate location in the future.

## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | NMR:1002007 |
| native | nfdi4c:NMRSpectrum |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NMRSpectrum
description: A set of chemical shifts obtained via NMR spectroscopy.
comments:
- This class serves as an example for the way in which we want to build domain specific
  schema profiles. It will be outsourced to a more appropriate location in the future.
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
is_a: AnalysedData
slot_usage:
  was_generated_by:
    name: was_generated_by
    range: NMRSpectroscopy
    multivalued: true
    inlined_as_list: true
class_uri: NMR:1002007

```
</details>

### Induced

<details>
```yaml
name: NMRSpectrum
description: A set of chemical shifts obtained via NMR spectroscopy.
comments:
- This class serves as an example for the way in which we want to build domain specific
  schema profiles. It will be outsourced to a more appropriate location in the future.
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
is_a: AnalysedData
slot_usage:
  was_generated_by:
    name: was_generated_by
    range: NMRSpectroscopy
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
    owner: NMRSpectrum
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
    owner: NMRSpectrum
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
    owner: NMRSpectrum
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
    owner: NMRSpectrum
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
    owner: NMRSpectrum
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
    owner: NMRSpectrum
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
    owner: NMRSpectrum
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
    owner: NMRSpectrum
    domain_of:
    - Dataset
    - EvaluatedEntity
    range: NMRSpectroscopy
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
    owner: NMRSpectrum
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
    owner: NMRSpectrum
    domain_of:
    - ClassifierMixin
    range: DefinedTerm
    recommended: true
    inlined: true
class_uri: NMR:1002007

```
</details>