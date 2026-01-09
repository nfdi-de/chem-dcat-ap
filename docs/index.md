# ChemDCAT-AP

ChemDCAT-AP is a domain-specific extension of the EU standard 
[DCAT-AP](https://semiceu.github.io/DCAT-AP/releases/3.0.0/). 
It is based on the domain-agnostic DCAT-AP extension [DCAT-AP+](https://github.com/NFDI-de/dcat-ap-plus) , which allows a more detailed description of the 
process/activity that generated a `dcat:Dataset` compared to the standard DCAT-AP.

ChemDCAT-AP is designed to provide chemistry and catalysis-specific metadata for the chemical substances, reactions and 
analyses associated with a dataset in a more user-friendly way than DCAT-AP+. This is achieved by introducing specialized 
sub-classes and sub-properties that are already mapped to relevant domain ontologies.

## Key Features
- Extends [DCAT-AP+](https://github.com/NFDI-de/dcat-ap-plus) with chemistry and catalysis-specific classes and properties
    - which are already mapped to chemistry and catalysis related ontologies (e.g., ChEBI, CHEMINF, CHMO and RXNO)
- Supports description of:
    - Chemical substances and their properties (e.g., InChI, InChIKey and SMILES)
    - Chemical reactions (e.g., starting material, products, catalysts, solvents and conditions)
    - Material samples and laboratory contexts (e.g., sample type, used devices and their settings)
- Designed primarily for use by NFDI4Chem & NFDI4Cat consortia
- Licensed under CC-BY 4.0

## Core Components
ChemDCAT-AP consists of several interconnected modules:

1. **Chemical Entities**: Atoms, molecules, polymers
2. **Chemical Reactions**: Reactants, products, catalysts
3. **Material Entities**: Samples, physical properties

For detailed usage patterns and implementation guidance, see [Design Patterns](design-patterns.md).

## Documentation

- [DCAT-AP+ Documentation](https://nfdi-de.github.io/dcat-ap-plus/): Base layer documentation of ChemDCAT-AP.
- [ChemDCAT-AP GitHub Repository](https://github.com/nfdi-de/chem-dcat-ap): Source code and schema definitions.
- Description of the [design patterns & decisions](design-patterns.md)
- Auto-generated [schema documentation](elements/overview.md)
- Description of the [versioning rationale](versioning.md)
- [Projects](chemdcat-ap-users.md) using ChemDCAT-AP



