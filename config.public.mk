# config.public.mk

# This file is public in git. No sensitive info allowed.

###### schema definition variables, used by justfile

# Note:
# - just works fine with quoted variables of dot-env files like this one
LINKML_SCHEMA_NAME="chem_dcat_ap"
LINKML_SCHEMA_AUTHOR="Philip Strömert <philip.stroemert@tib.eu>"
LINKML_SCHEMA_DESCRIPTION="This is an extension of the DCAT Application Profile in LinkML. It is intended to be used by NFDI4Chem & NFDI4Cat as a core that can further be extended in profiles to provide domain specific metadata for a dataset."
LINKML_SCHEMA_SOURCE_DIR="src/chem_dcat_ap/schema"

###### linkml generator variables, used by justfile

## gen-project configuration file
LINKML_GENERATORS_CONFIG_YAML=config.yaml

## pass args if gendoc ignores config.yaml (i.e. --no-mergeimports)
LINKML_GENERATORS_DOC_ARGS="--truncate-descriptions False --hierarchical-class-view --subfolder-type-separation --index-name overview"

## pass args to workaround genowl rdfs config bug (linkml#1453)
##   (i.e. --no-type-objects --no-metaclasses --metadata-profile rdfs)
LINKML_GENERATORS_OWL_ARGS=

## pass args to trigger experimental java/typescript generation
LINKML_GENERATORS_JAVA_ARGS=
LINKML_GENERATORS_TYPESCRIPT_ARGS=

## pass args to pydantic generator which isn't supported by gen-project
## https://github.com/linkml/linkml/issues/2537
LINKML_GENERATORS_PYDANTIC_ARGS=
