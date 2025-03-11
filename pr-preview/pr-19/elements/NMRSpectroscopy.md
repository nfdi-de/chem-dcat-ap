

# Class: NMRSpectroscopy


_Spectroscopy where the energy states of spin-active nuclei placed in a static magnetic field are interrogated by inducing transitions between the states via radio frequency irradiation. Each experiment consists of a sequence of radio frequency pulses with delay periods in between them._





URI: [nfdi4c:NMRSpectroscopy](https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap/NMRSpectroscopy)






```mermaid
 classDiagram
    class NMRSpectroscopy
    click NMRSpectroscopy href "../NMRSpectroscopy"
      DataCreatingActivity <|-- NMRSpectroscopy
        click DataCreatingActivity href "../DataCreatingActivity"
      
      NMRSpectroscopy : description
        
      NMRSpectroscopy : evaluated_activity
        
          
    
    
    NMRSpectroscopy --> "* _recommended_" EvaluatedActivity : evaluated_activity
    click EvaluatedActivity href "../EvaluatedActivity"

        
      NMRSpectroscopy : evaluated_entity
        
          
    
    
    NMRSpectroscopy --> "* _recommended_" ChemicalSample : evaluated_entity
    click ChemicalSample href "../ChemicalSample"

        
      NMRSpectroscopy : has_part
        
          
    
    
    NMRSpectroscopy --> "0..1" Activity : has_part
    click Activity href "../Activity"

        
      NMRSpectroscopy : occurred_in
        
          
    
    
    NMRSpectroscopy --> "0..1" Environment : occurred_in
    click Environment href "../Environment"

        
      NMRSpectroscopy : other_identifier
        
          
    
    
    NMRSpectroscopy --> "*" Identifier : other_identifier
    click Identifier href "../Identifier"

        
      NMRSpectroscopy : rdf_type
        
          
    
    
    NMRSpectroscopy --> "0..1 _recommended_" DefinedTerm : rdf_type
    click DefinedTerm href "../DefinedTerm"

        
      NMRSpectroscopy : realized_plan
        
          
    
    
    NMRSpectroscopy --> "0..1 _recommended_" Plan : realized_plan
    click Plan href "../Plan"

        
      NMRSpectroscopy : title
        
      NMRSpectroscopy : type
        
          
    
    
    NMRSpectroscopy --> "0..1" DefinedTerm : type
    click DefinedTerm href "../DefinedTerm"

        
      NMRSpectroscopy : used_tool
        
          
    
    
    NMRSpectroscopy --> "* _recommended_" Tool : used_tool
    click Tool href "../Tool"

        
      
```





## Inheritance
* [Activity](Activity.md)
    * [DataCreatingActivity](DataCreatingActivity.md) [ [ClassifierMixin](ClassifierMixin.md)]
        * **NMRSpectroscopy**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [title](title.md) | 0..1 <br/> [String](String.md) | This slot is described in more detail within the class in which it is used | [DataCreatingActivity](DataCreatingActivity.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | This slot is described in more detail within the class in which it is used | [DataCreatingActivity](DataCreatingActivity.md) |
| [other_identifier](other_identifier.md) | * <br/> [Identifier](Identifier.md) | A secondary identifier of the DataCreatingActivity | [DataCreatingActivity](DataCreatingActivity.md) |
| [evaluated_entity](evaluated_entity.md) | * _recommended_ <br/> [ChemicalSample](ChemicalSample.md) | The slot to specify the entity of interest that was evaluated | [DataCreatingActivity](DataCreatingActivity.md) |
| [evaluated_activity](evaluated_activity.md) | * _recommended_ <br/> [EvaluatedActivity](EvaluatedActivity.md) | The slot to specify the activity of interest that was evaluated | [DataCreatingActivity](DataCreatingActivity.md) |
| [used_tool](used_tool.md) | * _recommended_ <br/> [Tool](Tool.md) | The slot to specify the tool that was used | [DataCreatingActivity](DataCreatingActivity.md) |
| [realized_plan](realized_plan.md) | 0..1 _recommended_ <br/> [Plan](Plan.md) | The slot to specify the Method (aka Procedure) that was realized by a DataCre... | [DataCreatingActivity](DataCreatingActivity.md) |
| [has_part](has_part.md) | 0..1 <br/> [Activity](Activity.md) | The slot to specify one or more parts of the DataCreatingActivity that are th... | [DataCreatingActivity](DataCreatingActivity.md) |
| [occurred_in](occurred_in.md) | 0..1 <br/> [Environment](Environment.md) | The slot to specify the Method (aka Procedure) that was used in the DataCreat... | [DataCreatingActivity](DataCreatingActivity.md) |
| [type](type.md) | 0..1 <br/> [DefinedTerm](DefinedTerm.md) | This slot is described in more detail within the class in which it is used | [ClassifierMixin](ClassifierMixin.md) |
| [rdf_type](rdf_type.md) | 0..1 _recommended_ <br/> [DefinedTerm](DefinedTerm.md) | The type of NMR Spectroscopy provided as CURIE of a subclass of CHMO:0000613 | [ClassifierMixin](ClassifierMixin.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [NMRSpectrum](NMRSpectrum.md) | [was_generated_by](was_generated_by.md) | range | [NMRSpectroscopy](NMRSpectroscopy.md) |






## Comments

* This class serves as an example for the way in which we want to build domain specific schema profiles. It will be outsourced to a more appropriate location in the future.

## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | nfdi4c:NMRSpectroscopy |
| native | nfdi4c:NMRSpectroscopy |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NMRSpectroscopy
description: Spectroscopy where the energy states of spin-active nuclei placed in
  a static magnetic field are interrogated by inducing transitions between the states
  via radio frequency irradiation. Each experiment consists of a sequence of radio
  frequency pulses with delay periods in between them.
comments:
- This class serves as an example for the way in which we want to build domain specific
  schema profiles. It will be outsourced to a more appropriate location in the future.
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
is_a: DataCreatingActivity
slot_usage:
  evaluated_entity:
    name: evaluated_entity
    range: ChemicalSample
  rdf_type:
    name: rdf_type
    description: The type of NMR Spectroscopy provided as CURIE of a subclass of CHMO:0000613.
    bindings:
    - range: NMRAssayEnum
      obligation_level: RECOMMENDED
      binds_value_of: id
      description: NMR types from the Chemical Methods Ontology

```
</details>

### Induced

<details>
```yaml
name: NMRSpectroscopy
description: Spectroscopy where the energy states of spin-active nuclei placed in
  a static magnetic field are interrogated by inducing transitions between the states
  via radio frequency irradiation. Each experiment consists of a sequence of radio
  frequency pulses with delay periods in between them.
comments:
- This class serves as an example for the way in which we want to build domain specific
  schema profiles. It will be outsourced to a more appropriate location in the future.
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
is_a: DataCreatingActivity
slot_usage:
  evaluated_entity:
    name: evaluated_entity
    range: ChemicalSample
  rdf_type:
    name: rdf_type
    description: The type of NMR Spectroscopy provided as CURIE of a subclass of CHMO:0000613.
    bindings:
    - range: NMRAssayEnum
      obligation_level: RECOMMENDED
      binds_value_of: id
      description: NMR types from the Chemical Methods Ontology
attributes:
  title:
    name: title
    description: This slot is described in more detail within the class in which it
      is used.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:title
    alias: title
    owner: NMRSpectroscopy
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
    owner: NMRSpectroscopy
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
    owner: NMRSpectroscopy
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
    owner: NMRSpectroscopy
    domain_of:
    - DataCreatingActivity
    range: ChemicalSample
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
    owner: NMRSpectroscopy
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
    owner: NMRSpectroscopy
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
    owner: NMRSpectroscopy
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
    owner: NMRSpectroscopy
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
    owner: NMRSpectroscopy
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
    owner: NMRSpectroscopy
    domain_of:
    - Agent
    - Dataset
    - LicenseDocument
    - ClassifierMixin
    range: DefinedTerm
    inlined: true
  rdf_type:
    name: rdf_type
    description: The type of NMR Spectroscopy provided as CURIE of a subclass of CHMO:0000613.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: rdf:type
    alias: rdf_type
    owner: NMRSpectroscopy
    domain_of:
    - ClassifierMixin
    range: DefinedTerm
    bindings:
    - range: NMRAssayEnum
      obligation_level: RECOMMENDED
      binds_value_of: id
      description: NMR types from the Chemical Methods Ontology
    recommended: true
    inlined: true

```
</details>