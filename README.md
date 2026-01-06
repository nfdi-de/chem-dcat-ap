[![DOI](https://zenodo.org/badge/878493365.svg)](https://doi.org/10.5281/zenodo.17806247)
[![PyPI - Version](https://img.shields.io/pypi/v/chem-dcat-ap)](https://pypi.org/project/chem-dcat-ap)
[![Build and test](https://github.com/nfdi-de/chem-dcat-ap/actions/workflows/main.yaml/badge.svg)](https://github.com/nfdi-de/chem-dcat-ap/actions/workflows/main.yaml)
[![Copier Badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json)](https://github.com/linkml/linkml-project-copier) 

# ChemDCAT-AP

ChemDCAT-AP, the LinkML schema provided in this repository, is an extension of the 
[DCAT Application Profile](https://semiceu.github.io/DCAT-AP/releases/3.0.0/). 
It is developed and used by the German research data infrastructure projects [NFDI4Chem](https://nfdi4chem.de) & 
[NFDI4Cat](https://nfdi4cat.org/) as a core metadata schema layer that is extended further in profiles, to 
provide chemistry and catalysis specific metadata for a `dcat:Dataset`. To achieve this, ChemDCAT-AP imports the 
domain-agnostic extension of DCAT-AP called [DCAT-AP+](https://nfdi-de.github.io/dcat-ap-plus/) as a base layer and 
extends it by defining additional classes and slots that allow a detailed ontology aligned description of:

* the activities that generated a `dcat:dataset` (e.g., a spectral analysis of a chemical sample, an evaluation of a chemical reaction), 
* the chemical substances covered by a `dcat:dataset` (e.g., analysed sample, reaction products or catalysts),
* the chemical reactions covered by a `dcat:dataset`, (e.g., reaction conditions, reagents, solvents, catalysts or yield).

## Website
More documentation can be found at the official website: https://nfdi-de.github.io/chem-dcat-ap

## Repository Structure

* [examples/](examples/) - example data and code
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [chem_dcat_ap](src/chem_dcat_ap)
    * [schema](src/chem_dcat_ap/schema) -- LinkML schema
      (edit this)
    * [datamodel](src/chem_dcat_ap/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests

## Developer Documentation

See also the documentation of the template: https://github.com/linkml/linkml-project-copier?tab=readme-ov-file#prerequisites

* **uv**

  uv is a tool to manage Python projects and for managing isolated Python-based applications.
  You will use it in your generated project to manage dependencies and build distribution files.
  Install uv by following their [instructions](https://docs.astral.sh/uv/getting-started/installation/).
  
  Note: Environments with private pypi repository may need extra configuration (example):
    `export UV_DEFAULT_INDEX=https://nexus.example.com/repository/pypi-all/simple`

* **Copier**

  Copier is a tool for generating projects based on a template (like this one!). It 
also allows re-configuring the projects and to keep them updated when the original 
template changes. To insert dates into the template, copier requires 
[jinja2_time](https://github.com/hackebrot/jinja2-time) in the copier environment. Install both with uv by running:
  ````shell 
    uv tool install --with jinja2-time copier
  ````
  
* **just**

  The project contains a `justfile` with pre-defined complex commands.
  To execute these commands you need [just](https://github.com/casey/just) as command runner. Install it by running:

  ```shell
  uv tool install rust-just
  ```

  To generate project artefacts run:
    * `just gen-project`: generates all other representations
    * `just deploy`: deploys site
    * `just testdoc`: locally builds docs and runs test server

### Test data validation and convertion
Validate and test all: `just test`

  * Validate a ChemicalReaction example conforming to ChemDCAT-AP
    ````commandline
    uv run linkml validate tests/data/valid/ChemicalReaction-001.yaml -s src/chem_dcat_ap/schema/chem_dcat_ap.yaml -C ChemicalReaction
    ````
  * Validate a SubstanceSample example conforming to ChemDCAT-AP
    ````commandline
    uv run linkml validate tests/data/valid/SubstanceSample-001.yaml -s src/chem_dcat_ap/schema/chem_dcat_ap.yaml -C SubstanceSample
    ````
  * Validate a MaterialSample example conforming to ChemDCAT-AP
    ````commandline
    uv run linkml validate tests/data/valid/MaterialSample-001.yaml -s src/chem_dcat_ap/schema/chem_dcat_ap.yaml -C MaterialSample
    ````

To convert the test examples into a TTL graph run:

  * Convert a MaterialSample example conforming to ChemDCAT-AP
    ````commandline
    uv run linkml-convert -t ttl tests/data/valid/MaterialSample-001.yaml -s src/chem_dcat_ap/schema/chem_dcat_ap.yaml -P "_base=https://search.nfdi4chem.de/dataset/" -C MaterialSample
    ````
  * Convert a SubstanceSample example conforming to ChemDCAT-AP
    ````commandline
    uv run linkml-convert -t ttl tests/data/valid/SubstanceSample-001.yaml -s src/chem_dcat_ap/schema/chem_dcat_ap.yaml -P "_base=https://search.nfdi4chem.de/dataset/" -C SubstanceSample
    ````
  * Convert a ChemicalReaction example conforming to ChemDCAT-AP
    ````commandline
    uv run linkml-convert -t ttl tests/data/valid/ChemicalReaction-001.yaml -s src/chem_dcat_ap/schema/chem_dcat_ap.yaml -P "_base=https://search.nfdi4chem.de/dataset/" -C ChemicalReaction
    ````

## Funding

This work was funded by the German Research Foundation (DFG) through the projects: 
* "[NFDI4Cat](https://nfdi4cat.org/) - NFDI for Catalysis-Related Sciences" (DFG project no. [441926934](https://gepris.dfg.de/gepris/projekt/441926934)) and 
* "[NFDI4Chem](https://nfdi4chem.de) - NFDI for Chemistry" (DFG project no. [441958208](https://gepris.dfg.de/gepris/projekt/441958208))

within the National Research Data Infrastructure (NFDI) programme of the Joint Science Conference (GWK).

## Credits

This project uses the template [linkml-project-copier](https://github.com/linkml/linkml-project-copier).
