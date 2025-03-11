

# Class: NMRAnalysisDataset


_A dataset that is the result of a NMRSpectralAnalysis of a ChemicalSample._





URI: [dcat:Dataset](http://www.w3.org/ns/dcat#Dataset)






```mermaid
 classDiagram
    class NMRAnalysisDataset
    click NMRAnalysisDataset href "../NMRAnalysisDataset"
      AnalysisDataset <|-- NMRAnalysisDataset
        click AnalysisDataset href "../AnalysisDataset"
      
      NMRAnalysisDataset : access_rights
        
          
    
    
    NMRAnalysisDataset --> "0..1" RightsStatement : access_rights
    click RightsStatement href "../RightsStatement"

        
      NMRAnalysisDataset : applicable_legislation
        
          
    
    
    NMRAnalysisDataset --> "*" LegalResource : applicable_legislation
    click LegalResource href "../LegalResource"

        
      NMRAnalysisDataset : conforms_to
        
          
    
    
    NMRAnalysisDataset --> "*" Standard : conforms_to
    click Standard href "../Standard"

        
      NMRAnalysisDataset : contact_point
        
          
    
    
    NMRAnalysisDataset --> "* _recommended_" Kind : contact_point
    click Kind href "../Kind"

        
      NMRAnalysisDataset : creator
        
          
    
    
    NMRAnalysisDataset --> "*" Agent : creator
    click Agent href "../Agent"

        
      NMRAnalysisDataset : dataset_distribution
        
          
    
    
    NMRAnalysisDataset --> "*" Distribution : dataset_distribution
    click Distribution href "../Distribution"

        
      NMRAnalysisDataset : describes_activity
        
          
    
    
    NMRAnalysisDataset --> "* _recommended_" EvaluatedActivity : describes_activity
    click EvaluatedActivity href "../EvaluatedActivity"

        
      NMRAnalysisDataset : describes_entity
        
          
    
    
    NMRAnalysisDataset --> "* _recommended_" ChemicalSample : describes_entity
    click ChemicalSample href "../ChemicalSample"

        
      NMRAnalysisDataset : description
        
      NMRAnalysisDataset : documentation
        
          
    
    
    NMRAnalysisDataset --> "*" Document : documentation
    click Document href "../Document"

        
      NMRAnalysisDataset : frequency
        
          
    
    
    NMRAnalysisDataset --> "0..1" Frequency : frequency
    click Frequency href "../Frequency"

        
      NMRAnalysisDataset : geographical_coverage
        
          
    
    
    NMRAnalysisDataset --> "*" Location : geographical_coverage
    click Location href "../Location"

        
      NMRAnalysisDataset : has_version
        
          
    
    
    NMRAnalysisDataset --> "*" Dataset : has_version
    click Dataset href "../Dataset"

        
      NMRAnalysisDataset : id
        
      NMRAnalysisDataset : identifier
        
      NMRAnalysisDataset : in_series
        
          
    
    
    NMRAnalysisDataset --> "*" DatasetSeries : in_series
    click DatasetSeries href "../DatasetSeries"

        
      NMRAnalysisDataset : is_referenced_by
        
          
    
    
    NMRAnalysisDataset --> "*" Resource : is_referenced_by
    click Resource href "../Resource"

        
      NMRAnalysisDataset : keyword
        
      NMRAnalysisDataset : landing_page
        
          
    
    
    NMRAnalysisDataset --> "*" Document : landing_page
    click Document href "../Document"

        
      NMRAnalysisDataset : language
        
          
    
    
    NMRAnalysisDataset --> "*" LinguisticSystem : language
    click LinguisticSystem href "../LinguisticSystem"

        
      NMRAnalysisDataset : modification_date
        
      NMRAnalysisDataset : other_identifier
        
          
    
    
    NMRAnalysisDataset --> "*" Identifier : other_identifier
    click Identifier href "../Identifier"

        
      NMRAnalysisDataset : provenance
        
          
    
    
    NMRAnalysisDataset --> "*" ProvenanceStatement : provenance
    click ProvenanceStatement href "../ProvenanceStatement"

        
      NMRAnalysisDataset : publisher
        
          
    
    
    NMRAnalysisDataset --> "0..1" Agent : publisher
    click Agent href "../Agent"

        
      NMRAnalysisDataset : qualified_attribution
        
          
    
    
    NMRAnalysisDataset --> "*" Attribution : qualified_attribution
    click Attribution href "../Attribution"

        
      NMRAnalysisDataset : qualified_relation
        
          
    
    
    NMRAnalysisDataset --> "*" Relationship : qualified_relation
    click Relationship href "../Relationship"

        
      NMRAnalysisDataset : related_resource
        
          
    
    
    NMRAnalysisDataset --> "*" Resource : related_resource
    click Resource href "../Resource"

        
      NMRAnalysisDataset : release_date
        
      NMRAnalysisDataset : sample
        
          
    
    
    NMRAnalysisDataset --> "*" Distribution : sample
    click Distribution href "../Distribution"

        
      NMRAnalysisDataset : source
        
          
    
    
    NMRAnalysisDataset --> "*" Dataset : source
    click Dataset href "../Dataset"

        
      NMRAnalysisDataset : spatial_resolution
        
      NMRAnalysisDataset : temporal_coverage
        
          
    
    
    NMRAnalysisDataset --> "*" PeriodOfTime : temporal_coverage
    click PeriodOfTime href "../PeriodOfTime"

        
      NMRAnalysisDataset : temporal_resolution
        
      NMRAnalysisDataset : theme
        
          
    
    
    NMRAnalysisDataset --> "* _recommended_" Concept : theme
    click Concept href "../Concept"

        
      NMRAnalysisDataset : title
        
      NMRAnalysisDataset : type
        
          
    
    
    NMRAnalysisDataset --> "*" Concept : type
    click Concept href "../Concept"

        
      NMRAnalysisDataset : version
        
      NMRAnalysisDataset : version_notes
        
      NMRAnalysisDataset : was_generated_by
        
          
    
    
    NMRAnalysisDataset --> "1..*" NMRSpectralAnalysis : was_generated_by
    click NMRSpectralAnalysis href "../NMRSpectralAnalysis"

        
      
```





## Inheritance
* [Dataset](Dataset.md)
    * [ResearchDataset](ResearchDataset.md)
        * [AnalysisDataset](AnalysisDataset.md)
            * **NMRAnalysisDataset**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) |  | [ResearchDataset](ResearchDataset.md) |
| [describes_entity](describes_entity.md) | * _recommended_ <br/> [ChemicalSample](ChemicalSample.md) | A slot to provide the EvaluatedEntity that is described by a Dataset | [ResearchDataset](ResearchDataset.md) |
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
| [was_generated_by](was_generated_by.md) | 1..* <br/> [NMRSpectralAnalysis](NMRSpectralAnalysis.md) | An activity that generated, or provides the business context for, the creatio... | [Dataset](Dataset.md) |









## Comments

* This class serves as an example for the way in which we want to build domain specific schema profiles. It will be outsourced to a more appropriate location in the future.

## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:Dataset |
| native | nfdi4c:NMRAnalysisDataset |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NMRAnalysisDataset
description: A dataset that is the result of a NMRSpectralAnalysis of a ChemicalSample.
comments:
- This class serves as an example for the way in which we want to build domain specific
  schema profiles. It will be outsourced to a more appropriate location in the future.
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
is_a: AnalysisDataset
slot_usage:
  was_generated_by:
    name: was_generated_by
    range: NMRSpectralAnalysis
    multivalued: true
    inlined_as_list: true
  describes_entity:
    name: describes_entity
    range: ChemicalSample
class_uri: dcat:Dataset

```
</details>

### Induced

<details>
```yaml
name: NMRAnalysisDataset
description: A dataset that is the result of a NMRSpectralAnalysis of a ChemicalSample.
comments:
- This class serves as an example for the way in which we want to build domain specific
  schema profiles. It will be outsourced to a more appropriate location in the future.
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
is_a: AnalysisDataset
slot_usage:
  was_generated_by:
    name: was_generated_by
    range: NMRSpectralAnalysis
    multivalued: true
    inlined_as_list: true
  describes_entity:
    name: describes_entity
    range: ChemicalSample
attributes:
  id:
    name: id
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:identifier
    identifier: true
    alias: id
    owner: NMRAnalysisDataset
    domain_of:
    - DefinedTerm
    - ResearchDataset
    - ResearchCatalog
    - EvaluatedEntity
    - EvaluatedActivity
    range: uriorcurie
  describes_entity:
    name: describes_entity
    description: A slot to provide the EvaluatedEntity that is described by a Dataset.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:relation
    alias: describes_entity
    owner: NMRAnalysisDataset
    domain_of:
    - ResearchDataset
    range: ChemicalSample
    recommended: true
    multivalued: true
    inlined_as_list: true
  describes_activity:
    name: describes_activity
    description: A slot to provide the EvaluatedActivity that is described by a Dataset.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:relation
    alias: describes_activity
    owner: NMRAnalysisDataset
    domain_of:
    - ResearchDataset
    range: EvaluatedActivity
    recommended: true
    multivalued: true
    inlined_as_list: true
  access_rights:
    name: access_rights
    description: Information that indicates whether the Dataset is publicly accessible,
      has access restrictions or is not public.
    from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
    rank: 1000
    slot_uri: dcterms:accessRights
    alias: access_rights
    owner: NMRAnalysisDataset
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
    owner: NMRAnalysisDataset
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
    owner: NMRAnalysisDataset
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
    owner: NMRAnalysisDataset
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
    owner: NMRAnalysisDataset
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
    owner: NMRAnalysisDataset
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
    owner: NMRAnalysisDataset
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
    owner: NMRAnalysisDataset
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
    owner: NMRAnalysisDataset
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
    owner: NMRAnalysisDataset
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
    owner: NMRAnalysisDataset
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
    owner: NMRAnalysisDataset
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
    owner: NMRAnalysisDataset
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
    owner: NMRAnalysisDataset
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
    owner: NMRAnalysisDataset
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
    owner: NMRAnalysisDataset
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
    owner: NMRAnalysisDataset
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
    owner: NMRAnalysisDataset
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
    owner: NMRAnalysisDataset
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
    owner: NMRAnalysisDataset
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
    owner: NMRAnalysisDataset
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
    owner: NMRAnalysisDataset
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
    owner: NMRAnalysisDataset
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
    owner: NMRAnalysisDataset
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
    owner: NMRAnalysisDataset
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
    owner: NMRAnalysisDataset
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
    owner: NMRAnalysisDataset
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
    owner: NMRAnalysisDataset
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
    owner: NMRAnalysisDataset
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
    owner: NMRAnalysisDataset
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
    owner: NMRAnalysisDataset
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
    owner: NMRAnalysisDataset
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
    owner: NMRAnalysisDataset
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
    owner: NMRAnalysisDataset
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
    owner: NMRAnalysisDataset
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
    owner: NMRAnalysisDataset
    domain_of:
    - Dataset
    - EvaluatedEntity
    range: NMRSpectralAnalysis
    required: true
    multivalued: true
    inlined_as_list: true
class_uri: dcat:Dataset

```
</details>