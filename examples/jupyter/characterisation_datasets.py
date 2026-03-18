"""
Module to generate example datasets for chemical characterisation using the Chem DCAT-AP LinkML data model.
"""

from chem_dcat_ap.datamodel.chem_dcat_ap_pydantic import (
    Dataset, ChemicalEntity, InChi, InChIKey, SMILES, MolecularFormula, IUPACName,
    Agent, AgenticEntity, DataGeneratingActivity, DataAnalysis, Distribution, 
    QualitativeAttribute, QuantitativeAttribute, PhysicalStateEnum,
    Device, Software, Plan, AnalysisSourceData, EvaluatedActivity, EvaluatedEntity, ChemicalReaction, 
    ChemicalProduct, StartingMaterial, Reagent, Catalyst, DissolvingSubstance
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


def create_device(
    id: str,
    title: str,
    description: str,
    manufacturer: str,
    model: str
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
        part_of=[]
    )
    return device


def create_software(
    id: str,
    title: str,
    version: str,
    description: str
) -> Software:
    """Create a Software with the provided properties."""
    software = Software(
        id=id,
        title=title,
        description=description,
        other_identifier=[],
        has_qualitative_attribute=[],
        has_quantitative_attribute=[],
        has_part=[],
        part_of=[]
    )
    return software


def create_plan(
    id: str,
    title: str,
    description: str,
    steps: List[str]
) -> Plan:
    """Create a Plan with the provided properties."""
    plan = Plan(
        title=title,
        description=description
    )
    return plan


def create_analysis_source_data(
    id: str,
    title: str,
    description: str,
    chemical_entity: ChemicalEntity,
    data_type: str
) -> AnalysisSourceData:
    """Create AnalysisSourceData with the provided properties."""
    source_data = AnalysisSourceData(
        id=id,
        title=title,
        description=description,
        # composed_of=[chemical_entity],
        was_generated_by=[]
    )
    return source_data


def create_characterization_activity(
    id: str,
    title: str,
    description: str,
    creator: Agent,
    device: Device,
    software: Software,
    plan: Plan,
    source_data: AnalysisSourceData,
    analysis_type: str,
    analysis_date: date
) -> DataAnalysis:
    """Create a DataAnalysis activity for characterisation."""
    agentic_entity = AgenticEntity(
        id = str(uuid.uuid4()),
        title=f"Title of AgenticEntity {title}",
        description=description
    )
    activity = DataAnalysis(
        id=id,
        title=[title],
        description=[description],
        carried_out_by=[agentic_entity],
        had_input_entity=[source_data],
        had_output_entity=[],
        realized_plan=plan,
        occurred_in=None,
        has_part=[],
        had_input_activity=[],
        has_qualitative_attribute=[],
        has_quantitative_attribute=[],
        part_of=[],
        type=None,
        rdf_type=None
    )
    return activity


def create_dataset_for_characterization(
    dataset_id: str,
    activity: DataAnalysis,
    creator: Agent,
    title: str,
    description: str,
    release_date: date = None,
    chemical_entity: Optional[ChemicalEntity] = None
) -> Dataset:
    """Create a Dataset for a characterisation activity."""
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
        is_about_activity=[is_about_activity]
    )
    return dataset


def generate_characterisation_datasets() -> List[Dataset]:
    """Generate example datasets for chemical characterisation."""
    # Create agents
    researcher = Agent(
        name=["Dr. John Doe"],
        type=None
    )
    
    # Create chemical entities
    substance1 = create_chemical_entity(
        id="SUBSTANCE001",
        inchi="InChI=1S/C6H6/c1-2-4-6-5-3-1/h1-6H",
        inchikey="UHOVQNZJYSORNB-UHFFFAOYSA-N",
        smiles="c1ccccc1",
        molecular_formula="C6H6",
        iupac_name="benzene"
    )
    
    substance2 = create_chemical_entity(
        id="SUBSTANCE002",
        inchi="InChI=1S/C2H4O/c1-2-3/h1-3H",
        inchikey="QGZKDVFQNNGYKY-UHFFFAOYSA-N",
        smiles="CC=O",
        molecular_formula="C2H4O",
        iupac_name="acetaldehyde"
    )
    
    substance3 = create_chemical_entity(
        id="SUBSTANCE003",
        inchi="InChI=1S/C6H12O/c7-6-4-2-1-3-5-6/h1-5,7H2",
        inchikey="QVJZQZQZQZQZQZ-QVJZQZQZSA-N",
        smiles="C1CCCCC1O",
        molecular_formula="C6H12O",
        iupac_name="cyclohexanol"
    )
    
    # Create devices
    nmr_device = create_device(
        id="NMR001",
        title="Bruker AVANCE III HD 400 MHz",
        description="High-resolution NMR spectrometer",
        manufacturer="Bruker",
        model="AVANCE III HD 400 MHz"
    )
    
    ir_device = create_device(
        id="IR001",
        title="PerkinElmer Spectrum Two FT-IR",
        description="Fourier-transform infrared spectrometer",
        manufacturer="PerkinElmer",
        model="Spectrum Two FT-IR"
    )
    
    uvvis_device = create_device(
        id="UVVIS001",
        title="Shimadzu UV-3100",
        description="Ultraviolet-visible spectrophotometer",
        manufacturer="Shimadzu",
        model="UV-3100"
    )
    
    # Create software
    nmr_software = create_software(
        id="NMR_SOFTWARE001",
        title="TopSpin 4.1",
        version="4.1.0",
        description="Bruker NMR data processing software"
    )
    
    ir_software = create_software(
        id="IR_SOFTWARE001",
        title="Omega 3.0",
        version="3.0.0",
        description="PerkinElmer IR data processing software"
    )
    
    uvvis_software = create_software(
        id="UVVIS_SOFTWARE001",
        title="UV Probe 2.0",
        version="2.0.0",
        description="Shimadzu UV-Vis data processing software"
    )
    
    # Create plans
    nmr_plan = create_plan(
        id="NMR_PLAN001",
        title="NMR Spectroscopy Protocol",
        description="Standard protocol for 1H and 13C NMR spectroscopy",
        steps=[
            "Sample preparation",
            "Instrument calibration",
            "Data acquisition",
            "Data processing"
        ]
    )
    
    ir_plan = create_plan(
        id="IR_PLAN001",
        title="FT-IR Spectroscopy Protocol",
        description="Standard protocol for Fourier-transform infrared spectroscopy",
        steps=[
            "Sample preparation",
            "Instrument calibration",
            "Data acquisition",
            "Data processing"
        ]
    )
    
    uvvis_plan = create_plan(
        id="UVVIS_PLAN001",
        title="UV-Vis Spectroscopy Protocol",
        description="Standard protocol for ultraviolet-visible spectroscopy",
        steps=[
            "Sample preparation",
            "Instrument calibration",
            "Data acquisition",
            "Data processing"
        ]
    )
    
    # Create analysis source data
    source_data1 = create_analysis_source_data(
        id="SOURCE001",
        title="Benzene Sample",
        description="Pure benzene sample for characterisation",
        chemical_entity=substance1,
        data_type="chemical_sample"
    )
    
    source_data2 = create_analysis_source_data(
        id="SOURCE002",
        title="Acetaldehyde Sample",
        description="Pure acetaldehyde sample for characterisation",
        chemical_entity=substance2,
        data_type="chemical_sample"
    )
    
    source_data3 = create_analysis_source_data(
        id="SOURCE003",
        title="Cyclohexanol Sample",
        description="Pure cyclohexanol sample for characterisation",
        chemical_entity=substance3,
        data_type="chemical_sample"
    )
    
    # Create characterisation activities
    nmr_activity1 = create_characterization_activity(
        id="NMR_ACTIVITY001",
        title="NMR Spectroscopy of Benzene",
        description="1H and 13C NMR spectroscopy of benzene sample",
        creator=researcher,
        device=nmr_device,
        software=nmr_software,
        plan=nmr_plan,
        source_data=source_data1,
        analysis_type="NMR",
        analysis_date=date(2023, 2, 1)
    )
    
    ir_activity1 = create_characterization_activity(
        id="IR_ACTIVITY001",
        title="FT-IR Spectroscopy of Benzene",
        description="FT-IR spectroscopy of benzene sample",
        creator=researcher,
        device=ir_device,
        software=ir_software,
        plan=ir_plan,
        source_data=source_data1,
        analysis_type="FT-IR",
        analysis_date=date(2023, 2, 2)
    )
    
    uvvis_activity1 = create_characterization_activity(
        id="UVVIS_ACTIVITY001",
        title="UV-Vis Spectroscopy of Benzene",
        description="UV-Vis spectroscopy of benzene sample",
        creator=researcher,
        device=uvvis_device,
        software=uvvis_software,
        plan=uvvis_plan,
        source_data=source_data1,
        analysis_type="UV-Vis",
        analysis_date=date(2023, 2, 3)
    )
    
    # Create datasets for characterisation
    dataset1 = create_dataset_for_characterization(
        dataset_id="CHAR_DS001",
        activity=nmr_activity1,
        creator=researcher,
        title="Dataset D1: NMR Spectroscopy of Benzene",
        description="Dataset D1: 1H and 13C NMR spectroscopy of benzene sample",
        release_date=date(2023, 2, 1),
        chemical_entity=substance1
    )
    
    dataset2 = create_dataset_for_characterization(
        dataset_id="CHAR_DS002",
        activity=ir_activity1,
        creator=researcher,
        title="Dataset D2: FT-IR Spectroscopy of Benzene",
        description="Dataset D2: FT-IR spectroscopy of benzene sample",
        release_date=date(2023, 2, 2),
        chemical_entity=substance1
    )
    
    dataset3 = create_dataset_for_characterization(
        dataset_id="CHAR_DS003",
        activity=uvvis_activity1,
        creator=researcher,
        title="Dataset D3: UV-Vis Spectroscopy of Benzene",
        description="Dataset D3: UV-Vis spectroscopy of benzene sample",
        release_date=date(2023, 2, 3),
        chemical_entity=substance1
    )
    
    # Create characterisation activities for second substance
    nmr_activity2 = create_characterization_activity(
        id="NMR_ACTIVITY002",
        title="NMR Spectroscopy of Acetaldehyde",
        description="1H and 13C NMR spectroscopy of acetaldehyde sample",
        creator=researcher,
        device=nmr_device,
        software=nmr_software,
        plan=nmr_plan,
        source_data=source_data2,
        analysis_type="NMR",
        analysis_date=date(2023, 2, 4)
    )
    
    ir_activity2 = create_characterization_activity(
        id="IR_ACTIVITY002",
        title="FT-IR Spectroscopy of Acetaldehyde",
        description="FT-IR spectroscopy of acetaldehyde sample",
        creator=researcher,
        device=ir_device,
        software=ir_software,
        plan=ir_plan,
        source_data=source_data2,
        analysis_type="FT-IR",
        analysis_date=date(2023, 2, 5)
    )
    
    uvvis_activity2 = create_characterization_activity(
        id="UVVIS_ACTIVITY002",
        title="UV-Vis Spectroscopy of Acetaldehyde",
        description="UV-Vis spectroscopy of acetaldehyde sample",
        creator=researcher,
        device=uvvis_device,
        software=uvvis_software,
        plan=uvvis_plan,
        source_data=source_data2,
        analysis_type="UV-Vis",
        analysis_date=date(2023, 2, 6)
    )
    
    # Create datasets for second substance
    dataset4 = create_dataset_for_characterization(
        dataset_id="CHAR_DS004",
        activity=nmr_activity2,
        creator=researcher,
        title="Dataset D4: NMR Spectroscopy of Acetaldehyde",
        description="Dataset D4: 1H and 13C NMR spectroscopy of acetaldehyde sample",
        release_date=date(2023, 2, 4),
        chemical_entity=substance2
    )
    
    dataset5 = create_dataset_for_characterization(
        dataset_id="CHAR_DS005",
        activity=ir_activity2,
        creator=researcher,
        title="Dataset D5: FT-IR Spectroscopy of Acetaldehyde",
        description="Dataset D5: FT-IR spectroscopy of acetaldehyde sample",
        release_date=date(2023, 2, 5),
        chemical_entity=substance2
    )
    
    # Create datasets for third substance
    nmr_activity3 = create_characterization_activity(
        id="NMR_ACTIVITY003",
        title="NMR Spectroscopy of Cyclohexanol",
        description="1H and 13C NMR spectroscopy of cyclohexanol sample",
        creator=researcher,
        device=nmr_device,
        software=nmr_software,
        plan=nmr_plan,
        source_data=source_data3,
        analysis_type="NMR",
        analysis_date=date(2023, 2, 7)
    )
    
    ir_activity3 = create_characterization_activity(
        id="IR_ACTIVITY003",
        title="FT-IR Spectroscopy of Cyclohexanol",
        description="FT-IR spectroscopy of cyclohexanol sample",
        creator=researcher,
        device=ir_device,
        software=ir_software,
        plan=ir_plan,
        source_data=source_data3,
        analysis_type="FT-IR",
        analysis_date=date(2023, 2, 8)
    )
    
    uvvis_activity3 = create_characterization_activity(
        id="UVVIS_ACTIVITY003",
        title="UV-Vis Spectroscopy of Cyclohexanol",
        description="UV-Vis spectroscopy of cyclohexanol sample",
        creator=researcher,
        device=uvvis_device,
        software=uvvis_software,
        plan=uvvis_plan,
        source_data=source_data3,
        analysis_type="UV-Vis",
        analysis_date=date(2023, 2, 9)
    )
    
    # Create datasets for third substance
    dataset6 = create_dataset_for_characterization(
        dataset_id="CHAR_DS006",
        activity=nmr_activity3,
        creator=researcher,
        title="Dataset D6: NMR Spectroscopy of Cyclohexanol",
        description="Dataset D6: 1H and 13C NMR spectroscopy of cyclohexanol sample",
        release_date=date(2023, 2, 7),
        chemical_entity=substance3
    )
    
    dataset7 = create_dataset_for_characterization(
        dataset_id="CHAR_DS007",
        activity=ir_activity3,
        creator=researcher,
        title="Dataset D7: FT-IR Spectroscopy of Cyclohexanol",
        description="Dataset D7: FT-IR spectroscopy of cyclohexanol sample",
        release_date=date(2023, 2, 8),
        chemical_entity=substance3
    )
    
    dataset8 = create_dataset_for_characterization(
        dataset_id="CHAR_DS008",
        activity=uvvis_activity3,
        creator=researcher,
        title="Dataset D8: UV-Vis Spectroscopy of Cyclohexanol",
        description="Dataset D8: UV-Vis spectroscopy of cyclohexanol sample",
        release_date=date(2023, 2, 9),
        chemical_entity=substance3
    )
    
    return [dataset1, dataset2, dataset3, dataset4, dataset5, dataset6, dataset7, dataset8]