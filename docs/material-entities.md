# Material entities

The Material Entities AP module ([material_entities_ap.yaml](schema/material_entities_ap.yaml)) introduces classes for describing physical matter and its properties. It is the foundation on which chemical substances, molecular entities, atoms and reaction participants are built. 

!!! info "Cross-Domain Usage"
    This schema module can be used independently by other domain-specific DCAT-AP+ sub-profiles. Biologists describing specimen samples or material scientists describing non-chemical materials could import this module directly and thereby transitively DCAT-AP+ as well, without any chemistry-specific parts. 

## Design Pattern

![material_entities_light.svg](images/material_entities_light.svg#only-light)
![material_entities_dark.svg](images/material_entities_dark.svg#only-dark)

## MaterialEntity

`MaterialEntity` extends `Entity` and is mapped to `BFO:0000040` (_material entity_ in the Basic Formal Ontology). The mapping of the `has_part` slot it inherits from DCAT-AP+'s `Entity` class is changed to `BFO:0000051` and its range is tightened to `MaterialEntity` to allow a recursive description of its composition.

Use `MaterialEntity` when you need to describe a physical thing that participates in an `Activity` but is not itself an evaluated subject in a `DataGeneratingActivity`. In ChemDCAT-AP this class is used as a grouping for the chemical reaction participants: `StartingMaterial`, `Reagent`, and `ChemicalProduct` (see [Chemical Reactions](chemical-reactions.md)).

!!! warning "`has_part` ontology mapping deviation"
    Since `has_part` is mapped in `MaterialEntity` to BFO's _has part_ relation (`BFO:0000051`) via `slot_uri`, a SPARQL query that filters only on the DCAT-AP+ base predicate (`dcterms:has_part`) will **not** find these triples unless it is materialized in the knowledge graph via SPARQL CONSTRUCT rules. See [Ontology alignment: interoperability implications](ontology-alignment.md#interoperability-implications).

## MaterialSample

Mapped to `OBI:0000747` (_material sample_ in the Ontology for Biomedical Investigations), `MaterialSample` extends `EvaluatedEntity` and adds the `derived_from` slot (mapped to `prov:wasDerivedFrom`) to trace its provenance back to a source `Entity`.

Use `MaterialSample` when you need to describe a physical thing that was directly evaluated in a `DataGeneratingActivity`. Yet, since the DCAT-AP+ `evaluated_entity` slot on `DataGeneratingActivity` expects `EvaluatedEntity` instances, you would need to define a new `DataGeneratingActivity` subclass that constraints the range of this slot to `MaterialSample` to use it. In ChemDCAT-AP this class is used as the parent for a `SubstanceSample` (see [Chemical Entities](chemical-entities.md)).

!!! note "Why MaterialSample extends EvaluatedEntity, not MaterialEntity"
    In the DCAT-AP+ provenance core, `EvaluatedEntity` is the entity about which a `DataGeneratingActivity` produces information. A `MaterialSample` in an analytical workflow is exactly that: the thing being evaluated. Making `MaterialSample` extend `EvaluatedEntity` rather than `MaterialEntity` preserves this provenance semantics. The physical properties that both share are delivered via the `MaterialisticMixin` instead of through class inheritance.


## MaterialisticMixin & its physical attributes

`MaterialisticMixin` is an abstract LinkML mixin class whose sole purpose is to inject these physical property slots into any class that declares it:
 
| Slot                 | Range               | `class_uri` of range | Ontology Mapping |
|----------------------|---------------------|----------------------|------------------|
| `has_temperature`    | `Temperature`       | `qudt:Quantity`      | QUDT             |
| `has_mass`           | `Mass`              | `qudt:Quantity`      | QUDT             |
| `has_volume`         | `Volume`            | `qudt:Quantity`      | QUDT             |
| `has_density`        | `Density`           | `SIO:001406`         | SIO              |
| `has_pressure`       | `Pressure`          | `qudt:Quantity`      | QUDT             |
| `has_physical_state` | `PhysicalStateEnum` | --                   | PATO             |
 
 All slots are mapped to SIO:000008 (has attribute) via `slot_uri`. See [Ontology alignment](ontology-alignment.md#sio000008-as-the-chemistry-attribute-predicate) for why SIO is used here instead of the DCAT-AP+ default `dcterms:relation`. 

!!! warning "Sub-slot ontology mapping deviation"
    Since all slots of the `MaterialisticMixin` are mapped to `SIO:000008` (has attribute) via `slot_uri`, a SPARQL query that filters only on the DCAT-AP+ base predicate (`dcterms:relation`) will **not** find any triples unless it is materialized in the knowledge graph via SPARQL CONSTRUCT rules. See [Ontology alignment: interoperability implications](ontology-alignment.md#interoperability-implications).
 
Every quantity slot on this mixin is a sub-slot of the DCAT-AP+ `has_quantitative_attribute`. Hence, their range classes all extend `QuantitativeAttribute` to inherit the `value`, `has_quantity_type`, and `unit` structure from DCAT-AP+'s [QuantitativeAttribute pattern](https://nfdi-de.github.io/dcat-ap-plus/latest/design-patterns/#quantitativeattribute). Like their parent class, most of these range classes are mapped to `qudt:Quantity`. This is not ideal but pragmatically necessary, since OBO/BFO ontologies provide only classes for the *qualities* themselves (PATO terms like `PATO:0000146` for temperature), but not classes that represent the recorded quantified information about those qualities. `Density` is the exception: it is mapped to `SIO:001406`, which is an information content entity (ICE) about density, meaning it represents the *recorded value* of a material entity's density rather than the physical quality itself. This is exactly the kind of class that is needed but currently missing in the OBO ecosystem for the other quantities. See [Ontology alignment: why most quantity classes map to `qudt:Quantity`](ontology-alignment.md#why-most-quantity-classes-map-to-qudtquantity) for the full explanation.

!!! warning "Enum bindings for `has_quantity_type` and `unit` are still experimental"
    The schema declares bindings that constrain `has_quantity_type` and `unit` values to QUDT QuantityKind and Unit vocabularies respectively. These bindings are not enforced by `linkml-validate`. They will be validated using the [linkml-term-validator](https://linkml.io/linkml-term-validator/), which is meant to supports dynamic enums and binding validation. Yet, this still needs to be implemented in the ChemDCAT-AP pipeline.

The range of `has_physical_state` is modeled as a closed enum (`PhysicalStateEnum`) rather than a `QualitativeAttribute` to provide stricter validation. Only these four defined values are needed and thus accepted to describe the physical state of a material entity:

| Value     | Ontology Mapping (via LinkML's `meaning`) |
|-----------|-------------------------------------------|
| `SOLID`   | `PATO:0001736`                            |
| `PLASMA ` | `PATO:0015012ds<`                         |
| `LIQUID`  | `PATO:0001735`                            |
| `GASEOUS` | `PATO:0001737`                            |

Although `has_physical_state` should be considered a specialization of `has_quantitative_attribute`, it cannot be declared as such, because `has_quantitative_attribute` is set to `multivalued: true` and LinkML currently does not allow overriding this slot property to be false in sub-slots. The slot therefore stands alone, without a parent slot in the DCAT-AP+ attribute hierarchy. This is tracked as a schema TODO; if LinkML lifts this restriction, `has_physical_state` will be made a proper sub-slot of `has_qualitative_attribute`.

## Example instance of a wood sample

From the test dataset:

```yaml
id: https://www.example.com/wood3000
title: "Philip's wood sample"
rdf_type:
  id: ENVO:00002040
  title: "wood"
has_physical_state: SOLID
has_temperature:
  - title: "Temperature"
    has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
    unit: https://qudt.org/vocab/unit/DEG_C
    value: 20.0
has_mass:
  - title: "Mass in mg"
    has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
    unit: https://qudt.org/vocab/unit/MilliGM
    value: 300.0
has_volume:
  - title: "Volume in L"
    has_quantity_type: http://qudt.org/vocab/quantitykind/Volume
    unit: https://qudt.org/vocab/unit/L
    value: 0.03
has_pressure:
  - title: "Pressure in Bar"
    has_quantity_type: http://qudt.org/vocab/quantitykind/Pressure
    unit: https://qudt.org/vocab/unit/BAR
    value: 2.0
    description: "This is just a test value for this attribute"
derived_from:
  id: https://www.wikidata.org/wiki/Q4204
  title: "black forest germany"
  rdf_type:
    id: ENVO:01000174
    title: forest biome
```

Key observations:

- `rdf_type` uses the DCAT-AP+ [ClassifierMixin](https://nfdi-de.github.io/dcat-ap-plus/design-patterns/#pattern-3-flexible-classification-classifiermixin) to classify the sample as `ENVO:00002040` (wood).
- Each physical property follows the DCAT-AP+ `QuantitativeAttribute` pattern: `value` + `has_quantity_type` (QUDT QuantityKind) + `unit` (QUDT Unit).
- `derived_from` traces the sample back to a geographic origin, itself classified via `rdf_type` as a forest biome (`ENVO:01000174`).
