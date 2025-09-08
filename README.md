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
  * [dcat_4c_ap](src/dcat_4c_ap)
    * [schema](src/dcat_4c_ap/schema) -- LinkML schema
      (edit this)
    * [datamodel](src/dcat_4c_ap/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests

## Developer Documentation

Requirements (see also https://github.com/dalito/linkml-project-copier?tab=readme-ov-file#prerequisites):

### Poetry 
  
  Poetry is a Python project management tool. You will use it in your generated project to manage dependencies and 
  build distribution files. Install Poetry by running:
  ````commandline 
  pipx install poetry
  pipx inject poetry "poetry-dynamic-versioning[plugin]"
  ````
### Copier

  Copier is a tool for generating projects based on a template (like this one!). It also allows re-configuring the projects and to keep them updated when the original template changes. To insert dates into the template, copier requires [jinja2_time](https://github.com/hackebrot/jinja2-time) in the copier environment. Install both with pipx by running:
  ````commandline 
    pipx install copier
    pipx inject copier jinja2_time
  ````
### just
  
  The project contains a justfile with pre-defined complex commands. To execute these commands you need [just](https://github.com/casey/just) as command runner. Install it by running:

  ````commandline 
  pipx install rust-just
  ````
To create a Poetry env with all dependencies you then need to run:
  * `just setup`

To generate project artefacts run:
  * `just gen-project`: generates all other representations
  * `just deploy`: deploys site
  * `just testdoc`: locally builds docs and runs test server

### Regenerate schema files from DCAT-AP SHACL shapes
To regenerate the DCAT-AP LinkML representation as well as the PLUS extension run:
  ````commandline 
  poetry run python src/dcat_ap_shacl_2_linkml.py
  ````

### Test data validation and convertion
Validate and test all: `just test`

Validate a single example dataset using LinkML's validator framework:
  * Validate domain agnostic DCAT-AP extension conform example
    ````commandline
    poetry run linkml validate tests/data/valid/AnalysisDataset-001.yaml -s src/dcat_4c_ap/schema/dcat_4c_ap.yaml -C AnalysisDataset
    ````
  * Validate a NMR spectroscopy-specific DCAT-AP extension conform example
    ````commandline
    poetry run linkml validate tests/data/valid/NMRAnalysisDataset-001.yaml -s src/dcat_4c_ap/schema/dcat_4c_ap.yaml -C NMRAnalysisDataset
    ````

To convert the test datasets of each DCAT-AP profile into a TTL graph run:
  * Convert domain agnostic DCAT-AP extension conform example of an analysis
    ````commandline
    poetry run linkml-convert -t ttl tests/data/valid/AnalysisDataset-001.yaml -s src/dcat_4C_ap/schema/dcat_4c_ap.yaml -P "_base=https://search.nfdi4chem.de/dataset/" -C AnalysisDataset
    ````
  * Convert a NMR spectroscopy-specific DCAT-AP extension conform example
    ````commandline
    poetry run linkml-convert -t ttl tests/data/valid/NMRAnalysisDataset-001.yaml -s src/dcat_4C_ap/schema/dcat_4c_ap.yaml -P "_base=https://search.nfdi4chem.de/dataset/" -C NMRAnalysisDataset
    ````

## Credits

This project was initially created with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
and later migrated to
[linkml-project-copier](https://github.com/dalito/linkml-project-copier).
