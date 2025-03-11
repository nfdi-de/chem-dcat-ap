

# Class: LinguisticSystem


_See [DCAT-AP specs:LinguisticSystem](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#LinguisticSystem)_





URI: [dcterms:LinguisticSystem](http://purl.org/dc/terms/LinguisticSystem)






```mermaid
 classDiagram
    class LinguisticSystem
    click LinguisticSystem href "../LinguisticSystem"
      SupportiveEntity <|-- LinguisticSystem
        click SupportiveEntity href "../SupportiveEntity"
      
      
```





## Inheritance
* [SupportiveEntity](SupportiveEntity.md)
    * **LinguisticSystem**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [NMRAnalysisDataset](NMRAnalysisDataset.md) | [language](language.md) | range | [LinguisticSystem](LinguisticSystem.md) |
| [Catalogue](Catalogue.md) | [language](language.md) | range | [LinguisticSystem](LinguisticSystem.md) |
| [CatalogueRecord](CatalogueRecord.md) | [language](language.md) | range | [LinguisticSystem](LinguisticSystem.md) |
| [Dataset](Dataset.md) | [language](language.md) | range | [LinguisticSystem](LinguisticSystem.md) |
| [Distribution](Distribution.md) | [language](language.md) | range | [LinguisticSystem](LinguisticSystem.md) |
| [ResearchDataset](ResearchDataset.md) | [language](language.md) | range | [LinguisticSystem](LinguisticSystem.md) |
| [AnalysisDataset](AnalysisDataset.md) | [language](language.md) | range | [LinguisticSystem](LinguisticSystem.md) |
| [ResearchCatalog](ResearchCatalog.md) | [language](language.md) | range | [LinguisticSystem](LinguisticSystem.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterms:LinguisticSystem |
| native | nfdi4c:LinguisticSystem |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: LinguisticSystem
description: See [DCAT-AP specs:LinguisticSystem](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#LinguisticSystem)
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
is_a: SupportiveEntity
abstract: false
class_uri: dcterms:LinguisticSystem

```
</details>

### Induced

<details>
```yaml
name: LinguisticSystem
description: See [DCAT-AP specs:LinguisticSystem](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#LinguisticSystem)
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
is_a: SupportiveEntity
abstract: false
class_uri: dcterms:LinguisticSystem

```
</details>