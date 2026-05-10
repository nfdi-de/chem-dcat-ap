"""
Module to generate example datasets for chemical reactions using the Chem DCAT-AP LinkML data model.
"""

from chem_dcat_ap.datamodel.chem_dcat_ap_pydantic import (
    Dataset,
    ChemicalEntity,
    InChi,
    InChIKey,
    SMILES,
    MolecularFormula,
    IUPACName,
    MolarMass,
    Entity,
    Agent,
    AgenticEntity,
    EvaluatedActivity,
    EvaluatedEntity,
    DataGeneratingActivity,
    DataAnalysis,
    Distribution,
    QualitativeAttribute,
    QuantitativeAttribute,
    PhysicalStateEnum,
    Device,
    Software,
    Plan,
    AnalysisSourceData,
    ChemicalReaction,
    StartingMaterial,
    ChemicalProduct,
    StartingMaterial,
    Reagent,
    Catalyst,
    DissolvingSubstance,
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
    iupac_name: Optional[str] = None,
) -> ChemicalEntity:
    """Create a ChemicalEntity with the provided properties."""
    entity = ChemicalEntity(
        id=id,
        inchi=[InChi(value=inchi)] if inchi else [],
        inchikey=[InChIKey(value=inchikey)] if inchikey else [],
        smiles=[SMILES(value=smiles)] if smiles else [],
        molecular_formula=[MolecularFormula(value=molecular_formula)]
        if molecular_formula
        else [],
        iupac_name=[IUPACName(value=iupac_name)] if iupac_name else [],
    )
    return entity


def create_device(
    id: str, title: str, description: str, manufacturer: str, model: str
) -> Device:
    """Create a Device with the provided properties."""
    device = Device(
        id=id,
        title=title,
        description=description,
        other_identifier=[],
        has_qualitative_attribute=[],
        has_quantitative_attribute=[],
        has_part=[],
        part_of=[],
    )
    return device


def create_software(id: str, title: str, version: str, description: str) -> Software:
    """Create a Software with the provided properties."""
    software = Software(
        id=id,
        title=title,
        description=description,
        other_identifier=[],
        has_qualitative_attribute=[],
        has_quantitative_attribute=[],
        has_part=[],
        part_of=[],
    )
    return software


def create_plan(name: str, title: str, description: str, steps: List[str]) -> Plan:
    """Create a Plan with the provided properties."""
    plan = Plan(title=title, description=description)
    return plan


def create_analysis_source_data(
    id: str,
    title: str,
    description: str,
    chemical_entity: ChemicalEntity,
    data_type: str,
) -> AnalysisSourceData:
    """Create AnalysisSourceData with the provided properties."""
    source_data = AnalysisSourceData(
        id=id,
        title=title,
        description=description,
        composed_of=[chemical_entity],
        was_generated_by=[],
    )
    return source_data


def create_reaction_activity(
    id: str,
    title: str,
    description: str,
    creator: Agent,
    device: Device,
    software: Software,
    plan: Plan,
    reaction: ChemicalReaction,
    reaction_date: date,
) -> DataGeneratingActivity:
    """Create a DataGeneratingActivity for a chemical reaction."""

    researcher_assistant = AgenticEntity(
        title=f"Research Assistant for {title}", id=str(uuid.uuid4()), type=None
    )
    output_entity = Entity( 
        id=str(uuid.uuid4()),
        title=f"Output of {title}",
        description=f"Output entity generated from the reaction activity {title}",
    )

    activity = DataGeneratingActivity(
        id=id,
        title=[title],
        description=[description],
        carried_out_by=[researcher_assistant],
        had_input_entity=[],
        had_output_entity=[output_entity],
        realized_plan=plan,
        occurred_in=None,
        has_part=[],
        had_input_activity=[],
        has_qualitative_attribute=[],
        has_quantitative_attribute=[],
        part_of=[],
        type=None,
        rdf_type=None,
    )
    return activity


def create_dataset_for_reaction(
    dataset_id: str,
    activity: DataGeneratingActivity,
    creator: Agent,
    title: str,
    description: str,
    release_date: date = None,
    reaction: Optional[ChemicalReaction] = None,
) -> Dataset:
    """Create a Dataset for a chemical reaction activity."""
    is_about_entity = EvaluatedEntity(
        title=f"Evaluated entity for {title}", id=str(uuid.uuid4()), type=None
    )
    # !!! inconsistency - list / str in title - need to check the data model
    is_about_activity = EvaluatedActivity(
        title=[f"Evaluated activity for {title}"], id=str(uuid.uuid4()), type=None
    )

    dataset = Dataset(
        id=dataset_id,
        title=[title],
        description=[description],
        was_generated_by=[activity],
        creator=[creator],
        release_date=release_date,
        is_about_entity=[is_about_entity],
        is_about_activity=[is_about_activity],
    )
    return dataset


def generate_reaction_datasets() -> List[Dataset]:
    """Generate example datasets for chemical reactions."""
    # Create agents
    researcher = Agent(name=["Dr. Jane Smith"], type=None)

    # Create chemical entities for reactions
    # Reaction 1: Aldol Condensation
    benzaldehyde = create_chemical_entity(
        id="REACTANT001",
        inchi="InChI=1S/C7H6O/c8-6-4-2-1-3-5-6/h1-7H",
        inchikey="VWWQXPODVHRPQS-UHFFFAOYSA-N",
        smiles="c1ccccc1C=O",
        molecular_formula="C7H6O",
        iupac_name="benzaldehyde",
    )

    acetone = create_chemical_entity(
        id="REACTANT002",
        inchi="InChI=1S/C3H6O/c1-3(2)4/h1-4H3",
        inchikey="KFZMGEQVEWPINO-UHFFFAOYSA-N",
        smiles="CC(C)=O",
        molecular_formula="C3H6O",
        iupac_name="acetone",
    )
    benzoin = create_chemical_entity(
        id="PRODUCT001",
        inchi="InChI=1S/C14H12O/c1-2-4-10-14(10)12-6-8-13(13)11-5-7-12/h1-14H",
        inchikey="QVJZQZQZQZQZQZ-QVJZQZQZSA-N",
        smiles="c1ccccc1C(c2ccccc2)c3ccccc3",
        molecular_formula="C14H12O",
        iupac_name="benzoin",
    )
    phenylalanine = create_chemical_entity(
        id="PRODUCT002",
        inchi="InChI=1S/C9H11NO2/c10-8(11)12-9-5-3-1-2-4-9/h1-9H,10H2,(H,11,12)",
        inchikey="QVJZQZQZQZQZQZ-QVJZQZQZSA-N",
        smiles="N[C@@H](Cc1ccccc1)C(=O)O",
        molecular_formula="C9H11NO2",
        iupac_name="phenylalanine",
    )
    decane = create_chemical_entity(
        id="PRODUCT003",
        inchi="InChI=1S/C10H22/c1-3-5-7-9-10-8-6-4-2/h3-10H2,1-2H3",
        inchikey="QVJZQZQZQZQZQZ-QVJZQZQZSA-N",
        smiles="CCCCCCCCC",
        molecular_formula="C10H22",
        iupac_name="decane",
    )

    # Reaction 2: Transamination
    glutamate = create_chemical_entity(
        id="REACTANT003",
        inchi="InChI=1S/C5H9NO4/c6-2(1-5(9)10)3-4(7)8/h2-4,6H,1H2,(H,9,10)(H,7,8)/t2-/m0/s1",
        inchikey="QVJZQZQZQZQZQZ-QVJZQZQZSA-N",
        smiles="N[C@@H](CO)C(=O)O",
        molecular_formula="C5H9NO4",
        iupac_name="glutamic acid",
    )

    alpha_ketoglutarate = create_chemical_entity(
        id="REACTANT004",
        inchi="InChI=1S/C5H6O5/c6-2(1-5(9)10)3-4(7)8/h2-4,6H,1H2,(H,9,10)(H,7,8)/t2-/m0/s1",
        inchikey="QVJZQZQZQZQZQZ-QVJZQZQZSA-N",
        smiles="C[C@@H](C(=O)O)C(=O)O",
        molecular_formula="C5H6O5",
        iupac_name="alpha-ketoglutaric acid",
    )

    phenylalanine_product = ChemicalProduct(
        id="PRODUCT002", composed_of=[phenylalanine]
    )

    # Reaction 3: Fischer-Tropsch Synthesis
    carbon_monoxide = create_chemical_entity(
        id="REACTANT005",
        inchi="InChI=1S/CO/c1-2",
        inchikey="VNWKTOKETHGBQD-UHFFFAOYSA-N",
        smiles="CO",
        molecular_formula="CO",
        iupac_name="carbon monoxide",
    )

    hydrogen = create_chemical_entity(
        id="REACTANT006",
        inchi="InChI=1S/H2/h1H",
        inchikey="UFHFLXCUPAHTMO-UHFFFAOYSA-N",
        smiles="H2",
        molecular_formula="H2",
        iupac_name="hydrogen",
    )

    benzaldehyde_starting_material = StartingMaterial(
        id="STARTING_MATERIAL001", composed_of=[benzaldehyde]
    )

    acetone_starting_material = StartingMaterial(
        id="STARTING_MATERIAL002", composed_of=[acetone]
    )

    glutamate_starting_material = StartingMaterial(
        id="STARTING_MATERIAL003", composed_of=[glutamate]
    )

    alpha_ketoglutarate_starting_material = StartingMaterial(
        id="STARTING_MATERIAL004", composed_of=[alpha_ketoglutarate]
    )

    carbon_monoxide_starting_material = StartingMaterial(
        id="STARTING_MATERIAL005", composed_of=[carbon_monoxide]
    )
    hydrogen_starting_material = StartingMaterial(
        id="STARTING_MATERIAL006", composed_of=[hydrogen]
    )

    # add all reagents here:

    carbon_monoxide_reagent = Reagent(id="REAGENT001", composed_of=[carbon_monoxide])

    hydrogen_reagent = Reagent(id="REAGENT002", composed_of=[hydrogen])

    decane_product = ChemicalProduct(id="PRODUCT003", composed_of=[decane])

    benzoin_product = ChemicalProduct(
        composed_of=[benzoin],
        id="PRODUCT001",
    )

    # Create devices
    reactor_device = create_device(
        id="REACTOR001",
        title="Laboratory Reactor",
        description="Glass reactor with heating mantle and magnetic stirrer",
        manufacturer="Schlenk",
        model="SR-2000",
    )

    # Create software
    reaction_software = create_software(
        id="REACTION_SOFTWARE001",
        title="ChemDraw Pro",
        version="18.0",
        description="Chemical structure drawing software",
    )

    # Create plans
    reaction_plan = create_plan(
        name="REACTION_PLAN001",
        title="Chemical Reaction Protocol",
        description="Standard protocol for conducting chemical reactions",
        steps=[
            "Reactant preparation",
            "Reaction setup",
            "Reaction monitoring",
            "Product isolation",
            "Product characterization",
        ],
    )

    # Create chemical reactions
    aldol_condensation = ChemicalReaction(
        id="REACTION001",
        title=["Aldol Condensation"],
        description=["Aldol condensation between benzaldehyde and acetone"],
        used_reactant=[],
        used_catalyst=[],
        used_solvent=[],
        used_starting_material=[
            benzaldehyde_starting_material,
            acetone_starting_material,
        ],
        generated_product=[benzoin_product],
        has_part=[],
        part_of=[],
        type=None,
        rdf_type=None,
    )

    transamination = ChemicalReaction(
        id="REACTION002",
        title=["Transamination"],
        description=[
            "Transamination reaction between glutamate and alpha-ketoglutarate"
        ],
        used_reactant=[],
        used_catalyst=[],
        used_solvent=[],
        used_starting_material=[
            glutamate_starting_material,
            alpha_ketoglutarate_starting_material,
        ],
        generated_product=[phenylalanine_product],
        has_part=[],
        part_of=[],
        type=None,
        rdf_type=None,
    )

    fischer_tropsch = ChemicalReaction(
        id="REACTION003",
        title=["Fischer-Tropsch Synthesis"],
        description=["Fischer-Tropsch synthesis of hydrocarbons from CO and H2"],
        used_reactant=[carbon_monoxide_reagent, hydrogen_reagent],
        used_catalyst=[],
        used_solvent=[],
        used_starting_material=[
            carbon_monoxide_starting_material,
            hydrogen_starting_material,
        ],
        generated_product=[decane_product],
        has_part=[],
        part_of=[],
        type=None,
        rdf_type=None,
    )

    # Create reaction activities (replicates)
    # Aldol Condensation - Replicate 1
    reaction_activity1 = create_reaction_activity(
        id="REACTION_ACTIVITY001",
        title="Aldol Condensation - Replicate 1",
        description="First replicate of aldol condensation reaction",
        creator=researcher,
        device=reactor_device,
        software=reaction_software,
        plan=reaction_plan,
        reaction=aldol_condensation,
        reaction_date=date(2023, 1, 1),
    )

    # Aldol Condensation - Replicate 2
    reaction_activity2 = create_reaction_activity(
        id="REACTION_ACTIVITY002",
        title="Aldol Condensation - Replicate 2",
        description="Second replicate of aldol condensation reaction",
        creator=researcher,
        device=reactor_device,
        software=reaction_software,
        plan=reaction_plan,
        reaction=aldol_condensation,
        reaction_date=date(2023, 1, 2),
    )

    # Aldol Condensation - Replicate 3
    reaction_activity3 = create_reaction_activity(
        id="REACTION_ACTIVITY003",
        title="Aldol Condensation - Replicate 3",
        description="Third replicate of aldol condensation reaction",
        creator=researcher,
        device=reactor_device,
        software=reaction_software,
        plan=reaction_plan,
        reaction=aldol_condensation,
        reaction_date=date(2023, 1, 3),
    )

    # Transamination - Replicate 1
    reaction_activity4 = create_reaction_activity(
        id="REACTION_ACTIVITY004",
        title="Transamination - Replicate 1",
        description="First replicate of transamination reaction",
        creator=researcher,
        device=reactor_device,
        software=reaction_software,
        plan=reaction_plan,
        reaction=transamination,
        reaction_date=date(2023, 1, 4),
    )

    # Transamination - Replicate 2
    reaction_activity5 = create_reaction_activity(
        id="REACTION_ACTIVITY005",
        title="Transamination - Replicate 2",
        description="Second replicate of transamination reaction",
        creator=researcher,
        device=reactor_device,
        software=reaction_software,
        plan=reaction_plan,
        reaction=transamination,
        reaction_date=date(2023, 1, 5),
    )

    # Transamination - Replicate 3
    reaction_activity6 = create_reaction_activity(
        id="REACTION_ACTIVITY006",
        title="Transamination - Replicate 3",
        description="Third replicate of transamination reaction",
        creator=researcher,
        device=reactor_device,
        software=reaction_software,
        plan=reaction_plan,
        reaction=transamination,
        reaction_date=date(2023, 1, 6),
    )

    # Fischer-Tropsch - Replicate 1
    reaction_activity7 = create_reaction_activity(
        id="REACTION_ACTIVITY007",
        title="Fischer-Tropsch Synthesis - Replicate 1",
        description="First replicate of Fischer-Tropsch synthesis reaction",
        creator=researcher,
        device=reactor_device,
        software=reaction_software,
        plan=reaction_plan,
        reaction=fischer_tropsch,
        reaction_date=date(2023, 1, 7),
    )

    # Fischer-Tropsch - Replicate 2
    reaction_activity8 = create_reaction_activity(
        id="REACTION_ACTIVITY008",
        title="Fischer-Tropsch Synthesis - Replicate 2",
        description="Second replicate of Fischer-Tropsch synthesis reaction",
        creator=researcher,
        device=reactor_device,
        software=reaction_software,
        plan=reaction_plan,
        reaction=fischer_tropsch,
        reaction_date=date(2023, 1, 8),
    )

    # Fischer-Tropsch - Replicate 3
    reaction_activity9 = create_reaction_activity(
        id="REACTION_ACTIVITY009",
        title="Fischer-Tropsch Synthesis - Replicate 3",
        description="Third replicate of Fischer-Tropsch synthesis reaction",
        creator=researcher,
        device=reactor_device,
        software=reaction_software,
        plan=reaction_plan,
        reaction=fischer_tropsch,
        reaction_date=date(2023, 1, 9),
    )

    # Create datasets for reactions
    dataset1 = create_dataset_for_reaction(
        dataset_id="REACTION_DS001",
        activity=reaction_activity1,
        creator=researcher,
        title="Dataset D1: Aldol Condensation - Replicate 1",
        description="Dataset D1: First replicate of aldol condensation reaction",
        release_date=date(2023, 1, 1),
        reaction=aldol_condensation,
    )

    dataset2 = create_dataset_for_reaction(
        dataset_id="REACTION_DS002",
        activity=reaction_activity2,
        creator=researcher,
        title="Dataset D2: Aldol Condensation - Replicate 2",
        description="Dataset D2: Second replicate of aldol condensation reaction",
        release_date=date(2023, 1, 2),
        reaction=aldol_condensation,
    )

    dataset3 = create_dataset_for_reaction(
        dataset_id="REACTION_DS003",
        activity=reaction_activity3,
        creator=researcher,
        title="Dataset D3: Aldol Condensation - Replicate 3",
        description="Dataset D3: Third replicate of aldol condensation reaction",
        release_date=date(2023, 1, 3),
        reaction=aldol_condensation,
    )

    dataset4 = create_dataset_for_reaction(
        dataset_id="REACTION_DS004",
        activity=reaction_activity4,
        creator=researcher,
        title="Dataset D4: Transamination - Replicate 1",
        description="Dataset D4: First replicate of transamination reaction",
        release_date=date(2023, 1, 4),
        reaction=transamination,
    )

    dataset5 = create_dataset_for_reaction(
        dataset_id="REACTION_DS005",
        activity=reaction_activity5,
        creator=researcher,
        title="Dataset D5: Transamination - Replicate 2",
        description="Dataset D5: Second replicate of transamination reaction",
        release_date=date(2023, 1, 5),
        reaction=transamination,
    )

    dataset6 = create_dataset_for_reaction(
        dataset_id="REACTION_DS006",
        activity=reaction_activity6,
        creator=researcher,
        title="Dataset D6: Transamination - Replicate 3",
        description="Dataset D6: Third replicate of transamination reaction",
        release_date=date(2023, 1, 6),
        reaction=transamination,
    )

    dataset7 = create_dataset_for_reaction(
        dataset_id="REACTION_DS007",
        activity=reaction_activity7,
        creator=researcher,
        title="Dataset D7: Fischer-Tropsch Synthesis - Replicate 1",
        description="Dataset D7: First replicate of Fischer-Tropsch synthesis reaction",
        release_date=date(2023, 1, 7),
        reaction=fischer_tropsch,
    )

    dataset8 = create_dataset_for_reaction(
        dataset_id="REACTION_DS008",
        activity=reaction_activity8,
        creator=researcher,
        title="Dataset D8: Fischer-Tropsch Synthesis - Replicate 2",
        description="Dataset D8: Second replicate of Fischer-Tropsch synthesis reaction",
        release_date=date(2023, 1, 8),
        reaction=fischer_tropsch,
    )

    dataset9 = create_dataset_for_reaction(
        dataset_id="REACTION_DS009",
        activity=reaction_activity9,
        creator=researcher,
        title="Dataset D9: Fischer-Tropsch Synthesis - Replicate 3",
        description="Dataset D9: Third replicate of Fischer-Tropsch synthesis reaction",
        release_date=date(2023, 1, 9),
        reaction=fischer_tropsch,
    )

    return [
        dataset1,
        dataset2,
        dataset3,
        dataset4,
        dataset5,
        dataset6,
        dataset7,
        dataset8,
        dataset9,
    ]
