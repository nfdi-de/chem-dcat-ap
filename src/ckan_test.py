from chem_dcat_ap import (AnalysisDataset,
                          AnalysisSourceData,
                          DataAnalysis,
                          Activity,
                          DefinedTerm,
                          Standard,
                          EvaluatedEntity,
                          QualitativeAttribute)
from linkml_runtime.dumpers import RDFLibDumper
from linkml_runtime.utils.schemaview import SchemaView


example_dataset = {
    'author': 'Yanagisawa, K., Kaneko, K., Ikeda, H., Iwata, S., Muranaka, A., Koshino, H., Nagao, N., Watari, S., Nishimura, S., Shinzato, N., Onaka, H., Kakeya, H.',
    'author_email': None,
    'creator_user_id': '8a5c874c-b5ab-4df4-87d3-dfdc40fe20f6',
    'doi': '10.57992/nmrxiv.p85.s729.d3596',
    'exactmass': '',
    'id': 'nmrxiv-d3596',
    'inchi': 'InChI=1S/C21H23NO7/c1-9(2)3-4-14-16-10(5-11(29-14)7-15(24)25)6-12-17(21(16)28)19(26)13(8-23)18(22)20(12)27/h6,8-9,11,14,28H,3-5,7,22H2,1-2H3,(H,24,25)/t11-,14-/m0/s1',
    'inchi_key': 'NPGKFFQPHSMESG-FZMZJTMJSA-N',
    'isopen': False,
    'iupacName': '',
    'language': 'english',
    'license_id': 'CC BY-NC 4.0 Deed',
    'license_title': 'Attribution-NonCommercial 4.0 International',
    'license_url': 'https://creativecommons.org/licenses/by-nc/4.0/legalcode',
    'maintainer': '',
    'maintainer_email': None,
    'measurement_technique': 'heteronuclear single quantum coherence',
    'measurement_technique_iri': 'CHMO:0000604',
    'metadata_created': '2025-02-03T14:35:36.229612',
    'metadata_modified': '2025-03-07T09:58:42.738120',
    'mol_formula': '',
    'name': 'actinoquinonal_a_nmr_data-hsqc',
    'notes': 'This dataset contains NMR spectra obtained for the sample -actinoquinonal_A_NMR_Data date: 2021-10-02T04:26:18.000Z isFt: true name: actinoquinonal_A_NMR_Data/0 phc0: 0,0 phc1: 0,0 type: NMR Spectrum DECIM: 16 aqMod: 3 isFid: false tdOff: 0,0 title: Parameter file, TOPSPIN\t\tVersion 2.1 DSPFVS: 12 nucleus: 1H,1H reverse: false,false solvent: CDCl3 dimension: 2 increment: 10.01513082882905 isComplex: false probeName: 5 mm TXI D/1H-13C/15N XYZ-GRD Z8323/141 experiment: cosy groupDelay: -1 temperature: 298 spectrumSize: 1024,1024 baseFrequency: 600.05,600.05 fieldStrength: 14.093131413328843 numberOfScans: 256 pulseSequence: cosygpqf spectralWidth: 20.0302616576581,20 numberOfPoints: 3 relaxationTime: 1.5 acquisitionTime: 0.0000832000000000001 frequencyOffset: 3607.619024023734,3607.619024023734 originFrequency: 600.053607619024,600.053607619024 pulseStrength90: 25000 experimentNumber: 0 acquisitionScheme: notPhaseSensitive linearPredictionBin: 0,256 lpNumberOfCoefficients: 0,32 windowMultiplicationMode: 3,3 date: 2021-10-03T09:12:33.000Z isFt: true name: actinoquinonal_A_NMR_Data/0 phc0: 0,0 phc1: 0,0 type: NMR Spectrum DECIM: 16 aqMod: 3 isFid: false tdOff: 0,0 title: Parameter file, TOPSPIN\t\tVersion 2.1 DSPFVS: 12 nucleus: 1H,13C reverse: false,false solvent: CDCl3 dimension: 2 increment: 0.41729699776872503 isComplex: false probeName: 5 mm TXI D/1H-13C/15N XYZ-GRD Z8323/141 experiment: hmbc groupDelay: -1 temperature: 298 spectrumSize: 2048,1024 baseFrequency: 600.05,150.882693 fieldStrength: 14.093131413328843 numberOfScans: 256 pulseSequence: hmbcgplpndqf spectralWidth: 20.0302558928988,222.095059442626 numberOfPoints: 49 relaxationTime: 1.5 acquisitionTime: 0.0019968000000000013 frequencyOffset: 3780.3160000748903,16597.096230015042 originFrequency: 600.053780316,150.89929009623 pulseStrength90: 25000 experimentNumber: 0 acquisitionScheme: notPhaseSensitive linearPredictionBin: 0,256 lpNumberOfCoefficients: 0,32 windowMultiplicationMode: 3,3 date: 2021-10-02T18:55:08.000Z isFt: true name: actinoquinonal_A_NMR_Data/0 phc0: -65.8161,0 phc1: 0,0 type: NMR Spectrum DECIM: 16 aqMod: 3 isFid: false tdOff: 0,0 title: Parameter file, TOPSPIN\t\tVersion 2.1 DSPFVS: 12 nucleus: 1H,13C reverse: false,false solvent: CDCl3 dimension: 2 increment: 5.007565475493225 isComplex: false probeName: 5 mm TXI D/1H-13C/15N XYZ-GRD Z8323/141 experiment: hsqc groupDelay: -1 temperature: 298 spectrumSize: 1024,1024 baseFrequency: 600.05,150.882693 fieldStrength: 14.093131413328843 numberOfScans: 128 pulseSequence: hsqcetgpsi2 spectralWidth: 20.0302619019729,220 numberOfPoints: 5 relaxationTime: 1.5 acquisitionTime: 0.00016640000000000006 frequencyOffset: 3600.300000016432,16597.096230015042 originFrequency: 600.0536003,150.89929009623 pulseStrength90: 25000 experimentNumber: 0 acquisitionScheme: Echo-antiecho linearPredictionBin: 0,512 lpNumberOfCoefficients: 0,32 windowMultiplicationMode: 4,4 date: 2021-12-23T09:41:36.000Z isFt: true name: actinoquinonal_A_NMR_Data/0 phc0: -162.15,90 phc1: 0,-180 type: NMR Spectrum DECIM: 16 aqMod: 3 isFid: false tdOff: 0,0 title: Parameter file, TOPSPIN\t\tVersion 2.1 DSPFVS: 12 nucleus: 1H,1H reverse: false,false solvent: CDCl3 dimension: 2 increment: 4.00605238039458 isComplex: false probeName: 5 mm TXI D/1H-13C/15N XYZ-GRD Z8323/141 experiment: noesy groupDelay: -1 temperature: 298 spectrumSize: 1024,1024 baseFrequency: 600.05,600.05 fieldStrength: 14.093131413328843 numberOfScans: 64 pulseSequence: noesyphpp spectralWidth: 20.0302619019729,20 numberOfPoints: 6 relaxationTime: 2 acquisitionTime: 0.0002080000000000001 frequencyOffset: 3600.300000016432,3600.300000016432 originFrequency: 600.0536003,600.0536003 pulseStrength90: 25000 experimentNumber: 0 acquisitionScheme: States-TPPI linearPredictionBin: 0,0 lpNumberOfCoefficients: 0,0 windowMultiplicationMode: 4,4 date: {"year":2021,"month":10,"day":23} isFt: true name: actinoquinonal_A_13C.jdf type: NMR SPECTRUM isFid: false title: title: Parameter file, TOPSPIN\t\tVersion 2.1 / comment: Parameter file, TOPSPIN\t\tVersion 2.1 / author:nmr / site: author: nmr nucleus: 13C solvent: CHLOROFORM-D metadata: [object Object] dimension: 1 isComplex: true probeName: null experiment: 1d temperature: 298 baseFrequency: 150.91875159839753 fieldStrength: 14.093496686836302 numberOfScans: 25600 pulseSequence: zgpg30 spectralWidth: null numberOfPoints: 32768 relaxationTime: NA acquisitionMode: 0 acquisitionTime: NA frequencyOffset: null originFrequency: null pulseStrength90: null spectralWidthClipped: null date: {"year":2021,"month":5,"day":13} isFt: false name: actinoquinonal_A_1H.jdf type: NMR SPECTRUM isFid: true title: title: 210515 1 / comment: single_pulse / author:delta / site: JNM-ECS400 author: delta nucleus: 1H solvent: CHLOROFORM-D metadata: [object Object] dimension: 1 isComplex: true probeName: 2772 experiment: 1d sampleName: 2105151 temperature: 292.54999999999995 baseFrequency: 399.79256015247455 digitalFilter: 19.686298370361328 fieldStrength: 9.389766 numberOfScans: 16 pulseSequence: proton.jxp spectralWidth: 23.75913755462968 numberOfPoints: 16384 relaxationTime: 5 acquisitionMode: 0 acquisitionTime: 1.7249075200000001 frequencyOffset: 1998.9628007623728 originFrequency: 399.78219837825003 pulseStrength90: 39682.53968253968 spectralWidthClipped: 19006817.414588254',
    'num_resources': 1,
    'num_tags': 1,
    'organization': {'id': '0170ebc4-b55a-47a9-96b2-9981cef2ac7e',
                     'name': 'nhs-wirral-ccg',
                     'title': 'NHS Wirral CCG',
                     'type': 'repository',
                     'description': '',
                     'image_url': '',
                     'created': '2021-11-22T10:59:13.904545',
                     'is_organization': True,
                     'approval_status': 'approved',
                     'state': 'active'},
    'owner_org': '0170ebc4-b55a-47a9-96b2-9981cef2ac7e',
    'private': False,
    'related_molecule': [],
    'smiles': 'CC(C)CC[C@@H]1O[C@H](CC(=O)O)CC2=CC3=C(C(=O)C(C=O)=C(N)C3=O)C(O)=C21',
    'state': 'active',
    'title': 'actinoquinonal_A_NMR_Data.hsqc',
    'type': 'dataset',
    'url': 'https://nmrxiv.org/D3596',
    'version': '',
    'extras': [
        {'key': 'license_url',
         'value': 'https://creativecommons.org/licenses/by-nc/4.0/legalcode'},
        {'key': 'harvest_object_id',
         'value': '287f82dc-5804-438d-b2e2-798e43cbf517'},
        {'key': 'harvest_source_id',
         'value': 'b11775da-a6bc-45c1-bb4c-f71a5890d34b'},
        {'key': 'harvest_source_title',
         'value': 'nmrXiv'}
    ],
    'resources': [
        {'cache_last_updated': None,
         'cache_url': None,
         'created': '2025-02-03T14:35:36.232125',
         'format': 'HTML',
         'hash': '',
         'id': '2c48d6cc-2af2-4448-a8f8-90881a49c6d1',
         'last_modified': None,
         'metadata_modified': '2025-02-03T14:35:36.225126',
         'mimetype': None,
         'mimetype_inner': None,
         'name': 'actinoquinonal_A_NMR_Data.hsqc',
         'package_id': 'nmrxiv-d3596',
         'position': 0,
         'resource_type': 'HTML',
         'size': None,
         'state': 'active',
         'url': 'https://nmrxiv.org/D3596',
         'url_type': None,
         'tracking_summary': {'total': 0, 'recent': 0},
         'has_views': False}
    ],
    'tags': [
        {'display_name': 'heteronuclear-single-quantum-coherence',
         'id': 'f769ca74-abeb-472d-a347-15d945c46e11',
         'name': 'heteronuclear-single-quantum-coherence',
         'state': 'active',
         'vocabulary_id': None}
    ],
    'variableMeasured': [
        {'variableMeasured_name': 'NMR solvent',
         'variableMeasured_propertyID': 'NMR:1000330',
         'variableMeasured_tsurl': '',
         'variableMeasured_value': 'CDCl3'},
        {'variableMeasured_name': 'acquisition nucleus',
         'variableMeasured_propertyID': 'NMR:1400083',
         'variableMeasured_tsurl': '',
         'variableMeasured_value': "['1H','13C']"},
        {'variableMeasured_name': 'number of data points',
         'variableMeasured_propertyID': 'NMR:1000176',
         'variableMeasured_tsurl': '',
         'variableMeasured_value': '5'},
        {'variableMeasured_name': 'relaxation time measurement',
         'variableMeasured_propertyID': 'FIX:0000202',
         'variableMeasured_tsurl': 'http://purl.obolibrary.org/obo/FIX_0000202',
         'variableMeasured_value': '1.5'},
        {'variableMeasured_name': 'NMR spectrum by dimensionality',
         'variableMeasured_propertyID': 'NMR:1000117',
         'variableMeasured_tsurl': '',
         'variableMeasured_value': '2'},
        {'variableMeasured_name': 'NMR probe',
         'variableMeasured_propertyID': 'OBI:0000516',
         'variableMeasured_tsurl': 'http://purl.obolibrary.org/obo/OBI_0000516',
         'variableMeasured_value': '5 mm TXI D/1H-13C/15N XYZ-GRD Z8323/141'},
        {'variableMeasured_name': 'Temperature',
         'variableMeasured_propertyID': 'NCIT:C25206',
         'variableMeasured_tsurl': 'http://purl.obolibrary.org/obo/NCIT_C25206',
         'variableMeasured_value': '298'},
        {'variableMeasured_name': 'irradiation frequency',
         'variableMeasured_propertyID': 'NMR:1400026',
         'variableMeasured_tsurl': '',
         'variableMeasured_value': '[600.05, 150.882693]'},
        {'variableMeasured_name': 'magnetic field strength',
         'variableMeasured_propertyID': 'MR:1400253',
         'variableMeasured_tsurl': '',
         'variableMeasured_value': '14.093131413328843'},
        {'variableMeasured_name': 'number of scans',
         'variableMeasured_propertyID': 'NMR:1400087',
         'variableMeasured_tsurl': '',
         'variableMeasured_value': '128'},
        {'variableMeasured_name': 'nuclear magnetic resonance pulse sequence',
         'variableMeasured_propertyID': 'CHMO:0001841',
         'variableMeasured_tsurl': 'http://purl.obolibrary.org/obo/CHMO_0001841',
         'variableMeasured_value': 'hsqcetgpsi2'},
        {'variableMeasured_name': 'Spectral Width',
         'variableMeasured_propertyID': 'NCIT:C156496',
         'variableMeasured_tsurl': 'http://purl.obolibrary.org/obo/NCIT_C156496',
         'variableMeasured_value': '[20.0302619019729, 220]'}
    ]
}

# TODO: Think about which namespaces shouldbe passed to the RDFLibDumper as prefix_map for those prefixes that are
#  not already part of the DCAT-AP schema YAMLs. Should probably just be a Python dict maintained in this profile.

def graph_from_dataset(dataset_dict):
    # Get the ID of the dataset
    if dataset_dict.get('doi'):
        dataset_uri = 'https://doi.org/' + dataset_dict.get('doi')
        # not a mandatory field, but makes sense to do this here as it's the same value as the node URI
        dataset_id = 'https://doi.org/'+ dataset_dict.get('doi')
    else:
        dataset_uri = dataset_dict.get('id').strip()
        dataset_id = dataset_dict.get('id').strip()

    # Instantiate the evaluated sample
    # TODO: We used a fake ID, as the real one is not within the example dataset, but might be in the source data.
    # TODO: Do we need different instantiation steps/conditions based on where the metadata comes from?
    sample = EvaluatedEntity(
        id=dataset_id + '/sample',
        has_qualitative_attribute=[
            QualitativeAttribute(
                rdf_type=DefinedTerm(
                    id='CHEMINF:000059',
                    title='InChiKey'),
                title='assigned InChiKey',
                value=dataset_dict.get('inchi_key')),
            QualitativeAttribute(
                rdf_type=DefinedTerm(
                    id='CHEMINF:000113',
                    title='InChi'),
                title='assigned InChi',
                value=dataset_dict.get('inchi')),
            QualitativeAttribute(
                rdf_type=DefinedTerm(
                    id='CHEMINF:000018',
                    title='SMILES'),
                title='assigned SMILES',
                value=dataset_dict.get('smiles')),
            QualitativeAttribute(
                rdf_type=DefinedTerm(
                    id='CHEMINF:000037',
                    title='IUPACChemicalFormula'),
                title='assigned IUPACChemicalFormula',
                value=dataset_dict.get('mol_formula'))
        ]
    )

    # Instantiate the measurement process/activity
    measurement = Activity(
        rdf_type=DefinedTerm(
            id=dataset_dict.get('measurement_technique_iri'),
            title=dataset_dict.get('measurement_technique')),
        evaluated_entity=[sample]
    )
    # TODO: add a condition to account for MassBank and other sources not providing this, where we could hardcode,
    #  like in the below Massbank example.
    # elif source == 'Massbank:
    #    measurement = DataCreatingActivity(
    #        rdf_type=DefinedTerm(
    #            id='CHMO:0000470',
    #            title='mass spectrometry,
    #        evaluated_entity=[sample]
    #    )

    # Instantiate the spectrum that was analysed by the measurement with a fake ID, as it does not have one,
    # but the ID is a mandatory slot for an AnalysisSourceData (which is a EvaluatedEntity)
    # Hardcode the rdf_type, as this is necessary in the domain agnostic version of our DCAT-AP extension
    spectrum = AnalysisSourceData(
        id=dataset_id + '/spectrum',
        rdf_type=DefinedTerm(id='CHMO:0000800',
                             title='spectrum'),
        was_generated_by=[measurement]
    )

    # Instantiate the analysis of the spectrum
    # Hardcode the rdf_type, as this is necessary in this domain agnostic version of our DCAT-AP extension
    analysis = DataAnalysis(
        rdf_type=DefinedTerm(
            id='http://purl.allotrope.org/ontologies/process#AFP_0003618',
            title='peak identification'),
        evaluated_entity=[spectrum])

    # Instantiate the dataset
    dataset = AnalysisDataset(id=dataset_uri,
                              title=dataset_dict.get('title'),
                              description=dataset_dict.get('notes'),
                              was_generated_by=analysis,
                              identifier=dataset_id,
                              describes_entity=dataset_id + '/sample',
                              # using nmrXiv docs just as a dummy example for how we could use this slot
                              # TODO: Use MICHI PURL once possible
                              conforms_to=Standard(
                                  identifier='https://docs.nmrxiv.org/submission-guides/data-model/spectra.html')
                              )

    #TODO: Instantiate the rest of the given dataset attributes, most importantly the measurement variables

    # Create an RDFLib graph using RDFLibDumper & SchemaView classes from the linkml package
    g = RDFLibDumper().as_rdf_graph(dataset, schemaview=SchemaView("chem_dcat_ap/schema/chem_dcat_ap.yaml", merge_imports=True))

    print(g.serialize(format='ttl'))

    return g

def main():
    graph_from_dataset(example_dataset)

if __name__ == '__main__':
    main()
