from pathlib import Path
from .chem_dcat_ap import *

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "chem_dcat_ap.yaml"
