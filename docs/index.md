# ChemDCAT-AP: A DCAT-AP+ based Application Profile for Chemistry and Catalysis

ChemDCAT-AP is an application profile that extends [DCAT-AP+](https://nfdi-de.github.io/dcat-ap-plus/) for **chemistry and catalysis research data**. Like DCAT-AP+, it is written in [LinkML](https://linkml.io/) ([Moxon et al. 2025](https://doi.org/10.1093/gigascience/giaf152)) and developed jointly by [NFDI4Chem](https://nfdi4chem.de) and [NFDI4Cat](https://nfdi4cat.org/). As the first domain-specific extension of DCAT-AP+, ChemDCAT-AP serves as the **reference implementation** that demonstrates how the domain-agnostic provenance core of DCAT-AP+ can be specialized for a certain scientific domain while preserving full interoperability with the European data standard [DCAT-AP](https://semiceu.github.io/DCAT-AP/releases/3.0.0/).

As in DCAT-AP+, the schema itself — [**chem_dcat_ap.yaml**](schema/chem_dcat_ap.yaml) — is **the single source of truth** from which SHACL shapes, JSON/-LD Schema and Context, Python/Pydantic data classes, and an HTML schema reference documentation are generated, which means all are guaranteed to be coherent.

## What ChemDCAT-AP adds

DCAT-AP+ provides the [generic building blocks](https://nfdi-de.github.io/dcat-ap-plus/latest/design-patterns/) that allow a detailed, machine-readable description of *how* a dataset was created and *what it is about*. Yet, it requires explicitly typing the instance data with the correct domain ontology or vocabulary terms.

ChemDCAT-AP eliminates this potential hurdle by baking domain knowledge directly into the schema. Every ChemDCAT-AP class extends a DCAT-AP+ class via `is_a`. Every slot inherits from a DCAT-AP+ slot the same way. All schema elements are mapped to established, relevant ontologies, such as the [Chemical Entities of Biological Interest (ChEBI)](http://www.ebi.ac.uk/chebi) ontology, the [Chemical Information Ontology (CHEMINF)](https://terminology.nfdi4chem.de/ts/ontologies/cheminf?lang=en), the [Semanticscience Integrated Ontology (SIO)](https://github.com/MaastrichtU-IDS/semanticscience), or the [Named Reaction Ontology (RXNO)](https://terminology.nfdi4chem.de/ts/ontologies/rxno). The [extension rules](https://nfdi-de.github.io/dcat-ap-plus/latest/how-to-extend/) of DCAT-AP+ are followed throughout. 

Consequently, instance data gets automatically typed correctly, removing the need for external lookups. The result is a cognitively lighter modeling experience that yields less verbose instance data, stricter validation, and semantically more precise RDF output. 

| DCAT-AP+ base                             | ChemDCAT-AP specialization                                                                    | What it enables                                                                                                                                                                            |
|-------------------------------------------|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Dataset`                                 | <code>Substance<wbr>Sample<wbr>Characterization<wbr>Dataset</code>, <code>ReactionMonitoringDataset</code>                         | Constraining a dataset to be about a SubstanceSample respectively a ChemicalReaction in a very general way (ChemDCAT-AP sub profiles are expected to define their own more specific ones)  |
| <code>DataGenerating<wbr>Activity</code>                  | <code>Substance<wbr>Sample<wbr>Characterization</code>, <code>Reaction<wbr>Monitoring</code>                                       | Describing the activities that generate chemistry and catalysis datasets in a very general way (ChemDCAT-AP sub profiles are expected to define their own more specific ones)              |
| `Entity`                                  | <code>Material<wbr>Entity</code>, <code>Chemical<wbr>Entity</code>, <code>Atom</code>, <code>Chemical<wbr>Product</code>, <code>Reagent</code>, <code>Starting<wbr>Material</code>  | Describing chemical substances by composition and role, with identifiers and physical properties                                                                                           |
| `EvaluatedEntity`                         | <code>Material<wbr>Sample</code>, <code>Substance<wbr>Sample</code>, <code>PolymerSample</code>                                          | Describing what kind of chemical substance or material was evaluated                                                                                                                       |
| `EvaluatedActivity`                       | <code>Chemical<wbr>Reaction</code>                                                                            | Describing what kind of chemical reaction was evaluated including its inputs, outputs, agents and conditions                                                                               |
| `AgenticEntity`                           | <code>Catalyst</code>, <code>Dissolving<wbr>Substance</code>, <code>Reactor</code>                                                  | Describing what influenced or enabled a chemical reaction without being consumed                                                                                                           |
| `has_qualitative_attribute`               | <code>inchi</code>, <code>inchikey</code>, <code>smiles</code>, <code>molecular_formula</code>, <code>iupac_name</code>,                             | Providing common chemical identifiers via dedicated slots                                                                                                                                  |
| `has_quantitative_attribute`              | <code>has_temperature</code>, <code>has_mass</code>, <code>has_concentration</code>, <code>has_yield</code>, ...                          | Providing common physical and chemical quantities via dedicated slots                                                                                                                      |


### Example: A chemical substance sample in ChemDCAT-AP

```yaml
# A SubstanceSample
id: doi:10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N.2
title: "CRS-50440"
composed_of:
  - id: doi:10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N.2#EvaluatedCompound
    inchikey:
      - value: "UGRXAOUDHZOHPF-UHFFFAOYSA-N"
        title: "assigned InChIKey"
    smiles:
      - value: "CNCc1csc(n1)c1ccccc1"
        title: "assigned SMILES"
    molecular_formula:
      - value: "C11H12N2S"
        title: "assigned formula"
    iupac_name:
      - value: "N-methyl-1-(2-phenyl-1,3-thiazol-4-yl)methanamine"
        title: "assigned IUPAC name"
    has_molar_mass:
      - has_quantity_type: http://qudt.org/vocab/quantitykind/MolarMass
        unit: https://qudt.org/vocab/unit/GM-PER-MOL
        value: 204.072119
        title: "calculated molar mass"
```

This is valid ChemDCAT-AP instance data (see [A substance sample characterization dataset](quickstart.md#a-substance-characterization-dataset) for a full `dcat:Dataset` example). It can be validated and converted to RDF using the LinkML tooling. 

## Architecture

ChemDCAT-AP is organized as four LinkML schema modules that import each other:

![arcitecture_light.svg](images/arcitecture_light.svg#only-light)
![arcitecture_dark.svg](images/arcitecture_dark.svg#only-dark)

Each module has a distinct responsibility:

* **Material Entities AP** — handles physical matter and its properties. 
* **Chemical Entities AP** — adds chemical entities and substances, their structures and properties.
* **Chemical Reaction AP** — models all things needed for describing chemical reactions.
* **ChemDCAT-AP** — ties these schemas together and adds exemplary DCAT-AP+ specializations for `Dataset` and `DataGeneratingActivity` constrained to be about/evaluating chemical substances and reactions.

This layered approach ensures that each profile can be used independently and all profiles align with the DCAT-AP+ core patterns.


## Documentation

- [**Material entities**](material-entities.md) — MaterialEntity, MaterialSample, and the MaterialisticMixin
- [**Chemical entities**](chemical-entities.md) — ChemicalEntity, SubstanceSample and the ChemicalSubstanceMixin
- [**Chemical reactions**](chemical-reactions.md) — ChemicalReaction, its participants and conditions
- [**Chemical datasets**](dataset-activity-shapes.md) — Convenience shapes for chemical substance and reaction datasets
- [**Ontology alignment**](ontology-alignment.md) — Ontology mapping choices and `slot_uri` replacement strategy
- [**Adoption guide**](guidance.md) — Practical do/don't rules, decision tables, dual-role of substances explanation, extension checklist
- [**Quick start for developers**](quickstart.md) — Installation, tooling, complete Dataset examples, serialization types 
- [**Schema Reference Documentation**](elements/overview.md) — Auto-generated schema reference documentation
- [**Versioning**](versioning.md) — Versioning rationale
- [**About**](about.md) — Origin, publication, funding

For DCAT-AP+ concepts (provenance core, QuantitativeAttribute/QualitativeAttribute, ClassifierMixin), see the [DCAT-AP+ documentation](https://nfdi-de.github.io/dcat-ap-plus/).

## Planned extensions

Several schema elements are currently stubs intended for future specialization:

**PolymerSample** (`chemical_entites_ap.yaml`): Extends `SubstanceSample` with `PolymerMixin`. The mixin currently has no additional slots. Future versions will add polymer-specific properties (degree of polymerization, molecular weight distribution, branching, etc.) following the same pattern as `ChemicalSubstanceMixin`. Note: `PolymerSample` currently shares `class_uri: SIO:001378` with its parent `SubstanceSample`; a more specific mapping is planned.

**Laboratory** (`chem_dcat_ap.yaml`): Extends `Surrounding` (from DCAT-AP+), mapped to `ENVO:01001405`. Currently has no additional slots beyond those inherited from `Surrounding`. It is intended as an extension point where downstream profiles that import ChemDCAT-AP can plug in their own sub-shapes for laboratory-specific metadata.

**Device** (DCAT-AP+ scope): The `Device` class from DCAT-AP+ is planned to be extended with a dedicated device profile aligned with the [PIDInst schema](https://github.com/rdawg-pidinst/schema) of the RDA Persistent Identification of Instruments Working Group. This is outside ChemDCAT-AP's scope and would be a separate DCAT-AP+ extension that plugs into the existing `Device` class.

**Plan** (DCAT-AP+ scope, with ChemDCAT-AP extensions): The DCAT-AP+ `Plan` class (mapped to `prov:Plan`) is planned to be extended to allow structured description of procedures, methods, and experimental executions. The goal is compatibility with the OBO Foundry `planned process` pattern, which uses `IAO:0000104` (plan specification) for its definition. `IAO:0000104` is planned to be used either as an additional ontology mapping on `Plan` or as the `class_uri` of a dedicated subclass. This would align with the [formal BFO-to-PROV-O mapping](https://doi.org/10.1038/s41597-025-04580-1) and enable structured protocol metadata alongside the existing provenance chain.

## Source code

The LinkML schemas, test data, and documentation source are on GitHub: [nfdi-de/chem-dcat-ap](https://github.com/nfdi-de/chem-dcat-ap)
