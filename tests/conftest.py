"""pytest configuration module.

   In this module we define fixtures and helper functions for testing the chem-dcat-ap data model.

"""

import pytest
from random import randint, choice
from datetime import datetime, timedelta
import factory


from chem_dcat_ap.datamodel.chem_dcat_ap_pydantic import ChemicalEntity

def pytest_addoption(parser):
    """Advanced pytest command line options.
    
    This function adds a custom command line option `--num-instances` to pytest, 
    which allows users to specify the number of instances to create for testing purposes.
    """
    parser.addoption("--num-instances", action="store", default=1, help="Number of instances to create test")


@pytest.fixture(scope="session")
def num_instances(pytestconfig):
    return int(pytestconfig.getoption("num_instances"))


# helper functions

# inchi faker

def inchi_faker():
    """Generate a random InChI string for testing purposes."""
    return f"InChI=1S/C{randint(1, 20)}H{randint(0, 20)}/c{randint(1, 20)}-{randint(1, 20)}-{randint(1, 20)}/h{randint(1, 20)}H,{randint(1, 20)}H2,{randint(1, 20)}H3"

def smiles_faker():
    """Generate a random SMILES string for testing purposes."""
    elements = ['C', 'O', 'N', 'S', 'P', 'F', 'Cl', 'Br', 'I']
    return ''.join(choice(elements) for _ in range(randint(5, 15)))


# Fixture generation with factory boy
# TODO: move the facotries into an own module
class ChemicalEntityFactory(factory.Factory):
    class Meta:
        model = ChemicalEntity

    id = factory.Sequence(lambda n: 'chemical_entity_%d' % n)
    inchi = [] # [factory.Sequence(lambda n: inchi_faker())]
    smiles = [] #[factory.Sequence(lambda n: smiles_faker())]
    has_molar_mass = [] #factory.LazyAttribute(lambda x: round(randint(10, 500) + randint(0, 99)/100, 2))
    molecular_formula  = [] # factory.LazyAttribute(lambda x: ''.join(sample(['C', 'H', 'O', 'N', 'S', 'P'], randint(1, 5))))


@pytest.fixture
def chemical_entities(num_instances):
    return ChemicalEntityFactory.create_batch(num_instances)
