

# Class: RightsStatement


_See [DCAT-AP specs:RightsStatement](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#RightsStatement)_





URI: [dcterms:RightsStatement](http://purl.org/dc/terms/RightsStatement)






```mermaid
 classDiagram
    class RightsStatement
    click RightsStatement href "../RightsStatement"
      SupportiveEntity <|-- RightsStatement
        click SupportiveEntity href "../SupportiveEntity"
      
      
```





## Inheritance
* [SupportiveEntity](SupportiveEntity.md)
    * **RightsStatement**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [NMRAnalysisDataset](NMRAnalysisDataset.md) | [access_rights](access_rights.md) | range | [RightsStatement](RightsStatement.md) |
| [Catalogue](Catalogue.md) | [rights](rights.md) | range | [RightsStatement](RightsStatement.md) |
| [DataService](DataService.md) | [access_rights](access_rights.md) | range | [RightsStatement](RightsStatement.md) |
| [Dataset](Dataset.md) | [access_rights](access_rights.md) | range | [RightsStatement](RightsStatement.md) |
| [Distribution](Distribution.md) | [rights](rights.md) | range | [RightsStatement](RightsStatement.md) |
| [ResearchDataset](ResearchDataset.md) | [access_rights](access_rights.md) | range | [RightsStatement](RightsStatement.md) |
| [AnalysisDataset](AnalysisDataset.md) | [access_rights](access_rights.md) | range | [RightsStatement](RightsStatement.md) |
| [ResearchCatalog](ResearchCatalog.md) | [rights](rights.md) | range | [RightsStatement](RightsStatement.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterms:RightsStatement |
| native | nfdi4c:RightsStatement |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RightsStatement
description: See [DCAT-AP specs:RightsStatement](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#RightsStatement)
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
is_a: SupportiveEntity
abstract: false
class_uri: dcterms:RightsStatement

```
</details>

### Induced

<details>
```yaml
name: RightsStatement
description: See [DCAT-AP specs:RightsStatement](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#RightsStatement)
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
is_a: SupportiveEntity
abstract: false
class_uri: dcterms:RightsStatement

```
</details>