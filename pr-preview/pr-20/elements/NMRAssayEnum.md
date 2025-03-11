# Enum: NMRAssayEnum




_NMR types from the Chemical Methods Ontology_



URI: [NMRAssayEnum](NMRAssayEnum.md)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| CHMO:0000595 | CHMO:0000595 | Spectroscopy where the energy states of 13C nuclei placed in a static magneti... |









## Identifier and Mapping Information







### Schema Source


* from schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap






## LinkML Source

<details>
```yaml
name: NMRAssayEnum
description: NMR types from the Chemical Methods Ontology
from_schema: https://stroemphi.github.io/dcat-4C-ap/dcat_4c_ap
rank: 1000
permissible_values:
  CHMO:0000595:
    text: CHMO:0000595
    description: Spectroscopy where the energy states of 13C nuclei placed in a static
      magnetic field are interrogated by inducing transitions between the states via
      radio frequency irradiation. Each experiment consists of a sequence of radio
      frequency pulses with delay periods in between them.
    meaning: CHMO:0000595
    title: 13C nuclear magnetic resonance spectroscopy
reachable_from:
  source_ontology: bioregistry:chmo
  source_nodes:
  - CHMO:0000613
  relationship_types:
  - rdfs:subClassOf
  is_direct: false

```
</details>
