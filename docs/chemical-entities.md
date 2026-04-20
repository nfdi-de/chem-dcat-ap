# Chemical entities

The Chemical Entities AP module ([chemical_entities_ap.yaml](schema/chemical_entities_ap.yaml)) imports the Material Entities AP module and thus adds chemical identity to the material entity layer. It allows describing chemical substances as material things that are mixable, soluble and most importantly composed of certain chemical structures.

## Design Pattern

![chemical_entities_dark.svg](images/chemical_entities_dark.svg#only-dark)
![chemical_entities_light.svg](images/chemical_entities_light.svg#only-light)

## ChemicalEntity

The `ChemicalEntity` shape is mapped to `CHEBI:23367` (labeled _molecular entity_ in CHEBI; aliased as such in the schema) and extends `Entity` from DCAT-AP+, **not** `MaterialEntity`. It was labeled `ChemicalEntity` because chemists often find CHEBI's label misleading as it suggests only molecules, excluding ions, radicals, complexes, and conformers that are all in scope of `CHEBI:23367`.

!!! note "Why ChemicalEntity extends Entity, not MaterialEntity"
    Ontologically, a CHEBI chemical entity *is* a BFO material entity, and a reasoner can infer this from the ontology axioms. But ChemDCAT-AP is a shape specification, not an ontology. If `ChemicalEntity` extended `MaterialEntity`, it would inherit the `MaterialisticMixin` slots (`has_temperature`, `has_mass`, `has_volume`, `has_density`, `has_pressure`, `has_physical_state`) via LinkML's `is_a` inheritance. These physical property slots do not make sense at the molecular level (an individual molecule does not have a temperature or a density) and would confuse schema users into thinking they should populate them. Extending `Entity` directly avoids this: molecular-level classes get only the slots they need (structure descriptors), while macroscopic substance classes get physical properties through the `ChemicalSubstanceMixin` applied to `MaterialEntity` subclasses.

### Structure descriptor slots

`ChemicalEntity` introduces six slots for chemical identity, all sub-slots of the DCAT-AP+ `has_qualitative_attribute` or `has_quantitative_attribute`:

| Slot                | Range class        | class_uri        | What it captures           |
|---------------------|--------------------|------------------|----------------------------|
| `inchi`             | `InChi`            | `CHEMINF:000113` | InChI structure descriptor |
| `inchikey`          | `InChIKey`         | `CHEMINF:000059` | InChI key descriptor       |
| `smiles`            | `SMILES`           | `CHEMINF:000018` | SMILES line notation       |
| `molecular_formula` | `MolecularFormula` | `CHEMINF:000042` | Hill system formula        |
| `iupac_name`        | `IUPACName`        | `CHEMINF:000107` | Systematic IUPAC name      |
| `has_molar_mass`    | `MolarMass`        | `AFR:0002409`    | Molar mass quantity        |

The first five are `QualitativeAttribute` subclasses (string-valued descriptors); `MolarMass` is a `QuantitativeAttribute` subclass (numeric-valued with unit). All use `slot_uri: SIO:000008` (has attribute). All descriptor slots are `recommended: true`, meaning they should be provided when available but are not required for validation.

!!! tip "Use dedicated slots, not generic `has_qualitative_attribute`"
    ChemDCAT-AP defines `inchi`, `smiles`, etc. as dedicated sub-slots with typed ranges. Use these instead of the generic `has_qualitative_attribute` with a `rdf_type` classification. The dedicated slots produce more explicit instance data, enable tighter validation, and are easier to query.

### Compositional structure 

`ChemicalEntity` overrides `has_part` (inherited from `Entity`) to constrain its range to `ChemicalEntity` and its mapping is changed to `BFO:0000051`. This enables recursive molecular composition: a complex can declare its ligands as parts, each with their own structure descriptors.

## ChemicalSubstanceMixin

An abstract mixin that extends `MaterialisticMixin` with chemistry-specific substance properties. It is applied to `MaterialEntity` subclasses that represent macroscopic chemical substances.

| Slot | Range | Inherited from |
|---|---|---|
| `has_concentration` | `Concentration` | ChemicalSubstanceMixin |
| `has_ph_value` | `PHValue` | ChemicalSubstanceMixin |
| `has_amount` | `AmountOfSubstance` | ChemicalSubstanceMixin |
| `composed_of` | `ChemicalEntity[]` | ChemicalSubstanceMixin |
| `has_temperature` | `Temperature` | MaterialisticMixin |
| `has_mass` | `Mass` | MaterialisticMixin |
| `has_volume` | `Volume` | MaterialisticMixin |
| `has_density` | `Density` | MaterialisticMixin |
| `has_pressure` | `Pressure` | MaterialisticMixin |
| `has_physical_state` | `PhysicalStateEnum` | MaterialisticMixin |
| `alternative_label` | `string` | MaterialisticMixin |

The `composed_of` slot (a sub-slot of `has_part`, mapped to `BFO:0000051`) links a substance to its constituent `ChemicalEntity` instances. This is the bridge between the macroscopic substance and the molecular-level identity.

### Chemistry-specific attribute classes

| Class | class_uri | Parent | Mappings |
|---|---|---|---|
| `Concentration` | `CHMO:0002820` | `QuantitativeAttribute` | exact: `EDAM:2140`, `NCIT:C41185`, `VOC4CAT:0007244`, `AFR:0002036` |
| `AmountOfSubstance` | `qudt:Quantity` | `QuantitativeAttribute` | close: `PATO:0000070` |
| `PHValue` | `SIO:001089` | `QuantitativeAttribute` | exact: `NCIT:C45997`, `AFR:0001142` |

These follow the DCAT-AP+ [QuantitativeAttribute pattern](https://nfdi-de.github.io/dcat-ap-plus/latest/design-patterns/#quantitativeattribute). Each narrows the semantic intent while preserving the structural `value` + `has_quantity_type` + `unit` shape.

!!! warning "Enum bindings for `has_quantity_type` and `unit` are still experimental"
    The schema declares bindings that constrain `has_quantity_type` and `unit` values to QUDT QuantityKind and Unit vocabularies respectively. These bindings are not enforced by `linkml-validate`. They will be validated using the [linkml-term-validator](https://linkml.io/linkml-term-validator/), which is meant to supports dynamic enums and binding validation. Yet, this still needs to be implemented in the ChemDCAT-AP pipeline.

## SubstanceSample

Mapped to `SIO:001378` (analyte), `SubstanceSample` extends `MaterialSample` (from `material_entities_ap`) and uses the `ChemicalSubstanceMixin`. It is the central class for any evaluated chemical substance in ChemDCAT-AP. It combines three capabilities:

- **Provenance linking** (via `EvaluatedEntity`): it is meant to be used as the range of `evaluated_entity` and `is_about_entity` in specializations of `DataGeneratingActivity` respectively `Dataset` (see [dataset and activity shapes](dataset-activity-shapes.md)).
- **Physical properties** (via `MaterialisticMixin`, inherited through `ChemicalSubstanceMixin`): temperature, mass, volume, density, pressure, physical state.
- **Chemical identity** (via `ChemicalSubstanceMixin`): `composed_of` linking to `ChemicalEntity` instances with structure descriptors, plus concentration, pH, and amount of substance.

Use `SubstanceSample` whenever your data describes a chemical substance that was the subject of a measurement or analysis. This covers NMR samples, catalysis test substances, reaction aliquots, and any other analytically characterized chemical material. For substances that participate in a reaction but are not themselves the evaluated subject, use the reaction participant classes (`StartingMaterial`, `Reagent`, etc.) instead.

### Example: a SubstanceSample with chemical identity

From the test dataset, a Chemotion Repository compound:

```yaml
id: https://dx.doi.org/10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N.2
title: "CRS-50440"
rdf_type:
  id: CHEBI:59999
  title: "chemical substance"
other_identifier:
  - notation: https://www.chemotion-repository.net/pid/50440
has_temperature:
  - rdf_type:
      id: NMR:1400025
      title: "sample temperature in magnet"
    has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
    unit: https://qudt.org/vocab/unit/K
    value: 300.0
composed_of:
  - id: https://dx.doi.org/10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N.2#EvaluatedCompound
    description: "compound assigned to the sample"
    other_identifier:
      - notation: https://pubchem.ncbi.nlm.nih.gov/compound/26248854
    inchikey:
      - value: "UGRXAOUDHZOHPF-UHFFFAOYSA-N"
        title: "assigned InChiKey"
    inchi:
      - value: "InChI=1S/C11H12N2S/c1-12-7-10-8-14-11(13-10)9-5-3-2-4-6-9/h2-6,8,12H,7H2,1H3"
        title: "assigned InChi"
    smiles:
      - value: " CNCc1csc(n1)c1ccccc1"
        title: "assigned SMILES"
    molecular_formula:
      - value: "C11H12N2S"
        title: "assigned molecular formula"
    iupac_name:
      - value: "N-methyl-1-(2-phenyl-1,3-thiazol-4-yl)methanamine"
        description: Chemotion IUPAC name
      - value: "Methyl[(2-phenyl-1,3-thiazol-4-yl)methyl]amine"
        description: PubChem IUPAC name
    has_molar_mass:
      - has_quantity_type: http://qudt.org/vocab/quantitykind/MolarMass
        unit: https://qudt.org/vocab/unit/GM-PER-MOL
        value: 204.072119
        description: Molar mass as specified in the Chemotion repository.
      - has_quantity_type: http://qudt.org/vocab/quantitykind/MolarMass
        unit: https://qudt.org/vocab/unit/GM-PER-MOL
        value: 204.29
        description: Molar mass as specified in PubChem.
```

Key observations:

- The `SubstanceSample` (macroscopic level) links to its `ChemicalEntity` (molecular level) via `composed_of`.
- The `ChemicalEntity` carries all structure descriptors. Each descriptor slot allows multiple values (e.g. two `iupac_name` entries from different sources, two `has_molar_mass` entries with different precision).
- The sample's temperature uses `rdf_type` to classify it as specifically the sample temperature in the NMR magnet (`NMR:1400025`), not just any temperature. Similarly, the `SubstanceSample` is additionally typed to be an instance of CHEBI's _chemical substance_ class. This is the [ClassifierMixin](https://nfdi-de.github.io/dcat-ap-plus/latest/design-patterns/#pattern-3-flexible-classification-classifiermixin) at work.

## PolymerSample and PolymerMixin

`PolymerSample` extends `SubstanceSample` and mixes in `PolymerMixin`. It follows the same pattern as `SubstanceSample` itself: a substance class gains domain-specific properties through a mixin.

`PolymerMixin` extends `ChemicalSubstanceMixin` but currently defines no additional slots. It is a placeholder for future polymer-specific properties (degree of polymerization, molecular weight distribution, branching, etc.) that will follow the same mixin-based pattern used throughout ChemDCAT-AP.

!!! warning "Stub: shared `class_uri`"
    `PolymerSample` currently shares `class_uri: SIO:001378` with its parent `SubstanceSample`. A more specific mapping is planned for a future release. The schema flags this as a TODO.

## Atom

`Atom` (mapped to `CHEBI:33250`) extends `Entity` directly. It is a currently minimal shape whose only addition is that `rdf_type` is `required: true`, forcing every instance to declare which specific atom type it is via the [ClassifierMixin](https://nfdi-de.github.io/dcat-ap-plus/latest/design-patterns/#pattern-3-flexible-classification-classifiermixin). The slot description indicates that the value should come from CHEBI's atom branch (`CHEBI:33250` and its subclasses, e.g. `CHEBI:26708` for a sodium atom), but this constraint is not yet enforced programmatically. Future versions of ChemDCAT-AP will use LinkML [slot bindings](https://linkml.io/linkml-model/latest/docs/bindings/) and the [linkml-term-validator](https://linkml.io/linkml-term-validator/) to validate this.

!!! note "Why Atom extends Entity, not ChemicalEntity"
    Since `ChemicalEntity` is grounded in CHEBI' _molecular entity_, and CHEBI's atom class (`CHEBI:33250`) is not a subclass of molecular entity in CHEBI's class hierarchy, subsuming `Atom` under `ChemicalEntity` would be ontologically incorrect. Extending `Entity` directly fixes this issue.
