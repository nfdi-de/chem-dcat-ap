# dcat-4C-ap

This is an extension of the DCAT Application Profile in LinkML. It is intended to be used by NFDI4Chem & NFDI 4Cat as a core that can further be extended in profiles to provide domain specific metadata for a dataset.

## Website

[https://StroemPhi.github.io/dcat-4C-ap](https://StroemPhi.github.io/dcat-4C-ap)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [dcat_4c_ap](src/dcat_4c_ap)
    * [schema](src/dcat_4c_ap/schema) -- LinkML schema
      (edit this)
    * [datamodel](src/dcat_4c_ap/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests

## Developer Documentation

Requirements:
*  Poetry must be installed
   * `pipx install poetry`
*  `make setup` to install Poetry env
*  If you want you could run `poetry run python src/dcat-ap_shacl_2_linkml.py` to recreate the [dcat-ap.yaml](src%2Fdcat_4c_ap%2Fschema%2Fdcat-ap.yaml) from the [dcat-ap-SHACL.jsonld](src%2Fdcat-ap-SHACL.jsonld)
* To build the docs locally run: 
  ` poetry run gen-doc  -d docs "src/dcat_4C_ap/schema/dcat-ap.yaml" --template-directory "src/docgen/" && poetry run mkdocs serve`
  * Use another LinkML YAML in `src` if you want to build the docs of a profile.

<details>
Use the `make` command to generate project artefacts:

* `make all`: make everything
* `make deploy`: deploys site
</details>

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
