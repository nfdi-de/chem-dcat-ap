

# Class: DataCreatingActivity


_An activity (process) that has the objective to produce information about an entity by evaluating it._





URI: [prov:Activity](http://www.w3.org/ns/prov#Activity)






```mermaid
 classDiagram
    class DataCreatingActivity
    click DataCreatingActivity href "../DataCreatingActivity"
      ClassifierMixin <|-- DataCreatingActivity
        click ClassifierMixin href "../ClassifierMixin"
      Activity <|-- DataCreatingActivity
        click Activity href "../Activity"
      

      DataCreatingActivity <|-- NMRSpectroscopy
        click NMRSpectroscopy href "../NMRSpectroscopy"
      DataCreatingActivity <|-- DataAnalysis
        click DataAnalysis href "../DataAnalysis"
      
      
      DataCreatingActivity : description
        
      DataCreatingActivity : evaluated_activity
        
          
    
    
    DataCreatingActivity --> "* _recommended_" EvaluatedActivity : evaluated_activity
    click EvaluatedActivity href "../EvaluatedActivity"

        
      DataCreatingActivity : evaluated_entity
        
          
    
    
    DataCreatingActivity --> "* _recommended_" EvaluatedEntity : evaluated_entity
    click EvaluatedEntity href "../EvaluatedEntity"

        
      DataCreatingActivity : has_part
        
          
    
    
    DataCreatingActivity --> "0..1" Activity : has_part
    click Activity href "../Activity"

        
      DataCreatingActivity : occurred_in
        
          
    
    
    DataCreatingActivity --> "0..1" Environment : occurred_in
    click Environment href "../Environment"

        
      DataCreatingActivity : other_identifier
        
          
    
    
    DataCreatingActivity --> "*" Identifier : other_identifier
    click Identifier href "../Identifier"

        
      DataCreatingActivity : rdf_type
        
          
    
    
    DataCreatingActivity --> "0..1 _recommended_" DefinedTerm : rdf_type
    click DefinedTerm href "../DefinedTerm"

        
      DataCreatingActivity : realized_plan
        
          
    
    
    DataCreatingActivity --> "0..1 _recommended_" Plan : realized_plan
    click Plan href "../Plan"

        
      DataCreatingActivity : title
        
      DataCreatingActivity : type
        
          
    
    
    DataCreatingActivity --> "0..1" DefinedTerm : type
    click DefinedTerm href "../DefinedTerm"

        
      DataCreatingActivity : used_tool
        
          
    
    
    DataCreatingActivity --> "* _recommended_" Tool : used_tool
    click Tool href "../Tool"

        
      
```





## Inheritance
* [Activity](Activity.md)
    * **DataCreatingActivity** [ [ClassifierMixin](ClassifierMixin.md)]
        * [NMRSpectroscopy](NMRSpectroscopy.md)
        * [DataAnalysis](DataAnalysis.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [title](title.md) | 0..1 <br/> [String](String.md) | This slot is described in more detail within the class in which it is used | direct |
| [description](description.md) | 0..1 <br/> [String](String.md) | This slot is described in more detail within the class in which it is used | direct |
| [other_identifier](other_identifier.md) | * <br/> [Identifier](Identifier.md) | A secondary identifier of the DataCreatingActivity | direct |
| [evaluated_entity](evaluated_entity.md) | * _recommended_ <br/> [EvaluatedEntity](EvaluatedEntity.md) | The slot to specify the entity of interest that was evaluated | direct |
| [evaluated_activity](evaluated_activity.md) | * _recommended_ <br/> [EvaluatedActivity](EvaluatedActivity.md) | The slot to specify the activity of interest that was evaluated | direct |
| [used_tool](used_tool.md) | * _recommended_ <br/> [Tool](Tool.md) | The slot to specify the tool that was used | direct |
| [realized_plan](realized_plan.md) | 0..1 _recommended_ <br/> [Plan](Plan.md) | The slot to specify the Method (aka Procedure) that was realized by a DataCre... | direct |
| [has_part](has_part.md) | 0..1 <br/> [Activity](Activity.md) | The slot to specify one or more parts of the DataCreatingActivity that are th... | direct |
| [occurred_in](occurred_in.md) | 0..1 <br/> [Environment](Environment.md) | The slot to specify the Method (aka Procedure) that was used in the DataCreat... | direct |
| [type](type.md) | 0..1 <br/> [DefinedTerm](DefinedTerm.md) | This slot is described in more detail within the class in which it is used | [ClassifierMixin](ClassifierMixin.md) |
| [rdf_type](rdf_type.md) | 0..1 _recommended_ <br/> [DefinedTerm](DefinedTerm.md) | The slot to specify the ontology class that is instantiated by an entity | [ClassifierMixin](ClassifierMixin.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ResearchDataset](ResearchDataset.md) | [was_generated_by](was_generated_by.md) | range | [DataCreatingActivity](DataCreatingActivity.md) |
| [AnalysedData](AnalysedData.md) | [was_generated_by](was_generated_by.md) | range | [DataCreatingActivity](DataCreatingActivity.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | prov:Activity |
| native | nfdi4c:DataCreatingActivity |
| narrow | NCIT:C25598, sosa:Observation, OBI:0000070 |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DataCreatingActivity
description: An activity (process) that has the objective to produce information about
  an entity by evaluating it.
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
narrow_mappings:
- NCIT:C25598
- sosa:Observation
- OBI:0000070
is_a: Activity
mixins:
- ClassifierMixin
slots:
- title
- description
- other_identifier
- evaluated_entity
- evaluated_activity
- used_tool
- realized_plan
- has_part
- occurred_in
slot_usage:
  has_part:
    name: has_part
    description: The slot to specify one or more parts of the DataCreatingActivity
      that are themselves also data generating activities.
    range: Activity
    inlined: true
  other_identifier:
    name: other_identifier
    description: A secondary identifier of the DataCreatingActivity
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
name: DataCreatingActivity
description: An activity (process) that has the objective to produce information about
  an entity by evaluating it.
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
narrow_mappings:
- NCIT:C25598
- sosa:Observation
- OBI:0000070
is_a: Activity
mixins:
- ClassifierMixin
slot_usage:
  has_part:
    name: has_part
    description: The slot to specify one or more parts of the DataCreatingActivity
      that are themselves also data generating activities.
    range: Activity
    inlined: true
  other_identifier:
    name: other_identifier
    description: A secondary identifier of the DataCreatingActivity
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
    owner: DataCreatingActivity
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
    owner: DataCreatingActivity
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
    description: A secondary identifier of the DataCreatingActivity
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: adms:identifier
    alias: other_identifier
    owner: DataCreatingActivity
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
  evaluated_entity:
    name: evaluated_entity
    description: The slot to specify the entity of interest that was evaluated.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: prov:used
    alias: evaluated_entity
    owner: DataCreatingActivity
    domain_of:
    - DataCreatingActivity
    range: EvaluatedEntity
    recommended: true
    multivalued: true
    inlined: true
    inlined_as_list: true
  evaluated_activity:
    name: evaluated_activity
    description: The slot to specify the activity of interest that was evaluated.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: prov:wasInformedBy
    alias: evaluated_activity
    owner: DataCreatingActivity
    domain_of:
    - DataCreatingActivity
    range: EvaluatedActivity
    recommended: true
    multivalued: true
    inlined: true
    inlined_as_list: true
  used_tool:
    name: used_tool
    description: The slot to specify the tool that was used.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: prov:used
    alias: used_tool
    owner: DataCreatingActivity
    domain_of:
    - DataCreatingActivity
    range: Tool
    recommended: true
    multivalued: true
    inlined: true
    inlined_as_list: true
  realized_plan:
    name: realized_plan
    description: The slot to specify the Method (aka Procedure) that was realized
      by a DataCreatingActivity.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: prov:used
    alias: realized_plan
    owner: DataCreatingActivity
    domain_of:
    - DataCreatingActivity
    range: Plan
    recommended: true
  has_part:
    name: has_part
    description: The slot to specify one or more parts of the DataCreatingActivity
      that are themselves also data generating activities.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:hasPart
    alias: has_part
    owner: DataCreatingActivity
    domain_of:
    - Catalogue
    - DataCreatingActivity
    - EvaluatedEntity
    - EvaluatedActivity
    - Tool
    range: Activity
    inlined: true
  occurred_in:
    name: occurred_in
    description: The slot to specify the Method (aka Procedure) that was used in the
      DataCreatingActivity.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: BFO:0000066
    alias: occurred_in
    owner: DataCreatingActivity
    domain_of:
    - DataCreatingActivity
    range: Environment
  type:
    name: type
    description: This slot is described in more detail within the class in which it
      is used.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:type
    alias: type
    owner: DataCreatingActivity
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
    owner: DataCreatingActivity
    domain_of:
    - ClassifierMixin
    range: DefinedTerm
    recommended: true
    inlined: true
class_uri: prov:Activity

```
</details>