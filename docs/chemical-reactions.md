# Chemical reactions

The Chemical Reaction AP module (`chemical_reaction_ap.yaml`) models chemical reactions as a specialized DCAT-AP+ activity with typed participants. It imports the Chemical Entities AP module and thereby transitively also the Material Entities AP module and DCAT-AP+. 

## Design pattern

![chemical_reaction_dark.svg](images/chemical_reaction_dark.svg#only-dark)
![chemical_reaction_light.svg](images/chemical_reaction_light.svg#only-light)

## ChemicalReaction

Mapped to `SIO:010345` (chemical reaction), `ChemicalReaction`extends `EvaluatedActivity` from DCAT-AP+. The rationale for extending this DCAT-AP+ class is that a reaction is the *subject matter* of a dataset, not anthe data-generating activity itself. The `DataGeneratingActivity` that produces the dataset could be reaction monitoring, reaction calorimetry, complex catalytic reaction evaluation, or simply an experimental write-up. `EvaluatedActivity` is the DCAT-AP+ shape that enables linking a reaction to both the `DataGeneratingActivity` (via `evaluated_activity`) and the `Dataset` (via `is_about_activity`). See the [DCAT-AP+ dual linking pattern](https://nfdi-de.github.io/dcat-ap-plus/latest/design-patterns/#dual-linking-dataset--subject-matter).

!!! note "Reaction datasets, participant datasets, and combined analyses"
    Chemistry and catalysis research typically produces datasets at different levels: datasets about a reaction (where the `ChemicalReaction` is the `EvaluatedActivity`), and datasets about individual participants such as a catalyst, starting material, or product (where the substance, as a `SubstanceSample` or similar `EvaluatedEntity`, is characterized by an analytical `DataGeneratingActivity` like NMR, XRD, or GC-MS). Both types of datasets can also serve as `AnalysisSourceData` feeding into a `DataAnalysis` that produces a combined `AnalysisDataset`. All three levels are handled by the DCAT-AP+ provenance architecture ([DataAnalysis chain](https://nfdi-de.github.io/dcat-ap-plus/latest/design-patterns/#the-dataanalysis-chain)) and require no ChemDCAT-AP-specific additions. Such use cases will be modeled in seperate ChemDCAT-AP-based sub-profiles developed by NFDI4Cat and NFDI4Chem. 

### Reaction slots

ChemicalReaction declares the following slots for its participants and conditions:

| Slot                     | Parent slot                  | slot_uri                          | Range                 | Role                 |
|--------------------------|------------------------------|-----------------------------------|-----------------------|----------------------|
| `used_starting_material` | `had_input_entity`           | `RO:0004009` (has primary input)  | `StartingMaterial`    | Input substance      |
| `used_reactant`          | `had_input_entity`           | `RO:0004009`                      | `Reagent`             | Consumed substance   |
| `generated_product`      | `had_output_entity`          | `RO:0004008` (has primary output) | `ChemicalProduct`     | Output substance     |
| `used_catalyst`          | `carried_out_by`             | `RXNO:0000425` (has_catalyst)     | `Catalyst`            | Catalytic agent      |
| `used_solvent`           | `carried_out_by`             | `prov:wasAssociatedWith`          | `DissolvingSubstance` | Dissolving agent     |
| `used_reactor`           | `carried_out_by`             | `prov:wasAssociatedWith`          | `Reactor`             | Container/vessel     |
| `has_yield`              | `has_quantitative_attribute` | `SIO:000008`  (has attribute))    | `Yield`               | Reaction yield       |
| `has_temperature`        | `has_quantitative_attribute` | `SIO:000008`                      | `Temperature`         | Reaction temperature |
| `has_pressure`           | `has_quantitative_attribute` | `SIO:000008`                      | `Pressure`            | Reaction pressure    |
| `has_duration`           | --                           | `schema:duration`                 | `duration`            | xsd:duration         |
| `has_reaction_step`      | `has_part`                   | `BFO:0000051`     (has part)      | `ChemicalReaction`    | Sub-reaction         |
| `related_resource`       | --                           | `dcterms:relation`                | `Resource`            | Related documents    |

Every participant slot is a sub-slot of a DCAT-AP+ slot, following the [extension rules](https://nfdi-de.github.io/dcat-ap-plus/latest/how-to-extend/). Input substances sub-slot → `had_input_entity`; output substances sub-slot → `had_output_entity`; agents (catalyst, solvent, reactor) sub-slots → `carried_out_by`.

!!! warning "`Catalyst` and `DissolvingSubstance` extend `AgenticEntity`, not `MaterialEntity`"
    In the DCAT-AP+ provenance model, `carried_out_by` has range `AgenticEntity` (mapped to `prov:Agent`). A catalyst or solvent is an *agent* that influences the reaction without being consumed. Both `Catalyst` and `DissolvingSubstance` therefore extend `AgenticEntity` and mix in the `ChemicalSubstanceMixin` for their chemical properties. This is consistent with PROV-O: an agent bears responsibility for (or influences) an activity.

### Reaction participants

ChemDCAT-AP defines six classes for the different roles a substance or device can play in a `ChemicalReaction`. Each extends either `MaterialEntity` (for consumed inputs and outputs), `AgenticEntity` (for substances and devices that influence the reaction without being consumed), or `Device` (for physical equipment):

* **StartingMaterial** (mapped to `PROCO:0000029`): A substance with a starting material role in a `ChemicalReaction`.  
* **Reagent** (mapped to `SIO:010411`): A substance consumed or transformed in a `ChemicalReaction`.
* **ChemicalProduct** (`NCIT:C48810`): A chemical substance that is produced by a `ChemicalReaction`.
* **Catalyst** (`SIO:010344`): A substance or material that initiates or accelerates a `ChemicalReaction` without being consumed.
* **DissolvingSubstance** (`SIO:010417`): A liquid that dissolves other substances.
* **Reactor** (`AFE:0000153`): The container in which a `ChemicalReaction` takes place. It extends `Device` (from DCAT-AP+) and mixes in the `MaterialisticMixin`.

All reaction participants that are chemical substances mix in the `ChemicalSubstanceMixin`, giving them access to `composed_of` (linking to `ChemicalEntity` instances with structure descriptors), `has_concentration`, `has_ph_value`, `has_amount`, and all physical properties from `MaterialisticMixin`.

`StartingMaterial`, `Reagent`, and `Catalyst` carry a `has_molar_equivalent` slot for expressing stoichiometric ratios relative to a reference substance. `DissolvingSubstance` carries a `has_percentage_of_total` slot for tracking how solvent volume is distributed across steps in a multi-step reaction. These slots are specific to the reaction context and are not inherited from the mixins.

!!! warning "Reagent vs. Reactant: terminology under review"
    The class is named `Reagent` based on the SIO definition, but the slot that references it is `used_reactant`. The IUPAC Gold Book treats "reagent" as a synonym of "reactant," but the SIO definition of reagent ("a substance added to bring about a chemical reaction") is broad enough to also cover catalysts and starting materials. A more precise ontology mapping is being discussed in [issue #119](https://github.com/nfdi-de/chem-dcat-ap/issues/119). The class name or mapping may change in a future version.

### Reaction-specific attribute classes

| Class               | class_uri       | Description                                                   |
|---------------------|-----------------|---------------------------------------------------------------|
| `Yield`             | `qudt:Quantity` | Fraction of product formed relative to stoichiometric maximum |
| `MolarEquivalent`   | `qudt:Quantity` | Stoichiometric ratio relative to a reference substance        |
| `PercentageOfTotal` | `qudt:Quantity` | Fraction of a substance relative to total amount across steps |

All three extend `QuantitativeAttribute` and follow the standard `value` + `has_quantity_type` + `unit` pattern.

### Multi-step reactions

The `has_reaction_step` slot (sub-slot of `has_part`, mapped to `BFO:0000051`) enables recursive reaction composition. A multi-step synthesis is itself a `ChemicalReaction` whose steps are also `ChemicalReaction` instances. Each step can have its own participants, temperature, pressure, and duration. Using the `has_part` slot inherited from `EvaluatedActivity`, also other steps of a reaction that are not themselves reactions, such as stirring, filtering, or washing, can be described. For a more elaborate example of this see [this reaction monitoring dataset example](quickstart.md#a-reaction-monitoring-dataset).

## Example: a phosphine synthesis

From the test dataset ([Chemotion Repository CRR-56408](https://www.chemotion-repository.net/pid/56408)), this is valid instance data for a reaction producing 1-diphenylphosphoryl-2-fluorobenzene in 86% yield. It is a truncated excerpt showing the basic structural pattern of a `ChemicalReaction`:

```yaml
id: doi:10.14272/reaction/SA-FUHFF-UHFFFADPSC-MTSVGCFANK-UHFFFADPSC-NUHFF-NUHFF-NUHFF-ZZZ
title:
  - "CRR-56408"
description:
  - "The reaction has been conducted in dry glass ware under argon atmosphere. A solution of 1-bromo-2-fluorobenzene (1.76 g, 1.10 mL, 9.86 mmol, 1.08 equiv) in anhydrous THF (24.0 mL) was cooled to -78 °C, and n-BuLi (689 mg, 4.30 mL, 10.8 mmol, 2.50M in hexane, 1.18 equiv) was added drop-wise over 10 min. After stirring for further 50 min, a solution of chloro(diphenyl)phosphine (2.09 g, 1.70 mL, 9.09 mmol, 1.00 equiv) in anhydrous THF (3.00 mL) was added drop-wise over 10 min, and the reaction mixture was stirred for 8 h at -78 °C. [...]"
rdf_type:
  id: RXNO:0000329
  title: "planned synthesis"
other_identifier:
  - notation: https://www.chemotion-repository.net/pid/56408

# --- Literature references ---
related_resource:
  - id: doi:10.1080/03086648208081193
    title: "SYNTHESE UND NMR-UNTERSUCHUNGEN VON 2-FLUOR-TRIPHENYLPHOSPHINEN..."

# --- Starting materials (sub-slot of had_input_entity) ---
used_starting_material:
  - id: https://www.chemotion-repository.net/pid/56408_StartMat-1
    title: "StartMat-1: 1-bromo-2-fluorobenzene"
    rdf_type:
      id: CHEBI:59999
      title: "chemical substance"
    has_amount:
      - title: "Amount [mmol]"
        has_quantity_type: http://qudt.org/vocab/quantitykind/AmountOfSubstance
        unit: https://qudt.org/vocab/unit/MilliMOL
        value: 9.862
    has_volume:
      - title: "Volume [mL]"
        has_quantity_type: http://qudt.org/vocab/quantitykind/Volume
        unit: https://qudt.org/vocab/unit/MilliL
        value: 1.100
    has_mass:
      - title: "Mass [mg]"
        has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
        unit: https://qudt.org/vocab/unit/MilliGM
        value: 1761.100
    has_density:
      - title: "Density [g/mL]"
        has_quantity_type: http://qudt.org/vocab/quantitykind/Density
        unit: https://qudt.org/vocab/unit/GM-PER-MilliL
        value: 1.601
    has_molar_equivalent:
      - title: "Molar Equivalent"
        has_quantity_type: http://qudt.org/vocab/quantitykind/Dimensionless
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 1.085
    composed_of:
      - id: https://pubchem.ncbi.nlm.nih.gov/compound/61259
        rdf_type:
          id: CHEBI:35496
          title: "fluorobenzenes"

# --- Product (sub-slot of had_output_entity) ---
generated_product:
  - id: https://dx.doi.org/10.14272/MTSVGCFANKMACF-UHFFFAOYSA-N.1
    title: "Reaction mixture containing crude 1-diphenylphosphoryl-2-fluorobenzene"
    rdf_type:
      id: CHEBI:59999
      title: "chemical substance"
    has_amount:
      - title: "Amount [mmol]"
        has_quantity_type: http://qudt.org/vocab/quantitykind/AmountOfSubstance
        unit: https://qudt.org/vocab/unit/MilliMOL
        value: 7.779
    has_mass:
      - title: "Mass [mg]"
        has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
        unit: https://qudt.org/vocab/unit/MilliGM
        value: 2328.000
    composed_of:
      - id: https://pubchem.ncbi.nlm.nih.gov/compound/13005284
        molecular_formula:
          - value: "C18H14FOP"
        iupac_name:
          - value: "1-diphenylphosphoryl-2-fluorobenzene"
    has_physical_state: SOLID
    has_qualitative_attribute:
      - title: "property: colorless"
        value: "colorless"
        rdf_type:
          id: PATO:0000337
          title: colorless

# --- Solvents (sub-slot of carried_out_by) ---
used_solvent:
  - id: https://www.chemotion-repository.net/pid/56408_Solvent-1
    rdf_type:
      id: CHEBI:59999
      title: "chemical substance"
    has_volume:
      - title: "Volume [mL]"
        has_quantity_type: http://qudt.org/vocab/quantitykind/Volume
        unit: https://qudt.org/vocab/unit/MilliL
        value: 24.000
    has_percentage_of_total:
      - title: "PercentageOfTotal"
        has_quantity_type: http://qudt.org/vocab/quantitykind/Dimensionless
        unit: https://qudt.org/vocab/unit/PERCENT
        value: 13
    composed_of:
      - id: https://pubchem.ncbi.nlm.nih.gov/compound/8028
        rdf_type:
          id: CHEBI:26911
          title: "oxolane"
        title: "THF"

# --- Reaction conditions ---
has_yield:
  - type:
      id: VOC4CAT:0005005
      title: "yield"
    has_quantity_type: http://qudt.org/vocab/quantitykind/Dimensionless
    unit: http://qudt.org/vocab/unit/PERCENT
    value: 86
    title: "Yield [%]"
has_duration: PT22H
```

Key observations:

- Each participating chemical substance links to its `ChemicalEntity` via `composed_of`.
- Quantitative properties use the standard DCAT-AP+ pattern consistently: `value` + `has_quantity_type` + `unit`.
- `has_percentage_of_total` on solvents enables tracking how solvent volume is distributed across a multi-step procedure.
- `has_duration` uses the `xsd:duration` type (`PT22H` = 22 hours), defined as a custom LinkML type in DCAT-AP+.
- `related_resource` links to literature DOIs that describe or inform the reaction protocol.
