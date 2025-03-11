

# Class: Kind


_See [DCAT-AP specs:Kind](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Kind)_





URI: [vcard:Kind](http://www.w3.org/2006/vcard/ns#Kind)






```mermaid
 classDiagram
    class Kind
    click Kind href "../Kind"
      SupportiveEntity <|-- Kind
        click SupportiveEntity href "../SupportiveEntity"
      
      
```





## Inheritance
* [SupportiveEntity](SupportiveEntity.md)
    * **Kind**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [NMRAnalysisDataset](NMRAnalysisDataset.md) | [contact_point](contact_point.md) | range | [Kind](Kind.md) |
| [DataService](DataService.md) | [contact_point](contact_point.md) | range | [Kind](Kind.md) |
| [Dataset](Dataset.md) | [contact_point](contact_point.md) | range | [Kind](Kind.md) |
| [DatasetSeries](DatasetSeries.md) | [contact_point](contact_point.md) | range | [Kind](Kind.md) |
| [ResearchDataset](ResearchDataset.md) | [contact_point](contact_point.md) | range | [Kind](Kind.md) |
| [AnalysisDataset](AnalysisDataset.md) | [contact_point](contact_point.md) | range | [Kind](Kind.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vcard:Kind |
| native | nfdi4c:Kind |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Kind
description: See [DCAT-AP specs:Kind](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Kind)
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
is_a: SupportiveEntity
abstract: false
class_uri: vcard:Kind

```
</details>

### Induced

<details>
```yaml
name: Kind
description: See [DCAT-AP specs:Kind](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Kind)
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
is_a: SupportiveEntity
abstract: false
class_uri: vcard:Kind

```
</details>