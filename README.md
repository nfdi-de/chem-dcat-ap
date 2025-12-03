[![DOI](https://zenodo.org/badge/1080296103.svg)](https://doi.org/10.5281/zenodo.17702369)
[![PyPI - Version](https://img.shields.io/pypi/v/chem-dcat-ap)](https://pypi.org/project/chem-dcat-ap)
[![Build and test](https://github.com/nfdi-de/chem-dcat-ap/actions/workflows/main.yaml/badge.svg)](https://github.com/nfdi-de/chem-dcat-ap/actions/workflows/main.yaml)
[![Copier Badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json)](https://github.com/linkml/linkml-project-copier) 

# Chem-DCAT-AP

This is an extension of the DCAT Application Profile v3.0 in LinkML. It is intended to be used by NFDI4Chem & NFDI4Cat
as a core that can further be extended in profiles to provide domain specific metadata for a dataset.

## DCAT-AP to LinkML translation
The [official DCAT-AP 3.0.0 SHACL shapes](src%2Fdcat_ap_shacl.jsonld) where downloaded from the DCAT-AP GitHub repository
from the [3.0.0 release folder within the master branch](https://github.com/SEMICeu/DCAT-AP/blob/master/releases/3.0.0/shacl/dcat-ap-SHACL.jsonld). We chose this shapes definition file, as they are in line with the current DCAT-AP Specification website and because its IRI resolves. It must be noted, that this is not case for the shapes provides in the GitHub 3.0.0 release
(respectively the release branch).

The downloaded SHACL shapes were then processed by the [dcat_ap_shacl_2_linkml.py](src%2Fdcat_ap_shacl_2_linkml.py)
to generate two LinkML representations from it:
* [dcat_ap_linkml.yaml](src%2Fdcat_4c_ap%2Fschema%2Fdcat_ap_linkml.yaml) - an almost 1:1 translation from SHACL to
  LinkML that could be reused by anyone who wants to.
* [dcat_ap_plus.yaml](src%2Fdcat_4c_ap%2Fschema%2Fdcat_ap_plus.yaml) - the LinkML representation of DCAT-AP to which 
  we added the additional constraints, classes and properties we need for our DCAT-AP extension. 

## Website

https://nfdi-de.github.io/chem-dcat-ap

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

  Copier is a tool for generating projects based on a template (like this one!). It also allows re-configuring the projects and to keep them updated when the original template changes. To insert dates into the template, copier requires [jinja2_time](https://github.com/hackebrot/jinja2-time) in the copier environment. Install both with uv by running:
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

### Regenerate schema files from DCAT-AP SHACL shapes
To regenerate the DCAT-AP LinkML representation as well as the PLUS extension run:
  ````commandline 
  uv run python src/dcat_ap_shacl_2_linkml.py
  ````

### Test data validation and convertion
Validate and test all: `just test`

Validate a single example dataset using LinkML's validator framework:
  * Validate domain agnostic DCAT-AP extension conform example
    ````commandline
    uv run linkml validate tests/data/valid/AnalysisDataset-001.yaml -s src/chem_dcat_ap/schema/chem_dcat_ap.yaml -C AnalysisDataset
    ````
  * Validate a NMR spectroscopy-specific DCAT-AP extension conform example
    ````commandline
    uv run linkml validate tests/data/valid/NMRAnalysisDataset-001.yaml -s src/chem_dcat_ap/schema/chem_dcat_ap.yaml -C NMRAnalysisDataset
    ````
  * Validate a ChemicalReaction specific DCAT-AP extension conform example
    ````commandline
    uv run linkml validate tests/data/valid/ChemicalReaction-001.yaml -s src/chem_dcat_ap/schema/chem_dcat_ap.yaml -C ChemicalReaction
    ````
  * Validate a SubstanceSample specific DCAT-AP extension conform example
    ````commandline
    uv run linkml validate tests/data/valid/SubstanceSample-001.yaml -s src/chem_dcat_ap/schema/chem_dcat_ap.yaml -C SubstanceSample
    ````
  * Validate a MaterialSample specific DCAT-AP extension conform example
    ````commandline
    uv run linkml validate tests/data/valid/MaterialSample-001.yaml -s src/chem_dcat_ap/schema/chem_dcat_ap.yaml -C MaterialSample
    ````

To convert the test datasets of each DCAT-AP profile into a TTL graph run:
  * Convert domain agnostic DCAT-AP extension conform example of an analysis
    ````commandline
    uv run linkml-convert -t ttl tests/data/valid/AnalysisDataset-001.yaml -s src/chem_dcat_ap/schema/chem_dcat_ap.yaml -P "_base=https://search.nfdi4chem.de/dataset/" -C AnalysisDataset
    ````
  * Convert a NMR spectroscopy-specific DCAT-AP extension conform example
    ````commandline
    uv run linkml-convert -t ttl tests/data/valid/NMRAnalysisDataset-001.yaml -s src/chem_dcat_ap/schema/chem_dcat_ap.yaml -P "_base=https://search.nfdi4chem.de/dataset/" -C NMRAnalysisDataset
    ````
  * Convert domain agnostic DCAT-AP extension conform example of a MaterialSample
    ````commandline
    uv run linkml-convert -t ttl tests/data/valid/MaterialSample-001.yaml -s src/chem_dcat_ap/schema/chem_dcat_ap.yaml -P "_base=https://search.nfdi4chem.de/dataset/" -C MaterialSample
    ````
  * Convert domain agnostic DCAT-AP extension conform example of a SubstanceSample
    ````commandline
    uv run linkml-convert -t ttl tests/data/valid/SubstanceSample-001.yaml -s src/chem_dcat_ap/schema/chem_dcat_ap.yaml -P "_base=https://search.nfdi4chem.de/dataset/" -C SubstanceSample
    ````
  * Convert domain agnostic DCAT-AP extension conform example of a ChemicalReaction
    ````commandline
    uv run linkml-convert -t ttl tests/data/valid/ChemicalReaction-001.yaml -s src/chem_dcat_ap/schema/chem_dcat_ap.yaml -P "_base=https://search.nfdi4chem.de/dataset/" -C ChemicalReaction
    ````
### Build GitHub pages docs locally
    ````commandline
    uv run mkdocs serve
    ````
    ````commandline
    rm -rf docs/elements/*.md && uv run gen-doc  -d docs/elements src/chem_dcat_ap/schema/chem_dcat_ap.yaml
    ````

## Credits

This project was initially created with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
and later migrated to
[linkml-project-copier](https://github.com/linkml/linkml-project-copier).
