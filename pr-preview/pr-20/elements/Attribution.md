

# Class: Attribution


_See [DCAT-AP specs:Attribution](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Attribution)_





URI: [prov:Attribution](http://www.w3.org/ns/prov#Attribution)






```mermaid
 classDiagram
    class Attribution
    click Attribution href "../Attribution"
      SupportiveEntity <|-- Attribution
        click SupportiveEntity href "../SupportiveEntity"
      
      
```





## Inheritance
* [SupportiveEntity](SupportiveEntity.md)
    * **Attribution**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [NMRAnalysisDataset](NMRAnalysisDataset.md) | [qualified_attribution](qualified_attribution.md) | range | [Attribution](Attribution.md) |
| [Dataset](Dataset.md) | [qualified_attribution](qualified_attribution.md) | range | [Attribution](Attribution.md) |
| [ResearchDataset](ResearchDataset.md) | [qualified_attribution](qualified_attribution.md) | range | [Attribution](Attribution.md) |
| [AnalysisDataset](AnalysisDataset.md) | [qualified_attribution](qualified_attribution.md) | range | [Attribution](Attribution.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | prov:Attribution |
| native | nfdi4c:Attribution |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Attribution
description: See [DCAT-AP specs:Attribution](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Attribution)
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
is_a: SupportiveEntity
abstract: false
class_uri: prov:Attribution

```
</details>

### Induced

<details>
```yaml
name: Attribution
description: See [DCAT-AP specs:Attribution](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Attribution)
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
is_a: SupportiveEntity
abstract: false
class_uri: prov:Attribution

```
</details>