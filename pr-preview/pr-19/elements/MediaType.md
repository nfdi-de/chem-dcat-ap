

# Class: MediaType


_See [DCAT-AP specs:MediaType](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#MediaType)_





URI: [dcterms:MediaType](http://purl.org/dc/terms/MediaType)






```mermaid
 classDiagram
    class MediaType
    click MediaType href "../MediaType"
      SupportiveEntity <|-- MediaType
        click SupportiveEntity href "../SupportiveEntity"
      
      
```





## Inheritance
* [SupportiveEntity](SupportiveEntity.md)
    * **MediaType**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Distribution](Distribution.md) | [compression_format](compression_format.md) | range | [MediaType](MediaType.md) |
| [Distribution](Distribution.md) | [media_type](media_type.md) | range | [MediaType](MediaType.md) |
| [Distribution](Distribution.md) | [packaging_format](packaging_format.md) | range | [MediaType](MediaType.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterms:MediaType |
| native | nfdi4c:MediaType |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MediaType
description: See [DCAT-AP specs:MediaType](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#MediaType)
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
is_a: SupportiveEntity
abstract: false
class_uri: dcterms:MediaType

```
</details>

### Induced

<details>
```yaml
name: MediaType
description: See [DCAT-AP specs:MediaType](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#MediaType)
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
is_a: SupportiveEntity
abstract: false
class_uri: dcterms:MediaType

```
</details>