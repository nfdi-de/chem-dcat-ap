# Quick start for developers

This page is for developers who need to produce ChemDCAT-AP-conformant output from a database or API. It assumes familiarity with data schemas (JSON Schema, YAML, JSON-LD) but not with LinkML or semantic web technologies.

## LinkML in 60 seconds

ChemDCAT-AP is written in [LinkML](https://linkml.io/), a YAML-based schema language. If you know JSON Schema, the mental model transfers:

- A **class** is like a JSON Schema `object` with typed properties. It defines a data shape.
- A **slot** is a property on a class (a key in your JSON/YAML). It has a `range` (the expected type).
- **`is_a`** is structural inheritance: a child class gets all the parent's slots.
- A **mixin** injects slots into a class without being a parent. Think of it as a trait or interface.
- **`class_uri`** and **`slot_uri`** are the ontology terms the class/slot maps to in RDF output. They do not affect the JSON/YAML structure.
- **`inlined_as_list: true`** means the value is an array of nested objects (not references).
- **`range`** is the type constraint: another class, a primitive (`string`, `float`, `uriorcurie`), or an enum.

For a full introduction, see the [LinkML documentation](https://linkml.io/linkml/).

## CURIEs and prefixes

Throughout the schema and instance data you will see two forms of identifiers:

- **Full URIs**: `http://purl.obolibrary.org/obo/CHEBI_23367`
- **CURIEs** (Compact URI Expressions): `CHEBI:23367`

A CURIE is a shorthand. It consists of a **prefix** (`CHEBI`) and a **local part** (`23367`), separated by a colon. The prefix maps to a base URI declared in the schema's `prefixes` block. The CURIE expands by concatenating the base URI with the local part:

```yaml
# In the schema:
prefixes:
  CHEBI: http://purl.obolibrary.org/obo/CHEBI_
  SIO: http://semanticscience.org/resource/SIO_
  qudt: http://qudt.org/schema/qudt/
  doi: https://doi.org/

# In instance data, these are equivalent:
id: CHEBI:23367           # → http://purl.obolibrary.org/obo/CHEBI_23367
id: SIO:000008            # → http://semanticscience.org/resource/SIO_000008
id: doi:10.14272/...      # → https://doi.org/10.14272/...
```

This matters for three reasons:

1. **RDF output** uses the expanded URIs. If you produce RDF directly (bypassing `linkml-convert`), you need to expand CURIEs yourself.
2. **JSON-LD context** is generated from the prefix map. If you serve JSON-LD, the `@context` handles CURIE expansion for consumers automatically.
3. **Validation**: `linkml-validate` understands CURIEs via the prefix map. Your YAML/JSON can use either form.

The prefix maps for ChemDCAT-AP are declared in each schema module (`chem_dcat_ap.yaml`, `chemical_entities_ap.yaml`, etc.) and include all ontology namespaces used in `class_uri`, `slot_uri`, and the broad, narrow or exact mappings.

## What you produce, and how it becomes RDF

You write instance data as **YAML or JSON** conforming to the ChemDCAT-AP schema. The LinkML toolchain can then validate it, convert it to RDF (Turtle, JSON-LD, N-Triples). You do not need to write RDF directly.

```
Your DB/API → JSON or YAML → linkml-validate → linkml-convert → Turtle / JSON-LD
```

Alternatively, you can use the auto-generated **JSON Schema** to validate JSON output from your API directly, or the auto-generated **SHACL shapes** to validate RDF you produce by other means.

## Accessing the schema and its artifacts

**All schema artifacts** (LinkML YAML schemas, JSON Schema, SHACL shapes, JSON-LD context, etc.) are accessible via content negotiation through the w3id PURLs:

- DCAT-AP+: `https://w3id.org/nfdi-de/dcat-ap-plus/`
- ChemDCAT-AP: `https://w3id.org/nfdi-de/dcat-ap-plus/chemistry/`

This is also how the schemas import each other.

**Python dataclasses** for programmatic instantiation are [published on PyPI](https://pypi.org/project/chem-dcat-ap/):

```bash
pip install dcat-ap-plus chem-dcat-ap
```

## Three ways to use ChemDCAT-AP

### 1. Write YAML/JSON and validate with the CLI
 
Write instance data as YAML (as shown in the examples throughout this documentation), then validate. You must specify the target class (`-C`) that represents the root of your data:
 
```bash
uv run linkml validate tests/data/valid/SubstanceSampleCharacterizationDataset-001.yaml \
  -s src/chem_dcat_ap/schema/chem_dcat_ap.yaml \
  -C SubstanceCharacterizationDataset
```
 
!!! warning "QUDT vocabulary bindings"
    The schema declares bindings that constrain `has_quantity_type` and `unit` values to QUDT vocabularies. These are not yet enforced by `linkml-validate`. Validation via the [linkml-term-validator](https://linkml.io/linkml-term-validator/) is planned but not yet implemented in the ChemDCAT-AP pipeline. This means that, for now, values of these slots need to be validates externally.

Convert to RDF:
 
```bash
uv run linkml-convert -t ttl tests/data/valid/SubstanceSampleCharacterizationDataset-001.yaml \
  -s src/chem_dcat_ap/schema/chem_dcat_ap.yaml \
  -C SubstanceCharacterizationDataset
  -o SubstanceCharacterizationDataset-001.ttl
```

### 2. Use the Python dataclasses

```python
import chem_dcat_ap
from chem_dcat_ap.datamodel.chem_dcat_ap import SubstanceSample, ChemicalEntity, MolecularFormula,
    InChIKey, Temperature
)

sample = SubstanceSample(
    id="https://example.org/sample-001",
    title="My sample",
    has_temperature=[
        Temperature(
            title= "my sample's temperature",
            value=300.0,
            has_quantity_type={"id": "http://qudt.org/vocab/quantitykind/Temperature"},
            unit={"id": "https://qudt.org/vocab/unit/K"},
        )
    ],
    composed_of=[
        ChemicalEntity(
            id="https://example.org/sample-001#compound",
            molecular_formula=[MolecularFormula(value="C11H12N2S")],
            inchikey=[InChIKey(value="UGRXAOUDHZOHPF-UHFFFAOYSA-N")],
        )
    ],
)
```

### 3. Restructure your existing JSON API

If you have an existing API that already serves chemical data in its own JSON format, you can restructure its output to conform to ChemDCAT-AP. Fetch the generated JSON Schema via content negotiation from the w3id PURL and use it as the target structure for your serializer. Once your output conforms, validate it with any JSON Schema validator.

If your pipeline produces RDF, use the generated SHACL shapes (also via content negotiation) with a processor like `pyshacl` to validate conformance.

## The complete picture: Dataset to subject matter

The examples in the other documentation pages show individual classes (a `MaterialSample`, a `SubstanceSample`, a `ChemicalReaction`). Here is how they fit together in a complete `Dataset` structure using ChemDCAT-AP's [convenience shapes](dataset-activity-shapes.md). This is what your API ultimately needs to produce.

### A reaction monitoring dataset

This is a real example from the [Chemotion Repository (CRR-56408)](https://www.chemotion-repository.net/pid/56408), showing a multi-step phosphine synthesis. The source file is part of ChemDCAT-AP's validation test suite: [tests/data/valid/ReactionMonitoringDataset-001.yaml](https://github.com/nfdi-de/chem-dcat-ap/blob/main/tests/data/valid/ReactionMonitoringDataset-001.yaml). The full example is extensive (~1400 lines) because it models individual reaction steps, work-up procedures, and purification as nested activities. The excerpt below shows the top-level Dataset structure and the first reaction step to illustrate the pattern.

```yaml
# A ReactionMonitoringDataset - the Chemotion reaction DOI serves as the Dataset ID
id: doi:10.14272/reaction/SA-FUHFF-UHFFFADPSC-MTSVGCFANK-UHFFFADPSC-NUHFF-NUHFF-NUHFF-ZZZ
title:
  - "Dataset for Chemotion Repository synthesis CRR-56408"
description:
  - "This dataset contains the recorded information for the Chemotion Repository
     synthesis CRR-56408."
related_resource:
  - id: doi:10.1080/03086648208081193
    title: "SYNTHESE UND NMR-UNTERSUCHUNGEN VON 2-FLUOR-TRIPHENYLPHOSPHINEN..."
  - id: doi:10.1002/adsc.202400919
    title: "Arylation of Secondary Phosphines with Diaryliodonium Salts..."

# The full ChemicalReaction description lives here
is_about_activity:
  - id: https://www.chemotion-repository.net/pid/56408
    title:
      - "Chemotion Repository synthesis CRR-56408"
    description:
      - "The reaction has been conducted in dry glass ware under argon atmosphere..."
    rdf_type:
      id: RXNO:0000329
      title: "planned synthesis"
    # Participants, conditions, yield
    used_starting_material:
      - id: https://www.chemotion-repository.net/pid/56408_StartMat-1
        title: "StartMat-1: 1-bromo-2-fluorobenzene"
        has_mass:
          - title: "Mass [mg]"
            has_quantity_type: http://qudt.org/vocab/quantitykind/Mass
            unit: https://qudt.org/vocab/unit/MilliGM
            value: 1761.100
        composed_of:
          - id: https://pubchem.ncbi.nlm.nih.gov/compound/61259
            rdf_type:
              id: CHEBI:35496
              title: "fluorobenzenes"
    used_reactant: [...]
    used_solvent: [...]
    generated_product: [...]
    used_reactor: [...]
    has_yield:
      - value: 86
        has_quantity_type: http://qudt.org/vocab/quantitykind/Dimensionless
        unit: http://qudt.org/vocab/unit/PERCENT
    has_duration: PT22H
    # Reaction steps (chemical transformations)
    has_reaction_step:
      - id: https://www.chemotion-repository.net/pid/56408#step-1
        title: "Step 1: Lithiation and Phosphination"
        has_part:
          # step-1_part-1: dissolving of 1-bromo-2-fluorobenzene in anhydrous Tetrahydrofuran
          - id: https://www.chemotion-repository.net/pid/56408#step-1_part-1
            title:
              - "step-1_part-1: dissolving of 1-bromo-2-fluorobenzene in Tetrahydrofuran"
            rdf_type:
              id: CHMO:0002773
              title: "dissolving"
      - id: https://www.chemotion-repository.net/pid/56408#step-3
        title: "Step 3: Oxidation to Phosphine Oxide"
    # All steps including non-reaction activities (work-up, purification)
    has_part:
      - id: https://www.chemotion-repository.net/pid/56408#step-1
      - id: https://www.chemotion-repository.net/pid/56408#step-2
        rdf_type:
          id: OBI:0000094
          title: "material processing"
      - id: https://www.chemotion-repository.net/pid/56408#step-3
      - id: https://www.chemotion-repository.net/pid/56408#step-4
        rdf_type: 
          id: OBI:0000094
          title: "material processing"
      - id: https://www.chemotion-repository.net/pid/56408#step-5
        rdf_type: 
          id: CHMO:0002582
          title: "flash chromatography"

# The ReactionMonitoring activity -- references the reaction by IRI
was_generated_by:
  - id: doi:10.14272/reaction/SA-FUHFF-UHFFFADPSC-MTSVGCFANK-UHFFFADPSC-NUHFF-NUHFF-NUHFF-ZZZ#Monitoring
    title:
      - "Monitoring of the Chemotion Repo synthesis CRR-56408"
    evaluated_activity:
      - id: https://www.chemotion-repository.net/pid/56408
```

Key structural points:

- This is a `ReactionMonitoringDataset`: `was_generated_by` points to a `ReactionMonitoring` and `is_about_activity` points to a `ChemicalReaction`.
- The **full reaction description** (participants, conditions, yield, steps) lives on the `is_about_activity` node. The `ReactionMonitoring` activity under `was_generated_by` only references the reaction by IRI via `evaluated_activity`. This keeps one authoritative description in one place.
- The `ChemicalReaction` uses **two complementary nesting mechanisms**: `has_reaction_step` for steps that are themselves chemical reactions (here lithiation and oxidation), and `has_part` for all steps including non-reaction activities (work-up, purification). Steps in `has_reaction_step` are also listed in `has_part`.
- Non-reaction steps (warming, quenching, washing, drying, filtering, evaporation, chromatography) are modeled as generic `Activity` instances classified via `rdf_type` with OBI and CHMO terms.
- Within each step, **sub-steps** (`has_part` on the step itself) model the fine-grained experimental procedure: dissolving, drop-wise addition, stirring, cooling, etc. Each sub-step is classified with an OBI or CHMO term (e.g., `CHMO:0002773` dissolving, `OBI:0000274` adding a material entity, `CHMO:0002774` stirring) and declares its own inputs (`had_input_entity`) and outputs (`had_output_entity`), forming a complete input/output chain. Sub-steps link to their predecessor via `had_input_activity`, capturing the chronological sequence of the procedure.

### Converting YAML to RDF

The reaction example is converted to Turtle using:
```bash
uv run linkml-convert -t ttl \
  tests/data/valid/ReactionMonitoringDataset-001.yaml \
  -s src/chem_dcat_ap/schema/chem_dcat_ap.yaml \
  -C ReactionMonitoringDataset
```

This produces the following Turtle (abbreviated for readability):

```turtle
@base <https://search.nfdi4chem.de/dataset/> .
@prefix SIO: <http://semanticscience.org/resource/SIO_> .
@prefix RXNO: <http://purl.obolibrary.org/obo/RXNO_> .
@prefix RO: <http://purl.obolibrary.org/obo/RO_> .
@prefix BFO: <http://purl.obolibrary.org/obo/BFO_> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

# The ReactionMonitoringDataset
<https://doi.org/10.14272/reaction/SA-FUHFF-UHFFFADPSC-MTSVGCFANK-...> a dcat:Dataset ;
    dcterms:title "Dataset for Chemotion Repository synthesis CRR-56408" ;
    dcterms:subject <https://www.chemotion-repository.net/pid/56408> ;
    theme:
        - preferred_label:
            - "Science and technology" ;
    prov:wasGeneratedBy <https://doi.org/10.14272/reaction/SA-FUHFF-UHFFFADPSC-MTSVGCFANK-UHFFFADPSC-NUHFF-NUHFF-NUHFF-ZZZ#Monitoring> .

# The ReactionMonitoring - references the reaction
<https://doi.org/10.14272/reaction/SA-FUHFF-UHFFFADPSC-MTSVGCFANK-UHFFFADPSC-NUHFF-NUHFF-NUHFF-ZZZ#Monitoring> a prov:Activity ;
    dcterms:title "Monitoring of the Chemotion Repo synthesis CRR-56408" ;
    prov:wasInformedBy <https://www.chemotion-repository.net/pid/56408> .

# The ChemicalReaction - full description
<https://www.chemotion-repository.net/pid/56408> a RXNO:0000329, SIO:010345 ;
    dcterms:title "Chemotion Repository synthesis CRR-56408" ;
    dcterms:description "The reaction has been conducted in dry glass ware under argon atmosphere. ..."
    schema:duration "PT22H"^^xsd:duration ;
    # Starting materials and reactants via 'has_starting_material' and 'has_reactant' which are both mapped to RO's 'has primary input'
    RO:0004009 <https://www.chemotion-repository.net/pid/56408_Reactant-1>,
        <https://www.chemotion-repository.net/pid/56408_Reactant-2>,
        <https://www.chemotion-repository.net/pid/56408_Reactant-3>,
        <https://www.chemotion-repository.net/pid/56408_StartMat-1>,
        <https://www.chemotion-repository.net/pid/56408_StartMat-2> ;
    # Product via 'has_product', which is mapped to RO's 'has primary output'
    RO:0004008 <https://dx.doi.org/10.14272/MTSVGCFANKMACF-UHFFFAOYSA-N.1> ;
    # AgenticEntites via DCAT-AP+ predicate
    prov:wasAssociatedWith <https://www.chemotion-repository.net/pid/56408_Reactor-1>,
        <https://www.chemotion-repository.net/pid/56408_Solvent-1>,
        <https://www.chemotion-repository.net/pid/56408_Solvent-2>,
        <https://www.chemotion-repository.net/pid/56408_Solvent-3>,
        <https://www.chemotion-repository.net/pid/56408_Solvent-4>,
        <https://www.chemotion-repository.net/pid/56408_Solvent-5>,
        <https://www.chemotion-repository.net/pid/56408_Solvent-6> .
    # Yield
    SIO:000008 [ a CHMO:0002855 ;
            dcterms:title "Yield [%]" ;
            dcterms:type VOC4CAT:0005005 ;
            qudt:hasQuantityKind <http://qudt.org/vocab/quantitykind/Dimensionless> ;
            qudt:unit <http://qudt.org/vocab/unit/PERCENT> ;
            prov:value "86.0"^^xsd:float ] ;
    # Reaction steps (chemical transformations) via has_reaction_step, which is mapped to BFO's 'has part' 
    BFO:0000051 <https://www.chemotion-repository.net/pid/56408#step-1>,
        <https://www.chemotion-repository.net/pid/56408#step-3> ;
    # All steps including work-up and purification via the 'has part' slot inherited from the Activity class
    dcterms:hasPart <https://www.chemotion-repository.net/pid/56408#step-1>,
        <https://www.chemotion-repository.net/pid/56408#step-2>,
        <https://www.chemotion-repository.net/pid/56408#step-3>,
        <https://www.chemotion-repository.net/pid/56408#step-4>,
        <https://www.chemotion-repository.net/pid/56408#step-5> ;
```

Notice how the YAML-to-RDF mapping works:

- `is_about_activity` becomes `dcterms:subject` → the Dataset links to the ChemicalReaction.
- `was_generated_by` becomes `prov:wasGeneratedBy` → the Dataset links to the ReactionMonitoring.
- `evaluated_activity` becomes `prov:wasInformedBy` → the ReactionMonitoring references the ChemicalReaction.
- `has_reaction_step` becomes `BFO:0000051` (has part) → only chemical reaction steps.
- `has_part` becomes `dcterms:hasPart` → all steps including non-reaction activities.
- Reaction participants use domain-specific predicates: `RO:0004009` for inputs, `RO:0004008` for outputs, `prov:wasAssociatedWith` for agents.


### A substance sample characterization dataset

This is a real example from the [Chemotion Repository](https://www.chemotion-repository.net/pid/50438), showing an HSQC NMR measurement of a chemical substance sample. The source file is part of ChemDCAT-AP's validation test suite: [`tests/data/valid/SubstanceSampleCharacterizationDataset-001.yaml`](https://github.com/nfdi-de/chem-dcat-ap/blob/main/tests/data/valid/SubstanceSampleCharacterizationDataset-001.yaml). Every CI run validates this file against the schema.

Note how the `SubstanceSampleCharacterization` activity uses the generic DCAT-AP+ attribute and agent slots (`has_qualitative_attribute`, `has_quantitative_attribute`, `carried_out_by`) rather than chemistry-specific sub-slots. This is deliberate: `SubstanceSampleCharacterization` is a [coarse-grained convenience shape](dataset-activity-shapes.md) that leaves method-specific structuring to sub-profiles like [NMR-DCAT-AP](https://nfdi4chem.github.io/nmr-dcat-ap).

```yaml
# A SubstanceSampleCharacterizationDataset
id: doi:10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N/CHMO0000604
other_identifier:
  - notation: https://www.chemotion-repository.net/pid/50438
title:
  - "heteronuclear single quantum coherence (HSQC) dataset"
description:
  - "Dataset analysing Sample ID: CRS-50440 with heteronuclear single quantum
     coherence (HSQC) NMR spectroscopy"
theme:
  - preferred_label:
      - "Science and technology"

# Dual link: the Dataset is directly about the SubstanceSample
is_about_entity:
  - id: doi:10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N.2
    title: "CRS-50440"
    description: "The analysed chemical substance sample CRS-50440."
    rdf_type:
      id: CHEBI:59999
      title: "chemical substance"
    composed_of:
      - id: doi:10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N.2#EvaluatedCompound
        description: "compound assigned to doi:10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N.2"
        other_identifier:
          - notation: https://pubchem.ncbi.nlm.nih.gov/compound/26248854
        inchikey:
          - value: "KVOIVNBYNQXCNY-BOCHJOTCSA-N"
            title: "assigned InChiKey"
        inchi:
            value: "InChI=1S/C11H12N2S/c1-12-7-10-8-14-11(13-10)9-5-3-2-4-6-9/..."
            title: "assigned InChi"
        smiles:
          - value: "CNCc1csc(n1)c1ccccc1"
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
            description: "Molar mass as specified in the Chemotion repository."
          - has_quantity_type: http://qudt.org/vocab/quantitykind/MolarMass
            unit: https://qudt.org/vocab/unit/GM-PER-MOL
            value: 204.29
            description: "Molar mass as specified in PubChem"

# The SubstanceSampleCharacterization activity that produced this dataset
was_generated_by:
  - id: doi:10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N/CHMO0000604#X27932
    description:
      - "heteronuclear single quantum coherence (HSQC) NMR spectroscopy."
    title: X27932
    evaluated_entity:
      - id: doi:10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N.2
        title: "CRS-50440"
    # Generic DCAT-AP+ attribute and agent slots are used here.
    # Sub-profiles like NMR-DCAT-AP should define more granular shapes.
    has_qualitative_attribute:
      - rdf_type:
          id: NMR:1400037
          title: "NMR pulse sequence"
        value: hsqcedetgp
        description: "used pulse program"
    has_quantitative_attribute:
      - rdf_type:
          id: NMR:1400025
          title: "sample temperature in magnet"
        description: "used sample temperature setting"
        has_quantity_type: http://qudt.org/vocab/quantitykind/Temperature
        unit: https://qudt.org/vocab/unit/K
        value: 300.1
      - rdf_type:
          id: NMR:1400087
          title: "number of scans"
        value: 2
        has_quantity_type: http://qudt.org/vocab/quantitykind/Count
        unit: http://qudt.org/vocab/unit/NUM
        description: "used number of scans"
    carried_out_by:
      - id: doi:10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N/CHMO0000604#X27932_NMR_Spectrometer
        rdf_type:
          id: NMR:1000371
          title: "AVANCE III HD"
        title: "Avance III 400 NMR spectrometer"
        description: "used NMR spectrometer"
      - id: doi:10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N/CHMO0000604#X27932_NMR_Solvent
        description: "used solvent"
        rdf_type:
          id: NCIT:C45790
          title: Solvent
        has_part:
          - id: https://pubchem.ncbi.nlm.nih.gov/compound/71583
            rdf_type:
              id: CHEBI:85365
              title: "deuterated chloroform"
            title: "chloroform-D1 (CDCl3)"
```

Key structural points:

- This is a `SubstanceSampleCharacterizationDataset`: `was_generated_by` points to a `SubstanceSampleCharacterization` and `is_about_entity` points to a `SubstanceSample`.
- The `SubstanceSample` uses `rdf_type: CHEBI:59999` for additional typing beyond its schema-level `class_uri: SIO:001378`. This is the [ClassifierMixin](https://nfdi-de.github.io/dcat-ap-plus/latest/design-patterns/#pattern-3-flexible-classification-classifiermixin) providing multi-typing.
- The `SubstanceSampleCharacterization` activity uses generic DCAT-AP+ slots for its method-specific attributes (pulse program, temperature, scan count) and agents (spectrometer, solvent). This is intentional: the convenience shape is under-specified, leaving method-specific structuring to sub-profiles.
- The `evaluated_entity` on the activity and `is_about_entity` on the dataset both point to the same `SubstanceSample`, implementing the [dual linking pattern](https://nfdi-de.github.io/dcat-ap-plus/latest/design-patterns/#dual-linking-dataset-subject-matter).

### Converting YAML to RDF

The above YAML is converted to Turtle using `linkml-convert`:

```bash
uv run linkml-convert -t ttl \
  tests/data/valid/SubstanceSampleCharacterizationDataset-001.yaml \
  -s src/chem_dcat_ap/schema/chem_dcat_ap.yaml \
  -P "_base=https://search.nfdi4chem.de/dataset/" \
  -C SubstanceCharacterizationDataset
```

The flags:

- `-t ttl`: output format is Turtle
- `-s`: path to the ChemDCAT-AP schema
- `-P "_base=..."`: sets the RDF base URI (so relative `id` values resolve correctly)
- `-C SubstanceCharacterizationDataset`: the target class (tells the converter which shape to convert against)

This produces the following Turtle (abbreviated for readability):

```turtle
@base <https://search.nfdi4chem.de/dataset/> .
@prefix AFR: <http://purl.allotrope.org/ontologies/result#AFR_> .
@prefix BFO: <http://purl.obolibrary.org/obo/BFO_> .
@prefix SIO: <http://semanticscience.org/resource/SIO_> .
@prefix CHEBI: <http://purl.obolibrary.org/obo/CHEBI_> .
@prefix CHEMINF: <http://semanticscience.org/resource/CHEMINF_> .
@prefix CHMO: <http://purl.obolibrary.org/obo/CHMO_> .
@prefix NMR: <http://nmrML.org/nmrCV#NMR:> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix NCIT: <http://purl.obolibrary.org/obo/NCIT_> .
@prefix schema: <http://schema.org/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix adms: <http://www.w3.org/ns/adms#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix qudt: <http://qudt.org/schema/qudt/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

# The Dataset
<https://doi.org/10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N/CHMO0000604> a dcat:Dataset ;
    dcterms:description "Dataset analysing Sample ID: CRS-50440 with heteronuclear single quantum coherence (HSQC) NMR spectroscopy" ;
    dcterms:subject <https://doi.org/10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N.2> ; # Linking to the evaluated entity
    dcterms:title "heteronuclear single quantum coherence (HSQC) dataset" ;
    adms:identifier [ a adms:Identifier ;
            skos:notation "https://www.chemotion-repository.net/pid/50438" ] ;
    dcat:theme [ a skos:Concept ;
            skos:prefLabel "Science and technology" ] ;
    prov:wasGeneratedBy <https://doi.org/10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N/CHMO0000604#X27932> .

# The SubstanceSample (dual-typed: SIO:001378 from class_uri + CHEBI:59999  from rdf_type)
<https://doi.org/10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N.2> a CHEBI:59999, SIO:001378 ;
    dcterms:description "The analysed chemical substance sample CRS-50440." ;
    dcterms:title "CRS-50440" ;
    BFO:0000051 <https://doi.org/10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N.2#EvaluatedCompound> .

# The ChemicalEntity with structure descriptors and quantitative attributes (all via SIO:000008)
<https://doi.org/10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N.2#EvaluatedCompound> a CHEBI:23367 ;
    dcterms:description "compound assigned to doi:10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N.2" ;
    SIO:000008 [ a CHEMINF:000059 ; prov:value "KVOIVNBYNQXCNY-BOCHJOTCSA-N" ],
               [ a CHEMINF:000018 ; prov:value "CNCc1csc(n1)c1ccccc1" ],
               [ a CHEMINF:000042 ; prov:value "C11H12N2S" ],
               [ a AFR:0002409 ;
                 dcterms:description "Molar mass as specified in PubChem" ;
                 qudt:hasQuantityKind <http://qudt.org/vocab/quantitykind/MolarMass> ;
                 prov:value "204.072119"^^xsd:float ] .

# The SubstanceSampleCharacterization activity (generic DCAT-AP+ predicates & dual-typed: CHMO:0000604 from rdf_type)
<https://doi.org/10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N/CHMO0000604#X27932> a CHMO:0000604, prov:Activity ;
    dcterms:description "heteronuclear single quantum coherence (HSQC) NMR spectroscopy." ;
    dcterms:relation [ a NMR:1400087, qudt:Quantity ;  # dual-typed: NMR:1400087 from rdf_type
            dcterms:description "used number of scans" ;
            qudt:hasQuantityKind <http://qudt.org/vocab/quantitykind/Count> ;
            qudt:unit <http://qudt.org/vocab/unit/NUM> ;
            prov:value "2.0"^^xsd:float ],
        [ a NMR:1400037, prov:Entity ; # dual-typed: NMR:1400037 from rdf_type
            dcterms:description "used pulse program" ;
            prov:value "hsqcedetgp" ],
        [ a NMR:1400025, qudt:Quantity ; # dual-typed: NMR:1400025 from rdf_type
            dcterms:description "used sample temperature setting" ;
            qudt:hasQuantityKind <http://qudt.org/vocab/quantitykind/Temperature> ;
            qudt:unit <https://qudt.org/vocab/unit/K> ;
            prov:value "300.1"^^xsd:float ] ;
    dcterms:title "X27932" ;
    # Linking to the evaluated SubstanceSample 
    prov:used <https://doi.org/10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N.2> ;
    # Linking to the agents involved 
    prov:wasAssociatedWith <https://doi.org/10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N/CHMO0000604#X27932_NMR_Solvent>,
        <https://doi.org/10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N/CHMO0000604#X27932_NMR_Spectrometer> .

<https://doi.org/10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N/CHMO0000604#X27932_NMR_Solvent> a NCIT:C45790, prov:Agent ;
    dcterms:description "used solvent" ;
    dcterms:hasPart <https://pubchem.ncbi.nlm.nih.gov/compound/71583> .

<https://doi.org/10.14272/UGRXAOUDHZOHPF-UHFFFAOYSA-N/CHMO0000604#X27932_NMR_Spectrometer> a NMR:1000371, prov:Agent ;
    dcterms:description "used NMR spectrometer" ;
    dcterms:title "Avance III 400 NMR spectrometer" .

# `DefinedTerm` instances (ontology classes) used for additional typing
NMR:1000371 a schema:DefinedTerm ;
    schema:name "AVANCE III HD" .
NMR:1400025 a schema:DefinedTerm ;
    schema:name "sample temperature in magnet" .
NMR:1400037 a schema:DefinedTerm ;
    schema:name "NMR pulse sequence" .
NMR:1400087 a schema:DefinedTerm ;
    schema:name "number of scans" .
CHEBI:59999 a schema:DefinedTerm ;
    schema:name "chemical substance" .
CHEBI:85365 a schema:DefinedTerm ;
    schema:name "deuterated chloroform" .
CHMO:0000604 a schema:DefinedTerm ;
    schema:name "heteronuclear single quantum coherence" .
NCIT:C45790 a schema:DefinedTerm ;
    schema:name "Solvent" .
```

Notice how the YAML-to-RDF mapping works:

- `class_uri` determines `rdf:type`: `SubstanceSample` becomes `SIO:001378`, `ChemicalEntity` becomes `CHEBI:23367`. The `rdf_type` slot adds *additional* types (e.g. `CHEBI:59999`).
- `slot_uri` determines RDF predicates: `composed_of` becomes `BFO:0000051`, structure descriptors become `SIO:000008`, generic attributes become `dcterms:relation`, agents become `prov:wasAssociatedWith`.
- `DefinedTerm` instances (from `rdf_type`, `has_quantity_type`, `unit`) become typed resources with `schema:name` for the title.
- CURIEs expand via the prefix map: `doi:10.14272/...` becomes `https://doi.org/10.14272/...`.

For the full documentation of these shapes and when to use them vs. defining your own, see [Dataset and activity shapes](dataset-activity-shapes.md).

## Key types for serialization

When building a serializer, you need to know which fields expect which data types:

| Field                              | Type                                                              | Example                                                    |
|------------------------------------|-------------------------------------------------------------------|------------------------------------------------------------|
| `id`                               | URI or CURIE                                                      | `https://example.org/sample-001` or `doi:10.14272/...`     |
| `value` on `QuantitativeAttribute` | `float`                                                           | `300.0`                                                    |
| `value` on `QualitativeAttribute`  | `string`                                                          | `"UGRXAOUDHZOHPF-UHFFFAOYSA-N"`                            |
| `has_quantity_type`                | `DefinedTerm` (object with `id` and optional `title` & `from_CV`) | `{"id": "http://qudt.org/vocab/quantitykind/Temperature"}` |
| `unit`                             | `DefinedTerm`                                                     | `{"id": "https://qudt.org/vocab/unit/K"}`                  |
| `rdf_type`                         | `DefinedTerm`                                                     | `{"id": "CHMO:0000595", "title": "..."}`                   |
| `type`                             | `DefinedTerm`                                                     | `{"id": "http://example.org/vocab/...", "title": "..."}`   |
| `has_duration`                     | `xsd:duration` string                                             | `"PT22H"`, `"P2D"`, `"PT1H30M"`                            |
| `has_physical_state`               | enum value                                                        | `"SOLID"`, `"LIQUID"`, `"GASEOUS"`, `"PLASMA"`             |

`DefinedTerm` is a lightweight object for referencing ontology classes or vocabulary concepts. At minimum it needs an `id` (the URI or CURIE of the term). `title` is optional but recommended for human readability.

## Where to find valid QUDT URIs

Every `QuantitativeAttribute` needs a `has_quantity_type` (what kind of quantity) and a `unit` (what unit it's measured in). Both are expected to be QUDT URIs (validation not yet implemented → see above warning):

- **Quantity kinds**: browse at [qudt.org/vocab/quantitykind/](http://qudt.org/vocab/quantitykind/). Common ones: `Temperature`, `Mass`, `Volume`, `Pressure`, `AmountOfSubstance`, `Density`, `MolarMass`, `Dimensionless`.
- **Units**: browse at [qudt.org/vocab/unit/](http://qudt.org/vocab/unit/). Common ones: `K`, `DEG_C`, `GM`, `MilliGM`, `L`, `MilliL`, `MOL`, `MilliMOL`, `BAR`, `GM-PER-MOL`, `PERCENT`.

## Development workflow and CI

The ChemDCAT-AP repository uses [just](https://github.com/casey/just) as a command runner. The key recipes for developers:

| Command            | What it does                                                                                       |
|--------------------|----------------------------------------------------------------------------------------------------|
| `just install`     | Install project dependencies via `uv sync`                                                         |
| `just gen-project` | Generate all artifacts: JSON Schema, SHACL, OWL, Python dataclasses, Pydantic models               |
| `just test`        | Run the full test suite: schema generation, Python unit tests, and validation of all example files |
| `just testdoc`     | Build and serve the documentation locally via MkDocs                                               |

The test pipeline (`just test`) validates every YAML file in `tests/data/` against the schema and converts them to JSON and YAML output. Files in `tests/data/invalid/` are expected to fail validation. This runs on every push to a PR, so only PRs that pass the full suite are merged.

If you want to try the examples locally:

```bash
git clone https://github.com/nfdi-de/chem-dcat-ap.git
cd chem-dcat-ap
just install
just test
```

## Further reading

- [LinkML documentation](https://linkml.io/linkml/) for the schema language
- [DCAT-AP+ documentation](https://nfdi-de.github.io/dcat-ap-plus/) for the base patterns (provenance core, QuantitativeAttribute, ClassifierMixin)
- [DCAT-AP+ extension rules](https://nfdi-de.github.io/dcat-ap-plus/latest/how-to-extend/) if you need to extend ChemDCAT-AP further
- [QUDT catalog](https://www.qudt.org/) for quantity kinds and units
