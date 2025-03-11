

# Class: ProvenanceStatement


_See [DCAT-AP specs:ProvenanceStatement](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#ProvenanceStatement)_





URI: [dcterms:ProvenanceStatement](http://purl.org/dc/terms/ProvenanceStatement)






```mermaid
 classDiagram
    class ProvenanceStatement
    click ProvenanceStatement href "../ProvenanceStatement"
      SupportiveEntity <|-- ProvenanceStatement
        click SupportiveEntity href "../SupportiveEntity"
      
      
```





## Inheritance
* [SupportiveEntity](SupportiveEntity.md)
    * **ProvenanceStatement**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [NMRAnalysisDataset](NMRAnalysisDataset.md) | [provenance](provenance.md) | range | [ProvenanceStatement](ProvenanceStatement.md) |
| [Dataset](Dataset.md) | [provenance](provenance.md) | range | [ProvenanceStatement](ProvenanceStatement.md) |
| [ResearchDataset](ResearchDataset.md) | [provenance](provenance.md) | range | [ProvenanceStatement](ProvenanceStatement.md) |
| [AnalysisDataset](AnalysisDataset.md) | [provenance](provenance.md) | range | [ProvenanceStatement](ProvenanceStatement.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterms:ProvenanceStatement |
| native | nfdi4c:ProvenanceStatement |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProvenanceStatement
description: See [DCAT-AP specs:ProvenanceStatement](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#ProvenanceStatement)
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
is_a: SupportiveEntity
abstract: false
class_uri: dcterms:ProvenanceStatement

```
</details>

### Induced

<details>
```yaml
name: ProvenanceStatement
description: See [DCAT-AP specs:ProvenanceStatement](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#ProvenanceStatement)
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
is_a: SupportiveEntity
abstract: false
class_uri: dcterms:ProvenanceStatement

```
</details>