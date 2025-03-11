

# Class: Document


_See [DCAT-AP specs:Document](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Document)_





URI: [foaf:Document](http://xmlns.com/foaf/0.1/Document)






```mermaid
 classDiagram
    class Document
    click Document href "../Document"
      SupportiveEntity <|-- Document
        click SupportiveEntity href "../SupportiveEntity"
      
      
```





## Inheritance
* [SupportiveEntity](SupportiveEntity.md)
    * **Document**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [NMRAnalysisDataset](NMRAnalysisDataset.md) | [documentation](documentation.md) | range | [Document](Document.md) |
| [NMRAnalysisDataset](NMRAnalysisDataset.md) | [landing_page](landing_page.md) | range | [Document](Document.md) |
| [Catalogue](Catalogue.md) | [homepage](homepage.md) | range | [Document](Document.md) |
| [DataService](DataService.md) | [documentation](documentation.md) | range | [Document](Document.md) |
| [DataService](DataService.md) | [landing_page](landing_page.md) | range | [Document](Document.md) |
| [Dataset](Dataset.md) | [documentation](documentation.md) | range | [Document](Document.md) |
| [Dataset](Dataset.md) | [landing_page](landing_page.md) | range | [Document](Document.md) |
| [Distribution](Distribution.md) | [documentation](documentation.md) | range | [Document](Document.md) |
| [ResearchDataset](ResearchDataset.md) | [documentation](documentation.md) | range | [Document](Document.md) |
| [ResearchDataset](ResearchDataset.md) | [landing_page](landing_page.md) | range | [Document](Document.md) |
| [AnalysisDataset](AnalysisDataset.md) | [documentation](documentation.md) | range | [Document](Document.md) |
| [AnalysisDataset](AnalysisDataset.md) | [landing_page](landing_page.md) | range | [Document](Document.md) |
| [ResearchCatalog](ResearchCatalog.md) | [homepage](homepage.md) | range | [Document](Document.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | foaf:Document |
| native | nfdi4c:Document |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Document
description: See [DCAT-AP specs:Document](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Document)
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
is_a: SupportiveEntity
abstract: false
class_uri: foaf:Document

```
</details>

### Induced

<details>
```yaml
name: Document
description: See [DCAT-AP specs:Document](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Document)
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
is_a: SupportiveEntity
abstract: false
class_uri: foaf:Document

```
</details>