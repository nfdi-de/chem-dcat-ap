"""Data test."""
import os
import glob
import unittest

from linkml_runtime.loaders import yaml_loader
from src.dcat_4c_ap.datamodel.dcat_4c_ap import NMRDataset, Dataset, NFDIDataset


ROOT = os.path.join(os.path.dirname(__file__), '..')
DATA_DIR = os.path.join(ROOT, "src", "data", "examples")

EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR, '*.yaml'))


class TestData(unittest.TestCase):
    """Test data and datamodel."""

    def test_data(self):
        """Data test."""
        for path in EXAMPLE_FILES:
            if path == 'Dataset001_dcat_ap.yaml':
                obj = yaml_loader.load(path, target_class=Dataset)
                assert obj
            elif path == 'Dataset001_dcat_4nfdi_ap.yaml':
                obj = yaml_loader.load(path, target_class=NFDIDataset)
                assert obj
            elif path == 'Dataset001_dcat_4c_ap_NMRDataset.yaml':
                obj = yaml_loader.load(path, target_class=NMRDataset)
                assert obj
