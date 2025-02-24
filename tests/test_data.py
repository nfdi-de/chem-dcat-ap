"""Data test."""
import os
import glob
import unittest

from linkml_runtime.loaders import yaml_loader
from src.dcat_4c_ap.datamodel.dcat_4c_ap import NMRDataset, Dataset, ResearchDataset


ROOT = os.path.join(os.path.dirname(__file__), '..')
DATA_DIR = os.path.join(ROOT, "src", "data", "examples")

EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR, '*.yaml'))


class TestData(unittest.TestCase):
    """Test data and datamodel."""

    def test_data(self):
        """Data test."""
        for path in EXAMPLE_FILES:
            if 'Dataset001_dcat_ap.yaml' in path:
                obj = yaml_loader.load(path, target_class=Dataset)
                assert obj
            elif 'Dataset001_dcat_4nfdi_ap.yaml' in path:
                obj = yaml_loader.load(path, target_class=ResearchDataset)
                assert obj
            elif 'Dataset001_dcat_4c_ap_NMRDataset.yaml' in path:
                obj = yaml_loader.load(path, target_class=NMRDataset)
                assert obj
