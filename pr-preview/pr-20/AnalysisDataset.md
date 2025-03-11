

# Class: AnalysisDataset



URI: [dcat:Dataset](http://www.w3.org/ns/dcat#Dataset)






```mermaid
 classDiagram
    class AnalysisDataset
    click AnalysisDataset href "../AnalysisDataset"
      ResearchDataset <|-- AnalysisDataset
        click ResearchDataset href "../ResearchDataset"
      

      AnalysisDataset <|-- NMRAnalysisDataset
        click NMRAnalysisDataset href "../NMRAnalysisDataset"
      
      
      AnalysisDataset : access_rights
        
          
    
    
    AnalysisDataset --> "0..1" RightsStatement : access_rights
    click RightsStatement href "../RightsStatement"

        
      AnalysisDataset : applicable_legislation
        
          
    
    
    AnalysisDataset --> "*" LegalResource : applicable_legislation
    click LegalResource href "../LegalResource"

        
      AnalysisDataset : conforms_to
        
          
    
    
    AnalysisDataset --> "*" Standard : conforms_to
    click Standard href "../Standard"

        
      AnalysisDataset : contact_point
        
          
    
    
    AnalysisDataset --> "* _recommended_" Kind : contact_point
    click Kind href "../Kind"

        
      AnalysisDataset : creator
        
          
    
    
    AnalysisDataset --> "*" Agent : creator
    click Agent href "../Agent"

        
      AnalysisDataset : dataset_distribution
        
          
    
    
    AnalysisDataset --> "*" Distribution : dataset_distribution
    click Distribution href "../Distribution"

        
      AnalysisDataset : describes_activity
        
          
    
    
    AnalysisDataset --> "* _recommended_" EvaluatedActivity : describes_activity
    click EvaluatedActivity href "../EvaluatedActivity"

        
      AnalysisDataset : describes_entity
        
          
    
    
    AnalysisDataset --> "* _recommended_" EvaluatedEntity : describes_entity
    click EvaluatedEntity href "../EvaluatedEntity"

        
      AnalysisDataset : description
        
      AnalysisDataset : documentation
        
          
    
    
    AnalysisDataset --> "*" Document : documentation
    click Document href "../Document"

        
      AnalysisDataset : frequency
        
          
    
    
    AnalysisDataset --> "0..1" Frequency : frequency
    click Frequency href "../Frequency"

        
      AnalysisDataset : geographical_coverage
        
          
    
    
    AnalysisDataset --> "*" Location : geographical_coverage
    click Location href "../Location"

        
      AnalysisDataset : has_version
        
          
    
    
    AnalysisDataset --> "*" Dataset : has_version
    click Dataset href "../Dataset"

        
      AnalysisDataset : id
        
      AnalysisDataset : identifier
        
      AnalysisDataset : in_series
        
          
    
    
    AnalysisDataset --> "*" DatasetSeries : in_series
    click DatasetSeries href "../DatasetSeries"

        
      AnalysisDataset : is_referenced_by
        
          
    
    
    AnalysisDataset --> "*" Resource : is_referenced_by
    click Resource href "../Resource"

        
      AnalysisDataset : keyword
        
      AnalysisDataset : landing_page
        
          
    
    
    AnalysisDataset --> "*" Document : landing_page
    click Document href "../Document"

        
      AnalysisDataset : language
        
          
    
    
    AnalysisDataset --> "*" LinguisticSystem : language
    click LinguisticSystem href "../LinguisticSystem"

        
      AnalysisDataset : modification_date
        
      AnalysisDataset : other_identifier
        
          
    
    
    AnalysisDataset --> "*" Identifier : other_identifier
    click Identifier href "../Identifier"

        
      AnalysisDataset : provenance
        
          
    
    
    AnalysisDataset --> "*" ProvenanceStatement : provenance
    click ProvenanceStatement href "../ProvenanceStatement"

        
      AnalysisDataset : publisher
        
          
    
    
    AnalysisDataset --> "0..1" Agent : publisher
    click Agent href "../Agent"

        
      AnalysisDataset : qualified_attribution
        
          
    
    
    AnalysisDataset --> "*" Attribution : qualified_attribution
    click Attribution href "../Attribution"

        
      AnalysisDataset : qualified_relation
        
          
    
    
    AnalysisDataset --> "*" Relationship : qualified_relation
    click Relationship href "../Relationship"

        
      AnalysisDataset : related_resource
        
          
    
    
    AnalysisDataset --> "*" Resource : related_resource
    click Resource href "../Resource"

        
      AnalysisDataset : release_date
        
      AnalysisDataset : sample
        
          
    
    
    AnalysisDataset --> "*" Distribution : sample
    click Distribution href "../Distribution"

        
      AnalysisDataset : source
        
          
    
    
    AnalysisDataset --> "*" Dataset : source
    click Dataset href "../Dataset"

        
      AnalysisDataset : spatial_resolution
        
      AnalysisDataset : temporal_coverage
        
          
    
    
    AnalysisDataset --> "*" PeriodOfTime : temporal_coverage
    click PeriodOfTime href "../PeriodOfTime"

        
      AnalysisDataset : temporal_resolution
        
      AnalysisDataset : theme
        
          
    
    
    AnalysisDataset --> "* _recommended_" Concept : theme
    click Concept href "../Concept"

        
      AnalysisDataset : title
        
      AnalysisDataset : type
        
          
    
    
    AnalysisDataset --> "*" Concept : type
    click Concept href "../Concept"

        
      AnalysisDataset : version
        
      AnalysisDataset : version_notes
        
      AnalysisDataset : was_generated_by
        
          
    
    
    AnalysisDataset --> "1..*" DataAnalysis : was_generated_by
    click DataAnalysis href "../DataAnalysis"

        
      
```





## Inheritance
* [Dataset](Dataset.md)
    * [ResearchDataset](ResearchDataset.md)
        * **AnalysisDataset**
            * [NMRAnalysisDataset](NMRAnalysisDataset.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) |  | [ResearchDataset](ResearchDataset.md) |
| [describes_entity](describes_entity.md) | * _recommended_ <br/> [EvaluatedEntity](EvaluatedEntity.md) | A slot to provide the EvaluatedEntity that is described by a Dataset | [ResearchDataset](ResearchDataset.md) |
| [describes_activity](describes_activity.md) | * _recommended_ <br/> [EvaluatedActivity](EvaluatedActivity.md) | A slot to provide the EvaluatedActivity that is described by a Dataset | [ResearchDataset](ResearchDataset.md) |
| [access_rights](access_rights.md) | 0..1 <br/> [RightsStatement](RightsStatement.md) | Information that indicates whether the Dataset is publicly accessible, has ac... | [Dataset](Dataset.md) |
| [applicable_legislation](applicable_legislation.md) | * <br/> [LegalResource](LegalResource.md) | The legislation that mandates the creation or management of the Dataset | [Dataset](Dataset.md) |
| [conforms_to](conforms_to.md) | * <br/> [Standard](Standard.md) | An implementing rule or other specification | [Dataset](Dataset.md) |
| [contact_point](contact_point.md) | * _recommended_ <br/> [Kind](Kind.md) | Contact information that can be used for sending comments about the Dataset | [Dataset](Dataset.md) |
| [creator](creator.md) | * <br/> [Agent](Agent.md) | An entity responsible for producing the dataset | [Dataset](Dataset.md) |
| [dataset_distribution](dataset_distribution.md) | * <br/> [Distribution](Distribution.md) | An available Distribution for the Dataset | [Dataset](Dataset.md) |
| [description](description.md) | 1..* <br/> [String](String.md) | A free-text account of the Dataset | [Dataset](Dataset.md) |
| [documentation](documentation.md) | * <br/> [Document](Document.md) | A page or document about this Dataset | [Dataset](Dataset.md) |
| [frequency](frequency.md) | 0..1 <br/> [Frequency](Frequency.md) | The frequency at which the Dataset is updated | [Dataset](Dataset.md) |
| [geographical_coverage](geographical_coverage.md) | * <br/> [Location](Location.md) | A geographic region that is covered by the Dataset | [Dataset](Dataset.md) |
| [has_version](has_version.md) | * <br/> [Dataset](Dataset.md) | A related Dataset that is a version, edition, or adaptation of the described ... | [Dataset](Dataset.md) |
| [identifier](identifier.md) | * <br/> [Uri](Uri.md) | The main identifier for the Dataset, e | [Dataset](Dataset.md) |
| [in_series](in_series.md) | * <br/> [DatasetSeries](DatasetSeries.md) | A dataset series of which the dataset is part | [Dataset](Dataset.md) |
| [is_referenced_by](is_referenced_by.md) | * <br/> [Resource](Resource.md) | A related resource, such as a publication, that references, cites, or otherwi... | [Dataset](Dataset.md) |
| [keyword](keyword.md) | * _recommended_ <br/> [String](String.md) | A keyword or tag describing the Dataset | [Dataset](Dataset.md) |
| [landing_page](landing_page.md) | * <br/> [Document](Document.md) | A web page that provides access to the Dataset, its Distributions and/or addi... | [Dataset](Dataset.md) |
| [language](language.md) | * <br/> [LinguisticSystem](LinguisticSystem.md) | A language of the Dataset | [Dataset](Dataset.md) |
| [modification_date](modification_date.md) | 0..1 <br/> [String](String.md) | The most recent date on which the Dataset was changed or modified | [Dataset](Dataset.md) |
| [other_identifier](other_identifier.md) | * <br/> [Identifier](Identifier.md) | A secondary identifier of the Dataset | [Dataset](Dataset.md) |
| [provenance](provenance.md) | * <br/> [ProvenanceStatement](ProvenanceStatement.md) | A statement about the lineage of a Dataset | [Dataset](Dataset.md) |
| [publisher](publisher.md) | 0..1 <br/> [Agent](Agent.md) | An entity (organisation) responsible for making the Dataset available | [Dataset](Dataset.md) |
| [qualified_attribution](qualified_attribution.md) | * <br/> [Attribution](Attribution.md) | An Agent having some form of responsibility for the resource | [Dataset](Dataset.md) |
| [qualified_relation](qualified_relation.md) | * <br/> [Relationship](Relationship.md) | A description of a relationship with another resource | [Dataset](Dataset.md) |
| [related_resource](related_resource.md) | * <br/> [Resource](Resource.md) | A related resource | [Dataset](Dataset.md) |
| [release_date](release_date.md) | 0..1 <br/> [String](String.md) | The date of formal issuance (e | [Dataset](Dataset.md) |
| [sample](sample.md) | * <br/> [Distribution](Distribution.md) | A sample distribution of the dataset | [Dataset](Dataset.md) |
| [source](source.md) | * <br/> [Dataset](Dataset.md) | A related Dataset from which the described Dataset is derived | [Dataset](Dataset.md) |
| [spatial_resolution](spatial_resolution.md) | 0..1 <br/> [Decimal](Decimal.md) | The minimum spatial separation resolvable in a dataset, measured in meters | [Dataset](Dataset.md) |
| [temporal_coverage](temporal_coverage.md) | * <br/> [PeriodOfTime](PeriodOfTime.md) | A temporal period that the Dataset covers | [Dataset](Dataset.md) |
| [temporal_resolution](temporal_resolution.md) | 0..1 <br/> [Duration](Duration.md) | The minimum time period resolvable in the dataset | [Dataset](Dataset.md) |
| [theme](theme.md) | * _recommended_ <br/> [Concept](Concept.md) | A category of the Dataset | [Dataset](Dataset.md) |
| [title](title.md) | 1..* <br/> [String](String.md) | A name given to the Dataset | [Dataset](Dataset.md) |
| [type](type.md) | * <br/> [Concept](Concept.md) | A type of the Dataset | [Dataset](Dataset.md) |
| [version](version.md) | 0..1 <br/> [String](String.md) | The version indicator (name or identifier) of a resource | [Dataset](Dataset.md) |
| [version_notes](version_notes.md) | * <br/> [String](String.md) | A description of the differences between this version and a previous version ... | [Dataset](Dataset.md) |
| [was_generated_by](was_generated_by.md) | 1..* <br/> [DataAnalysis](DataAnalysis.md) | An activity that generated, or provides the business context for, the creatio... | [Dataset](Dataset.md) |









## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:Dataset |
| native | nfdi4c:AnalysisDataset |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AnalysisDataset
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
is_a: ResearchDataset
slot_usage:
  was_generated_by:
    name: was_generated_by
    range: DataAnalysis
class_uri: dcat:Dataset

```
</details>

### Induced

<details>
```yaml
name: AnalysisDataset
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
is_a: ResearchDataset
slot_usage:
  was_generated_by:
    name: was_generated_by
    range: DataAnalysis
attributes:
  id:
    name: id
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:identifier
    identifier: true
    alias: id
    owner: AnalysisDataset
    domain_of:
    - DefinedTerm
    - ResearchDataset
    - ResearchCatalog
    - EvaluatedEntity
    - EvaluatedActivity
    range: uriorcurie
    required: true
  describes_entity:
    name: describes_entity
    description: A slot to provide the EvaluatedEntity that is described by a Dataset.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:relation
    alias: describes_entity
    owner: AnalysisDataset
    domain_of:
    - ResearchDataset
    range: EvaluatedEntity
    recommended: true
    multivalued: true
    inlined: true
    inlined_as_list: true
  describes_activity:
    name: describes_activity
    description: A slot to provide the EvaluatedActivity that is described by a Dataset.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:relation
    alias: describes_activity
    owner: AnalysisDataset
    domain_of:
    - ResearchDataset
    range: EvaluatedActivity
    recommended: true
    multivalued: true
    inlined: true
    inlined_as_list: true
  access_rights:
    name: access_rights
    description: Information that indicates whether the Dataset is publicly accessible,
      has access restrictions or is not public.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:accessRights
    alias: access_rights
    owner: AnalysisDataset
    domain_of:
    - DataService
    - Dataset
    range: RightsStatement
    required: false
    multivalued: false
    inlined_as_list: true
  applicable_legislation:
    name: applicable_legislation
    description: The legislation that mandates the creation or management of the Dataset.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcatap:applicableLegislation
    alias: applicable_legislation
    owner: AnalysisDataset
    domain_of:
    - Catalogue
    - DataService
    - Dataset
    - DatasetSeries
    - Distribution
    range: LegalResource
    required: false
    multivalued: true
    inlined_as_list: true
  conforms_to:
    name: conforms_to
    description: An implementing rule or other specification.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:conformsTo
    alias: conforms_to
    owner: AnalysisDataset
    domain_of:
    - DataService
    - Dataset
    range: Standard
    required: false
    multivalued: true
    inlined_as_list: true
  contact_point:
    name: contact_point
    description: Contact information that can be used for sending comments about the
      Dataset.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcat:contactPoint
    alias: contact_point
    owner: AnalysisDataset
    domain_of:
    - DataService
    - Dataset
    - DatasetSeries
    range: Kind
    required: false
    recommended: true
    multivalued: true
    inlined_as_list: true
  creator:
    name: creator
    description: An entity responsible for producing the dataset.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:creator
    alias: creator
    owner: AnalysisDataset
    domain_of:
    - Catalogue
    - Dataset
    range: Agent
    required: false
    multivalued: true
    inlined_as_list: true
  dataset_distribution:
    name: dataset_distribution
    description: An available Distribution for the Dataset.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcat:distribution
    alias: dataset_distribution
    owner: AnalysisDataset
    domain_of:
    - Dataset
    range: Distribution
    required: false
    multivalued: true
    inlined_as_list: true
  description:
    name: description
    description: A free-text account of the Dataset.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:description
    alias: description
    owner: AnalysisDataset
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
    required: true
    multivalued: true
    inlined_as_list: true
  documentation:
    name: documentation
    description: A page or document about this Dataset.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: foaf:page
    alias: documentation
    owner: AnalysisDataset
    domain_of:
    - DataService
    - Dataset
    - Distribution
    range: Document
    required: false
    multivalued: true
    inlined_as_list: true
  frequency:
    name: frequency
    description: The frequency at which the Dataset is updated.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:accrualPeriodicity
    alias: frequency
    owner: AnalysisDataset
    domain_of:
    - Dataset
    - DatasetSeries
    range: Frequency
    required: false
    multivalued: false
    inlined_as_list: false
  geographical_coverage:
    name: geographical_coverage
    description: A geographic region that is covered by the Dataset.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:spatial
    alias: geographical_coverage
    owner: AnalysisDataset
    domain_of:
    - Catalogue
    - Dataset
    - DatasetSeries
    range: Location
    required: false
    multivalued: true
    inlined_as_list: true
  has_version:
    name: has_version
    description: A related Dataset that is a version, edition, or adaptation of the
      described Dataset.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcat:hasVersion
    alias: has_version
    owner: AnalysisDataset
    domain_of:
    - Dataset
    range: Dataset
    required: false
    multivalued: true
    inlined_as_list: true
  identifier:
    name: identifier
    description: The main identifier for the Dataset, e.g. the URI or other unique
      identifier in the context of the Catalogue.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:identifier
    alias: identifier
    owner: AnalysisDataset
    domain_of:
    - Dataset
    range: uri
    required: false
    multivalued: true
    inlined_as_list: true
  in_series:
    name: in_series
    description: A dataset series of which the dataset is part.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcat:inSeries
    alias: in_series
    owner: AnalysisDataset
    domain_of:
    - Dataset
    range: DatasetSeries
    required: false
    multivalued: true
    inlined_as_list: true
  is_referenced_by:
    name: is_referenced_by
    description: A related resource, such as a publication, that references, cites,
      or otherwise points to the dataset.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:isReferencedBy
    alias: is_referenced_by
    owner: AnalysisDataset
    domain_of:
    - Dataset
    range: Resource
    required: false
    multivalued: true
    inlined_as_list: true
  keyword:
    name: keyword
    description: A keyword or tag describing the Dataset.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcat:keyword
    alias: keyword
    owner: AnalysisDataset
    domain_of:
    - DataService
    - Dataset
    range: string
    required: false
    recommended: true
    multivalued: true
    inlined_as_list: true
  landing_page:
    name: landing_page
    description: A web page that provides access to the Dataset, its Distributions
      and/or additional information.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcat:landingPage
    alias: landing_page
    owner: AnalysisDataset
    domain_of:
    - DataService
    - Dataset
    range: Document
    required: false
    multivalued: true
    inlined_as_list: true
  language:
    name: language
    description: A language of the Dataset.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:language
    alias: language
    owner: AnalysisDataset
    domain_of:
    - Catalogue
    - CatalogueRecord
    - Dataset
    - Distribution
    range: LinguisticSystem
    required: false
    multivalued: true
    inlined_as_list: true
  modification_date:
    name: modification_date
    description: The most recent date on which the Dataset was changed or modified.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:modified
    alias: modification_date
    owner: AnalysisDataset
    domain_of:
    - Catalogue
    - CatalogueRecord
    - Dataset
    - DatasetSeries
    - Distribution
    range: string
    required: false
    multivalued: false
    inlined_as_list: false
  other_identifier:
    name: other_identifier
    description: A secondary identifier of the Dataset
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: adms:identifier
    alias: other_identifier
    owner: AnalysisDataset
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
  provenance:
    name: provenance
    description: A statement about the lineage of a Dataset.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:provenance
    alias: provenance
    owner: AnalysisDataset
    domain_of:
    - Dataset
    range: ProvenanceStatement
    required: false
    multivalued: true
    inlined_as_list: true
  publisher:
    name: publisher
    description: An entity (organisation) responsible for making the Dataset available.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:publisher
    alias: publisher
    owner: AnalysisDataset
    domain_of:
    - Catalogue
    - DataService
    - Dataset
    - DatasetSeries
    range: Agent
    required: false
    multivalued: false
    inlined_as_list: true
  qualified_attribution:
    name: qualified_attribution
    description: An Agent having some form of responsibility for the resource.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: prov:qualifiedAttribution
    alias: qualified_attribution
    owner: AnalysisDataset
    domain_of:
    - Dataset
    range: Attribution
    required: false
    multivalued: true
    inlined_as_list: true
  qualified_relation:
    name: qualified_relation
    description: A description of a relationship with another resource.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcat:qualifiedRelation
    alias: qualified_relation
    owner: AnalysisDataset
    domain_of:
    - Dataset
    range: Relationship
    required: false
    multivalued: true
    inlined_as_list: true
  related_resource:
    name: related_resource
    description: A related resource.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:relation
    alias: related_resource
    owner: AnalysisDataset
    domain_of:
    - Dataset
    range: Resource
    required: false
    multivalued: true
    inlined_as_list: true
  release_date:
    name: release_date
    description: The date of formal issuance (e.g., publication) of the Dataset.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:issued
    alias: release_date
    owner: AnalysisDataset
    domain_of:
    - Catalogue
    - Dataset
    - DatasetSeries
    - Distribution
    range: string
    required: false
    multivalued: false
    inlined_as_list: false
  sample:
    name: sample
    description: A sample distribution of the dataset.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: adms:sample
    alias: sample
    owner: AnalysisDataset
    domain_of:
    - Dataset
    range: Distribution
    required: false
    multivalued: true
    inlined_as_list: true
  source:
    name: source
    description: A related Dataset from which the described Dataset is derived.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:source
    alias: source
    owner: AnalysisDataset
    domain_of:
    - Dataset
    range: Dataset
    required: false
    multivalued: true
    inlined_as_list: true
  spatial_resolution:
    name: spatial_resolution
    description: The minimum spatial separation resolvable in a dataset, measured
      in meters.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcat:spatialResolutionInMeters
    alias: spatial_resolution
    owner: AnalysisDataset
    domain_of:
    - Dataset
    - Distribution
    range: decimal
    required: false
    multivalued: false
    inlined_as_list: false
  temporal_coverage:
    name: temporal_coverage
    description: A temporal period that the Dataset covers.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:temporal
    alias: temporal_coverage
    owner: AnalysisDataset
    domain_of:
    - Catalogue
    - Dataset
    - DatasetSeries
    range: PeriodOfTime
    required: false
    multivalued: true
    inlined_as_list: true
  temporal_resolution:
    name: temporal_resolution
    description: The minimum time period resolvable in the dataset.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcat:temporalResolution
    alias: temporal_resolution
    owner: AnalysisDataset
    domain_of:
    - Dataset
    - Distribution
    range: duration
    required: false
    multivalued: false
    inlined_as_list: true
  theme:
    name: theme
    description: A category of the Dataset.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcat:theme
    alias: theme
    owner: AnalysisDataset
    domain_of:
    - DataService
    - Dataset
    range: Concept
    required: false
    recommended: true
    multivalued: true
    inlined_as_list: true
  title:
    name: title
    description: A name given to the Dataset.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:title
    alias: title
    owner: AnalysisDataset
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
    required: true
    multivalued: true
    inlined_as_list: true
  type:
    name: type
    description: A type of the Dataset.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:type
    alias: type
    owner: AnalysisDataset
    domain_of:
    - Agent
    - Dataset
    - LicenseDocument
    - ClassifierMixin
    range: Concept
    required: false
    multivalued: true
    inlined_as_list: true
  version:
    name: version
    description: The version indicator (name or identifier) of a resource.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcat:version
    alias: version
    owner: AnalysisDataset
    domain_of:
    - Dataset
    range: string
    required: false
    multivalued: false
    inlined_as_list: true
  version_notes:
    name: version_notes
    description: A description of the differences between this version and a previous
      version of the Dataset.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: adms:versionNotes
    alias: version_notes
    owner: AnalysisDataset
    domain_of:
    - Dataset
    range: string
    required: false
    multivalued: true
    inlined_as_list: true
  was_generated_by:
    name: was_generated_by
    description: An activity that generated, or provides the business context for,
      the creation of the dataset.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: prov:wasGeneratedBy
    alias: was_generated_by
    owner: AnalysisDataset
    domain_of:
    - Dataset
    - EvaluatedEntity
    range: DataAnalysis
    required: true
    multivalued: true
    inlined_as_list: true
class_uri: dcat:Dataset

```
</details>