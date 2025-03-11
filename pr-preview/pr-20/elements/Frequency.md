

# Class: Frequency


_See [DCAT-AP specs:Frequency](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Frequency)_





URI: [dcterms:Frequency](http://purl.org/dc/terms/Frequency)






```mermaid
 classDiagram
    class Frequency
    click Frequency href "../Frequency"
      SupportiveEntity <|-- Frequency
        click SupportiveEntity href "../SupportiveEntity"
      
      
```





## Inheritance
* [SupportiveEntity](SupportiveEntity.md)
    * **Frequency**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [NMRAnalysisDataset](NMRAnalysisDataset.md) | [frequency](frequency.md) | range | [Frequency](Frequency.md) |
| [Dataset](Dataset.md) | [frequency](frequency.md) | range | [Frequency](Frequency.md) |
| [DatasetSeries](DatasetSeries.md) | [frequency](frequency.md) | range | [Frequency](Frequency.md) |
| [ResearchDataset](ResearchDataset.md) | [frequency](frequency.md) | range | [Frequency](Frequency.md) |
| [AnalysisDataset](AnalysisDataset.md) | [frequency](frequency.md) | range | [Frequency](Frequency.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterms:Frequency |
| native | nfdi4c:Frequency |







## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Frequency
description: See [DCAT-AP specs:Frequency](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Frequency)
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
is_a: SupportiveEntity
abstract: false
class_uri: dcterms:Frequency

```
</details>

### Induced

<details>
```yaml
name: Frequency
description: See [DCAT-AP specs:Frequency](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Frequency)
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
is_a: SupportiveEntity
abstract: false
class_uri: dcterms:Frequency

```
</details>