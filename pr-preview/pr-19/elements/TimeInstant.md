

# Class: TimeInstant


_See [DCAT-AP specs:TimeInstant](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#TimeInstant)_





URI: [time:Instant](http://www.w3.org/2006/time#Instant)






```mermaid
 classDiagram
    class TimeInstant
    click TimeInstant href "../TimeInstant"
      SupportiveEntity <|-- TimeInstant
        click SupportiveEntity href "../SupportiveEntity"
      
      
```





## Inheritance
* [SupportiveEntity](SupportiveEntity.md)
    * **TimeInstant**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [PeriodOfTime](PeriodOfTime.md) | [beginning](beginning.md) | range | [TimeInstant](TimeInstant.md) |
| [PeriodOfTime](PeriodOfTime.md) | [end](end.md) | range | [TimeInstant](TimeInstant.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | time:Instant |
| native | nfdi4c:TimeInstant |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TimeInstant
description: See [DCAT-AP specs:TimeInstant](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#TimeInstant)
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
is_a: SupportiveEntity
abstract: false
class_uri: time:Instant

```
</details>

### Induced

<details>
```yaml
name: TimeInstant
description: See [DCAT-AP specs:TimeInstant](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#TimeInstant)
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
is_a: SupportiveEntity
abstract: false
class_uri: time:Instant

```
</details>