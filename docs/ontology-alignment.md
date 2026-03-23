# Ontology alignment

ChemDCAT-AP maps every class and slot to established ontology terms via `class_uri` and `slot_uri`. This page documents the ontology choices, the `slot_uri` replacement strategy, and the rationale for BFO alignment.

## Ontologies used

| Prefix    | Ontology                                                                                            | Used for                                                                                                                                                                                                             |
|-----------|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *CHEBI*   | [Chemical Entities of Biological Interest](https://terminology.nfdi4chem.de/ts/ontologies/chebi)    | Chemical entity types (`ChemicalEntity`, `Atom`)                                                                                                                                                                     |
| *CHEMINF* | [Chemical Information Ontology](https://terminology.nfdi4chem.de/ts/ontologies/cheminf)             | Structure descriptors (`InChi`, `SMILES`, `MolecularFormula`, `IUPACName`, `InChIKey`). Also used in PubChemRDF alongside SIO.                                                                                       |
| *CHMO*    | [Chemical Methods Ontology](https://terminology.nfdi4chem.de/ts/ontologies/chmo)                    | Analytical methods, concentration (`Concentration`), yield (`Yield`)                                                                                                                                                 |
| *SIO*     | [Semanticscience Integrated Ontology](https://terminology.nfdi4chem.de/ts/ontologies/sio)           | Chemical processes and substances (`ChemicalReaction`, `Reagent`, `Catalyst`, `DissolvingSubstance`, `SubstanceSample`), attribute predicate (`SIO:000008`), pH, density. Also used in PubChemRDF alongside CHEMINF. |
| *OBI*     | [Ontology for Biomedical Investigations](https://terminology.nfdi4chem.de/ts/ontologies/obi)        | `MaterialSample`                                                                                                                                                                                                     |
| *BFO*     | [Basic Formal Ontology](https://terminology.nfdi4chem.de/ts/ontologies/bfo)                         | `MaterialEntity`, parthood (`BFO:0000051`)                                                                                                                                                                           |
| *IAO*     | [Information Artifact Ontology](https://terminology.nfdi4chem.de/ts/ontologies/iao)                 | Information content entity concept; identifier class (`IAO:0020000`) used for reaction identifiers (e.g. RInChI) without a dedicated CHEMINF class                                                                   |
| *PATO*    | [Phenotype And Trait Ontology](https://terminology.nfdi4chem.de/ts/ontologies/pato)                 | Physical states, close mappings for physical quantities                                                                                                                                                              |
| *QUDT*    | [Quantities, Units, Dimensions, Types](https://www.qudt.org/pages/QUDToverviewPage.html)            | Quantity classes (`Temperature`, `Mass`, `Volume`, `Pressure`, etc.), quantity kinds, units                                                                                                                          |
| *RO*      | [OBO Relations Ontology](https://terminology.nfdi4chem.de/ts/ontologies/ro)                         | Reaction input/output (`RO:0004009`, `RO:0004008`)                                                                                                                                                                   |
| *RXNO*    | [Named Reaction Ontology](https://terminology.nfdi4chem.de/ts/ontologies/rxno)                      | Reaction types, catalyst role (`RXNO:0000425`)                                                                                                                                                                       |
| *MOP*     | [Molecular Process Ontology](https://terminology.nfdi4chem.de/ts/ontologies/mop)                    | Molecular process types (exact mapping)                                                                                                                                                                              |
| *PROCO*   | [Process Chemistry Ontology](https://terminology.nfdi4chem.de/ts/ontologies/proco)                  | Starting material (`PROCO:0000029`)                                                                                                                                                                                  |
| *NCIT*    | [NCI Thesaurus OBO Edition](https://terminology.nfdi4chem.de/ts/ontologies/ncit)                    | Product, catalyst, reagent, pH (exact/close mappings)                                                                                                                                                                |
| *VOC4CAT* | [Voc4Cat - A SKOS vocabulary for Catalysis](https://terminology.nfdi4chem.de/ts/ontologies/voc4cat) | Catalysis-specific terms (exact mappings)                                                                                                                                                                            |
| *AFE/AFR* | [Allotrope Foundation Ontology](https://terminology.nfdi4chem.de/ts/ontologies/afo)                 | Equipment (`Reactor`), molar mass, concentration (exact mappings)                                                                                                                                                    |
| *ENVO*    | [The Environment Ontology](https://terminology.nfdi4chem.de/ts/ontologies/envo)                     | `Laboratory` (`ENVO:01001405`)                                                                                                                                                                                       |

## The `slot_uri` replacement strategy

DCAT-AP+ assigns intentionally generic predicates to its slots. The Dublin Core Terms predicates (`dcterms:relation`, `dcterms:hasPart`) are semantically weak by design, chosen as the lowest common denominator that avoids conflicting with domain-specific vocabularies. The PROV-O predicates (`prov:used`, `prov:generated`, `prov:wasAssociatedWith`) are well-defined within the provenance model but carry no domain-specific semantics: `prov:used` does not distinguish a starting material from a reactant, and `prov:wasAssociatedWith` does not distinguish a catalyst from a solvent.

| DCAT-AP+ slot                | Default `slot_uri`       |
|------------------------------|--------------------------|
| `has_quantitative_attribute` | `dcterms:relation`       |
| `has_qualitative_attribute`  | `dcterms:relation`       |
| `had_input_entity`           | `prov:used`              |
| `had_output_entity`          | `prov:generated`         |
| `carried_out_by`             | `prov:wasAssociatedWith` |
| `has_part`                   | `dcterms:hasPart`        |

When ChemDCAT-AP creates a sub-slot (via `is_a`), it may assign a different, semantically richer `slot_uri` that replaces the parent's predicate in the generated RDF. This is a valid specialization per the [DCAT-AP+ extension rules](https://nfdi-de.github.io/dcat-ap-plus/how-to-extend/), but it has interoperability implications. The following table summarizes all replacements; the subsections below document the rationale for each.

| ChemDCAT-AP sub-slot(s) | Parent slot | Parent `slot_uri` | Replacement `slot_uri` |
|---|---|---|---|
| `has_temperature`, `has_mass`, `inchi`, `smiles`, `has_concentration`, `has_yield`, etc. | `has_quantitative/qualitative_attribute` | `dcterms:relation` | `SIO:000008` (has attribute) |
| `used_starting_material`, `used_reactant` | `had_input_entity` | `prov:used` | `RO:0004009` (has input) |
| `generated_product` | `had_output_entity` | `prov:generated` | `RO:0004008` (has output) |
| `used_catalyst` | `carried_out_by` | `prov:wasAssociatedWith` | `RXNO:0000425` (has catalyst) |
| `has_part` (on MaterialEntity), `composed_of`, `has_reaction_step` | `has_part` | `dcterms:hasPart` | `BFO:0000051` (has part) |
| `used_solvent`, `used_reactor` | `carried_out_by` | `prov:wasAssociatedWith` | *(not replaced)* |

!!! info "Planned: formal projection queries"
    We plan to provide a complete set of SPARQL CONSTRUCT queries covering all predicate replacements listed above, with worked examples from the ChemDCAT-AP test data. These will allow any triplestore hosting ChemDCAT-AP data to materialize the DCAT-AP+ base predicates alongside the domain-specific ones, ensuring backward-compatible querying without losing semantic precision.

### SIO:000008 as the chemistry attribute predicate

All ChemDCAT-AP attribute sub-slots (`has_temperature`, `has_mass`, `inchi`, `smiles`, `has_concentration`, `has_yield`, etc.) use `slot_uri: SIO:000008` (has attribute) instead of the DCAT-AP+ default `dcterms:relation`. The rationale:

- `dcterms:relation` is maximally generic and says nothing about the nature of the relationship.
- `SIO:000008` is a well-established predicate in the Semanticscience Integrated Ontology that means "has attribute." It is semantically more appropriate for linking an entity to its characteristics.
- SIO is already used elsewhere in ChemDCAT-AP for class mappings (`ChemicalReaction`, `Catalyst`, etc.), so adding it as a predicate does not introduce a new dependency.

### RO predicates for reaction inputs/outputs

The reaction participant slots use OBO Relations Ontology predicates instead of the PROV-O defaults:

| ChemDCAT-AP slot | Replaces | New `slot_uri` | Meaning |
|---|---|---|---|
| `used_starting_material` | `had_input_entity` (`prov:used`) | `RO:0004009` | has input |
| `used_reactant` | `had_input_entity` (`prov:used`) | `RO:0004009` | has input |
| `generated_product` | `had_output_entity` (`prov:generated`) | `RO:0004008` | has output |

`RO:0004009` (has input) and `RO:0004008` (has output) are process-to-entity relations from the OBO Relations Ontology. They are more specific than `prov:used` and `prov:generated` and align with OBO Foundry practices.

### RXNO for catalyst association

The `used_catalyst` slot uses `slot_uri: RXNO:0000425` (has catalyst) from the RXNO Ontology, replacing the parent `carried_out_by`'s `prov:wasAssociatedWith`. This predicate precisely captures the catalytic role. `used_solvent` and `used_reactor` keep the parent's `prov:wasAssociatedWith` because there currently is no established predicate that provides equivalent precision for these roles.

### BFO:0000051 for parthood

`has_part` on `MaterialEntity`, `ChemicalEntity`, `composed_of`, and `has_reaction_step` uses `slot_uri: BFO:0000051` (has part), replacing the DCAT-AP+ default `dcterms:hasPart`. BFO's parthood relation carries formal mereological axioms (transitivity, reflexivity) that `dcterms:hasPart` does not.

### Interoperability implications

When a ChemDCAT-AP instance is serialized to RDF, the triples use the domain-specific predicates (`SIO:000008`, `RO:0004009`, etc.), not the DCAT-AP+ defaults (`dcterms:relation`, `prov:used`, etc.). This means:

- A SPARQL query written against DCAT-AP+ predicates will **not** find ChemDCAT-AP data unless the query accounts for the replaced predicates.
- Conversely, a query written against ChemDCAT-AP predicates will find exactly the right data with higher precision.

To bridge both query patterns, use SPARQL CONSTRUCT rules that add DCAT-AP+ predicates alongside the domain-specific ones:

```sparql
CONSTRUCT {
  ?entity dcterms:relation ?attr .
}
WHERE {
  ?entity SIO:000008 ?attr .
}
```

This is the same approach recommended in the [DCAT-AP+ design patterns documentation](https://nfdi-de.github.io/dcat-ap-plus/latest/design-patterns/#for-slots-property-shapes-with-replaceable-predicates) for avoiding blank node duplication when projecting between vocabularies. Generate RDF from the domain-specific schema and use CONSTRUCT rules to add the generic predicates to the existing nodes.

## Why BFO alignment matters

Several of ChemDCAT-AP's ontology choices (CHEBI, OBI, RO, PATO) are part of the [OBO Foundry](https://obofoundry.org/), which is built on the [Basic Formal Ontology (BFO)](https://basic-formal-ontology.org/). This alignment has practical value:

- A [formal mapping between PROV-O and BFO](https://doi.org/10.1038/s41597-025-04580-1) has been published. This means ChemDCAT-AP data (which uses PROV-O via DCAT-AP+ and BFO-aligned terms via OBO ontologies) can be reasoned over coherently without manual bridging.
- OBO Foundry ontologies share a common upper-level structure, so terms from CHEBI, OBI, CHMO, and RO interoperate without custom alignment work.
- BFO's `material entity` (`BFO:0000040`) is the natural `class_uri` for `MaterialEntity`, and `BFO:0000051` (has part) is the established parthood relation in this ecosystem.

## Why SIO

The Semanticscience Integrated Ontology (SIO) is used in ChemDCAT-AP for both its `has attribute` predicate (`SIO:000008`) and several class mappings. Three reasons drove this choice.

### BFO-compatible upper level

SIO has its own upper-level structure, but it aligns naturally with BFO. SIO's three top-level branches under `entity` correspond to BFO's continuant subtypes, though not perfectly:

- `attribute` (with subtypes `quality` and `realizable entity`) corresponds to BFO's specifically dependent continuant (SDC) branch
- `object` groups together `material entity`, `information content entity`, and `spatial region`. In BFO, these are split: `material entity` and `spatial region` (via `immaterial entity`) fall under independent continuant, while `information content entity` is a generically dependent continuant (GDC), a sibling branch to both independent continuant and SDC
- `process` corresponds to BFO's occurrent/process branch

A formal OWL bridge module has not been published yet, but producing one would be a straightforward alignment task given this structural correspondence.

### Established prior art in PubChemRDF

SIO is used alongside CHEMINF in the [PubChemRDF](https://pubchem.ncbi.nlm.nih.gov/docs/rdf) graph ([Fu et al. 2015](https://doi.org/10.1186/s13321-015-0084-4)). The concrete overlap is the compound descriptor pattern: PubChemRDF links compounds to CHEMINF-typed descriptors via `SIO:000008` (has attribute), which is the same predicate and descriptor vocabulary ChemDCAT-AP uses for its chemical entity attribute slots (`inchi`, `smiles`, `molecular_formula`, etc.). This shared pattern means SPARQL queries over chemical descriptors can target both ChemDCAT-AP and PubChemRDF data using the same predicate and type assertions.

### Gap-filling for missing OBO classes

The SIO *classes* reused in ChemDCAT-AP (e.g., `SIO:010345` for chemical reaction, `SIO:010344` for catalyst) were chosen because no equivalent existed in OBO ontologies. Given SIO's BFO-similar upper level, their use was considered appropriate. If OBO equivalents are minted in the future, the `class_uri` mappings may change, but the SIO correspondence would be preserved via `exact_mappings` or `close_mappings` in the schema.

## Why most quantity classes map to `qudt:Quantity`

A glance at the schema shows that `Temperature`, `Mass`, `Volume`, `Pressure`, `AmountOfSubstance`, and others all carry `class_uri: qudt:Quantity`. This looks like a missed opportunity for more precise ontology mappings. It is, but the gap is not in ChemDCAT-AP; it is in the OBO/BFO ontology ecosystem.

The issue comes down to a BFO distinction between three layers:

1. **Qualities** (specifically dependent continuants in BFO): the physical property *inhering in* a material entity. PATO provides these: `PATO:0000146` (temperature), `PATO:0000125` (mass), `PATO:0000918` (volume), etc. In QUDT terms, these correspond to **QuantityKinds**.
2. **Information content entities (ICEs)**: a class from the OBO/BFO ecosystem (defined in the [Information Artifact Ontology, IAO](http://www.obofoundry.org/ontology/iao.html)) that represents an information artifact *about* a quality, i.e. the recorded measurement value as it appears in a dataset or lab notebook, not the physical property itself. In QUDT terms, this corresponds to a **Quantity** (a value + unit + quantity kind). This is what ChemDCAT-AP's attribute classes actually represent: a recorded value, not the quality itself.
3. **The QUDT model** collapses layers 1 and 2 into a single `qudt:Quantity` class that carries both the quantity kind reference and the numeric value.

The problem: OBO/BFO ontologies provide good coverage of layer 1 (PATO qualities) but almost no coverage of layer 2 (ICEs about those qualities). There is no established OBO class for "a recorded temperature measurement" as distinct from "the quality of temperature." Chris Mungall has created a [PATO-to-QUDT QuantityKinds SSSOM mapping](https://raw.githubusercontent.com/pato-ontology/pato/refs/heads/master/src/mappings/pato-to-qudt-quantitykind.sssom.tsv), which bridges layer 1 across the two ecosystems. But what ChemDCAT-AP needs for its `class_uri` values are layer 2 classes, and those mostly do not yet exist in the OBO world.

Four exceptions exist where a more precise class *is* available:

- **Density** is mapped to `SIO:001406`, an information content entity about density in SIO.
- **Yield** is mapped to `CHMO:0002855` (yield percentage), a CHMO class representing the recorded yield value.
- **Concentration** is mapped to `CHMO:0002820`, a CHMO class for concentration measurements.
- **Molar mass** is mapped to `AFR:0002409`, an Allotrope Foundation class for molar mass values.

These four demonstrate that precise mappings are possible when the right class exists in an established ontology. For the remaining quantities, ChemDCAT-AP maps to `qudt:Quantity` and uses `has_quantity_type` (pointing to QUDT QuantityKinds) to differentiate them. The PATO terms appear as `close_mappings` rather than `class_uri` values, because they represent the quality, not the information entity about the quality.

!!! tip "Future work"
    The long-term goal is to mint proper ICE classes for recorded quantity values in a suitable OBO ontology, allowing `class_uri` mappings that are both BFO-aligned and semantically precise. Until then, the QUDT mapping combined with `has_quantity_type` typing is the pragmatic solution, and the `close_mappings` to PATO terms preserve the link to the OBO ecosystem for future alignment.

## Known workarounds

### Duration on sub-steps

The DCAT-AP+ `has_duration` slot is only available on `EvaluatedActivity` and its subclasses (like `ChemicalReaction`). For sub-steps of a reaction that are modeled as generic `Activity` instances (dissolving, stirring, drop-wise addition), `has_duration` is not in scope. As a temporary workaround, these sub-steps express their duration using the generic `has_qualitative_attribute` slot with `type: schema:Duration` and an ISO 8601 value (e.g. `PT10M`). This is tracked in [DCAT-AP+ issue #69](https://github.com/nfdi-de/dcat-ap-plus/issues/69). Once `has_duration` is made available on `Activity`, the workaround will be replaced.

## Mapping annotations

ChemDCAT-AP uses LinkML's `exact_mappings`, `close_mappings`, `broad_mappings`, and `narrow_mappings` to document cross-ontology correspondences. These are documentation annotations, not formal OWL axioms. More mappings will be added over time, and it will be explored in how far they can be used to produce SSSOM mapping sets, which can then be transformed into OWL bridge modules using the [Ontology Development Kit (ODK)](https://github.com/INCATools/ontology-development-kit).

| Annotation        | Meaning                   | Use in ChemDCAT-AP                                                                                                              |
|-------------------|---------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| `exact_mappings`  | Equivalent semantics      | `ChemicalReaction` maps exactly to `MOP:0000543`, `REX:0000002`, `AFP:0003711`                                                  |
| `close_mappings`  | Similar but not identical | `Concentration` close to `PATO:0000033` (PATO captures the quality, not the measurement)                                        |
| `broad_mappings`  | Target is more general    | `SubstanceSampleCharacterization` broadly maps to `OBI:0000070` (assay), which covers more than just substance characterization |
| `narrow_mappings` | Target is more specific   | `ChemicalReaction` has narrow mapping to `RXNO:0000329` (a planned synthesis)                                                   |
