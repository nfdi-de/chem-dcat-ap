# Adoption Guide

This page provides practical guidance for chemists, data stewards, and developers working with ChemDCAT-AP, whether producing instance data, consuming it, or building further extensions.

For the generic extension rules (what you must do, may do, and must not do), see the [DCAT-AP+ Extension Rules](https://nfdi-de.github.io/dcat-ap-plus/latest/how-to-extend/).

---

## Producing instance data

### Use dedicated slots before falling back to generic attributes

ChemDCAT-AP defines dedicated slots for common chemistry properties. Use them instead of the generic DCAT-AP+ attribute pattern when they exist.

!!! tip "Do: use the dedicated `inchikey` slot"
    ```yaml
    # On a ChemicalEntity
    inchikey:
      - value: "UGRXAOUDHZOHPF-UHFFFAOYSA-N"
        title: "assigned InChiKey"
    ```

!!! warning "Don't: encode an InChIKey as a generic QualitativeAttribute"
    ```yaml
    # This works but is less precise and harder to query
    has_qualitative_attribute:
      - value: "UGRXAOUDHZOHPF-UHFFFAOYSA-N"
        rdf_type:
          id: CHEMINF:000059
          title: InChiKey
    ```

The generic `has_qualitative_attribute` pattern is the correct fallback when no dedicated slot exists. For example, when encoding an NMR-specific parameter that ChemDCAT-AP doesn't have a slot for.

### Decision table: which slot to use for chemical identifiers

| Identifier type   | Dedicated slot      | Fallback                                                    |
|-------------------|---------------------|-------------------------------------------------------------|
| InChI             | `inchi`             | `has_qualitative_attribute` with `rdf_type: CHEMINF:000113` |
| InChIKey          | `inchikey`          | `has_qualitative_attribute` with `rdf_type: CHEMINF:000059` |
| SMILES            | `smiles`            | `has_qualitative_attribute` with `rdf_type: CHEMINF:000018` |
| Molecular formula | `molecular_formula` | `has_qualitative_attribute` with `rdf_type: CHEMINF:000042` |
| IUPAC name        | `iupac_name`        | `has_qualitative_attribute` with `rdf_type: CHEMINF:000107` |
| CAS number        | *(none yet)*        | `has_qualitative_attribute` with appropriate `rdf_type`     |
| PubChem CID       | *(none yet)*        | `other_identifier` with `notation`                          |

### Place identifiers on the right entity

Chemical identifiers describe the *chemical entity*, not the *sample*. A sample may be impure, degraded, or a mixture. The identifiers belong to the constituent entities.

!!! tip "Do: identifiers on the ChemicalEntity inside `composed_of`"
    ```yaml
    # SubstanceSample
    id: ex:sample-001
    composed_of:
      - id: ex:compound-001
        inchikey:
          - value: "BSYNRYMUTXBXSQ-UHFFFAOYSA-N"
    ```

!!! warning "Don't: identifiers directly on the sample"
    ```yaml
    # Wrong level -- the sample is not the molecule
    id: ex:sample-001
    inchikey:
      - value: "BSYNRYMUTXBXSQ-UHFFFAOYSA-N"
    ```

    This would fail schema validation because `SubstanceSample` does not directly carry the `inchikey` slot. It inherits chemical identity only through the `ChemicalSubstanceMixin`'s `composed_of` -> `ChemicalEntity` chain. See [Chemical entities: SubstanceSample](chemical-entities.md#substancesample).

### Use `rdf_type` for ontology classification, `type` for vocabulary tagging

This is the [ClassifierMixin pattern](https://nfdi-de.github.io/dcat-ap-plus/v0.1.0rc4/design-patterns/#rdf_type-vs-type-when-to-use-which) from DCAT-AP+. The rule is straightforward:

|                         | `rdf_type`                                                                                                                                                                   | `type`                                                                                                                                                      |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Mapped to**           | `rdf:type`                                                                                                                                                                   | `dcterms:type`                                                                                                                                              |
| **Semantic commitment** | **Ontological assertion** — the instance *is* an instance of the referenced class                                                                                            | **Cataloging assertion** — the instance *is categorized as* the referenced concept                                                                          |
| **Range expectation**   | An OWL/RDFS class from a formal ontology                                                                                                                                     | A SKOS concept or term from a controlled vocabulary                                                                                                         |
| **Reasoner behaviour**  | OWL reasoners will infer class membership and apply class axioms                                                                                                             | No inference; treated as a simple annotation                                                                                                                |
| **Use when**            | You want the full semantic weight of formal ontology typing (e.g., classifying a `DataGeneratingActivity` as `CHMO:0000595` so that reasoners know it is an NMR measurement) | You want lightweight tagging without committing to an ontology's full logical structure (e.g., tagging a dataset with a SKOS concept from a local taxonomy) |

### Always provide QUDT quantity kinds and units

Every `QuantitativeAttribute` (and its subclasses like `Temperature`, `Mass`, `Concentration`, etc.) should specify `has_quantity_type` and `unit` using QUDT IRIs. Without these, the numeric `value` is meaningless: "300" could be Kelvin, Celsius, or milligrams. See the [Quick start](quickstart.md#where-to-find-valid-qudt-uris) for where to find valid QUDT URIs.

!!! tip "Do: explicit quantity kind and unit"
    ```yaml
    has_temperature:
      - value: 300.0
        has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
        unit: https://qudt.org/vocab/unit/K
    ```

!!! warning "Don't: value without unit context"
    ```yaml
    has_temperature:
      - value: 300.0
        title: "Temperature in K"  # title is for humans, not machines
    ```

---

## Modeling reactions

### Decision table: input vs. agent roles

| Question                                              | If yes → | Slot                                        |
|-------------------------------------------------------|----------|---------------------------------------------|
| Is the substance consumed or transformed?             | Input    | `used_starting_material` or `used_reactant` |
| Does the substance accelerate without being consumed? | Agent    | `used_catalyst`                             |
| Does the substance provide the reaction medium?       | Agent    | `used_solvent`                              |
| Is it a physical container?                           | Agent    | `used_reactor`                              |
| Is it produced by the reaction?                       | Output   | `generated_product`                         |

### Starting material vs. reactant

Both `used_starting_material` and `used_reactant` are sub-slots of `had_input_entity` and both map to `RO:0004009`. The distinction is conventional in synthetic chemistry:

- **Starting material**: the substrate that defines the synthetic target -- the molecule being built upon.
- **Reactant/reagent**: other consumed substances that enable the transformation (bases, oxidants, reducing agents, etc.).

If this distinction is not meaningful in your context, either slot is acceptable. Both produce the same RDF predicate.

---

## Substances in multiple roles: shapes, not classes

In chemistry, the same substance frequently plays different roles in different contexts. A palladium catalyst in a Suzuki coupling may also be the analyte in an XPS surface analysis. A solvent used in a reaction may be the subject of a purity measurement. The instinct, especially if you're used to OWL modeling, is to solve this in the schema: create a class that inherits from both `AgenticEntity` and `EvaluatedEntity`, or define a `CatalystSample` that is simultaneously an agent and an evaluated entity.

**Don't do this.** It conflates two modeling contexts that ChemDCAT-AP deliberately keeps separate.

### The trap: switching between SHACL and OWL thinking

ChemDCAT-AP classes represent [SHACL node shapes, not OWL classes](https://nfdi-de.github.io/dcat-ap-plus/latest/design-patterns/#pattern-1-the-provenance-core-prov-o-alignment). A node shape defines *what properties an instance must/may have when it appears in a specific slot*. It does not define what the instance *is* in the ontological sense.

When you write `used_catalyst: [{id: ex:pd-001, ...}]`, you are saying: "in this slot, `ex:pd-001` conforms to the `Catalyst` shape." When you write `evaluated_entity: [{id: ex:pd-001, ...}]`, you are saying: "in this slot, the same `ex:pd-001` conforms to the `EvaluatedEntity` shape." These are different validation contexts, not competing ontological claims.

In the RDF output, `ex:pd-001` receives type assertions from both shapes, `prov:Agent` and `prov:Entity`. This is explicitly legal in PROV-O, which anticipates that the same thing can be both.

| OWL thinking (wrong instinct) | SHACL thinking (correct approach) |
|---|---|
| "I need a class that is both Agent and Entity" | "The same IRI conforms to different shapes in different slots" |
| "Create `CatalystSample` with `is_a: AgenticEntity` and `is_a: EvaluatedEntity`" | "Use `ex:pd-001` in `used_catalyst` for one activity and in `evaluated_entity` for another" |
| Leads to multiple inheritance, schema complexity | No schema change needed |

### Worked example: catalyst studied by NMR spectroscopy

A palladium catalyst is used in a Suzuki coupling and then studied by 13C NMR spectroscopy:

```yaml
# Activity 1: The Suzuki coupling - Pd complex is the catalyst (agent)
# An instance of a ChemicalReaction as defined in ChemDCAT-AP
id: ex:suzuki-001
title: "Suzuki coupling of aryl bromide"
rdf_type:
  id: RXNO:0000329
  title: "Suzuki coupling"
used_catalyst:
  - id: ex:pd-catalyst-001
    rdf_type:
      id: CHEBI:59999
      title: "chemical substance"
    composed_of:
      - id: https://pubchem.ncbi.nlm.nih.gov/compound/6102075
        molecular_formula:
          - value: "C36H30Cl2P2Pd"
        iupac_name:
          - value: "dichloropalladium;bis(triphenylphosphane)"

# Activity 2: The NMR study - same Pd complex is now the evaluated entity
# An instance of a NMRSpectroscopy as defined in NMR-DCAT-AP
id: ex:nmr-measurement-001
rdf_type:
  id: CHMO:0000595
  title: "carbon-13 nuclear magnetic resonance spectroscopy"
evaluated_entity:
  - id: ex:pd-catalyst-001    # same IRI as the catalyst above
    has_quantitative_attribute:
      - rdf_type:
          id: NMR:1400025
          title: "sample temperature in magnet"
        value: 298.0
        has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
        unit: https://qudt.org/vocab/unit/K
```

If these instances get merged into an RDF graph `ex:pd-catalyst-001` carries types from both activity contexts:

```turtle
ex:pd-catalyst-001 a prov:Agent ;     # from Catalyst shape (via class_uri)
                    a prov:Entity ;    # from EvaluatedEntity shape (via class_uri)
                    a CHEBI:59999 .    # from rdf_type on the catalyst instance
```

One node, multiple type assertions, no conflict. 

The practical question is where to put the detailed description (composition, identifiers, physical properties) when the same substance appears in multiple activities.

!!! tip "Describe fully on first occurrence, reference by IRI thereafter"
    Put the complete substance description (composition, identifiers, quantitative attributes) in the activity where the substance is most central, typically the reaction for reactants/catalysts, or the measurement for analytes. In subsequent activities, reference by IRI only and add only the properties specific to that context (e.g. binding energy measured by XPS).

## Extending ChemDCAT-AP further

If ChemDCAT-AP doesn't cover your subdomain (e.g. NMR-specific metadata, polymer characterization, electrochemistry), you can build a third-layer profile that imports ChemDCAT-AP, following the same [extension rules](https://nfdi-de.github.io/dcat-ap-plus/latest/how-to-extend/) that ChemDCAT-AP follows for DCAT-AP+. [NMR-DCAT-AP](https://nfdi4chem.github.io/nmr-dcat-ap/) demonstrates this pattern.

ChemDCAT-AP also provides [coarse-grained convenience shapes](dataset-activity-shapes.md) for `Dataset` and `DataGeneratingActivity`. You may reuse these as-is, or define more granular alternatives in your sub-profile using the DCAT-AP+ [DataAnalysis chain](https://nfdi-de.github.io/dcat-ap-plus/latest/design-patterns/#the-dataanalysis-chain).

### Conformance checklist

In addition to the [DCAT-AP+ conformance checklist](https://nfdi-de.github.io/dcat-ap-plus/latest/how-to-extend/#conformance-checklist-for-your-domain-profile):

- [x] Schema imports `chem-dcat-ap` (which transitively imports `dcat-ap-plus`)
- [x] New sample types use `is_a: SubstanceSample` or `is_a: MaterialSample`
- [x] New quantity types use `is_a: QuantitativeAttribute` (or a ChemDCAT-AP subclass)
- [x] New identifier types use `is_a: QualitativeAttribute`
- [x] `class_uri` maps to a BFO-aligned ontology term (ensures PROV-O compatibility)
- [x] Chemical identifier slots use `is_a: has_qualitative_attribute` and `slot_uri: SIO:000008`
- [x] Reaction role slots specify `is_a` from the appropriate DCAT-AP+ base slot (`had_input_entity`, `had_output_entity`, or `carried_out_by`)

### Anti-patterns to avoid

!!! warning "Don't: duplicate DCAT-AP+ or ChemDCAT-AP classes"
    If you need a `Catalyst` with additional properties, subclass it. Don't redefine it. If you redefine it, you lose the slot inheritance chain and break backward compatibility.

!!! warning "Don't: use `class_uri` from non-BFO-aligned ontologies without considering the consequences"
    If your ontology term is not BFO-aligned, the BFO -> PROV-O inference chain breaks. Either use `rdf_type` instead (which doesn't replace the parent's `class_uri`) or verify the alignment manually. See [Ontology alignment: Why SIO](ontology-alignment.md#why-sio) for how ChemDCAT-AP handles this for SIO terms.
