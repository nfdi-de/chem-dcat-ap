# Implementations and Downstream Profiles

## Production deployment

### NFDI4Chem Search Service

[:octicons-globe-16: search.nfdi4chem.de](https://search.nfdi4chem.de/)

ChemDCAT-AP is currently being implemented in the NFDI4Chem Search Service, a [CKAN](https://ckan.org/)-based registry of NFDI4Chem's federation of data repositories. A custom profile for the [`ckanext-dcat`](https://github.com/ckan/ckanext-dcat) plugin enables the service to parse and export ChemDCAT-AP-compliant metadata. The auto-generated Python data classes generated from its LinkML model validate and transform metadata harvested from the source repositories into a standardized RDF graph.

This powers the **NFDI Chemistry Knowledge Graph** (ChemKG), enabling faceted SPARQL search queries that are impossible with generic catalog metadata. For example, finding all datasets where a specific solvent was used or that analyze a compound with a given InChIKey.

### Repo4Cat (NFDI4Cat Central Data Repository)
 
[:octicons-globe-16: repository.nfdi4cat.org](https://repository.nfdi4cat.org) · [:octicons-repo-16: nfdi4cat/repo4cat](https://github.com/nfdi4cat/repo4cat)
 
The NFDI4Cat Central Data Repository is a [Dataverse](https://dataverse.org/)-based platform for sharing catalysis research data. It is the target deployment for [CoreMeta4Cat](#coremeta4cat), NFDI4Cat's catalysis-specific profiles built on ChemDCAT-AP. Integration of ChemDCAT-AP-derived metadata into the Repo4Cat cataloging workflow is under development.

### Chemotion Repository

[:octicons-globe-16: chemotion-repository.net](https://www.chemotion-repository.net/)

The [Chemotion Repository](https://www.chemotion-repository.net/) is currently the primary data source validated against ChemDCAT-AP. All relevant metadata fields from Chemotion records have been successfully mapped to the ChemDCAT-AP schema. The test data used in the schema's CI pipeline comes from real Chemotion records (e.g., substance samples, chemical reactions with full stoichiometry and conditions). The implementation of ChemDCAT-AP more directly in Chemotion is currently being investigated.

---

## Downstream profiles

ChemDCAT-AP is designed to be imported and further specialized by domain-specific sub-profiles. These profiles add third-layer shapes on top of ChemDCAT-AP's chemistry classes, following the same [extension rules](https://nfdi-de.github.io/dcat-ap-plus/latest/how-to-extend/) that ChemDCAT-AP follows for DCAT-AP+. See the [Adoption guide: Extending ChemDCAT-AP](guidance.md#extending-chemdcat-ap-further) for practical guidance.

### NMR-DCAT-AP

[:octicons-repo-16: NFDI4Chem/nmr-dcat-ap](https://github.com/NFDI4Chem/nmr-dcat-ap) · [:octicons-book-16: Documentation](https://nfdi4chem.github.io/nmr-dcat-ap/)

NMR-DCAT-AP extends ChemDCAT-AP to formalize the [MARGARITAS](https://doi.org/10.25504/FAIRsharing.c29400) minimum information standard for NMR spectroscopy. It demonstrates the three-layer architecture: DCAT-AP+ -> ChemDCAT-AP -> NMR-DCAT-AP. Currently in beta.

The NMR-DCAT-AP development was able to capture richer metadata than is currently exposed via the Chemotion repository API. Details like calibration compound and probed nucleus, while present in raw data files or landing pages, could be structured for the first time using this model. The workflow now serves as a validated template for encoding other MIChI (Minimum Information for a Chemical Investigation) standards.

### CoreMeta4Cat

[:octicons-repo-16: nfdi4cat/CoreMeta4Cat](https://github.com/nfdi4cat/CoreMeta4Cat) · [:octicons-book-16: Documentation](https://nfdi4cat.github.io/CoreMeta4Cat/)

NFDI4Cat's catalysis-specific profiles, which import ChemDCAT-AP as the primary base for further domain-specific extensions for catalysis research data. Currently under development.

---

## Planned integrations

### Metadata Schema Service (MSS)

ChemDCAT-AP is a cornerstone for the planned Metadata Schema Service within the second funding phase of NFDI4Chem. The MSS will host chemistry-specific and other relevant schemas, provide mappings and automated transformations between them, and integrate with the [EOSC Metadata Schema and Crosswalk Registry (MSCR)](https://faircore4eosc.eu/eosc-core-components/metadata-schema-and-crosswalk-registry-mscr). The multiple code representations generated from the LinkML model (Python/Pydantic, JSON Schema, SHACL) are suited for this purpose.

### NFDIcore alignment

We are collaborating with the developers of the [NFDIcore ontology](https://nfdi.fiz-karlsruhe.de/ontology/) to explore mapping ChemDCAT-AP schema elements to NFDIcore classes and predicates. NFDIcore is a BFO-aligned ontology that provides narrower, more precisely scoped terms matching the intent of several DCAT-AP+ node shapes. Because ChemDCAT-AP uses LinkML's `class_uri` and `slot_uri` for ontology alignment, swapping the underlying ontology mappings does not require restructuring the schema. See [Ontology alignment](ontology-alignment.md) for details.

---

## Building your own profile

If your subdomain is not covered above, you can build a profile that imports ChemDCAT-AP. The [Adoption guide](guidance.md#extending-chemdcat-ap-further) provides a conformance checklist and anti-patterns to avoid. The [Dataset and activity shapes](dataset-activity-shapes.md) page documents the coarse-grained convenience shapes you can reuse or replace with more granular alternatives.

To allow us linking to your sub-profile, tag your GitHub repository with `chemdcatap`, `dcatapplus`, and `linkml`.

## Using ChemDCAT-AP?

If you are building on ChemDCAT-AP or using it in your infrastructure, we welcome additions to this page and other constructive feedback. Please, feel free to open an [issue](https://github.com/nfdi-de/chem-dcat-ap/issues) or pull request.

For the broader set of projects using the underlying DCAT-AP+ framework, see [DCAT-AP+ Projects](https://nfdi-de.github.io/dcat-ap-plus/latest/dcat-ap-plus-users/).
