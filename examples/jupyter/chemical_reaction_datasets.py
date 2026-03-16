"""
Module to generate example datasets for chemical reactions using the Chem DCAT-AP LinkML data model.
"""

from chem_dcat_ap.datamodel.chem_dcat_ap_pydantic import (
    Dataset, ChemicalReaction, StartingMaterial, Reagent, ChemicalProduct, 
    Catalyst, DissolvingSubstance, Reactor, Temperature, Pressure, Yield,
    ChemicalEntity, InChi, InChIKey, SMILES, MolecularFormula, IUPACName,
    Agent, DataGeneratingActivity, DataAnalysis, Distribution, 
    QualitativeAttribute, QuantitativeAttribute, PhysicalStateEnum
)
from datetime import date
from typing import List, Optional
import uuid


def create_chemical_entity(
    id: str,
    inchi: Optional[str] = None,
    inchikey: Optional[str] = None,
    smiles: Optional[str] = None,
    molecular_formula: Optional[str] = None,
    iupac_name: Optional[str] = None
) -> ChemicalEntity:
    """Create a ChemicalEntity with the provided properties."""
    entity = ChemicalEntity(
        id=id,
        inchi=[InChi(value=inchi)] if inchi else [],
        inchikey=[InChIKey(value=inchikey)] if inchikey else [],
        smiles=[SMILES(value=smiles)] if smiles else [],
        molecular_formula=[MolecularFormula(value=molecular_formula)] if molecular_formula else [],
        iupac_name=[IUPACName(value=iupac_name)] if iupac_name else []
    )
    return entity


def create_starting_material(
    id: str,
    chemical_entity: ChemicalEntity,
    mass: Optional[float] = None,
    volume: Optional[float] = None,
    temperature: Optional[float] = None,
    pressure: Optional[float] = None,
    physical_state: Optional[PhysicalStateEnum] = None
) -> StartingMaterial:
    """Create a StartingMaterial with the provided properties."""
    material = StartingMaterial(
        id=id,
        composed_of=[chemical_entity],
        has_mass=[QuantitativeAttribute(
            value=mass,
            has_quantity_type="mass",
            unit="g"
        )] if mass else [],
        has_volume=[QuantitativeAttribute(
            value=volume,
            has_quantity_type="volume",
            unit="mL"
        )] if volume else [],
        has_temperature=[QuantitativeAttribute(
            value=temperature,
            has_quantity_type="temperature",
            unit="K"
        )] if temperature else [],
        has_pressure=[QuantitativeAttribute(
            value=pressure,
            has_quantity_type="pressure",
            unit="bar"
        )] if pressure else [],
        has_physical_state=physical_state
    )
    return material


def create_reagent(
    id: str,
    chemical_entity: ChemicalEntity,
    mass: Optional[float] = None,
    volume: Optional[float] = None,
    temperature: Optional[float] = None,
    pressure: Optional[float] = None,
    physical_state: Optional[PhysicalStateEnum] = None
) -> Reagent:
    """Create a Reagent with the provided properties."""
    material = Reagent(
        id=id,
        composed_of=[chemical_entity],
        has_mass=[QuantitativeAttribute(
            value=mass,
            has_quantity_type="mass",
            unit="g"
        )] if mass else [],
        has_volume=[QuantitativeAttribute(
            value=volume,
            has_quantity_type="volume",
            unit="mL"
        )] if volume else [],
        has_temperature=[QuantitativeAttribute(
            value=temperature,
            has_quantity_type="temperature",
            unit="K"
        )] if temperature else [],
        has_pressure=[QuantitativeAttribute(
            value=pressure,
            has_quantity_type="pressure",
            unit="bar"
        )] if pressure else [],
        has_physical_state=physical_state
    )
    return material


def create_chemical_product(
    id: str,
    chemical_entity: ChemicalEntity,
    mass: Optional[float] = None,
    volume: Optional[float] = None,
    temperature: Optional[float] = None,
    pressure: Optional[float] = None,
    physical_state: Optional[PhysicalStateEnum] = None
) -> ChemicalProduct:
    """Create a ChemicalProduct with the provided properties."""
    product = ChemicalProduct(
        id=id,
        composed_of=[chemical_entity],
        has_mass=[QuantitativeAttribute(
            value=mass,
            has_quantity_type="mass",
            unit="g"
        )] if mass else [],
        has_volume=[QuantitativeAttribute(
            value=volume,
            has_quantity_type="volume",
            unit="mL"
        )] if volume else [],
        has_temperature=[QuantitativeAttribute(
            value=temperature,
            has_quantity_type="temperature",
            unit="K"
        )] if temperature else [],
        has_pressure=[QuantitativeAttribute(
            value=pressure,
            has_quantity_type="pressure",
            unit="bar"
        )] if pressure else [],
        has_physical_state=physical_state
    )
    return product


def create_catalyst(
    id: str,
    chemical_entity: ChemicalEntity,
    mass: Optional[float] = None,
    volume: Optional[float] = None,
    temperature: Optional[float] = None,
    pressure: Optional[float] = None,
    physical_state: Optional[PhysicalStateEnum] = None
) -> Catalyst:
    """Create a Catalyst with the provided properties."""
    catalyst = Catalyst(
        id=id,
        composed_of=[chemical_entity],
        has_mass=[QuantitativeAttribute(
            value=mass,
            has_quantity_type="mass",
            unit="g"
        )] if mass else [],
        has_volume=[QuantitativeAttribute(
            value=volume,
            has_quantity_type="volume",
            unit="mL"
        )] if volume else [],
        has_temperature=[QuantitativeAttribute(
            value=temperature,
            has_quantity_type="temperature",
            unit="K"
        )] if temperature else [],
        has_pressure=[QuantitativeAttribute(
            value=pressure,
            has_quantity_type="pressure",
            unit="bar"
        )] if pressure else [],
        has_physical_state=physical_state
    )
    return catalyst


def create_solvent(
    id: str,
    chemical_entity: ChemicalEntity,
    volume: Optional[float] = None,
    temperature: Optional[float] = None,
    pressure: Optional[float] = None,
    physical_state: Optional[PhysicalStateEnum] = None
) -> DissolvingSubstance:
    """Create a DissolvingSubstance (solvent) with the provided properties."""
    solvent = DissolvingSubstance(
        id=id,
        composed_of=[chemical_entity],
        has_volume=[QuantitativeAttribute(
            value=volume,
            has_quantity_type="volume",
            unit="mL"
        )] if volume else [],
        has_temperature=[QuantitativeAttribute(
            value=temperature,
            has_quantity_type="temperature",
            unit="K"
        )] if temperature else [],
        has_pressure=[QuantitativeAttribute(
            value=pressure,
            has_quantity_type="pressure",
            unit="bar"
        )] if pressure else [],
        has_physical_state=physical_state
    )
    return solvent


def create_reactor(
    id: str,
    name: str,
    volume: Optional[float] = None,
    temperature: Optional[float] = None,
    pressure: Optional[float] = None
) -> Reactor:
    """Create a Reactor with the provided properties."""
    reactor = Reactor(
        id=id,
        title=name,
        has_volume=[QuantitativeAttribute(
            value=volume,
            has_quantity_type="volume",
            unit="L"
        )] if volume else [],
        has_temperature=[QuantitativeAttribute(
            value=temperature,
            has_quantity_type="temperature",
            unit="K"
        )] if temperature else [],
        has_pressure=[QuantitativeAttribute(
            value=pressure,
            has_quantity_type="pressure",
            unit="bar"
        )] if pressure else []
    )
    return reactor


def create_chemical_reaction(
    id: str,
    title: str,
    description: str,
    starting_materials: List[StartingMaterial],
    reagents: List[Reagent],
    products: List[ChemicalProduct],
    catalysts: List[Catalyst],
    solvents: List[DissolvingSubstance],
    reactors: List[Reactor],
    temperature: Optional[float] = None,
    pressure: Optional[float] = None,
    duration: Optional[str] = None,
    yield_percentage: Optional[float] = None,
    creator: Optional[Agent] = None
) -> ChemicalReaction:
    """Create a ChemicalReaction with the provided properties."""
    reaction = ChemicalReaction(
        id=id,
        title=[title],
        description=[description],
        used_starting_material=starting_materials,
        used_reactant=reagents,
        generated_product=products,
        used_catalyst=catalysts,
        used_solvent=solvents,
        used_reactor=reactors,
        has_temperature=[QuantitativeAttribute(
            value=temperature,
            has_quantity_type="temperature",
            unit="K"
        )] if temperature else [],
        has_pressure=[QuantitativeAttribute(
            value=pressure,
            has_quantity_type="pressure",
            unit="bar"
        )] if pressure else [],
        has_duration=duration,
        has_yield=[QuantitativeAttribute(
            value=yield_percentage,
            has_quantity_type="yield",
            unit="%"
        )] if yield_percentage else []
    )
    
    if creator:
        reaction.carried_out_by = [creator]
        
    return reaction


def create_dataset_for_reaction(
    dataset_id: str,
    reaction: ChemicalReaction,
    creator: Agent,
    title: str,
    description: str,
    release_date: date = None
) -> Dataset:
    """Create a Dataset for a ChemicalReaction."""
    dataset = Dataset(
        id=dataset_id,
        title=[title],
        description=[description],
        was_generated_by=[reaction],
        creator=[creator],
        release_date=release_date,
        is_about_entity=[],
        is_about_activity=[reaction]
    )
    return dataset


def generate_chemical_reaction_datasets() -> List[Dataset]:
    """Generate example datasets for chemical reactions."""
    # Create agents
    researcher = Agent(
        name=["Dr. Jane Smith"],
        type=None
    )
    
    # Create chemical entities
    benzene = create_chemical_entity(
        id="CHEBI:15377",
        inchi="InChI=1S/C6H6/c1-2-4-6-5-3-1/h1-6H",
        inchikey="UHOVQNZJYSORNB-UHFFFAOYSA-N",
        smiles="c1ccccc1",
        molecular_formula="C6H6",
        iupac_name="benzene"
    )
    
    acetaldehyde = create_chemical_entity(
        id="CHEBI:15343",
        inchi="InChI=1S/C2H4O/c1-2-3/h1-3H",
        inchikey="QGZKDVFQNNGYKY-UHFFFAOYSA-N",
        smiles="CC=O",
        molecular_formula="C2H4O",
        iupac_name="acetaldehyde"
    )
    
    cyclohexanol = create_chemical_entity(
        id="CHEBI:17855",
        inchi="InChI=1S/C6H12O/c7-6-4-2-1-3-5-6/h1-5,7H2",
        inchikey="QVJZQZQZQZQZQZ-QVJZQZQZSA-N",
        smiles="C1CCCCC1O",
        molecular_formula="C6H12O",
        iupac_name="cyclohexanol"
    )
    
    # Create starting materials
    benzene_starting = create_starting_material(
        id="SM001",
        chemical_entity=benzene,
        mass=50.0,
        volume=50.0,
        temperature=298.15,
        pressure=1.0,
        physical_state=PhysicalStateEnum.LIQUID
    )
    
    acetaldehyde_starting = create_starting_material(
        id="SM002",
        chemical_entity=acetaldehyde,
        mass=30.0,
        volume=30.0,
        temperature=298.15,
        pressure=1.0,
        physical_state=PhysicalStateEnum.LIQUID
    )
    
    # Create reagents
    hydrogen_gas = create_reagent(
        id="R001",
        chemical_entity=create_chemical_entity(
            id="CHEBI:15379",
            inchi="InChI=1S/H2/h1H",
            inchikey="XUFQDOOMUQDZQJ-UHFFFAOYSA-N",
            smiles="[H][H]",
            molecular_formula="H2",
            iupac_name="hydrogen"
        ),
        mass=0.5,
        volume=100.0,
        temperature=298.15,
        pressure=10.0,
        physical_state=PhysicalStateEnum.GASEOUS
    )
    
    # Create products
    cyclohexanone = create_chemical_product(
        id="CP001",
        chemical_entity=create_chemical_entity(
            id="CHEBI:17856",
            inchi="InChI=1S/C6H10O/c7-6-4-2-1-3-5-6/h1-5,7H2",
            inchikey="QVJZQZQZQZQZQZ-QVJZQZQZSA-N",
            smiles="C1CCCCC1=O",
            molecular_formula="C6H10O",
            iupac_name="cyclohexanone"
        ),
        mass=45.0,
        volume=45.0,
        temperature=298.15,
        pressure=1.0,
        physical_state=PhysicalStateEnum.LIQUID
    )
    
    # Create catalysts
    nickel_catalyst = create_catalyst(
        id="CAT001",
        chemical_entity=create_chemical_entity(
            id="CHEBI:17857",
            inchi="InChI=1S/Ni/c1-2",
            inchikey="QVJZQZQZQZQZQZ-QVJZQZQZSA-N",
            smiles="[Ni]",
            molecular_formula="Ni",
            iupac_name="nickel"
        ),
        mass=0.1,
        volume=0.1,
        temperature=298.15,
        pressure=1.0,
        physical_state=PhysicalStateEnum.SOLID
    )
    
    # Create solvents
    ethanol_solvent = create_solvent(
        id="S001",
        chemical_entity=create_chemical_entity(
            id="CHEBI:16236",
            inchi="InChI=1S/C2H6O/c1-2-3/h1-3H3",
            inchikey="QVJZQZQZQZQZQZ-QVJZQZQZSA-N",
            smiles="CCO",
            molecular_formula="C2H6O",
            iupac_name="ethanol"
        ),
        volume=100.0,
        temperature=298.15,
        pressure=1.0,
        physical_state=PhysicalStateEnum.LIQUID
    )
    
    # Create reactors
    reactor1 = create_reactor(
        id="REACTOR001",
        name="Reactor A",
        volume=1.0,
        temperature=350.0,
        pressure=5.0
    )
    
    # Create chemical reactions
    aldol_condensation = create_chemical_reaction(
        id="CR001",
        title="Aldol Condensation Reaction",
        description="Aldol condensation reaction between benzene and acetaldehyde in presence of nickel catalyst",
        starting_materials=[benzene_starting, acetaldehyde_starting],
        reagents=[hydrogen_gas],
        products=[cyclohexanone],
        catalysts=[nickel_catalyst],
        solvents=[ethanol_solvent],
        reactors=[reactor1],
        temperature=350.0,
        pressure=5.0,
        duration="2 hours",
        yield_percentage=85.0,
        creator=researcher
    )
    
    # Create datasets for the reaction
    dataset1 = create_dataset_for_reaction(
        dataset_id="DS001",
        reaction=aldol_condensation,
        creator=researcher,
        title="Dataset D1: Aldol Condensation Reaction",
        description="Dataset D1: Aldol condensation reaction between benzene and acetaldehyde with nickel catalyst",
        release_date=date(2023, 1, 1)
    )
    
    # Create second replicate
    dataset2 = create_dataset_for_reaction(
        dataset_id="DS002",
        reaction=aldol_condensation,
        creator=researcher,
        title="Dataset D2: Aldol Condensation Reaction (Replicate 2)",
        description="Dataset D2: Aldol condensation reaction between benzene and acetaldehyde with nickel catalyst (replicate 2)",
        release_date=date(2023, 1, 2)
    )
    
    # Create third replicate
    dataset3 = create_dataset_for_reaction(
        dataset_id="DS003",
        reaction=aldol_condensation,
        creator=researcher,
        title="Dataset D3: Aldol Condensation Reaction (Replicate 3)",
        description="Dataset D3: Aldol condensation reaction between benzene and acetaldehyde with nickel catalyst (replicate 3)",
        release_date=date(2023, 1, 3)
    )
    
    # Create transamination reaction
    transamination = create_chemical_reaction(
        id="CR002",
        title="Transamination Reaction",
        description="Transamination reaction between amino acid and keto acid",
        starting_materials=[create_starting_material(
            id="SM003",
            chemical_entity=create_chemical_entity(
                id="CHEBI:17858",
                inchi="InChI=1S/C3H7NO2/c4-2(1-3(5)6)7/h2-7H,1H2,(H,5,6)",
                inchikey="QVJZQZQZQZQZQZ-QVJZQZQZSA-N",
                smiles="C(C(=O)O)CN",
                molecular_formula="C3H7NO2",
                iupac_name="alanine"
            ),
            mass=20.0,
            volume=20.0,
            temperature=298.15,
            pressure=1.0,
            physical_state=PhysicalStateEnum.LIQUID
        )],
        reagents=[create_reagent(
            id="R002",
            chemical_entity=create_chemical_entity(
                id="CHEBI:17859",
                inchi="InChI=1S/C3H4O3/c1-2(3(4)5)6/h2H2,1H3,(H,4,5)",
                inchikey="QVJZQZQZQZQZQZ-QVJZQZQZSA-N",
                smiles="C(=O)(C(=O)O)C",
                molecular_formula="C3H4O3",
                iupac_name="pyruvic acid"
            ),
            mass=15.0,
            volume=15.0,
            temperature=298.15,
            pressure=1.0,
            physical_state=PhysicalStateEnum.LIQUID
        )],
        products=[create_chemical_product(
            id="CP002",
            chemical_entity=create_chemical_entity(
                id="CHEBI:17860",
                inchi="InChI=1S/C3H7NO2/c4-2(1-3(5)6)7/h2-7H,1H2,(H,5,6)",
                inchikey="QVJZQZQZQZQZQZ-QVJZQZQZSA-N",
                smiles="C(C(=O)O)CN",
                molecular_formula="C3H7NO2",
                iupac_name="glutamic acid"
            ),
            mass=25.0,
            volume=25.0,
            temperature=298.15,
            pressure=1.0,
            physical_state=PhysicalStateEnum.LIQUID
        )],
        catalysts=[create_catalyst(
            id="CAT002",
            chemical_entity=create_chemical_entity(
                id="CHEBI:17861",
                inchi="InChI=1S/C6H12N2O2/c7-5(8)3-1-2-4-6(9)10/h1-10H2,(H,7,8)(H,9,10)",
                inchikey="QVJZQZQZQZQZQZ-QVJZQZQZSA-N",
                smiles="C1CC(NC(=O)C)C1",
                molecular_formula="C6H12N2O2",
                iupac_name="pyridoxal phosphate"
            ),
            mass=0.05,
            volume=0.05,
            temperature=298.15,
            pressure=1.0,
            physical_state=PhysicalStateEnum.SOLID
        )],
        solvents=[create_solvent(
            id="S002",
            chemical_entity=create_chemical_entity(
                id="CHEBI:17862",
                inchi="InChI=1S/H2O/h1H2",
                inchikey="QVJZQZQZQZQZQZ-QVJZQZQZSA-N",
                smiles="O",
                molecular_formula="H2O",
                iupac_name="water"
            ),
            volume=50.0,
            temperature=298.15,
            pressure=1.0,
            physical_state=PhysicalStateEnum.LIQUID
        )],
        reactors=[reactor1],
        temperature=300.0,
        pressure=1.0,
        duration="1 hour",
        yield_percentage=90.0,
        creator=researcher
    )
    
    # Create datasets for transamination
    dataset4 = create_dataset_for_reaction(
        dataset_id="DS004",
        reaction=transamination,
        creator=researcher,
        title="Dataset D4: Transamination Reaction",
        description="Dataset D4: Transamination reaction between alanine and pyruvic acid with pyridoxal phosphate catalyst",
        release_date=date(2023, 1, 4)
    )
    
    # Create Fisher-Tropsch synthesis reaction
    fisher_tropsch = create_chemical_reaction(
        id="CR003",
        title="Fisher-Tropsch Synthesis Reaction",
        description="Fisher-Tropsch synthesis reaction converting syngas to hydrocarbons",
        starting_materials=[create_starting_material(
            id="SM004",
            chemical_entity=create_chemical_entity(
                id="CHEBI:17863",
                inchi="InChI=1S/CH4/h1H4",
                inchikey="QVJZQZQZQZQZQZ-QVJZQZQZSA-N",
                smiles="C",
                molecular_formula="CH4",
                iupac_name="methane"
            ),
            mass=10.0,
            volume=10.0,
            temperature=298.15,
            pressure=1.0,
            physical_state=PhysicalStateEnum.GASEOUS
        )],
        reagents=[create_reagent(
            id="R003",
            chemical_entity=create_chemical_entity(
                id="CHEBI:17864",
                inchi="InChI=1S/CO/c1-2",
                inchikey="QVJZQZQZQZQZQZ-QVJZQZQZSA-N",
                smiles="C#O",
                molecular_formula="CO",
                iupac_name="carbon monoxide"
            ),
            mass=20.0,
            volume=20.0,
            temperature=298.15,
            pressure=1.0,
            physical_state=PhysicalStateEnum.GASEOUS
        )],
        products=[create_chemical_product(
            id="CP003",
            chemical_entity=create_chemical_entity(
                id="CHEBI:17865",
                inchi="InChI=1S/C2H6/c1-2/h1-2H3",
                inchikey="QVJZQZQZQZQZQZ-QVJZQZQZSA-N",
                smiles="CC",
                molecular_formula="C2H6",
                iupac_name="ethane"
            ),
            mass=15.0,
            volume=15.0,
            temperature=298.15,
            pressure=1.0,
            physical_state=PhysicalStateEnum.LIQUID
        )],
        catalysts=[create_catalyst(
            id="CAT003",
            chemical_entity=create_chemical_entity(
                id="CHEBI:17866",
                inchi="InChI=1S/Fe/c1-2",
                inchikey="QVJZQZQZQZQZQZ-QVJZQZQZSA-N",
                smiles="[Fe]",
                molecular_formula="Fe",
                iupac_name="iron"
            ),
            mass=0.2,
            volume=0.2,
            temperature=298.15,
            pressure=1.0,
            physical_state=PhysicalStateEnum.SOLID
        )],
        solvents=[create_solvent(
            id="S003",
            chemical_entity=create_chemical_entity(
                id="CHEBI:17867",
                inchi="InChI=1S/C2H6O/c1-2-3/h1-3H3",
                inchikey="QVJZQZQZQZQZQZ-QVJZQZQZSA-N",
                smiles="CCO",
                molecular_formula="C2H6O",
                iupac_name="ethanol"
            ),
            volume=100.0,
            temperature=298.15,
            pressure=1.0,
            physical_state=PhysicalStateEnum.LIQUID
        )],
        reactors=[reactor1],
        temperature=400.0,
        pressure=20.0,
        duration="3 hours",
        yield_percentage=75.0,
        creator=researcher
    )
    
    # Create dataset for Fisher-Tropsch
    dataset5 = create_dataset_for_reaction(
        dataset_id="DS005",
        reaction=fisher_tropsch,
        creator=researcher,
        title="Dataset D5: Fisher-Tropsch Synthesis Reaction",
        description="Dataset D5: Fisher-Tropsch synthesis reaction converting syngas to hydrocarbons with iron catalyst",
        release_date=date(2023, 1, 5)
    )
    
    return [dataset1, dataset2, dataset3, dataset4, dataset5]