

# Class: Role


_See [DCAT-AP specs:Role](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Role)_





URI: [dcat:Role](http://www.w3.org/ns/dcat#Role)






```mermaid
 classDiagram
    class Role
    click Role href "../Role"
      SupportiveEntity <|-- Role
        click SupportiveEntity href "../SupportiveEntity"
      
      
```





## Inheritance
* [SupportiveEntity](SupportiveEntity.md)
    * **Role**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Relationship](Relationship.md) | [had_role](had_role.md) | range | [Role](Role.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcat:Role |
| native | nfdi4c:Role |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Role
description: See [DCAT-AP specs:Role](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Role)
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
is_a: SupportiveEntity
abstract: false
class_uri: dcat:Role

```
</details>

### Induced

<details>
```yaml
name: Role
description: See [DCAT-AP specs:Role](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Role)
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
is_a: SupportiveEntity
abstract: false
class_uri: dcat:Role

```
</details>