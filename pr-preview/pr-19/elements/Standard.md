

# Class: Standard


_See [DCAT-AP specs:Standard](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Standard)_





URI: [dcterms:Standard](http://purl.org/dc/terms/Standard)






```mermaid
 classDiagram
    class Standard
    click Standard href "../Standard"
      SupportiveEntity <|-- Standard
        click SupportiveEntity href "../SupportiveEntity"
      
      
```





## Inheritance
* [SupportiveEntity](SupportiveEntity.md)
    * **Standard**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [NMRAnalysisDataset](NMRAnalysisDataset.md) | [conforms_to](conforms_to.md) | range | [Standard](Standard.md) |
| [CatalogueRecord](CatalogueRecord.md) | [application_profile](application_profile.md) | range | [Standard](Standard.md) |
| [DataService](DataService.md) | [conforms_to](conforms_to.md) | range | [Standard](Standard.md) |
| [Dataset](Dataset.md) | [conforms_to](conforms_to.md) | range | [Standard](Standard.md) |
| [Distribution](Distribution.md) | [linked_schemas](linked_schemas.md) | range | [Standard](Standard.md) |
| [ResearchDataset](ResearchDataset.md) | [conforms_to](conforms_to.md) | range | [Standard](Standard.md) |
| [AnalysisDataset](AnalysisDataset.md) | [conforms_to](conforms_to.md) | range | [Standard](Standard.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterms:Standard |
| native | nfdi4c:Standard |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Standard
description: See [DCAT-AP specs:Standard](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Standard)
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
is_a: SupportiveEntity
abstract: false
class_uri: dcterms:Standard

```
</details>

### Induced

<details>
```yaml
name: Standard
description: See [DCAT-AP specs:Standard](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Standard)
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
is_a: SupportiveEntity
abstract: false
class_uri: dcterms:Standard

```
</details>