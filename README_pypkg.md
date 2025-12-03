# Chem-DCAT-AP

Extension of the DCAT Application Profile (DCAT-AP) tailored for chemistry-related data.  
It adds links to use-case specific context and enables describing:

- chemical datasets (e.g. spectra, chromatograms, assay results)
- related samples, substances and instruments
- provenance, experimental conditions and other domain-specific metadata

From the LinkML schemas in `src/chem_dcat_ap/schema/*.yaml`, two Python datamodel variants are generated:

- A variant based on Python `dataclasses`
- A variant based on Pydantic models

## Installation

```powershell
pip install chem-dcat-ap
```

Requires Python >= 3.9, < 4.0.

## Quick start

The package exposes the generated classes that correspond to the entities defined in the
`src/chem_dcat_ap/schema/*.yaml` LinkML schemas.

```python
import chem_dcat_ap
from chem_dcat_ap.datamodel.chem_dcat_ap import Dataset, DataGeneratingActivity

print(chem_dcat_ap.__version__)

dataset = Dataset(
    id="https://example.org/dataset/chem-001",
    title="Example chemical dataset",
    description="Minimal example dataset following the Chem-DCAT-AP schema.",
    was_generated_by=DataGeneratingActivity(
        id="https://example.org/activity/chem-001"
    ),
)

print(dataset)
```

For details about all available classes and fields, inspect the schema YAML files in
`src/chem_dcat_ap/schema/` and the generated module `chem_dcat_ap.datamodel.chem_dcat_ap`.

## Documentation

- Project docs and schema reference: <https://nfdi-de.github.io/dcat-ap-plus>
- Source code: <https://github.com/nfdi-de/chem-dcat-ap>

## License

MIT License. See the bundled `LICENSE` file for details.
