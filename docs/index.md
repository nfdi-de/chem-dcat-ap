# ChemDCAT-AP

ChemDCAT-AP is a domain-specific extension of [DCAT-AP+](https://github.com/NFDI-de/dcat-ap-plus) designed to provide chemistry and catalysis-specific metadata capabilities. It introduces specialized sub-classes and sub-properties mapped to relevant domain ontologies, enabling precise description of chemical datasets, reactions, and substances.

## Key Features
- Extends DCAT-AP+ with chemistry and catalysis-specific classes and properties
- Provides classes and properties mapped to domain ontologies (ChEBI, CHEMINF, CHMO, etc.)
- Supports description of:
  - Chemical substances and their properties (e.g., InChI, InChIKey and SMILES)
  - Chemical reactions (e.g., starting material, products, catalysts, solvents and conditions)
  - Material samples and laboratory contexts (e.g., used devices and their settings)
- Designed primarily for use by NFDI4Chem & NFDI4Cat consortia
- Licensed under CC-BY 4.0

## Core Components
ChemDCAT-AP consists of several interconnected modules:
1. **Chemical Entities**: Atoms, molecules, polymers
2. **Chemical Reactions**: Reactants, products, catalysts
3. **Material Entities**: Samples, physical properties

For detailed usage patterns and implementation guidance, see [Design Patterns](design-patterns.md).

## Usage

ChemDCAT-AP is designed to be used as an application profile for describing datasets in chemistry and catalysis. It can be further extended for specific use cases while maintaining compatibility with the DCAT-AP standard.

## Documentation

- [DCAT-AP+ Documentation](https://nfdi-de.github.io/dcat-ap-plus/): Base layer documentation of ChemDCAT-AP.
- [ChemDCAT-AP GitHub Repository](https://github.com/nfdi-de/chem-dcat-ap): Source code and schema definitions.
- Description of the [design patterns & decisions](design-patterns.md)
- Auto-generated [schema documentation](elements/overview.md)
- Description of the [versioning rationale](versioning.md)
- [Projects](chemdcat-ap-users.md) using ChemDCAT-AP



