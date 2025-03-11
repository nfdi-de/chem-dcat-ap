

# Class: Plan


_A piece of information that specifies: a) how an activity has to be carried out by its agents including what _

_kind of steps have to be taken and what kind of parameters have to be met/set._





URI: [prov:Entity](http://www.w3.org/ns/prov#Entity)






```mermaid
 classDiagram
    class Plan
    click Plan href "../Plan"
      ClassifierMixin <|-- Plan
        click ClassifierMixin href "../ClassifierMixin"
      
      Plan : description
        
      Plan : rdf_type
        
          
    
    
    Plan --> "0..1 _recommended_" DefinedTerm : rdf_type
    click DefinedTerm href "../DefinedTerm"

        
      Plan : title
        
      Plan : type
        
          
    
    
    Plan --> "0..1" DefinedTerm : type
    click DefinedTerm href "../DefinedTerm"

        
      
```





## Inheritance
* **Plan** [ [ClassifierMixin](ClassifierMixin.md)]



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [title](title.md) | 0..1 <br/> [String](String.md) | This slot is described in more detail within the class in which it is used | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) | This slot is described in more detail within the class in which it is used | direct |
| [type](type.md) | 0..1 <br/> [DefinedTerm](DefinedTerm.md) | This slot is described in more detail within the class in which it is used | [ClassifierMixin](ClassifierMixin.md) |
| [rdf_type](rdf_type.md) | 0..1 _recommended_ <br/> [DefinedTerm](DefinedTerm.md) | The slot to specify the ontology class that is instantiated by an entity | [ClassifierMixin](ClassifierMixin.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [NMRSpectralAnalysis](NMRSpectralAnalysis.md) | [realized_plan](realized_plan.md) | range | [Plan](Plan.md) |
| [NMRSpectroscopy](NMRSpectroscopy.md) | [realized_plan](realized_plan.md) | range | [Plan](Plan.md) |
| [DataCreatingActivity](DataCreatingActivity.md) | [realized_plan](realized_plan.md) | range | [Plan](Plan.md) |
| [DataAnalysis](DataAnalysis.md) | [realized_plan](realized_plan.md) | range | [Plan](Plan.md) |




## Aliases


* Plan Specification
* Method
* Procedure




## Examples

| Value |
| --- |
| None |

## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | prov:Entity |
| native | nfdi4c:Plan |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Plan
description: "A piece of information that specifies: a) how an activity has to be\
  \ carried out by its agents including what \nkind of steps have to be taken and\
  \ what kind of parameters have to be met/set."
examples:
- description: 'We assigned the structure of sample CRS-37013 using a 13C NMR (CHMO:0000595)
    and the settings: pulse sequence: zgpg30, temperature: 298.0 K, number of scans:
    1024, Solvent : chloroform-D1 (CDCl3).'
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
aliases:
- Plan Specification
- Method
- Procedure
mixins:
- ClassifierMixin
slots:
- title
- description
class_uri: prov:Entity

```
</details>

### Induced

<details>
```yaml
name: Plan
description: "A piece of information that specifies: a) how an activity has to be\
  \ carried out by its agents including what \nkind of steps have to be taken and\
  \ what kind of parameters have to be met/set."
examples:
- description: 'We assigned the structure of sample CRS-37013 using a 13C NMR (CHMO:0000595)
    and the settings: pulse sequence: zgpg30, temperature: 298.0 K, number of scans:
    1024, Solvent : chloroform-D1 (CDCl3).'
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
aliases:
- Plan Specification
- Method
- Procedure
mixins:
- ClassifierMixin
attributes:
  title:
    name: title
    description: This slot is described in more detail within the class in which it
      is used.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:title
    alias: title
    owner: Plan
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
    owner: Plan
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
  type:
    name: type
    description: This slot is described in more detail within the class in which it
      is used.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:type
    alias: type
    owner: Plan
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
    owner: Plan
    domain_of:
    - ClassifierMixin
    range: DefinedTerm
    recommended: true
    inlined: true
class_uri: prov:Entity

```
</details>