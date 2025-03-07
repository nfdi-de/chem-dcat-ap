"""Data test."""
import os
import glob
import unittest

from linkml_runtime.loaders import yaml_loader
from src.dcat_4c_ap.datamodel.dcat_4c_ap import NMRAnalysisDataset, Dataset, AnalysisDataset


ROOT = os.path.join(os.path.dirname(__file__), '..')
DATA_DIR = os.path.join(ROOT, "src", "data", "examples")

EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR, '*.yaml'))


class TestData(unittest.TestCase):
    """Test data and datamodel."""

    def test_data(self):
        """Data test."""
        for path in EXAMPLE_FILES:
            print(path)
            if os.path.basename(path) == 'Dataset-001.yaml':
                obj = yaml_loader.load(path, target_class=Dataset)
                assert obj
            elif os.path.basename(path) == 'AnalysisDataset-001.yaml':
                obj = yaml_loader.load(path, target_class=AnalysisDataset)
                assert obj
            elif os.path.basename(path) == 'NMRAnalysisDataset-001.yaml':
                obj = yaml_loader.load(path, target_class=NMRAnalysisDataset)
                assert obj
